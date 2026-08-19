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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Lokalise Agentic Access
  operation_count: 10
  slug: lokalise-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 4
apis:
- description: Full-coverage REST API for the Lokalise TMS. Resources include projects, keys, translations, contributors, files, comments, screenshots, snapshots, teams, team users, team user groups, branches, langu
  name: Lokalise API v2
  slug: api-v2
- description: The Files API from Lokalise — 1 operation(s) for files.
  name: Lokalise Files API
  slug: lokalise-files-api
- description: The Keys API from Lokalise — 2 operation(s) for keys.
  name: Lokalise Keys API
  slug: lokalise-keys-api
- description: The Projects API from Lokalise — 2 operation(s) for projects.
  name: Lokalise Projects API
  slug: lokalise-projects-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lokalise API v2 Files API
  slug: open-lokalise-files-api
- collection_type: open
  name: Lokalise API v2 Files Keys API
  slug: open-lokalise-keys-api
- collection_type: open
  name: Lokalise API v2 Files Projects API
  slug: open-lokalise-projects-api
- collection_type: open
  name: Lokalise API v2
  slug: open-lokalise
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lokalise-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lokalise-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lokalise-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://lokalise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lokalise.com/
- group: company
  title: ''
  type: Blog
  url: https://lokalise.com/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lokalise
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lokalise
- group: commercial
  title: ''
  type: Plans
  url: plans/lokalise-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lokalise-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lokalise-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.lokalise.com/llms.txt
created: '2026-05-23'
description: Lokalise is a translation management system (TMS) for software, mobile, web, games, and documentation. It pairs collaborative localization workflows with AI machine translation and a full-coverage REST API (APIv2) that exposes projects, keys, translations, files, contributors, screenshots, snapshots, tasks, branches, glossaries, webhooks, and payments. Official SDKs are maintained for Node.js, Python, Ruby, PHP, Go, Java, .NET, and Elixir.
finops:
- name: Lokalise Finops
  service_category: API
  slug: lokalise-finops
graphqls:
- description: Lokalise is a translation management platform for apps and websites. The API covers project and key management, file uploads, translation creation, screenshot context, order management, task managemen
  name: Lokalise GraphQL API
  slug: lokalise-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lokalise.png
layout: provider
modified: '2026-05-23'
name: Lokalise
nav: Providers
network: true
overview: 'Lokalise publishes 3 APIs on the [APIs.io](https://apis.io/) network: Files API, Keys API, and Projects API. Tagged areas include Localization, Translation, TMS, AI Machine Translation, and REST.


  Lokalise''s developer surface includes authentication, documentation, engineering blog, GitHub presence, and 8 more developer resources.'
plans:
- name: Lokalise Plans Pricing
  plan_count: 1
  slug: lokalise-plans-pricing
random_paper: 107
rate_limits:
- limit_count: 2
  name: Lokalise Rate Limits
  slug: lokalise-rate-limits
score:
  band: thin
  composite: 35.5
  delta: -1.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 57.4
    developer_ergonomics: 19.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lokalise/refs/heads/main/screenshots/lokalise-2026-06-20T184709.png
security:
- kind: authentication
  name: Lokalise Authentication
  slug: lokalise-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lokalise Domain Security
  slug: lokalise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lokalise
tags:
- Localization
- Translation
- TMS
- AI Machine Translation
- REST
- Developer Tools
website: https://lokalise.com/
---
