---
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-30'
api_count: 15
apis:
- description: The consumer-mediated Data API (legacy v2.1) for querying a user's normalized health data - wellness data from wearable devices and apps, and medical data (records, labs, medications, encounters) from
  name: Human API Data API
  slug: human-api-data-api
- description: API endpoints to authorize a client app for the Admin API
  name: Human API Admin API
  slug: human-api-admin-api
- description: API endpoints to generate tokens for Connect App
  name: Human API Connect API
  slug: human-api-connect-api
- description: API endpoints to get orders
  name: Human API Orders API
  slug: human-api-orders-api
- description: API endpoints to manage user resports
  name: Human API Reports API
  slug: human-api-reports-api
- description: API endpoints to request different resources
  name: Human API Resources API
  slug: human-api-resources-api
- description: API endpoints to manage subscriptions
  name: Human API Subscriptions API
  slug: human-api-subscriptions-api
- description: API endpoints to manage users
  name: Human API Users API
  slug: human-api-users-api
artifact_total: 19
asyncapis:
- description: Webhook notifications the Health Intelligence Platform pushes to a configured client endpoint. Notifications are delivered as JSON arrays of event objects. Enablement is per-client and arranged with a
  name: Human API HIP Notifications
  slug: human-api-notifications-asyncapi
collections:
- collection_type: open
  name: Admin API
  slug: open-human-api-admin-order-types
- collection_type: open
  name: Admin API
  slug: open-human-api-admin-user-reports
- collection_type: open
  name: Admin API
  slug: open-human-api-admin-users-list
- collection_type: open
  name: HAPI Auth Public
  slug: open-human-api-auth-admin-token
- collection_type: open
  name: HAPI Auth Public
  slug: open-human-api-auth-connect-token
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
- group: commercial
  title: ''
  type: Plans
  url: plans/human-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/human-api-rate-limits.yml
- group: auth
  title: ''
  type: Compliance
  url: https://reference.humanapi.co/page/epic-documentation
- group: operate
  title: ''
  type: Support
  url: https://support.humanapi.co/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.humanapi.co/hc/en-us
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-user-create-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-user-details-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-user-actions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-user-providers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-subscriptions-list-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-subscription-create-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-subscription-details-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-subscription-delete-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-report-by-id-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/human-api-admin-consumer-link-overlay.yaml
created: '2026-07-24'
description: Human API is a United States health data platform, founded in 2013 and now part of LexisNexis Risk Solutions, that aggregates, normalizes, and delivers digital and clinical health data from providers, hospitals, labs, pharmacies, wearables, and apps through a single API. Its consumer-mediated Data API returns normalized wellness and medical records via user access tokens (Human Connect single sign-on), while its Health Intelligence Platform (HIP) Admin API lets enterprises order electronic health record (EHR) retrievals, manage users and subscriptions, and receive condensed clinical summary reports - primarily to accelerate life insurance underwriting by reaching 30,000+ data sources across roughly 270 million lives. The surface is a proprietary REST/JSON API secured with OAuth2-style client credentials and Bearer JWT tokens; it is not a HL7 FHIR or SMART-on-FHIR API. Access is gated behind a developer portal and partner agreement.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Human API MCP Server
  slug: human-api-mcp-server
modified: '2026-08-15'
name: Human API
nav: Providers
network: true
overview: 'Human API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Connect API, Orders API, and 4 more. Tagged areas include Healthcare, United States, Health Data, EHR, and Interoperability.


  The Human API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Human API''s developer surface includes authentication, documentation, API reference, getting-started guide, CLI, support, and 41 more developer resources.'
plans:
- name: Human Api Plans Pricing
  plan_count: 0
  slug: human-api-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Human Api Rate Limits
  slug: human-api-rate-limits
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 22
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 58.4
    developer_ergonomics: 67.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 55.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
