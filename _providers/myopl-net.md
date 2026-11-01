---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 62.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Myopl Net Agentic Access
  operation_count: 3
  slug: myopl-net-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.myopl.net
  baseurl_source: declared
  description: The Mcp API from myopl-net — 3 operation(s) for mcp.
  name: myopl-net MCP API
  slug: myopl-net-mcp-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/myopl-net/agentic-access/myopl-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/myopl-net-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/myopl-net/plans/myopl-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/myopl-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/myopl-net/rules/myopl-net-rules.yml
  title: ''
  type: Spectral
  url: rules/myopl-net-rules.yml
- group: design
  href: https://artifacts.apis.io/myopl-net/json-ld/myopl-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/myopl-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/myopl-net/vocabulary/myopl-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/myopl-net-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/myopl-net/data-model/myopl-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/myopl-net-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://myopl.net/security-policy/
- group: auth
  href: https://artifacts.apis.io/myopl-net/authentication/myopl-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/myopl-net-authentication.yml
- group: design
  href: https://artifacts.apis.io/myopl-net/errors/myopl-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/myopl-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/myopl-net/conformance/myopl-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/myopl-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/myopl-net/llms/myopl-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/myopl-net-llms.txt
- group: other
  href: https://artifacts.apis.io/myopl-net/a2a/myopl-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/myopl-net-a2a.yml
- group: agent
  href: https://artifacts.apis.io/myopl-net/mcp/myopl-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/myopl-net-mcp.yml
- group: auth
  href: https://artifacts.apis.io/myopl-net/well-known/myopl-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/myopl-net-security.txt
- group: auth
  href: https://artifacts.apis.io/myopl-net/well-known/myopl-net-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/myopl-net-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/myopl-net/well-known/myopl-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/myopl-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/myopl-net/hosts/myopl-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/myopl-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/myopl-net/vendors/myopl-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/myopl-net-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://myopl.net/terms-and-conditions/
- group: start
  title: ''
  type: SignUp
  url: https://myopl.net/wiki/clubs/registering-a-new-club/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://myopl.net/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://myopl.net/wiki/get-started/
- group: docs
  title: ''
  type: APIReference
  url: https://myopl.net/developers/?utm_source=home&utm_medium=web
- group: auth
  href: https://artifacts.apis.io/myopl-net/scopes/myopl-net-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/myopl-net-scopes.yml
- group: auth
  href: https://artifacts.apis.io/myopl-net/security/myopl-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/myopl-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/myopl-net/security/myopl-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/myopl-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://myopl.net/
- group: docs
  title: ''
  type: Documentation
  url: https://myopl.net/openapi.json
created: '2026-10-30'
description: MYOPL is a platform that helps recreational pickleball players find local games, track match statistics, and build personal ratings. It offers tools for organizing rotating doubles matches, connecting community members, and enhancing the open‑play experience with real‑time scoring and social features. The service targets casual athletes seeking convenient ways to join games, improve skills, and engage with a vibrant pickleball community across multiple regions.
image: https://myopl.net/assets/MYOPL_App_Icon_512.png?v=20260824-1
json_schemas:
- name: McpRequest
  property_count: 0
  slug: myopl-net-mcp-request
- name: McpResponse
  property_count: 0
  slug: myopl-net-mcp-response
jsonld:
- class_count: 37
  name: Myopl Net Context
  property_count: 62
  slug: myopl-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at myopl.net.
  name: myopl-net MCP Server
  slug: myopl-net-mcp-yml
modified: '2026-10-30'
name: myopl-net
nav: Providers
network: true
overview: 'myopl-net publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: MCP API. Tagged areas include Company, Pickleball, Sports, Community, and Platform.


  The myopl-net catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  myopl-net''s developer surface includes authentication, signup flow, getting-started guide, API reference, documentation, and 23 more developer resources.'
plans:
- name: Myopl Net Plans Pricing
  plan_count: 3
  slug: myopl-net-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: myopl-net API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: myopl-net-rules
scopes:
- name: Myopl Net Scopes
  scope_count: 4
  slug: myopl-net-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 52.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 69.3
    developer_ergonomics: 40.5
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Myopl Net Authentication
  slug: myopl-net-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Myopl Net Domain Security
  slug: myopl-net-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Myopl Net Vulnerability Disclosure
  slug: myopl-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: myopl-net
tags:
- Company
- Pickleball
- Sports
- Community
- Platform
website: https://myopl.net/
---
