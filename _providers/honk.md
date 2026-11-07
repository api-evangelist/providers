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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/honk/hosts/honk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/honk-hosts.yml
- group: other
  href: https://artifacts.apis.io/honk/vendors/honk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/honk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.honkforhelp.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.honkforhelp.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.honkforhelp.com/plans
- group: other
  title: ''
  type: Leadership
  url: https://www.honkforhelp.com/platform/management
- group: company
  title: ''
  type: Blog
  url: https://www.honkforhelp.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://developer.honkforhelp.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/honkforhelp
- group: auth
  href: https://artifacts.apis.io/honk/security/honk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/honk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://honkforhelp.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://developer.honkforhelp.com/mcp
  - status: 403
    url: https://mw.honkforhelp.com/mcp
  - status: 200
    url: https://honkforhelp.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Honk provides a cloud‑based platform that delivers roadside assistance, accident and catastrophe management, vehicle logistics, and reimbursement services. It offers specialized vehicle support for motorcycles, EVs and RVs and integrates with insurance, fleet/rental, automotive and logistics providers to manage multiple services in real time.
image: https://cdn.prod.website-files.com/6684038244dfbd9cc1631cde/66b2318cb29834fb32797587_social.png
layout: provider
modified: '2026-10-25'
name: Honk
nav: Providers
network: true
overview: 'Honk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Roadside Assistance, Fleet Management, Insurance Solutions, Logistics Management, and Accident Management.


  Honk''s developer surface includes pricing, engineering blog, documentation, and 8 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 49.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 8.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/honk/honk-2026-11-03T133440.png
security:
- kind: domain-security
  name: Honk Domain Security
  slug: honk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: honk
tags:
- Roadside Assistance
- Fleet Management
- Insurance Solutions
- Logistics Management
- Accident Management
- Reimbursement
- Specialized Vehicles
website: https://honkforhelp.com
---
