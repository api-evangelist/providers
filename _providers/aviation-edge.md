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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aviation Edge Agentic Access
  operation_count: 17
  slug: aviation-edge-agentic-access
  summary_line: 17 operations
api_count: 1
apis:
- baseURL: https://aviation-edge.com/v2/public
  baseurl_source: declared
  description: Aviation Edge API provides comprehensive aviation data including real-time flight tracking, airport information, airline schedules, aircraft data, and satellite tracking for global aviation intelligen
  name: Aviation Edge
  slug: aviation-edge
- baseURL: https://aviation-edge.com/v2/public
  baseurl_source: declared
  description: Real-time and live flight tracking
  name: Aviation Edge Real-Time API
  slug: aviation-edge-real-time-api
- baseURL: https://aviation-edge.com/v2/public
  baseurl_source: declared
  description: Static reference data
  name: Aviation Edge Reference API
  slug: aviation-edge-reference-api
- baseURL: https://aviation-edge.com/v2/public
  baseurl_source: declared
  description: Satellite tracking data
  name: Aviation Edge Satellites API
  slug: aviation-edge-satellites-api
- baseURL: https://aviation-edge.com/v2/public
  baseurl_source: declared
  description: Airport schedules and flight timetables
  name: Aviation Edge Schedules API
  slug: aviation-edge-schedules-api
- baseURL: https://aviation-edge.com/v2/public
  baseurl_source: declared
  description: Real-time and historical NOTAM data for airports and Flight Information Regions, by IATA code, ICAO code or FIR location code.
  name: Aviation Edge NOTAMs API
  slug: aviation-edge-notams-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Aviation Edge Real-Time API
  slug: open-aviation-edge-real-time-api
- collection_type: open
  name: Aviation Edge Real-Time Reference API
  slug: open-aviation-edge-reference-api
- collection_type: open
  name: Aviation Edge Real-Time Satellites API
  slug: open-aviation-edge-satellites-api
- collection_type: open
  name: Aviation Edge Real-Time Schedules API
  slug: open-aviation-edge-schedules-api
- collection_type: open
  name: Aviation Edge API
  slug: open-aviation-edge
common:
- group: company
  title: ''
  type: Website
  url: https://aviation-edge.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aviation-edge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aviation-edge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aviation-edge-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aviation-edge.com/developers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AviationEdgeAPI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aviation-edge/
- group: company
  title: ''
  type: Blog
  url: https://aviation-edge.com/blog/
- group: build
  title: ''
  type: Packages
  url: packages/aviation-edge-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aviation-edge-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/aviation-edge-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aviation-edge-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/aviation-edge-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aviation-edge-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aviation-edge-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aviation-edge-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aviation-edge-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aviation-edge-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aviation-edge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aviation-edge-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aviation-edge-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://aviation-edge.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://aviation-edge.com/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://aviation-edge.com/developers/
- group: commercial
  title: ''
  type: Pricing
  url: https://aviation-edge.com/premium-api/
- group: start
  title: ''
  type: SignUp
  url: https://aviation-edge.com/premium-api/
- group: start
  title: ''
  type: Login
  url: https://aviation-edge.com/subscribe/login.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aviation-edge.com/api-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aviation-edge.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://aviation-edge.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://aviation-edge.com/frequently-asked-questions/
- group: start
  title: ''
  type: Console
  url: https://aviation-edge.com/get.php
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://aviation-edge.com/service-level-agreement/
- group: company
  title: ''
  type: BlogRSS
  url: https://aviation-edge.com/feed/
created: '2025-02-06'
description: Aviation Edge is a leading provider of aviation data and technology solutions for the global aviation industry. The company offers comprehensive and accurate data sets that cover everything from flight schedules and airline information to airport details and aircraft data.
finops:
- name: Aviation Edge Finops
  service_category: API
  slug: aviation-edge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aviation-edge.png
layout: provider
modified: '2026-09-04'
name: Aviation Edge
nav: Providers
network: true
overview: 'Aviation Edge publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Aviation Edge, Real-Time API, Reference API, and 3 more. Tagged areas include Airlines, Airports, Aviation, Flight Data, and Real-Time.


  Aviation Edge''s developer surface includes authentication, developer portal, engineering blog, sandbox, documentation, API reference, getting-started guide, and 28 more developer resources.'
plans:
- name: Aviation Edge Plans Pricing
  plan_count: 4
  slug: aviation-edge-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Aviation Edge Rate Limits
  slug: aviation-edge-rate-limits
score:
  band: strong
  composite: 58.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 55.6
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aviation-edge/refs/heads/main/screenshots/aviation-edge-2026-06-20T172729.png
security:
- kind: authentication
  name: Aviation Edge Authentication
  slug: aviation-edge-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aviation Edge Domain Security
  slug: aviation-edge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aviation-edge
tags:
- Airlines
- Airports
- Aviation
- Flight Data
- Real-Time
website: https://aviation-edge.com/
---
