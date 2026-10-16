---
enabled: false
triggers:
  - provider: github
    event: pull_request_merged
    filter:
      repos: [akosgintl/software-factory]
      labels: ["factory:SoftwareFactory"]
  - provider: github
    event: pull_request_closed
    filter:
      repos: [akosgintl/software-factory]
      labels: ["factory:SoftwareFactory"]
---
A factory-labeled pull request was closed or merged. Inspect the PR
description for links to work items. When the PR was merged, move each
linked Linear issue to its completed state and close the loop on the factory
task that produced the PR. When the PR was closed without merging, report
that on the linked issue instead; do not mark anything done.
