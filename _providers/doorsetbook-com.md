---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DoorsetBook MCP API providing dataset tools
  name: DoorsetBook API
  slug: doorsetbook-api
- baseURL: https://doorsetbook.com
  baseurl_source: declared
  description: 'DoorsetBook (https://doorsetbook.com/): the site''s own MCP server, served from its domain. DoorsetBook: the monthly GB and US search demand across the tools this product ships, read from monthly searc'
  name: DoorsetBook API API
  slug: doorsetbook-api-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/doorsetbook-com/plans/doorsetbook-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doorsetbook-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/doorsetbook-com/rules/doorsetbook-com-rules.yml
  title: ''
  type: Spectral
  url: rules/doorsetbook-com-rules.yml
- group: design
  href: https://artifacts.apis.io/doorsetbook-com/vocabulary/doorsetbook-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/doorsetbook-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/doorsetbook-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://doorsetbook.com/terms
- group: design
  href: https://artifacts.apis.io/doorsetbook-com/errors/doorsetbook-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/doorsetbook-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/doorsetbook-com/conformance/doorsetbook-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doorsetbook-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/doorsetbook-com/llms/doorsetbook-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doorsetbook-com-llms.txt
- group: build
  href: https://artifacts.apis.io/doorsetbook-com/mcp/doorsetbook-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/doorsetbook-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/doorsetbook-com/mcp/doorsetbook-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/doorsetbook-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/doorsetbook-com/well-known/doorsetbook-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/doorsetbook-com-security.txt
- group: auth
  href: https://artifacts.apis.io/doorsetbook-com/well-known/doorsetbook-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/doorsetbook-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/doorsetbook-com/well-known/doorsetbook-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doorsetbook-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/doorsetbook-com/hosts/doorsetbook-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doorsetbook-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/doorsetbook-com/vendors/doorsetbook-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doorsetbook-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doorsetbook.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://doorsetbook.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doorsetbook.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://doorsetbook.com/pricing/
- group: auth
  href: https://artifacts.apis.io/doorsetbook-com/security/doorsetbook-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/doorsetbook-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/doorsetbook-com/security/doorsetbook-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doorsetbook-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doorsetbook.com/
created: '2026-11-05'
description: DoorsetBook provides free fire door inspection tools, checklists, survey cost calculators, maintenance plans, certification records, repair logs, and installation records for small property teams. It offers seven free tools and a paid plan for saving, branding, signing off, and exporting records, aiming to simplify fire door compliance and management.
image: https://doorsetbook.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at doorsetbook.com.
  name: DoorsetBook MCP Server
  slug: doorsetbook-com-mcp-yml
modified: '2026-11-05'
name: DoorsetBook
nav: Providers
network: true
overview: 'DoorsetBook publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include FireDoors, Inspection, Tools, Property Management, and Compliance.


  The DoorsetBook catalog on APIs.io includes 1 Spectral governance ruleset.


  DoorsetBook''s developer surface includes support, pricing, and 20 more developer resources.'
plans:
- name: Doorsetbook Com Plans Pricing
  plan_count: 2
  slug: doorsetbook-com-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: DoorsetBook API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: doorsetbook-com-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 48.4
    developer_ergonomics: 11.2
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doorsetbook Com Domain Security
  slug: doorsetbook-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Doorsetbook Com Vulnerability Disclosure
  slug: doorsetbook-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: doorsetbook-com
tags:
- FireDoors
- Inspection
- Tools
- Property Management
- Compliance
website: https://doorsetbook.com/
---
