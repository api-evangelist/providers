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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-10'
api_count: 9
apis:
- description: The core REST service behind the AdRoll and AdRoll ABM dashboards. Create and manage organizations, advertisables, campaigns, ad groups, ads, pixels, rules, segments, product feeds, marketplace deals,
  name: NextRoll CRUD API
  slug: nextroll-crud-api
- description: A single GraphQL endpoint for all AdRoll and AdRoll ABM reporting data — advertisable, campaign, ad group, ad, audience, email and account metrics, conversions, contextual targeting and CTV placements
  name: NextRoll GraphQL Reporting API
  slug: nextroll-graphql-reporting-api
- description: Create and manage audience segments — CRM (email list), custom (partner user id), composite, impression, user-events, user-attributes and cross-channel lookalike — plus AdRoll ABM Target Account Lists
  name: NextRoll Audience API
  slug: nextroll-audience-api
- description: Manage AdRoll Prospecting campaigns, ad groups, audiences, flights, geo-targets and advertisable-level prospecting settings, targeting digital profiles similar to existing retargeting segments.
  name: NextRoll Prospecting API
  slug: nextroll-prospecting-api
- description: Retrieve the size of audiences and user lists by ad, ad group, advertisable, segment and audience preview, including exact and CDP+ segment counts.
  name: NextRoll User Lists API
  slug: nextroll-user-lists-api
- description: Search for the geotargeting EIDs used when setting geographic targets on AdRoll and AdRoll ABM campaigns.
  name: NextRoll Geotargeting API
  slug: nextroll-geotargeting-api
- description: The AdRoll ABM (formerly RollWorks) activation surface — create, read and update playbooks, strategies, campaigns and ad groups used to run B2B account-based advertising programs.
  name: AdRoll ABM Activate and Playbooks API
  slug: adroll-abm-activate-and-playbooks-api
- description: Send conversion and engagement events directly from your servers to complement the AdRoll pixel and Mobile Measurement Partner integrations. Accepts batches of up to 100 JSON events across thirteen na
  name: NextRoll Server-to-Server (S2S) Event API
  slug: nextroll-server-to-server-s2s-event-api
- description: NextRoll's Model Context Protocol server (open beta, launched May 2026), exposing supported AdRoll and AdRoll ABM data and tools to MCP-compatible AI clients such as Claude, ChatGPT, Cursor, n8n and M
  name: AdRoll MCP Server
  slug: adroll-mcp-server
artifact_total: 19
asyncapis:
- description: ''
  name: Nextroll S2S Events
  slug: nextroll-s2s-events
common:
- group: company
  title: ''
  type: Website
  url: https://www.nextroll.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.nextroll.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.nextroll.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.nextroll.com/http-routingtable.html
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
- group: company
  title: ''
  type: Blog
  url: https://www.adroll.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdRoll
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adroll.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://developers.nextroll.com/accounts/create
- group: start
  title: ''
  type: Login
  url: https://app.adroll.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nextroll.com/terms/api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nextroll.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adroll.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.nextroll.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.nextroll.com/trust-center
- group: auth
  title: ''
  type: Security
  url: https://security.nextroll.com/
- group: operate
  title: ''
  type: FAQ
  url: https://apidocs.nextroll.com/faq.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/nextroll-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nextroll-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nextroll-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nextroll-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nextroll-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/nextroll-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nextroll-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nextroll-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nextroll-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nextroll-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/nextroll-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nextroll-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nextroll-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nextroll-plans.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nextroll-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/nextroll-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nextroll-sandbox.yml
- group: other
  title: ''
  type: EventCatalog
  url: asyncapi/nextroll-s2s-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: 'NextRoll, Inc. is a San Francisco-based marketing technology company that operates two brands on a shared machine-learning and identity platform: AdRoll, a cross-channel digital advertising and retargeting platform for ecommerce and D2C marketers, and AdRoll ABM (formerly RollWorks), an account-based marketing platform for B2B demand generation and sales teams. The NextRoll API is the single developer surface behind both brands, served from https://services.adroll.com and split into focused services: a REST CRUD API for organizations, advertisables, campaigns, ad groups, ads, pixels, segments and product feeds; a GraphQL Reporting API that replaces the legacy per-object report endpoints; an Audience API for CRM, custom, composite, lookalike and target-account segments; Prospecting, Geotargeting and User Lists APIs; an ABM Activate/Playbooks API; and a Server-to-Server event API for conversion and engagement events. Developers register applications at developers.nextroll.com
  and authenticate with OAuth 2.0 or a Personal Access Token plus an application API key. In May 2026 NextRoll launched the AdRoll MCP Server, an OAuth 2.1 protected Model Context Protocol endpoint that exposes AdRoll reporting, draft-first campaign creation and ABM account intelligence to AI assistants and agents.'
graphqls:
- description: <a id="graphql-reporting-api-schema"></a>
  name: GraphQL Reporting API Schema
  slug: nextroll-graphql-reporting-schema
image: https://www.nextroll.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: nextroll-mcp.yml
  slug: nextroll-mcpyml
modified: '2026-08-01'
name: NextRoll
nav: Providers
network: true
overview: 'NextRoll publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Marketing, and Account Based Marketing.


  The NextRoll catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  NextRoll''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Nextroll Plans
  plan_count: 2
  slug: nextroll-plans
random_paper: 76
rate_limits:
- limit_count: 2
  name: Nextroll Rate Limits
  slug: nextroll-rate-limits
scopes:
- name: Nextroll Scopes
  scope_count: 2
  slug: nextroll-scopes
  summary_line: 2 scopes · authorizationCode/implicit/password
score:
  band: strong
  composite: 59.9
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 51.6
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 60.5
  previous_composite: 59.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nextroll/refs/heads/main/screenshots/nextroll-2026-08-07T185216.png
security:
- kind: authentication
  name: Nextroll Authentication
  slug: nextroll-authentication
  summary_line: oauth2/apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Nextroll Domain Security
  slug: nextroll-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nextroll Vulnerability Disclosure
  slug: nextroll-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Nextroll Trust Center
  slug: nextroll-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: nextroll
tags:
- Company
- Advertising
- AdTech
- Marketing
- Account Based Marketing
- Retargeting
- Audiences
- Campaign Management
- Analytics
- Reporting
- MarTech
- Agents
website: https://www.nextroll.com/
---
