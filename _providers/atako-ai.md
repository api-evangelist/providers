---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
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
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Atako customer API — manage AI agents, their files, integrations, billing, and your company/team, programmatically.
  name: Atako API
  slug: atako-api
- baseURL: https://api.atako.ai
  baseurl_source: declared
  description: The Atako customer API — manage AI agents, their files, integrations, billing, and your company/team, programmatically.
  name: Atako API API
  slug: atako-api-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/atako-ai/rules/atako-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/atako-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/atako-ai/json-ld/atako-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/atako-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/atako-ai/vocabulary/atako-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atako-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/atako-ai/conventions/atako-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/atako-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/atako-ai/conformance/atako-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atako-ai-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/atako-ai/plans/atako-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atako-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/atako-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/atako-ai/data-model/atako-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atako-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/atako-ai/conventions/atako-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/atako-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/atako-ai/authentication/atako-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/atako-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/atako-ai/errors/atako-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/atako-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/atako-ai/llms/atako-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atako-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/atako-ai/a2a/atako-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/atako-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/atako-ai/mcp/atako-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atako-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/atako-ai/well-known/atako-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atako-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/atako-ai/hosts/atako-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atako-ai-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://atako.ai/en/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://atako.ai/en/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://atako.ai/fr/use-cases/auto-hr-operations
- group: auth
  href: https://artifacts.apis.io/atako-ai/security/atako-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atako-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atako.ai/
- group: other
  title: ''
  type: Image
  url: https://atako.ai/aiygent.svg
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atako.ai/en/developers
- group: docs
  title: ''
  type: Documentation
  url: https://atako.ai/en/developers
- group: company
  title: ''
  type: Blog
  url: https://atako.ai/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aiybiz
- group: operate
  title: ''
  type: Roadmap
  url: https://atako.ai/en/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://atako.ai/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://atako.ai/en/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atako.ai/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atako.ai/en/privacy
created: '2026-11-01'
description: 'Atako is the autonomous AI workforce platform that lets businesses deploy specialized AI agents in under a minute, with no technical setup required. Meet the team building the infrastructure for AI-native companies: making autonomous AI agents accessible to every business.'
image: https://atako.ai/og.png
json_schemas:
- name: AgentRecord
  property_count: 36
  slug: atako-ai-agent-record
- name: CompanySubscription
  property_count: 27
  slug: atako-ai-company-subscription
- name: CreateAgentBody
  property_count: 13
  slug: atako-ai-create-agent-body
- name: IntegrationPage
  property_count: 14
  slug: atako-ai-integration-page
- name: SiteBanner
  property_count: 15
  slug: atako-ai-site-banner
- name: UseCase
  property_count: 16
  slug: atako-ai-use-case
jsonld:
- class_count: 120
  name: Atako Ai Context
  property_count: 497
  slug: atako-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.atako.ai.
  name: Atako MCP Server
  slug: atako-ai-mcp-yml
modified: '2026-11-01'
name: Atako
nav: Providers
network: true
overview: 'Atako publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Artificial Intelligence, Autonomous Agents, Platform, Software-as-a-Service, and Workforce.


  The Atako catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Atako''s developer surface includes authentication, changelog, getting-started guide, documentation, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Atako Ai Plans Pricing
  plan_count: 2
  slug: atako-ai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Atako Ai Rate Limits
  slug: atako-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Atako API Rules
  rule_count: 54
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 15
  slug: atako-ai-rules
scopes:
- name: Atako Ai Scopes
  scope_count: 0
  slug: atako-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 35.0
    discoverability: 65.8
    operational_transparency: 13.2
  previous_composite: 51.4
  provenance:
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atako Ai Authentication
  slug: atako-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Atako Ai Domain Security
  slug: atako-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atako-ai
tags:
- Artificial Intelligence
- Autonomous Agents
- Platform
- Software-as-a-Service
- Workforce
website: https://atako.ai/
---
