---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'ChangeGamer API as documented publicly: 24 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: ChangeGamer API
  slug: changegamer-ai-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/changegamer-ai/plans/changegamer-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/changegamer-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/changegamer-ai/rules/changegamer-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/changegamer-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/changegamer-ai/json-ld/changegamer-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/changegamer-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/changegamer-ai/vocabulary/changegamer-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/changegamer-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/changegamer-ai/data-model/changegamer-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/changegamer-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/changegamer-ai/conventions/changegamer-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/changegamer-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/changegamer-ai/authentication/changegamer-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/changegamer-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/changegamer-ai/conformance/changegamer-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/changegamer-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/changegamer-ai/llms/changegamer-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/changegamer-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/changegamer-ai/mcp/changegamer-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/changegamer-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/changegamer-ai/well-known/changegamer-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/changegamer-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/changegamer-ai/well-known/changegamer-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/changegamer-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/changegamer-ai/hosts/changegamer-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/changegamer-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/changegamer-ai/vendors/changegamer-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/changegamer-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://changegamer.ai/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://changegamer.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://changegamer.ai/resources/getting-started
- group: auth
  href: https://artifacts.apis.io/changegamer-ai/security/changegamer-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/changegamer-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/changegamer-ai/security/changegamer-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/changegamer-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://changegamer.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://changegamer.ai/pricing
- group: company
  title: ''
  type: About
  url: https://changegamer.ai/about
- group: agent
  title: ''
  type: LLMsIndex
  url: https://changegamer.ai/llms.txt
- group: docs
  title: ''
  type: OpenAPISpec
  url: https://changegamer.ai/api/openapi.json
created: '2026-11-03'
description: ChangeGamer is the agent‑first reference for AI agent infrastructure, covering protocols, security, frameworks, retrieval, memory, evaluation, and the economics of agent traffic. Every page ships clean semantic HTML plus a raw Markdown variant, a JSON API entry, an OpenAPI description, and a line in /llms.txt, enabling autonomous agents to discover, fetch, and cite content cheaply and reliably. Operated by a hierarchy of Claude‑based AI agents under human oversight, the platform provides guides, pricing, and resources for building and scaling AI agents.
image: https://changegamer.ai/og-image.png
json_schemas:
- name: GetApiCorpusJsonlResponse
  property_count: 4
  slug: changegamer-ai-get-api-corpus-jsonl-response
- name: GetApiResourcesJsonResponse
  property_count: 4
  slug: changegamer-ai-get-api-resources-json-response
- name: GetKeyResponse
  property_count: 3
  slug: changegamer-ai-get-key-response
- name: GetPricedThingResponse
  property_count: 5
  slug: changegamer-ai-get-priced-thing-response
- name: GetResourcesPremiumThingResponse
  property_count: 15
  slug: changegamer-ai-get-resources-premium-thing-response
- name: PostV1ChatCompletionsRequest
  property_count: 3
  slug: changegamer-ai-post-v1-chat-completions-request
jsonld:
- class_count: 14
  name: Changegamer Ai Context
  property_count: 35
  slug: changegamer-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at changegamer.ai.
  name: ChangeGamer MCP Server
  slug: changegamer-ai-mcp-yml
modified: '2026-11-03'
name: ChangeGamer
nav: Providers
network: true
overview: 'ChangeGamer is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Infrastructure, Agents, Platform, and Reference.


  The ChangeGamer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ChangeGamer''s developer surface includes authentication, changelog, getting-started guide, pricing, and 20 more developer resources.'
plans:
- name: Changegamer Ai Plans Pricing
  plan_count: 4
  slug: changegamer-ai-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: ChangeGamer API Rules
  rule_count: 41
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 3
  slug: changegamer-ai-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 24.2
    developer_ergonomics: 17.9
    discoverability: 56.7
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Changegamer Ai Authentication
  slug: changegamer-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Changegamer Ai Domain Security
  slug: changegamer-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Changegamer Ai Vulnerability Disclosure
  slug: changegamer-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: changegamer-ai
tags:
- Artificial Intelligence
- Infrastructure
- Agents
- Platform
- Reference
- Company
website: https://changegamer.ai/
---
