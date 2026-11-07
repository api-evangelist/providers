---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bridgedays Eu Agentic Access
  operation_count: 5
  slug: bridgedays-eu-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Plan annual leave around public holidays via BridgeDays API.
  name: BridgeDays API
  slug: bridgedays-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/bridgedays-eu/agentic-access/bridgedays-eu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bridgedays-eu-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bridgedays-eu/rules/bridgedays-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/bridgedays-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/bridgedays-eu/errors/bridgedays-eu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bridgedays-eu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bridgedays-eu/conformance/bridgedays-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bridgedays-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bridgedays-eu/llms/bridgedays-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bridgedays-eu-llms.txt
- group: agent
  href: https://artifacts.apis.io/bridgedays-eu/mcp/bridgedays-eu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bridgedays-eu-mcp.yml
- group: other
  href: https://artifacts.apis.io/bridgedays-eu/hosts/bridgedays-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bridgedays-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/bridgedays-eu/vendors/bridgedays-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bridgedays-eu-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bridgedays.eu/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bridgedays.eu/privacy-policy
- group: auth
  href: https://artifacts.apis.io/bridgedays-eu/security/bridgedays-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bridgedays-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bridgedays.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://bridgedays.eu/developers
- group: docs
  title: ''
  type: APIReference
  url: https://bridgedays.eu/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://bridgedays.eu/planner
- group: operate
  title: ''
  type: Support
  url: https://bridgedays.eu/contact
- group: company
  title: ''
  type: Blog
  url: https://bridgedays.eu/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bridgedays.eu/pricing
created: '2026-11-03'
description: BridgeDays is a free online planner that helps users turn a few days of leave into long breaks by finding bridge days around public holidays for over 200 countries. It offers calendar export, customizable vacation preferences, and a widget for travel businesses, all without cost. The service is built as a web application accessible worldwide.
image: https://bridgedays.eu/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at bridgedays.eu.
  name: BridgeDays MCP Server
  slug: bridgedays-eu-mcp-yml
modified: '2026-11-03'
name: BridgeDays
nav: Providers
network: true
overview: 'BridgeDays is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Planner, Holidays, Vacation, and Free.


  The BridgeDays catalog on APIs.io includes 1 Spectral governance ruleset.


  BridgeDays'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 12 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: BridgeDays API Rules
  rule_count: 35
  severity_counts:
    error: 31
    hint: 0
    info: 3
    warn: 1
  slug: bridgedays-eu-rules
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 31.8
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bridgedays Eu Domain Security
  slug: bridgedays-eu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bridgedays-eu
tags:
- Company
- Planner
- Holidays
- Vacation
- Free
website: https://bridgedays.eu/
---
