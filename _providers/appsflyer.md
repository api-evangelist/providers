---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.7
  scored_at: '2026-08-26'
api_count: 11
apis:
- description: 'Report-pull endpoints that export AppsFlyer attribution and analytics data as CSV/JSON: raw-data installs, in-app events, re-engagements, retargeting, uninstalls, ad-revenue and protect360 reports (V1'
  name: Pull API (Reporting Data)
  slug: pull-api-reporting-data
- description: Event-ingestion endpoints for sending installs, sessions and in-app events to AppsFlyer from a server or a non-mobile client. Covers the mobile S2S events API (api3), the legacy mobile S2S API (api2),
  name: Events APIs (Server-to-Server & Client-to-Server)
  slug: events-apis-server-to-server-client-to-server
- description: 'Account and configuration management endpoints: app management V2.0 (add, update and delete apps), the app list API for app owners and ad networks, bulk user management, the audit public API for accou'
  name: Management APIs
  slug: management-apis
- description: 'Audience segmentation and activation endpoints: the Audience External API for listing, connecting, splitting, pausing and inspecting audiences and their partner connections, the Audience Import API fo'
  name: Audience APIs
  slug: audience-apis
- description: The OneLink API creates, reads, updates and deletes AppsFlyer OneLink attribution links and custom deep-link URLs programmatically, including the link parameters, TTL, branded domain and deep-link val
  name: OneLink API
  slug: onelink-api
- description: 'Apple SKAdNetwork endpoints: the SKAN aggregated performance report API, the SKAN aggregated postbacks-by-arrival-date API, the conversion-value (CV) schema APIs for advertisers and for ad networks, a'
  name: SKAdNetwork (SKAN) APIs
  slug: skadnetwork-skan-apis
- description: The OpenDSR (Data Subject Request) API implements the IAB OpenDSR specification so advertisers can submit, track, and cancel GDPR/CCPA subject access and erasure requests against AppsFlyer on behalf o
  name: OpenDSR API
  slug: opendsr-api
- description: The Protect360 click-signing API manages the secret keys, configuration, excluded apps, circuit breaker and reporting used to cryptographically sign attribution clicks so AppsFlyer can reject unsigned
  name: Click Signing API (Protect360)
  slug: click-signing-api-protect360
- description: The ROI360 net-revenue API returns store-tax and net-revenue figures per app and store so marketers can measure return on ad spend against revenue net of app-store commission and taxes, plus the suppo
  name: ROI360 Net Revenue API
  slug: roi360-net-revenue-api
- description: The Creative External API uploads creative assets and publishes ads to ad networks programmatically, bypassing the AppsFlyer Creative Dashboard UI. It is asynchronous — a batch is submitted for upload
  name: Creative External API
  slug: creative-external-api
- description: AppsFlyer's hosted Model Context Protocol server exposes AppsFlyer's unified marketing data to LLM clients and agents over an OAuth 2.1 authorization-code + PKCE flow with dynamic client registration,
  name: AppsFlyer MCP Server
  slug: appsflyer-mcp-server
artifact_total: 58
asyncapis:
- description: ''
  name: Appsflyer Push Api Webhooks
  slug: appsflyer-push-api-webhooks
collections:
- collection_type: open
  name: Additional Identifiers API
  slug: open-appsflyer-additional-identifiers-api
- collection_type: open
  name: AdRevenue Account Integrations API
  slug: open-appsflyer-adrevenue-account-integrations-api
- collection_type: open
  name: Aggregate Pull API V1 Token
  slug: open-appsflyer-aggregate-pull-api-v1-token
- collection_type: open
  name: Aggregate Pull API V2 Token
  slug: open-appsflyer-aggregate-pull-api-v2-token
- collection_type: open
  name: App list API
  slug: open-appsflyer-app-list-api
- collection_type: open
  name: App management API V2.0
  slug: open-appsflyer-app-management-api-v20
