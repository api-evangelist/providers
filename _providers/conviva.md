---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-09-03'
api_count: 9
apis:
- description: Programmatic access to historical and real-time Conviva experience metrics by metric name, with optional group-by dimensions, saved or dimensional filters, KPI thresholds and sorting. Historical reque
  name: Conviva Metrics V3 API
  slug: metrics-v3
- description: 'Session-level detail for content and ad sessions, including per-viewer session diagnostics, network_info with IPv4/IPv6, and summary metrics. Endpoints cover /sessions/content, /sessions/ad and their '
  name: Conviva Sessions V3 API
  slug: sessions-v3
- description: Retrieval of AI-driven content and ad alerts, alert diagnostics and impacted-session detail, filterable by time range and severity. Endpoints are /insights/2.6/ai-alerts/content-metrics and /insights/
  name: Conviva AI Alerts API
  slug: ai-alerts
- description: Bulk create, retrieve, update and delete of saved Conviva filters so large filter sets can be managed programmatically. Each call processes a maximum of 100 filters.
  name: Conviva Bulk Filters API
  slug: bulk-filters
- description: Programmatic control over Conviva Precision policies — retrieve policy definitions and their filters and resource shares, activate policies, and reorder Precision filters. POST operations require cred
  name: Conviva Precision Policy API
  slug: precision-policy
- description: Privacy-request surface for marking viewer identifiers for opt-out and deletion of Personally Identifiable Information, plus retrieval of opt-out request status. Supports GDPR/CCPA data-subject workfl
  name: Conviva PII Opt-Out API
  slug: pii-opt-out
- description: Session validation timeline data for QA and sensor-integration testing, queried by viewer_id and/or session_id, used to verify that a Conviva Sensor integration is emitting the expected event timeline
  name: Conviva Validation Timeline API v2
  slug: validation-timeline-v2
- description: Hosted Model Context Protocol server exposing Conviva VSI and DPI data to agents across five sub-services — /vsi/metrics, /vsi/ai-alerts, /vsi/sessions, /dpi/metrics and /dpi/ai-alerts. Protected by O
  name: Conviva MCP Server
  slug: mcp
- description: Hosted Model Context Protocol server for the Conviva Digital Intelligence Platform, exposing /insights, /nexa, /context-center, /session-replay and /metric-query sub-services. Authenticates via Okta-b
  name: Conviva DPI MCP Server
  slug: dpi-mcp
artifact_total: 16
asyncapis:
- description: ''
  name: Conviva Alerts Webhooks
  slug: conviva-alerts-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.conviva.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.conviva.ai/conviva-overview/developer-tools/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.conviva.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.conviva.ai/connect-data/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.conviva.ai/api/apis/conviva-vsi-api/metrics-v3-api-guide/
- group: operate
  title: ''
  type: Support
  url: https://www.conviva.ai/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.conviva.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Conviva
- group: start
  title: ''
  type: SignUp
  url: https://www.conviva.ai/get-started
- group: start
  title: ''
  type: Login
  url: https://pulse.conviva.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.conviva.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.conviva.ai/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.conviva.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.conviva.ai/api/whats-new-conviva-apis/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/conviva-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/conviva-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/conviva-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/conviva-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/conviva-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/conviva-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/conviva-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conviva-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/conviva-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/conviva-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/conviva-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/conviva-alerts-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/conviva-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.conviva.ai/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/conviva-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conviva-domain-security.yml
created: '2026-08-01'
description: Conviva is the streaming-media and digital-experience analytics company behind Experience-Centric Operations (ECO) — a real-time, full-census operational data platform that stitches client-side telemetry from its Sensor SDKs into stateful, per-viewer experience analytics for video streamers, broadcasters and app publishers. Its Pulse portal is fronted by a public REST surface at api.conviva.com covering Metrics V3, Sessions V3, AI Alerts, Bulk Filters, Precision Policy, PII Opt-Out and Validation Timeline, plus Conviva Connect session-summary data feeds (S3/GCS/Snowflake/BigQuery/SFTP), alert webhooks, and two hosted OAuth-protected Model Context Protocol servers (mcp.conviva.com for VSI/DPI metrics, alerts and sessions; dpi-mcp.conviva.com for Context Center, Nexa analysis, metric query and session replay). Conviva publishes a large first-party SDK estate — JavaScript/npm, Android/Maven, iOS/CocoaPods+SPM, React Native, Node and Python agent SDKs — and a Claude plugin marketplace
  carrying three provider-authored Agent Skills for its DPI MCP server. Authentication across the REST surface is HTTP Basic with a client-id/client-secret API key pair generated in Pulse API Management.
image: https://www.conviva.ai/wp-content/uploads/2025/10/conviva-logo.svg
layout: provider
mcp_servers:
- description: Conviva operates TWO hosted, remote-only Model Context Protocol servers. Neither can be run locally. Both are OAuth 2.1 protected resources implementing RFC 8414 + RFC 9728 discovery with dynamic clie
  name: Conviva MCP Server
  slug: conviva-mcp-server
modified: '2026-08-01'
name: Conviva
nav: Providers
network: true
overview: 'Conviva publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Streaming, Video, Observability, and Monitoring.


  The Conviva catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Conviva''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 24 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 6
  name: Conviva Rate Limits
  slug: conviva-rate-limits
scopes:
- name: Conviva Scopes
  scope_count: 4
  slug: conviva-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 71.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 81.6
  previous_composite: 55.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conviva/refs/heads/main/screenshots/conviva-2026-08-07T163806.png
security:
- kind: authentication
  name: Conviva Authentication
  slug: conviva-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Conviva Domain Security
  slug: conviva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Conviva Trust Center
  slug: conviva-trust-center
  summary_line: ISO/IEC 27001:2022
slug: conviva
tags:
- Analytics
- Streaming
- Video
- Observability
- Monitoring
- Media
- Quality of Experience
- Real-Time
- Telemetry
- Agents
- MCP
- Company
website: https://www.conviva.ai/
---
