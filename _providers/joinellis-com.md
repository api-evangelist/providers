---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/joinellis-com/well-known/joinellis-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/joinellis-com-status-security.txt
- group: commercial
  href: https://artifacts.apis.io/joinellis-com/plans/joinellis-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/joinellis-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/joinellis-com/llms/joinellis-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/joinellis-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/joinellis-com/well-known/joinellis-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/joinellis-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/joinellis-com/hosts/joinellis-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joinellis-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/joinellis-com/vendors/joinellis-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/joinellis-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ellis.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ellis.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ellis.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.ellis.com/team/henry-lam
- group: auth
  href: https://artifacts.apis.io/joinellis-com/security/joinellis-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joinellis-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joinellis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ellis.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ellis.com/pricing
- group: company
  title: ''
  type: About
  url: https://www.ellis.com/about
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.ellis.com/login
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://joinellis.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Ellis provides a Business Immigration Platform that helps individuals and employers navigate U.S. visa and green card processes. The service offers tools for H-1B, H-1B1, TN, O-1, L-1, J-1, E-1/E-2, E-3 visas, as well as green card options like EB-1A, EB-2 NIW, EB-2 PERM, and EB-3 PERM. It includes resources such as visa calculators, lottery odds, and immigration news, aiming to simplify complex immigration procedures for both applicants and sponsors.
image: https://www.ellis.com/images/opengraph.png
layout: provider
modified: '2026-10-22'
name: Ellis
nav: Providers
network: true
overview: 'Ellis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Immigration, Visa, GreenCard, and Platform.


  Ellis'' developer surface includes documentation, pricing, and 14 more developer resources.'
plans:
- name: Joinellis Com Plans Pricing
  plan_count: 16
  slug: joinellis-com-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 56.3
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/joinellis-com/joinellis-com-2026-11-03T134213.png
security:
- kind: domain-security
  name: Joinellis Com Domain Security
  slug: joinellis-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: joinellis-com
tags:
- Company
- Immigration
- Visa
- GreenCard
- Platform
website: https://joinellis.com/
---
