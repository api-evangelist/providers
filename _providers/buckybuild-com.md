---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 65.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Buckybuild Com Agentic Access
  operation_count: 24
  slug: buckybuild-com-agentic-access
  summary_line: 24 operations · 6 acting
api_count: 1
apis:
- baseURL: https://buckybuild.com
  baseurl_source: declared
  description: Operations under `addresses`.
  name: Bucky Addresses API
  slug: buckybuild-com-addresses-api
- baseURL: https://buckybuild.com
  baseurl_source: declared
  description: Operations under `citations`.
  name: Bucky Citations API
  slug: buckybuild-com-citations-api
- baseURL: https://buckybuild.com
  baseurl_source: declared
  description: Operations under `coverage`.
  name: Bucky Coverage API
  slug: buckybuild-com-coverage-api
- baseURL: https://buckybuild.com
  baseurl_source: declared
  description: Operations under `credentials`.
  name: Bucky Credentials API
  slug: buckybuild-com-credentials-api
- baseURL: https://buckybuild.com
  baseurl_source: declared
  description: Deterministic feasibility analysis and AI interpretations of it.
  name: Bucky Feasibility API
  slug: buckybuild-com-feasibility-api
- baseURL: https://buckybuild.com
  baseurl_source: declared
  description: 'Design and build marketplace: items, builds, and map markers.'
  name: Bucky Marketplace API
  slug: buckybuild-com-marketplace-api
- baseURL: https://buckybuild.com
  baseurl_source: declared
  description: Resolve an address, coordinate, lot, parcel, or polygon into a site snapshot.
  name: Bucky Sites API
  slug: buckybuild-com-sites-api
- baseURL: https://buckybuild.com
  baseurl_source: declared
  description: Operations under `usage`.
  name: Bucky Usage API
  slug: buckybuild-com-usage-api
artifact_total: 22
common:
- group: auth
  href: https://artifacts.apis.io/buckybuild-com/well-known/buckybuild-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buckybuild-com-www-security.txt
- group: agent
  href: https://artifacts.apis.io/buckybuild-com/agentic-access/buckybuild-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buckybuild-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/buckybuild-com/plans/buckybuild-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buckybuild-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/buckybuild-com/rules/buckybuild-com-rules.yml
  title: ''
  type: Spectral
  url: rules/buckybuild-com-rules.yml
- group: design
  href: https://artifacts.apis.io/buckybuild-com/json-ld/buckybuild-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buckybuild-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/buckybuild-com/vocabulary/buckybuild-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buckybuild-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buckybuild-com/data-model/buckybuild-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buckybuild-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/buckybuild-com/conventions/buckybuild-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/buckybuild-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/buckybuild-com/conventions/buckybuild-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/buckybuild-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://buckybuild.com/en/terms
- group: design
  href: https://artifacts.apis.io/buckybuild-com/errors/buckybuild-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buckybuild-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/buckybuild-com/conformance/buckybuild-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buckybuild-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buckybuild-com/llms/buckybuild-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buckybuild-com-llms.txt
- group: other
  href: https://artifacts.apis.io/buckybuild-com/a2a/buckybuild-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/buckybuild-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/buckybuild-com/mcp/buckybuild-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buckybuild-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/buckybuild-com/well-known/buckybuild-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buckybuild-com-security.txt
- group: agent
  href: https://artifacts.apis.io/buckybuild-com/well-known/buckybuild-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buckybuild-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/buckybuild-com/hosts/buckybuild-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buckybuild-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/buckybuild-com/vendors/buckybuild-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buckybuild-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buckybuild.com/terms
- group: operate
  title: ''
  type: Support
  url: https://buckybuild.com/en/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buckybuild.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://buckybuild.com/en-us/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://buckybuild.com/en-us/press
- group: start
  title: ''
  type: Login
  url: https://buckybuild.com/en-us/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://buckybuild.com/en-us/developers
- group: company
  title: ''
  type: Blog
  url: https://buckybuild.com/en-us/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.buckybuild.com/docs/mcp/connect
- group: docs
  title: ''
  type: Documentation
  url: https://docs.buckybuild.com/
- group: docs
  title: ''
  type: APIReference
  url: https://buckybuild.com/en/changelog
- group: auth
  href: https://artifacts.apis.io/buckybuild-com/authentication/buckybuild-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buckybuild-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/buckybuild-com/security/buckybuild-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/buckybuild-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/buckybuild-com/security/buckybuild-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buckybuild-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buckybuild.com/
created: '2026-11-03'
description: Bucky provides a platform to visualize what can be built on any address, offering zoning, height, setbacks, and buildable area data sourced from official bylaws. Users can enter an address to see detailed building potential without needing an account, enabling developers and planners to integrate this data into applications.
image: https://buckybuild.com/api/og?title=See+what+you+can+build+at+any+address%2C+fully+sourced&description=Enter+an+address+and+see+what+you+can+build%3A+zoning%2C+height%2C+setbacks%2C+and+buildable+area%2C+each+cited+to+the+bylaw+it+came+from.+Free+preview%2C+no+account.
json_schemas:
- name: CreateFeasibilityAnalysis
  property_count: 9
  slug: buckybuild-com-create-feasibility-analysis
- name: CredentialSelf
  property_count: 4
  slug: buckybuild-com-credential-self
- name: FeasibilityAnalysis
  property_count: 11
  slug: buckybuild-com-feasibility-analysis
- name: ResolvedSiteContext
  property_count: 15
  slug: buckybuild-com-resolved-site-context
- name: ResolvedSite
  property_count: 16
  slug: buckybuild-com-resolved-site
- name: SiteCheck
  property_count: 11
  slug: buckybuild-com-site-check
jsonld:
- class_count: 24
  name: Buckybuild Com Context
  property_count: 96
  slug: buckybuild-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at buckybuild.com requiring OAuth.
  name: Bucky MCP Server
  slug: buckybuild-com-mcp-yml
modified: '2026-11-03'
name: Bucky
nav: Providers
network: true
overview: 'Bucky publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Addresses API, Citations API, Coverage API, and 5 more. Tagged areas include Real Estate, Zoning, Mapping, Data API, and Visualization.


  The Bucky catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bucky''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, API reference, authentication, and 27 more developer resources.'
plans:
- name: Buckybuild Com Plans Pricing
  plan_count: 4
  slug: buckybuild-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Bucky API Rules
  rule_count: 62
  severity_counts:
    error: 52
    hint: 0
    info: 3
    warn: 7
  slug: buckybuild-com-rules
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 61.6
    developer_ergonomics: 34.5
    discoverability: 65.8
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
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
  name: Buckybuild Com Authentication
  slug: buckybuild-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Buckybuild Com Domain Security
  slug: buckybuild-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Buckybuild Com Vulnerability Disclosure
  slug: buckybuild-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: buckybuild-com
tags:
- Real Estate
- Zoning
- Mapping
- Data API
- Visualization
- Company
website: https://buckybuild.com/
---
