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
    agentic_commerce: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Numetric's authentication-gated REST API, served from api.numetric.com. The base host responds with a Numetric API banner and requires credentials on every path.
  name: Numetric API
  slug: numetric-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/numetric-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.numetric.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.numetric.com/
- group: operate
  title: ''
  type: Support
  url: https://support.numetric.com/en/
created: '2026-07-17'
description: Numetric operates a cloud data-analytics platform exposed through the Numetric REST API (api.numetric.com) alongside a developer portal and an Intercom-hosted help center for support. It is a portfolio company of Insight Partners, added to the API Evangelist network and enriched from its public API surface. The public API is authentication-gated and the marketing site is bot-protected, so this profile captures the verified developer, API, and support surfaces discovered by live probes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/numetric.png
layout: provider
modified: '2026-07-20'
name: Numetric
nav: Providers
network: true
overview: 'Numetric publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Data, and Software-as-a-Service.


  Numetric''s developer surface includes support and 3 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 2
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/numetric/refs/heads/main/screenshots/numetric-2026-08-07T185739.png
security:
- kind: domain-security
  name: Numetric Domain Security
  slug: numetric-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: numetric
tags:
- Company
- Analytics
- Data
- Software-as-a-Service
website: http://www.numetric.com/
---
