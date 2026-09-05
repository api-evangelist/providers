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
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-09-04'
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
- baseURL: https://api.amber.com.au/v1
  baseurl_source: declared
  description: The Sites API from Amber Electric — 4 operation(s) for sites.
  name: Amber Electric Sites API
  slug: amber-electric-sites-api
- baseURL: https://api.amber.com.au/v1
  baseurl_source: declared
  description: The State API from Amber Electric — 1 operation(s) for state.
  name: Amber Electric State API
  slug: amber-electric-state-api
artifact_total: 9
collections:
- collection_type: open
  name: Amber Electric Public API
  slug: open-amber-electric-public-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/amberelectric/public-api/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/amberelectric/public-api/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amber-electric-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amber-electric-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amber-electric-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/amber-electric-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/amber-electric-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amber-electric-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amber-electric-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/amber-electric-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amber-electric-public-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/amber-electric-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amber-electric-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amber-electric-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amber-electric-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amber-electric-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amber-electric-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/amber-electric-examples.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/amber-electric-scopes.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/amber-electric-grid-renewables.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/amber-electric-site-prices.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/amber-electric-usage-history.md
- group: company
  title: ''
  type: Website
  url: https://amber.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.amber.com.au/developers
- group: docs
  title: ''
  type: Documentation
  url: https://app.amber.com.au/developers
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
- group: company
  title: ''
  type: Blog
  url: https://amber.com.au/blog
- group: operate
  title: ''
  type: Support
  url: https://help.amber.com.au/
- group: operate
  title: ''
  type: Community
  url: https://github.com/amberelectric/public-api/discussions
- group: commercial
  title: ''
  type: Pricing
  url: https://amber.com.au/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amber.com.au/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amber.com.au/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.amber.com.au/developers
created: '2026-07-27'
description: 'Amber Electric is an Australian electricity retailer (ABN 98623603805) that sells wholesale National Electricity Market pricing straight through to residential customers on a flat monthly membership, rather than marking energy up, and automates home batteries, solar exports and EV charging against those half-hourly prices. It sits at the retail end of the Australian energy value chain, between AEMO''s wholesale market and the household meter. Its API posture is unusually honest and unusually split. Amber publishes a real, verbatim OpenAPI 3.0.0 contract for a REST API at https://api.amber.com.au/v1 covering sites, prices, forecasts and usage, but the token that unlocks it is generated inside the logged-in customer app at https://app.amber.com.au/developers, so the API is customer-account-required rather than self-serve — a developer who is not an Amber customer cannot obtain a key. One endpoint is the exception: the spec explicitly declares `security: []` on GET /state/{state}/renewables/current,
  and that grid renewables-percentage feed really does answer anonymously for NSW, VIC, QLD and SA, so open market data and gated consumer data live inside the same contract. Separately, Amber is a designated Consumer Data Right energy data holder that is genuinely live, not merely designated: it is listed on the ACCC CDR Register with a working public base URI at https://public.cdr.amber.com.au, whose CDS discovery endpoints and anonymously-served OpenID Connect configuration advertise the full Consumer Data Standards energy scope set behind private_key_jwt and CDR accreditation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amber-electric.png
layout: provider
modified: '2026-07-27'
name: Amber Electric
nav: Providers
network: true
overview: 'Amber Electric publishes 2 APIs on the [APIs.io](https://apis.io/) network: Sites API and State API. Tagged areas include Energy, Australia, Electricity, Utilities, and Consumer Data Right.


  Amber Electric''s developer surface includes authentication, code examples, documentation, API reference, engineering blog, support, pricing, and 28 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 1
  name: Amber Electric Rate Limits
  slug: amber-electric-rate-limits
scopes:
- name: Amber Electric Scopes
  scope_count: 16
  slug: amber-electric-scopes
  summary_line: 16 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 53.4
    developer_ergonomics: 54.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 74.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amber-electric/refs/heads/main/screenshots/amber-electric-2026-08-07T161314.png
security:
- kind: authentication
  name: Amber Electric Authentication
  slug: amber-electric-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Amber Electric Domain Security
  slug: amber-electric-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
website: https://amber.com.au/
---
