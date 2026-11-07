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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Deflectvo Com Agentic Access
  operation_count: 9
  slug: deflectvo-com-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 1
apis:
- baseURL: https://deflectvo.com
  baseurl_source: declared
  description: dataset
  name: Deflectvo Dataset API
  slug: deflectvo-com-dataset-api
- baseURL: https://deflectvo.com
  baseurl_source: declared
  description: The mcp API from Deflectvo — 1 operation(s) for mcp.
  name: Deflectvo MCP API
  slug: deflectvo-com-mcp-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/deflectvo-com/agentic-access/deflectvo-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deflectvo-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/deflectvo-com/plans/deflectvo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deflectvo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deflectvo-com/rules/deflectvo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/deflectvo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/deflectvo-com/vocabulary/deflectvo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deflectvo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/deflectvo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/deflectvo-com/conventions/deflectvo-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/deflectvo-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://deflectvo.com/terms
- group: design
  href: https://artifacts.apis.io/deflectvo-com/errors/deflectvo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deflectvo-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/deflectvo-com/conformance/deflectvo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deflectvo-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/deflectvo-com/overlays/deflectvo-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/deflectvo-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/deflectvo-com/llms/deflectvo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deflectvo-com-llms.txt
- group: build
  href: https://artifacts.apis.io/deflectvo-com/mcp/deflectvo-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/deflectvo-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/deflectvo-com/mcp/deflectvo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deflectvo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/deflectvo-com/well-known/deflectvo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deflectvo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/deflectvo-com/well-known/deflectvo-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deflectvo-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/deflectvo-com/well-known/deflectvo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deflectvo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/deflectvo-com/hosts/deflectvo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deflectvo-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/deflectvo-com/integrations/deflectvo-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/deflectvo-com-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/deflectvo-com/vendors/deflectvo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deflectvo-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/deflectvo-com/authentication/deflectvo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deflectvo-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/deflectvo-com/security/deflectvo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deflectvo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deflectvo-com/security/deflectvo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deflectvo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deflectvo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://deflectvo.com/tools/
- group: commercial
  title: ''
  type: Pricing
  url: https://deflectvo.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://deflectvo.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deflectvo.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deflectvo.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://app.deflectvo.com/?tab=account
- group: agent
  title: ''
  type: LLMsTxt
  url: https://deflectvo.com/llms.txt
created: '2026-11-05'
description: 'Deflectvo (deflectvo.com, ''Customer Self Service Portal Software'') is customer self-service portal software for small US companies. It publishes two free on-page worksheets: a deflection business case (tickets a month, share answered by the portal, cost per agent-handled ticket and portal cost into monthly savings and payback) and a help-center content plan (ticket categories, articles per category and minutes per article into articles to write, hours and ticket coverage). Deflectvo Pro tracks each customer''s account, cases, articles read and requests raised with monthly deflection figures, and exports the data. Surfaced via the MCP registry harvest.'
image: https://deflectvo.com/og.png
layout: provider
mcp_servers:
- description: Deflectvo's own remote MCP server served from its domain, exposing a read-only dataset of monthly US search demand across the worksheets the product ships. Server card read with GET https://deflectvo.
  name: Deflectvo MCP server
  slug: deflectvo-deflectvo-com
modified: '2026-11-05'
name: Deflectvo
nav: Providers
network: true
overview: 'Deflectvo publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API and MCP API. Tagged areas include Company, Customer Self-Service, Customer Service, Help Center, and Ticket Deflection.


  The Deflectvo catalog on APIs.io includes 1 Spectral governance ruleset.


  Deflectvo''s developer surface includes authentication, documentation, pricing, support, and 26 more developer resources.'
plans:
- name: Deflectvo Com Plans Pricing
  plan_count: 2
  slug: deflectvo-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Deflectvo Com Rate Limits
  slug: deflectvo-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Deflectvo API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: deflectvo-com-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 28.0
    discoverability: 71.7
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deflectvo Com Authentication
  slug: deflectvo-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deflectvo Com Domain Security
  slug: deflectvo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Deflectvo Com Vulnerability Disclosure
  slug: deflectvo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: look-up-search-demand
  slug: deflectvo-com-look-up-search-demand
- name: rank-and-cite-search-demand
  slug: deflectvo-com-rank-and-cite-search-demand
slug: deflectvo-com
tags:
- Company
- Customer Self-Service
- Customer Service
- Help Center
- Ticket Deflection
- Customer Portal
- Software-as-a-Service
website: https://deflectvo.com/
---
