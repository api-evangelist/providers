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
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Adsbiq Com Agentic Access
  operation_count: 14
  slug: adsbiq-com-agentic-access
  summary_line: 14 operations
api_count: 2
apis:
- baseURL: https://api.adsbiq.com
  baseurl_source: declared
  description: The Aircraft API from adsbiq-com — 7 operation(s) for aircraft.
  name: adsbiq-com Aircraft API
  slug: adsbiq-com-aircraft-api
- baseURL: https://api.adsbiq.com
  baseurl_source: declared
  description: The Airports API from adsbiq-com — 4 operation(s) for airports.
  name: adsbiq-com Airports API
  slug: adsbiq-com-airports-api
- baseURL: https://api.adsbiq.com
  baseurl_source: declared
  description: The Flights API from adsbiq-com — 2 operation(s) for flights.
  name: adsbiq-com Flights API
  slug: adsbiq-com-flights-api
- baseURL: https://api.adsbiq.com
  baseurl_source: declared
  description: The Geographic API from adsbiq-com — 2 operation(s) for geographic.
  name: adsbiq-com Geographic API
  slug: adsbiq-com-geographic-api
- baseURL: https://api.adsbiq.com
  baseurl_source: declared
  description: The Network API from adsbiq-com — 1 operation(s) for network.
  name: adsbiq-com Network API
  slug: adsbiq-com-network-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/adsbiq-com/agentic-access/adsbiq-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adsbiq-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/adsbiq-com/rules/adsbiq-com-rules.yml
  title: ''
  type: Spectral
  url: rules/adsbiq-com-rules.yml
- group: design
  href: https://artifacts.apis.io/adsbiq-com/json-ld/adsbiq-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adsbiq-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/adsbiq-com/vocabulary/adsbiq-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adsbiq-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/adsbiq-com/data-model/adsbiq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adsbiq-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/adsbiq-com/security/adsbiq-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/adsbiq-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/adsbiq-com/errors/adsbiq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adsbiq-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adsbiq-com/conformance/adsbiq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adsbiq-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adsbiq-com/mcp/adsbiq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adsbiq-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/adsbiq-com/well-known/adsbiq-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adsbiq-com-security.txt
- group: auth
  href: https://artifacts.apis.io/adsbiq-com/well-known/adsbiq-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adsbiq-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/adsbiq-com/well-known/adsbiq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adsbiq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adsbiq-com/hosts/adsbiq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adsbiq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adsbiq-com/vendors/adsbiq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adsbiq-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adsbiq.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://adsbiq.com/status
- group: operate
  title: ''
  type: Roadmap
  url: https://adsbiq.com/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adsbiq.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adsbiq
- group: docs
  title: ''
  type: APIReference
  url: https://adsbiq.com/api/docs
- group: auth
  href: https://artifacts.apis.io/adsbiq-com/authentication/adsbiq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adsbiq-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/adsbiq-com/security/adsbiq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adsbiq-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/adsbiq-com/security/adsbiq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adsbiq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adsbiq.com/
created: '2026-10-30'
description: AdsBiQ provides a comprehensive advertising intelligence platform that aggregates, normalizes, and analyzes ad campaign data across multiple channels and networks. Their API enables developers to retrieve detailed metrics, audience insights, and performance reports, facilitating data-driven marketing decisions and automated reporting workflows. The company focuses on transparency, data accuracy, and scalable solutions for agencies and enterprises.
image: https://adsbiq.com/static/og-image.png
json_schemas:
- name: Airport
  property_count: 10
  slug: adsbiq-com-airport
- name: RouteActivity
  property_count: 5
  slug: adsbiq-com-route-activity
jsonld:
- class_count: 7
  name: Adsbiq Com Context
  property_count: 45
  slug: adsbiq-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at adsbiq.com.
  name: adsbiq-com MCP Server
  slug: adsbiq-com-mcp-yml
modified: '2026-10-30'
name: adsbiq-com
nav: Providers
network: true
overview: 'adsbiq-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aircraft API, Airports API, Flights API, and 2 more. Tagged areas include Advertising, Data Analytics, Marketing Technology, and Company.


  The adsbiq-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  adsbiq-com''s developer surface includes API reference, authentication, and 22 more developer resources.'
plans:
- name: Adsbiq Com Plans Pricing
  plan_count: 0
  slug: adsbiq-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: adsbiq-com API Rules
  rule_count: 15
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 0
  slug: adsbiq-com-rules
scopes:
- name: Adsbiq Com Scopes
  scope_count: 0
  slug: adsbiq-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 10.5
    contract_governance: 33.3
    contract_quality: 62.8
    developer_ergonomics: 15.5
    discoverability: 56.7
    operational_transparency: 23.7
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/adsbiq-com/adsbiq-com-2026-11-03T120314.png
security:
- kind: authentication
  name: Adsbiq Com Authentication
  slug: adsbiq-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Adsbiq Com Domain Security
  slug: adsbiq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adsbiq Com Vulnerability Disclosure
  slug: adsbiq-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: get-aircraft
  slug: adsbiq-com-get-aircraft
- name: nearby-aircraft
  slug: adsbiq-com-nearby-aircraft
- name: network-stats
  slug: adsbiq-com-network-stats
slug: adsbiq-com
tags:
- Advertising
- Data Analytics
- Marketing Technology
- Company
website: https://adsbiq.com/
---
