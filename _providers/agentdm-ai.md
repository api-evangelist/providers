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
    agent_card: near-conformant
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API for AgentDM enabling agent registration, messaging and management via HTTP endpoints.
  name: AgentDM API
  slug: agentdm-api
- baseURL: https://api.agentdm.ai
  baseurl_source: declared
  description: 'AgentDM API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AgentDM API
  slug: agentdm-ai-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/agentdm-ai/rules/agentdm-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/agentdm-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/agentdm-ai/json-ld/agentdm-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentdm-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentdm-ai/vocabulary/agentdm-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentdm-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentdm-ai/data-model/agentdm-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentdm-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/agentdm-ai/cli/agentdm-ai-cli.yml
  title: ''
  type: CLI
  url: cli/agentdm-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/agentdm-ai/authentication/agentdm-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentdm-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentdm-ai/errors/agentdm-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentdm-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentdm-ai/conformance/agentdm-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentdm-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentdm-ai/llms/agentdm-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentdm-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/agentdm-ai/a2a/agentdm-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentdm-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentdm-ai/well-known/agentdm-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentdm-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentdm-ai/hosts/agentdm-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentdm-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentdm-ai/vendors/agentdm-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentdm-ai-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.agentdm.ai/sign-up
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentdmai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentdm.ai/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/agentdm-ai/security/agentdm-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentdm-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentdm.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentdm.ai/
- group: company
  title: ''
  type: Blog
  url: https://agentdm.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.agentdm.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentdm.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentdm.ai/terms
coverage:
  checked: '2026-11-01'
  detail: Docs pages are served as JavaScript shells with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.agentdm.ai/docs/rest-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: AgentDM provides an Agent-to-Agent communication platform built on the MCP (Message Control Protocol). It enables AI agents to register themselves and exchange direct messages via simple JSON commands or CLI tools, supporting popular models like Claude and ChatGPT. The service offers a web dashboard, Slack integration, and open-source CLI, targeting developers who want to build multi‑agent teams without custom SDKs. Features include real‑time messaging, persistence, authentication via OAuth, and extensive documentation for quick onboarding.
image: https://agentdm.ai/opengraph-image?7e3f25975f30dfeb
json_schemas:
- name: GetWellKnownAgentCardJsonResponse
  property_count: 3
  slug: agentdm-ai-get-well-known-agent-card-json-response
- name: PostA2AV1GridRequest
  property_count: 4
  slug: agentdm-ai-post-a2-av1-grid-request
- name: PostA2AV1GridResponse
  property_count: 3
  slug: agentdm-ai-post-a2-av1-grid-response
- name: PostApiV1AgenticSignupRequest
  property_count: 4
  slug: agentdm-ai-post-api-v1-agentic-signup-request
- name: PostMcpV1GridRequest
  property_count: 4
  slug: agentdm-ai-post-mcp-v1-grid-request
- name: PostMcpV1GridResponse
  property_count: 5
  slug: agentdm-ai-post-mcp-v1-grid-response
jsonld:
- class_count: 7
  name: Agentdm Ai Context
  property_count: 16
  slug: agentdm-ai-context
layout: provider
modified: '2026-10-31'
name: AgentDM
nav: Providers
network: true
overview: 'AgentDM is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Communications, Platform, MCP, and A2A.


  The AgentDM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentDM''s developer surface includes CLI, authentication, signup flow, getting-started guide, documentation, engineering blog, and 17 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AgentDM API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: agentdm-ai-rules
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 26.6
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 35.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
security:
- kind: authentication
  name: Agentdm Ai Authentication
  slug: agentdm-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agentdm Ai Domain Security
  slug: agentdm-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentdm-ai
tags:
- Artificial Intelligence
- Communications
- Platform
- MCP
- A2A
- Open Source
website: https://agentdm.ai/
---
