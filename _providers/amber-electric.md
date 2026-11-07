---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amber Electric Agentic Access
  operation_count: 5
  slug: amber-electric-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Amber's Consumer Data Right energy data-holder surface, mandated by the Australian CDR regime extended from banking into energy and administered by the ACCC with standards set by the Data Standards Bo
  name: Amber Electric Consumer Data Right Energy API
  slug: amber-electric-cdr-energy-api
- baseURL: https://public.cdr.amber.com.au/cds-au/v1
  baseurl_source: declared
  description: The Amber API from Amber Electric — 5 operation(s) for amber.
  name: Amber Electric Amber API
  slug: amber-electric-amber-api
artifact_total: 24
collections:
- collection_type: open
  name: Amber Electric Public API
  slug: open-amber-electric-public-api
common:
- group: other
  href: https://artifacts.apis.io/amber-electric/capabilities/amber-electric-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amber-electric-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/amber-electric/plans/amber-electric-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amber-electric-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/amber-electric/rules/amber-electric-rules.yml
  title: ''
  type: Spectral
  url: rules/amber-electric-rules.yml
- group: design
  href: https://artifacts.apis.io/amber-electric/json-ld/amber-electric-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amber-electric-context.jsonld
- group: design
  href: https://artifacts.apis.io/amber-electric/vocabulary/amber-electric-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amber-electric-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/amber-electric/hosts/amber-electric-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amber-electric-hosts.yml
- group: build
  href: https://artifacts.apis.io/amber-electric/integrations/amber-electric-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/amber-electric-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/amber-electric/vendors/amber-electric-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amber-electric-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.amber.com.au/hc/en-us/articles/360037454111-What-is-the-onboarding-process
- group: company
  title: ''
  type: Blog
  url: https://www.amber.com.au/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.amber.com.au/blog/rss.xml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/amberelectric/public-api/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/amberelectric/public-api/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/amber-electric/agentic-access/amber-electric-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amber-electric-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amber-electric/security/amber-electric-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amber-electric-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amber-electric/authentication/amber-electric-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amber-electric-authentication.yml
- group: build
  href: https://artifacts.apis.io/amber-electric/packages/amber-electric-packages.yml
  title: ''
  type: Packages
  url: packages/amber-electric-packages.yml
- group: build
  href: https://artifacts.apis.io/amber-electric/packages/amber-electric-packages.yml
  title: ''
  type: SDKs
  url: packages/amber-electric-packages.yml
- group: agent
  href: https://artifacts.apis.io/amber-electric/well-known/amber-electric-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amber-electric-well-known.yml
- group: agent
  href: https://artifacts.apis.io/amber-electric/mcp/amber-electric-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/amber-electric-mcp.yml
- group: other
  href: https://artifacts.apis.io/amber-electric/overlays/amber-electric-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amber-electric-public-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/amber-electric/conformance/amber-electric-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amber-electric-conformance.yml
- group: design
  href: https://artifacts.apis.io/amber-electric/errors/amber-electric-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amber-electric-problem-types.yml
- group: design
  href: https://artifacts.apis.io/amber-electric/lifecycle/amber-electric-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/amber-electric-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/amber-electric/conventions/amber-electric-conventions.yml
  title: ''
  type: Conventions
  url: conventions/amber-electric-conventions.yml
- group: operate
  href: https://artifacts.apis.io/amber-electric/rate-limits/amber-electric-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amber-electric-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/amber-electric/data-model/amber-electric-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amber-electric-data-model.yml
- group: build
  href: https://artifacts.apis.io/amber-electric/examples/amber-electric-examples.yml
  title: ''
  type: Examples
  url: examples/amber-electric-examples.yml
- group: auth
  href: https://artifacts.apis.io/amber-electric/scopes/amber-electric-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/amber-electric-scopes.yml
- group: agent
  href: https://artifacts.apis.io/amber-electric/skills/amber-electric-grid-renewables.md
  title: ''
  type: AgentSkill
  url: skills/amber-electric-grid-renewables.md
- group: agent
  href: https://artifacts.apis.io/amber-electric/skills/amber-electric-site-prices.md
  title: ''
  type: AgentSkill
  url: skills/amber-electric-site-prices.md
- group: agent
  href: https://artifacts.apis.io/amber-electric/skills/amber-electric-usage-history.md
  title: ''
  type: AgentSkill
  url: skills/amber-electric-usage-history.md
- group: company
  title: ''
  type: Website
  url: https://www.amber.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.amber.com.au/developers
- group: docs
  title: ''
  type: Documentation
  url: https://app.amber.com.au/developers/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://app.amber.com.au/developers/documentation
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/amberelectric/public-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amberelectric
- group: operate
  title: ''
  type: Support
  url: https://help.amber.com.au/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://github.com/amberelectric/public-api/discussions
