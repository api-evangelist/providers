---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Lyft Agentic Access
  operation_count: 19
  slug: lyft-agentic-access
  summary_line: 19 operations · 6 acting
api_count: 2
apis:
- baseURL: https://api.lyft.com
  baseurl_source: declared
  description: Endpoints for creating, scheduling, tracking, and managing rides on behalf of passengers who may not have a Lyft account.
  name: lyft Concierge Rides API
  slug: lyft-concierge-rides-api
- baseURL: https://api.lyft.com
  baseurl_source: declared
  description: Endpoints for estimating ride costs for concierge bookings.
  name: lyft Cost Estimates API
  slug: lyft-cost-estimates-api
- baseURL: https://api.lyft.com
  baseurl_source: declared
  description: Endpoints for checking the availability and proximity of nearby Lyft drivers.
  name: lyft Drivers API
  slug: lyft-drivers-api
- baseURL: https://api.lyft.com
  baseurl_source: declared
  description: Endpoints for estimating the time for the nearest driver to reach a specified pickup location.
  name: lyft ETA API
  slug: lyft-eta-api
- baseURL: https://api.lyft.com
  baseurl_source: declared
  description: Endpoints for retrieving profile information for the authenticated Lyft user.
  name: lyft Profile API
  slug: lyft-profile-api
- baseURL: https://api.lyft.com
  baseurl_source: declared
  description: Endpoints for retrieving available ride types for concierge bookings.
  name: lyft Ride Types API
  slug: lyft-ride-types-api
- baseURL: https://api.lyft.com
  baseurl_source: declared
  description: Endpoints for requesting, tracking, canceling, and managing Lyft rides on behalf of an authenticated user.
  name: lyft Rides API
  slug: lyft-rides-api
- description: Live General Bikeshare Feed Specification (GBFS) feeds for the eight bikeshare and scooter systems Lyft operates — Citi Bike, Divvy, Bay Wheels, Bluebikes, Capital Bikeshare, Biketown, Lyft Scooters D
  name: Lyft Micromobility GBFS Feeds
  slug: lyft-gbfs-feeds
artifact_total: 32
asyncapis:
- description: ''
  name: Lyft Webhooks
  slug: lyft-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lyft Concierge Concierge Rides API
  slug: open-lyft-concierge-rides-api
- collection_type: open
  name: Lyft Concierge API
  slug: open-lyft-concierge
- collection_type: open
  name: Lyft Concierge Concierge Rides Cost Estimates API
  slug: open-lyft-cost-estimates-api
- collection_type: open
  name: Lyft Concierge Concierge Rides Drivers API
  slug: open-lyft-drivers-api
- collection_type: open
  name: Lyft Concierge Concierge Rides ETA API
  slug: open-lyft-eta-api
- collection_type: open
  name: Lyft Concierge Concierge Rides Profile API
  slug: open-lyft-profile-api
- collection_type: open
  name: Lyft Ride-Sharing API
  slug: open-lyft-ride-sharing
- collection_type: open
  name: Lyft Concierge Concierge Rides Ride Types API
  slug: open-lyft-ride-types-api
