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
  url: security/vestwell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vestwell.com
- group: company
  title: ''
  type: Blog
  url: https://www.vestwell.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.vestwell.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://growth.vestwell.com/onboarding
- group: start
  title: ''
  type: Login
  url: https://signin.vestwell.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vestwell.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vestwell
created: '2026-07-17'
description: Vestwell is a New York City-based digital savings and retirement platform (founded 2016) that powers workplace savings programs for employers, financial advisors, financial institutions, TPAs, PEOs, payroll and benefit partners, and government agencies. Its recordkeeping and administration engine supports traditional and Safe Harbor 401(k), Solo-k, Starter-k, pooled/PEP plans, 403(b), 529 education savings, ABLE, emergency savings, student-loan repayment, and tuition reimbursement, as well as state-facilitated ("government savings") retirement programs. Vestwell emphasizes payroll and HR integrations (auto-sync across 190+ payroll providers) rather than a public developer API; onboarding, servicing, and saver access run through its web platform. Surfaced as a Lightspeed Venture Partners portfolio company and profiled here for the API Evangelist network.
image: https://cdn.sanity.io/images/1bb3tkb6/production/14342f728cf26b81ef038e34294fbb7e33c08393-1200x630.jpg
layout: provider
modified: '2026-07-21'
name: Vestwell
nav: Providers
network: true
overview: 'Vestwell is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retirement, Workplace Savings, 401k, and 529 College Savings.


  Vestwell''s developer surface includes engineering blog, support, signup flow, and 5 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vestwell/refs/heads/main/screenshots/vestwell-2026-09-02T165824.png
security:
- kind: domain-security
  name: Vestwell Domain Security
  slug: vestwell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vestwell
tags:
- Company
- Retirement
- Workplace Savings
- 401k
- 529 College Savings
- Financial-Services
- Fintech
- Recordkeeping
- Payroll Integration
- State Retirement Programs
website: https://www.vestwell.com
---
