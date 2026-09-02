---
access_model:
  confidence: high
  label: Free plan with self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://www.singular.net/pricing/
  - plans/singular-plans-pricing.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
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
  score: 50.0
  scored_at: '2026-09-01'
api_count: 11
apis:
- description: 'Asynchronous REST API for programmatically pulling Singular''s unified marketing data — attribution, cost, ad revenue, and creative metrics — as standardized, warehouse-ready reports. Create a report, '
  name: Singular Reporting API
  slug: singular-reporting-api
- description: Asynchronous reporting API for SKAdNetwork and AdAttributionKit data — aggregated SKAN reports, SKAN raw reports, modeled SKAN metrics and events, and the account's SKAN event catalog.
  name: Singular SKAdNetwork API
  slug: singular-skadnetwork-api
- description: Reporting endpoint for ad-monetization revenue pulled from mediation and monetization partners, joinable to user-acquisition campaign data.
  name: Singular Ad Monetization API
  slug: singular-ad-monetization-api
- description: Create and manage Singular tracking links programmatically, and enumerate the apps, configured partners, link domains, and available partners an organization can build links against. Supports destinat
  name: Singular Links (Tracking Links) API
  slug: singular-links-tracking-links-api
- description: 'List, inspect, create, and delete custom fraud-prevention rules for an organization, with a metadata endpoint returning the external-safe option lists. Rules carry an action of Suspicious, Reject, or '
  name: Singular Custom Fraud Rules API
  slug: singular-custom-fraud-rules-api
- description: Read and update the publisher blacklists used by Singular Fraud Prevention to block traffic from specific publisher sites and IDs.
  name: Singular Publisher Blacklist API
  slug: singular-publisher-blacklist-api
- description: Audit endpoint returning the log of configuration changes made to an attribution partner's settings, filterable by partner name, platform, and app bundle ID.
  name: Singular Partner Configuration Changes Log API
  slug: singular-partner-configuration-changes-log-api
- description: Server-side ingestion endpoints for reporting sessions/launches and in-app events without a client SDK — used for PC, console, CTV, web, and server-authoritative mobile integrations. Session notificat
  name: Singular Server-to-Server (S2S) API
  slug: singular-server-to-server-s2s-api
- description: OpenDSR/OpenGDPR-conformant data subject request API. An anonymous discovery endpoint publishes the supported identity types and subject-request types (erasure, access); authenticated endpoints submit
  name: Singular OpenDSR (GDPR) API
  slug: singular-opendsr-gdpr-api
- description: BETA integration-testing API. Register a real test device to open a one-hour logging session, then read back exactly what the SDK or S2S integration sent to Singular. Premium feature, enabled per acco
  name: Singular Testing Console API
  slug: singular-testing-console-api
- description: First-party remote Model Context Protocol server. Translates a natural-language prompt into a Singular reporting query, runs it against the connecting user's own account under that user's permissions,
  name: Singular MCP
  slug: singular-mcp
artifact_total: 19
asyncapis:
- description: ''
  name: Singular Postbacks Webhooks
  slug: singular-postbacks-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://singular.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.singular.net/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://support.singular.net/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://support.singular.net/hc/en-us/articles/360045245692-Reporting-API-Reference
- group: start
  title: ''
  type: GettingStarted
  url: https://support.singular.net/hc/en-us/articles/207553433-Getting-Started-with-the-Singular-Reporting-API
- group: operate
  title: ''
  type: Support
  url: https://support.singular.net/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.singular.net/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/singular-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.singular.net/react/freesignup/
- group: company
  title: ''
  type: Blog
  url: https://www.singular.net/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.singular.net/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.singular.net/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/singular-labs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.singular.net
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.singular.net/hc/en-us/articles/360061042971-Product-Updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/singular-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/singular-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/singular-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/singular-packages.yml
- group: design
  title: ''
  type: Components
  url: components/singular-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/singular-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/singular-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/singular-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/singular-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/singular-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/singular-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/singular-postbacks-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/singular-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/singular-tool-crosswalk.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/singular-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/singular-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.singular.net/data-security-privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: security/singular-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/singular-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/singular-well-known.yml
created: '2026-07-17'
description: Singular (Singular Labs, Inc.) is a mobile measurement partner (MMP) and marketing analytics platform that unifies attribution, cost aggregation, fraud prevention, ad monetization, and cross-platform analytics into a single source of truth. It aggregates campaign, cost, ad-revenue, and creative data from 1,200+ sources, measures omnichannel ROI across mobile, web, CTV, PC, and console, and powers deep linking, SKAdNetwork/SKAN reporting, audience activation, and marketing ETL. Singular exposes a broad REST surface under api.singular.net — asynchronous reporting, SKAdNetwork reporting, ad-monetization reporting, tracking-link management, custom fraud rules, and partner configuration — plus server-to-server session/event ingestion at s2s.singular.net, an OpenDSR (GDPR/CCPA) subject-request API at gdpr.singular.net, and a first-party remote MCP server at mcp.singular.net that lets ChatGPT, Claude, Cursor, Copilot, and Gemini query live campaign data in natural language. First-party
  iOS, Android, Unity, Flutter, React Native, Cordova, and Web SDKs instrument attribution on the client side. Used by brands including Airbnb, Lyft, and Rovio.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/singular.png
layout: provider
mcp_servers:
- description: Singular's first-party remote MCP server. It translates a natural-language prompt into a Singular Reporting API query, runs it against the caller's own Singular account, and returns the aggregated mar
  name: Singular MCP Server
  slug: singular-mcp-server
modified: '2026-08-12'
name: Singular
nav: Providers
network: true
overview: 'Singular publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing Analytics, Mobile Attribution, Attribution, and Marketing.


  The Singular catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Singular''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, engineering blog, and 28 more developer resources.'
plans:
- name: Singular Plans Pricing
  plan_count: 3
  slug: singular-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 11
  name: Singular Rate Limits
  slug: singular-rate-limits
scopes:
- name: Singular Scopes
  scope_count: 2
  slug: singular-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 63.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 71.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 63.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/singular/refs/heads/main/screenshots/singular-2026-08-17T080421.png
security:
- kind: authentication
  name: Singular Authentication
  slug: singular-authentication
  summary_line: apiKey/oauth2 · 5 schemes
- kind: domain-security
  name: Singular Domain Security
  slug: singular-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Singular Trust Center
  slug: singular-trust-center
  summary_line: SOC 1, SOC 2, ISO 27001, ePrivacy, CSA STAR, COPPA (certified by PRIVO), GDPR Kids (certified by PRIVO), EU-U.S. Data Privacy Framework
slug: singular
tags:
- Company
- Marketing Analytics
- Mobile Attribution
- Attribution
- Marketing
- Advertising
- Analytics
- Mobile Measurement Partner
- SKAdNetwork
- Deep Linking
- Fraud Prevention
- ETL
- MCP
- Ad Monetization
- Privacy
website: https://singular.net
---
