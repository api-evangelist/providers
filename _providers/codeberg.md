---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Codeberg Agentic Access
  operation_count: 44
  slug: codeberg-agentic-access
  summary_line: 44 operations · 18 acting
api_count: 8
apis:
- description: Read and write repository files, list commits, and read the Git tree.
  name: Codeberg Git Content API
  slug: codeberg-git-content-api
- description: List, search, create, get, edit, and comment on issues.
  name: Codeberg Issues API
  slug: codeberg-issues-api
- description: Server metadata.
  name: Codeberg Miscellaneous API
  slug: codeberg-miscellaneous-api
- description: Get and manage organizations and their repositories.
  name: Codeberg Organizations API
  slug: codeberg-organizations-api
- description: List, create, get, update, and merge pull requests.
  name: Codeberg Pull Requests API
  slug: codeberg-pull-requests-api
- description: Manage repository releases attached to Git tags.
  name: Codeberg Releases API
  slug: codeberg-releases-api
- description: Create, search, get, edit, and delete repositories and their branches and tags.
  name: Codeberg Repositories API
  slug: codeberg-repositories-api
- description: Look up and search users and the authenticated account.
  name: Codeberg Users API
  slug: codeberg-users-api
artifact_total: 15
collections:
- collection_type: open
  name: Codeberg API (Forgejo)
  slug: open-codeberg
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codeberg-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codeberg-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codeberg-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forgejo/forgejo
- group: other
  title: ''
  type: Fediverse
  url: https://social.anoxinon.de/@codeberg
- group: company
  title: ''
  type: Website
  url: https://codeberg.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codeberg.org
- group: commercial
  title: ''
  type: Plans
  url: plans/codeberg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/codeberg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/codeberg-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.codeberg.org/
created: '2026-07-12'
description: Codeberg is a community-run, non-profit platform for hosting Git repositories and collaborating on free and open source software, operated by the Codeberg e.V. association in Germany. It runs on Forgejo (a community fork of Gitea) and exposes the Forgejo/Gitea-compatible REST API at https://codeberg.org/api/v1 for repositories, issues, pull requests, releases, Git content, users, and organizations. Access is free and donation-funded; requests authenticate with a personal access token or OAuth2.
finops:
- name: Codeberg Finops
  service_category: Developer Tools and Code Hosting
  slug: codeberg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codeberg.png
layout: provider
modified: '2026-07-12'
name: Codeberg
nav: Providers
network: true
overview: 'Codeberg publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Git Content API, Issues API, Miscellaneous API, and 5 more. Tagged areas include Code Hosting, Git, Git Hosting, Version Control, and Repositories.


  Codeberg''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Codeberg Plans Pricing
  plan_count: 2
  slug: codeberg-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 3
  name: Codeberg Rate Limits
  slug: codeberg-rate-limits
score:
  band: thin
  composite: 35.2
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codeberg/refs/heads/main/screenshots/codeberg-2026-07-25T205910.png
security:
- kind: authentication
  name: Codeberg Authentication
  slug: codeberg-authentication
  summary_line: apiKey/basic/oauth2 · 3 schemes
- kind: domain-security
  name: Codeberg Domain Security
  slug: codeberg-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: codeberg
tags:
- Code Hosting
- Git
- Git Hosting
- Version Control
- Repositories
- Pull Requests
- Issue Tracking
- Open Source
- Forgejo
- Non-Profit
website: https://codeberg.org
---
