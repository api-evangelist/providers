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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Aard Ai Agentic Access
  operation_count: 5
  slug: aard-ai-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.aard.ai
  baseurl_source: declared
  description: Unauthenticated status endpoints.
  name: Aard Status API
  slug: aard-ai-status-api
- baseURL: https://api.aard.ai
  baseurl_source: declared
  description: The four REST tools. POST only; one flat JSON object per call.
  name: Aard Tools API
  slug: aard-ai-tools-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/aard-ai/agentic-access/aard-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aard-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/aard-ai/plans/aard-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aard-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aard-ai/rules/aard-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/aard-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/aard-ai/json-ld/aard-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aard-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/aard-ai/vocabulary/aard-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aard-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aard-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aard-ai/data-model/aard-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aard-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/aard-ai/authentication/aard-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aard-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/aard-ai/errors/aard-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aard-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aard-ai/conformance/aard-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aard-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aard-ai/llms/aard-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aard-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/aard-ai/well-known/aard-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aard-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/aard-ai/well-known/aard-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aard-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/aard-ai/hosts/aard-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aard-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/aard-ai/vendors/aard-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aard-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://aard.ai/security
- group: start
  title: ''
  type: Login
  url: https://aard.ai/signin
- group: auth
  href: https://artifacts.apis.io/aard-ai/security/aard-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aard-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aard-ai/security/aard-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aard-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aard.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://aard.ai/docs/mcp-oauth
- group: docs
  title: ''
  type: APIReference
  url: https://aard.ai/macro
- group: operate
  title: ''
  type: Support
  url: https://aard.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://aard.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aard.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aard.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aard-ai
created: '2026-10-31'
description: Aard provides an MCP server and API delivering macroeconomic data and official statistics, enabling organisations to build AI workflows powered by real-world data. The platform offers macro data endpoints, pricing plans, and comprehensive documentation for developers to integrate grounded intelligence into large language models.
image: https://aard.ai/aard_logo.png
json_schemas:
- name: AskRequest
  property_count: 16
  slug: aard-ai-ask-request
- name: BuildUrlRequest
  property_count: 8
  slug: aard-ai-build-url-request
- name: DiscoverRequest
  property_count: 9
  slug: aard-ai-discover-request
- name: Health
  property_count: 2
  slug: aard-ai-health
- name: InspectRequest
  property_count: 3
  slug: aard-ai-inspect-request
- name: ToolSuccess
  property_count: 5
  slug: aard-ai-tool-success
jsonld:
- class_count: 7
  name: Aard Ai Context
  property_count: 34
  slug: aard-ai-context
layout: provider
modified: '2026-10-31'
name: Aard
nav: Providers
network: true
overview: 'Aard publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Status API and Tools API. Tagged areas include Artificial Intelligence, Data, Macroeconomics, and MCP.


  The Aard catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aard''s developer surface includes authentication, documentation, API reference, support, pricing, and 22 more developer resources.'
plans:
- name: Aard Ai Plans Pricing
  plan_count: 4
  slug: aard-ai-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Aard API Rules
  rule_count: 18
  severity_counts:
    error: 13
    hint: 0
    info: 4
    warn: 1
  slug: aard-ai-rules
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 66.0
    developer_ergonomics: 29.0
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aard Ai Authentication
  slug: aard-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aard Ai Domain Security
  slug: aard-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aard Ai Vulnerability Disclosure
  slug: aard-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: aard
  slug: aard-ai-aard
slug: aard-ai
tags:
- Artificial Intelligence
- Data
- Macroeconomics
- MCP
website: https://aard.ai/
---
