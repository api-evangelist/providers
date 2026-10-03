---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Findlocal Agentic Access
  operation_count: 18
  slug: findlocal-agentic-access
  summary_line: 18 operations
api_count: 2
apis:
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Bluesky API from FindLocal — 2 operation(s) for bluesky.
  name: FindLocal Bluesky API
  slug: findlocal-bluesky-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Github API from FindLocal — 2 operation(s) for github.
  name: FindLocal GitHub API
  slug: findlocal-github-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The History API from FindLocal — 1 operation(s) for history.
  name: FindLocal History API
  slug: findlocal-history-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Instagram API from FindLocal — 1 operation(s) for instagram.
  name: FindLocal Instagram API
  slug: findlocal-instagram-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Linktree API from FindLocal — 1 operation(s) for linktree.
  name: FindLocal Linktree API
  slug: findlocal-linktree-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Mastodon API from FindLocal — 2 operation(s) for mastodon.
  name: FindLocal Mastodon API
  slug: findlocal-mastodon-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Medium API from FindLocal — 1 operation(s) for medium.
  name: FindLocal Medium API
  slug: findlocal-medium-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Movers API from FindLocal — 1 operation(s) for movers.
  name: FindLocal Movers API
  slug: findlocal-movers-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: Hyper‑local events API providing upcoming events across US metros.
  name: FindLocal Events API
  slug: findlocal-events-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Nichos API from FindLocal — 1 operation(s) for nichos.
  name: FindLocal Nichos API
  slug: findlocal-nichos-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Pinterest API from FindLocal — 1 operation(s) for pinterest.
  name: FindLocal Pinterest API
  slug: findlocal-pinterest-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Soundcloud API from FindLocal — 1 operation(s) for soundcloud.
  name: FindLocal Soundcloud API
  slug: findlocal-soundcloud-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Threads API from FindLocal — 2 operation(s) for threads.
  name: FindLocal Threads API
  slug: findlocal-threads-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Tiktok API from FindLocal — 1 operation(s) for tiktok.
  name: FindLocal Tiktok API
  slug: findlocal-tiktok-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Trends API from FindLocal — 1 operation(s) for trends.
  name: FindLocal Trends API
  slug: findlocal-trends-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Events API from FindLocal — 2 operation(s) for events.
  name: FindLocal Events API
  slug: findlocal-events-api
- baseURL: https://findlocal.community/api
  baseurl_source: declared
  description: The Venues API from FindLocal — 1 operation(s) for venues.
  name: FindLocal Venues API
  slug: findlocal-venues-api
artifact_total: 27
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/overlays/findlocal-bluesky-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/findlocal-bluesky-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/agentic-access/findlocal-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/findlocal-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/plans/findlocal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/findlocal-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/rules/findlocal-rules.yml
  title: ''
  type: Spectral
  url: rules/findlocal-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/json-ld/findlocal-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/findlocal-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/vocabulary/findlocal-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/findlocal-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/data-model/findlocal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/findlocal-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/conventions/findlocal-conventions.yml
  title: ''
  type: Conventions
  url: conventions/findlocal-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/authentication/findlocal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/findlocal-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/errors/findlocal-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/findlocal-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/conformance/findlocal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/findlocal-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/llms/findlocal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/findlocal-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/hosts/findlocal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/findlocal-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/vendors/findlocal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/findlocal-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://findlocal.community/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://findlocal.community/privacy
- group: company
  title: ''
  type: Blog
  url: https://findlocal.community/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/findlocal/refs/heads/main/security/findlocal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/findlocal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://findlocal.community/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/findlocal
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/findlocal/workspace
- group: docs
  title: ''
  type: Documentation
  url: https://findlocal.community/docs
- group: docs
  title: ''
  type: APIReference
  url: https://findlocal.community/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://findlocal.community/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://findlocal.community/pricing
- group: start
  title: ''
  type: SignUp
  url: https://findlocal.community/signup
- group: start
  title: ''
  type: Login
  url: https://findlocal.community/login
created: '2026-09-25'
description: FindLocal provides a hyper‑local events API that aggregates over 86,000 upcoming events from more than 10,000 venues across 83 US metros. The platform offers JSON API access and an MCP server for developers to integrate event data into applications, with features like searchable calendars, maps, and widgets. Users can sign up for free API keys, manage billing, and explore event data via a developer portal. The service reads venue calendars directly, ensuring up‑to‑date listings of concerts, comedy shows, theater, and community events, and offers a free tier of 1,000 calls per month with no credit‑card required.
image: https://findlocal.community/og-default.png
json_schemas:
- name: Item
  property_count: 9
  slug: findlocal-item
- name: Mover
  property_count: 7
  slug: findlocal-mover
- name: PostsEnvelope
  property_count: 8
  slug: findlocal-posts-envelope
- name: ProfileEnvelope
  property_count: 13
  slug: findlocal-profile-envelope
jsonld:
- class_count: 8
  name: Findlocal Context
  property_count: 50
  slug: findlocal-context
layout: provider
modified: '2026-09-25'
name: FindLocal
nav: Providers
network: true
overview: 'FindLocal publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Bluesky API, GitHub API, History API, and 14 more. Tagged areas include Event, Hyperlocal, Community, Data, and Open Data.


  The FindLocal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FindLocal''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Findlocal Plans Pricing
  plan_count: 3
  slug: findlocal-plans-pricing
random_paper: 16
rules:
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: FindLocal API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: findlocal-rules
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 65.3
    developer_ergonomics: 47.6
    discoverability: 73.2
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Findlocal Authentication
  slug: findlocal-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Findlocal Domain Security
  slug: findlocal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: findlocal
tags:
- Event
- Hyperlocal
- Community
- Data
- Open Data
website: https://findlocal.community/
---
