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
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 62.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 54
  human_in_the_loop: 17
  name: Agentdrives Com Agentic Access
  operation_count: 103
  slug: agentdrives-com-agentic-access
  summary_line: 103 operations · 54 acting · 17 human-in-the-loop
api_count: 1
apis:
- baseURL: https://agentdrives.com
  baseurl_source: declared
  description: Sign in, API keys, agent accounts and your account
  name: agentdrives-com Accounts API
  slug: agentdrives-com-accounts-api
- baseURL: https://agentdrives.com
  baseurl_source: declared
  description: Claim and prove your product's domain
  name: agentdrives-com Claims API
  slug: agentdrives-com-claims-api
- baseURL: https://agentdrives.com
  baseurl_source: declared
  description: 'The products our agent drove: search, categories, capabilities, levels, the data explorer and the evidence'
  name: agentdrives-com Directory API
  slug: agentdrives-com-directory-api
- baseURL: https://agentdrives.com
  baseurl_source: declared
  description: 'Hear when a tool''s level changes: follows and the webhook'
  name: agentdrives-com Follows API
  slug: agentdrives-com-follows-api
- baseURL: https://agentdrives.com
  baseurl_source: declared
  description: The monthly report by email
  name: agentdrives-com Newsletter API
  slug: agentdrives-com-newsletter-api
- baseURL: https://agentdrives.com
  baseurl_source: declared
  description: Order, pay and manage drives and plans
  name: agentdrives-com Orders API
  slug: agentdrives-com-orders-api
- baseURL: https://agentdrives.com
  baseurl_source: declared
  description: Pay for a drive or a call over HTTP 402 (x402 or MPP), prepaid credit and receipts
  name: agentdrives-com Pay over HTTP 402 API
  slug: agentdrives-com-pay-over-http-402-api
- baseURL: https://agentdrives.com
  baseurl_source: declared
  description: Questions, disputes and support cases
  name: agentdrives-com Support API
  slug: agentdrives-com-support-api
artifact_total: 26
asyncapis:
- description: ''
  name: Agentdrives Com Webhooks
  slug: agentdrives-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/agentdrives-com/agentic-access/agentdrives-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentdrives-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/agentdrives-com/plans/agentdrives-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentdrives-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentdrives-com/rules/agentdrives-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentdrives-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentdrives-com/json-ld/agentdrives-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentdrives-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentdrives-com/vocabulary/agentdrives-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentdrives-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentdrives-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentdrives-com/asyncapi/agentdrives-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agentdrives-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/agentdrives-com/data-model/agentdrives-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentdrives-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/agentdrives-com/authentication/agentdrives-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentdrives-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentdrives-com/errors/agentdrives-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentdrives-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentdrives-com/conformance/agentdrives-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentdrives-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentdrives-com/llms/agentdrives-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentdrives-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agentdrives-com/a2a/agentdrives-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentdrives-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/agentdrives-com/mcp/agentdrives-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentdrives-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentdrives-com/mcp/agentdrives-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentdrives-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentdrives-com/well-known/agentdrives-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentdrives-com-security.txt
- group: agent
  href: https://artifacts.apis.io/agentdrives-com/well-known/agentdrives-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentdrives-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentdrives-com/hosts/agentdrives-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentdrives-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentdrives-com/vendors/agentdrives-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentdrives-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentdrives.com/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://agentdrives.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentdrives.com/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://agentdrives.com/research/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentdrives.com/categories/developer
- group: operate
  title: ''
  type: ChangeLog
  url: https://agentdrives.com/method/changelog
- group: start
  title: ''
  type: SignUp
  url: https://agentdrives.com/api/agents/signup
- group: auth
  href: https://artifacts.apis.io/agentdrives-com/security/agentdrives-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentdrives-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentdrives-com/security/agentdrives-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentdrives-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentdrives.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agentdrives.com/data
- group: docs
  title: ''
  type: APIReference
  url: https://agentdrives.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agentdrives.com/index.md
- group: commercial
  title: ''
  type: Pricing
  url: https://agentdrives.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://agentdrives.com/research
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AgentDrives
created: '2026-10-31'
description: AgentDrives is an independent lab that evaluates how AI agents can access and use software. It provides open data on agent-driven interactions, tools, and APIs, offering a searchable directory of software products, detailed drive reports, and an MCP server for agents to discover suitable tools before signing up. The platform publishes pricing, data sets, and documentation to help developers understand agent capabilities and improve integration.
image: https://agentdrives.com/logo.png
json_schemas:
- name: AuditFixes
  property_count: 12
  slug: agentdrives-com-audit-fixes
- name: BotChecks
  property_count: 13
  slug: agentdrives-com-bot-checks
- name: Order
  property_count: 34
  slug: agentdrives-com-order
- name: PaymentMap
  property_count: 5
  slug: agentdrives-com-payment-map
- name: TaskResult
  property_count: 35
  slug: agentdrives-com-task-result
- name: Tool
  property_count: 87
  slug: agentdrives-com-tool
jsonld:
- class_count: 39
  name: Agentdrives Com Context
  property_count: 287
  slug: agentdrives-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentdrives.com requiring an API key.
  name: agentdrives-com MCP Server
  slug: agentdrives-com-mcp-yml
modified: '2026-10-31'
name: agentdrives-com
nav: Providers
network: true
overview: 'agentdrives-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Claims API, Directory API, and 5 more. Tagged areas include Artificial Intelligence, Agents, Lab, Software, and Testing.


  The agentdrives-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  agentdrives-com''s developer surface includes authentication, changelog, signup flow, documentation, API reference, getting-started guide, pricing, and 28 more developer resources.'
plans:
- name: Agentdrives Com Plans Pricing
  plan_count: 13
  slug: agentdrives-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Agentdrives Com Rate Limits
  slug: agentdrives-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: agentdrives-com API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 2
  slug: agentdrives-com-rules
scopes:
- name: Agentdrives Com Scopes
  scope_count: 0
  slug: agentdrives-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 71.8
    developer_ergonomics: 38.6
    discoverability: 65.8
    operational_transparency: 23.7
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentdrives Com Authentication
  slug: agentdrives-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentdrives Com Domain Security
  slug: agentdrives-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agentdrives Com Vulnerability Disclosure
  slug: agentdrives-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: check-agent-access
  slug: agentdrives-com-check-agent-access
slug: agentdrives-com
tags:
- Artificial Intelligence
- Agents
- Lab
- Software
- Testing
- Data
website: https://agentdrives.com/
---
