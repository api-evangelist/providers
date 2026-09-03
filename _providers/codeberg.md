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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Codeberg Agentic Access
  operation_count: 44
  slug: codeberg-agentic-access
  summary_line: 44 operations · 18 acting
api_count: 1
apis:
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: Read and write repository files, list commits, and read the Git tree.
  name: Codeberg Git Content API
  slug: codeberg-git-content-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: List, search, create, get, edit, and comment on issues.
  name: Codeberg Issues API
  slug: codeberg-issues-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: Server metadata.
  name: Codeberg Miscellaneous API
  slug: codeberg-miscellaneous-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: Get and manage organizations and their repositories.
  name: Codeberg Organizations API
  slug: codeberg-organizations-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: List, create, get, update, and merge pull requests.
  name: Codeberg Pull Requests API
  slug: codeberg-pull-requests-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: Manage repository releases attached to Git tags.
  name: Codeberg Releases API
  slug: codeberg-releases-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: Create, search, get, edit, and delete repositories and their branches and tags.
  name: Codeberg Repositories API
  slug: codeberg-repositories-api
- baseURL: https://codeberg.org/api/v1
  baseurl_source: declared
  description: Look up and search users and the authenticated account.
  name: Codeberg Users API
  slug: codeberg-users-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Codeberg API (Forgejo) Git Content API
  slug: open-codeberg-git-content-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Issues API
  slug: open-codeberg-issues-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Miscellaneous API
  slug: open-codeberg-miscellaneous-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Organizations API
  slug: open-codeberg-organizations-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Pull Requests API
  slug: open-codeberg-pull-requests-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Releases API
  slug: open-codeberg-releases-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Repositories API
  slug: open-codeberg-repositories-api
- collection_type: open
  name: Codeberg API (Forgejo) Git Content Users API
  slug: open-codeberg-users-api
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
random_paper: 8
rate_limits:
- limit_count: 3
  name: Codeberg Rate Limits
  slug: codeberg-rate-limits
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Open-Source
- Forgejo
- Non-Profit
website: https://codeberg.org
---
