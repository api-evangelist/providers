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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides job search, salary, tax calculator and employer tools via HTTP endpoints.
  name: Talent.com API
  slug: talent-com-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/talent-com/hosts/talent-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/talent-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/talent-com/vendors/talent-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/talent-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.talent.com:443/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.talent.com:443/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://employers.talent.com/resources/news
- group: company
  title: ''
  type: Blog
  url: https://blog.talent.com
- group: auth
  href: https://artifacts.apis.io/talent-com/security/talent-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/talent-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://talent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.talent.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.talent.com/api-docs
coverage:
  checked: '2026-10-27'
  detail: API documentation pages return HTML shells without machine‑readable OpenAPI or other contract files.
  evidence:
  - status: 200
    url: https://www.talent.com/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Talent.com is a global job search platform that aggregates millions of job listings from employers, recruiters, and staffing agencies worldwide. It helps job seekers find opportunities across various industries and locations, offering tools such as salary calculators, tax calculators, and personalized job alerts. The site also provides services for employers to post jobs and reach a broad audience.
image: https://cdn-static.talent.com/img/others/talent_meta_img.png
layout: provider
modified: '2026-10-27'
name: Talent.com
nav: Providers
network: true
overview: 'Talent.com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Job Search, Recruiting, Employment, and Technology.


  Talent.com''s developer surface includes engineering blog, documentation, API reference, and 7 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 58.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/talent-com/talent-com-2026-11-03T144311.png
security:
- kind: domain-security
  name: Talent Com Domain Security
  slug: talent-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: talent-com
tags:
- Company
- Job Search
- Recruiting
- Employment
- Technology
website: https://talent.com/
---
