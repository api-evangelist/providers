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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Reachable endpoints an agent can call directly, including NLWeb /ask and public read‑only docs MCP.
  name: Aeon Agent API
  slug: aeon-agent-api
- baseURL: https://www.aeon.fun/v1
  baseurl_source: declared
  description: 'Reachable endpoints an agent can call directly: the NLWeb /ask natural-language query endpoint, the public read-only aeon docs MCP server (Streamable HTTP at /mcp), POST /api/feedback for reporting wh'
  name: aeon agent-facing API API
  slug: aeon-agent-facing-api-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/aeon-fun/rules/aeon-fun-rules.yml
  title: ''
  type: Spectral
  url: rules/aeon-fun-rules.yml
- group: design
  href: https://artifacts.apis.io/aeon-fun/json-ld/aeon-fun-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aeon-fun-context.jsonld
- group: design
  href: https://artifacts.apis.io/aeon-fun/vocabulary/aeon-fun-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aeon-fun-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aeon-fun/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aeon-fun/data-model/aeon-fun-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aeon-fun-data-model.yml
- group: operate
  href: https://artifacts.apis.io/aeon-fun/changelog/aeon-fun-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aeon-fun-changelog.yml
- group: auth
  href: https://artifacts.apis.io/aeon-fun/authentication/aeon-fun-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aeon-fun-authentication.yml
- group: design
  href: https://artifacts.apis.io/aeon-fun/errors/aeon-fun-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aeon-fun-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aeon-fun/conformance/aeon-fun-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aeon-fun-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aeon-fun/llms/aeon-fun-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aeon-fun-llms.txt
- group: build
  href: https://artifacts.apis.io/aeon-fun/mcp/aeon-fun-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aeon-fun-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aeon-fun/mcp/aeon-fun-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aeon-fun-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aeon-fun/well-known/aeon-fun-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aeon-fun-security.txt
- group: auth
  href: https://artifacts.apis.io/aeon-fun/well-known/aeon-fun-aeon-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aeon-fun-aeon-security.txt
- group: agent
  href: https://artifacts.apis.io/aeon-fun/well-known/aeon-fun-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aeon-fun-well-known.yml
- group: other
  href: https://artifacts.apis.io/aeon-fun/hosts/aeon-fun-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aeon-fun-hosts.yml
- group: other
  href: https://artifacts.apis.io/aeon-fun/vendors/aeon-fun-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aeon-fun-vendors.yml
- group: build
  href: https://artifacts.apis.io/aeon-fun/packages/aeon-fun-packages.yml
  title: ''
  type: SDKs
  url: packages/aeon-fun-packages.yml
- group: build
  href: https://artifacts.apis.io/aeon-fun/packages/aeon-fun-packages.yml
  title: ''
  type: Packages
  url: packages/aeon-fun-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aeon.fun/terms
- group: auth
  title: ''
  type: Security
  url: https://www.aeon.fun/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aeon.fun/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.aeon.fun/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aeon.fun/developers
- group: company
  title: ''
  type: Blog
  url: https://www.aeon.fun/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.aeon.fun/changelog
- group: auth
  href: https://artifacts.apis.io/aeon-fun/security/aeon-fun-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aeon-fun-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aeon-fun/security/aeon-fun-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aeon-fun-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aeon.fun/
created: '2026-10-31'
description: Aeon provides an autonomous agent framework that enables developers to configure once and let the system execute complex workflows across 87 built‑in skills. Open‑source and MIT‑licensed, it integrates with major AI models and cloud services, targeting enterprises and developers seeking to automate decision‑making without manual approval loops. The platform showcases use cases from Harvard, Deloitte, Accenture, and leading tech firms, emphasizing scalability, extensibility, and self‑healing capabilities.
image: https://www.aeon.fun/og-image.jpg
json_schemas:
- name: AgentSkillsIndex
  property_count: 2
  slug: aeon-fun-agent-skills-index
- name: AiCatalog
  property_count: 3
  slug: aeon-fun-ai-catalog
- name: ApiCatalog
  property_count: 1
  slug: aeon-fun-api-catalog
- name: FeedbackDescriptor
  property_count: 8
  slug: aeon-fun-feedback-descriptor
- name: FeedbackRequest
  property_count: 7
  slug: aeon-fun-feedback-request
- name: McpServerCard
  property_count: 17
  slug: aeon-fun-mcp-server-card
jsonld:
- class_count: 16
  name: Aeon Fun Context
  property_count: 48
  slug: aeon-fun-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.aeon.fun.
  name: Aeon MCP Server
  slug: aeon-fun-mcp-yml
modified: '2026-10-31'
name: Aeon
nav: Providers
network: true
overview: 'Aeon publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including agent-facing API API, and 1 more. Tagged areas include Artificial Intelligence, Automation, Open Source, Framework, and Enterprise.


  The Aeon catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aeon''s developer surface includes changelog, authentication, documentation, engineering blog, API reference, and 24 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Aeon API Rules
  rule_count: 55
  severity_counts:
    error: 51
    hint: 0
    info: 3
    warn: 1
  slug: aeon-fun-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 55.2
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 43.1
  provenance:
    conformance: derived
    mcp: first-party
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
  name: Aeon Fun Authentication
  slug: aeon-fun-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Aeon Fun Domain Security
  slug: aeon-fun-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aeon Fun Vulnerability Disclosure
  slug: aeon-fun-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: ask
  slug: aeon-fun-ask
slug: aeon-fun
tags:
- Artificial Intelligence
- Automation
- Open Source
- Framework
- Enterprise
website: https://aeon.fun/
---
