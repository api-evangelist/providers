---
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
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.6
  scored_at: '2026-08-10'
api_count: 10
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
- description: AppsFlyer's hosted Model Context Protocol server exposes AppsFlyer's unified marketing data to LLM clients and agents over an OAuth 2.1 authorization-code + PKCE flow with dynamic client registration,
  name: AppsFlyer MCP Server
  slug: appsflyer-mcp-server
artifact_total: 16
asyncapis:
- description: ''
  name: Appsflyer Push Api Webhooks
  slug: appsflyer-push-api-webhooks
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
created: '2026-07-31'
description: 'AppsFlyer is a mobile marketing analytics and attribution platform used by app marketers to measure, attribute and optimize user acquisition across mobile, web, CTV, console and PC. Its developer surface spans mobile and platform SDKs (iOS, Android, Unity, React Native, Flutter, Cordova, Unreal, Roku, Tizen, webOS) and a large REST API estate published on the AppsFlyer developer hub: Pull APIs for raw and aggregate report export, the Master and Cohort reporting APIs, server-to-server and client-to-server event ingestion APIs, the OneLink deep-linking API, audience import/activation APIs, SKAdNetwork conversion-value and postback APIs, app and user management APIs, the Protect360 click-signing anti-fraud API, the ROI360 net-revenue API, and an OpenDSR privacy-request API. AppsFlyer also runs a Push API webhook surface for real-time postbacks and a hosted Model Context Protocol (MCP) server for agent access.'
image: https://www.appsflyer.com/wp-content/uploads/2020/08/appsflyer-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: appsflyer-mcp.yml
  slug: appsflyer-mcpyml
modified: '2026-07-31'
name: AppsFlyer
nav: Providers
network: true
overview: 'AppsFlyer publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Pull API (Reporting Data), Events APIs (Server-to-Server & Client-to-Server), Management APIs, and 6 more. Tagged areas include Company, Mobile Attribution, Marketing Analytics, Mobile Measurement, and Deep Linking.


  The AppsFlyer catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AppsFlyer''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 32 more developer resources.'
random_paper: 54
score:
  band: strong
  composite: 61.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 70.4
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 61.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 39
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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
