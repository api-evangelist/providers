---
aid: codeowners
url: https://raw.githubusercontent.com/api-evangelist/codeowners/refs/heads/main/apis.yml
name: CODEOWNERS
tags:
  - Access Control
  - Automation
  - Code Review
  - Governance
  - Repository File
  - Standards
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: standard
created: '2025-01-01'
modified: '2026-04-26'
position: Consumer
description: CODEOWNERS is the file format originally introduced by GitHub and later adopted by GitLab, Bitbucket Cloud, Gitea, and Azure Repos that lets a repository declare which individuals or teams are responsible for a path or pattern within the codebase. Platforms use it to auto-request reviews on pull/merge requests, enforce required approvals via branch protection or push rules, and route pings on issues. The file is plain text with one rule per line - a glob pattern followed by one or more owner handles (`@username` or `@org/team`) or email addresses. Comments start with `#` and the last matching pattern wins.
x-status: De facto convention (GitHub-originated)
x-canonical-host: GitHub Docs
x-supported-platforms:
  - name: GitHub
    docs: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
    locations:
      - .github/CODEOWNERS
      - CODEOWNERS
      - docs/CODEOWNERS
  - name: GitLab
    docs: https://docs.gitlab.com/user/project/codeowners/reference/
    locations:
      - .gitlab/CODEOWNERS
      - CODEOWNERS
      - docs/CODEOWNERS
    extras: Section headers, optional approvals, required approval counts
  - name: Bitbucket Cloud
    docs: https://support.atlassian.com/bitbucket-cloud/docs/code-owners/
    locations:
      - CODEOWNERS
  - name: Gitea
    docs: https://docs.gitea.com/usage/code-owners
    locations:
      - .gitea/CODEOWNERS
      - CODEOWNERS
      - docs/CODEOWNERS
  - name: Azure Repos
    docs: https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies
x-syntax-rules:
  - One pattern per line
  - Pattern is a fnmatch-style glob (e.g. *.js, /docs/, src/api/**/*.ts)
  - 'Owners follow the pattern, separated by whitespace: @user, @org/team, or email'
  - Comments start with
  - Blank lines are ignored
  - Last matching pattern wins
  - Invalid lines are silently skipped
  - File size limit is 3 MB on GitHub
x-pattern-precedence: Last matching pattern in the file wins
x-owner-types:
  - GitHub username (@username)
  - GitHub team (@org/team-name)
  - Email address (some platforms)
x-best-practices:
  - Place CODEOWNERS in .github/ to keep it adjacent to other GitHub metadata
  - Use teams instead of individuals for resilience
  - Order rules from broad to specific so specific overrides win
  - Combine with branch protection 'Require review from Code Owners'
  - Validate with a CI step (e.g., codeowners-validator)
  - Document each section with a comment header
x-validators:
  - name: mszostok/codeowners-validator
    url: https://github.com/mszostok/codeowners-validator
  - name: hmarr/actions/codeowners-validator
    url: https://github.com/hmarr/codeowners
  - name: codeowners-discover
    url: https://github.com/beaugunderson/codeowners
x-related-files:
  - .github/CODEOWNERS
  - CODE_OF_CONDUCT.md
  - CONTRIBUTING.md
  - SECURITY.md
  - branch protection rules (server-side)
apis: []
common:
  - type: Specification
    url: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
  - type: Reference
    url: https://docs.gitlab.com/user/project/codeowners/reference/
  - type: Documentation
    url: https://support.atlassian.com/bitbucket-cloud/docs/code-owners/
  - type: Documentation
    url: https://docs.gitea.com/usage/code-owners
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies
  - type: Sample
    url: https://github.com/dotnet/samples/blob/main/.github/CODEOWNERS
  - type: Tool
    url: https://github.com/mszostok/codeowners-validator
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
