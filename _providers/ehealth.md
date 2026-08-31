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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: eHealth's partner-facing developer API for embedding health-insurance shopping, quoting, and enrollment. Access is gated behind the eHealth developer portal (registration/login required); no public Op
  name: eHealth API
  slug: ehealth-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ehealth-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ehealth.com/
- group: start
  title: ''
  type: Login
  url: https://developer.ehealth.com/login
- group: operate
  title: ''
  type: Support
  url: https://developer.ehealth.com/faqs
- group: company
  title: ''
  type: Website
  url: https://www.ehealth.com/
created: '2026-07-17'
description: 'eHealth, Inc. (NASDAQ: EHTH) operates a licensed online health insurance marketplace where U.S. consumers can compare and enroll in health coverage from more than 180 insurance carriers across all 50 states and Washington, D.C. Founded in 1997, the company offers individual and family plans, Medicare products (Medicare Advantage, Medigap, and Part D prescription drug plans), small-business coverage, and Individual Coverage Health Reimbursement Arrangements (ICHRA). eHealth also provides a partner-facing developer API, documented at its gated developer portal, that lets affiliates and partners embed health-insurance shopping, quoting, and enrollment into their own applications.'
image: https://www.ehealth.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: eHealth
nav: Providers
network: true
overview: 'eHealth publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Insurance, Healthcare, Insurance, and Medicare.


  eHealth''s developer surface includes support and 4 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 1
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Ehealth Domain Security
  slug: ehealth-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ehealth
tags:
- Company
- Health Insurance
- Healthcare
- Insurance
- Medicare
- Marketplace
- Enrollment
- Insurtech
website: https://www.ehealth.com/
---
