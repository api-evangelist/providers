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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Create and manage diagnostic collection orders.
  name: Orange Health Orders API
  slug: orange-health-orders-api
- description: Retrieve order status and structured test results.
  name: Orange Health Results API
  slug: orange-health-results-api
- description: Check whether a location is serviceable and fetch available slots.
  name: Orange Health Serviceability API
  slug: orange-health-serviceability-api
- description: The Orange Health Partner API API from Orange Health — 0 operation(s) for orange health partner api.
  name: Orange Health Orange Health Partner API
  slug: orange-health-orange-health-partner-api-api
artifact_total: 13
asyncapis:
- description: ''
  name: Orange Health Webhooks
  slug: orange-health-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Orange Health Partner Orders API
  slug: open-orange-health-orders-api
- collection_type: open
  name: Orange Health Partner Orders Results API
  slug: open-orange-health-results-api
- collection_type: open
  name: Orange Health Partner Orders Serviceability API
  slug: open-orange-health-serviceability-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/orange-health-partner-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.orangehealth.in/
- group: docs
  title: ''
  type: Documentation
  url: https://orangehealth.docs.apiary.io/
- group: docs
  title: ''
  type: APIReference
  url: https://orangehealth.docs.apiary.io/
- group: company
  title: ''
  type: Blog
  url: https://www.orangehealth.in/blog
- group: operate
  title: ''
  type: Support
  url: https://www.orangehealth.in/corporate-partners
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orangehealth.in/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orangehealth.in/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/orange-health-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orange-health-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orange-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/orange-health-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/orange-health-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/orange-health-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/orange-health-mcp.yml
created: '2026-07-17'
description: Orange Health Labs is an Indian at-home diagnostics laboratory serving Bengaluru, Delhi, Gurgaon, Noida and Hyderabad, offering 60-minute home sample collection and test results within about six hours. Its Partner API (documented on Apiary as the "Partner API Public Order Flow") lets healthcare partners, employers and apps check location serviceability and slots, create home-collection, lab-drop-off and health-camp orders, track order status, reschedule, cancel and add on tests, and pull structured investigation-level test results. Order lifecycle transitions (order.created through order.completed / order.cancelled) are delivered as HMAC-SHA256 signed webhooks. Authentication is an api_key request header.
image: https://d1wi3p9y2i20go.cloudfront.net/website/homepage/dweb/hero-section/hero-new.webp
layout: provider
mcp_servers:
- description: ''
  name: Orange Health MCP Server
  slug: orange-health-mcp-server
modified: '2026-07-20'
name: Orange Health
nav: Providers
network: true
overview: 'Orange Health publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Orders API, Results API, Serviceability API, and 1 more. Tagged areas include Company, Mobile, Healthcare, Diagnostics, and Lab Testing.


  The Orange Health catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Orange Health''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 21.0
    developer_ergonomics: 29.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 23.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orange-health/refs/heads/main/screenshots/orange-health-2026-08-07T190830.png
security:
- kind: authentication
  name: Orange Health Authentication
  slug: orange-health-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Orange Health Domain Security
  slug: orange-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Orange Health Vulnerability Disclosure
  slug: orange-health-vulnerability-disclosure
  summary_line: contact published
slug: orange-health
tags:
- Company
- Mobile
- Healthcare
- Diagnostics
- Lab Testing
- Home Collection
- Webhook
- India
website: https://www.orangehealth.in/
---
