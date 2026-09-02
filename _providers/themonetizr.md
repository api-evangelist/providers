---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Serves active branded campaigns/missions to games and lets a game reset campaign progress and claim rewards. Consumed by the official Monetizr Unity SDK with a per-game HTTP Bearer API key.
  name: Monetizr Campaigns API
  slug: monetizr-campaigns-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/themonetizr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://monetizr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/themonetizr/The-Monetizr-Campaigns-Unity-SDK/wiki/Unity-Campaigns-SDK
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/themonetizr/The-Monetizr-Campaigns-Unity-SDK/wiki/Unity-Campaigns-SDK
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/themonetizr
- group: build
  title: ''
  type: Packages
  url: packages/themonetizr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/themonetizr-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.themonetizr.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/themonetizr-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/themonetizr-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/themonetizr-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/themonetizr-well-known.yml
- group: operate
  title: ''
  type: Support
  url: https://monetizr.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://monetizr.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monetizr.com/privacy-policy
created: '2026-07-17'
description: Monetizr (TheMonetizr) is a gaming media platform for in-game brand advertising that turns gameplay into measurable, voluntary, and non-skippable brand engagement. Brands run branded campaigns and missions inside mobile games; players complete them for in-game or brand-sponsored rewards, reporting >30% average engagement, >90% viewability, and >85% video completion across a 340M mobile-gamer reach. The Monetizr Campaigns API (base https://api.themonetizr.com) serves active campaigns to games — listing campaigns/missions, resetting progress, and claiming rewards — and is consumed by the official open-source Unity SDK using a per-game HTTP Bearer API key. The company is a Techstars-backed portfolio company.
image: https://avatars.githubusercontent.com/u/19929995?s=400
layout: provider
mcp_servers:
- description: ''
  name: TheMonetizr MCP Server
  slug: themonetizr-mcp-server
modified: '2026-07-21'
name: TheMonetizr
nav: Providers
network: true
overview: 'TheMonetizr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Gaming, In-Game Advertising, and Monetization.


  TheMonetizr''s developer surface includes documentation, getting-started guide, changelog, support, and 11 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 27.3
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Themonetizr Authentication
  slug: themonetizr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Themonetizr Domain Security
  slug: themonetizr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: themonetizr
tags:
- Company
- Advertising
- Gaming
- In-Game Advertising
- Monetization
- Mobile
- Rewards
- AdTech
- Programmatic
- Unity
website: https://monetizr.com/
---
