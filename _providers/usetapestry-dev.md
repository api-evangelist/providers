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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Weave your social graph on Solana
  name: Tapestry API
  slug: tapestry-api
- baseURL: https://api.usetapestry.dev
  baseurl_source: declared
  description: 'Tapestry API as documented publicly: 41 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Tapestry API
  slug: usetapestry-dev-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/usetapestry-dev/rules/usetapestry-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/usetapestry-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/usetapestry-dev/json-ld/usetapestry-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usetapestry-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/usetapestry-dev/vocabulary/usetapestry-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usetapestry-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/usetapestry-dev/data-model/usetapestry-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usetapestry-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/usetapestry-dev/authentication/usetapestry-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usetapestry-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/usetapestry-dev/conformance/usetapestry-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usetapestry-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/usetapestry-dev/well-known/usetapestry-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usetapestry-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/usetapestry-dev/hosts/usetapestry-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usetapestry-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/usetapestry-dev/vendors/usetapestry-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usetapestry-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/usetapestry-dev/packages/usetapestry-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/usetapestry-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/usetapestry-dev/packages/usetapestry-dev-packages.yml
  title: ''
  type: Packages
  url: packages/usetapestry-dev-packages.yml
- group: auth
  href: https://artifacts.apis.io/usetapestry-dev/security/usetapestry-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usetapestry-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usetapestry.dev
- group: company
  title: ''
  type: Blog
  url: https://blog.usetapestry.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usetapestry.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usetapestry.dev/
- group: start
  title: ''
  type: SignUp
  url: https://1uuq2fsw8t6.typeform.com/to/S4RPS1UZ?typeform-source=www.usetapestry.dev
coverage:
  checked: '2026-10-29'
  detail: API documentation is rendered via JavaScript and no machine‑readable OpenAPI spec could be retrieved.
  evidence:
  - status: 200
    url: https://docs.usetapestry.dev/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Tapestry is Solana’s leading social protocol that provides developers with a unified social layer across Solana, Farcaster, Lens, Bluesky and more. By leveraging wallet identities, Tapestry enables rapid integration of profiles, follows, likes, comments and activity feeds, reducing the need for custom social infrastructure. The platform offers a quick‑start guide, extensive documentation, and an early‑access sign‑up, helping builders launch social features in minutes rather than weeks.
image: https://cdn.prod.website-files.com/67814d9fc76ba46748750247/678fe574dc9c8c78bc2af16f_logo_full.svg
json_schemas:
- name: GetV1CommentsResponse
  property_count: 2
  slug: usetapestry-dev-get-v1-comments-response
- name: GetV1ContentsPost123Response
  property_count: 2
  slug: usetapestry-dev-get-v1-contents-post123-response
- name: GetV1ContentsProfileUser123Response
  property_count: 2
  slug: usetapestry-dev-get-v1-contents-profile-user123-response
- name: PostContentsCreateRequest
  property_count: 6
  slug: usetapestry-dev-post-contents-create-request
- name: PostV1ContentsDeleteResponse
  property_count: 2
  slug: usetapestry-dev-post-v1-contents-delete-response
- name: PutV1ProfilesUpdateResponse
  property_count: 2
  slug: usetapestry-dev-put-v1-profiles-update-response
jsonld:
- class_count: 45
  name: Usetapestry Dev Context
  property_count: 47
  slug: usetapestry-dev-context
layout: provider
modified: '2026-10-29'
name: Tapestry
nav: Providers
network: true
overview: 'Tapestry is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Solana, Protocol, and API.


  The Tapestry catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tapestry''s developer surface includes authentication, engineering blog, documentation, API reference, signup flow, and 12 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Tapestry API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: usetapestry-dev-rules
scopes:
- name: Usetapestry Dev Scopes
  scope_count: 0
  slug: usetapestry-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Usetapestry Dev Authentication
  slug: usetapestry-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Usetapestry Dev Domain Security
  slug: usetapestry-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: usetapestry-dev
tags:
- Company
- Social
- Solana
- Protocol
- API
- Developer
website: https://www.usetapestry.dev
---
