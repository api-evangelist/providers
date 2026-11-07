---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hiring assistant API (no public machine‑readable contract found)
  name: BKK Staff API
  slug: bkk-staff-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bkkstaff-com/plans/bkkstaff-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bkkstaff-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/bkkstaff-com/authentication/bkkstaff-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bkkstaff-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/bkkstaff-com/llms/bkkstaff-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bkkstaff-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bkkstaff-com/well-known/bkkstaff-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bkkstaff-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bkkstaff-com/hosts/bkkstaff-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bkkstaff-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bkkstaff-com/vendors/bkkstaff-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bkkstaff-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.bkkstaff.com/signup
- group: auth
  href: https://artifacts.apis.io/bkkstaff-com/security/bkkstaff-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bkkstaff-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bkkstaff.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bkkstaff.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bkkstaff.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bkkstaff.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bkkstaff.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://www.bkkstaff.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.bkkstaff.com/blog
- group: company
  title: ''
  type: About
  url: https://www.bkkstaff.com/about
coverage:
  checked: '2026-11-02'
  detail: Provider docs are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://www.bkkstaff.com/go
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: BKK Staff provides a hiring assistant service for small businesses, screening job applications, following up with candidates, and delivering a shortlist of interview‑ready applicants. Priced at $99 per open position for 30 days with no monthly fees, the platform supports multiple languages and integrates via email or Slack notifications. It aims to simplify hiring for owners and small HR teams by handling applicant communication and qualification without acting as a job board or recruitment agency.
image: https://s3.biznitos.com/curator/mcp/uploads/a1c7b536-487d-436e-8727-51d8b6b465c9.jpg
layout: provider
modified: '2026-11-02'
name: BKK Staff
nav: Providers
network: true
overview: 'BKK Staff is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hiring, Staffing, Small Business, Automation, and Thailand.


  BKK Staff''s developer surface includes authentication, signup flow, documentation, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Bkkstaff Com Plans Pricing
  plan_count: 1
  slug: bkkstaff-com-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - thailand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bkkstaff Com Authentication
  slug: bkkstaff-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bkkstaff Com Domain Security
  slug: bkkstaff-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bkkstaff-com
tags:
- Hiring
- Staffing
- Small Business
- Automation
- Thailand
website: https://bkkstaff.com/
---
