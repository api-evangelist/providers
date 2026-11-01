---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Discover APIs, learn how to use them, try them out interactively, and sign up to acquire keys.
  name: Kantar API
  slug: kantar-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/kantar/hosts/kantar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kantar-hosts.yml
- group: other
  href: https://artifacts.apis.io/kantar/vendors/kantar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kantar-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.kantar.com/investor-relations/register
- group: company
  title: ''
  type: Newsroom
  url: https://www.kantar.com/industries/media
- group: auth
  href: https://artifacts.apis.io/kantar/security/kantar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kantar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kantar.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.kantar.com/campaigns/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.kantar.com/campaigns/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.kantar.com/campaigns/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kantar.com/campaigns/api
- group: operate
  title: ''
  type: Support
  url: https://www.kantar.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kantar.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kantar.com/cookies-policies
coverage:
  checked: '2026-10-28'
  detail: Developer portal requires sign‑in to view APIs, blocking unauthenticated access.
  evidence:
  - status: 302
    url: https://portal.api.kantar.com/apis
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Kantar is a global data, insights, and consulting firm that helps brands understand consumer behavior, market trends, and brand performance. Through extensive research, advanced analytics, and strategic advisory services, Kantar delivers actionable intelligence to drive business decisions across advertising, media, retail, and product development. The company operates in over 100 markets, offering a wide range of solutions including brand health tracking, audience measurement, and digital transformation consulting.
image: https://www.kantar.com/-/media/project/kantar/global/may-cx-header.png
layout: provider
modified: '2026-10-28'
name: Kantar
nav: Providers
network: true
overview: 'Kantar is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Insights, MarketResearch, Analytics, and Consulting.


  Kantar''s developer surface includes signup flow, documentation, API reference, getting-started guide, support, and 8 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kantar Domain Security
  slug: kantar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kantar
tags:
- Data
- Insights
- MarketResearch
- Analytics
- Consulting
website: https://kantar.com/
---