- collection_type: open
  name: Audience External API
  slug: open-appsflyer-audience-external-api
- collection_type: open
  name: Audience Import API
  slug: open-appsflyer-audience-import-api
- collection_type: open
  name: Audiences User Attribution Import API
  slug: open-appsflyer-audiences-user-attribution-import-api
- collection_type: open
  name: Audit Public API
  slug: open-appsflyer-audit-public-api
- collection_type: open
  name: Click Signing API
  slug: open-appsflyer-click-signing-api
- collection_type: open
  name: Cohort API
  slug: open-appsflyer-cohort-api
- collection_type: open
  name: Deep linking REST API
  slug: open-appsflyer-deep-linking-rest-api
- collection_type: open
  name: Engagements API
  slug: open-appsflyer-engagements-api
- collection_type: open
  name: GCD API for SDK attribution testing
  slug: open-appsflyer-gcd-api-for-sdk-attribution-testing-1
- collection_type: open
  name: InCost API
  slug: open-appsflyer-incost-api-1
- collection_type: open
  name: '[Legacy] Server-to-server events API (for mobile)'
  slug: open-appsflyer-legacy-server-to-server-events-api-for-mobile
- collection_type: open
  name: Master API
  slug: open-appsflyer-master-api
- collection_type: open
  name: Master freshness API
  slug: open-appsflyer-master-freshness-api
- collection_type: open
  name: OneLink API v2.0
  slug: open-appsflyer-onelink-api-v20
- collection_type: open
  name: OpenDSR API
  slug: open-appsflyer-opendsr-api
- collection_type: open
  name: Partner integration settings API
  slug: open-appsflyer-partner-integration-settings-api
- collection_type: open
  name: PC/Console/CTV Client-app Events API
  slug: open-appsflyer-pcconsolectv-client-app-events-api
- collection_type: open
  name: PC/Console/CTV Events API
  slug: open-appsflyer-pcconsolectv-events-api
- collection_type: open
  name: Preload C2S Measurement API
  slug: open-appsflyer-preload-c2s-measurement-api
- collection_type: open
  name: Preload Measurement API
  slug: open-appsflyer-preload-measurement-api-1
- collection_type: open
  name: Push API Configuration API
  slug: open-appsflyer-push-api-configuration-api
- collection_type: open
  name: Raw Data Pull API V1 Token
  slug: open-appsflyer-raw-data-pull-api-v1-token
- collection_type: open
  name: Raw Data Pull API V2 Token
  slug: open-appsflyer-raw-data-pull-api-v2-token
- collection_type: open
  name: ROI360 Net Revenue API (v2.0)
  slug: open-appsflyer-roi360-net-revenue-api-v20
- collection_type: open
  name: Server-to-server events API (for mobile)
  slug: open-appsflyer-server-to-server-events-api-for-mobile
- collection_type: open
  name: SKAN aggregated performance report API
  slug: open-appsflyer-skan-aggregated-performance-report-api
- collection_type: open
  name: SKAN aggregated postback by arrival date API
  slug: open-appsflyer-skan-aggregated-postback-by-arrival-date-api
- collection_type: open
  name: SKAN conversion studio API
  slug: open-appsflyer-skan-conversion-studio-api
- collection_type: open
  name: SKAN CV schema API for ad networks
  slug: open-appsflyer-skan-cv-schema-api-for-ad-networks-2
- collection_type: open
  name: SKAN CV Schema API for Advertisers
  slug: open-appsflyer-skan-cv-schema-api-for-advertisers-1
- collection_type: open
  name: Test Console API
  slug: open-appsflyer-test-console-api
- collection_type: open
  name: User management
  slug: open-appsflyer-user-management
- collection_type: open
  name: WEB Server-TO-Server API
  slug: open-appsflyer-web-server-to-server-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appsflyer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appsflyer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.appsflyer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.appsflyer.com/hc
