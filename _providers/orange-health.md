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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-08-06'
api_count: 3
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
artifact_total: 8
asyncapis:
- description: ''
  name: Orange Health Webhooks
  slug: orange-health-webhooks
common:
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
  name: orange-health-mcp.yml
  slug: orange-health-mcpyml
modified: '2026-07-20'
name: Orange Health
nav: Providers
network: true
overview: 'Orange Health publishes 3 APIs on the [APIs.io](https://apis.io/) network: Orders API, Results API, and Serviceability API. Tagged areas include Company, Mobile, Healthcare, Diagnostics, and Lab Testing.


  The Orange Health catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Orange Health''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 68
score:
  band: thin
  composite: 41.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 73.6
    developer_ergonomics: 36.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 18.4
  previous_composite: 41.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
- Webhooks
- India
website: https://www.orangehealth.in/
---
