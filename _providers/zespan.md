---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for Zespan AI agent reliability platform
  name: Zespan API
  slug: zespan-api-2
- baseURL: https://api.zespan.com
  baseurl_source: declared
  description: 'Zespan API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Zespan API
  slug: zespan-api
artifact_total: 14
asyncapis:
- description: ''
  name: Zespan Webhooks
  slug: zespan-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/zespan/plans/zespan-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zespan-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/zespan/rules/zespan-rules.yml
  title: ''
  type: Spectral
  url: rules/zespan-rules.yml
- group: design
  href: https://artifacts.apis.io/zespan/json-ld/zespan-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zespan-context.jsonld
- group: design
  href: https://artifacts.apis.io/zespan/vocabulary/zespan-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zespan-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/zespan/asyncapi/zespan-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/zespan-webhooks.yml
- group: design
  href: https://artifacts.apis.io/zespan/data-model/zespan-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zespan-data-model.yml
- group: auth
  href: https://artifacts.apis.io/zespan/authentication/zespan-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zespan-authentication.yml
- group: design
  href: https://artifacts.apis.io/zespan/conformance/zespan-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zespan-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zespan/llms/zespan-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zespan-llms.txt
- group: other
  href: https://artifacts.apis.io/zespan/a2a/zespan-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/zespan-a2a.yml
- group: agent
  href: https://artifacts.apis.io/zespan/well-known/zespan-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zespan-well-known.yml
- group: other
  href: https://artifacts.apis.io/zespan/hosts/zespan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zespan-hosts.yml
- group: other
  href: https://artifacts.apis.io/zespan/vendors/zespan-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zespan-vendors.yml
- group: build
  href: https://artifacts.apis.io/zespan/packages/zespan-packages.yml
  title: ''
  type: SDKs
  url: packages/zespan-packages.yml
- group: build
  href: https://artifacts.apis.io/zespan/packages/zespan-packages.yml
  title: ''
  type: Packages
  url: packages/zespan-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zespan.com/
- group: start
  title: ''
  type: Sandbox
  url: https://zespan.com/features/playground
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Zespan
- group: auth
  href: https://artifacts.apis.io/zespan/security/zespan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zespan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zespan.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zespan.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zespan.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zespan.com/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://zespan.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://zespan.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.zespan.com/auth/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.zespan.com/auth/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zespan.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zespan.com/privacy-policy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.zespan.com/mcp
  - status: 401
    url: https://app.zespan.com/api/mcp
  - status: 401
    url: https://api.zespan.com/mcp
  - status: 200
    url: https://zespan.com/
  reason: partner-login
  state: gated
created: '2026-10-19'
description: Zespan provides AI agent reliability tooling that detects and prevents silent mistakes in production AI agents. It offers guardrails, monitoring, tracing, evaluation, and cost management across major LLM providers. Users can self‑host or use a SaaS version, integrating with OpenAI, Anthropic, Google Gemini, AWS Bedrock, LangChain, CrewAI, and more, to ensure AI agents behave as intended.
image: https://zespan.com/dashboard.png
json_schemas:
- name: GetV1OrgsOrgidPoliciesResponse
  property_count: 3
  slug: zespan-get-v1-orgs-orgid-policies-response
- name: GetV1OrgsOrgidPolicyAppliesResponse
  property_count: 2
  slug: zespan-get-v1-orgs-orgid-policy-applies-response
- name: GetV1SdkConfigResponse
  property_count: 1
  slug: zespan-get-v1-sdk-config-response
- name: PostV1PromptsNameVersionsVersionGateRequest
  property_count: 8
  slug: zespan-post-v1-prompts-name-versions-version-gate-request
- name: PostWebhooksZespanRequest
  property_count: 11
  slug: zespan-post-webhooks-zespan-request
- name: PostWebhooksZespanResponse
  property_count: 1
  slug: zespan-post-webhooks-zespan-response
jsonld:
- class_count: 8
  name: Zespan Context
  property_count: 23
  slug: zespan-context
layout: provider
modified: '2026-10-19'
name: Zespan
nav: Providers
network: true
overview: 'Zespan is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Monitoring, Reliability, Agents, and Platform.


  The Zespan catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Zespan''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, pricing, engineering blog, and 22 more developer resources.'
plans:
- name: Zespan Plans Pricing
  plan_count: 5
  slug: zespan-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Zespan API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: zespan-rules
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.0
    catalog_earned_first_party: 12.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 19.7
    contract_quality: 33.7
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zespan Authentication
  slug: zespan-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zespan Domain Security
  slug: zespan-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: zespan
tags:
- Artificial Intelligence
- Monitoring
- Reliability
- Agents
- Platform
website: https://zespan.com/
---
