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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bookmax-net/plans/bookmax-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bookmax-net-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bookmax-net/llms/bookmax-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bookmax-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/bookmax-net/well-known/bookmax-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bookmax-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/bookmax-net/hosts/bookmax-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bookmax-net-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bookmax.net/terms
- group: start
  title: ''
  type: SignUp
  url: https://my.bookmax.net/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bookmax.net/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bookmax.net/help/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.bookmax.net/help/docs
- group: auth
  href: https://artifacts.apis.io/bookmax-net/security/bookmax-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bookmax-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bookmax.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bookmax.net/pricing
- group: operate
  title: ''
  type: Help
  url: https://www.bookmax.net/help
- group: company
  title: ''
  type: Blog
  url: https://www.bookmax.net/blog
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found on the API host api.bookmax.net.
  evidence:
  - status: 0
    url: https://api.bookmax.net
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bookmax is an online bookmark manager founded in 2003, offering free and premium accounts for storing bookmarks, lists, contacts, notes, documents and RSS feeds. It operates from Austria with servers in Germany, provides web, iOS and Android access, and includes features like folder organization, tagging, and synchronization across devices.
image: https://www.bookmax.net/img/og-bookmax.jpg
layout: provider
modified: '2026-11-02'
name: Bookmax
nav: Providers
network: true
overview: 'Bookmax is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Bookmark, OnlineService, Austria, Free, and Premium.


  Bookmax''s developer surface includes signup flow, getting-started guide, documentation, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Bookmax Net Plans Pricing
  plan_count: 3
  slug: bookmax-net-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - austria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
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
- kind: domain-security
  name: Bookmax Net Domain Security
  slug: bookmax-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bookmax-net
tags:
- Bookmark
- OnlineService
- Austria
- Free
- Premium
website: https://bookmax.net/
---
