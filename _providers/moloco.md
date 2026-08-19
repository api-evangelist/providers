---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 62.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 131
  human_in_the_loop: 2
  name: Moloco Agentic Access
  operation_count: 203
  slug: moloco-agentic-access
  summary_line: 203 operations · 131 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: REST API for creating and managing Moloco Ads (Cloud DSP) campaigns — ad accounts, products, tracking links, campaigns, ad groups, creatives, creative groups, audience targets and customer sets — plus
  name: Moloco Ads Campaign Management API
  slug: moloco-ads-campaign-management-api
- description: Authentication and authorization API for Moloco Cloud — issues bearer access tokens from an API key and manages workplaces, userspaces, users, passwords, role grants, permissions and ad-account regist
  name: Moloco Cloud Auth API
  slug: moloco-cloud-auth-api
- description: REST API for retail-media platform operators to manage ad manager accounts, ad accounts, campaigns, sponsored product/brand/display and reserved-display line items, image and video assets, custom targ
  name: Moloco Commerce Media Management API
  slug: moloco-commerce-media-management-api
- description: Real-time ad decisioning API for retail media — request sponsored product, display, brand and reserved display ads for a given page/placement and user context, returning the ads to render together wit
  name: Moloco Commerce Media Decision API
  slug: moloco-commerce-media-decision-api
- description: First-party user-event ingestion API — posts real-time shopper events (home, page view, item view, search, add to cart, purchase and more) from a retailer's site or app into Moloco Commerce Media so t
  name: Moloco Commerce Media Event API
  slug: moloco-commerce-media-event-api
- description: Outbound webhook surface for Moloco Commerce Media, published as an OpenAPI 3.1 webhooks document. Moloco POSTs signed JSON deliveries to a platform-configured HTTPS endpoint for churned-ad-account re
  name: Moloco Commerce Media Webhooks
  slug: moloco-commerce-media-webhooks
artifact_total: 21
asyncapis:
- description: ''
  name: Moloco Commerce Media Webhooks
  slug: moloco-commerce-media-webhooks
collections:
- collection_type: open
  name: Moloco Ads Campaign Management API
  slug: open-moloco-ads-campaign-management
- collection_type: open
  name: MOLOCO Cloud Auth API
  slug: open-moloco-cloud-auth
- collection_type: open
  name: Decision API
  slug: open-moloco-commerce-media-decision
- collection_type: open
  name: Event API
  slug: open-moloco-commerce-media-event
- collection_type: open
  name: Management API
  slug: open-moloco-commerce-media-management
- collection_type: open
  name: MCM Webhooks
  slug: open-moloco-commerce-media-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moloco-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/moloco-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moloco-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moloco-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.moloco.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.moloco.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.moloco.cloud/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.moloco.cloud/reference/dspapi_listadaccounts-1
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.moloco.cloud/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.moloco.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.moloco.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moloco-mcm
- group: start
  title: ''
  type: SignUp
  url: https://portal.moloco.cloud/signin
- group: start
  title: ''
  type: Login
  url: https://portal.moloco.cloud/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moloco.com/terms-and-policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moloco.com/terms-and-policies/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.moloco.com/terms-and-policies/security
- group: auth
  title: ''
  type: Compliance
  url: https://trust.moloco.com/
- group: build
  title: ''
  type: Postman
  url: https://github.com/moloco-mcm/mcm-postman-templates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/moloco-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.moloco.cloud/page/release-notes
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moloco-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moloco-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/moloco-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moloco-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/moloco-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moloco-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/moloco-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moloco-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/moloco-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moloco-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/moloco-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moloco-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/moloco-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moloco-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moloco-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/moloco-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/moloco-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moloco-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/moloco-commerce-media-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moloco-commerce-media-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/moloco-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://help.moloco.com/hc/en-us/articles/15764588719255-Pricing
created: '2026-07-31'
description: 'Moloco is a machine-learning advertising company that operates three developer-facing platforms: Moloco Ads (a performance demand-side platform for app marketers), Moloco Commerce Media / MCM (a retail-media platform that lets marketplaces and retailers run sponsored product, brand, display and reserved-display ads on their own inventory), and Moloco Streaming Monetization. Its public API surface spans a Campaign Management API and a Cloud Auth API on api.moloco.cloud for the DSP side, plus MCM Management, Decision, Event and Webhook APIs on mcm-api.moloco.com for the commerce-media side, covering ad accounts, products, campaigns, ad groups, creatives, audience targets, catalog items, wallets, spending limits, reporting, log export, real-time ad decisioning and first-party user-event ingestion.'
image: https://cdn.prod.website-files.com/6237fca0466ffd9274a1dbdd/6a4b55676ce1b724bd4b3bb2_Open%20Graph%20image.jpg
layout: provider
mcp_servers:
- description: ''
  name: moloco-mcp.yml
  slug: moloco-mcpyml
modified: '2026-08-13'
name: MOLOCO
nav: Providers
network: true
overview: 'MOLOCO publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Ads Campaign Management API, Cloud Auth API, Commerce Media Management API, and 3 more. Tagged areas include advertising, adtech, demand-side-platform, retail-media, and commerce-media.


  The MOLOCO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MOLOCO''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 37 more developer resources.'
plans:
- name: Moloco Plans Pricing
  plan_count: 0
  slug: moloco-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 11
  name: Moloco Rate Limits
  slug: moloco-rate-limits
scopes:
- name: Moloco Scopes
  scope_count: 2
  slug: moloco-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 59.1
  delta: -7.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 16.7
    contract_quality: 69.1
    developer_ergonomics: 66.1
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 72.4
  previous_composite: 66.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 33.3
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/moloco/refs/heads/main/screenshots/moloco-2026-08-07T184114.png
security:
- kind: authentication
  name: Moloco Authentication
  slug: moloco-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Moloco Domain Security
  slug: moloco-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Moloco Trust Center
  slug: moloco-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: moloco
tags:
- advertising
- adtech
- demand-side-platform
- retail-media
- commerce-media
- programmatic-advertising
- campaign-management
- ad-serving
- machine-learning
- mobile-marketing
- reporting
- user-events
website: https://www.moloco.com/
---
