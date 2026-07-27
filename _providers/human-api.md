---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 56.7
  scored_at: '2026-07-27'
api_count: 3
apis:
- description: The Health Intelligence Platform (HIP) Admin API for creating and managing Human API users, submitting and managing EHR order types, managing subscriptions, and fetching delivered clinical summary rep
  name: Human API Admin API
  slug: human-api-admin-api
- description: The HAPI Auth Public API for facilitating token exchange with external authentication systems. Exposes POST /v1/admin/token (Admin API client-type token via client_id/client_secret) and POST /v1/conne
  name: Human API Authentication API
  slug: human-api-authentication-api
- description: The consumer-mediated Data API (legacy v2.1) for querying a user's normalized health data - wellness data from wearable devices and apps, and medical data (records, labs, medications, encounters) from
  name: Human API Data API
  slug: human-api-data-api
artifact_total: 7
asyncapis:
- description: Webhook notifications the Health Intelligence Platform pushes to a configured client endpoint. Notifications are delivered as JSON arrays of event objects. Enablement is per-client and arranged with a
  name: Human API HIP Notifications
  slug: human-api-notifications-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/human-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/human-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://humanapi.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.humanapi.co/
- group: docs
  title: ''
  type: Documentation
  url: https://reference.humanapi.co/
- group: docs
  title: ''
  type: APIReference
  url: https://reference.humanapi.co/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://reference.humanapi.co/docs/integration-best-practices
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/humanapi
- group: operate
  title: ''
  type: StatusPage
  url: https://status.humanapi.co/
- group: start
  title: ''
  type: Login
  url: https://developer.humanapi.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.humanapi.co/developer-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://humanapi.co/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/human-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/human-api-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/human-api-cli.yml
- group: design
  title: ''
  type: Components
  url: components/human-api-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/human-api-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/human-api-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/human-api-tool-crosswalk.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/human-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/human-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/human-api-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/human-api-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/human-api-conformance.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/human-api-notifications-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/human-api-notifications-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-order-types-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-user-reports-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-users-list-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-auth-admin-token-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-auth-connect-token-overlay.yaml
created: '2026-07-24'
description: Human API is a United States health data platform, founded in 2013 and now part of LexisNexis Risk Solutions, that aggregates, normalizes, and delivers digital and clinical health data from providers, hospitals, labs, pharmacies, wearables, and apps through a single API. Its consumer-mediated Data API returns normalized wellness and medical records via user access tokens (Human Connect single sign-on), while its Health Intelligence Platform (HIP) Admin API lets enterprises order electronic health record (EHR) retrievals, manage users and subscriptions, and receive condensed clinical summary reports - primarily to accelerate life insurance underwriting by reaching 30,000+ data sources across roughly 270 million lives. The surface is a proprietary REST/JSON API secured with OAuth2-style client credentials and Bearer JWT tokens; it is not a HL7 FHIR or SMART-on-FHIR API. Access is gated behind a developer portal and partner agreement.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: human-api-mcp.yml
  slug: human-api-mcpyml
modified: '2026-07-24'
name: Human API
nav: Providers
network: true
overview: 'Human API publishes 2 APIs on the [APIs.io](https://apis.io/) network: Admin API and Authentication API. Tagged areas include Healthcare, United States, Health Data, EHR, and Interoperability.


  The Human API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Human API''s developer surface includes authentication, documentation, API reference, getting-started guide, CLI, and 27 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 51.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 60.4
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 51.1
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/human-api/refs/heads/main/screenshots/human-api-2026-07-25T221654.png
security:
- kind: authentication
  name: Human Api Authentication
  slug: human-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Human Api Domain Security
  slug: human-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: human-api
tags:
- Healthcare
- United States
- Health Data
- EHR
- Interoperability
- Remote Monitoring
- Wearables
- Life Insurance
- Clinical Data
- Health API
website: https://humanapi.co/
---
