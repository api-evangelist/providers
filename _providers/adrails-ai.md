---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Adrails Ai Agentic Access
  operation_count: 1
  slug: adrails-ai-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: 'First-party tracking for your own site and server. The script records visits and the campaign, ad and click id they arrived with; the collect endpoint records events such as purchases and leads. Only '
  name: Adrails Tracking API
  slug: adrails-tracking-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/adrails-ai/agentic-access/adrails-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adrails-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/adrails-ai/plans/adrails-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adrails-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/adrails-ai/rules/adrails-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/adrails-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/adrails-ai/vocabulary/adrails-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adrails-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/adrails-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/adrails-ai/errors/adrails-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adrails-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adrails-ai/conformance/adrails-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adrails-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adrails-ai/llms/adrails-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adrails-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/adrails-ai/mcp/adrails-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adrails-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/adrails-ai/well-known/adrails-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adrails-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/adrails-ai/well-known/adrails-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adrails-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/adrails-ai/hosts/adrails-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adrails-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/adrails-ai/vendors/adrails-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adrails-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://adrails.ai/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://adrails.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://adrails.ai/docs/tracking/setup
- group: auth
  href: https://artifacts.apis.io/adrails-ai/security/adrails-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adrails-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/adrails-ai/security/adrails-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adrails-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adrails.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://adrails.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://adrails.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://adrails.ai/docs
- group: operate
  title: ''
  type: Support
  url: https://adrails.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://adrails.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/devthomy/adrails-mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://adrails.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://adrails.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adrails.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adrails.ai/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://adrails.ai/api/mcp
  - status: 200
    url: https://adrails.ai/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Adrails provides AI-powered ad management for Shopify brands, enabling paid‑media teams and agencies to automate campaign creation, testing, spend monitoring, and performance explanation across Meta and Google ad accounts. Built and operated by TBSS Labs, LLC, the platform offers a remote MCP server and integrates with Shopify, Meta, and Google data sources.
image: https://adrails.ai/adrails-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at adrails.ai.
  name: Adrails MCP Server
  slug: adrails-ai-mcp-yml
modified: '2026-10-31'
name: Adrails
nav: Providers
network: true
overview: 'Adrails is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Advertising, Marketing, Shopify, and Paid Media.


  The Adrails catalog on APIs.io includes 1 Spectral governance ruleset.


  Adrails'' developer surface includes changelog, getting-started guide, documentation, API reference, support, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Adrails Ai Plans Pricing
  plan_count: 2
  slug: adrails-ai-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Adrails API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: adrails-ai-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.6
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 29.0
    discoverability: 65.0
    operational_transparency: 15.8
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: derived
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
- kind: domain-security
  name: Adrails Ai Domain Security
  slug: adrails-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adrails Ai Vulnerability Disclosure
  slug: adrails-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-tracking-script
  slug: adrails-ai-get-tracking-script
slug: adrails-ai
tags:
- Artificial Intelligence
- Advertising
- Marketing
- Shopify
- Paid Media
website: https://adrails.ai/
---
