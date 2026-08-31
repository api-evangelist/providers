---
access_model:
  confidence: high
  label: Sales-gated partner API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developers.jeeng.com/docs/publisher-overview
  - https://developers.jeeng.com/docs/advertiser-overview
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-30'
api_count: 6
apis:
- description: The Management API from Jeeng — 3 operation(s) for management.
  name: Jeeng Management API
  slug: jeeng-management-api
- description: The Reporting API from Jeeng — 6 operation(s) for reporting.
  name: Jeeng Reporting API
  slug: jeeng-reporting-api
- description: The Revenuestripe.onmicrosoft.com API from Jeeng — 1 operation(s) for revenuestripe.onmicrosoft.com.
  name: Jeeng Revenuestripe.onmicrosoft.com API
  slug: jeeng-revenuestripe-onmicrosoft-com-api
artifact_total: 12
collections:
- collection_type: open
  name: Jeeng Email Monetization — Advertisers API
  slug: open-jeeng-advertisers
- collection_type: open
  name: Jeeng Email Monetization — Authentication (OAuth 2.0 token)
  slug: open-jeeng-authentication
- collection_type: open
  name: Jeeng Email Monetization — Publishers API
  slug: open-jeeng-publishers
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/openweb/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/jeeng-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/jeeng-advertisers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/jeeng-publishers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/jeeng-authentication-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://jeeng.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.jeeng.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.jeeng.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.jeeng.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.jeeng.com/docs/getting-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jeeng.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jeeng.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.jeeng.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.jeeng.com/news/
- group: start
  title: ''
  type: Login
  url: https://manage.jeeng.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jeeng-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jeeng-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/jeeng-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jeeng-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jeeng-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jeeng-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jeeng-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jeeng-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jeeng-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/jeeng-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jeeng-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jeeng-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jeeng-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/jeeng-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Jeeng (formerly PowerInbox, acquired by OpenWeb in 2022 and now marketed as OpenWeb Email Monetization) is a multichannel monetization and audience-engagement platform for digital publishers. It helps publishers grow first-party, opt-in audiences and generate advertising revenue across email newsletters, websites, push notifications, and newsreader apps, reaching more than 150M opt-in subscribers. Its products — AdFill, AdServe, AdMarket, and Renderer — fill vacant ad inventory with monetized content, extend direct ad campaigns into email through existing ad servers, connect advertisers to opt-in audiences, and streamline Google Ad Manager ad-ops workflows. Publisher integration is handled through merge tags, per-newsletter ad tags, and cs_email tracking parameters plus direct Google Ad Manager integration; campaigns and reporting are managed through the portal at manage.jeeng.com. Jeeng also publishes partner Reporting & Management APIs at developers.jeeng.com — an advertiser
  API for campaign line and creative management plus campaign/performance reporting, and a publisher API for container, placement and publisher performance reporting — served from powerinbox.azure-api.net behind Microsoft Entra ID OAuth 2.0 client-credentials tokens. API access is not self-serve: an account manager provisions the client id and client secret.'
image: https://www.jeeng.com/wp-content/uploads/2022/04/Jeeng_w_OW.png
layout: provider
mcp_servers:
- description: ''
  name: Jeeng MCP Server
  slug: jeeng-mcp-server
modified: '2026-08-12'
name: Jeeng
nav: Providers
network: true
overview: 'Jeeng publishes 3 APIs on the [APIs.io](https://apis.io/) network: Management API, Reporting API, and Revenuestripe.onmicrosoft.com API. Tagged areas include Company, Advertising, Publishing, Email, and Push Notifications.


  Jeeng''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 24 more developer resources.'
plans:
- name: Jeeng Plans Pricing
  plan_count: 0
  slug: jeeng-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Jeeng Rate Limits
  slug: jeeng-rate-limits
scopes:
- name: Jeeng Scopes
  scope_count: 1
  slug: jeeng-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 58.5
    developer_ergonomics: 39.9
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jeeng/refs/heads/main/screenshots/jeeng-2026-07-25T223120.png
security:
- kind: authentication
  name: Jeeng Authentication
  slug: jeeng-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Jeeng Domain Security
  slug: jeeng-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jeeng
tags:
- Company
- Advertising
- Publishing
- Email
- Push Notifications
- Monetization
- AdTech
- Newsletters
- Audience Engagement
- Reporting
- Analytics
- OData
- Authentication
website: https://jeeng.com
---
