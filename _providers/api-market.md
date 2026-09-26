---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-09-25'
api_count: 1
apis:
- baseURL: https://prod.api.market
  baseurl_source: declared
  description: 'API.market API as documented publicly: 77 operations. Contract generated from the documentation by API Evangelist (2026-09-25); not the provider''s own document.'
  name: API.market API
  slug: api-market-api
artifact_total: 10
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/overlays/api-market-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/api-market-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/rules/api-market-rules.yml
  title: ''
  type: Spectral
  url: rules/api-market-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/json-ld/api-market-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/api-market-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/vocabulary/api-market-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/api-market-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/data-model/api-market-data-model.yml
  title: ''
  type: DataModel
  url: data-model/api-market-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/errors/api-market-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/api-market-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/conformance/api-market-conformance.yml
  title: ''
  type: Conformance
  url: conformance/api-market-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/llms/api-market-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/api-market-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/well-known/api-market-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/api-market-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/hosts/api-market-hosts.yml
  title: ''
  type: Hosts
  url: hosts/api-market-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/vendors/api-market-vendors.yml
  title: ''
  type: Vendors
  url: vendors/api-market-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.market/terms_of_service
- group: auth
  title: ''
  type: Security
  url: https://api.market/category/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.market/privacy_policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Noveum
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/api-market/refs/heads/main/security/api-market-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/api-market-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.market/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.market/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.market/api.market-usage-api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.market/getting-started
- group: company
  title: ''
  type: Blog
  url: https://api.market/blog
- group: operate
  title: ''
  type: Support
  url: https://api.market/contact
- group: start
  title: ''
  type: SignUp
  url: https://api.market/auth/login
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  reason: no-developer-program
  state: unreadable
created: '2026-09-25'
description: API.market is a marketplace platform that aggregates and sells access to a wide variety of APIs and AI models. It offers developers a single MCP (Multi-Channel Platform) connection to discover, subscribe, and integrate over 590 APIs across categories like image editing, video generation, mapping, and data intelligence. The platform provides tools for subscription management, usage analytics, and payment handling, aiming to simplify API consumption for both sellers and buyers. API.market also features a seller console for API providers to list their products, set pricing plans, and manage deployments, fostering a vibrant ecosystem of API services.
image: https://api.market/images/seo-cover.png
json_schemas:
- name: GetApiV1MagicapiWhisperWhisperResponse
  property_count: 11
  slug: api-market-get-api-v1-magicapi-whisper-whisper-response
- name: GetApiV1PipfeedParseExtractResponse
  property_count: 13
  slug: api-market-get-api-v1-pipfeed-parse-extract-response
- name: PostApiV1MagicapiAiqrcodePredictionsRequest
  property_count: 1
  slug: api-market-post-api-v1-magicapi-aiqrcode-predictions-request
- name: PostApiV1MagicapiUpscalerUpscale2XResponse
  property_count: 10
  slug: api-market-post-api-v1-magicapi-upscaler-upscale2-xresponse
- name: PostApiV1MagicapiWhisperWhisperRequest
  property_count: 11
  slug: api-market-post-api-v1-magicapi-whisper-whisper-request
- name: PostPipfeedParseExtractResponse
  property_count: 13
  slug: api-market-post-pipfeed-parse-extract-response
jsonld:
- class_count: 92
  name: Api Market Context
  property_count: 113
  slug: api-market-context
layout: provider
modified: '2026-09-25'
name: API.market
nav: Providers
network: true
overview: 'API.market publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Artificial Intelligence, Integration, and MCP.


  The API.market catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  API.market''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, and 18 more developer resources.'
random_paper: 13
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: API.market API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: api-market-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 20.6
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Api Market Domain Security
  slug: api-market-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: api-market
tags:
- Company
- Marketplace
- Artificial Intelligence
- Integration
- MCP
website: https://api.market/
---
