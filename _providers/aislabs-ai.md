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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AIS API provides CVE intelligence, brief summaries, and flight recorder monitoring.
  name: AIS API
  slug: ais-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/aislabs-ai/rules/aislabs-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/aislabs-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/aislabs-ai/conformance/aislabs-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aislabs-ai-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/aislabs-ai/plans/aislabs-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aislabs-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aislabs-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/aislabs-ai/cli/aislabs-ai-cli.yml
  title: ''
  type: CLI
  url: cli/aislabs-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/aislabs-ai/security/aislabs-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aislabs-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aislabs-ai/authentication/aislabs-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aislabs-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/aislabs-ai/errors/aislabs-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aislabs-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/aislabs-ai/llms/aislabs-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aislabs-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/aislabs-ai/mcp/aislabs-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aislabs-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aislabs-ai/mcp/aislabs-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aislabs-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aislabs-ai/well-known/aislabs-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aislabs-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/aislabs-ai/well-known/aislabs-ai-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aislabs-ai-api-security.txt
- group: agent
  href: https://artifacts.apis.io/aislabs-ai/well-known/aislabs-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aislabs-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/aislabs-ai/hosts/aislabs-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aislabs-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/aislabs-ai/vendors/aislabs-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aislabs-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aislabs-ai/security/aislabs-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aislabs-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aislabs-ai/security/aislabs-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aislabs-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aislabs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://aislabs.ai/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://aislabs.ai/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://aislabs.ai/products/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aislabs-ai
created: '2026-10-29'
description: AIS Labs AI is a product lab that builds practical AI‑powered tools and concise briefs for users who prefer actionable signals over endless dashboards. Offering a suite of deterministic, auditable services such as CVE prioritization, brief summaries, and monitoring utilities, the platform operates on a pay‑per‑use model with transparent pricing. All tools are open‑source where possible, and the companion CLI is MIT‑licensed. The company is operated by Autonomous Intelligent Systems LLC.
image: https://aislabs.ai/og/v2/home.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at api.aislabs.ai.
  name: aislabs-ai MCP Server
  slug: aislabs-ai-mcp-yml
modified: '2026-10-29'
name: aislabs-ai
nav: Providers
network: true
overview: 'aislabs-ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Tools, Briefs, and Security.


  The aislabs-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  aislabs-ai''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, and 18 more developer resources.'
plans:
- name: Aislabs Ai Plans Pricing
  plan_count: 2
  slug: aislabs-ai-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Aislabs Ai Rate Limits
  slug: aislabs-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: aislabs-ai API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: aislabs-ai-rules
scopes:
- name: Aislabs Ai Scopes
  scope_count: 0
  slug: aislabs-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 39.8
    discoverability: 75.0
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/aislabs-ai/aislabs-ai-2026-11-03T120543.png
security:
- kind: authentication
  name: Aislabs Ai Authentication
  slug: aislabs-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aislabs Ai Domain Security
  slug: aislabs-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aislabs Ai Vulnerability Disclosure
  slug: aislabs-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-teaser
  slug: aislabs-ai-get-teaser
slug: aislabs-ai
tags:
- Company
- Artificial Intelligence
- Tools
- Briefs
- Security
- Data
website: https://aislabs.ai/
---
