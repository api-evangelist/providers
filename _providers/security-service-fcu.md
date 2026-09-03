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
- group: start
  title: ''
  type: Login
  url: https://ssfcu.org/login
- group: auth
  title: ''
  type: DomainSecurity
  url: security/security-service-fcu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ssfcu.org/
- group: operate
  title: ''
  type: Support
  url: https://ssfcu.org/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ssfcu.org/enrollment/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ssfcu.org/account-services/disclosures-and-terms#privacy
created: '2026-07-23'
description: 'Security Service Federal Credit Union (SSFCU), headquartered in San Antonio, Texas, is a member-owned, not-for-profit financial cooperative federally chartered and insured by the National Credit Union Administration (NCUA). It is one of the largest credit unions in the United States, serving members across Texas, Colorado, and Utah with consumer and business banking, deposit accounts, credit cards, auto and mortgage lending, and investment services through branches, online banking, and mobile apps. Its open-finance posture is the norm for a US credit union: there is no first-party public developer portal or downloadable API specification, and no public FDX or CFPB Section 1033 data-access API is documented. Consumer-permissioned account data is reachable only indirectly through third-party aggregators, and any API capability is delivered through its core banking provider rather than a self-serve developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Security Service Federal Credit Union
nav: Providers
network: true
overview: 'Security Service Federal Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Credit Union, and Open Finance.


  Security Service Federal Credit Union''s developer surface includes support and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/security-service-fcu/refs/heads/main/screenshots/security-service-fcu-2026-09-02T154721.png
security:
- kind: domain-security
  name: Security Service Fcu Domain Security
  slug: security-service-fcu-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: security-service-fcu
tags:
- Financial-Services
- Banking
- United States
- Credit Union
- Open Finance
- Data Aggregation
website: https://ssfcu.org/
---
