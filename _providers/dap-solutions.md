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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Dap Solutions Agentic Access
  operation_count: 22
  slug: dap-solutions-agentic-access
  summary_line: 22 operations · 5 acting
api_count: 3
apis:
- baseURL: https://bellwether.dap.solutions
  baseurl_source: declared
  description: The Change API from Dartmouth Advisory Partners — 1 operation(s) for change.
  name: Dartmouth Advisory Partners Change API
  slug: dap-solutions-change-api
- baseURL: https://dap.solutions
  baseurl_source: declared
  description: The Compute API from Dartmouth Advisory Partners — 13 operation(s) for compute.
  name: Dartmouth Advisory Partners Compute API
  slug: dap-solutions-compute-api
- baseURL: https://foundry.dap.solutions
  baseurl_source: declared
  description: The Compute Day Count To Settlement API from Dartmouth Advisory Partners — 1 operation(s) for compute day count to settlement.
  name: Dartmouth Advisory Partners Compute Day Count To Settlement API
  slug: dap-solutions-compute-day-count-to-settlement-api
- baseURL: https://foundry.dap.solutions
  baseurl_source: declared
  description: The Convert Unix Timestamp To Date API from Dartmouth Advisory Partners — 1 operation(s) for convert unix timestamp to date.
  name: Dartmouth Advisory Partners Convert Unix Timestamp To Date API
  slug: dap-solutions-convert-unix-timestamp-to-date-api
- baseURL: https://bellwether.dap.solutions
  baseurl_source: declared
  description: The Coverage API from Dartmouth Advisory Partners — 1 operation(s) for coverage.
  name: Dartmouth Advisory Partners Coverage API
  slug: dap-solutions-coverage-api
- baseURL: https://foundry.dap.solutions
  baseurl_source: declared
  description: The Decode Base64 To Text API from Dartmouth Advisory Partners — 1 operation(s) for decode base64 to text.
  name: Dartmouth Advisory Partners Decode Base64 To Text API
  slug: dap-solutions-decode-base64-to-text-api
- baseURL: https://foundry.dap.solutions
  baseurl_source: declared
  description: The Diff Two Line Lists API from Dartmouth Advisory Partners — 1 operation(s) for diff two line lists.
  name: Dartmouth Advisory Partners Diff Two Line Lists API
  slug: dap-solutions-diff-two-line-lists-api
- baseURL: https://bellwether.dap.solutions
  baseurl_source: declared
  description: The Recent API from Dartmouth Advisory Partners — 1 operation(s) for recent.
  name: Dartmouth Advisory Partners Recent API
  slug: dap-solutions-recent-api
- baseURL: https://bellwether.dap.solutions
  baseurl_source: declared
  description: The Search API from Dartmouth Advisory Partners — 1 operation(s) for search.
  name: Dartmouth Advisory Partners Search API
  slug: dap-solutions-search-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/dap-solutions/agentic-access/dap-solutions-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dap-solutions-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dap-solutions/rules/dap-solutions-rules.yml
  title: ''
  type: Spectral
  url: rules/dap-solutions-rules.yml
- group: design
  href: https://artifacts.apis.io/dap-solutions/json-ld/dap-solutions-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dap-solutions-context.jsonld
- group: design
  href: https://artifacts.apis.io/dap-solutions/vocabulary/dap-solutions-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dap-solutions-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dap-solutions/data-model/dap-solutions-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dap-solutions-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dap-solutions/security/dap-solutions-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dap-solutions-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/dap-solutions/errors/dap-solutions-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dap-solutions-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dap-solutions/conformance/dap-solutions-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dap-solutions-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dap-solutions/llms/dap-solutions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dap-solutions-llms.txt
- group: build
  href: https://artifacts.apis.io/dap-solutions/mcp/dap-solutions-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dap-solutions-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dap-solutions/mcp/dap-solutions-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dap-solutions-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dap-solutions/well-known/dap-solutions-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dap-solutions-security.txt
- group: auth
  href: https://artifacts.apis.io/dap-solutions/well-known/dap-solutions-foundry-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dap-solutions-foundry-security.txt
- group: auth
  href: https://artifacts.apis.io/dap-solutions/well-known/dap-solutions-bellwether-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dap-solutions-bellwether-security.txt
- group: agent
  href: https://artifacts.apis.io/dap-solutions/well-known/dap-solutions-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dap-solutions-well-known.yml
- group: other
  href: https://artifacts.apis.io/dap-solutions/hosts/dap-solutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dap-solutions-hosts.yml
- group: other
  href: https://artifacts.apis.io/dap-solutions/vendors/dap-solutions-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dap-solutions-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://dap.solutions/whats-new/
- group: docs
  title: ''
  type: APIReference
  url: https://dap.solutions/llms.txt
- group: auth
  href: https://artifacts.apis.io/dap-solutions/authentication/dap-solutions-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dap-solutions-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dap-solutions/security/dap-solutions-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dap-solutions-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dap-solutions/security/dap-solutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dap-solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dap.solutions/
- group: start
  title: ''
  type: GettingStarted
  url: https://dap.solutions/solutions/resources/start-here/
- group: operate
  title: ''
  type: Support
  url: https://dap.solutions/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dap.solutions/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dap.solutions/privacy/
created: '2026-11-04'
description: Dartmouth Advisory Partners (DAP) is an institutional governance‑technology firm based in Toronto. They compile what an organization has written about how it must operate into systems that run that way, and record the evidence that they did. Their solutions include governance systems, decision provenance, AI‑driven sovereign agents, and reporting tools for asset owners and managers.
image: https://dap.solutions/assets/social-card.png
json_schemas:
- name: Record
  property_count: 11
  slug: dap-solutions-record
jsonld:
- class_count: 2
  name: Dap Solutions Context
  property_count: 13
  slug: dap-solutions-context
layout: provider
mcp_servers:
- description: Remote MCP server at bellwether.dap.solutions.
  name: Dartmouth Advisory Partners MCP Server
  slug: dap-solutions-mcp-yml
modified: '2026-11-04'
name: Dartmouth Advisory Partners
nav: Providers
network: true
overview: 'Dartmouth Advisory Partners publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Change API, Compute API, Compute Day Count To Settlement API, and 6 more. Tagged areas include Governance, Artificial Intelligence, Toronto, Institutional, and Technology.


  The Dartmouth Advisory Partners catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dartmouth Advisory Partners'' developer surface includes changelog, API reference, authentication, getting-started guide, support, and 22 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Dartmouth Advisory Partners API Rules
  rule_count: 62
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 8
  slug: dap-solutions-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 59.2
    catalog_earned_first_party: 0.0
    catalog_gap: 55.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 57.7
    developer_ergonomics: 35.7
    discoverability: 70.0
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dap Solutions Authentication
  slug: dap-solutions-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Dap Solutions Domain Security
  slug: dap-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dap Solutions Vulnerability Disclosure
  slug: dap-solutions-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dap-solutions
tags:
- Governance
- Artificial Intelligence
- Toronto
- Institutional
- Technology
- Company
website: https://dap.solutions/
---
