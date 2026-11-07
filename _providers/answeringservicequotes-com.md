---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Answeringservicequotes Com Agentic Access
  operation_count: 12
  slug: answeringservicequotes-com-agentic-access
  summary_line: 12 operations · 10 acting
api_count: 1
apis:
- description: Provides pricing data for US answering service providers.
  name: Answering Service Quotes API
  slug: answeringservicequotes-api
- baseURL: https://answeringservicequotes.com
  baseurl_source: declared
  description: dataset
  name: Answering Service Quotes Dataset API
  slug: answeringservicequotes-com-dataset-api
- baseURL: https://answeringservicequotes.com
  baseurl_source: declared
  description: enquiry
  name: Answering Service Quotes Enquiry API
  slug: answeringservicequotes-com-enquiry-api
- baseURL: https://answeringservicequotes.com
  baseurl_source: declared
  description: The mcp API from Answering Service Quotes — 1 operation(s) for mcp.
  name: Answering Service Quotes MCP API
  slug: answeringservicequotes-com-mcp-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/answeringservicequotes-com/agentic-access/answeringservicequotes-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/answeringservicequotes-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/answeringservicequotes-com/rules/answeringservicequotes-com-rules.yml
  title: ''
  type: Spectral
  url: rules/answeringservicequotes-com-rules.yml
- group: design
  href: https://artifacts.apis.io/answeringservicequotes-com/vocabulary/answeringservicequotes-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/answeringservicequotes-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/answeringservicequotes-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://answeringservicequotes.com/terms
- group: auth
  href: https://artifacts.apis.io/answeringservicequotes-com/authentication/answeringservicequotes-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/answeringservicequotes-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/answeringservicequotes-com/lifecycle/answeringservicequotes-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/answeringservicequotes-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/answeringservicequotes-com/errors/answeringservicequotes-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/answeringservicequotes-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/answeringservicequotes-com/conformance/answeringservicequotes-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/answeringservicequotes-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/answeringservicequotes-com/llms/answeringservicequotes-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/answeringservicequotes-com-llms.txt
- group: build
  href: https://artifacts.apis.io/answeringservicequotes-com/mcp/answeringservicequotes-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/answeringservicequotes-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/answeringservicequotes-com/mcp/answeringservicequotes-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/answeringservicequotes-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/answeringservicequotes-com/well-known/answeringservicequotes-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/answeringservicequotes-com-security.txt
- group: agent
  href: https://artifacts.apis.io/answeringservicequotes-com/well-known/answeringservicequotes-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/answeringservicequotes-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/answeringservicequotes-com/hosts/answeringservicequotes-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/answeringservicequotes-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/answeringservicequotes-com/vendors/answeringservicequotes-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/answeringservicequotes-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/answeringservicequotes-com/security/answeringservicequotes-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/answeringservicequotes-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/answeringservicequotes-com/security/answeringservicequotes-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/answeringservicequotes-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://answeringservicequotes.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://answeringservicequotes.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://answeringservicequotes.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://answeringservicequotes.com/contact
coverage:
  checked: '2026-11-01'
  detail: OpenAPI spec at https://answeringservicequotes.com/openapi.json describes a different service, so no owned machine-readable contract is available.
  evidence:
  - status: 200
    url: https://answeringservicequotes.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Answering Service Quotes aggregates pricing information from nine US answering service and virtual receptionist providers, quoting each providers prices verbatim from their own pricing pages with the date read, and includes industry coverage for two sectors.
image: https://answeringservicequotes.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at answeringservicequotes.com requiring an API key.
  name: Answering Service Quotes MCP Server
  slug: answeringservicequotes-com-mcp-yml
modified: '2026-11-01'
name: Answering Service Quotes
nav: Providers
network: true
overview: 'Answering Service Quotes publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dataset API, Enquiry API, MCP API, and 1 more. Tagged areas include Pricing, Answering Service, US, Comparison, and Data.


  The Answering Service Quotes catalog on APIs.io includes 1 Spectral governance ruleset.


  Answering Service Quotes'' developer surface includes authentication, support, and 20 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Answering Service Quotes API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 1
  slug: answeringservicequotes-com-rules
scopes:
- name: Answeringservicequotes Com Scopes
  scope_count: 0
  slug: answeringservicequotes-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.8
    developer_ergonomics: 20.7
    discoverability: 56.7
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Answeringservicequotes Com Authentication
  slug: answeringservicequotes-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Answeringservicequotes Com Domain Security
  slug: answeringservicequotes-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Answeringservicequotes Com Vulnerability Disclosure
  slug: answeringservicequotes-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset-tools
  slug: answeringservicequotes-com-dataset-skill
slug: answeringservicequotes-com
tags:
- Pricing
- Answering Service
- US
- Comparison
- Data
website: https://answeringservicequotes.com/
---
