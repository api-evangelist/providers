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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 65.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://listingsapi.com/api/v4
  baseurl_source: declared
  description: Per-publisher insights (Google / Facebook / Bing) and indexing rate.
  name: Listings API Analytics API
  slug: listings-api-analytics-api
- baseURL: https://listingsapi.com/api/v4
  baseurl_source: declared
  description: Bulk Google / Facebook / Yelp / TripAdvisor account connection flows.
  name: Listings API Connected Accounts API
  slug: listings-api-connected-accounts-api
- baseURL: https://listingsapi.com/api/v4
  baseurl_source: declared
  description: Premium and additional directory listings, duplicates, and AI evaluation.
  name: Listings API Listings API
  slug: listings-api-listings-api
- baseURL: https://listingsapi.com/api/v4
  baseurl_source: declared
  description: Create, update, archive, and inspect business locations.
  name: Listings API Locations API
  slug: listings-api-locations-api
- baseURL: https://listingsapi.com/api/v4
  baseurl_source: declared
  description: Create and manage Google Business Profile posts — announcements, events, and offers — across locations.
  name: Listings API Posts API
  slug: listings-api-posts-api
- baseURL: https://listingsapi.com/api/v4
  baseurl_source: declared
  description: Reviews and review-response endpoints, including analytics.
  name: Listings API Reviews API
  slug: listings-api-reviews-api
- baseURL: https://listingsapi.com/api/v4
  baseurl_source: declared
  description: Supporting reference data — countries, sub-categories, and publisher site categories — plus the publisher sites included in your plan.
  name: Listings API Supporting APIs API
  slug: listings-api-supporting-apis-api
- baseURL: https://listingsapi.com
  baseurl_source: declared
  description: 'A free 24-hour sandbox day pass, offered for limited periods. These calls need no API key: request the pass, then start it with the emailed 6-digit code, or poll until the owner presses Start in the e'
  name: Listings API Day pass API
  slug: listings-api-day-pass-api
- baseURL: https://listingsapi.com
  baseurl_source: declared
  description: Brand-level social publishing across Facebook, Instagram, X, LinkedIn and Pinterest — connect channels, schedule posts, and read engagement.
  name: Listings API Social API
  slug: listings-api-social-api
artifact_total: 23
asyncapis:
- description: ''
  name: Listings Api Webhooks
  slug: listings-api-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/listings-api/plans/listings-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/listings-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/listings-api/rate-limits/listings-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/listings-api-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/listings-api/capabilities/listings-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/listings-api-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://listingsapi.com/mcp
- group: agent
  href: https://artifacts.apis.io/listings-api/mcp/listings-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/listings-api-mcp.yml
- group: other
  href: https://artifacts.apis.io/listings-api/overlays/listings-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/listings-api-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://listingsapi.com
- group: auth
  href: https://artifacts.apis.io/listings-api/security/listings-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/listings-api-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/listings-api/security/listings-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/listings-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/listings-api/authentication/listings-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/listings-api-authentication.yml
- group: agent
  href: https://artifacts.apis.io/listings-api/well-known/listings-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/listings-api-well-known.yml
- group: auth
  href: https://artifacts.apis.io/listings-api/well-known/listings-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/listings-api-security.txt
- group: build
  href: https://artifacts.apis.io/listings-api/packages/listings-api-packages.yml
  title: ''
  type: Packages
  url: packages/listings-api-packages.yml
- group: build
  href: https://artifacts.apis.io/listings-api/packages/listings-api-packages.yml
  title: ''
  type: SDKs
  url: packages/listings-api-packages.yml
- group: design
  href: https://artifacts.apis.io/listings-api/conformance/listings-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/listings-api-conformance.yml
- group: agent
  href: https://artifacts.apis.io/listings-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/listings-api/security/listings-api-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/listings-api-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.listingsapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.listingsapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.listingsapi.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.listingsapi.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/listings-api
- group: start
  title: ''
  type: SignUp
  url: https://listingsapi.com/signup
created: '2026-07-12'
description: REST API and agent-native platform for managing business listings, citations, reviews, Google Business Profile posts, and local analytics across major publisher directories (Google, Facebook, Bing, Yelp, TripAdvisor). A facade over Synup's federated GraphQL backend, with first-party Python and Node SDKs, a hosted MCP server, and llms.txt.
finops:
- has_sources: true
  method: derived
  name: Listings Api Finops
  primary_unit: location plan
  service_category: ''
  slug: listings-api-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/listings-api.png
layout: provider
mcp_servers:
- description: ''
  name: Listings API MCP Server
  slug: mcp
modified: '2026-09-03'
name: Listings API
nav: Providers
network: true
overview: 'Listings API publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Connected Accounts API, Listings API, and 6 more. Tagged areas include Business Listings, Local SEO, Location, Reviews, and Google Business Profile.


  The Listings API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Listings API''s developer surface includes authentication, pricing, support, signup flow, and 19 more developer resources.'
plans:
- name: Listings Api Plans Pricing
  plan_count: 8
  slug: listings-api-plans-pricing
- name: Listings Api Price Estimates
  plan_count: 0
  slug: listings-api-price-estimates
random_paper: 12
rate_limits:
- limit_count: 3
  name: Listings Api Rate Limits
  slug: listings-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 115
  extends:
  - spectral:oas
  name: Listings API API Rules
  rule_count: 74
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 11
  slug: listings-api-rules
scopes:
- name: Listings Api Scopes
  scope_count: 2
  slug: listings-api-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 64.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 62.7
    developer_ergonomics: 59.5
    discoverability: 75.0
    operational_transparency: 52.6
  previous_composite: 64.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/listings-api/listings-api-2026-07-25T225325.png
security:
- kind: authentication
  name: Listings Api Authentication
  slug: listings-api-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Listings Api Domain Security
  slug: listings-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Listings Api Vulnerability Disclosure
  slug: listings-api-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: listingsapi
  slug: listings-api-listingsapi-skill
- name: listings-api-publish-local-posts
  slug: listings-api-publish-local-posts
- name: listings-api-respond-to-reviews
  slug: listings-api-respond-to-reviews
slug: listings-api
tags:
- Business Listings
- Local SEO
- Location
- Reviews
- Google Business Profile
- Analytics
- citation-management
- Local Marketing
- social-publishing
- MCP
- Agent-Native
website: https://listingsapi.com
---
