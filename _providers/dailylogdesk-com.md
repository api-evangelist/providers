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
  name: Dailylogdesk Com Agentic Access
  operation_count: 9
  slug: dailylogdesk-com-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 1
apis:
- baseURL: https://dailylogdesk.com
  baseurl_source: declared
  description: dataset
  name: DailyLogDesk Dataset API
  slug: dailylogdesk-com-dataset-api
- baseURL: https://dailylogdesk.com
  baseurl_source: declared
  description: The mcp API from DailyLogDesk — 1 operation(s) for mcp.
  name: DailyLogDesk MCP API
  slug: dailylogdesk-com-mcp-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://dailylogdesk.com/mcp
- group: build
  href: https://artifacts.apis.io/dailylogdesk-com/integrations/dailylogdesk-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dailylogdesk-com-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/dailylogdesk-com/agentic-access/dailylogdesk-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dailylogdesk-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dailylogdesk-com/plans/dailylogdesk-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dailylogdesk-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dailylogdesk-com/rules/dailylogdesk-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dailylogdesk-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dailylogdesk-com/vocabulary/dailylogdesk-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dailylogdesk-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dailylogdesk-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dailylogdesk-com/conventions/dailylogdesk-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dailylogdesk-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://dailylogdesk.com/terms
- group: design
  href: https://artifacts.apis.io/dailylogdesk-com/errors/dailylogdesk-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dailylogdesk-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dailylogdesk-com/conformance/dailylogdesk-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dailylogdesk-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/dailylogdesk-com/overlays/dailylogdesk-com-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dailylogdesk-com-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/dailylogdesk-com/llms/dailylogdesk-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dailylogdesk-com-llms.txt
- group: build
  href: https://artifacts.apis.io/dailylogdesk-com/mcp/dailylogdesk-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dailylogdesk-com-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/dailylogdesk-com/well-known/dailylogdesk-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dailylogdesk-com-security.txt
- group: auth
  href: https://artifacts.apis.io/dailylogdesk-com/well-known/dailylogdesk-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dailylogdesk-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/dailylogdesk-com/well-known/dailylogdesk-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dailylogdesk-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dailylogdesk-com/hosts/dailylogdesk-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dailylogdesk-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dailylogdesk-com/vendors/dailylogdesk-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dailylogdesk-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dailylogdesk-com/authentication/dailylogdesk-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dailylogdesk-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dailylogdesk-com/security/dailylogdesk-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dailylogdesk-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dailylogdesk-com/security/dailylogdesk-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dailylogdesk-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dailylogdesk.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://dailylogdesk.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.dailylogdesk.com/?tab=account
- group: operate
  title: ''
  type: Support
  url: https://dailylogdesk.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dailylogdesk.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dailylogdesk.com/privacy/
- group: company
  title: ''
  type: About
  url: https://dailylogdesk.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://dailylogdesk.com/contact/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://dailylogdesk.com/llms.txt
created: '2026-11-05'
description: 'DailyLogDesk is site-record software built only for small construction contractors, sold by Ellul Solutions Ltd (UK). Its site offers 8 free tools: an incident report with the OSHA reporting clock, a 5x5 risk assessment, a risk assessment and method statement (RAMS), a construction quote, a daily activity report, a certificate of completion, a field service report and a post-construction cleaning checklist. DailyLogDesk Pro ($29 per month for a whole site team) keeps the records, and the service publishes an OpenAPI description and an MCP endpoint at dailylogdesk.com.'
image: https://dailylogdesk.com/og.png
layout: provider
mcp_servers:
- description: ''
  name: DailyLogDesk MCP Server
  slug: mcp
modified: '2026-11-05'
name: DailyLogDesk
nav: Providers
network: true
overview: 'DailyLogDesk publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API and MCP API. Tagged areas include Company, Construction, Site Records, Incident Reporting, and Risk Assessment.


  The DailyLogDesk catalog on APIs.io includes 1 Spectral governance ruleset.


  DailyLogDesk''s developer surface includes authentication, pricing, support, and 28 more developer resources.'
plans:
- name: Dailylogdesk Com Plans Pricing
  plan_count: 3
  slug: dailylogdesk-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Dailylogdesk Com Rate Limits
  slug: dailylogdesk-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: DailyLogDesk API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: dailylogdesk-com-rules
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 18.5
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
    matched_via: tags
    regime: Health
    regime_id: health
    score: 24.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dailylogdesk Com Authentication
  slug: dailylogdesk-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dailylogdesk Com Domain Security
  slug: dailylogdesk-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Dailylogdesk Com Vulnerability Disclosure
  slug: dailylogdesk-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: dailylogdesk-com-explore-the-dataset
  slug: dailylogdesk-com-explore-the-dataset
- name: dailylogdesk-com-rank-and-compare
  slug: dailylogdesk-com-rank-and-compare
slug: dailylogdesk-com
tags:
- Company
- Construction
- Site Records
- Incident Reporting
- Risk Assessment
- Health and Safety
- Contractors
- Quotes
website: https://dailylogdesk.com/
---
