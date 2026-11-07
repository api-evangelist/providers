---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Doseedo provides a session suite for music creators with tools for audio conversion, separation, transcription, and editing across DAWs.
  name: Doseedo API
  slug: doseedo-api
- baseURL: https://api.doseedo.com
  baseurl_source: declared
  description: 'Doseedo API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Doseedo API
  slug: doseedo-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/doseedo-com/plans/doseedo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doseedo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/doseedo-com/rules/doseedo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/doseedo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/doseedo-com/json-ld/doseedo-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/doseedo-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/doseedo-com/vocabulary/doseedo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/doseedo-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/doseedo-com/data-model/doseedo-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/doseedo-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://doseedo.com/terms
- group: design
  href: https://artifacts.apis.io/doseedo-com/conformance/doseedo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doseedo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/doseedo-com/llms/doseedo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doseedo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/doseedo-com/mcp/doseedo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/doseedo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/doseedo-com/well-known/doseedo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/doseedo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/doseedo-com/well-known/doseedo-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/doseedo-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/doseedo-com/well-known/doseedo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doseedo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/doseedo-com/hosts/doseedo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doseedo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/doseedo-com/vendors/doseedo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doseedo-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://doseedo.com/help
- group: auth
  href: https://artifacts.apis.io/doseedo-com/security/doseedo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/doseedo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/doseedo-com/security/doseedo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doseedo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doseedo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doseedo.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://doseedo.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://doseedo.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://doseedo.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doseedo.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doseedo.com/privacy
coverage:
  checked: '2026-11-06'
  detail: Documentation is a JavaScript-rendered site with no accessible OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://doseedo.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Doseedo provides a session suite for music creators, offering tools to convert, separate, transcribe, and edit audio sessions across popular DAWs. Users can convert audio files into stems, extract MIDI, and remix tracks using web‑based and desktop applications. The platform includes a studio environment, film‑scoring tools, and a pricing model with free credits and paid plans, supporting multiple languages and platforms.
image: https://doseedo.com/og/home.jpg
json_schemas:
- name: GetApiJobsIdEventsResponse
  property_count: 1
  slug: doseedo-com-get-api-jobs-id-events-response
- name: GetApiJobsIdResponse
  property_count: 4
  slug: doseedo-com-get-api-jobs-id-response
- name: GetApiJobsKindsRenderMidiResponse
  property_count: 1
  slug: doseedo-com-get-api-jobs-kinds-render-midi-response
- name: PostApiJobsRequest
  property_count: 2
  slug: doseedo-com-post-api-jobs-request
jsonld:
- class_count: 4
  name: Doseedo Com Context
  property_count: 6
  slug: doseedo-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.doseedo.com.
  name: Doseedo MCP Server
  slug: doseedo-com-mcp-yml
modified: '2026-11-05'
name: Doseedo
nav: Providers
network: true
overview: 'Doseedo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Audio, Production, and Tools.


  The Doseedo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Doseedo''s developer surface includes support, documentation, pricing, engineering blog, signup flow, and 19 more developer resources.'
plans:
- name: Doseedo Com Plans Pricing
  plan_count: 4
  slug: doseedo-com-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Doseedo API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: doseedo-com-rules
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 21.4
    developer_ergonomics: 16.7
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doseedo Com Domain Security
  slug: doseedo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Doseedo Com Vulnerability Disclosure
  slug: doseedo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: doseedo-com
tags:
- Company
- Music
- Audio
- Production
- Tools
- Software-as-a-Service
website: https://doseedo.com/
---
