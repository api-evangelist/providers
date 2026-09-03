---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://hounddiagnostics.com/
- group: operate
  title: ''
  type: Support
  url: https://hounddiagnostics.com/contact
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hound-labs-domain-security.yml
coverage:
  checked: '2026-08-22'
  detail: Hound Labs sells a handheld cannabis breathalyzer and, as Hound Diagnostics since the rename, a HIPAA-compliant results dashboard called Hound Chart, but the dashboard is an end-user web product with no developer portal, no API reference and no login host of its own — the whole site is a five-page brochure whose only call to action is a demo request form, and the retired houndlabs.com is now a Flywheel "Unknown Domain" 404 served under a certificate that does not even cover the name.
  evidence:
  - status: 404
    url: https://houndlabs.com/
  - status: 404
    url: https://houndlabs.com/.well-known/agent-card.json
  - status: 200
    url: https://hounddiagnostics.com/
  - status: 404
    url: https://hounddiagnostics.com/openapi.json
  - status: 404
    url: https://hounddiagnostics.com/developers
  - status: 200
    url: https://hounddiagnostics.com/robots.txt
  - status: 200
    url: https://api.github.com/orgs/Hound-Labs
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Hound Labs was a breath-measurement company founded in 2014 in the San Francisco Bay Area that built the HOUND CANNABIS BREATHALYZER, an ultra-sensitive analytical test that identifies THC molecules in breath down to picogram levels and so narrows cannabis detection to a two-to-three hour recent-use window rather than the days-to-weeks window of urine testing. The company shipped its first commercial product, the HOUND CANNABIS BREATHALYZER Collect + Send, in 2023 into construction, energy, gaming, manufacturing and transportation employers, pairing the handheld device with the Hound Labs Retriever results portal for paperless chain-of-custody and result delivery. The business now trades as Hound Diagnostics, whose about page states it is "formerly known as Hound Labs" and which sells Hound Breathalyzer, Hound Screens (a customizable panel covering cannabis plus up to nineteen substances), Hound Chart (a HIPAA-compliant cloud results platform) and Hound Check background screening.
  The original houndlabs.com host has been decommissioned and now answers a Flywheel "Unknown Domain" 404 behind a TLS certificate that does not cover the name; neither the retired domain nor the live successor site publishes a developer program, API reference, SDK, or machine-readable contract of any kind, so the products are sold and delivered as devices plus a customer-facing web dashboard rather than as a programmable surface.
image: https://hounddiagnostics.com/assets/img/logo-hound.png
layout: provider
modified: '2026-08-22'
name: Hound Labs
nav: Providers
network: true
overview: 'Hound Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diagnostics, Drug Testing, Medical Devices, and Occupational Health.


  Hound Labs'' developer surface includes support and 2 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hound-labs/refs/heads/main/screenshots/hound-labs-2026-09-02T145746.png
security:
- kind: domain-security
  name: Hound Labs Domain Security
  slug: hound-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hound-labs
tags:
- Company
- Diagnostics
- Drug Testing
- Medical Devices
- Occupational Health
- Workplace Safety
- Cannabis
- Breath Analysis
- Renamed
website: https://hounddiagnostics.com/
---
