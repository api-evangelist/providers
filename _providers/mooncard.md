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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mooncard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mooncard.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.mooncard.co/developers/sign_in
- group: start
  title: ''
  type: SignUp
  url: https://developers.mooncard.co/developers/sign_up
- group: operate
  title: ''
  type: Support
  url: https://success.mooncard.co/s/?language=en_US
- group: company
  title: ''
  type: Blog
  url: https://www.mooncard.co/en/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mooncard.co/en/privacy-policy
created: '2026-07-17'
description: Mooncard is a French corporate expense-management platform that pairs a smart payment card, a mobile app, and accounting-automation software so finance teams can handle business spending end to end without manual data entry. It automates expense reports, VAT recovery, and mileage and per-diem calculations, then syncs transactions into accounting systems such as Sage, Cegid, SAP, Microsoft Dynamics, Exact Online, and Agicap. Mooncard also runs a developer program that offers API access plus a sandbox environment, though the API reference and OpenAPI are gated behind a developer-portal login and are not publicly discoverable.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mooncard.png
layout: provider
modified: '2026-07-20'
name: Mooncard
nav: Providers
network: true
overview: 'Mooncard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Expense Management, Corporate Cards, and Fintech.


  Mooncard''s developer surface includes signup flow, support, engineering blog, and 4 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mooncard/refs/heads/main/screenshots/mooncard-2026-08-07T184234.png
security:
- kind: domain-security
  name: Mooncard Domain Security
  slug: mooncard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mooncard
tags:
- Company
- Financial-Services
- Expense Management
- Corporate Cards
- Fintech
- Accounting Automation
- Payments
website: https://www.mooncard.co/
---
