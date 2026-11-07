---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ReadySetAuction provides auction software platform; API details are not publicly documented.
  name: ReadySetAuction API
  slug: readysetauction-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/readysetauction/plans/readysetauction-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/readysetauction-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/readysetauction/hosts/readysetauction-hosts.yml
  title: ''
  type: Hosts
  url: hosts/readysetauction-hosts.yml
- group: other
  href: https://artifacts.apis.io/readysetauction/vendors/readysetauction-vendors.yml
  title: ''
  type: Vendors
  url: vendors/readysetauction-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://control.readysetauction.com/auth/login
- group: auth
  href: https://artifacts.apis.io/readysetauction/security/readysetauction-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/readysetauction-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://readysetauction.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.readysetauction.com/tour/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.readysetauction.com/tour/
- group: operate
  title: ''
  type: Support
  url: https://www.readysetauction.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.readysetauction.com/rsablog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.readysetauction.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.readysetauction.com/policies/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.readysetauction.com/policies/privacy-security/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.readysetauction.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: ReadySetAuction provides a cloud‑based auction software platform designed for nonprofit organizations, schools, faith‑based groups, sports teams, and other charitable entities. It supports silent, live, mobile, and online fundraising auctions, offering features such as guest management, RSVP tracking, table assignments, meal selections, and real‑time auction monitoring. The solution aims to streamline auction planning, increase proceeds, and simplify event logistics for a wide range of charitable fundraising activities.
image: https://uploads.readysetauction.com/images/feature-home-guest-mgmt.jpg
layout: provider
modified: '2026-10-27'
name: ReadySetAuction
nav: Providers
network: true
overview: 'ReadySetAuction is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Auction Software, Event Management, Mobile Bidding, Online Auction, and Guest Management.


  ReadySetAuction''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Readysetauction Plans Pricing
  plan_count: 3
  slug: readysetauction-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Readysetauction Rate Limits
  slug: readysetauction-rate-limits
scopes:
- name: Readysetauction Scopes
  scope_count: 0
  slug: readysetauction-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 28.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/readysetauction/readysetauction-2026-11-03T142023.png
security:
- kind: authentication
  name: Readysetauction Authentication
  slug: readysetauction-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Readysetauction Domain Security
  slug: readysetauction-domain-security
  summary_line: TLSv1.3
slug: readysetauction
tags:
- Auction Software
- Event Management
- Mobile Bidding
- Online Auction
- Guest Management
website: https://readysetauction.com/
---
