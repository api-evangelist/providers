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
  href: https://artifacts.apis.io/storyraise/hosts/storyraise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/storyraise-hosts.yml
- group: other
  href: https://artifacts.apis.io/storyraise/vendors/storyraise-vendors.yml
  title: ''
  type: Vendors
  url: vendors/storyraise-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://storyraise.com/terms-conditions?hsLang=en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://storyraise.com/privacy-policy?hsLang=en
- group: auth
  href: https://artifacts.apis.io/storyraise/security/storyraise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/storyraise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://storyraise.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.storyraise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.storyraise.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.storyraise.com/docs/getting-started/what-is-storyraise/
- group: operate
  title: ''
  type: Support
  url: https://storyraise.com/support
- group: company
  title: ''
  type: Blog
  url: https://storyraise.com/blog?hsLang=en
- group: commercial
  title: ''
  type: Pricing
  url: https://storyraise.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://storyraise.com/demo
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI or other machine‑readable contract was found on the provider's site.
  evidence:
  - status: 200
    url: https://docs.storyraise.com/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Storyraise provides donor engagement software that helps nonprofits and foundations build real connections with supporters. Their platform offers tools for fundraising, donor stewardship, impact reporting, and analytics, enabling organizations to manage campaigns, major gifts, and communications across sectors such as education, healthcare, and social justice.
layout: provider
modified: '2026-10-27'
name: Storyraise
nav: Providers
network: true
overview: 'Storyraise is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Non-Profit, Fundraising, Donor Management, and Software-as-a-Service.


  Storyraise''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 7 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.8
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/storyraise/storyraise-2026-11-03T143859.png
security:
- kind: domain-security
  name: Storyraise Domain Security
  slug: storyraise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: storyraise
tags:
- Company
- Non-Profit
- Fundraising
- Donor Management
- Software-as-a-Service
website: https://storyraise.com/
---
