---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.channel99.com/company/request-demo
  - https://support.channel99.com/hc/en-us/articles/49766041989787-Channel99-Reporting-API-Developer-Guide
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: First-party remote Model Context Protocol server that exposes Channel99 marketing intelligence - visits, pixel impressions, vendor and channel scores, audiences, account identity and pipeline influenc
  name: Channel99 MCP Server
  slug: channel99-mcp-server
- description: Ad account dimension records — `GET /dimensions/ad-accounts`
  name: Channel99 Ad Accounts API
  slug: channel99-ad-accounts-api
- description: Ad campaign group dimension records — `GET /dimensions/ad-campaign-groups`
  name: Channel99 Ad Campaign Groups API
  slug: channel99-ad-campaign-groups-api
- description: Ad campaign dimension records — `GET /dimensions/ad-campaigns`
  name: Channel99 Ad Campaigns API
  slug: channel99-ad-campaigns-api
- description: Ad group dimension records — `GET /dimensions/ad-groups`
  name: Channel99 Ad Groups API
  slug: channel99-ad-groups-api
- description: Ad unit dimension records — `GET /dimensions/ad-units`
  name: Channel99 Ad Units API
  slug: channel99-ad-units-api
- description: Ad dimension records — `GET /dimensions/ads`
  name: Channel99 Ads API
  slug: channel99-ads-api
- description: Audience dimension records — `GET /dimensions/audiences`
  name: Channel99 Audiences API
  slug: channel99-audiences-api
- description: Token issuance — `POST /auth/token`
  name: Channel99 Auth API
  slug: channel99-auth-api
- description: Channel dimension records — `GET /dimensions/channels`
  name: Channel99 Channels API
  slug: channel99-channels-api
- description: Company dimension records — `GET /dimensions/companies`
  name: Channel99 Companies API
  slug: channel99-companies-api
- description: Service health check
  name: Channel99 Health API
  slug: channel99-health-api
- description: Ad impression events — `GET /events/impressions`
  name: Channel99 Impressions API
  slug: channel99-impressions-api
- description: Buyer intent signal events — `GET /events/intents`
  name: Channel99 Intents API
  slug: channel99-intents-api
- description: Company information lookup by IP address — `GET /ip/{ipAddress}`
  name: Channel99 IP Lookup API
  slug: channel99-ip-lookup-api
- description: Website pageview events — `GET /events/pageviews`
  name: Channel99 Pageviews API
  slug: channel99-pageviews-api
- description: Vendor dimension records — `GET /dimensions/vendors`
  name: Channel99 Vendors API
  slug: channel99-vendors-api
- description: Website visit events — `GET /events/visits`
  name: Channel99 Visits API
  slug: channel99-visits-api
artifact_total: 25
collections:
- collection_type: open
  name: Pulsar API
  slug: open-channel99-pulsar
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/channel99-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://channel99.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.channel99.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://pulsar.channel99.com/docs/#/
- group: operate
  title: ''
  type: Support
  url: https://support.channel99.com/hc/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://www.channel99.com/articles/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.channel99.com/resources
- group: start
  title: ''
  type: SignUp
  url: https://app.channel99.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.channel99.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.channel99.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.channel99.com/company/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/channel99-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/channel99-domain-security.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/channel99-pulsar-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/channel99-pulsar-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/channel99-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/channel99-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/channel99-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/channel99-rate-limits.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/channel99-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/channel99-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/channel99-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://channel99.freshstatus.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/channel99-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/channel99-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/channel99-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/channel99-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/channel99-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/channel99-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Channel99 is a B2B marketing performance and attribution platform founded by Demandbase creator Chris Golec. It uses AI and first-party account identification to unify cross-channel marketing results, verify B2B ad delivery, reveal the "dark funnel" and view-through traffic, and benchmark vendor and channel performance against the industry, then recommend budget and campaign changes that grow pipeline while reducing wasted spend. Marketing and RevOps teams export unified performance data into data warehouses (Snowflake), CDPs, and BI tools, and activate intent-based audiences. Developers reach the same data through the Pulsar Reporting API, a documented OAuth-issued M2M REST surface of visit, pageview, impression and intent facts with cursor pagination, and through a first-party read-only MCP server that connects Channel99 marketing intelligence to ChatGPT and Claude. Backed by Norwest Venture Partners, Jackson Square Ventures, Industry Ventures, Ridge Ventures, Geek Ventures,
  and Marin-Sonoma Impact Ventures.
image: https://framerusercontent.com/images/dSAqQ1GEpOzYDyupOzsHlZaB9g.png
layout: provider
mcp_servers:
- description: Channel99 operates a first-party, remote Model Context Protocol server that exposes its B2B marketing performance data - website visits, pixel impressions, vendor and channel scores, audiences, accoun
  name: Channel99 MCP Server
  slug: channel99-mcp-server
modified: '2026-08-12'
name: Channel99
nav: Providers
network: true
overview: 'Channel99 publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Ad Accounts API, Ad Campaign Groups API, Ad Campaigns API, and 14 more. Tagged areas include Company, Marketing, Analytics, Attribution, and B2B.


  Channel99''s developer surface includes authentication, documentation, API reference, support, getting-started guide, engineering blog, signup flow, and 23 more developer resources.'
plans:
- name: Channel99 Plans Pricing
  plan_count: 0
  slug: channel99-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Channel99 Rate Limits
  slug: channel99-rate-limits
scopes:
- name: Channel99 Scopes
  scope_count: 0
  slug: channel99-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 22
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 48.5
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 63.2
  previous_composite: 44.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/channel99/refs/heads/main/screenshots/channel99-2026-07-25T205041.png
security:
- kind: authentication
  name: Channel99 Authentication
  slug: channel99-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Channel99 Domain Security
  slug: channel99-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: channel99
tags:
- Company
- Marketing
- Analytics
- Attribution
- B2B
- Advertising
- Marketing Technology
- Artificial Intelligence
- Account-Based Marketing
- Reporting
- MCP
- Agent Ready
- Intent Data
- Account Identification
- Data Export
website: https://channel99.com
---
