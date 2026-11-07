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
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://proxy.atlasburn.com
  baseurl_source: declared
  description: 'atlasburn-com API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: atlasburn-com API
  slug: atlasburn-com-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/atlasburn-com/rules/atlasburn-com-rules.yml
  title: ''
  type: Spectral
  url: rules/atlasburn-com-rules.yml
- group: design
  href: https://artifacts.apis.io/atlasburn-com/json-ld/atlasburn-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/atlasburn-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/atlasburn-com/vocabulary/atlasburn-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atlasburn-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/atlasburn-com/data-model/atlasburn-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atlasburn-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/atlasburn-com/cli/atlasburn-com-cli.yml
  title: ''
  type: CLI
  url: cli/atlasburn-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/atlasburn-com/changelog/atlasburn-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/atlasburn-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/atlasburn-com/conformance/atlasburn-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atlasburn-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/atlasburn-com/llms/atlasburn-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlasburn-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/atlasburn-com/well-known/atlasburn-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlasburn-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/atlasburn-com/hosts/atlasburn-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlasburn-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/atlasburn-com/vendors/atlasburn-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlasburn-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/atlasburn-com/packages/atlasburn-com-packages.yml
  title: ''
  type: Packages
  url: packages/atlasburn-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atlasburn.com/terms
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@atlasburn/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlasburn.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlasburn
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.atlasburn.com/docs/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.atlasburn.com/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/atlasburn-com/security/atlasburn-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlasburn-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlasburn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atlasburn.com/
- group: company
  title: ''
  type: Blog
  url: https://atlasburn.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.atlasburn.com/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://atlasburn.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://atlasburn.com/contact
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are served as a JavaScript SPA, providing no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.atlasburn.com/docs/api-reference/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: AtlasBurn provides an AI capital risk engine that monitors and controls AI/LLM API costs in real time. It tracks usage across providers like OpenAI, Anthropic, and Gemini, forecasts spend, and enforces budget guardrails to prevent runaway costs. The platform offers dashboards, alerts, and SDKs for developers to integrate cost management into their applications.
image: https://storage.googleapis.com/gpt-engineer-file-uploads/TXzjpANWp2UK439omIkwUvv2OuD3/social-images/social-1774972780366-AtlasBurn_Inverted_Color_2400x1800.webp
json_schemas:
- name: PostApiGuardrailsEnforceRequest
  property_count: 7
  slug: atlasburn-com-post-api-guardrails-enforce-request
- name: PostApiGuardrailsEnforceResponse
  property_count: 3
  slug: atlasburn-com-post-api-guardrails-enforce-response
- name: PostApiIngestRequest
  property_count: 9
  slug: atlasburn-com-post-api-ingest-request
- name: PostApiIngestResponse
  property_count: 2
  slug: atlasburn-com-post-api-ingest-response
- name: PostOpenaiV1ChatCompletionsRequest
  property_count: 2
  slug: atlasburn-com-post-openai-v1-chat-completions-request
jsonld:
- class_count: 5
  name: Atlasburn Com Context
  property_count: 13
  slug: atlasburn-com-context
layout: provider
modified: '2026-10-30'
name: atlasburn-com
nav: Providers
network: true
overview: 'atlasburn-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Cost Management, Monitoring, and SDK.


  The atlasburn-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  atlasburn-com''s developer surface includes CLI, changelog, API reference, documentation, engineering blog, getting-started guide, pricing, and 18 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: atlasburn-com API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: atlasburn-com-rules
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 15.8
    contract_governance: 19.7
    contract_quality: 26.0
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 35.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/atlasburn-com/atlasburn-com-2026-11-03T121451.png
security:
- kind: domain-security
  name: Atlasburn Com Domain Security
  slug: atlasburn-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atlasburn-com
tags:
- Company
- Artificial Intelligence
- Cost Management
- Monitoring
- SDK
website: https://atlasburn.com/
---
