---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/myfantasyleague/hosts/myfantasyleague-hosts.yml
  title: ''
  type: Hosts
  url: hosts/myfantasyleague-hosts.yml
- group: build
  href: https://artifacts.apis.io/myfantasyleague/packages/myfantasyleague-packages.yml
  title: ''
  type: SDKs
  url: packages/myfantasyleague-packages.yml
- group: build
  href: https://artifacts.apis.io/myfantasyleague/packages/myfantasyleague-packages.yml
  title: ''
  type: Packages
  url: packages/myfantasyleague-packages.yml
- group: auth
  href: https://artifacts.apis.io/myfantasyleague/security/myfantasyleague-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/myfantasyleague-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://home.myfantasyleague.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://home.myfantasyleague.com/get-started.html
- group: operate
  title: ''
  type: Support
  url: https://home.myfantasyleague.com/contact.html
- group: company
  title: ''
  type: Blog
  url: https://home.myfantasyleague.com/blog.html
- group: commercial
  title: ''
  type: Pricing
  url: https://home.myfantasyleague.com/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://home.myfantasyleague.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://home.myfantasyleague.com/privacy.html
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation is static HTML with no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://home.myfantasyleague.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: MyFantasyLeague provides a comprehensive fantasy football platform allowing users to create, manage, and customize leagues with various scoring formats, including standard, H2H, dynasty, and keeper options. The service offers features such as free NFL playoff leagues, mock drafts, contests, and integration with ADP. It serves fantasy enthusiasts seeking robust league management tools and a rich set of customization options for the 2026 season and beyond.
layout: provider
modified: '2026-10-28'
name: MyFantasyLeague API
nav: Providers
network: true
overview: 'MyFantasyLeague API is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fantasy Sports, Football, League Management, Custom Scoring, and Community.


  MyFantasyLeague API''s developer surface includes getting-started guide, support, engineering blog, pricing, and 7 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Myfantasyleague Domain Security
  slug: myfantasyleague-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: myfantasyleague
tags:
- Fantasy Sports
- Football
- League Management
- Custom Scoring
- Community
website: https://home.myfantasyleague.com/
---
