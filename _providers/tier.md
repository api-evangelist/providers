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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Partner-facing data API from Dott (formerly TIER), providing vehicle and availability data (GBFS-style) to authorized partners. Access requires a per-partner API Key issued through Dott's registration
  name: Dott Partner API
  slug: dott-partner-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tier-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ridedott.com
- group: company
  title: ''
  type: Blog
  url: https://ridedott.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.ridedott.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ridedott.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ridedott.com/website-terms/
- group: auth
  title: ''
  type: Authentication
  url: authentication/tier-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tier-llms.txt
created: '2026-07-17'
description: Tier (now operating as Dott following the 2024 merger of TIER Mobility and Dott) is a European micromobility operator providing shared e-scooters and e-bikes across more than 400 cities in Europe and the Middle East. The company exposes a partner-facing Dott Partner API — an API-Key-gated data feed (including GBFS-style vehicle-availability data) governed by its published API Licence — alongside consumer rider apps for iOS and Android. Founded in 2018 and headquartered in Amsterdam, Tier/Dott was backed by Northzone, Point Nine, and Speedinvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tier.png
layout: provider
modified: '2026-07-21'
name: Tier
nav: Providers
network: true
overview: 'Tier publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Micromobility, Transportation, and Mobility.


  Tier''s developer surface includes engineering blog, support, authentication, and 5 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tier/refs/heads/main/screenshots/tier-2026-09-02T163730.png
security:
- kind: authentication
  name: Tier Authentication
  slug: tier-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tier Domain Security
  slug: tier-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tier
tags:
- Company
- Consumer
- Micromobility
- Transportation
- Mobility
- Scooters
- E-Bikes
- GBFS
- Europe
website: https://ridedott.com
---
