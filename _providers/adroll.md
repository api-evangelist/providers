---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.7
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: REST API for managing AdRoll advertisers, campaigns, ads, audience segments, and reporting on the NextRoll platform. Supports OAuth 2.0 flows and Personal Access Tokens with the client API key sent as
  name: NextRoll API for AdRoll
  slug: nextroll-api
- description: GraphQL API for retrieving all AdRoll and AdRoll ABM reporting data in a single request — organization, advertisable, campaign, adgroup, ad, audience, email and automation metrics, plus conversions, r
  name: NextRoll GraphQL Reporting API
  slug: nextroll-graphql-reporting
- description: Remote Model Context Protocol server that exposes AdRoll and AdRoll ABM data and supported workflows to MCP-compatible AI clients including Claude, ChatGPT, Cursor, n8n and Microsoft Copilot Studio. L
  name: AdRoll MCP Server
  slug: nextroll-mcp
- description: Server-side event ingestion API for sending user events and conversions to AdRoll directly from your own servers, complementing the AdRoll pixel and mobile measurement partner integrations. Accepts ba
  name: NextRoll Server-to-Server (S2S) Event API
  slug: nextroll-s2s
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adroll-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.nextroll.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adroll
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adroll
- group: company
  title: ''
  type: Website
  url: https://www.adroll.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.nextroll.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adroll.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.adroll.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.adroll.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.nextroll.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.nextroll.com/crud-api/reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.nextroll.com/guides/get-started.html
- group: operate
  title: ''
  type: Support
  url: https://apidocs.nextroll.com/support.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.adroll.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nextroll.com/terms
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.nextroll.com/terms/api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nextroll.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/adroll-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adroll-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adroll-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adroll-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adroll-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adroll-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nextroll.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/adroll-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adroll-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adroll-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adroll-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.nextroll.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/adroll-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adroll-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://security.nextroll.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adroll-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adroll-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/adroll-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adroll-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/adroll-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/adroll-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/adroll-packages.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/adroll-reporting.graphql
created: '2026-05-11'
description: AdRoll is a display advertising and retargeting platform from NextRoll that helps direct-to-consumer brands run cross-channel display, social, and email campaigns from a single dashboard powered by the BidIQ machine learning bidder. The platform manages audience segmentation, creative serving, and attribution across the open web and major social networks. The NextRoll API for AdRoll exposes campaign, ad, audience, and reporting endpoints using OAuth 2.0 or Personal Access Token authentication.
graphqls:
- description: 'generated: ''2026-08-13'''
  name: NextRoll GraphQL Reporting API (AdRoll)
  slug: adroll-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adroll.png
layout: provider
mcp_servers:
- description: ''
  name: AdRoll MCP Server
  slug: adroll-mcp-server
modified: '2026-08-13'
name: AdRoll
nav: Providers
network: true
overview: 'AdRoll publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Display Advertising, Retargeting, Marketing, and AdTech.


  AdRoll''s developer surface includes engineering blog, documentation, pricing, signup flow, API reference, getting-started guide, support, and 34 more developer resources.'
plans:
- name: Adroll Plans Pricing
  plan_count: 4
  slug: adroll-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Adroll Rate Limits
  slug: adroll-rate-limits
scopes:
- name: Adroll Scopes
  scope_count: 2
  slug: adroll-scopes
  summary_line: 2 scopes · authorizationCode/implicit/password
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 46.8
    developer_ergonomics: 49.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 57.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adroll/refs/heads/main/screenshots/adroll-2026-06-20T165128.png
security:
- kind: authentication
  name: Adroll Authentication
  slug: adroll-authentication
  summary_line: oauth2/apiKey/http · 5 schemes
- kind: domain-security
  name: Adroll Domain Security
  slug: adroll-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adroll Vulnerability Disclosure
  slug: adroll-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Adroll Trust Center
  slug: adroll-trust-center
  summary_line: SOC 2, SOC 3, ISO 27001, PCI DSS, GDPR, CCPA
slug: adroll
tags:
- Advertising
- Display Advertising
- Retargeting
- Marketing
- AdTech
- Programmatic
website: https://www.adroll.com
---
