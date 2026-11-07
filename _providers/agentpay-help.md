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
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Pay-per-call AI microservices API
  name: AgentPay API
  slug: agentpay-api
- baseURL: https://agentpay.help
  baseurl_source: declared
  description: Pay-per-call AI microservices via x402 (HTTP 402). USDC on Base. No accounts, no API keys.
  name: AgentPay Api API
  slug: agentpay-api-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/agentpay-help/rules/agentpay-help-rules.yml
  title: ''
  type: Spectral
  url: rules/agentpay-help-rules.yml
- group: design
  href: https://artifacts.apis.io/agentpay-help/vocabulary/agentpay-help-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentpay-help-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentpay-help/conformance/agentpay-help-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentpay-help-conformance.yml
- group: auth
  href: https://artifacts.apis.io/agentpay-help/security/agentpay-help-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentpay-help-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/agentpay-help/errors/agentpay-help-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentpay-help-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/agentpay-help/llms/agentpay-help-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentpay-help-llms.txt
- group: other
  href: https://artifacts.apis.io/agentpay-help/a2a/agentpay-help-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentpay-help-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentpay-help/mcp/agentpay-help-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentpay-help-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentpay-help/well-known/agentpay-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentpay-help-security.txt
- group: agent
  href: https://artifacts.apis.io/agentpay-help/well-known/agentpay-help-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentpay-help-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentpay-help/hosts/agentpay-help-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentpay-help-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentpay-help/vendors/agentpay-help-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentpay-help-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentpay-help/security/agentpay-help-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentpay-help-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentpay-help/security/agentpay-help-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentpay-help-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentpay.help/
created: '2026-11-01'
description: AgentPay provides a marketplace of 34 pay-per-call APIs on the Base blockchain, allowing developers to integrate tools that settle payments in USDC without requiring an account or API key. The platform offers bundled credit packs, transparent pricing, and a simple token‑based authentication model, targeting Web3 developers seeking on‑demand functionality.
image: https://agentpay.help/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at agentpay.help.
  name: AgentPay MCP Server
  slug: agentpay-help-mcp-yml
modified: '2026-11-01'
name: AgentPay
nav: Providers
network: true
overview: 'AgentPay publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Api API, and 1 more. Tagged areas include AI APIs, Cryptocurrency, Finance, Compliance, and Data.


  The AgentPay catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AgentPay API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: agentpay-help-rules
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 16.6
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentpay Help Domain Security
  slug: agentpay-help-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Agentpay Help Vulnerability Disclosure
  slug: agentpay-help-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentpay-help
tags:
- AI APIs
- Cryptocurrency
- Finance
- Compliance
- Data
- Web
- Natural Language Processing
website: https://agentpay.help/
---
