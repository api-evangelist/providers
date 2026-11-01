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
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-31'
api_count: 3
apis:
- baseURL: https://get.stalw.art
  baseurl_source: declared
  description: 'Stalwart Auth overview API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Stalwart Auth overview API
  slug: auth-api
- baseURL: https://get.stalw.art
  baseurl_source: declared
  description: 'Stalwart core API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Stalwart core API
  slug: core-api
- baseURL: https://get.stalw.art
  baseurl_source: declared
  description: 'Stalwart HTTP overview API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Stalwart HTTP overview API
  slug: http-api
artifact_total: 22
common:
- group: commercial
  href: https://artifacts.apis.io/stalwart/plans/stalwart-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stalwart-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/stalwart/rules/stalwart-rules.yml
  title: ''
  type: Spectral
  url: rules/stalwart-rules.yml
- group: design
  href: https://artifacts.apis.io/stalwart/json-ld/stalwart-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stalwart-context.jsonld
- group: design
  href: https://artifacts.apis.io/stalwart/vocabulary/stalwart-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stalwart-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/stalwart/data-model/stalwart-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stalwart-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://stalw.art/legal/security
- group: design
  href: https://artifacts.apis.io/stalwart/conformance/stalwart-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stalwart-conformance.yml
- group: agent
  href: https://artifacts.apis.io/stalwart/llms/stalwart-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stalwart-llms.txt
- group: auth
  href: https://artifacts.apis.io/stalwart/well-known/stalwart-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stalwart-security.txt
- group: agent
  href: https://artifacts.apis.io/stalwart/well-known/stalwart-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stalwart-well-known.yml
- group: other
  href: https://artifacts.apis.io/stalwart/hosts/stalwart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stalwart-hosts.yml
- group: other
  href: https://artifacts.apis.io/stalwart/vendors/stalwart-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stalwart-vendors.yml
- group: auth
  href: https://artifacts.apis.io/stalwart/security/stalwart-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stalwart-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/stalwart/security/stalwart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stalwart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stalw.art/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://stalw.art/
- group: docs
  title: ''
  type: Documentation
  url: https://stalw.art/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://stalw.art/docs/
- group: operate
  title: ''
  type: Support
  url: https://stalw.art/support/
- group: company
  title: ''
  type: Blog
  url: https://stalw.art/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://stalw.art/pricing/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are HTML only and provide no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://stalw.art/docs/sieve/reference/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Stalwart Labs develops an open-source mail and collaboration server offering JMAP, IMAP4, POP3, SMTP, CalDAV, CardDAV, and WebDAV support. Built in Rust, it emphasizes security, scalability, and ease of operation for enterprises and developers seeking a modern, self-hosted communication platform.
image: https://stalw.art/img/stalwart-social-card.jpg
json_schemas:
- name: GetApiAccountResponse
  property_count: 3
  slug: stalwart-get-api-account-response
- name: GetApiAuthClientResponse
  property_count: 11
  slug: stalwart-get-api-auth-client-response
- name: GetScimV2UsersResponse
  property_count: 2
  slug: stalwart-get-scim-v2-users-response
- name: PostApiAuthRequest
  property_count: 7
  slug: stalwart-post-api-auth-request
- name: PostApiAuthResponse
  property_count: 4
  slug: stalwart-post-api-auth-response
- name: PostApiCalendarRsvpRequest
  property_count: 3
  slug: stalwart-post-api-calendar-rsvp-request
- name: PostApiCalendarRsvpResponse
  property_count: 4
  slug: stalwart-post-api-calendar-rsvp-response
- name: PostAuthDeviceRequest
  property_count: 2
  slug: stalwart-post-auth-device-request
- name: PostAuthDeviceResponse
  property_count: 6
  slug: stalwart-post-auth-device-response
- name: PostAuthIntrospectResponse
  property_count: 6
  slug: stalwart-post-auth-introspect-response
- name: PostAuthRegisterRequest
  property_count: 3
  slug: stalwart-post-auth-register-request
- name: PostAutodiscoverAutodiscoverXmlRequest
  property_count: 1
  slug: stalwart-post-autodiscover-autodiscover-xml-request
- name: PostAutodiscoverAutodiscoverXmlResponse
  property_count: 3
  slug: stalwart-post-autodiscover-autodiscover-xml-response
- name: PostUsersRequest
  property_count: 2
  slug: stalwart-post-users-request
jsonld:
- class_count: 23
  name: Stalwart Context
  property_count: 55
  slug: stalwart-context
layout: provider
modified: '2026-10-28'
name: Stalwart
nav: Providers
network: true
overview: 'Stalwart is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Auth overview API, core API, and HTTP overview API. Tagged areas include Email, OpenSource, Rust, Collaboration, and Server.


  The Stalwart catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Stalwart''s developer surface includes documentation, API reference, support, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Stalwart Plans Pricing
  plan_count: 8
  slug: stalwart-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Stalwart API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: stalwart-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 77.0
    catalog_earned_first_party: 12.0
    catalog_gap: 38.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 19.7
    contract_quality: 25.6
    developer_ergonomics: 33.3
    discoverability: 71.4
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 24
      marker_coverage: 100.0
      total: 24
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stalwart Domain Security
  slug: stalwart-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Stalwart Vulnerability Disclosure
  slug: stalwart-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: stalwart
tags:
- Email
- OpenSource
- Rust
- Collaboration
- Server
- Company
website: https://stalw.art/
---
