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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Background Check Quotes API provides dataset and enquiry tools for US background screening pricing.
  name: Background Check Quotes API
  slug: background-check-quotes-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/backgroundcheckquotes-com/vocabulary/backgroundcheckquotes-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/backgroundcheckquotes-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/backgroundcheckquotes-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://backgroundcheckquotes.com/terms
- group: design
  href: https://artifacts.apis.io/backgroundcheckquotes-com/conformance/backgroundcheckquotes-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/backgroundcheckquotes-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/backgroundcheckquotes-com/llms/backgroundcheckquotes-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/backgroundcheckquotes-com-llms.txt
- group: build
  href: https://artifacts.apis.io/backgroundcheckquotes-com/mcp/backgroundcheckquotes-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/backgroundcheckquotes-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/backgroundcheckquotes-com/mcp/backgroundcheckquotes-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/backgroundcheckquotes-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/backgroundcheckquotes-com/well-known/backgroundcheckquotes-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/backgroundcheckquotes-com-security.txt
- group: agent
  href: https://artifacts.apis.io/backgroundcheckquotes-com/well-known/backgroundcheckquotes-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/backgroundcheckquotes-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/backgroundcheckquotes-com/hosts/backgroundcheckquotes-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backgroundcheckquotes-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/backgroundcheckquotes-com/vendors/backgroundcheckquotes-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backgroundcheckquotes-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://backgroundcheckquotes.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://backgroundcheckquotes.com/privacy/
- group: auth
  href: https://artifacts.apis.io/backgroundcheckquotes-com/security/backgroundcheckquotes-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/backgroundcheckquotes-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/backgroundcheckquotes-com/security/backgroundcheckquotes-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backgroundcheckquotes-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backgroundcheckquotes.com/
created: '2026-11-02'
description: Background Check Quotes aggregates pricing information from U.S. employment and tenant background screening providers. It lists 25 companies from the CFPB consumer reporting list, showing which publish prices (median $29.99) and which require quotes. The site is run by Joseph Ellul and provides data, guides, and tools for professionals needing background check cost insights.
image: https://backgroundcheckquotes.com/favicon.svg?v=0.5.0
layout: provider
mcp_servers:
- description: Remote MCP server at backgroundcheckquotes.com.
  name: Background Check Quotes MCP Server
  slug: backgroundcheckquotes-com-mcp-yml
modified: '2026-11-02'
name: Background Check Quotes
nav: Providers
network: true
overview: Background Check Quotes publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Background Checks, Pricing, Employment, Tenants, and Data.
plans:
- name: Backgroundcheckquotes Com Plans Pricing
  plan_count: 0
  slug: backgroundcheckquotes-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Backgroundcheckquotes Com Rate Limits
  slug: backgroundcheckquotes-com-rate-limits
scopes:
- name: Backgroundcheckquotes Com Scopes
  scope_count: 0
  slug: backgroundcheckquotes-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 16.7
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Backgroundcheckquotes Com Authentication
  slug: backgroundcheckquotes-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Backgroundcheckquotes Com Domain Security
  slug: backgroundcheckquotes-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Backgroundcheckquotes Com Vulnerability Disclosure
  slug: backgroundcheckquotes-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset-tools
  slug: backgroundcheckquotes-com-dataset-tools
slug: backgroundcheckquotes-com
tags:
- Background Checks
- Pricing
- Employment
- Tenants
- Data
website: https://backgroundcheckquotes.com/
---
