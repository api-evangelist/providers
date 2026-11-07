---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.lvt.com/v1
  baseurl_source: declared
  description: Operations on cameras
  name: LVT Cameras API
  slug: lvt-cameras-api
- baseURL: https://api.lvt.com/v1
  baseurl_source: declared
  description: The Events API from LVT — 5 operation(s) for events.
  name: LVT Events API
  slug: lvt-events-api
- baseURL: https://api.lvt.com/v1
  baseurl_source: declared
  description: Operations on LiveUnits
  name: LVT Live Units API
  slug: lvt-liveunits-api
- baseURL: https://api.lvt.com/v1
  baseurl_source: declared
  description: Operations on locations
  name: LVT Locations API
  slug: lvt-locations-api
- baseURL: https://api.lvt.com/v1
  baseurl_source: declared
  description: The Media API from LVT — 1 operation(s) for media.
  name: LVT Media API
  slug: lvt-media-api
- baseURL: https://api.lvt.com/v1
  baseurl_source: declared
  description: The Streams API from LVT — 3 operation(s) for streams.
  name: LVT Streams API
  slug: lvt-streams-api
- baseURL: https://api.lvt.com/v1
  baseurl_source: declared
  description: Operations related to Partner Talkdown
  name: LVT Talkdown API
  slug: lvt-talkdown-api
- baseURL: https://api.lvt.com/v1
  baseurl_source: declared
  description: Operations on webhooks
  name: LVT Webhooks API
  slug: lvt-webhooks-api
- baseURL: https://api.lvt.com/v1
  baseurl_source: declared
  description: Operations related to outbound message verification
  name: LVT Public Keys API
  slug: lvt-public-keys-api
artifact_total: 24
asyncapis:
- description: ''
  name: Lvt Webhooks
  slug: lvt-webhooks
common:
- group: other
  href: https://artifacts.apis.io/lvt/capabilities/lvt-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lvt-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/lvt/security/lvt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lvt-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lvt/scopes/lvt-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lvt-scopes.yml
- group: auth
  href: https://artifacts.apis.io/lvt/authentication/lvt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lvt-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.lvt.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lvt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lvt.com/r/lvt-partner-api-manual
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/LiveViewTech/lvt-public-api/blob/master/api-specs/api.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/LiveViewTech/lvt-public-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LiveViewTech
- group: operate
  title: ''
  type: Support
  url: https://www.lvt.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.lvt.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lvt.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://vms.liveviewtech.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lvt.com/legal/msa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lvt.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lvt.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.lvt.com/
- group: agent
  href: https://artifacts.apis.io/lvt/llms/lvt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lvt-llms.txt
- group: build
  href: https://artifacts.apis.io/lvt/packages/lvt-packages.yml
  title: ''
  type: Packages
  url: packages/lvt-packages.yml
- group: agent
  href: https://artifacts.apis.io/lvt/mcp/lvt-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lvt-mcp.yml
- group: build
  href: https://artifacts.apis.io/lvt/mcp/lvt-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lvt-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/lvt/overlays/lvt-partner-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lvt-partner-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/lvt/conformance/lvt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lvt-conformance.yml
- group: auth
  href: https://artifacts.apis.io/lvt/conformance/lvt-conformance.yml
  title: ''
  type: Compliance
  url: conformance/lvt-conformance.yml
- group: design
  href: https://artifacts.apis.io/lvt/errors/lvt-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lvt-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lvt/lifecycle/lvt-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lvt-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/lvt/security/lvt-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lvt-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lvt/security/lvt-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/lvt-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/lvt/conventions/lvt-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lvt-conventions.yml
- group: design
  href: https://artifacts.apis.io/lvt/data-model/lvt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lvt-data-model.yml
- group: design
  href: https://artifacts.apis.io/lvt/asyncapi/lvt-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lvt-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/lvt/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/lvt/plans/lvt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lvt-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lvt/rate-limits/lvt-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lvt-rate-limits.yml
created: '2026-08-25'
description: 'LVT (LiveView Technologies) is an American physical-security company that builds solar-powered, cellular-connected mobile surveillance units (MSUs) and the SaaS/PaaS platform that runs them — live video, AI analytics, alerting, lights, loudspeakers and AI talk-down — for retail, commercial, industrial, critical-infrastructure and public-sector sites. Founded in 2005 and headquartered in American Fork, Utah, LVT publishes a public Partner API: a REST service over JSON, described by a first-party OpenAPI 3.0.3 document on GitHub, that lets SOC operators and integrators list live units and locations, control cameras (pan/tilt/zoom), start RTSP and WebRTC streams through the LVT camera relay, play sounds, toggle lights, initiate speaker talk-down, review and resolve security alert events, fetch signed media URLs, and register HMAC-signed webhooks. The same API backs LVT''s pre-built integrations with Immix, Axon Fusus and Genetec Security Center, and LVT units also present themselves
  to third-party VMS platforms as ONVIF cameras.'
finops:
- has_sources: true
  method: derived
  name: Lvt Finops
  primary_unit: mobile security unit
  service_category: ''
  slug: lvt-finops
  template: false
image: https://cdn.prod.website-files.com/674d649ddd92d4cd09236107/6848c7616683823ae0acc47c_a61093f6d3186e071147c4359eed84e2_lvt-open-graph-preview_v1.jpg
layout: provider
modified: '2026-08-25'
name: LVT
nav: Providers
network: true
overview: 'LVT publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cameras API, Events API, Live Units API, and 6 more. Tagged areas include Company, Physical Security, Video Surveillance, Camera, and Video Streaming.


  The LVT catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  LVT''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 28 more developer resources.'
plans:
- name: Lvt Plans Pricing
  plan_count: 2
  slug: lvt-plans-pricing
- name: Lvt Price Estimates
  plan_count: 0
  slug: lvt-price-estimates
random_paper: 6
rate_limits:
- limit_count: 0
  name: Lvt Rate Limits
  slug: lvt-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: LVT API Rules
  rule_count: 55
  severity_counts:
    error: 45
    hint: 0
    info: 3
    warn: 7
  slug: lvt-rules
scopes:
- name: Lvt Scopes
  scope_count: 3
  slug: lvt-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 65.7
    developer_ergonomics: 39.9
    discoverability: 73.2
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 58.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lvt/lvt-2026-09-02T150348.png
security:
- kind: authentication
  name: Lvt Authentication
  slug: lvt-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lvt Domain Security
  slug: lvt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lvt Vulnerability Disclosure
  slug: lvt-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: Lvt Trust Center
  slug: lvt-trust-center
  summary_line: trust center published
skill_count: 4
skills:
- name: lvt-deter-onsite-activity
  slug: lvt-deter-onsite-activity
- name: lvt-live-stream-a-camera
  slug: lvt-live-stream-a-camera
- name: lvt-register-a-webhook-receiver
  slug: lvt-register-a-webhook-receiver
- name: lvt-triage-a-security-event
  slug: lvt-triage-a-security-event
slug: lvt
tags:
- Company
- Physical Security
- Video Surveillance
- Camera
- Video Streaming
- WebRTC
- RTSP
- ONVIF
- IoT
- Alerts
- Webhook
- Public Safety
- Retail
- Critical Infrastructure
website: https://www.lvt.com/
---
