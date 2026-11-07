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
- group: commercial
  href: https://artifacts.apis.io/little-green-light/plans/little-green-light-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/little-green-light-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/little-green-light/llms/little-green-light-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/little-green-light-llms.txt
- group: other
  href: https://artifacts.apis.io/little-green-light/hosts/little-green-light-hosts.yml
  title: ''
  type: Hosts
  url: hosts/little-green-light-hosts.yml
- group: other
  href: https://artifacts.apis.io/little-green-light/vendors/little-green-light-vendors.yml
  title: ''
  type: Vendors
  url: vendors/little-green-light-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.littlegreenlight.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://www.littlegreenlight.com/support/
- group: start
  title: ''
  type: SignUp
  url: https://www.littlegreenlight.com/signup
- group: auth
  title: ''
  type: Security
  url: https://www.littlegreenlight.com/security/
- group: build
  title: ''
  type: SDKs
  url: https://www.littlegreenlight.com/libraries/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.littlegreenlight.com/privacypolicy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.littlegreenlight.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.littlegreenlight.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.littlegreenlight.com/category/16-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.littlegreenlight.com/
- group: auth
  href: https://artifacts.apis.io/little-green-light/security/little-green-light-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/little-green-light-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://littlegreenlight.com/
coverage:
  checked: '2026-10-27'
  detail: The provider's documentation is a knowledge base with no public API specifications.
  evidence:
  - status: 200
    url: https://help.littlegreenlight.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Little Green Light provides cloud‑based donor management software for nonprofits, offering tools to track donations, manage contacts, run fundraising campaigns, and generate reports. It aims to help small and mid‑size charitable organizations streamline their operations and improve donor relationships.
image: https://www.littlegreenlight.com/wp-content/uploads/2024/12/Dasboard-widgets-image.png
layout: provider
modified: '2026-10-27'
name: Little Green Light
nav: Providers
network: true
overview: 'Little Green Light is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Donor Management, Nonprofit Software, Fundraising, Online Donations, and Data Management.


  Little Green Light''s developer surface includes support, signup flow, pricing, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
plans:
- name: Little Green Light Plans Pricing
  plan_count: 8
  slug: little-green-light-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 55.4
    operational_transparency: 5.3
  previous_composite: 29.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/little-green-light/little-green-light-2026-11-03T134932.png
security:
- kind: domain-security
  name: Little Green Light Domain Security
  slug: little-green-light-domain-security
  summary_line: TLSv1.2 · DMARC
slug: little-green-light
tags:
- Donor Management
- Nonprofit Software
- Fundraising
- Online Donations
- Data Management
website: https://littlegreenlight.com/
---
