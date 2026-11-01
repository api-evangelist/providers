---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 62.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Prereason Com Agentic Access
  operation_count: 59
  slug: prereason-com-agentic-access
  summary_line: 59 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.prereason.com
  baseurl_source: declared
  description: How an agent with no key gets one from inside its own session. The agent creates a claim, shows one link to the human who owns it, and polls until the human has signed in and approved; the key it then
  name: prereason-com Agent access API
  slug: prereason-com-agent-access-api
- baseURL: https://api.prereason.com
  baseurl_source: declared
  description: One listed company's briefing bought per call, whole or one block at a time, for a company of a market that is live. A key reads the same briefing through GET /api/context when its plan reaches the ma
  name: prereason-com Company Briefings API
  slug: prereason-com-company-briefings-api
- baseURL: https://api.prereason.com
  baseurl_source: declared
  description: Briefing-based context endpoints. The primary way to consume PreReason data. Each briefing bundles related metrics with trend analysis and confidence scores.
  name: prereason-com Context API
  slug: prereason-com-context-api
- baseURL: https://api.prereason.com
  baseurl_source: declared
  description: Individual metric data with trend analysis and interpretation
  name: prereason-com Metrics API
  slug: prereason-com-metrics-api
- baseURL: https://api.prereason.com
  baseurl_source: declared
  description: Convenience aliases that forward to context briefings. Same auth, same response. Use these for quick access or human-friendly URLs.
  name: prereason-com Short URLs API
  slug: prereason-com-short-urls-api
- baseURL: https://api.prereason.com
  baseurl_source: declared
  description: Health, status, and version endpoints
  name: prereason-com System API
  slug: prereason-com-system-api
- baseURL: https://api.prereason.com
  baseurl_source: declared
  description: 'Per-company corporate Bitcoin treasury holdings with provenance. The btc.treasury briefing interprets and ranks the top holders; these endpoints are the lookup surface for every tracked company, with '
  name: prereason-com Treasury Holdings API
  slug: prereason-com-treasury-holdings-api
- baseURL: https://api.prereason.com
  baseurl_source: declared
  description: 'Change events, pushed by webhook to an account''s registered addresses or read from the feed. What changed since a cursor: a live briefing''s state label, a tracked release, and, for the companies a rea'
  name: prereason-com Webhooks API
  slug: prereason-com-webhooks-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/prereason-com/agentic-access/prereason-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/prereason-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/prereason-com/rate-limits/prereason-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/prereason-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/prereason-com/plans/prereason-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prereason-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/prereason-com/rules/prereason-com-rules.yml
  title: ''
  type: Spectral
  url: rules/prereason-com-rules.yml
- group: design
  href: https://artifacts.apis.io/prereason-com/json-ld/prereason-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/prereason-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/prereason-com/vocabulary/prereason-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/prereason-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/prereason-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/prereason-com/data-model/prereason-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/prereason-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/prereason-com/security/prereason-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/prereason-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/prereason-com/authentication/prereason-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/prereason-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/prereason-com/errors/prereason-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/prereason-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/prereason-com/conformance/prereason-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prereason-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/prereason-com/llms/prereason-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/prereason-com-llms.txt
- group: other
  href: https://artifacts.apis.io/prereason-com/a2a/prereason-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/prereason-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/prereason-com/mcp/prereason-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/prereason-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/prereason-com/well-known/prereason-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prereason-com-security.txt
- group: auth
  href: https://artifacts.apis.io/prereason-com/well-known/prereason-com-prereason-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prereason-com-prereason-security.txt
- group: auth
  href: https://artifacts.apis.io/prereason-com/well-known/prereason-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/prereason-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/prereason-com/well-known/prereason-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prereason-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/prereason-com/hosts/prereason-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prereason-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/prereason-com/vendors/prereason-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prereason-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/prereason-com/packages/prereason-com-packages.yml
  title: ''
  type: SDKs
  url: packages/prereason-com-packages.yml
- group: build
  href: https://artifacts.apis.io/prereason-com/packages/prereason-com-packages.yml
  title: ''
  type: Packages
  url: packages/prereason-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/prereason-com/security/prereason-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/prereason-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/prereason-com/security/prereason-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prereason-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prereason.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.prereason.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.prereason.com/api/openapi/spec.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.prereason.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.prereason.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prereason.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prereason.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PreReason
created: '2026-10-31'
description: PreReason provides a Financial Market Context API and MCP server designed for AI agents. It delivers macroeconomic, rates, bonds, FX, commodities, company and Bitcoin data in a single briefing, including interpreted trends, momentum, percentile rankings, cross‑asset correlations and regime classification. Each figure is dated, sourced, and available as markdown or JSON, enabling seamless integration with LLMs and agent frameworks.
image: https://www.prereason.com/og/home.png?v=6
json_schemas:
- name: MetricData
  property_count: 15
  slug: prereason-com-metric-data
- name: MetricLateRelease
  property_count: 13
  slug: prereason-com-metric-late-release
- name: MetricLatestReading
  property_count: 12
  slug: prereason-com-metric-latest-reading
- name: MetricListResponse
  property_count: 6
  slug: prereason-com-metric-list-response
jsonld:
- class_count: 8
  name: Prereason Com Context
  property_count: 55
  slug: prereason-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.prereason.com.
  name: prereason-com MCP Server
  slug: prereason-com-mcp-yml
modified: '2026-10-31'
name: prereason-com
nav: Providers
network: true
overview: 'prereason-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent access API, Company Briefings API, Context API, and 5 more. Tagged areas include Financial, Market, API, AI, and Data.


  The prereason-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  prereason-com''s developer surface includes authentication, documentation, API reference, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Prereason Com Plans Pricing
  plan_count: 5
  slug: prereason-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 8
  name: Prereason Com Rate Limits
  slug: prereason-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: prereason-com API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: prereason-com-rules
score:
  band: strong
  composite: 61.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 94.3
    catalog_earned_first_party: 0.0
    catalog_gap: 20.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 62.0
    developer_ergonomics: 42.1
    discoverability: 56.7
    operational_transparency: 44.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Prereason Com Authentication
  slug: prereason-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Prereason Com Domain Security
  slug: prereason-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prereason Com Vulnerability Disclosure
  slug: prereason-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: get-briefing-by-id
  slug: get-briefing-by-id
- name: get-health
  slug: get-health
- name: list-briefings
  slug: list-briefings
slug: prereason-com
tags:
- Financial
- Market
- API
- AI
- Data
- MCP
website: https://prereason.com/
---
