---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
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
    error_semantics: documented
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
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AdLibrarySpy provides free tools for Shopify store and Meta ads intelligence via a public API.
  name: AdLibrarySpy API
  slug: adlibraryspy-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/adlibraryspy-com/errors/adlibraryspy-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adlibraryspy-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/adlibraryspy-com/llms/adlibraryspy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adlibraryspy-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/adlibraryspy-com/well-known/adlibraryspy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adlibraryspy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adlibraryspy-com/hosts/adlibraryspy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adlibraryspy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adlibraryspy-com/vendors/adlibraryspy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adlibraryspy-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/adlibraryspy-com/security/adlibraryspy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adlibraryspy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adlibraryspy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://adlibraryspy.com/guides
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adlibraryspy.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://adlibraryspy.com/signup
- group: start
  title: ''
  type: Login
  url: https://adlibraryspy.com/login
coverage:
  checked: '2026-10-31'
  detail: The provider’s documentation site is a JavaScript‑rendered SPA with no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://adlibraryspy.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Follow me on X. The winning ads and stores I find, and what ships next. @sangngqang AdLibrarySpy provides free tools for Shopify store and Meta ads intelligence. Features include MCP, shops directory, trending stores, weekly reports, guides, and comparisons. Built for the community with no card, no trial, and 100% free access.
image: https://adlibraryspy.com/favicon.ico
layout: provider
modified: '2026-10-31'
name: AdLibrarySpy
nav: Providers
network: true
overview: 'AdLibrarySpy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Shopify, Meta Ads, Free Tools, and Community.


  AdLibrarySpy''s developer surface includes documentation, signup flow, and 9 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 12.4
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
security:
- kind: authentication
  name: Adlibraryspy Com Authentication
  slug: adlibraryspy-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adlibraryspy Com Domain Security
  slug: adlibraryspy-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adlibraryspy-com
tags:
- Advertising
- Shopify
- Meta Ads
- Free Tools
- Community
website: https://adlibraryspy.com/
---
