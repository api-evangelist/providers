---
access_model:
  confidence: high
  label: Free and open — no signup, no key
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cheniere Energy's corporate website. It carries no developer documentation and no API reference; supplier and contractor integration is handled through a dedicated portal. The company's one public API
  name: Cheniere Energy Website
  slug: website
- baseURL: https://lngconnectionapi.cheniere.com
  baseurl_source: declared
  description: Operationally available and unsubscribed capacity postings by nomination cycle.
  name: Cheniere Energy Capacity API
  slug: cheniere-energy-capacity-api
- baseURL: https://lngconnectionapi.cheniere.com
  baseurl_source: declared
  description: The posting page tree and the TSPs served.
  name: Cheniere Energy Discovery API
  slug: cheniere-energy-discovery-api
- baseURL: https://lngconnectionapi.cheniere.com
  baseurl_source: declared
  description: Documents attached to posting pages.
  name: Cheniere Energy Documents API
  slug: cheniere-energy-documents-api
- baseURL: https://lngconnectionapi.cheniere.com
  baseurl_source: declared
  description: Daily, comingled and mainline gas-quality analyses.
  name: Cheniere Energy Gas Quality API
  slug: cheniere-energy-gas-quality-api
- baseURL: https://lngconnectionapi.cheniere.com
  baseurl_source: declared
  description: Posted imbalance reports.
  name: Cheniere Energy Imbalances API
  slug: cheniere-energy-imbalances-api
- baseURL: https://lngconnectionapi.cheniere.com
  baseurl_source: declared
  description: Quarterly Index of Customers postings.
  name: Cheniere Energy Index of Customers API
  slug: cheniere-energy-index-of-customers-api
- baseURL: https://lngconnectionapi.cheniere.com
  baseurl_source: declared
  description: Critical and non-critical operational notices.
  name: Cheniere Energy Notices API
  slug: cheniere-energy-notices-api
- baseURL: https://lngconnectionapi.cheniere.com
  baseurl_source: declared
  description: Locations, stations, contacts, legends and footers.
  name: Cheniere Energy Reference Data API
  slug: cheniere-energy-reference-data-api
- baseURL: https://lngconnectionapi.cheniere.com
  baseurl_source: declared
  description: Client-side error reporting sink.
  name: Cheniere Energy Telemetry API
  slug: cheniere-energy-telemetry-api
- baseURL: https://lngconnectionapi.cheniere.com
  baseurl_source: declared
  description: Firm, interruptible and capacity-release transactional reporting.
  name: Cheniere Energy Transactional Reporting API
  slug: cheniere-energy-transactional-reporting-api
artifact_total: 25
common:
- group: commercial
  href: https://artifacts.apis.io/cheniere-energy/finops/cheniere-energy-finops.yml
  title: ''
  type: FinOps
  url: finops/cheniere-energy-finops.yml
- group: auth
  href: https://artifacts.apis.io/cheniere-energy/security/cheniere-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cheniere-energy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cheniere-energy-inc
- group: company
  title: ''
  type: Website
  url: https://www.cheniere.com
- group: start
  title: ''
  type: SupplierPortal
  url: https://www.cheniere.com/about/resources/suppliers-and-contractors
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.cheniere.com/investors
- group: company
  title: ''
  type: Careers
  url: https://www.cheniere.com/careers
- group: operate
  title: ''
  type: ContactUs
  url: https://www.cheniere.com/contact-us
- group: other
  title: ''
  type: Operations
  url: ''
- group: other
  title: ''
  type: Services
  url: ''
- group: other
  title: ''
  type: Sustainability
  url: https://www.cheniere.com/our-responsibility
- group: company
  title: ''
  type: Newsroom
  url: https://www.cheniere.com/newsroom
- group: other
  title: ''
  type: Operations
  url: https://www.cheniere.com/about/where-we-work
- group: docs
  href: https://artifacts.apis.io/cheniere-energy/openapi/_original/cheniere-energy-lng-connection.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/cheniere-energy-lng-connection.yml
- group: other
  href: https://artifacts.apis.io/cheniere-energy/overlays/cheniere-energy-lng-connection-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cheniere-energy-lng-connection-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/cheniere-energy/mcp/cheniere-energy-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cheniere-energy-mcp.yml
- group: build
  href: https://artifacts.apis.io/cheniere-energy/mcp/cheniere-energy-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cheniere-energy-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/cheniere-energy/authentication/cheniere-energy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cheniere-energy-authentication.yml
