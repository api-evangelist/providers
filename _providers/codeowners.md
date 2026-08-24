---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 0
common:
- group: docs
  title: ''
  type: Specification
  url: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- group: docs
  title: ''
  type: Reference
  url: https://docs.gitlab.com/user/project/codeowners/reference/
- group: docs
  title: ''
  type: Documentation
  url: https://support.atlassian.com/bitbucket-cloud/docs/code-owners/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gitea.com/usage/code-owners
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/devops/repos/git/branch-policies
- group: build
  title: ''
  type: Sample
  url: https://github.com/dotnet/samples/blob/main/.github/CODEOWNERS
- group: build
  title: ''
  type: Tools
  url: https://github.com/mszostok/codeowners-validator
created: '2025-01-01'
description: CODEOWNERS is the file format originally introduced by GitHub and later adopted by GitLab, Bitbucket Cloud, Gitea, and Azure Repos that lets a repository declare which individuals or teams are responsible for a path or pattern within the codebase. Platforms use it to auto-request reviews on pull/merge requests, enforce required approvals via branch protection or push rules, and route pings on issues. The file is plain text with one rule per line - a glob pattern followed by one or more owner handles (`@username` or `@org/team`) or email addresses. Comments start with `#` and the last matching pattern wins.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codeowners.png
layout: provider
modified: '2026-04-26'
name: CODEOWNERS
nav: Providers
network: true
overview: 'CODEOWNERS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Access Control, Automation, Code Review, Governance, and Repository File.


  CODEOWNERS''s developer surface includes documentation, tooling, and 5 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 8.3
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 8.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codeowners/refs/heads/main/screenshots/codeowners-2026-06-20T174703.png
slug: codeowners
tags:
- Access Control
- Automation
- Code Review
- Governance
- Repository File
- Standards
---
