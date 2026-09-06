---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API (OpenAPI 3.1) for managing locations, listings, connected accounts, reviews, posts, and analytics, with a hosted MCP server and llms.txt for agent-native access.
  name: Listings API
  slug: listings-api
artifact_total: 10
asyncapis:
- description: ''
  name: Listings Api Webhooks
  slug: listings-api-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://listingsapi.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/listings-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/listings-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/listings-api-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/listings-api-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/listings-api-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/listings-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/listings-api-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/listings-api-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
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
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/listings-api.png
layout: provider
mcp_servers:
- description: ''
  name: Listings API MCP Server
  slug: listings-api-mcp-server
- description: 'Official hosted MCP server for the Listings API. Streamable HTTP at https://listingsapi.com/mcp - nothing to install. Authenticates with "Authorization: API <key>" (dev-portal API key) or OAuth 2.0 Be'
  name: Listings API MCP
  slug: listings-api-mcp
modified: '2026-09-03'
name: Listings API
nav: Providers
network: true
overview: 'Listings API publishes 1 API on the [APIs.io](https://apis.io/) network: Listings API. Tagged areas include Business Listings, Local SEO, Locations, Reviews, and Google Business Profile.


  The Listings API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Listings API''s developer surface includes authentication, pricing, support, signup flow, and 13 more developer resources.'
plans:
- name: Listings Api Plans Pricing
  plan_count: 3
  slug: listings-api-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Listings Api Rate Limits
  slug: listings-api-rate-limits
scopes:
- name: Listings Api Scopes
  scope_count: 0
  slug: listings-api-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 48.1
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 54.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/listings-api/refs/heads/main/screenshots/listings-api-2026-07-25T225325.png
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
slug: listings-api
tags:
- Business Listings
- Local SEO
- Locations
- Reviews
- Google Business Profile
- Analytics
- citation-management
- Local Marketing
- social-publishing
- MCP
- agent-native
website: https://listingsapi.com
---
