---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Vehicle safety recall notices API
  name: CarsMultiverse Recall API
  slug: carsmultiverse-recall-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/carsmultiverse-com/security/carsmultiverse-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/carsmultiverse-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/carsmultiverse-com/conformance/carsmultiverse-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carsmultiverse-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carsmultiverse-com/llms/carsmultiverse-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carsmultiverse-com-llms.txt
- group: other
  href: https://artifacts.apis.io/carsmultiverse-com/a2a/carsmultiverse-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/carsmultiverse-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/carsmultiverse-com/mcp/carsmultiverse-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/carsmultiverse-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/carsmultiverse-com/well-known/carsmultiverse-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carsmultiverse-com-security.txt
- group: auth
  href: https://artifacts.apis.io/carsmultiverse-com/well-known/carsmultiverse-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carsmultiverse-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/carsmultiverse-com/well-known/carsmultiverse-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carsmultiverse-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/carsmultiverse-com/hosts/carsmultiverse-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carsmultiverse-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/carsmultiverse-com/vendors/carsmultiverse-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carsmultiverse-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carsmultiverse.com/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: https://carsmultiverse.com/status/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carsmultiverse.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/carsmultiverse-com/security/carsmultiverse-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/carsmultiverse-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/carsmultiverse-com/security/carsmultiverse-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carsmultiverse-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carsmultiverse.com/
created: '2026-11-03'
description: CarsMultiverse is an independent website that archives every version of vehicle recall notices, allowing users to see how safety authorities update information after announcements. It aggregates official recall data, provides searchable archives, and offers tools for tracking changes, without being a government authority. Sources are cited on each page.
image: https://carsmultiverse.com/wp-content/uploads/cmv-cards/home-03b599ca34.png
layout: provider
mcp_servers:
- description: Remote MCP server at carsmultiverse.com.
  name: CarsMultiverse MCP Server
  slug: carsmultiverse-com-mcp-yml
modified: '2026-11-03'
name: CarsMultiverse
nav: Providers
network: true
overview: CarsMultiverse is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Data, Recall, Archives, and Open Data.
random_paper: 21
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 18.4
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carsmultiverse Com Domain Security
  slug: carsmultiverse-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Carsmultiverse Com Vulnerability Disclosure
  slug: carsmultiverse-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: carsmultiverse-com
tags:
- Automotive
- Data
- Recall
- Archives
- Open Data
website: https://carsmultiverse.com/
---
