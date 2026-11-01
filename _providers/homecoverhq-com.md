---
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Homecoverhq Com Agentic Access
  operation_count: 12
  slug: homecoverhq-com-agentic-access
  summary_line: 12 operations · 10 acting
api_count: 1
apis:
- baseURL: https://homecoverhq.com
  baseurl_source: declared
  description: dataset
  name: homecoverhq-com Dataset API
  slug: homecoverhq-com-dataset-api
- baseURL: https://homecoverhq.com
  baseurl_source: declared
  description: enquiry
  name: homecoverhq-com Enquiry API
  slug: homecoverhq-com-enquiry-api
- baseURL: https://homecoverhq.com
  baseurl_source: declared
  description: The mcp API from homecoverhq-com — 1 operation(s) for mcp.
  name: homecoverhq-com MCP API
  slug: homecoverhq-com-mcp-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/homecoverhq-com/agentic-access/homecoverhq-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/homecoverhq-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/homecoverhq-com/rules/homecoverhq-com-rules.yml
  title: ''
  type: Spectral
  url: rules/homecoverhq-com-rules.yml
- group: design
  href: https://artifacts.apis.io/homecoverhq-com/vocabulary/homecoverhq-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/homecoverhq-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/homecoverhq-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://homecoverhq.com/terms
- group: auth
  href: https://artifacts.apis.io/homecoverhq-com/authentication/homecoverhq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/homecoverhq-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/homecoverhq-com/errors/homecoverhq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/homecoverhq-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/homecoverhq-com/conformance/homecoverhq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/homecoverhq-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/homecoverhq-com/overlays/homecoverhq-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/homecoverhq-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/homecoverhq-com/llms/homecoverhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/homecoverhq-com-llms.txt
- group: build
  href: https://artifacts.apis.io/homecoverhq-com/mcp/homecoverhq-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/homecoverhq-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/homecoverhq-com/mcp/homecoverhq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/homecoverhq-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/homecoverhq-com/well-known/homecoverhq-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/homecoverhq-com-security.txt
- group: agent
  href: https://artifacts.apis.io/homecoverhq-com/well-known/homecoverhq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/homecoverhq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/homecoverhq-com/hosts/homecoverhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/homecoverhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/homecoverhq-com/vendors/homecoverhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/homecoverhq-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/homecoverhq-com/packages/homecoverhq-com-packages.yml
  title: ''
  type: SDKs
  url: packages/homecoverhq-com-packages.yml
- group: build
  href: https://artifacts.apis.io/homecoverhq-com/packages/homecoverhq-com-packages.yml
  title: ''
  type: Packages
  url: packages/homecoverhq-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/homecoverhq-com/security/homecoverhq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/homecoverhq-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/homecoverhq-com/security/homecoverhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/homecoverhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://homecoverhq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://homecoverhq.com/openapi.json
- group: start
  title: ''
  type: SignUp
  url: https://homecoverhq.com/quote/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://homecoverhq.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://homecoverhq.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://homecoverhq.com/#enquire
created: '2026-10-30'
description: HomeCover HQ provides measured US renters and homeowners insurance premium data, aggregating NAIC filings and Census records for over 44 million renter households. It offers an API (OpenAPI 3.1) exposing datasets, analytics tools, and a consumer quote service, enabling developers and agents to retrieve rates, compare datasets, and submit enquiries.
image: https://homecoverhq.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at homecoverhq.com.
  name: homecoverhq-com MCP Server
  slug: homecoverhq-com-mcp-yml
modified: '2026-10-30'
name: homecoverhq-com
nav: Providers
network: true
overview: 'homecoverhq-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API, Enquiry API, and MCP API. Tagged areas include Company, Insurance, Data, RealEstate, and API.


  The homecoverhq-com catalog on APIs.io includes 1 Spectral governance ruleset.


  homecoverhq-com''s developer surface includes authentication, API reference, signup flow, support, and 22 more developer resources.'
plans:
- name: Homecoverhq Com Plans Pricing
  plan_count: 0
  slug: homecoverhq-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Homecoverhq Com Rate Limits
  slug: homecoverhq-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: homecoverhq-com API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 1
  slug: homecoverhq-com-rules
scopes:
- name: Homecoverhq Com Scopes
  scope_count: 0
  slug: homecoverhq-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 48.8
    developer_ergonomics: 37.4
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 42.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Homecoverhq Com Authentication
  slug: homecoverhq-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Homecoverhq Com Domain Security
  slug: homecoverhq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Homecoverhq Com Vulnerability Disclosure
  slug: homecoverhq-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: homecoverhq-com-dataset
  slug: homecoverhq-com-dataset
- name: homecoverhq-com-enquiry
  slug: homecoverhq-com-enquiry
slug: homecoverhq-com
tags:
- Company
- Insurance
- Data
- RealEstate
- API
website: https://homecoverhq.com/
---
