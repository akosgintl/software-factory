#!/usr/bin/env bash
# Machine setup for the warpdotdev-factory experiment (Linux / WSL2 with WSLg).
# Safe to run again: every step checks before it changes anything.
#
#   scripts/warp-setup.sh system   Warp apt repo + warp-terminal + oz (uses sudo)
#   scripts/warp-setup.sh user     Agent CLI, global skills, CLI-agent plugins, tab config
#   scripts/warp-setup.sh          both, then the manual steps
#
# Nothing here signs in, stores a key, or changes Warp settings: those are the
# manual steps printed at the end.

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
step() { printf '\n\033[1m== %s\033[0m\n' "$*"; }
ok() { printf '   ok: %s\n' "$*"; }
skip() { printf '   skip: %s\n' "$*"; }
have() { command -v "$1" >/dev/null 2>&1; }

prereqs() {
  step "Prerequisites"
  if [[ -n "${WAYLAND_DISPLAY:-}${DISPLAY:-}" ]]; then ok "WSLg display (${WAYLAND_DISPLAY:-$DISPLAY})"; else
    echo "   warning: no WAYLAND_DISPLAY/DISPLAY; the Warp app needs WSLg (wsl --update)"; fi
  local missing=()
  for c in git gh jq python3 curl node npx; do have "$c" && ok "$c" || missing+=("$c"); done
  if ((${#missing[@]})); then echo "   missing: ${missing[*]}"; fi
}

system() {
  step "Warp apt repository (sudo)"
  if [[ -f /etc/apt/sources.list.d/warpdotdev.list ]]; then skip "already configured"; else
    local tmp; tmp="$(mktemp -d)"
    curl -fsSL https://releases.warp.dev/linux/keys/warp.asc | gpg --dearmor > "$tmp/warpdotdev.gpg"
    sudo install -D -o root -g root -m 644 "$tmp/warpdotdev.gpg" /etc/apt/keyrings/warpdotdev.gpg
    echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/warpdotdev.gpg] https://releases.warp.dev/linux/deb stable main" \
      | sudo tee /etc/apt/sources.list.d/warpdotdev.list >/dev/null
    rm -rf "$tmp"
    ok "added releases.warp.dev"
  fi

  step "warp-terminal (the app) and oz (Oz CLI)"
  local pkgs=()
  dpkg -s warp-terminal >/dev/null 2>&1 && skip "warp-terminal installed" || pkgs+=(warp-terminal)
  dpkg -s oz-stable >/dev/null 2>&1 && skip "oz-stable installed" || pkgs+=(oz-stable)
  if ((${#pkgs[@]})); then
    sudo apt-get update -qq
    sudo apt-get install -y "${pkgs[@]}"
    ok "installed ${pkgs[*]}"
  fi
}

user() {
  step "Warp Agent CLI (warp)"
  if [[ -x "$HOME/.local/bin/warp" ]] || have warp; then skip "warp already installed ($(command -v warp || echo ~/.local/bin/warp))"; else
    # Reviewed installer: puts the binary under ~/.warp/tui and links ~/.local/bin/warp. No sudo.
    curl -fsSL https://app.warp.dev/download/agent-cli | bash
  fi

  step "Global skills without a license (kept out of the repo): factory-setup, oz"
  local tmp; tmp="$(mktemp -d)"
  install_global_skill "$tmp" warpdotdev/warp-factories-skills .agents/skills/factory-setup factory-setup
  install_global_skill "$tmp" warpdotdev/oz-agent-skill skills/oz oz
  rm -rf "$tmp"

  step "Warp integration for CLI agents found on this machine"
  if have claude; then
    if claude plugin list 2>/dev/null | grep -q 'warp@claude-code-warp'; then skip "claude: warp plugin installed"; else
      claude plugin marketplace add warpdotdev/claude-code-warp
      claude plugin install warp@claude-code-warp
      ok "claude: warp plugin"
    fi
  else skip "claude not installed"; fi
  if have codex; then
    if codex plugin list 2>/dev/null | grep -q 'warp@codex-warp.*installed'; then skip "codex: warp plugin installed"; else
      codex plugin marketplace add warpdotdev/codex-warp || true
      codex plugin add warp@codex-warp
      ok "codex: warp plugin"
    fi
  else skip "codex not installed"; fi
  if have opencode; then opencode_plugin; else skip "opencode not installed"; fi
  have gemini || skip "gemini not installed (warpdotdev/gemini-cli-warp)"

  step "Tab config 'Software factory'"
  local linked=0
  for dir in "$HOME/.warp/tab_configs" "${XDG_DATA_HOME:-$HOME/.local/share}/warp-terminal/tab_configs"; do
    [[ -d "$(dirname "$dir")" ]] || continue
    mkdir -p "$dir"
    ln -sfn "$REPO/warp/tab_configs/software-factory.toml" "$dir/software-factory.toml"
    ok "linked into $dir"; linked=1
  done
  ((linked)) || echo "   Warp has not created its data dir yet. Start warp-terminal once, then run: $0 user"

  step "Repo skills"
  python3 "$REPO/scripts/warp-skills.py" sync
  python3 "$REPO/scripts/warp-skills.py" check
}

# Copy one skill directory from a GitHub repo into ~/.agents/skills/<name>.
install_global_skill() {
  local tmp="$1" repo="$2" path="$3" name="$4" dest="$HOME/.agents/skills/$4"
  if [[ -f "$dest/SKILL.md" ]]; then skip "$name already in ~/.agents/skills"; return; fi
  git clone -q --depth 1 "https://github.com/$repo.git" "$tmp/$name"
  mkdir -p "$HOME/.agents/skills"
  cp -r "$tmp/$name/$path" "$dest"
  ok "$name -> $dest (from $repo@$(git -C "$tmp/$name" rev-parse --short HEAD))"
}

# Add the Warp plugin to opencode's config, keeping what is already there.
opencode_plugin() {
  local cfg="$HOME/.config/opencode/opencode.jsonc"
  [[ -f "$cfg" ]] || cfg="$HOME/.config/opencode/opencode.json"
  python3 -I - "$cfg" <<'EOF'
import json, os, sys
path, plugin = sys.argv[1], "@warp-dot-dev/opencode-warp"
data = {}
if os.path.exists(path):
    try:
        data = json.load(open(path))
    except json.JSONDecodeError:
        sys.exit(f"   manual: {path} has comments; add \"{plugin}\" to its \"plugin\" array")
if plugin in data.get("plugin", []):
    print(f"   skip: opencode: {plugin} already configured")
else:
    data.setdefault("plugin", []).append(plugin)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"   ok: opencode: added {plugin} to {path}")
EOF
}

manual() {
  step "Manual steps (Warp keeps these in your account or keychain)"
  cat <<'EOF'
 1. Start the app:            warp-terminal &
    Sign in (free account). Open this repo in it.
 2. Your own model key:       Settings -> search "API keys" -> Anthropic -> paste key.
    Pick an explicit Claude model, not Auto (Auto always uses Warp credits).
 3. Agent CLI key + login:    warp --set-provider-api-key anthropic   then run: warp
 4. Oz CLI login:             oz login    (check: oz whoami, oz model list)
 5. Profiles:                 create "Factory" and "Review (read-only)" as in warp/profiles.md
 6. Project MCP servers:      Settings -> Agents -> MCP servers -> enable github, playwright
    (project servers need this again after every Warp restart)
 7. Community workflows:      Settings -> Features -> Workflows -> show Global Workflows
 8. Drive objects (optional): vendor/warp-drive/do-things/IMPORT.md
 9. Check:                    /skills in an agent pane lists the repo skills, factory-setup and oz;
                              Ctrl+Shift+R lists the "Factory:" and "Skills:" workflows;
                              "+" -> "Software factory" opens the tab config.
    If /skills misses the vendored skills, Warp is not following the symlinks:
                              python3 scripts/warp-skills.py sync --copy
EOF
}

case "${1:-all}" in
  system) prereqs; system ;;
  user) prereqs; user ;;
  all) prereqs; system; user; manual ;;
  manual) manual ;;
  *) echo "usage: $0 [system|user|manual|all]" >&2; exit 2 ;;
esac
