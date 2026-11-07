---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Lara is an adaptive translation AI platform offering translation, audio, document, and language detection APIs.
  name: Lara
  slug: lara
- description: 'ModernMT API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: ModernMT API
  slug: modernmt-api
artifact_total: 17
common:
- group: design
  href: https://artifacts.apis.io/modernmt/rules/modernmt-rules.yml
  title: ''
  type: Spectral
  url: rules/modernmt-rules.yml
- group: design
  href: https://artifacts.apis.io/modernmt/json-ld/modernmt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/modernmt-context.jsonld
- group: design
  href: https://artifacts.apis.io/modernmt/vocabulary/modernmt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/modernmt-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/modernmt/data-model/modernmt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/modernmt-data-model.yml
- group: build
  href: https://artifacts.apis.io/modernmt/cli/modernmt-cli.yml
  title: ''
  type: CLI
  url: cli/modernmt-cli.yml
- group: design
  href: https://artifacts.apis.io/modernmt/conformance/modernmt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/modernmt-conformance.yml
- group: agent
  href: https://artifacts.apis.io/modernmt/mcp/modernmt-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/modernmt-mcp.yml
- group: agent
  href: https://artifacts.apis.io/modernmt/well-known/modernmt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/modernmt-well-known.yml
- group: other
  href: https://artifacts.apis.io/modernmt/hosts/modernmt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/modernmt-hosts.yml
- group: other
  href: https://artifacts.apis.io/modernmt/vendors/modernmt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/modernmt-vendors.yml
- group: build
  href: https://artifacts.apis.io/modernmt/packages/modernmt-packages.yml
  title: ''
  type: SDKs
  url: packages/modernmt-packages.yml
- group: build
  href: https://artifacts.apis.io/modernmt/packages/modernmt-packages.yml
  title: ''
  type: Packages
  url: packages/modernmt-packages.yml
- group: start
  title: ''
  type: Login
  url: https://www.modernmt.com/login
- group: company
  title: ''
  type: Blog
  url: https://blog.modernmt.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.laratranslate.com/docs/switch-from-modernmt
- group: auth
  href: https://artifacts.apis.io/modernmt/security/modernmt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/modernmt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.modernmt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.laratranslate.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.laratranslate.com/docs/translation-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.laratranslate.com/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://laratranslate.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.modernmt.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.modernmt.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.laratranslate.com
coverage:
  checked: '2026-10-27'
  detail: Developer docs are served as HTML shells requiring JavaScript; no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://developers.laratranslate.com/docs/translation-api.md
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: ModernMT provides AI-powered translation services and is transitioning to Lara, a next‑generation translation platform. The company offers API access for text, document, image, and audio translation, supporting over 200 languages and various file formats. Existing ModernMT API keys remain valid until the end of 2026, after which users are encouraged to migrate to Lara for enhanced quality and new features.
image: https://www.modernmt.com/assets/images/cover/MMT-og-1-min.png
json_schemas:
- name: GetContextVectorResponse
  property_count: 2
  slug: modernmt-get-context-vector-response
- name: GetTranslateBatchResponse
  property_count: 2
  slug: modernmt-get-translate-batch-response
- name: GetTranslateDetectResponse
  property_count: 2
  slug: modernmt-get-translate-detect-response
- name: GetTranslateLanguagesResponse
  property_count: 2
  slug: modernmt-get-translate-languages-response
- name: GetTranslateResponse
  property_count: 2
  slug: modernmt-get-translate-response
- name: PostRequest
  property_count: 5
  slug: modernmt-post-request
- name: PostResponse
  property_count: 2
  slug: modernmt-post-response
jsonld:
- class_count: 19
  name: Modernmt Context
  property_count: 12
  slug: modernmt-context
layout: provider
mcp_servers:
- description: Remote MCP server at developers.laratranslate.com.
  name: ModernMT MCP Server
  slug: modernmt-mcp-yml
modified: '2026-10-27'
name: ModernMT
nav: Providers
network: true
overview: 'ModernMT is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Translation, and Multilingual.


  The ModernMT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ModernMT''s developer surface includes CLI, engineering blog, documentation, API reference, getting-started guide, pricing, support, and 17 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ModernMT API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: modernmt-rules
scopes:
- name: Modernmt Scopes
  scope_count: 0
  slug: modernmt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 26.8
    developer_ergonomics: 36.9
    discoverability: 51.7
    operational_transparency: 0.0
  previous_composite: 38.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/modernmt/modernmt-2026-11-03T135747.png
security:
- kind: authentication
  name: Modernmt Authentication
  slug: modernmt-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Modernmt Domain Security
  slug: modernmt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: get-modernmt
  slug: modernmt-get-modernmt-skill
- name: translate-batch
  slug: modernmt-post-skill
slug: modernmt
tags:
- Company
- Artificial Intelligence
- Translation
- Multilingual
website: https://www.modernmt.com/
---
