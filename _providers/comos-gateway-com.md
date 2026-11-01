---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
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
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 128
  human_in_the_loop: 2
  name: Comos Gateway Com Agentic Access
  operation_count: 128
  slug: comos-gateway-com-agentic-access
  summary_line: 128 operations · 128 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://mcp.comos-federation.com
  baseurl_source: declared
  description: The actions API from comos-gateway-com — 7 operation(s) for actions.
  name: comos-gateway-com Actions API
  slug: comos-gateway-com-actions-api
- baseURL: https://mcp.comos-federation.com
  baseurl_source: declared
  description: The Tools API from comos-gateway-com — 121 operation(s) for tools.
  name: comos-gateway-com Tools API
  slug: comos-gateway-com-tools-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/comos-gateway-com/agentic-access/comos-gateway-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/comos-gateway-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/comos-gateway-com/rules/comos-gateway-com-rules.yml
  title: ''
  type: Spectral
  url: rules/comos-gateway-com-rules.yml
- group: design
  href: https://artifacts.apis.io/comos-gateway-com/json-ld/comos-gateway-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/comos-gateway-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/comos-gateway-com/vocabulary/comos-gateway-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/comos-gateway-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/comos-gateway-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/comos-gateway-com/data-model/comos-gateway-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/comos-gateway-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/comos-gateway-com/conformance/comos-gateway-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/comos-gateway-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/comos-gateway-com/llms/comos-gateway-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/comos-gateway-com-llms.txt
- group: other
  href: https://artifacts.apis.io/comos-gateway-com/a2a/comos-gateway-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/comos-gateway-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/comos-gateway-com/mcp/comos-gateway-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/comos-gateway-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/comos-gateway-com/well-known/comos-gateway-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/comos-gateway-com-security.txt
- group: auth
  href: https://artifacts.apis.io/comos-gateway-com/well-known/comos-gateway-com-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/comos-gateway-com-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/comos-gateway-com/well-known/comos-gateway-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/comos-gateway-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/comos-gateway-com/hosts/comos-gateway-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/comos-gateway-com-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://comos-gateway.com/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://comos-gateway.com/terms
- group: auth
  title: ''
  type: Security
  url: https://comos-gateway.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://comos-gateway.com/privacy
- group: start
  title: ''
  type: Login
  url: https://comos-gateway.com/login
- group: auth
  href: https://artifacts.apis.io/comos-gateway-com/security/comos-gateway-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/comos-gateway-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/comos-gateway-com/security/comos-gateway-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comos-gateway-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://comos-gateway.com/
- group: docs
  title: ''
  type: Documentation
  url: https://comos-gateway.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://comos-gateway.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://comos-gateway.com/start
- group: operate
  title: ''
  type: Support
  url: https://comos-gateway.com/support
- group: company
  title: ''
  type: Blog
  url: https://comos-gateway.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://comos-gateway.com/pricing
created: '2026-10-30'
description: ComOS is a federation of federations enabling businesses to run their own complete digital world—including catalog, customers, and agents—while participating in a broader networked economy. The platform offers customizable, on‑premise solutions that empower enterprises to own their data and integrate seamlessly with partners, delivering scalable, secure, and extensible services for modern commerce.
image: https://comos-federation.com/comos-logo.svg
json_schemas:
- name: ToolCallResult
  property_count: 5
  slug: comos-gateway-com-tool-call-result
jsonld:
- class_count: 1
  name: Comos Gateway Com Context
  property_count: 5
  slug: comos-gateway-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at comos-gateway.com requiring OAuth.
  name: comos-gateway-com MCP Server
  slug: comos-gateway-com-mcp-yml
modified: '2026-10-30'
name: comos-gateway-com
nav: Providers
network: true
overview: 'comos-gateway-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Actions API and Tools API. Tagged areas include Company, Federation, OnPremise, Commerce, and API.


  The comos-gateway-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  comos-gateway-com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 22 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: comos-gateway-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: comos-gateway-com-rules
scopes:
- name: Comos Gateway Com Scopes
  scope_count: 0
  slug: comos-gateway-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 48.1
    developer_ergonomics: 42.1
    discoverability: 65.0
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
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Comos Gateway Com Authentication
  slug: comos-gateway-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Comos Gateway Com Domain Security
  slug: comos-gateway-com-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Comos Gateway Com Vulnerability Disclosure
  slug: comos-gateway-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: catalog-search
  slug: comos-gateway-com-catalog-search
slug: comos-gateway-com
tags:
- Company
- Federation
- OnPremise
- Commerce
- API
website: https://comos-gateway.com/
---
