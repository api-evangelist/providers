---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'spritefusion-com API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: spritefusion-com API
  slug: spritefusion-com-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/spritefusion-com/rules/spritefusion-com-rules.yml
  title: ''
  type: Spectral
  url: rules/spritefusion-com-rules.yml
- group: design
  href: https://artifacts.apis.io/spritefusion-com/json-ld/spritefusion-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/spritefusion-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/spritefusion-com/vocabulary/spritefusion-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/spritefusion-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/spritefusion-com/data-model/spritefusion-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/spritefusion-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/spritefusion-com/components/spritefusion-com-components.yml
  title: ''
  type: Components
  url: components/spritefusion-com-components.yml
- group: auth
  href: https://artifacts.apis.io/spritefusion-com/authentication/spritefusion-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/spritefusion-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/spritefusion-com/errors/spritefusion-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/spritefusion-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/spritefusion-com/conformance/spritefusion-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spritefusion-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/spritefusion-com/llms/spritefusion-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spritefusion-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/spritefusion-com/well-known/spritefusion-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spritefusion-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/spritefusion-com/hosts/spritefusion-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spritefusion-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/spritefusion-com/vendors/spritefusion-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spritefusion-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.spritefusion.com/docs/pixel-art-generator/api/api-reference
- group: auth
  href: https://artifacts.apis.io/spritefusion-com/security/spritefusion-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spritefusion-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spritefusion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.spritefusion.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.spritefusion.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.spritefusion.com/docs/pixel-art-generator/quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.spritefusion.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spritefusion.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spritefusion.com/
coverage:
  checked: '2026-10-31'
  detail: Documentation provides API reference but no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract.
  evidence:
  - status: 200
    url: https://www.spritefusion.com/docs/pixel-art-generator/api/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Sprite Fusion is an online tool that lets game developers create tilemaps, generate pixel art sprites, and animate them for 2D games. It offers a web‑based editor with real‑time preview, supports exporting maps up to 4.5 MB, and provides both free forever usage and paid desktop editions. The platform is used by universities, studios, and indie creators, and requires no login to start creating.
image: https://www.spritefusion.com/images/logoWhite.svg
json_schemas:
- name: GetApiV1TagsResponse
  property_count: 1
  slug: spritefusion-com-get-api-v1-tags-response
- name: GetApiV1VfxLibraryIceResponse
  property_count: 5
  slug: spritefusion-com-get-api-v1-vfx-library-ice-response
- name: PatchApiV1AssetsAssetResponse
  property_count: 1
  slug: spritefusion-com-patch-api-v1-assets-asset-response
- name: PostApiV1GenerateRequest
  property_count: 3
  slug: spritefusion-com-post-api-v1-generate-request
- name: PostApiV1NormalMapsRequest
  property_count: 1
  slug: spritefusion-com-post-api-v1-normal-maps-request
- name: PostApiV1NormalMapsResponse
  property_count: 4
  slug: spritefusion-com-post-api-v1-normal-maps-response
jsonld:
- class_count: 11
  name: Spritefusion Com Context
  property_count: 13
  slug: spritefusion-com-context
layout: provider
modified: '2026-10-31'
name: spritefusion-com
nav: Providers
network: true
overview: 'spritefusion-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Game Development, Pixel Art, Tilemap Editor, 2D Games, and Open Source.


  The spritefusion-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  spritefusion-com''s developer surface includes authentication, API reference, documentation, getting-started guide, engineering blog, and 16 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: spritefusion-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: spritefusion-com-rules
scopes:
- name: Spritefusion Com Scopes
  scope_count: 0
  slug: spritefusion-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 72.7
    catalog_earned_first_party: 0.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 79.1
    contract_quality: 54.3
    developer_ergonomics: 52.4
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Spritefusion Com Authentication
  slug: spritefusion-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Spritefusion Com Domain Security
  slug: spritefusion-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spritefusion-com
tags:
- Game Development
- Pixel Art
- Tilemap Editor
- 2D Games
- Open Source
website: https://spritefusion.com/
---
