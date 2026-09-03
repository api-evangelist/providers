---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: http://api.amp.active.com
  baseurl_source: declared
  description: The Activities API from Active Network — 1 operation(s) for activities.
  name: Active Network Activities API
  slug: active-network-activities-api
- baseURL: http://api.amp.active.com
  baseurl_source: declared
  description: The Camping API from Active Network — 1 operation(s) for camping.
  name: Active Network Camping API
  slug: active-network-camping-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ACTIVE Network Activity Search API v2 Activities API
  slug: open-active-network-activities-api
- collection_type: open
  name: ACTIVE Network Activity Search API v2 Activities Camping API
  slug: open-active-network-camping-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/active-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.activenetwork.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.active.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.active.com/docs/Home
- group: docs
  title: ''
  type: APIReference
  url: https://developer.active.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.active.com/member/register
- group: start
  title: ''
  type: SignUp
  url: https://developer.active.com/member/register
- group: operate
  title: ''
  type: Support
  url: https://developer.active.com/help_center
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.activenetwork.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.activenetwork.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.activenetwork.com/information/products-services-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.activenetwork.com/information/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/active-network-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/active-network-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/active-network-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/active-network-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/active-network-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/active-network-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/active-network-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/active-network-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/active-network-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/active-network-activity-search-overlay.yaml
created: '2026-07-17'
description: 'ACTIVE Network provides intelligent activity and event management software for communities and organizations, powering registration, payments, marketing, and attendance for recreation departments, YMCAs, camps, schools, event organizers, and municipalities, and is trusted by over 6,300 organizations worldwide. For developers, ACTIVE Network publishes a set of read-only public data APIs on its AMP platform (api.amp.active.com): the Activity Search API v2 surfaces searchable activities and events from ACTIVE.com and ACTIVEkids.com, and the Campground / Campsite Search APIs surface campgrounds and campsites. All APIs are authenticated with a simple api_key query parameter and are rate limited.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/active-network.png
layout: provider
mcp_servers:
- description: ''
  name: Active Network MCP Server
  slug: active-network-mcp-server
modified: '2026-07-17'
name: Active Network
nav: Providers
network: true
overview: 'Active Network publishes 2 APIs on the [APIs.io](https://apis.io/) network: Activities API and Camping API. Tagged areas include Company, Event, Registration, Recreation, and Activities.


  Active Network''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 16 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 2
  name: Active Network Rate Limits
  slug: active-network-rate-limits
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 55.1
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 43.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/active-network/refs/heads/main/screenshots/active-network-2026-07-25T181526.png
security:
- kind: authentication
  name: Active Network Authentication
  slug: active-network-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Active Network Domain Security
  slug: active-network-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: active-network
tags:
- Company
- Event
- Registration
- Recreation
- Activities
- Sports
- Camping
- Search
- Ticketing
website: https://www.activenetwork.com/
---
