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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-03'
api_count: 3
apis:
- baseURL: https://developers.atomtickets.com/api
  baseurl_source: declared
  description: Partner API for managing venues, productions, showtimes, ordering and loyalty.
  name: Atomtickets Partner API
  slug: atomtickets-partner-api
- baseURL: https://developers.atomtickets.com/api
  baseurl_source: declared
  description: The Partner API from Atomtickets — 12 operation(s) for partner.
  name: Atomtickets Partner API
  slug: atomtickets-partner-api
- baseURL: https://developers.atomtickets.com/api
  baseurl_source: declared
  description: The Ping API from Atomtickets — 1 operation(s) for ping.
  name: Atomtickets Ping API
  slug: atomtickets-ping-api
artifact_total: 12
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atomtickets/refs/heads/main/rules/atomtickets-rules.yml
  title: ''
  type: Spectral
  url: rules/atomtickets-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atomtickets/refs/heads/main/json-ld/atomtickets-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/atomtickets-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atomtickets/refs/heads/main/vocabulary/atomtickets-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atomtickets-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atomtickets/refs/heads/main/data-model/atomtickets-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atomtickets-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atomtickets/refs/heads/main/conformance/atomtickets-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atomtickets-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atomtickets/refs/heads/main/hosts/atomtickets-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atomtickets-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atomtickets/refs/heads/main/vendors/atomtickets-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atomtickets-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atomtickets/refs/heads/main/packages/atomtickets-packages.yml
  title: ''
  type: SDKs
  url: packages/atomtickets-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atomtickets/refs/heads/main/packages/atomtickets-packages.yml
  title: ''
  type: Packages
  url: packages/atomtickets-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atomtickets.com/tos
- group: operate
  title: ''
  type: Support
  url: https://www.atomtickets.com/help/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atomtickets.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.atomtickets.com/press
- group: start
  title: ''
  type: Login
  url: https://www.atomtickets.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.atomtickets.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.atomtickets.com/getting-started/introduction/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.atomtickets.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AtomTickets
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atomtickets/refs/heads/main/security/atomtickets-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atomtickets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atomtickets.com
coverage:
  checked: 2026-09-26
  detail: Developer portal provides HTML docs but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://developers.atomtickets.com/api/venues/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Atomtickets is a ticketing platform that provides APIs for event organizers to create, manage, and sell tickets online. It offers functionalities such as event creation, seat selection, pricing tiers, discount codes, and real-time sales analytics. The service aims to simplify ticket distribution for concerts, conferences, and other live events, integrating with payment gateways and offering webhook notifications for transaction updates. Atomtickets targets both small venues and large enterprises, emphasizing scalability, security, and a developer-friendly experience.
image: https://images.atomtickets.com/image/upload/website/share-site.png
json_schemas:
- name: GetPartnerV1ProductionSearchBynameResponse
  property_count: 12
  slug: atomtickets-get-partner-v1-production-search-byname-response
- name: GetPartnerV1ProductionsByvendorproductionidByvendorproductio
  property_count: 11
  slug: atomtickets-get-partner-v1-productions-byvendorproductionid-byvendorproductio
- name: GetPartnerV1VenueDetailsDetailidResponse
  property_count: 2
  slug: atomtickets-get-partner-v1-venue-details-detailid-response
- name: GetPartnerV1VenuesByvendorvenueidByvendorvenueididShowtimesB
  property_count: 3
  slug: atomtickets-get-partner-v1-venues-byvendorvenueid-byvendorvenueidid-showtimes-b
- name: GetPartnerV1VenuesC00682352378ShowtimesByvendorshowtimeidByv
  property_count: 3
  slug: atomtickets-get-partner-v1-venues-c00682352378-showtimes-byvendorshowtimeid-byv
- name: PostPartnerV1V1IdDetailsByidsResponse
  property_count: 13
  slug: atomtickets-post-partner-v1-v1-id-details-byids-response
jsonld:
- class_count: 15
  name: Atomtickets Context
  property_count: 33
  slug: atomtickets-context
layout: provider
modified: '2026-09-26'
name: Atomtickets
nav: Providers
network: true
overview: 'Atomtickets publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Partner API, Ping API, and 1 more. Tagged areas include Company, Ticketing, Event, and Payments.


  The Atomtickets catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Atomtickets'' developer surface includes support, getting-started guide, documentation, and 17 more developer resources.'
random_paper: 4
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Atomtickets API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: atomtickets-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 42.9
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Atomtickets Domain Security
  slug: atomtickets-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atomtickets
tags:
- Company
- Ticketing
- Event
- Payments
website: https://www.atomtickets.com
---