- collection_type: open
  name: Lyft Concierge Concierge Rides API
  slug: open-lyft-rides-api
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/security/lyft-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lyft-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://lyft.com
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/capabilities/lyft-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lyft-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/agentic-access/lyft-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lyft-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/security/lyft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lyft-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/authentication/lyft-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lyft-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lyft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lyft
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/json-ld/lyft-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lyft-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/json-schema/lyft-ride-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/lyft-ride-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/json-schema/lyft-ride-type-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/lyft-ride-type-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/json-schema/lyft-cost-estimate-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/lyft-cost-estimate-schema.json
- group: company
  title: ''
  type: Blog
  url: https://www.lyft.com/blog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/well-known/lyft-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lyft-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/scopes/lyft-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lyft-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/packages/lyft-packages.yml
  title: ''
  type: Packages
  url: packages/lyft-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/packages/lyft-packages.yml
  title: ''
  type: SDKs
  url: packages/lyft-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/conformance/lyft-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lyft-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/errors/lyft-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lyft-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/lifecycle/lyft-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lyft-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/conventions/lyft-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lyft-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/data-model/lyft-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lyft-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/mcp/lyft-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lyft-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/asyncapi/lyft-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lyft-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/llms/lyft-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lyft-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/plans/lyft-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lyft-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/rate-limits/lyft-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lyft-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/finops/lyft-finops.yml
  title: ''
  type: FinOps
  url: finops/lyft-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/gbfs/lyft-gbfs.yml
  title: ''
  type: GBFS
  url: gbfs/lyft-gbfs.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lyft.com/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.lyft.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://help.lyft.com/business/hc/en-us/articles/360001599667-Concierge-API-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://help.lyft.com/business/hc/en-us/articles/8587470351891-Managing-your-API-client-and-program-connections
- group: operate
  title: ''
  type: Support
  url: https://help.lyft.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lyft.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lyft.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.lyft.com/signup
created: '2026-05-03'
description: 'Lyft is a transportation network company operating ride-hailing, bikeshare, scooter-share and related mobility services across the United States and Canada. Its API surface has two halves that behave very differently. The ride-hailing developer program — the Rides and Concierge APIs on api.lyft.com, used for patient transport, employee transit and customer-service ride booking — is gated: www.lyft.com/developers redirects to a sign-in, access is granted through a Lyft Business relationship, and the old documentation host developer.lyft.com no longer resolves. The micromobility side is wide open: Lyft serves live GBFS feeds for eight bikeshare and scooter systems (Citi Bike, Divvy, Bay Wheels, Bluebikes, Capital Bikeshare, Biketown, and its own DC and Denver fleets) anonymously from gbfs.lyft.com, alongside a public RFC 8414 OAuth metadata document that publishes the platform''s full 47-scope vocabulary.'
finops:
- name: Lyft Finops
  service_category: API
  slug: lyft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lyft.png
json_schemas:
- name: Lyft Cost Estimate
  property_count: 9
  slug: lyft-cost-estimate
- name: Lyft Ride
  property_count: 16
  slug: lyft-ride
- name: Lyft Ride Type
  property_count: 5
  slug: lyft-ride-type
jsonld:
- class_count: 0
  name: Lyft Context
  property_count: 9
  slug: lyft-context
layout: provider
modified: '2026-09-17'
name: Lyft
nav: Providers
network: true
overview: 'Lyft publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Concierge Rides API, Cost Estimates API, Drivers API, and 4 more. Tagged areas include Transportation, Mobility, Ride Hailing, Micromobility, and Bike Share.


  The Lyft catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Lyft''s developer surface includes authentication, engineering blog, documentation, getting-started guide, support, signup flow, and 32 more developer resources.'
plans:
- name: Lyft Plans Pricing
  plan_count: 0
  slug: lyft-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Lyft Rate Limits
  slug: lyft-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Lyft API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: lyft-jsonschema-spectral-rules
scopes:
- name: Lyft Scopes
  scope_count: 47
  slug: lyft-scopes
  summary_line: 47 scopes
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 48.3
    catalog_earned_first_party: 0.0
    catalog_gap: 66.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 31.6
    contract_governance: 28.0
    contract_quality: 67.6
    developer_ergonomics: 58.9
    discoverability: 75.9
    operational_transparency: 15.8
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/lyft/refs/heads/main/screenshots/lyft-2026-06-20T184816.png
security:
- kind: authentication
  name: Lyft Authentication
  slug: lyft-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Lyft Domain Security
  slug: lyft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lyft Vulnerability Disclosure
  slug: lyft-vulnerability-disclosure
  summary_line: Hackerone
slug: lyft
tags:
- Transportation
- Mobility
- Ride Hailing
- Micromobility
- Bike Share
- Scooters
- GBFS
- Logistics
- Travel
website: https://lyft.com
---
