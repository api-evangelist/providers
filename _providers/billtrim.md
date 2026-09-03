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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/billtrim-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://billtrim.com
- group: start
  title: ''
  type: SignUp
  url: https://app.billtrim.com/a3register
- group: start
  title: ''
  type: Login
  url: https://app.billtrim.com/a4login
- group: operate
  title: ''
  type: Support
  url: mailto:support@billtrim.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.billtrim.com/privacy-pledge.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.billtrim.com/terms.html
created: '2026-07-17'
description: BillTrim is a consumer bill-management and negotiation service that helps households lower, monitor, and pay their recurring bills. Its team negotiates with providers on the customer's behalf (up to twice a year), watches for price increases before autopay processes, and can pay bills automatically from a connected bank account. BillTrim advertises support for 20,000+ service providers across internet, cable, phone, insurance, and other recurring household expenses. Backed by 500 Global, it operates as a consumer-facing web and mobile application; no public developer API or developer portal is currently published.
image: https://www.billtrim.com/images/webclip.png
layout: provider
modified: '2026-07-18'
name: BillTrim
nav: Providers
network: true
overview: 'BillTrim is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bill Negotiation, Bill Management, Personal Finance, and Fintech.


  BillTrim''s developer surface includes signup flow, support, and 5 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.5
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/billtrim/refs/heads/main/screenshots/billtrim-2026-07-25T202949.png
security:
- kind: domain-security
  name: Billtrim Domain Security
  slug: billtrim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: billtrim
tags:
- Company
- Bill Negotiation
- Bill Management
- Personal Finance
- Fintech
- Consumer
- Bill Pay
- Savings
website: https://billtrim.com
---
