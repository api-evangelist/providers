---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.7
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: The complete OneSignal REST API as OneSignal publishes it — OpenAPI 3.1.0, info.version 11.6, 39 paths and 59 operations covering messaging, users, subscriptions, segments, templates, custom events, i
  name: OneSignal REST API
  slug: onesignal-rest-api
- description: The Apps API from OneSignal — 21 operation(s) for apps.
  name: OneSignal Apps API
  slug: onesignal-apps-api
- description: The Notifications API from OneSignal — 4 operation(s) for notifications.
  name: OneSignal Notifications API
  slug: onesignal-notifications-api
- description: The Players API from OneSignal — 1 operation(s) for players.
  name: OneSignal Players API
  slug: onesignal-players-api
- description: The Templates API from OneSignal — 3 operation(s) for templates.
  name: OneSignal Templates API
  slug: onesignal-templates-api
- description: OneSignal's hosted Model Context Protocol server at https://api.onesignal.com/mcp/oauth, connected over browser-based OAuth 2.1 with PKCE. Listed in the Cursor marketplace and Claude's connector direc
  name: OneSignal MCP Server
  slug: onesignal-mcp
artifact_total: 22
asyncapis:
- description: ''
  name: Onesignal Webhooks
  slug: onesignal-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OneSignal Apps API
  slug: open-onesignal-apps-api
- collection_type: open
  name: OneSignal Notifications API
  slug: open-onesignal-notifications-api
- collection_type: open
  name: OneSignal Players API
  slug: open-onesignal-players-api
- collection_type: open
  name: OneSignal Templates API
  slug: open-onesignal-templates-api
- collection_type: open
  name: OneSignal
  slug: open-onesignal
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/onesignal-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/onesignal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onesignal-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OneSignal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onesignal
- group: company
  title: ''
  type: Website
  url: https://onesignal.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/onesignal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/onesignal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/onesignal-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://onesignal.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://onesignal.com/blog/feed
- group: build
  title: ''
  type: Packages
  url: packages/onesignal-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/onesignal-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/onesignal-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/onesignal-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/onesignal-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/onesignal-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/onesignal-a2a.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onesignal-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/onesignal-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/onesignal-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/onesignal-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/onesignal-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/onesignal-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/onesignal-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.onesignal.com
- group: design
  title: ''
  type: Conventions
  url: conventions/onesignal-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/onesignal-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/onesignal-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/onesignal-cli.yml
- group: design
  title: ''
  type: Components
  url: components/onesignal-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/onesignal-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/onesignal-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.onesignal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.onesignal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.onesignal.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.onesignal.com/docs/en/quickstart-guide
- group: operate
  title: ''
  type: Support
  url: https://onesignal.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://onesignal.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.onesignal.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.onesignal.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onesignal.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onesignal.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/onesignaldevs
- group: build
  title: ''
  type: PostmanCollection
  url: collections/onesignal.postman_collection.json
created: '2026-05-08'
description: OneSignal is a lifecycle customer engagement platform for mobile push, web push, email, SMS/RCS, in-app messaging and iOS Live Activities, orchestrated through Journeys, segments and a single REST API at api.onesignal.com. It reports 1.3 trillion messages a year across 200k apps and 1.5 billion monthly active users. The developer surface is a published OpenAPI 3.1 contract, a full set of first-party server and client SDKs, a hosted OAuth-authenticated MCP server, an A2A agent card and six provider-published Agent Skills.
finops:
- name: Onesignal Finops
  service_category: Notifications
  slug: onesignal-finops
graphqls:
- description: Conceptual GraphQL schema for the OneSignal multi-channel customer engagement platform, derived from the OneSignal REST API v1 (https://documentation.onesignal.com/reference).
  name: OneSignal GraphQL Schema
  slug: onesignal-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onesignal.png
layout: provider
mcp_servers:
- description: ''
  name: onesignal-mcp.yml
  slug: onesignal-mcpyml
modified: '2026-08-13'
name: OneSignal
nav: Providers
network: true
overview: 'OneSignal publishes 5 APIs on the [APIs.io](https://apis.io/) network, including REST API, Apps API, Notifications API, and 2 more. Tagged areas include Notifications, Push, Email, SMS, and Mobile.


  The OneSignal catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OneSignal''s developer surface includes authentication, engineering blog, changelog, CLI, documentation, API reference, getting-started guide, and 39 more developer resources.'
plans:
- name: Onesignal Plans Pricing
  plan_count: 4
  slug: onesignal-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 6
  name: Onesignal Rate Limits
  slug: onesignal-rate-limits
score:
  band: exemplar
  composite: 77.7
  delta: 10.6
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 16.7
    contract_quality: 76.5
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 84.2
  previous_composite: 67.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/onesignal/refs/heads/main/screenshots/onesignal-2026-06-20T190717.png
security:
- kind: authentication
  name: Onesignal Authentication
  slug: onesignal-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Onesignal Domain Security
  slug: onesignal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Onesignal Vulnerability Disclosure
  slug: onesignal-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Onesignal Trust Center
  slug: onesignal-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27701, EU-U.S. Data Privacy Framework
slug: onesignal
tags:
- Notifications
- Push
- Email
- SMS
- Mobile
- Push Notifications
- Web Push
- Customer Engagement
- Marketing Automation
- Live Activities
- RCS
- In-App Messaging
- Journeys
- Lifecycle Marketing
- MCP
- Agent Ready
website: https://onesignal.com/
---
