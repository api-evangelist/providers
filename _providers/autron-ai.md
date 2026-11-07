---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Autron API provides endpoints for managing Amazon advertising automation.
  name: Autron API
  slug: autron-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/autron-ai/rules/autron-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/autron-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/autron-ai/vocabulary/autron-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/autron-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/autron-ai/conformance/autron-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autron-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/autron-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/autron-ai/data-model/autron-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/autron-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/autron-ai/security/autron-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/autron-ai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/autron-ai/errors/autron-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/autron-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/autron-ai/llms/autron-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autron-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/autron-ai/mcp/autron-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/autron-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/autron-ai/well-known/autron-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autron-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/autron-ai/well-known/autron-ai-agent-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autron-ai-agent-security.txt
- group: agent
  href: https://artifacts.apis.io/autron-ai/well-known/autron-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autron-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/autron-ai/hosts/autron-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autron-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/autron-ai/vendors/autron-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autron-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://agent.autron.ai/login
- group: auth
  href: https://artifacts.apis.io/autron-ai/security/autron-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/autron-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/autron-ai/security/autron-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autron-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autron.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://autron.ai/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://autron.ai/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://autron.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://autron.ai/help
- group: company
  title: ''
  type: Blog
  url: https://autron.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://autron.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autron.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autron.ai/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.autron.ai/swagger.json
  - status: 401
    url: https://agent.autron.ai/api/mcp
  - status: 200
    url: https://autron.ai/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Autron is an AI‑driven agent for Amazon advertising that reads your Amazon Ads and seller data, identifies wasted spend, and makes automated changes you approve. It empowers small businesses to scale with optimized campaigns, transparent insights, and maximum ROI without manual management or high fees. Start free to let Autron automate your Amazon ad operations.
image: https://autron.ai/logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at agent.autron.ai requiring OAuth.
  name: Autron MCP Server
  slug: autron-ai-mcp-yml
modified: '2026-11-02'
name: Autron
nav: Providers
network: true
overview: 'Autron publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Advertising, Amazon, Automation, and Software-as-a-Service.


  The Autron catalog on APIs.io includes 1 Spectral governance ruleset.


  Autron''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Autron Ai Plans Pricing
  plan_count: 0
  slug: autron-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Autron Ai Rate Limits
  slug: autron-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Autron API Rules
  rule_count: 28
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 9
  slug: autron-ai-rules
scopes:
- name: Autron Ai Scopes
  scope_count: 0
  slug: autron-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 25.5
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 31.7
  provenance:
    conformance: derived
    mcp: derived
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
  name: Autron Ai Authentication
  slug: autron-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Autron Ai Domain Security
  slug: autron-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Autron Ai Vulnerability Disclosure
  slug: autron-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-agent-iframe
  slug: autron-ai-get-agent-iframe
slug: autron-ai
tags:
- Artificial Intelligence
- Advertising
- Amazon
- Automation
- Software-as-a-Service
- Marketing
website: https://autron.ai/
---
