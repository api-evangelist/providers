---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Sipi Agentic Access
  operation_count: 13
  slug: sipi-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 1
apis:
- baseURL: https://sipi.bot
  baseurl_source: spec
  description: Register agents and issue API keys
  name: GitDealFlow Agents API
  slug: sipi-agents-api
- baseURL: https://sipi.bot
  baseurl_source: spec
  description: Human-in-the-loop approval queue for FLAGGED transactions
  name: GitDealFlow Approvals API
  slug: sipi-approvals-api
- baseURL: https://sipi.bot
  baseurl_source: spec
  description: Live spend activity, budget status, and dashboard aggregates
  name: GitDealFlow Budget API
  slug: sipi-budget-api
- baseURL: https://sipi.bot
  baseurl_source: spec
  description: The core spend-decision call an agent makes
  name: GitDealFlow Evaluate API
  slug: sipi-evaluate-api
- baseURL: https://sipi.bot
  baseurl_source: spec
  description: Create, list, and delete spend-policy rules
  name: GitDealFlow Rules API
  slug: sipi-rules-api
- baseURL: https://sipi.bot
  baseurl_source: spec
  description: Service health and metadata
  name: GitDealFlow System API
  slug: sipi-system-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/sipi/agentic-access/sipi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sipi-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/sipi/plans/sipi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sipi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sipi/rules/sipi-rules.yml
  title: ''
  type: Spectral
  url: rules/sipi-rules.yml
- group: design
  href: https://artifacts.apis.io/sipi/json-ld/sipi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sipi-context.jsonld
- group: design
  href: https://artifacts.apis.io/sipi/vocabulary/sipi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sipi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sipi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sipi/data-model/sipi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sipi-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://sipi.bot/security
- group: auth
  title: ''
  type: Security
  url: https://sipi.bot/privacy
- group: design
  href: https://artifacts.apis.io/sipi/errors/sipi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sipi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sipi/conformance/sipi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sipi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sipi/llms/sipi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sipi-llms.txt
- group: other
  href: https://artifacts.apis.io/sipi/a2a/sipi-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sipi-a2a.yml
- group: build
  href: https://artifacts.apis.io/sipi/mcp/sipi-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/sipi-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/sipi/mcp/sipi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sipi-mcp.yml
- group: auth
  href: https://artifacts.apis.io/sipi/well-known/sipi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sipi-security.txt
- group: agent
  href: https://artifacts.apis.io/sipi/well-known/sipi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sipi-well-known.yml
- group: other
  href: https://artifacts.apis.io/sipi/hosts/sipi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sipi-hosts.yml
- group: other
  href: https://artifacts.apis.io/sipi/vendors/sipi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sipi-vendors.yml
- group: auth
  href: https://artifacts.apis.io/sipi/authentication/sipi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sipi-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sipi/security/sipi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sipi-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sipi/security/sipi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sipi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sipi/security/sipi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sipi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sipi.bot/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sipi.bot/
- group: docs
  title: ''
  type: Documentation
  url: https://sipi.bot/guides/
- group: docs
  title: ''
  type: APIReference
  url: https://sipi.bot/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://sipi.bot/learn/how-to-control-ai-agent-spending
- group: operate
  title: ''
  type: Support
  url: https://sipi.bot/faq
- group: company
  title: ''
  type: Blog
  url: https://sipi.bot/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kindrat86/sipi-bot
- group: commercial
  title: ''
  type: Pricing
  url: https://sipi.bot/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sipi.bot/pilot
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sipi.bot/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sipi.bot/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kindrat86/workspace/sipi-bot
created: '2026-10-18'
description: GitDealFlow, operating as sipi.bot, provides a pre‑spend firewall for autonomous AI agents. It lets developers set budget caps, velocity limits, and merchant rules so that every proposed payment is evaluated before execution. The service offers a free live sandbox, detailed pricing, and integrations with major AI frameworks, aiming to prevent uncontrolled spending in the agent economy.
image: https://sipi.bot/og.png
json_schemas:
- name: EvaluationResponse
  property_count: 8
  slug: sipi-evaluation-response
- name: RuleCreate
  property_count: 5
  slug: sipi-rule-create
- name: Rule
  property_count: 8
  slug: sipi-rule
- name: Stats
  property_count: 7
  slug: sipi-stats
- name: TransactionRequest
  property_count: 6
  slug: sipi-transaction-request
- name: Transaction
  property_count: 8
  slug: sipi-transaction
jsonld:
- class_count: 10
  name: Sipi Context
  property_count: 31
  slug: sipi-context
layout: provider
mcp_servers:
- description: Remote MCP server at sipi.bot.
  name: GitDealFlow MCP Server
  slug: sipi-mcp-yml
modified: '2026-10-18'
name: GitDealFlow
nav: Providers
network: true
overview: 'GitDealFlow publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Approvals API, Budget API, and 3 more. Tagged areas include Artificial Intelligence, Finance, Security, Automation, and Software-as-a-Service.


  The GitDealFlow catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GitDealFlow''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Sipi Plans Pricing
  plan_count: 2
  slug: sipi-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: GitDealFlow API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: sipi-rules
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 65.0
    catalog_earned_first_party: 8.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 19.7
    contract_quality: 60.7
    developer_ergonomics: 68.3
    discoverability: 56.7
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sipi Authentication
  slug: sipi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sipi Domain Security
  slug: sipi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sipi Vulnerability Disclosure
  slug: sipi-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Sipi Trust Center
  slug: sipi-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA
skill_count: 1
skills:
- name: evaluate-spend
  slug: sipi-evaluate_spend
slug: sipi
tags:
- Artificial Intelligence
- Finance
- Security
- Automation
- Software-as-a-Service
website: https://sipi.bot/
---
