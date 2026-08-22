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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'REST API for Rachio smart irrigation controllers, Smart Hose Timers and lighting controllers: read people, devices and zones; start/stop watering; manage schedules and rain delays; subscribe to webhoo'
  name: Rachio Public API
  slug: rachio-public-api
artifact_total: 6
asyncapis:
- description: ''
  name: Rachio Webhooks
  slug: rachio-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://rachio.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rachio.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://rachio.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://rachio.readme.io/reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://rachio.readme.io/reference/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.rachio.com
- group: company
  title: ''
  type: Blog
  url: https://rachio.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://rachio.com/products
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rachio.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rachio.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/rachio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rachio-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rachio-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rachio-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rachio-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rachio-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rachio-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/rachio-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rachio-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rachio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rachio-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rachio-domain-security.yml
created: '2026-07-17'
description: Rachio makes smart, WiFi-connected irrigation controllers, Smart Hose Timers and lighting controllers for homes and landscapes. The Rachio Public API lets developers read a person's account, controllers (devices) and irrigation zones, start and stop watering, manage fixed and Flex (weather-adjusted) schedules, set rain delays, and subscribe to real-time webhook events for schedule and zone activity. Requests authenticate with an OAuth2 bearer token retrieved from the Rachio mobile app; the Controller and User API is served at https://api.rach.io/1 and newer product surfaces at https://cloud-rest.rach.io, with a quota of 3,500 requests per day per token.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rachio.png
layout: provider
mcp_servers:
- description: ''
  name: rachio-mcp.yml
  slug: rachio-mcpyml
modified: '2026-07-20'
name: Rachio
nav: Providers
network: true
overview: 'Rachio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Home, IoT, Irrigation, and Home Automation.


  The Rachio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rachio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 16 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 1
  name: Rachio Rate Limits
  slug: rachio-rate-limits
score:
  band: developing
  composite: 41.3
  delta: -0.8
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 42.1
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/screenshots/rachio-2026-08-17T081438.png
security:
- kind: authentication
  name: Rachio Authentication
  slug: rachio-authentication
  summary_line: oauth2/http · 1 scheme
- kind: domain-security
  name: Rachio Domain Security
  slug: rachio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rachio
tags:
- Company
- Smart Home
- IoT
- Irrigation
- Home Automation
- Water Management
- Webhooks
website: https://rachio.com
---
