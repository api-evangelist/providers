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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 149
  human_in_the_loop: 0
  name: Google Analytics 4 Agentic Access
  operation_count: 247
  slug: google-analytics-4-agentic-access
  summary_line: 247 operations · 149 acting
api_count: 8
apis:
- description: 'The Measurement Protocol for Google Analytics 4 allows developers to send events directly to Google Analytics servers for web and app streams. Fire-and-forget: the production endpoint returns HTTP 204'
  name: Google Analytics Measurement Protocol
  slug: google-analytics-measurement-protocol
- description: The accounts API from Google Analytics 4 — 18 operation(s) for accounts.
  name: Google Analytics 4 Accounts API
  slug: google-analytics-4-accounts-api
- description: The accountSummaries API from Google Analytics 4 — 2 operation(s) for accountsummaries.
  name: Google Analytics 4 Account Summaries API
  slug: google-analytics-4-accountsummaries-api
- description: The properties API from Google Analytics 4 — 120 operation(s) for properties.
  name: Google Analytics 4 Properties API
  slug: google-analytics-4-properties-api
artifact_total: 22
asyncapis:
- description: ''
  name: Google Analytics 4 Webhooks
  slug: google-analytics-4-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Analytics Admin API
  slug: open-google-analytics-4-admin-v1alpha
- collection_type: open
  name: Google Analytics Admin API
  slug: open-google-analytics-4-admin-v1beta
- collection_type: open
  name: Google Analytics Data API
  slug: open-google-analytics-4-data-v1alpha
- collection_type: open
  name: Google Analytics Data API
  slug: open-google-analytics-4-data-v1beta
- collection_type: open
  name: Google Analytics Data V1beta API
  slug: open-google-analytics-4-v1beta-api
- collection_type: open
  name: Google Analytics Data API
  slug: open-google-analytics-4
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/google-analytics-4-data-v1beta-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-analytics-4-data-v1alpha-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-analytics-4-admin-v1beta-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-analytics-4-admin-v1alpha-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-analytics-4-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-analytics-4-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-analytics-4-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/google-analytics-4-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://support.google.com/analytics/answer/6004245
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-analytics-4-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-analytics-4-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-analytics-4-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-analytics-4-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-analytics-4-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/google-analytics-4-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-analytics-4-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-analytics-4-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/google-analytics-4-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/google-analytics-4-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/google-analytics-4-finops.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/google-analytics-4-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/google-analytics-4-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/google-analytics-4-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/google-analytics-4-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/google-analytics-4-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/google-analytics-4-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/google-analytics-4-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-analytics-4-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-analytics-4-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-analytics-4-llms.txt
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleanalytics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/googleanalytics4
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/analytics
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/analytics/devguides
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/analytics/devguides/reporting/data/v1/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries
- group: start
  title: ''
  type: Console
  url: https://analytics.google.com/
- group: start
  title: ''
  type: SignUp
  url: https://analytics.google.com/analytics/web/provision/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/analytics/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/analytics
- group: operate
  title: ''
  type: Community
  url: https://developers.google.com/analytics/community
- group: company
  title: ''
  type: Blog
  url: https://blog.google/products/marketingplatform/analytics/
- group: commercial
  title: ''
  type: Pricing
  url: https://marketingplatform.google.com/about/analytics/
created: '2024-01-01'
description: 'Google Analytics 4 (GA4) is Google''s event-based web and app analytics platform and the successor to Universal Analytics. Its developer surface has three distinct parts: the Analytics Data API (analyticsdata.googleapis.com) for running core, pivot, funnel and realtime reports and for exporting audiences; the Analytics Admin API (analyticsadmin.googleapis.com) for managing accounts, properties, data streams, custom dimensions and metrics, key events, access bindings and product links; and the Measurement Protocol (www.google-analytics.com/mp/collect) for sending server-side events directly into a property. Google publishes no OpenAPI for GA4 — the machine-readable contract is served as Google API Discovery documents on the API hosts themselves, alongside canonical protobuf service definitions in the googleapis repository. Authentication is Google OAuth 2.0 only for the Data and Admin APIs; the Measurement Protocol uses a per-stream shared secret.'
finops:
- name: Google Analytics 4 Finops
  service_category: API
  slug: google-analytics-4-finops
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_analytics.svg
layout: provider
mcp_servers:
- description: ''
  name: Google Analytics 4 MCP Server
  slug: google-analytics-4-mcp-server
modified: '2026-08-13'
name: Google Analytics 4
nav: Providers
network: true
overview: 'Google Analytics 4 publishes 3 APIs on the [APIs.io](https://apis.io/) network: Accounts API, Account Summaries API, and Properties API. Tagged areas include Analytics, Data Collection, Marketing, Measurements, and Mobile Analytics.


  The Google Analytics 4 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Google Analytics 4''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, developer console, and 41 more developer resources.'
plans:
- name: Google Analytics 4 Plans Pricing
  plan_count: 2
  slug: google-analytics-4-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 15
  name: Google Analytics 4 Rate Limits
  slug: google-analytics-4-rate-limits
scopes:
- name: Google Analytics 4 Scopes
  scope_count: 5
  slug: google-analytics-4-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 66.2
  coverage:
    artifact_dirs: 27
    catalog_gap: 52.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 4.5
    contract_quality: 64.4
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 84.2
  previous_composite: 66.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-analytics-4/refs/heads/main/screenshots/google-analytics-4-2026-06-20T182011.png
security:
- kind: authentication
  name: Google Analytics 4 Authentication
  slug: google-analytics-4-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Google Analytics 4 Domain Security
  slug: google-analytics-4-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Analytics 4 Vulnerability Disclosure
  slug: google-analytics-4-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Google Analytics 4 Trust Center
  slug: google-analytics-4-trust-center
  summary_line: ISO 27001
slug: google-analytics-4
tags:
- Analytics
- Data Collection
- Marketing
- Measurements
- Mobile Analytics
- Reporting
- Web Analytics
- Attribution
- Audiences
- Event Tracking
website: https://developers.google.com/analytics
---
