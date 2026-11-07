---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Provides AI‑driven marketing automation via a remote MCP server; documented in the AutoWhisper developer portal.
  name: AutoWhisper API
  slug: autowhisper-api
- description: 'AutoWhisper API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: AutoWhisper API
  slug: autowhisper-xyz-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/autowhisper-xyz/rules/autowhisper-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/autowhisper-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/autowhisper-xyz/json-ld/autowhisper-xyz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/autowhisper-xyz-context.jsonld
- group: design
  href: https://artifacts.apis.io/autowhisper-xyz/vocabulary/autowhisper-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/autowhisper-xyz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/autowhisper-xyz/data-model/autowhisper-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/autowhisper-xyz-data-model.yml
- group: design
  href: https://artifacts.apis.io/autowhisper-xyz/conformance/autowhisper-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autowhisper-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/autowhisper-xyz/llms/autowhisper-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autowhisper-xyz-llms.txt
- group: agent
  href: https://artifacts.apis.io/autowhisper-xyz/well-known/autowhisper-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autowhisper-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/autowhisper-xyz/hosts/autowhisper-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autowhisper-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/autowhisper-xyz/vendors/autowhisper-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autowhisper-xyz-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://autowhisper.xyz/en/playbook/quickstart
- group: auth
  href: https://artifacts.apis.io/autowhisper-xyz/security/autowhisper-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autowhisper-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autowhisper.xyz/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autowhisper.xyz/en/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autowhisper.xyz/en/terms
coverage:
  checked: '2026-11-02'
  detail: Public documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 404
    url: https://autowhisper.xyz/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: AutoWhisper offers an AI-powered marketing agent for e‑commerce businesses, acting as an AI Chief Marketing Officer. It learns a product’s details, analyzes competitor content, and generates multilingual, platform‑specific marketing posts that avoid obvious AI signatures. Users can review drafts, connect publishing accounts, and automate daily content creation across TikTok, Instagram, Facebook, LinkedIn, YouTube, Pinterest, Threads, and Bluesky. Pricing starts at $30 per month with a free trial credit. The service emphasizes ease of setup, no credit‑card required, and supports both SaaS and agency workflows.
image: https://autowhisper.xyz/assets/how_it_works/hero-084e160b.png
json_schemas:
- name: GetApiContractResponse
  property_count: 3
  slug: autowhisper-xyz-get-api-contract-response
- name: PostApiCmoMessageRequest
  property_count: 3
  slug: autowhisper-xyz-post-api-cmo-message-request
- name: PostApiProductsSummaryResponse
  property_count: 3
  slug: autowhisper-xyz-post-api-products-summary-response
- name: PostDeviceCodeRequest
  property_count: 1
  slug: autowhisper-xyz-post-device-code-request
- name: PostDeviceCodeResponse
  property_count: 4
  slug: autowhisper-xyz-post-device-code-response
- name: PostDeviceTokenResponse
  property_count: 2
  slug: autowhisper-xyz-post-device-token-response
jsonld:
- class_count: 8
  name: Autowhisper Xyz Context
  property_count: 16
  slug: autowhisper-xyz-context
layout: provider
modified: '2026-11-02'
name: AutoWhisper
nav: Providers
network: true
overview: 'AutoWhisper is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, E-Commerce, Content Generation, and Automation.


  The AutoWhisper catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AutoWhisper''s developer surface includes getting-started guide and 13 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 0
  name: Autowhisper Xyz Rate Limits
  slug: autowhisper-xyz-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: AutoWhisper API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: autowhisper-xyz-rules
scopes:
- name: Autowhisper Xyz Scopes
  scope_count: 0
  slug: autowhisper-xyz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 23.7
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
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Autowhisper Xyz Authentication
  slug: autowhisper-xyz-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Autowhisper Xyz Domain Security
  slug: autowhisper-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autowhisper-xyz
tags:
- Artificial Intelligence
- Marketing
- E-Commerce
- Content Generation
- Automation
website: https://autowhisper.xyz/
---
