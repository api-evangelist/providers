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
    auth_clarity: bearer
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
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for generating and accessing 3D assets such as textures, decals, HDRIs, and models.
  name: 3D Asset API
  slug: 3d-asset-api
- description: '3DTexel API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: 3DTexel API
  slug: 3dtexel-com-api
- baseURL: https://3dtexel.com/wp-json/3dtexel/v1
  baseurl_source: declared
  description: Read-only search over 3DTexel asset libraries (free CC0 and AI-generated) and list of AI generators. No authentication. See https://3dtexel.com/llms.txt
  name: 3DTexel public API API
  slug: 3dtexel-public-api-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/3dtexel-com/plans/3dtexel-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/3dtexel-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/3dtexel-com/rules/3dtexel-com-rules.yml
  title: ''
  type: Spectral
  url: rules/3dtexel-com-rules.yml
- group: design
  href: https://artifacts.apis.io/3dtexel-com/json-ld/3dtexel-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/3dtexel-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/3dtexel-com/vocabulary/3dtexel-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/3dtexel-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/3dtexel-com/data-model/3dtexel-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/3dtexel-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/3dtexel-com/conformance/3dtexel-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/3dtexel-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/3dtexel-com/llms/3dtexel-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/3dtexel-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/3dtexel-com/well-known/3dtexel-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/3dtexel-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/3dtexel-com/hosts/3dtexel-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3dtexel-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/3dtexel-com/vendors/3dtexel-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/3dtexel-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://3dtexel.com/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://3dtexel.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://3dtexel.com/login/
- group: auth
  href: https://artifacts.apis.io/3dtexel-com/security/3dtexel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3dtexel-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://3dtexel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://3dtexel.com/developers/
- group: commercial
  title: ''
  type: Pricing
  url: https://3dtexel.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://3dtexel.com/contact/
coverage:
  checked: '2026-10-31'
  detail: The developer portal returns HTML pages without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://3dtexel.com/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 3DTexel provides AI-powered generation of PBR textures, decals, HDRIs, terrain, animations, and 3D models, offering over 1,653 free CC0 assets for game developers using Unreal, Unity, Blender, and other platforms. The service enables creators to quickly produce high-quality, game-ready assets, streamlining development pipelines and reducing the need for manual asset creation.
image: https://3dtexel.com/wp-content/uploads/2025/02/cropped-freepik-202505042034043Rd3.png
json_schemas:
- name: GetCreditsResponse
  property_count: 2
  slug: 3dtexel-com-get-credits-response
- name: PostGenerationsQuoteRequest
  property_count: 2
  slug: 3dtexel-com-post-generations-quote-request
- name: PostGenerationsQuoteResponse
  property_count: 4
  slug: 3dtexel-com-post-generations-quote-response
- name: PostGenerationsRequest
  property_count: 3
  slug: 3dtexel-com-post-generations-request
- name: PostWpJson3DtexelApiV1GenerationsQuoteRequest
  property_count: 2
  slug: 3dtexel-com-post-wp-json3-dtexel-api-v1-generations-quote-request
- name: PostWpJson3DtexelApiV1GenerationsRequest
  property_count: 3
  slug: 3dtexel-com-post-wp-json3-dtexel-api-v1-generations-request
jsonld:
- class_count: 9
  name: 3Dtexel Com Context
  property_count: 12
  slug: 3dtexel-com-context
layout: provider
modified: '2026-10-31'
name: 3DTexel
nav: Providers
network: true
overview: '3DTexel publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including public API API, and 2 more. Tagged areas include Company, Artificial Intelligence, 3D Assets, Textures, and Game Development.


  The 3DTexel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  3DTexel''s developer surface includes documentation, pricing, support, and 15 more developer resources.'
plans:
- name: 3Dtexel Com Plans Pricing
  plan_count: 7
  slug: 3dtexel-com-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: 3DTexel API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: 3dtexel-com-rules
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 24.1
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 32.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 3Dtexel Com Domain Security
  slug: 3dtexel-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 3dtexel-com
tags:
- Company
- Artificial Intelligence
- 3D Assets
- Textures
- Game Development
website: https://3dtexel.com/
---
