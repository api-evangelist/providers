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
    dynamic_client_registration: false
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
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/pinion/well-known/pinion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pinion-well-known.yml
- group: other
  href: https://artifacts.apis.io/pinion/hosts/pinion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pinion-hosts.yml
- group: other
  href: https://artifacts.apis.io/pinion/vendors/pinion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pinion-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pinionglobal.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://support.pinionglobal.com/support/home?logged_out=true
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pinionglobal.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.pinionglobal.com/blog/category/news-room/
- group: auth
  href: https://artifacts.apis.io/pinion/security/pinion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pinion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pinionglobal.com/
coverage:
  checked: '2026-10-28'
  detail: MCP endpoint at https://support.pinionglobal.com/mcp requires authentication, preventing contract discovery.
  evidence:
  - status: 401
    url: https://support.pinionglobal.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-28'
description: 'Food & Ag Consulting: Specialized Advisory Services | Pinion Global. With roots in food & ag consulting, Pinion offers specialized advisory services to optimize financial and operational business outcomes. Connect with us to drive your business forward.'
image: https://www.pinionglobal.com/wp-content/uploads/2017/05/PS_Crops_people_650x500.jpg
layout: provider
modified: '2026-10-28'
name: Pinion
nav: Providers
network: true
overview: 'Pinion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Food, Agriculture, Consulting, Advisory, and Finance.


  Pinion''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.1
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pinion/pinion-2026-11-03T141227.png
security:
- kind: domain-security
  name: Pinion Domain Security
  slug: pinion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pinion
tags:
- Food
- Agriculture
- Consulting
- Advisory
- Finance
website: https://pinionglobal.com/
---