- group: docs
  title: ''
  type: Documentation
  url: https://dev.appsflyer.com/hc/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.appsflyer.com/hc/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.appsflyer.com/hc/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.appsflyer.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.appsflyer.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.appsflyer.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AppsFlyerSDK
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appsflyer.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.appsflyer.com/start/
- group: start
  title: ''
  type: Login
  url: https://hq1.appsflyer.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appsflyer.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appsflyer.com/legal/services-privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.appsflyer.com/product-news/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.appsflyer.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.appsflyer.com/trust/
- group: auth
  title: ''
  type: Compliance
  url: https://www.appsflyer.com/trust/security/
- group: build
  title: ''
  type: Packages
  url: packages/appsflyer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/appsflyer-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/appsflyer-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://dev.appsflyer.com/.well-known/api-catalog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/appsflyer-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/appsflyer-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appsflyer-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/appsflyer-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appsflyer-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appsflyer-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appsflyer-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/appsflyer-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/appsflyer-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/appsflyer-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appsflyer-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/appsflyer-push-api-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/appsflyer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/appsflyer-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/appsflyer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/appsflyer-rate-limits.yml
created: '2026-07-31'
description: 'AppsFlyer is a mobile marketing analytics and attribution platform used by app marketers to measure, attribute and optimize user acquisition across mobile, web, CTV, console and PC. Its developer surface spans mobile and platform SDKs (iOS, Android, Unity, React Native, Flutter, Cordova, Unreal, Roku, Tizen, webOS) and a large REST API estate published on the AppsFlyer developer hub: Pull APIs for raw and aggregate report export, the Master and Cohort reporting APIs, server-to-server and client-to-server event ingestion APIs, the OneLink deep-linking API, audience import/activation APIs, SKAdNetwork conversion-value and postback APIs, app and user management APIs, the Protect360 click-signing anti-fraud API, the ROI360 net-revenue API, and an OpenDSR privacy-request API. AppsFlyer also runs a Push API webhook surface for real-time postbacks and a hosted Model Context Protocol (MCP) server for agent access.'
image: https://www.appsflyer.com/wp-content/uploads/2020/08/appsflyer-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: AppsFlyer MCP Server
  slug: appsflyer-mcp-server
modified: '2026-08-13'
name: AppsFlyer
nav: Providers
network: true
overview: 'AppsFlyer publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Pull API (Reporting Data), Events APIs (Server-to-Server & Client-to-Server), Management APIs, and 6 more. Tagged areas include Company, Mobile Attribution, Marketing Analytics, Mobile Measurement, and Deep Linking.


  The AppsFlyer catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AppsFlyer''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 34 more developer resources.'
plans:
- name: Appsflyer Plans Pricing
  plan_count: 3
  slug: appsflyer-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 11
  name: Appsflyer Rate Limits
  slug: appsflyer-rate-limits
score:
  band: exemplar
  composite: 66.8
  delta: -0.1
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 16.7
    contract_quality: 63.2
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 73.7
  previous_composite: 66.9
  provenance:
    conformance: derived
    contracts:
      callable: 94.9
      derived: 0
      marker_coverage: 0.0
      total: 39
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appsflyer/refs/heads/main/screenshots/appsflyer-2026-08-07T161507.png
security:
- kind: authentication
  name: Appsflyer Authentication
  slug: appsflyer-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Appsflyer Domain Security
  slug: appsflyer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Appsflyer Vulnerability Disclosure
  slug: appsflyer-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Appsflyer Trust Center
  slug: appsflyer-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, ISO 27032, ISO 27701, CSA STAR, TrustArc Enterprise Privacy Certification, PRIVO (GDPR + COPPA), EU-US Data Privacy Framework
slug: appsflyer
tags:
- Company
- Mobile Attribution
- Marketing Analytics
- Mobile Measurement
- Deep Linking
- Audiences
- Ad Fraud Prevention
- SKAdNetwork
- Privacy
- Advertising Technology
- Mobile SDK
- Agentic AI
website: https://www.appsflyer.com/
---
