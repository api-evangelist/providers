---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://api.realtyfeed.com/reso/odata
  baseurl_source: declared
  description: 'RESO-certified Web API (OData) for MLS data distribution: OAuth2 client-credentials token, $metadata, Field/Lookup, Property, Member, Office, OpenHouse, PropertyRooms and Media, with RESO or RealtyFee'
  name: MLS Router API
  slug: mls-router-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/realtyfeed/refs/heads/main/llms/realtyfeed-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/realtyfeed-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/realtyfeed/refs/heads/main/well-known/realtyfeed-realtyna-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/realtyfeed-realtyna-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/realtyfeed/refs/heads/main/well-known/realtyfeed-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/realtyfeed-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/realtyfeed/refs/heads/main/hosts/realtyfeed-hosts.yml
  title: ''
  type: Hosts
  url: hosts/realtyfeed-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/realtyfeed/refs/heads/main/vendors/realtyfeed-vendors.yml
  title: ''
  type: Vendors
  url: vendors/realtyfeed-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/realtyfeed/refs/heads/main/security/realtyfeed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/realtyfeed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://realtyfeed.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.realtyfeed.com/
- group: docs
  title: ''
  type: APIReference
  url: https://realtyna.atlassian.net/wiki/spaces/RA/pages/1157300225/MLS+Router+API
- group: auth
  title: ''
  type: Authentication
  url: https://realtyna.atlassian.net/wiki/spaces/RA/pages/1750892546/Authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://realtyna.atlassian.net/wiki/spaces/RA/pages/1952710661/Rate+Limits
- group: design
  title: ''
  type: ErrorCodes
  url: https://realtyna.atlassian.net/wiki/spaces/RA/pages/1143046151/Error+Handling
- group: operate
  title: ''
  type: ChangeLog
  url: https://realtyna.atlassian.net/wiki/spaces/RA/pages/1934852101/Changelog
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/realtyfeed/refs/heads/main/postman/realtyfeed-mls-router-postman.json
  title: ''
  type: Postman
  url: postman/realtyfeed-mls-router-postman.json
- group: build
  title: ''
  type: PostmanCollection
  url: https://postman.realtyfeed.com/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.realtyfeed.com/
- group: company
  title: ''
  type: Blog
  url: https://realtyfeed.com/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://realtyfeed.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://realtyfeed.com/about/leadership/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://realtyfeed.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://realtyfeed.com/legal/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://realtyfeed.com/contact/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.realtyfeed.com/mcp
  - status: 200
    url: https://realtyfeed.com/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: RealtyFeed, a Realtyna company, is a real estate data platform that distributes MLS listing data to brokers, agents, IDX website builders and data vendors. Its MLS Router API is a RESO-certified Web API (OData) at api.realtyfeed.com, authenticated with OAuth2 client credentials issued through the RealtyFeed Dashboard (data vendors get access through a separate invitation-only dashboard). It serves Property, Member, Office, OpenHouse, PropertyRooms, Media, metadata and lookup resources in either RESO or RealtyFeed output, plus geo and history endpoints, and publishes documentation (authentication, searchable fields, error handling, rate limits, changelog) and a public Postman collection. RealtyFeed also offers MLS On The Fly IDX widgets.
layout: provider
modified: '2026-10-13'
name: RealtyFeed
nav: Providers
network: true
overview: 'RealtyFeed is listed with 1 API on the [APIs.io](https://apis.io/) network: MLS Router API. Tagged areas include Company, Real Estate, MLS, RESO Web API, and OData.


  RealtyFeed''s developer surface includes documentation, API reference, authentication, changelog, signup flow, engineering blog, support, and 15 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 73.2
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Realtyfeed Domain Security
  slug: realtyfeed-domain-security
  summary_line: TLSv1.3 · DMARC
slug: realtyfeed
tags:
- Company
- Real Estate
- MLS
- RESO Web API
- OData
- IDX
- Property Data
website: https://realtyfeed.com/
---
