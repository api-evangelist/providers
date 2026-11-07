---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Halo Agentic Access
  operation_count: 72
  slug: halo-agentic-access
  summary_line: 72 operations
api_count: 4
apis:
- baseURL: https://s3publicapis.azure-api.net/metadata
  baseurl_source: declared
  description: The H5 API from Halo — 44 operation(s) for h5.
  name: Halo H5 API
  slug: halo-h5-api
- baseURL: https://s3publicapis.azure-api.net/stats
  baseurl_source: declared
  description: The H5pc API from Halo — 3 operation(s) for h5pc.
  name: Halo H5pc API
  slug: halo-h5pc-api
- baseURL: https://s3publicapis.azure-api.net/metadata
  baseurl_source: declared
  description: The Hw2 API from Halo — 25 operation(s) for hw2.
  name: Halo Hw2 API
  slug: halo-hw2-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/halo/agentic-access/halo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/halo-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/halo/rate-limits/halo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/halo-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/halo/rules/halo-rules.yml
  title: ''
  type: Spectral
  url: rules/halo-rules.yml
- group: design
  href: https://artifacts.apis.io/halo/conventions/halo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/halo-conventions.yml
- group: design
  href: https://artifacts.apis.io/halo/errors/halo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/halo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/halo/conformance/halo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/halo-conformance.yml
- group: other
  href: https://artifacts.apis.io/halo/hosts/halo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/halo-hosts.yml
- group: other
  href: https://artifacts.apis.io/halo/vendors/halo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/halo-vendors.yml
- group: auth
  href: https://artifacts.apis.io/halo/authentication/halo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/halo-authentication.yml
- group: auth
  href: https://artifacts.apis.io/halo/security/halo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/halo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.haloapi.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.haloapi.com/terms-of-use
- group: docs
  title: ''
  type: APIReference
  url: https://developer.haloapi.com/apis
created: '2026-05-28'
description: 'The Halo Public API (Beta) is Microsoft''s game data API for Halo 5: Guardians and Halo Wars 2, published through an Azure API Management developer portal at developer.haloapi.com. It exposes four read-only REST APIs - Metadata, Profile, Stats and UGC (user-generated content) - authenticated with an Ocp-Apim-Subscription-Key obtained by subscribing to the Developer Access product, which is limited to 10 requests per 10 seconds. Use is governed by the Halo Game Data Terms of Use.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/halo.png
layout: provider
modified: '2026-11-05'
name: Halo
nav: Providers
network: true
overview: 'Halo publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: H5 API, H5pc API, and Hw2 API. Tagged areas include Game Data, Gaming, Halo, Microsoft, and Player Statistics.


  The Halo catalog on APIs.io includes 1 Spectral governance ruleset.


  Halo''s developer surface includes authentication, API reference, and 12 more developer resources.'
plans:
- name: Halo Plans Pricing
  plan_count: 0
  slug: halo-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Halo Rate Limits
  slug: halo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Halo API Rules
  rule_count: 38
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 4
  slug: halo-rules
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 27.9
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 46.5
    developer_ergonomics: 28.6
    discoverability: 78.6
    operational_transparency: 21.1
  previous_composite: 5.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/halo/halo-2026-06-20T182500.png
security:
- kind: authentication
  name: Halo Authentication
  slug: halo-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Halo Domain Security
  slug: halo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: halo
tags:
- Game Data
- Gaming
- Halo
- Microsoft
- Player Statistics
- Public APIs
- Video Games
- Xbox
website: https://developer.haloapi.com/
---