- group: commercial
  title: ''
  type: Pricing
  url: https://www.amber.com.au/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amber.com.au/terms-and-conditions/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amber.com.au/legal/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.amber.com.au/signup
- group: start
  title: ''
  type: Login
  url: https://app.amber.com.au/sign-in
- group: operate
  title: ''
  type: StatusPage
  url: https://www.amber.com.au/status
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amberelectric/
created: '2026-07-27'
description: 'Amber Electric is an Australian electricity retailer (ABN 98623603805) that sells wholesale National Electricity Market pricing straight through to residential customers on a flat monthly membership, rather than marking energy up, and automates home batteries, solar exports and EV charging against those half-hourly prices. It sits at the retail end of the Australian energy value chain, between AEMO''s wholesale market and the household meter. Its API posture is unusually honest and unusually split. Amber publishes a real, verbatim OpenAPI 3.0.0 contract for a REST API at https://api.amber.com.au/v1 covering sites, prices, forecasts and usage, but the token that unlocks it is generated inside the logged-in customer app at https://app.amber.com.au/developers, so the API is customer-account-required rather than self-serve — a developer who is not an Amber customer cannot obtain a key. One endpoint is the exception: the spec explicitly declares `security: []` on GET /state/{state}/renewables/current,
  and that grid renewables-percentage feed really does answer anonymously for NSW, VIC, QLD and SA, so open market data and gated consumer data live inside the same contract. Separately, Amber is a designated Consumer Data Right energy data holder that is genuinely live, not merely designated: it is listed on the ACCC CDR Register with a working public base URI at https://public.cdr.amber.com.au, whose CDS discovery endpoints and anonymously-served OpenID Connect configuration advertise the full Consumer Data Standards energy scope set behind private_key_jwt and CDR accreditation.'
finops:
- has_sources: true
  method: derived
  name: Amber Electric Finops
  primary_unit: subscription
  service_category: ''
  slug: amber-electric-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amber-electric.png
json_schemas:
- name: ActualInterval
  property_count: 13
  slug: amber-electric-actual-interval
- name: ActualRenewable
  property_count: 8
  slug: amber-electric-actual-renewable
- name: CurrentInterval
  property_count: 15
  slug: amber-electric-current-interval
- name: CurrentRenewable
  property_count: 8
  slug: amber-electric-current-renewable
- name: ForecastInterval
  property_count: 14
  slug: amber-electric-forecast-interval
- name: ForecastRenewable
  property_count: 8
  slug: amber-electric-forecast-renewable
- name: Site
  property_count: 7
  slug: amber-electric-site
- name: Usage
  property_count: 17
  slug: amber-electric-usage
jsonld:
- class_count: 10
  name: Amber Electric Context
  property_count: 28
  slug: amber-electric-context
layout: provider
modified: '2026-10-21'
name: Amber Electric
nav: Providers
network: true
overview: 'Amber Electric publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Amber API, and 1 more. Tagged areas include Energy, Australia, Electricity, Utilities, and Consumer Data Right.


  The Amber Electric catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amber Electric''s developer surface includes getting-started guide, engineering blog, authentication, code examples, documentation, API reference, support, and 40 more developer resources.'
plans:
- name: Amber Electric Plans Pricing
  plan_count: 1
  slug: amber-electric-plans-pricing
- name: Amber Electric Price Estimates
  plan_count: 0
  slug: amber-electric-price-estimates
random_paper: 15
rate_limits:
- limit_count: 1
  name: Amber Electric Rate Limits
  slug: amber-electric-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Amber Electric API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: amber-electric-rules
scopes:
- name: Amber Electric Scopes
  scope_count: 16
  slug: amber-electric-scopes
  summary_line: 16 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 36
    catalog_earned: 81.8
    catalog_earned_first_party: 16.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 51.3
    contract_governance: 35.6
    contract_quality: 70.3
    developer_ergonomics: 58.9
    discoverability: 66.1
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 66.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/amber-electric/amber-electric-2026-08-07T161314.png
security:
- kind: authentication
  name: Amber Electric Authentication
  slug: amber-electric-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Amber Electric Domain Security
  slug: amber-electric-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: amber-electric-grid-renewables
  slug: amber-electric-grid-renewables
- name: amber-electric-site-prices
  slug: amber-electric-site-prices
- name: amber-electric-usage-history
  slug: amber-electric-usage-history
slug: amber-electric
tags:
- Energy
- Australia
- Electricity
- Utilities
- Consumer Data Right
- Energy Markets
- Renewables
- Solar
- Batteries
- DER
- Smart Metering
- Wholesale Pricing
website: https://www.amber.com.au/
---
