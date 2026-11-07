---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Oruk Ai Agentic Access
  operation_count: 19
  slug: oruk-ai-agentic-access
  summary_line: 19 operations · 12 acting
api_count: 1
apis:
- description: oruk Speech API providing transcription, emotion detection, speaking style analysis, and proficiency scoring.
  name: Speech API
  slug: speech-api
- baseURL: https://speech-api.oruk.ai
  baseurl_source: declared
  description: The Affect API from oruk-ai — 2 operation(s) for affect.
  name: oruk-ai Affect API
  slug: oruk-ai-affect-api
- baseURL: https://speech-api.oruk.ai
  baseurl_source: declared
  description: The Audio API from oruk-ai — 8 operation(s) for audio.
  name: oruk-ai Audio API
  slug: oruk-ai-audio-api
- baseURL: https://speech-api.oruk.ai
  baseurl_source: declared
  description: The Client Token API from oruk-ai — 1 operation(s) for client token.
  name: oruk-ai Client Token API
  slug: oruk-ai-client-token-api
- baseURL: https://speech-api.oruk.ai
  baseurl_source: declared
  description: The Livez API from oruk-ai — 1 operation(s) for livez.
  name: oruk-ai Livez API
  slug: oruk-ai-livez-api
- baseURL: https://speech-api.oruk.ai
  baseurl_source: declared
  description: The Models API from oruk-ai — 2 operation(s) for models.
  name: oruk-ai Models API
  slug: oruk-ai-models-api
- baseURL: https://speech-api.oruk.ai
  baseurl_source: declared
  description: The OrukZero API from oruk-ai — 2 operation(s) for orukzero.
  name: oruk-ai Oruk Zero API
  slug: oruk-ai-orukzero-api
- baseURL: https://speech-api.oruk.ai
  baseurl_source: declared
  description: The Pricing API from oruk-ai — 1 operation(s) for pricing.
  name: oruk-ai Pricing API
  slug: oruk-ai-pricing-api
- baseURL: https://speech-api.oruk.ai
  baseurl_source: declared
  description: The Readyz API from oruk-ai — 1 operation(s) for readyz.
  name: oruk-ai Readyz API
  slug: oruk-ai-readyz-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/oruk-ai/agentic-access/oruk-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/oruk-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/oruk-ai/plans/oruk-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/oruk-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/oruk-ai/rules/oruk-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/oruk-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/oruk-ai/json-ld/oruk-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oruk-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/oruk-ai/vocabulary/oruk-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/oruk-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/oruk-ai/data-model/oruk-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/oruk-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/oruk-ai/changelog/oruk-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/oruk-ai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://oruk.ai/security
- group: design
  href: https://artifacts.apis.io/oruk-ai/errors/oruk-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/oruk-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/oruk-ai/conformance/oruk-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/oruk-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/oruk-ai/llms/oruk-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oruk-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/oruk-ai/mcp/oruk-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/oruk-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/oruk-ai/well-known/oruk-ai-speech-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/oruk-ai-speech-api-security.txt
- group: auth
  href: https://artifacts.apis.io/oruk-ai/well-known/oruk-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/oruk-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/oruk-ai/well-known/oruk-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/oruk-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/oruk-ai/hosts/oruk-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oruk-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/oruk-ai/vendors/oruk-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oruk-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/oruk-ai/packages/oruk-ai-packages.yml
  title: ''
  type: Packages
  url: packages/oruk-ai-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://oruk.ai/status
- group: auth
  title: ''
  type: Security
  url: https://oruk.ai/security
- group: build
  title: ''
  type: SDKs
  url: https://oruk.ai/sdk/oruk-ai-sdk-0.2.15.tgz
- group: start
  title: ''
  type: Login
  url: https://oruk.ai/auth/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://oruk.ai/changelog
- group: auth
  href: https://artifacts.apis.io/oruk-ai/authentication/oruk-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/oruk-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/oruk-ai/security/oruk-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/oruk-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/oruk-ai/security/oruk-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/oruk-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/oruk-ai/security/oruk-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oruk-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oruk.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://oruk.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://oruk.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://oruk.ai/docs#quickstart
- group: operate
  title: ''
  type: Support
  url: https://oruk.ai/#contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Oruk-AI
- group: commercial
  title: ''
  type: Pricing
  url: https://oruk.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oruk.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oruk.ai/privacy
created: '2026-10-30'
description: Oruk AI provides speech understanding APIs that enable transcription and vocal delivery analysis for both recorded audio and live speech. Their platform supports multiple languages and offers various output formats tailored to developers integrating speech AI into applications such as voice assistants, call analytics, and content creation tools. The service emphasizes low latency, high accuracy models, and flexible pricing options for different usage scales.
image: https://oruk.ai/brand/web/2026-09-09-light-signal/home.png
jsonld:
- class_count: 27
  name: Oruk Ai Context
  property_count: 112
  slug: oruk-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at oruk.ai.
  name: oruk-ai MCP Server
  slug: oruk-ai-mcp-yml
modified: '2026-10-30'
name: oruk-ai
nav: Providers
network: true
overview: 'oruk-ai publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Affect API, Audio API, Client Token API, and 6 more. Tagged areas include Company, Speech, Artificial Intelligence, Transcription, and Voice.


  The oruk-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  oruk-ai''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, pricing, and 29 more developer resources.'
plans:
- name: Oruk Ai Plans Pricing
  plan_count: 4
  slug: oruk-ai-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: oruk-ai API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 1
  slug: oruk-ai-rules
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.5
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 53.2
    developer_ergonomics: 35.7
    discoverability: 65.0
    operational_transparency: 23.7
  previous_composite: 60.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/oruk-ai/oruk-ai-2026-11-03T140740.png
security:
- kind: authentication
  name: Oruk Ai Authentication
  slug: oruk-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Oruk Ai Domain Security
  slug: oruk-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oruk Ai Vulnerability Disclosure
  slug: oruk-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Oruk Ai Trust Center
  slug: oruk-ai-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: oruk-ai
tags:
- Company
- Speech
- Artificial Intelligence
- Transcription
- Voice
website: https://oruk.ai/
---
