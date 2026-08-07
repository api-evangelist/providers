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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Localytics Agentic Access
  operation_count: 13
  slug: localytics-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 3
apis:
- description: Requests relating to audiences
  name: Localytics Audiences API
  slug: localytics-audiences-api
- description: Requests relating to all channel campaigns
  name: Localytics Campaigns API
  slug: localytics-campaigns-api
- description: Requests relating to push-channel campaigns
  name: Localytics Push Campaigns API
  slug: localytics-push-campaigns-api
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.localytics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.localytics.com/dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.localytics.com/campaigns_audiences_api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.localytics.com/docs/resources/developer-documentation
- group: operate
  title: ''
  type: Support
  url: https://www.localytics.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.localytics.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.localytics.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.localytics.com/terms
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/localytics-campaigns-audiences-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/localytics-campaigns-audiences-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/localytics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/localytics-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/localytics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/localytics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/localytics-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/localytics-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/localytics-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/localytics-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/localytics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/localytics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/localytics-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/localytics-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/localytics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/localytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.localytics.com/
created: '2026-07-17'
description: Localytics is a mobile analytics and customer-engagement platform that turns the behavioral signals a mobile app already produces into real-time analytics and personalized, data-driven campaigns across push notifications, in-app messages, and inbox messaging. It serves product, marketing, and engineering teams with segmentation, audience building, and campaign management. For developers it exposes a set of HTTP REST APIs — a Query/Reporting API (HAL+JSON), a Push API for message delivery, and a Campaigns & Audience API (OpenAPI 3.0.3) for programmatic campaign and audience management — alongside first-party SDKs for Android, iOS, Apple TV, React Native, Web, and Windows. Added to the API Evangelist network as a portfolio lead and enriched from its live developer documentation.
image: https://localytics.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: localytics-mcp.yml
  slug: localytics-mcpyml
modified: '2026-07-20'
name: Localytics
nav: Providers
network: true
overview: 'Localytics publishes 3 APIs on the [APIs.io](https://apis.io/) network: Audiences API, Campaigns API, and Push Campaigns API. Tagged areas include Company, Martech, Mobile Analytics, Push Notifications, and Customer Engagement.


  Localytics'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 20 more developer resources.'
random_paper: 62
rate_limits:
- limit_count: 0
  name: Localytics Rate Limits
  slug: localytics-rate-limits
score:
  band: thin
  composite: 41.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 57.4
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/localytics/refs/heads/main/screenshots/localytics-2026-07-25T225426.png
security:
- kind: authentication
  name: Localytics Authentication
  slug: localytics-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Localytics Domain Security
  slug: localytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: localytics
tags:
- Company
- Martech
- Mobile Analytics
- Push Notifications
- Customer Engagement
- Marketing Automation
- APIs
website: https://www.localytics.com/
---
