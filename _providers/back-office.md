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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://finally.com
- group: company
  title: ''
  type: Blog
  url: https://finally.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://finally.com/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://apps.finally.com/onboarding/business?target=signup
- group: start
  title: ''
  type: Login
  url: https://apply.finally.com/product-login
- group: operate
  title: ''
  type: Support
  url: https://help.finally.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finally.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finally.com/privacy.html
- group: auth
  title: ''
  type: TrustCenter
  url: security/back-office-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/back-office-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/back-office-domain-security.yml
created: '2026-07-17'
description: Back Office, Inc. operates Finally (finally.com), a Miami-based fintech that provides a unified, AI-powered bookkeeping, accounting, and finance suite for growing small and medium-sized businesses. The platform combines automated bookkeeping and ledger management, accounts payable and bill pay, expense management, corporate cards with built-in controls, invoicing, payment processing, payroll across 150+ countries, and credit monitoring, with AI agents that classify transactions, reconcile accounts, close the books, and prepare audits. Founded in 2018 and trusted by over 3,500 companies, Finally publishes a SOC 2 trust center but does not currently expose a public developer API or developer portal; this profile tracks its identity, web properties, and security posture in the API Evangelist network.
image: https://finally.com/wp-content/uploads/2026/01/Frame-8.png
layout: provider
modified: '2026-07-18'
name: Back Office
nav: Providers
network: true
overview: 'Back Office is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Accounting, Bookkeeping, and Payroll.


  Back Office''s developer surface includes engineering blog, pricing, signup flow, support, and 7 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 16.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/back-office/refs/heads/main/screenshots/back-office-2026-07-25T202210.png
security:
- kind: domain-security
  name: Back Office Domain Security
  slug: back-office-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Back Office Trust Center
  slug: back-office-trust-center
  summary_line: SOC 2
slug: back-office
tags:
- Company
- Fintech
- Accounting
- Bookkeeping
- Payroll
- Expense Management
- Accounts Payable
- Corporate Cards
- Invoicing
- Financial Automation
- AI Agents
website: https://finally.com
---
