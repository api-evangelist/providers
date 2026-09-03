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
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://paytient.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paytient.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.paytient.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paytient.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paytient.com/terms
- group: start
  title: ''
  type: Login
  url: https://my.paytient.com/login
- group: auth
  title: ''
  type: Security
  url: https://www.paytient.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.paytient.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/paytient-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/paytient-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paytient-domain-security.yml
created: '2026-07-17'
description: Paytient operates a healthcare payments platform built around the Health Payment Account (HPA) — an interest-free, no-credit-check payment card that lets members pay for medical, dental, vision, pharmacy, and veterinary care and then repay on a self-selected schedule. It is distributed through employers, health plans, insurers, brokers, and providers to reduce out-of-pocket cost friction, and provides employer dashboards for tracking healthcare spend. Paytient is SOC 2 Type II audited and holds NMLS licensure (ID 2040265). The company was surfaced as a portfolio company of Felicis and added to the API Evangelist network; as of this pass it publishes no public developer API, SDKs, OpenAPI, or documentation surface — only a member/employer application and marketing site.
image: https://cdn.prod.website-files.com/631eddfd322acf4bde169f3f/69cd3cd08d2fab3a5a631e51_Paytient_Webclip_Webflow_256x256_Light.png
layout: provider
modified: '2026-07-20'
name: Paytient
nav: Providers
network: true
overview: 'Paytient is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Healthcare, Payments, and Fintech.


  Paytient''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 19.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paytient/refs/heads/main/screenshots/paytient-2026-08-07T191704.png
security:
- kind: domain-security
  name: Paytient Domain Security
  slug: paytient-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Paytient Vulnerability Disclosure
  slug: paytient-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Paytient Trust Center
  slug: paytient-trust-center
  summary_line: SOC 2
slug: paytient
tags:
- Company
- Financial-Services
- Healthcare
- Payments
- Fintech
- Health Benefits
- Lending
website: https://paytient.com
---
