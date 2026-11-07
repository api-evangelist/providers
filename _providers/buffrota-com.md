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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Buffrota Com Agentic Access
  operation_count: 12
  slug: buffrota-com-agentic-access
  summary_line: 12 operations · 10 acting
api_count: 1
apis:
- baseURL: https://buffrota.com
  baseurl_source: declared
  description: dataset
  name: Buffrota Dataset API
  slug: buffrota-com-dataset-api
- baseURL: https://buffrota.com
  baseurl_source: declared
  description: enquiry
  name: Buffrota Enquiry API
  slug: buffrota-com-enquiry-api
- baseURL: https://buffrota.com
  baseurl_source: declared
  description: The mcp API from Buffrota — 1 operation(s) for mcp.
  name: Buffrota MCP API
  slug: buffrota-com-mcp-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/buffrota-com/agentic-access/buffrota-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buffrota-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/buffrota-com/rules/buffrota-com-rules.yml
  title: ''
  type: Spectral
  url: rules/buffrota-com-rules.yml
- group: design
  href: https://artifacts.apis.io/buffrota-com/vocabulary/buffrota-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buffrota-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/buffrota-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://buffrota.com/terms
- group: design
  href: https://artifacts.apis.io/buffrota-com/errors/buffrota-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buffrota-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/buffrota-com/conformance/buffrota-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buffrota-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buffrota-com/llms/buffrota-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buffrota-com-llms.txt
- group: build
  href: https://artifacts.apis.io/buffrota-com/mcp/buffrota-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/buffrota-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/buffrota-com/mcp/buffrota-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buffrota-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/buffrota-com/well-known/buffrota-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buffrota-com-security.txt
- group: agent
  href: https://artifacts.apis.io/buffrota-com/well-known/buffrota-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buffrota-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/buffrota-com/hosts/buffrota-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buffrota-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/buffrota-com/vendors/buffrota-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buffrota-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buffrota.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buffrota.com/privacy/
- group: auth
  href: https://artifacts.apis.io/buffrota-com/authentication/buffrota-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buffrota-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/buffrota-com/security/buffrota-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/buffrota-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/buffrota-com/security/buffrota-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buffrota-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buffrota.com/
created: '2026-11-03'
description: Buffrota aggregates and publishes commercial floor stripping and cleaning rates across 13 US cleaning companies, providing verbatim quoted pricing data with dates. The site offers a searchable record of rates, vendor links, and a quote request tool, aiming to help facility managers compare costs transparently.
image: https://buffrota.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at buffrota.com.
  name: Buffrota MCP Server
  slug: buffrota-com-mcp-yml
modified: '2026-11-03'
name: Buffrota
nav: Providers
network: true
overview: 'Buffrota publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API, Enquiry API, and MCP API. Tagged areas include Data, Cleaning, Pricing, US, and Commercial.


  The Buffrota catalog on APIs.io includes 1 Spectral governance ruleset.


  Buffrota''s developer surface includes authentication and 19 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Buffrota API Rules
  rule_count: 53
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 6
  slug: buffrota-com-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.8
    developer_ergonomics: 13.7
    discoverability: 65.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
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
  name: Buffrota Com Authentication
  slug: buffrota-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Buffrota Com Domain Security
  slug: buffrota-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Buffrota Com Vulnerability Disclosure
  slug: buffrota-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: buffrota-com-dataset-search-and-stats
  slug: buffrota-com-dataset-search-and-stats
- name: buffrota-com-enquiry-process
  slug: buffrota-com-enquiry-process
slug: buffrota-com
tags:
- Data
- Cleaning
- Pricing
- US
- Commercial
website: https://buffrota.com/
---
