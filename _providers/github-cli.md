---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: GitHub CLI (gh) is the official command-line tool for GitHub, bringing pull requests, issues, actions, and other GitHub features to the terminal.
  name: GitHub CLI
  slug: github-cli
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cli/cli/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/cli/cli/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/cli/cli/blob/trunk/.github/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/cli/cli/blob/trunk/.github/CODE-OF-CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cli/cli/blob/trunk/.github/CONTRIBUTING.md
- group: company
  title: ''
  type: Website
  url: https://cli.github.com
- group: docs
  title: ''
  type: Documentation
  url: https://cli.github.com/manual/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cli/cli
created: '2026-03-25'
description: GitHub CLI (gh) is the official command-line tool for GitHub, bringing pull requests, issues, actions, and other GitHub features to the terminal.
finops:
- name: Github Cli Finops
  service_category: API
  slug: github-cli-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/github-cli.png
layout: provider
modified: '2026-04-28'
name: GitHub CLI
nav: Providers
network: true
overview: 'GitHub CLI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Command Line Interface and Platform CLI.


  The GitHub CLI catalog on APIs.io includes 1 Spectral governance ruleset.


  GitHub CLI''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Github Cli Plans Pricing
  plan_count: 3
  slug: github-cli-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Github Cli Rate Limits
  slug: github-cli-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: GitHub CLI API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: github-cli-rules
score:
  band: emerging
  composite: 13.9
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 13.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/github-cli/refs/heads/main/screenshots/github-cli-2026-06-20T181836.png
slug: github-cli
tags:
- Command Line Interface
- Platform CLI
---
