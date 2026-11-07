---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Endeavour Energy Agentic Access
  operation_count: 32
  slug: endeavour-energy-agentic-access
  summary_line: 32 operations
api_count: 2
apis:
- baseURL: https://data.endeavourenergy.com.au/api/explore/v2.1
  baseurl_source: declared
  description: API to enumerate datasets
  name: Endeavour Energy Catalog API
  slug: endeavour-energy-catalog-api
- baseURL: https://data.endeavourenergy.com.au/api/explore/v2.1
  baseurl_source: declared
  description: API to work on records
  name: Endeavour Energy Dataset API
  slug: endeavour-energy-dataset-api
artifact_total: 24
collections:
- collection_type: open
  name: Explore API
  slug: open-endeavour-energy-open-data-explore-api-v2-0
- collection_type: open
  name: Explore API
  slug: open-endeavour-energy-open-data-explore-api-v2-1
common:
- group: design
  href: https://artifacts.apis.io/endeavour-energy/rules/endeavour-energy-rules.yml
  title: ''
  type: Spectral
  url: rules/endeavour-energy-rules.yml
- group: design
  href: https://artifacts.apis.io/endeavour-energy/json-ld/endeavour-energy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/endeavour-energy-context.jsonld
- group: design
  href: https://artifacts.apis.io/endeavour-energy/vocabulary/endeavour-energy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/endeavour-energy-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/endeavour-energy/overlays/endeavour-energy-catalog-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/endeavour-energy-catalog-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/endeavour-energy/well-known/endeavour-energy-data-portal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/endeavour-energy-data-portal-security.txt
- group: other
  href: https://artifacts.apis.io/endeavour-energy/hosts/endeavour-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/endeavour-energy-hosts.yml
- group: other
  href: https://artifacts.apis.io/endeavour-energy/vendors/endeavour-energy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/endeavour-energy-vendors.yml
- group: other
  href: https://artifacts.apis.io/endeavour-energy/capabilities/endeavour-energy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/endeavour-energy-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/endeavour-energy/agentic-access/endeavour-energy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/endeavour-energy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/endeavour-energy/security/endeavour-energy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/endeavour-energy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/endeavour-energy/security/endeavour-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/endeavour-energy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/endeavour-energy/authentication/endeavour-energy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/endeavour-energy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.endeavourenergy.com.au/
- group: start
  title: ''
  type: Portal
  url: https://data.endeavourenergy.com.au/pages/home/
- group: docs
  title: ''
  type: Documentation
  url: https://www.endeavourenergy.com.au/our-network/resilience-and-emergency-planning/nsw-emergency-backstop-mechanism
- group: docs
  title: ''
  type: Documentation
  url: https://www.endeavourenergy.com.au/for-your-home/solar-and-battery-options/flexible-exports
- group: docs
  title: ''
  type: Documentation
  url: https://www.endeavourenergy.com.au/our-network/network-demand-and-capacity/network-capacity-map
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.endeavourenergy.com.au/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/endeavour-energy/well-known/endeavour-energy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/endeavour-energy-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.endeavourenergy.com.au/.well-known/security.txt
- group: agent
  href: https://artifacts.apis.io/endeavour-energy/well-known/endeavour-energy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/endeavour-energy-well-known.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/endeavour-energy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCOCblQ8mMDZszyJIqX51vMw
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/endeavourenergy
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/endeavourenergy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.endeavourenergy.com.au/pages/home/
- group: docs
  title: ''
  type: Documentation
  url: https://help.opendatasoft.com/apis/ods-explore-v2/explore_v2.1.html
- group: docs
  title: ''
  type: APIReference
  url: https://data.endeavourenergy.com.au/api-console/explore/v2.1/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.opendatasoft.com/apis/ods-explore-v2/explore_v2.1.html#section/Getting-Started
- group: operate
  title: ''
  type: Support
  url: https://www.endeavourenergy.com.au/about-us/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.endeavourenergy.com.au/about-us/newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.endeavourenergy.com.au/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://data.endeavourenergy.com.au/login/
- group: design
  href: https://artifacts.apis.io/endeavour-energy/components/endeavour-energy-components.yml
  title: ''
  type: Components
  url: components/endeavour-energy-components.yml
- group: agent
  href: https://artifacts.apis.io/endeavour-energy/mcp/endeavour-energy-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/endeavour-energy-mcp.yml
- group: design
  href: https://artifacts.apis.io/endeavour-energy/conformance/endeavour-energy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/endeavour-energy-conformance.yml
- group: design
  href: https://artifacts.apis.io/endeavour-energy/errors/endeavour-energy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/endeavour-energy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/endeavour-energy/lifecycle/endeavour-energy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/endeavour-energy-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.opendatasoft.com/apis/ods-explore-v2/explore_v2.1.html#section/Versioning/Deprecation-warnings
- group: operate
  href: https://artifacts.apis.io/endeavour-energy/changelog/endeavour-energy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/endeavour-energy-changelog.yml
