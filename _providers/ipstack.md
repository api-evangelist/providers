---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Real-time IP geolocation lookup returning 100+ data fields per IP — country, region and city, latitude/longitude, timezone, currency, connection and ASN details, plus security signals for VPN, proxy a
  name: ipstack REST API
  slug: ipstack-rest-api
- description: Hosted MCP server exposing the ipstack geolocation lookups as agent-callable tools.
  name: ipstack MCP Server
  slug: ipstack-mcp-server
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/ipstack/finops/ipstack-finops.yml
  title: ''
  type: FinOps
  url: finops/ipstack-finops.yml
- group: agent
  href: https://artifacts.apis.io/ipstack/llms/ipstack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ipstack-llms.txt
- group: other
  href: https://artifacts.apis.io/ipstack/hosts/ipstack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ipstack-hosts.yml
- group: build
  href: https://artifacts.apis.io/ipstack/integrations/ipstack-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/ipstack-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/ipstack/vendors/ipstack-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ipstack-vendors.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/
- group: auth
  href: https://artifacts.apis.io/ipstack/security/ipstack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ipstack-domain-security.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://blog.apilayer.com/feed/
- group: company
  title: ''
  type: Website
  url: https://ipstack.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://ipstack.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/ipstack/well-known/ipstack-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ipstack-well-known.yml
- group: build
  href: https://artifacts.apis.io/ipstack/packages/ipstack-packages.yml
  title: ''
  type: Packages
  url: packages/ipstack-packages.yml
- group: build
  href: https://artifacts.apis.io/ipstack/packages/ipstack-packages.yml
  title: ''
  type: SDKs
  url: packages/ipstack-packages.yml
- group: auth
  href: https://artifacts.apis.io/ipstack/authentication/ipstack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ipstack-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ipstack/scopes/ipstack-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ipstack-scopes.yml
- group: design
  href: https://artifacts.apis.io/ipstack/conventions/ipstack-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ipstack-conventions.yml
- group: design
  href: https://artifacts.apis.io/ipstack/errors/ipstack-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ipstack-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ipstack/lifecycle/ipstack-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ipstack-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://ipstack.com/api-status/
- group: design
  href: https://artifacts.apis.io/ipstack/conformance/ipstack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ipstack-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/ipstack/plans/ipstack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ipstack-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ipstack/rate-limits/ipstack-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ipstack-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://ipstack.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.ipstack.com/signup/free
- group: start
  title: ''
  type: Login
  url: https://ipstack.com/login
- group: operate
  title: ''
  type: Support
  url: https://ipstack.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apilayer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ideracorp.com/legal/APILayer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ideracorp.com/Legal/PrivacyPolicy
created: '2026-05-28'
description: IPstack is an IP geolocation API from APILayer, an Idera, Inc. brand. A single GET request against api.ipstack.com resolves an IPv4 or IPv6 address into more than 100 fields — country, region and city, latitude and longitude, time zone, local currency, ISP, ASN and connection type — plus an optional security module that flags proxies, VPNs, Tor exit nodes and known threat actors. Standard, bulk (up to 50 addresses) and requester lookups are offered in JSON, XML and JSONP. The same data is exposed to agents through APILayer's hosted MCP server at mcp.apilayer.com, which publishes RFC 9728 protected-resource metadata and an OAuth authorization server at auth.apilayer.com.
finops:
- has_sources: true
  method: derived
  name: Ipstack Finops
  primary_unit: requests
  service_category: ''
  slug: ipstack-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ipstack.png
layout: provider
mcp_servers:
- description: ''
  name: IPstack MCP Server
  slug: mcp
modified: '2026-09-04'
name: IPstack
nav: Providers
network: true
overview: 'IPstack is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including REST API, and 1 more. Tagged areas include Geocoding, IP Geolocation, Location, Threat Intelligence, and Networking.


  IPstack''s developer surface includes engineering blog, authentication, pricing, signup flow, support, and 25 more developer resources.'
plans:
- name: Ipstack Plans Pricing
  plan_count: 8
  slug: ipstack-plans-pricing
- name: Ipstack Price Estimates
  plan_count: 0
  slug: ipstack-price-estimates
random_paper: 7
rate_limits:
- limit_count: 4
  name: Ipstack Rate Limits
  slug: ipstack-rate-limits
scopes:
- name: Ipstack Scopes
  scope_count: 5
  slug: ipstack-scopes
  summary_line: 5 scopes
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 81.7
    operational_transparency: 50.0
  previous_composite: 47.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ipstack/ipstack-2026-06-20T183602.png
security:
- kind: authentication
  name: Ipstack Authentication
  slug: ipstack-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ipstack Domain Security
  slug: ipstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ipstack
tags:
- Geocoding
- IP Geolocation
- Location
- Threat Intelligence
- Networking
- MCP
- Public APIs
website: https://ipstack.com/
---
