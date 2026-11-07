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
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Averta runtime decision API.
  name: Averta Runtime Decision API
  slug: averta-runtime-decision-api
artifact_total: 7
asyncapis:
- description: ''
  name: Averta Io Webhooks
  slug: averta-io-webhooks
common:
- group: design
  href: https://artifacts.apis.io/averta-io/rules/averta-io-rules.yml
  title: ''
  type: Spectral
  url: rules/averta-io-rules.yml
- group: design
  href: https://artifacts.apis.io/averta-io/json-ld/averta-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/averta-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/averta-io/vocabulary/averta-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/averta-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/averta-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/averta-io/asyncapi/averta-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/averta-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/averta-io/data-model/averta-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/averta-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/averta-io/errors/averta-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/averta-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/averta-io/conformance/averta-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/averta-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/averta-io/llms/averta-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/averta-io-llms.txt
- group: other
  href: https://artifacts.apis.io/averta-io/a2a/averta-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/averta-io-a2a.yml
- group: build
  href: https://artifacts.apis.io/averta-io/mcp/averta-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/averta-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/averta-io/mcp/averta-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/averta-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/averta-io/well-known/averta-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/averta-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/averta-io/hosts/averta-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/averta-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/averta-io/vendors/averta-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/averta-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://averta.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://averta.io/privacy
- group: auth
  href: https://artifacts.apis.io/averta-io/security/averta-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/averta-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://averta.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.averta.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.averta.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.averta.io/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.averta.io/demo
- group: company
  title: ''
  type: Blog
  url: https://www.averta.io/blog
coverage:
  checked: '2026-11-02'
  detail: The provider’s documentation does not publish any machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://docs.averta.io/api-reference/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Averta provides an agentic AI security platform, the AI Agent Operating System, which classifies, governs, and audits every prompt, tool call, and action to ensure safe execution of enterprise AI agents. The operating system offers comprehensive controls, policy enforcement, and audit trails for AI workloads, helping organizations mitigate risks associated with advanced language models.
image: https://averta.io/assets/og.png
jsonld:
- class_count: 2
  name: Averta Io Context
  property_count: 4
  slug: averta-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.averta.io.
  name: Averta MCP Server
  slug: averta-io-mcp-yml
modified: '2026-11-02'
name: Averta
nav: Providers
network: true
overview: 'Averta publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Security, AI Agents, Enterprise, and Platform.


  The Averta catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Averta''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 20 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Averta API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: averta-io-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 45.5
    developer_ergonomics: 26.7
    discoverability: 65.0
    operational_transparency: 7.9
  previous_composite: 36.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
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
- kind: domain-security
  name: Averta Io Domain Security
  slug: averta-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: averta
  slug: averta-io-averta
slug: averta-io
tags:
- Artificial Intelligence
- Security
- AI Agents
- Enterprise
- Platform
website: https://averta.io/
---
