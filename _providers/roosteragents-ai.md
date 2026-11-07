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
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Roosteragents Ai Agentic Access
  operation_count: 6
  slug: roosteragents-ai-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- baseURL: https://roosteragents.ai
  baseurl_source: declared
  description: The Agent Readiness API from roosteragents-ai — 1 operation(s) for agent readiness.
  name: roosteragents-ai Agent Readiness API
  slug: roosteragents-ai-agent-readiness-api
- baseURL: https://roosteragents.ai
  baseurl_source: declared
  description: The Gateway API from roosteragents-ai — 2 operation(s) for gateway.
  name: roosteragents-ai Gateway API
  slug: roosteragents-ai-gateway-api
- baseURL: https://roosteragents.ai
  baseurl_source: declared
  description: The Mcp API from roosteragents-ai — 1 operation(s) for mcp.
  name: roosteragents-ai MCP API
  slug: roosteragents-ai-mcp-api
- baseURL: https://roosteragents.ai
  baseurl_source: declared
  description: The Scan API from roosteragents-ai — 2 operation(s) for scan.
  name: roosteragents-ai Scan API
  slug: roosteragents-ai-scan-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/roosteragents-ai/agentic-access/roosteragents-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/roosteragents-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/roosteragents-ai/plans/roosteragents-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/roosteragents-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/roosteragents-ai/rules/roosteragents-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/roosteragents-ai-rules.yml
- group: agent
  href: https://artifacts.apis.io/roosteragents-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://roosteragents.ai/
- group: design
  href: https://artifacts.apis.io/roosteragents-ai/errors/roosteragents-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/roosteragents-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/roosteragents-ai/conformance/roosteragents-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/roosteragents-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/roosteragents-ai/llms/roosteragents-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/roosteragents-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/roosteragents-ai/a2a/roosteragents-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/roosteragents-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/roosteragents-ai/mcp/roosteragents-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/roosteragents-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/roosteragents-ai/mcp/roosteragents-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/roosteragents-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/roosteragents-ai/well-known/roosteragents-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/roosteragents-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/roosteragents-ai/well-known/roosteragents-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/roosteragents-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/roosteragents-ai/hosts/roosteragents-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/roosteragents-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/roosteragents-ai/vendors/roosteragents-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/roosteragents-ai-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://roosteragents.ai/help/
- group: commercial
  title: ''
  type: Pricing
  url: https://roosteragents.ai/help/subscription-billing/pricing-plans/
- group: company
  title: ''
  type: Newsroom
  url: https://roosteragents.ai/press/agent-to-human-pay-benchmark/
- group: auth
  href: https://artifacts.apis.io/roosteragents-ai/authentication/roosteragents-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/roosteragents-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/roosteragents-ai/security/roosteragents-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/roosteragents-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/roosteragents-ai/security/roosteragents-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/roosteragents-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://roosteragents.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://roosteragents.ai/tools/
- group: docs
  title: ''
  type: Documentation
  url: https://roosteragents.ai/openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://roosteragents.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://roosteragents.ai/whats-included/
- group: company
  title: ''
  type: Blog
  url: https://roosteragents.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://roosteragents.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://roosteragents.ai/privacy/
created: '2026-10-29'
description: 'Rooster Agents builds and runs the AI marketing machine behind MON$TER MONEY ambassadors and the Data Kings & Queens, enabling businesses to become the #1 name in their market for monetizing data. The platform automates, optimizes, and outperforms marketing efforts through 25 AI agents managed by Rudy, requiring no dashboard interaction.'
image: https://roosteragents.ai/uploads/og-card-v1.png
layout: provider
mcp_servers:
- description: Remote MCP server at roosteragents.ai.
  name: roosteragents-ai MCP Server
  slug: roosteragents-ai-mcp-yml
modified: '2026-10-29'
name: roosteragents-ai
nav: Providers
network: true
overview: 'roosteragents-ai publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Readiness API, Gateway API, MCP API, and 1 more. Tagged areas include Artificial Intelligence, Marketing, Automation, Software-as-a-Service, and Data.


  The roosteragents-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  roosteragents-ai''s developer surface includes support, pricing, authentication, documentation, API reference, getting-started guide, engineering blog, and 22 more developer resources.'
plans:
- name: Roosteragents Ai Plans Pricing
  plan_count: 2
  slug: roosteragents-ai-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: roosteragents-ai API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: roosteragents-ai-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 41.0
    discoverability: 75.8
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/roosteragents-ai/roosteragents-ai-2026-11-03T142404.png
security:
- kind: authentication
  name: Roosteragents Ai Authentication
  slug: roosteragents-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Roosteragents Ai Domain Security
  slug: roosteragents-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Roosteragents Ai Vulnerability Disclosure
  slug: roosteragents-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: discover-businesses
  slug: roosteragents-ai-discover-businesses
- name: get-business
  slug: roosteragents-ai-get-business
slug: roosteragents-ai
tags:
- Artificial Intelligence
- Marketing
- Automation
- Software-as-a-Service
- Data
website: https://roosteragents.ai/
---
