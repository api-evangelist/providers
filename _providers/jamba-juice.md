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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jamba-juice-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://focusbrands.onspring.com/Survey/c8f3c589-0151-4e3c-bc73-4f1089ab2928
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jamba-juice-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jamba.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.jamba.com
created: '2026-07-17'
description: Jamba (formerly Jamba Juice) is an American quick-service restaurant chain that blends fruit-and-vegetable smoothies, fresh juices, bowls, and boosts. Founded in 1990 in San Luis Obispo, California, it operates hundreds of locations and is owned by GoTo Foods (formerly Focus Brands). The brand runs a consumer website, mobile ordering apps, and a rewards program; it publishes no public developer API. Surfaced in the API Evangelist network as a trinity-ventures portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jamba-juice.png
layout: provider
modified: '2026-07-19'
name: Jamba Juice
nav: Providers
network: true
overview: Jamba Juice is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Food and Beverage, Restaurant, and Quick Service.
random_paper: 9
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jamba-juice/refs/heads/main/screenshots/jamba-juice-2026-07-25T223049.png
security:
- kind: domain-security
  name: Jamba Juice Domain Security
  slug: jamba-juice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jamba Juice Vulnerability Disclosure
  slug: jamba-juice-vulnerability-disclosure
  summary_line: disclosure policy published
slug: jamba-juice
tags:
- Company
- Consumer
- Food and Beverage
- Restaurant
- Quick Service
- Smoothies
- Juice
website: https://www.jamba.com
---
