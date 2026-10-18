---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.8
  scored_at: '2026-10-17'
api_count: 3
apis:
- baseURL: https://api.digitalrealty.com
  baseurl_source: declared
  description: The Auth API from Digital Realty — 1 operation(s) for auth.
  name: Digital Realty Auth API
  slug: digital-realty-auth-api
- baseURL: https://api.digitalrealty.com
  baseurl_source: declared
  description: The Facility Access API from Digital Realty — 4 operation(s) for facility access.
  name: Digital Realty Facility Access API
  slug: digital-realty-facility-access-api
- baseURL: https://api.digitalrealty.com
  baseurl_source: declared
  description: The Remotehands Tickets API from Digital Realty — 2 operation(s) for remotehands tickets.
  name: Digital Realty Remotehands Tickets API
  slug: digital-realty-remotehands-tickets-api
artifact_total: 13
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/digital-realty/refs/heads/main/rules/digital-realty-rules.yml
  title: ''
  type: Spectral
  url: rules/digital-realty-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/digital-realty/refs/heads/main/json-ld/digital-realty-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/digital-realty-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/digital-realty/refs/heads/main/vocabulary/digital-realty-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/digital-realty-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/digital-realty/refs/heads/main/data-model/digital-realty-data-model.yml
  title: ''
  type: DataModel
  url: data-model/digital-realty-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/digital-realty/refs/heads/main/changelog/digital-realty-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/digital-realty-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/digital-realty/refs/heads/main/conventions/digital-realty-conventions.yml
  title: ''
  type: Conventions
  url: conventions/digital-realty-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/digital-realty/refs/heads/main/authentication/digital-realty-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digital-realty-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/digital-realty/refs/heads/main/conformance/digital-realty-conformance.yml
  title: ''
  type: Conformance
  url: conformance/digital-realty-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/digital-realty/refs/heads/main/well-known/digital-realty-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/digital-realty-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/digital-realty/refs/heads/main/hosts/digital-realty-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digital-realty-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digitalrealty.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.digitalrealty.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.digitalrealty.com/partners/register-a-lead
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digitalrealty.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.digitalrealty.com/about/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.digitalrealty.com/about/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.digitalrealty.com/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.digitalrealty.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.digitalrealty.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/digital-realty/refs/heads/main/security/digital-realty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digital-realty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digitalrealty.com
coverage:
  checked: '2026-10-14'
  detail: Documentation pages exist but provide no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://developer.digitalrealty.com/docs/registration
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Digital Realty is a global provider of data center, colocation, and interconnection solutions. Operating over 300 data centers in 55+ metros worldwide, it serves enterprises and service providers with secure, scalable infrastructure for AI, cloud, and hybrid workloads. The company emphasizes sustainability, high availability, and extensive partner ecosystems, delivering 99.999% uptime and comprehensive compliance certifications.
json_schemas:
- name: GetV1FacilityAccessAccessTicketsTicketidResponse
  property_count: 33
  slug: digital-realty-get-v1-facility-access-access-tickets-ticketid-response
- name: GetV1FacilityAccessFacilityacceidResponse
  property_count: 33
  slug: digital-realty-get-v1-facility-access-facilityacceid-response
- name: GetV1FacilityAccessPopPoesPoppoeidResponse
  property_count: 2
  slug: digital-realty-get-v1-facility-access-pop-poes-poppoeid-response
- name: GetV1RemotehandsTicketsCategoriesResponse
  property_count: 1
  slug: digital-realty-get-v1-remotehands-tickets-categories-response
- name: GetV1RemotehandsTicketsResponse
  property_count: 2
  slug: digital-realty-get-v1-remotehands-tickets-response
- name: PostV2AuthTokenResponse
  property_count: 2
  slug: digital-realty-post-v2-auth-token-response
jsonld:
- class_count: 8
  name: Digital Realty Context
  property_count: 37
  slug: digital-realty-context
layout: provider
modified: '2026-10-14'
name: Digital Realty
nav: Providers
network: true
overview: 'Digital Realty is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Auth API, Facility Access API, and Remotehands Tickets API. Tagged areas include DataCenter, Colocation, Cloud, Infrastructure, and Sustainability.


  The Digital Realty catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Digital Realty''s developer surface includes changelog, authentication, signup flow, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Digital Realty API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: digital-realty-rules
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 35.7
    discoverability: 71.4
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Digital Realty Authentication
  slug: digital-realty-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Digital Realty Domain Security
  slug: digital-realty-domain-security
  summary_line: TLSv1.3 · DMARC
slug: digital-realty
tags:
- DataCenter
- Colocation
- Cloud
- Infrastructure
- Sustainability
website: https://www.digitalrealty.com
---