- group: auth
  href: https://artifacts.apis.io/endeavour-energy/scopes/endeavour-energy-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/endeavour-energy-scopes.yml
- group: design
  href: https://artifacts.apis.io/endeavour-energy/conventions/endeavour-energy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/endeavour-energy-conventions.yml
- group: design
  href: https://artifacts.apis.io/endeavour-energy/conventions/endeavour-energy-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/endeavour-energy-conventions.yml
- group: operate
  href: https://artifacts.apis.io/endeavour-energy/rate-limits/endeavour-energy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/endeavour-energy-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/endeavour-energy/data-model/endeavour-energy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/endeavour-energy-data-model.yml
- group: start
  href: https://artifacts.apis.io/endeavour-energy/sandbox/endeavour-energy-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/endeavour-energy-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/endeavour-energy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-27'
description: 'Endeavour Energy is the regulated electricity distribution network service provider (DNSP) for Greater Western Sydney, the Blue Mountains, the Illawarra, the Southern Highlands, the South Coast and Central West of New South Wales, Australia, delivering power to around 2.8 million people over the poles-and-wires network it owns and operates. It sits between transmission and retail in the value chain - it moves electricity and hosts the meters, but it does not sell energy to consumers, so it holds no retail billing relationship. Its API posture is a sharp split. On the market and network side it is genuinely open: a live Opendatasoft portal at data.endeavourenergy.com.au serves eight network datasets (poles, conductors, distribution districts, other network assets, distribution substation available capacity, and live planned/unplanned/single-premise outages) through a documented, anonymous, no-key REST Explore API with a downloadable OpenAPI 3.0.3 contract, most of it under the
  Open Database Licence. On the consumer side it is closed and, more importantly, unobligated: Australia''s Consumer Data Right was extended to energy, but the designation put the data-holder obligation on electricity retailers as primary holders and AEMO as the secondary holder and gateway, not on distributors. Endeavour Energy appears nowhere in the 84 brands of the CDR energy data holder register, publishes no CDR base URI, and makes no reference to the Consumer Data Right anywhere on its corporate site. It does operate a CSIP-AUS (Common Smart Inverter Profile - Australia) utility server for NSW flexible exports and the emergency backstop mechanism, but that machine interface is device-facing and entirely undocumented publicly. The open data portal itself is not linked from the corporate website.'
image: https://www.endeavourenergy.com.au/images/ee-logo.svg
json_schemas:
- name: attachment
  property_count: 2
  slug: endeavour-energy-attachment
- name: dataset
  property_count: 2
  slug: endeavour-energy-dataset
- name: datasets
  property_count: 3
  slug: endeavour-energy-datasets
- name: facet_enumeration
  property_count: 2
  slug: endeavour-energy-facet-enumeration
- name: links
  property_count: 2
  slug: endeavour-energy-links
- name: record
  property_count: 2
  slug: endeavour-energy-record
- name: records
  property_count: 3
  slug: endeavour-energy-records
jsonld:
- class_count: 10
  name: Endeavour Energy Context
  property_count: 10
  slug: endeavour-energy-context
layout: provider
modified: '2026-10-21'
name: Endeavour Energy
nav: Providers
network: true
overview: 'Endeavour Energy publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Catalog API and Dataset API. Tagged areas include Energy, Australia, Utilities, Electricity, and Grid.


  The Endeavour Energy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Endeavour Energy''s developer surface includes authentication, developer portal, documentation, YouTube channel, API reference, getting-started guide, support, and 40 more developer resources.'
plans:
- name: Endeavour Energy Plans Pricing
  plan_count: 0
  slug: endeavour-energy-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Endeavour Energy Rate Limits
  slug: endeavour-energy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Endeavour Energy API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: endeavour-energy-rules
scopes:
- name: Endeavour Energy Scopes
  scope_count: 1
  slug: endeavour-energy-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 36
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 70.8
    developer_ergonomics: 66.1
    discoverability: 83.9
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 42.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/endeavour-energy/endeavour-energy-2026-08-07T164855.png
security:
- kind: authentication
  name: Endeavour Energy Authentication
  slug: endeavour-energy-authentication
  summary_line: none/apiKey/oauth2 · 5 schemes
- kind: domain-security
  name: Endeavour Energy Domain Security
  slug: endeavour-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Endeavour Energy Vulnerability Disclosure
  slug: endeavour-energy-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: endeavour-energy-discover-datasets
  slug: endeavour-energy-discover-datasets
- name: endeavour-energy-export-network-assets
  slug: endeavour-energy-export-network-assets
- name: endeavour-energy-find-substation-capacity
  slug: endeavour-energy-find-substation-capacity
- name: endeavour-energy-track-live-outages
  slug: endeavour-energy-track-live-outages
slug: endeavour-energy
tags:
- Energy
- Australia
- Utilities
- Electricity
- Grid
- Open Data
- Energy Networks
- Distribution
- Outages
- Consumer Data Right
- Smart Metering
- DER
- Solar
- Renewables
website: https://www.endeavourenergy.com.au/
---
