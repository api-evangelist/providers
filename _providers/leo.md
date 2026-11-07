---
access_model:
  confidence: medium
  label: Customer-gated
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.meetleo.com/pricing
  - https://www.meetleo.com/mcp
  - openapi/leo-account-api-openapi.yml
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Leo Agentic Access
  operation_count: 7
  slug: leo-agentic-access
  summary_line: 7 operations · 1 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.meetleo.com
  baseurl_source: declared
  description: REST API for account entitlements, credit balance, commercial-insurance prospect search across 134 filter properties, single-prospect retrieval, and asynchronous decision-maker contact enrichment with
  name: LeO Public API
  slug: leo-public-api
- description: First-party, hosted, remote MCP server exposing LeO's insurance intelligence -- 25M+ US businesses across 200+ filters, x-dates, Form 5500 financials, benefits red flags, DOT Intelligence, Trucking Tr
  name: LeO MCP Connector
  slug: leo-mcp-connector
- description: Platform-provided Wix Site MCP server fronting LeO's marketing site, advertised in LeO's llms.txt. Nine tools covering business details, site search and generic Wix site tooling. Unauthenticated, publ
  name: LeO Site MCP (Wix-provided)
  slug: leo-site-mcp-wix-provided
- baseURL: https://api.meetleo.com
  baseurl_source: declared
  description: The Health API from LeO — 1 operation(s) for health.
  name: LeO Health API
  slug: leo-health-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/leo/llms/leo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leo-llms.txt
- group: company
  title: ''
  type: Newsroom
  url: https://resources.meetleo.com/media
- group: company
  title: ''
  type: Blog
  url: https://resources.meetleo.com/blog
- group: agent
  href: https://artifacts.apis.io/leo/agentic-access/leo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/leo-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/leo/rules/leo-rules.yml
  title: ''
  type: Spectral
  url: rules/leo-rules.yml
- group: design
  href: https://artifacts.apis.io/leo/json-ld/leo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/leo-context.jsonld
- group: design
  href: https://artifacts.apis.io/leo/vocabulary/leo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/leo-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/leo/lifecycle/leo-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/leo-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/leo/hosts/leo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/leo-hosts.yml
- group: build
  href: https://artifacts.apis.io/leo/integrations/leo-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/leo-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/leo/vendors/leo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/leo-vendors.yml
- group: other
  href: https://artifacts.apis.io/leo/capabilities/leo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/leo-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.meetleo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meetleo.com/pricing
- group: commercial
  href: https://artifacts.apis.io/leo/plans/leo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leo-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://insights-app.meetleo.com/signup/register
- group: start
  title: ''
  type: Login
  url: https://insights-app.meetleo.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.meetleo.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.meetleo.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meetleo.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meetleo.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.meetleo.com/ai-transparency
- group: design
  href: https://artifacts.apis.io/leo/conformance/leo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leo-conformance.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.meetleo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.meetleo.com/docs
- group: auth
  href: https://artifacts.apis.io/leo/authentication/leo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leo-authentication.yml
- group: auth
  href: https://artifacts.apis.io/leo/scopes/leo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/leo-scopes.yml
- group: design
  href: https://artifacts.apis.io/leo/conventions/leo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/leo-conventions.yml
- group: design
  href: https://artifacts.apis.io/leo/errors/leo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/leo/data-model/leo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leo-data-model.yml
- group: operate
  href: https://artifacts.apis.io/leo/rate-limits/leo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/leo-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/leo/lifecycle/leo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/leo-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/leo/overlays/leo-servers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/leo-servers-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/leo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/leo/mcp/leo-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/leo-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/leo/well-known/leo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leo-well-known.yml
- group: auth
  href: https://artifacts.apis.io/leo/security/leo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leo-domain-security.yml
