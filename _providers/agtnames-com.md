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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'AGT Names API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AGT Names API
  slug: agtnames-com-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/agtnames-com/rules/agtnames-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agtnames-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agtnames-com/json-ld/agtnames-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agtnames-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agtnames-com/vocabulary/agtnames-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agtnames-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agtnames-com/data-model/agtnames-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agtnames-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/agtnames-com/cli/agtnames-com-cli.yml
  title: ''
  type: CLI
  url: cli/agtnames-com-cli.yml
- group: design
  href: https://artifacts.apis.io/agtnames-com/errors/agtnames-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agtnames-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agtnames-com/conformance/agtnames-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agtnames-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agtnames-com/llms/agtnames-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agtnames-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agtnames-com/well-known/agtnames-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agtnames-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agtnames-com/hosts/agtnames-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agtnames-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agtnames-com/vendors/agtnames-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agtnames-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/agtnames-com/packages/agtnames-com-packages.yml
  title: ''
  type: SDKs
  url: packages/agtnames-com-packages.yml
- group: build
  href: https://artifacts.apis.io/agtnames-com/packages/agtnames-com-packages.yml
  title: ''
  type: Packages
  url: packages/agtnames-com-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://agtnames.com/register
- group: auth
  href: https://artifacts.apis.io/agtnames-com/security/agtnames-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agtnames-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agtnames.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agtnames.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agtnames.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://agtnames.com/docs/quickstart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agtnames.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agtnames.com/privacy
created: '2026-11-01'
description: AGT Names provides on‑chain identity for AI agents via the .agt namespace on Polygon. It lets developers register a human‑readable name that resolves to a manifest containing endpoints, keys and capabilities, enabling MCP, A2A and standard HTTP interactions without centralized accounts. The platform offers migration tools, SDKs and documentation for building AI agents that can be discovered and invoked across the decentralized web.
image: https://agtnames.com/opengraph-image?0a5c07b60da9d41b
json_schemas:
- name: GetApiClaimStatusResponse
  property_count: 7
  slug: agtnames-com-get-api-claim-status-response
- name: GetApiSearchResponse
  property_count: 13
  slug: agtnames-com-get-api-search-response
- name: GetApiV2AgentCardLabelResponse
  property_count: 13
  slug: agtnames-com-get-api-v2-agent-card-label-response
- name: PostApiCheckoutRequest
  property_count: 5
  slug: agtnames-com-post-api-checkout-request
- name: PostApiV2ManifestPinResponse
  property_count: 5
  slug: agtnames-com-post-api-v2-manifest-pin-response
- name: PostApiV2QuoteRequest
  property_count: 5
  slug: agtnames-com-post-api-v2-quote-request
jsonld:
- class_count: 27
  name: Agtnames Com Context
  property_count: 74
  slug: agtnames-com-context
layout: provider
modified: '2026-11-01'
name: AGT Names
nav: Providers
network: true
overview: 'AGT Names is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Identity, Artificial Intelligence, Decentralized, and Web3.


  The AGT Names catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AGT Names'' developer surface includes CLI, signup flow, documentation, API reference, getting-started guide, and 16 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: AGT Names API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: agtnames-com-rules
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 22.7
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 29.8
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
  name: Agtnames Com Domain Security
  slug: agtnames-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agtnames-com
tags:
- Blockchain
- Identity
- Artificial Intelligence
- Decentralized
- Web3
website: https://agtnames.com/
---
