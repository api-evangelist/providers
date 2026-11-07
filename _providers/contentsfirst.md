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
- group: company
  title: ''
  type: Website
  url: https://www.contentsfirst.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.contentsfirst.com/media/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tappytoon
- group: other
  href: https://artifacts.apis.io/contentsfirst/hosts/contentsfirst-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contentsfirst-hosts.yml
- group: other
  href: https://artifacts.apis.io/contentsfirst/vendors/contentsfirst-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contentsfirst-vendors.yml
- group: auth
  href: https://artifacts.apis.io/contentsfirst/security/contentsfirst-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contentsfirst-domain-security.yml
coverage:
  checked: '2026-11-04'
  detail: Contents First is the corporate site for a Seoul webtoon/webnovel holding company (parent of consumer platform Tappytoon); it publishes no API, no developer portal, and no docs host, and the standard contract paths on www.contentsfirst.com (/openapi.json, /swagger.json, /asyncapi.yaml, /graphql, /mcp) all return 404 while api.contentsfirst.com and developers.contentsfirst.com do not resolve in DNS.
  evidence:
  - status: 404
    url: https://www.contentsfirst.com/openapi.json
  - status: 404
    url: https://www.contentsfirst.com/swagger.json
  - status: 404
    url: https://www.contentsfirst.com/asyncapi.yaml
  - status: 404
    url: https://www.contentsfirst.com/graphql
  - status: 404
    url: https://www.contentsfirst.com/mcp
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Contents First, Inc. is a Seoul-based digital storytelling company founded in January 2013 to bring Korean webtoon, webnovel, entertainment and game IP to global readers. It operates Tappytoon, a premier digital-first webtoon and webnovel platform launched in August 2016 that serves more than 8 million readers across 241 countries in English, French and German, with over 450 million chapter views to date. Contents First produces and licenses original IP through in-house Tappytoon Studio and its affiliate production studios Maru Comics, C&C Revolution, and Studio Alive (a joint venture with Redice Studio). The corporate site publishes a company narrative and a media room; no developer portal, public API, or machine-readable contract (OpenAPI, AsyncAPI, GraphQL, MCP) is advertised. Media contact meetus@contentsfirst.com, business contact corp@contentsfirst.com.
image: https://www.contentsfirst.com/images/hero.jpg
layout: provider
modified: '2026-11-04'
name: Contents First
nav: Providers
network: true
overview: Contents First is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Integration, Platform, and Webtoon.
random_paper: 14
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 2.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contentsfirst Domain Security
  slug: contentsfirst-domain-security
  summary_line: TLSv1.3 · DMARC
slug: contentsfirst
tags:
- Company
- Data
- Integration
- Platform
- Webtoon
- Webnovel
- Entertainment
- Media
- Content
- South Korea
website: https://www.contentsfirst.com
---
