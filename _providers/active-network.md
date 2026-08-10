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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: The Activities API from Active Network — 1 operation(s) for activities.
  name: Active Network Activities API
  slug: active-network-activities-api
- description: The Camping API from Active Network — 1 operation(s) for camping.
  name: Active Network Camping API
  slug: active-network-camping-api
artifact_total: 6
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
  name: active-network-mcp.yml
  slug: active-network-mcpyml
modified: '2026-07-17'
name: Active Network
nav: Providers
network: true
overview: 'Active Network publishes 2 APIs on the [APIs.io](https://apis.io/) network: Activities API and Camping API. Tagged areas include Company, Events, Registration, Recreation, and Activities.


  Active Network''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 16 more developer resources.'
random_paper: 67
rate_limits:
- limit_count: 2
  name: Active Network Rate Limits
  slug: active-network-rate-limits
score:
  band: developing
  composite: 46.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 62.8
    developer_ergonomics: 56.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 46.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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
- Events
- Registration
- Recreation
- Activities
- Sports
- Camping
- Search
- Ticketing
website: https://www.activenetwork.com/
---