- group: design
  href: https://artifacts.apis.io/cheniere-energy/errors/cheniere-energy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cheniere-energy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cheniere-energy/conventions/cheniere-energy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cheniere-energy-conventions.yml
- group: design
  href: https://artifacts.apis.io/cheniere-energy/data-model/cheniere-energy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cheniere-energy-data-model.yml
- group: design
  href: https://artifacts.apis.io/cheniere-energy/conformance/cheniere-energy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cheniere-energy-conformance.yml
- group: design
  href: https://artifacts.apis.io/cheniere-energy/lifecycle/cheniere-energy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cheniere-energy-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cheniere-energy/rate-limits/cheniere-energy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cheniere-energy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cheniere-energy/plans/cheniere-energy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cheniere-energy-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/cheniere-energy/packages/cheniere-energy-packages.yml
  title: ''
  type: Packages
  url: packages/cheniere-energy-packages.yml
- group: agent
  href: https://artifacts.apis.io/cheniere-energy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cheniere-energy/llms/cheniere-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cheniere-energy-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cheniere.com/about/resources/privacypolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cheniere.com/about/resources/disclaimer
- group: company
  title: ''
  type: InvestorRelations
  url: https://cqpir.cheniere.com/
- group: operate
  title: ''
  type: Support
  url: https://www.cheniere.com/letstalk
created: '2026-03-21'
description: 'Cheniere Energy, Inc. is an international energy company headquartered in Houston, Texas, and the leading producer and exporter of liquefied natural gas (LNG) in the United States, operating the Sabine Pass terminal in Louisiana and the Corpus Christi terminal in Texas. It also owns two FERC-regulated interstate natural gas pipelines, Cheniere Creole Trail Pipeline and Cheniere Corpus Christi Pipeline. Cheniere runs no developer program and publishes no API documentation, yet it does operate one public, unauthenticated JSON API: the LNG Connection informational-postings API at lngconnectionapi.cheniere.com, serving the pipeline capacity, transactional reporting, Index of Customers, gas quality, imbalance and notice postings that FERC 18 CFR 284.13 requires, in the NAESB Wholesale Gas Quadrant data model.'
finops:
- has_sources: false
  method: generated
  name: Cheniere Energy Finops
  primary_unit: request
  service_category: API
  slug: cheniere-energy-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cheniere-energy.png
layout: provider
mcp_servers:
- description: MCP server; 12 tools listed. A candidate, not confirmed as published by the provider.
  name: Cheniere Energy MCP Server
  slug: cheniere-energy-mcp-yml
modified: '2026-09-16'
name: Cheniere Energy
nav: Providers
network: true
overview: 'Cheniere Energy publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Capacity API, Discovery API, Documents API, and 8 more. Tagged areas include Corpus Christi, Energy, Export, FERC, and Houston.


  The Cheniere Energy catalog on APIs.io includes 1 Spectral governance ruleset.


  Cheniere Energy''s developer surface includes authentication, support, and 28 more developer resources.'
plans:
- name: Cheniere Energy Plans Pricing
  plan_count: 0
  slug: cheniere-energy-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Cheniere Energy Rate Limits
  slug: cheniere-energy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Cheniere Energy API Rules
  rule_count: 57
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 6
  slug: cheniere-energy-rules
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 12.6
    developer_ergonomics: 18.5
    discoverability: 58.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 21.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cheniere-energy/cheniere-energy-2026-06-20T174259.png
security:
- kind: authentication
  name: Cheniere Energy Authentication
  slug: cheniere-energy-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cheniere Energy Domain Security
  slug: cheniere-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: cheniere-check-available-capacity
  slug: cheniere-energy-check-available-capacity
- name: cheniere-pull-transactional-reporting
  slug: cheniere-energy-pull-transactional-reporting
slug: cheniere-energy
tags:
- Corpus Christi
- Energy
- Export
- FERC
- Houston
- Informational Postings
- LNG
- Liquefaction
- NAESB
- Natural Gas
- Open Data
- Pipelines
- Regasification
- Sabine Pass
- Texas
use_cases:
- name: International LNG Export
- name: Long-Term LNG Supply Contracts
- name: Spot LNG Cargo Sales
- name: Energy Security
- name: Natural Gas Liquefaction Services
website: https://www.cheniere.com
---
