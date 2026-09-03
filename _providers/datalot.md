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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datalot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datalot.com/
- group: start
  title: ''
  type: Login
  url: https://app.datalot.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.centerfield.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.centerfield.com/terms-and-conditions/
created: '2026-07-17'
description: Datalot (now operating under parent company Centerfield Insurance Services) is an analytics-driven digital customer-acquisition and live lead/call marketplace platform for the insurance industry, spanning auto, home, life, health, Medicare, and commercial lines. It runs digital demand-generation campaigns, qualifies consumers in a real-time marketplace, and routes them by data to carriers and agents, adding agent-presence and telephony management, TCPA/regulatory compliance tooling, and secondary-market handling for unmatched consumers. Named carrier clients include Liberty Mutual, Allstate, Farmers, Progressive, Travelers, Aetna, and Humana. The company is SOC 2 certified. It was surfaced as a portfolio company of bessemer-venture-partners; the customer-facing surface is an authenticated carrier/agent portal at app.datalot.com with no public API, SDK, or developer documentation.
image: https://www.datalot.com/images/datalot-logo.png
layout: provider
modified: '2026-07-18'
name: Datalot
nav: Providers
network: true
overview: Datalot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Lead Generation, and Customer Acquisition.
random_paper: 10
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datalot/refs/heads/main/screenshots/datalot-2026-07-25T211336.png
security:
- kind: domain-security
  name: Datalot Domain Security
  slug: datalot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datalot
tags:
- Company
- Insurance
- Insurtech
- Lead Generation
- Customer Acquisition
- Marketing
- Marketplace
- Advertising
website: https://www.datalot.com/
---