created: '2026-07-17'
description: 'LeO is an AI-powered sales and prospecting platform for commercial insurance professionals, serving property & casualty (P&C) brokers, employee benefits advisors, and nonprofit insurance specialists. The platform pairs a commercial-lines prospect database of 25M+ US businesses and 200+ filters -- NAICS codes, revenue thresholds, workers'' compensation, DOT/FMCSA records, OSHA compliance history, Form 5500 benefits and pension filings, and IRS 990 nonprofit data -- with a renewal-date (X-date) database carrying key contacts and AI-predicted renewal months. LeO generates AI-personalized email outreach, produces pre-meeting intelligence on incumbent carriers, brokers, coverage and risk gaps, and pushes qualified prospects to CRM or CSV export. Founded by CEO Liri Halperin Segal, LeO is a Techstars portfolio company and has been certified HIPAA compliant by an external auditing firm. Alongside the subscription web application it ships two programmatic surfaces: a REST "Leo Public
  API" at api.meetleo.com with a published OpenAPI 3.0.0 definition covering account, credits, prospect search and asynchronous contact enrichment, and a first-party, OAuth-protected MCP Connector at mcp.meetleo.com marketed for Claude, ChatGPT, Gemini and Copilot. Both are entitlement-gated to existing customers and metered in credits.'
finops:
- has_sources: true
  method: derived
  name: Leo Finops
  primary_unit: ''
  service_category: ''
  slug: leo-finops
  template: true
image: https://static.wixstatic.com/media/38dea4_5b1d1b85783146d8b6cf1c6f354c9be8%7Emv2.jpg/v1/fit/w_2500,h_1330,al_c/38dea4_5b1d1b85783146d8b6cf1c6f354c9be8%7Emv2.jpg
json_schemas:
- name: EnrichProspectsDto
  property_count: 2
  slug: leo-enrich-prospects-dto
- name: EnrichProspectsResponseData
  property_count: 5
  slug: leo-enrich-prospects-response-data
- name: ProspectResponse
  property_count: 21
  slug: leo-prospect-response
- name: SearchProspectsDto
  property_count: 3
  slug: leo-search-prospects-dto
- name: SearchProspectsResponseData
  property_count: 2
  slug: leo-search-prospects-response-data
jsonld:
- class_count: 24
  name: Leo Context
  property_count: 248
  slug: leo-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.meetleo.com over HTTP; 3 tools listed.
  name: LeO MCP Connector
  slug: leo-mcp-connector
- description: Remote MCP server at www.meetleo.com over HTTP; 9 tools listed.
  name: LeO 3.0 Site Visitor Assistant
  slug: leo-3-0-site-visitor-assistant
modified: '2026-10-20'
name: LeO
nav: Providers
network: true
overview: 'LeO publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Public API, Health API, and 2 more. Tagged areas include Company, Insurance, Commercial Insurance, Property and Casualty, and Employee Benefits.


  The LeO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LeO''s developer surface includes engineering blog, pricing, signup flow, support, FAQ, documentation, API reference, and 30 more developer resources.'
plans:
- name: Leo Plans Pricing
  plan_count: 4
  slug: leo-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Leo Rate Limits
  slug: leo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: LeO API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 4
    warn: 1
  slug: leo-rules
scopes:
- name: Leo Scopes
  scope_count: 7
  slug: leo-scopes
  summary_line: 7 scopes
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 77.6
    contract_governance: 35.6
    contract_quality: 53.4
    developer_ergonomics: 36.3
    discoverability: 75.8
    operational_transparency: 7.9
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: platform-generated
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 38.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/leo/leo-2026-07-25T224918.png
security:
- kind: authentication
  name: Leo Authentication
  slug: leo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Leo Domain Security
  slug: leo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: enrich-prospect-contacts
  slug: leo-enrich-prospect-contacts
- name: preflight-account-and-credits
  slug: leo-preflight-account-and-credits
- name: search-prospects-by-renewal-window
  slug: leo-search-prospects-by-renewal-window
slug: leo
tags:
- Company
- Insurance
- Commercial Insurance
- Property and Casualty
- Employee Benefits
- Insurtech
- Artificial Intelligence
- Sales
- Lead Generation
- Prospecting
- Data Enrichment
- Sales Intelligence
- Non-Profit
- Trucking
- MCP
- Agent-Native
website: https://www.meetleo.com/
---
