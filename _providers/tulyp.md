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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tulyp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tulyp.io
- group: commercial
  title: ''
  type: Pricing
  url: https://tulyp.io/pricing
- group: company
  title: ''
  type: About
  url: https://tulyp.io/about
- group: operate
  title: ''
  type: Contact
  url: https://tulyp.io/contact
- group: start
  title: ''
  type: Login
  url: https://app.tulyp.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tulyp.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tulyp.io/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tulyp-io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tulyp-llms.txt
created: '2026-07-17'
description: Tulyp is a SaaS treasury platform from French company SmarTrade SAS that gives CFOs and treasurers of SMEs and mid-caps (10-200M euro revenue) real-time visibility into their foreign-exchange (FX) exposure. The platform aggregates financial data from connected ERPs, accounting software, and banks, calculates net currency exposure by type and timeframe, translates currency movements into impact on revenue, margins, and EBITDA, and alerts when exposure crosses risk-policy thresholds. Backed by Speedinvest. Tulyp publishes no public developer API; it does publish an llms.txt content index for AI systems.
image: https://tulyp.io/og/og-tulyp-default.jpg
layout: provider
modified: '2026-07-21'
name: Tulyp
nav: Providers
network: true
overview: 'Tulyp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Treasury, Foreign Exchange, and Risk Management.


  Tulyp''s developer surface includes pricing and 9 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 7.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tulyp/refs/heads/main/screenshots/tulyp-2026-09-02T164512.png
security:
- kind: domain-security
  name: Tulyp Domain Security
  slug: tulyp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tulyp
tags:
- Company
- Fintech
- Treasury
- Foreign Exchange
- Risk Management
- Software-as-a-Service
- France
website: https://tulyp.io
---
