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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Bing Maps REST Services (dev.virtualearth.net/REST/v1) provide geocoding, reverse geocoding, routing, imagery, elevations, time zone, traffic and location recognition over HTTP with a Bing Maps ke
  name: Bing Maps REST Services
  slug: bing-maps
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/bingmaps/getting-started/bing-maps-api-best-practices
- group: design
  href: https://artifacts.apis.io/bing-maps/lifecycle/bing-maps-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bing-maps-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bing-maps/errors/bing-maps-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bing-maps-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/bing-maps/llms/bing-maps-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bing-maps-llms.txt
- group: auth
  href: https://artifacts.apis.io/bing-maps/well-known/bing-maps-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bing-maps-security.txt
- group: agent
  href: https://artifacts.apis.io/bing-maps/well-known/bing-maps-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bing-maps-well-known.yml
- group: other
  href: https://artifacts.apis.io/bing-maps/hosts/bing-maps-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bing-maps-hosts.yml
- group: other
  href: https://artifacts.apis.io/bing-maps/vendors/bing-maps-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bing-maps-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.microsoft.com/privacy?icid=DSM_Footer_Company_Privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: auth
  href: https://artifacts.apis.io/bing-maps/security/bing-maps-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bing-maps-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bing-maps/security/bing-maps-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bing-maps-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bing-maps/security/bing-maps-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bing-maps-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/maps/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/bingmaps/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bingmapsportal.com/
coverage:
  checked: '2026-11-05'
  detail: Bing Maps REST Services are documented only as prose on learn.microsoft.com (no OpenAPI anywhere, dev.virtualearth.net answers 401 to every unauthenticated path) and the service is deprecated, retired for Basic accounts and closing to Enterprise accounts on June 30th, 2028.
  evidence:
  - status: 200
    url: https://learn.microsoft.com/en-us/bingmaps/rest-services/
  - status: 401
    url: https://dev.virtualearth.net/REST/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-05-28'
description: 'Bing Maps for Enterprise is Microsoft''s mapping platform offering REST Services, a Web Control SDK and spatial data services for geocoding, routing, imagery and traffic. Microsoft has deprecated it: free (Basic) accounts are retired and Enterprise accounts can use it until June 30th, 2028, after which customers must move to Azure Maps.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bing-maps.png
layout: provider
modified: '2026-11-05'
name: Bing Maps
nav: Providers
network: true
overview: 'Bing Maps is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding, Maps, Routing, Geospatial, and Microsoft.


  Bing Maps'' developer surface includes support, pricing, changelog, engineering blog, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.0
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 73.2
    operational_transparency: 39.5
  previous_composite: 9.7
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
screenshot: https://apis.io/screenshots/bing-maps/bing-maps-2026-06-20T173249.png
security:
- kind: domain-security
  name: Bing Maps Domain Security
  slug: bing-maps-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bing Maps Vulnerability Disclosure
  slug: bing-maps-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bing Maps Trust Center
  slug: bing-maps-trust-center
  summary_line: GDPR
slug: bing-maps
tags:
- Geocoding
- Maps
- Routing
- Geospatial
- Microsoft
- Deprecated
- Public APIs
website: https://www.microsoft.com/maps/
---
