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
    agent_card: flavored
    agent_skills: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: MCP gateway providing 51 tools at https://mcp.aleeth.com/mcp, OAuth 2.0.
  name: ALEETH MCP
  slug: aleeth-mcp
- baseURL: https://ica.aleeth.com
  baseurl_source: declared
  description: 'ALEETH API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: ALEETH API
  slug: aleeth-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/aleeth-com/rules/aleeth-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aleeth-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aleeth-com/json-ld/aleeth-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aleeth-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/aleeth-com/vocabulary/aleeth-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aleeth-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aleeth-com/data-model/aleeth-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aleeth-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://aleeth.com/trust/
- group: design
  href: https://artifacts.apis.io/aleeth-com/conformance/aleeth-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aleeth-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aleeth-com/llms/aleeth-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aleeth-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aleeth-com/a2a/aleeth-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aleeth-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aleeth-com/mcp/aleeth-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aleeth-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aleeth-com/well-known/aleeth-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aleeth-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aleeth-com/well-known/aleeth-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aleeth-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aleeth-com/hosts/aleeth-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aleeth-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aleeth-com/vendors/aleeth-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aleeth-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://aleeth.com/status/
- group: auth
  href: https://artifacts.apis.io/aleeth-com/security/aleeth-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aleeth-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aleeth-com/security/aleeth-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aleeth-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aleeth-com/security/aleeth-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aleeth-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aleeth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aleeth.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://aleeth.com/doctrine/
- group: start
  title: ''
  type: GettingStarted
  url: https://aleeth.com/verify/
- group: company
  title: ''
  type: Blog
  url: https://aleeth.com/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aleeth.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aleeth.com/terms/
- group: auth
  title: ''
  type: Security
  url: https://aleeth.com/security/
coverage:
  checked: '2026-11-01'
  detail: Developers page lists MCP endpoint but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://aleeth.com/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ALEETH is the institutional control layer for autonomous AI. It provides a rail that issues, revokes, and proves permission for consequential AI actions, delivering signed, independently verifiable evidence that AI‑influenced decisions were authorized, supervised, and defensible. The platform serves as the control plane for autonomous AI, enabling boards, auditors, and regulators to verify AI actions without requiring login.
image: https://aleeth.com/icon-192.png
json_schemas:
- name: GetApiPublicDecisionLatencyResponse
  property_count: 5
  slug: aleeth-com-get-api-public-decision-latency-response
jsonld:
- class_count: 1
  name: Aleeth Com Context
  property_count: 5
  slug: aleeth-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.aleeth.com requiring OAuth.
  name: ALEETH MCP Server
  slug: aleeth-com-mcp-yml
modified: '2026-11-01'
name: ALEETH
nav: Providers
network: true
overview: 'ALEETH is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Governance, Control Plane, Autonomous AI, and InstitutionalControl.


  The ALEETH catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ALEETH''s developer surface includes documentation, getting-started guide, engineering blog, and 22 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: ALEETH API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: aleeth-com-rules
scopes:
- name: Aleeth Com Scopes
  scope_count: 0
  slug: aleeth-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 18.8
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 13.2
  previous_composite: 34.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aleeth Com Authentication
  slug: aleeth-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aleeth Com Domain Security
  slug: aleeth-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aleeth Com Vulnerability Disclosure
  slug: aleeth-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aleeth Com Trust Center
  slug: aleeth-com-trust-center
  summary_line: SOC 2, FedRAMP
slug: aleeth-com
tags:
- Artificial Intelligence
- Governance
- Control Plane
- Autonomous AI
- InstitutionalControl
website: https://aleeth.com/
---
