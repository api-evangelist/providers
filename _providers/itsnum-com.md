---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 2
  name: Itsnum Com Agentic Access
  operation_count: 15
  slug: itsnum-com-agentic-access
  summary_line: 15 operations · 7 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://itsnum.com
  baseurl_source: declared
  description: The Agent API from itsnum-com — 15 operation(s) for agent.
  name: itsnum-com Agent API
  slug: itsnum-com-agent-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/itsnum-com/agentic-access/itsnum-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/itsnum-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/itsnum-com/plans/itsnum-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/itsnum-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/itsnum-com/rules/itsnum-com-rules.yml
  title: ''
  type: Spectral
  url: rules/itsnum-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/itsnum-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/itsnum-com/authentication/itsnum-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/itsnum-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/itsnum-com/conformance/itsnum-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/itsnum-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/itsnum-com/llms/itsnum-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/itsnum-com-llms.txt
- group: build
  href: https://artifacts.apis.io/itsnum-com/mcp/itsnum-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/itsnum-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/itsnum-com/mcp/itsnum-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/itsnum-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/itsnum-com/well-known/itsnum-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/itsnum-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/itsnum-com/hosts/itsnum-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/itsnum-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/itsnum-com/vendors/itsnum-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/itsnum-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://itsnum.com/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/itsnum-com/security/itsnum-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/itsnum-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://itsnum.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://itsnum.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://itsnum.com/guides/
- group: start
  title: ''
  type: Login
  url: https://app.itsnum.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://itsnum.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://itsnum.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://itsnum.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://itsnum.com/terms/
created: '2026-10-30'
description: itsnum.com provides a travel eSIM platform that allows users to purchase and activate mobile data plans for international travel instantly. The service offers a marketplace of destinations, flexible pricing, and a developer portal with APIs for managing eSIM orders, checking availability, and retrieving account information. Its public API is documented at itsnum.com/developers/ and includes OpenAPI specifications. The company focuses on seamless connectivity for travelers, offering support, pricing details, and privacy policies openly on its website.
image: https://itsnum.com/assets/og.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at itsnum.com.
  name: itsnum-com MCP Server
  slug: itsnum-com-mcp-yml
modified: '2026-10-30'
name: itsnum-com
nav: Providers
network: true
overview: 'itsnum-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Agent API. Tagged areas include Travel, eSIM, Telecom, Marketplace, and API.


  The itsnum-com catalog on APIs.io includes 1 Spectral governance ruleset.


  itsnum-com''s developer surface includes authentication, API reference, documentation, pricing, support, and 17 more developer resources.'
plans:
- name: Itsnum Com Plans Pricing
  plan_count: 7
  slug: itsnum-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Itsnum Com Rate Limits
  slug: itsnum-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: itsnum-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: itsnum-com-rules
scopes:
- name: Itsnum Com Scopes
  scope_count: 0
  slug: itsnum-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 45.3
    developer_ergonomics: 49.3
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 35.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Itsnum Com Authentication
  slug: itsnum-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Itsnum Com Domain Security
  slug: itsnum-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: get-place
  slug: itsnum-com-get-place
- name: search-places
  slug: itsnum-com-search-places
- name: submit-business
  slug: itsnum-com-submit-business
slug: itsnum-com
tags:
- Travel
- eSIM
- Telecom
- Marketplace
- API
- Company
website: https://itsnum.com/
---
