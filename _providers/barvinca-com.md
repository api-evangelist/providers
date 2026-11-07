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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Bulk User Manager API documented at the developer portal. No machine‑readable contract was found despite probing known locations and the markdown documentation.
  name: Barvinca MCP API
  slug: barvinca-mcp-api
- description: 'Barvinca API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Barvinca API
  slug: barvinca-com-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/barvinca-com/plans/barvinca-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/barvinca-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/barvinca-com/rules/barvinca-com-rules.yml
  title: ''
  type: Spectral
  url: rules/barvinca-com-rules.yml
- group: design
  href: https://artifacts.apis.io/barvinca-com/json-ld/barvinca-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/barvinca-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/barvinca-com/vocabulary/barvinca-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/barvinca-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/barvinca-com/data-model/barvinca-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/barvinca-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/barvinca-com/authentication/barvinca-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/barvinca-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/barvinca-com/conformance/barvinca-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/barvinca-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/barvinca-com/llms/barvinca-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/barvinca-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/barvinca-com/mcp/barvinca-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/barvinca-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/barvinca-com/well-known/barvinca-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/barvinca-com-security.txt
- group: auth
  href: https://artifacts.apis.io/barvinca-com/well-known/barvinca-com-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/barvinca-com-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/barvinca-com/well-known/barvinca-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/barvinca-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/barvinca-com/hosts/barvinca-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barvinca-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/barvinca-com/vendors/barvinca-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/barvinca-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://barvinca.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://barvinca.com/news
- group: auth
  href: https://artifacts.apis.io/barvinca-com/security/barvinca-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/barvinca-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/barvinca-com/security/barvinca-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barvinca-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://barvinca.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://barvinca.com/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://barvinca.com/mcp.md
- group: company
  title: ''
  type: Blog
  url: https://barvinca.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://barvinca.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://barvinca.com/support
- group: docs
  title: ''
  type: SetupGuide
  url: https://barvinca.com/setup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://barvinca.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://barvinca.com/privacy
coverage:
  checked: '2026-11-02'
  detail: Developer portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://dev.barvinca.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Barvinca provides bulk user management for Autodesk Forma and BIM 360, offering dry‑run previews, approval‑bound writes, operation history, and audit‑ready evidence. The platform enables administrators to efficiently manage large numbers of users across Autodesk’s construction and design tools, ensuring compliance and traceability while simplifying onboarding and off‑boarding processes.
image: https://barvinca.com/shared/screenshots/bum-dashboard.webp
json_schemas:
- name: GetProjectV1HubsBD6Cf8C84C25E4534Ae5C62E08480E751ProjectsRes
  property_count: 1
  slug: barvinca-com-get-project-v1-hubs-bd6-cf8-c84-c25-e4534-ae5-c62-e08480-e751-projects-res
- name: GetProjectV1HubsResponse
  property_count: 1
  slug: barvinca-com-get-project-v1-hubs-response
jsonld:
- class_count: 2
  name: Barvinca Com Context
  property_count: 1
  slug: barvinca-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.barvinca.com requiring OAuth.
  name: Barvinca MCP Server
  slug: barvinca-com-mcp-yml
modified: '2026-11-02'
name: Barvinca
nav: Providers
network: true
overview: 'Barvinca is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, BulkUserManagement, Autodesk, BIM360, and Automation.


  The Barvinca catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Barvinca''s developer surface includes authentication, documentation, engineering blog, pricing, support, and 22 more developer resources.'
plans:
- name: Barvinca Com Plans Pricing
  plan_count: 3
  slug: barvinca-com-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Barvinca API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: barvinca-com-rules
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 20.7
    developer_ergonomics: 25.0
    discoverability: 57.5
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Barvinca Com Authentication
  slug: barvinca-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Barvinca Com Domain Security
  slug: barvinca-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Barvinca Com Vulnerability Disclosure
  slug: barvinca-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: barvinca-com
tags:
- Company
- BulkUserManagement
- Autodesk
- BIM360
- Automation
website: https://barvinca.com/
---
