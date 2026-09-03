---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rx-redefined-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rxredefined.com/
- group: company
  title: ''
  type: About
  url: https://rxredefined.com/company
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rxredefined.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.rxredefined.com/login
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@press_48315
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rxredefined/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/rxredefined
- group: company
  title: ''
  type: Careers
  url: https://ats.rippling.com/rxredefined/jobs
- group: operate
  title: ''
  type: Support
  url: mailto:support@rxredefined.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rx-redefined-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/rx-redefined-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/rx-redefined-conformance.yml
coverage:
  checked: '2026-08-26'
  detail: 'Rx Redefined ships a DMEPOS platform only as a customer-only web application — app.rxredefined.com 307s every path to /login and its robots.txt is `Disallow: /` — while the four-page marketing site has no developer, docs or API section and returns a real 404 for /openapi.json, /llms.txt and every /.well-known path, and no api./docs./developer. subdomain resolves.'
  evidence:
  - status: 404
    url: https://rxredefined.com/openapi.json
  - status: 404
    url: https://rxredefined.com/llms.txt
  - status: 404
    url: https://rxredefined.com/.well-known/api-catalog
  - status: 200
    url: https://app.rxredefined.com/robots.txt
  - status: 404
    url: https://api.github.com/orgs/rxredefined
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Rx Redefined Inc is a healthcare technology company in Arroyo Grande, California, founded in 2018, that operates a patented, compliance-focused DMEPOS (durable medical equipment, prosthetics, orthotics and supplies) platform for physicians. The platform lets a medical practice become a licensed physician-owned DMEPOS supplier and distribute medical supplies — insulin pumps, breast pumps, ostomy pouches, urinary catheters — directly to its own patients instead of handing the order to a third-party supplier. It ships two products: a Full-Service product built around physician personal performance, and an In-Office product built around the in-office ancillary services exception. The platform covers CMS licensing onboarding, electronic ordering with per-order compliance and eligibility checks, supply-chain integration with 10+ U.S. distribution centers, and end-to-end revenue-cycle and audit management. The company reports use across 350+ U.S. clinics and runs on ISO 27001 certified
  infrastructure with HIPAA controls. The product is a customer-only web application at app.rxredefined.com; Rx Redefined publishes no public API, developer portal, SDK or machine-readable contract of any kind.'
image: https://rxredefined.com/apple-touch-icon.png
layout: provider
modified: '2026-08-26'
name: Rx Redefined
nav: Providers
network: true
overview: 'Rx Redefined is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Supplies, DMEPOS, and Durable Medical Equipment.


  Rx Redefined''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Rx Redefined Plans Pricing
  plan_count: 0
  slug: rx-redefined-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Rx Redefined Rate Limits
  slug: rx-redefined-rate-limits
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rx-redefined/refs/heads/main/screenshots/rx-redefined-2026-09-02T154222.png
security:
- kind: domain-security
  name: Rx Redefined Domain Security
  slug: rx-redefined-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rx-redefined
tags:
- Company
- Healthcare
- Medical Supplies
- DMEPOS
- Durable Medical Equipment
- Compliance
- HIPAA
- Revenue Cycle Management
- Supply Chain
- Physicians
- Clinical
website: https://rxredefined.com/
---
