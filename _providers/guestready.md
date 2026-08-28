---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 32.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API for the RentalReady property management system built by GuestReady Group. 252 operations across 60 resource groups — rentals and property layout, reservations and quotes, calendar and daily p
  name: RentalReady API
  slug: rentalready-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/guestready-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/guestready-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/guestready-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.guestready.com/
- group: company
  title: ''
  type: Blog
  url: https://www.guestready.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.guestready.com/blog/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.guestready.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.guestready.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.guestready.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://support.rentalready.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/guestready
- group: start
  title: ''
  type: Login
  url: https://pms.rentalready.io/account/login/
- group: operate
  title: ''
  type: FAQ
  url: https://www.guestready.com/faq/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/guestready-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/guestready-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/guestready-tool-crosswalk.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/guestready-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/guestready-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/guestready-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/guestready-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/guestready-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/guestready-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/guestready-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/guestready-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/guestready-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/guestready-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/guestready-rentalready-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-22'
description: 'GuestReady is a full-service short-term and mid-term rental hospitality management company operating across Europe and the Middle East (United Kingdom, France, Portugal, Spain, Switzerland and the UAE), managing Airbnb, Booking.com, Vrbo and direct-booking properties on behalf of owners and investors — listing optimisation, dynamic pricing, guest communication, cleaning, maintenance and on-the-ground operations. GuestReady Group is also the author of RentalReady, the property management system (PMS) it originally built for its own operations and now sells to external property managers. RentalReady is the group''s developer-facing surface: a 252-operation OpenAPI 3.0.3 REST API at pms.rentalready.io/api/v3/ covering rentals, reservations, calendar, pricing, missions, issues, conversations, reviews, owners, invoicing and payments, secured with OAuth 2.0 authorization-code flow and 50+ granular scopes, plus a Model Context Protocol (MCP) server that connects AI agents to live
  PMS data.'
image: https://d1od3nh65mn5zb.cloudfront.net/app/uploads/2024/06/18144540/Template-1-Homepage.png
layout: provider
mcp_servers:
- description: ''
  name: RentalReady MCP
  slug: rentalready-mcp
modified: '2026-08-22'
name: GuestReady
nav: Providers
network: true
overview: 'GuestReady publishes 1 API on the [APIs.io](https://apis.io/) network: RentalReady API. Tagged areas include Property Management, Short Term Rentals, Vacation Rentals, Hospitality, and Travel.


  GuestReady''s developer surface includes authentication, engineering blog, pricing, support, FAQ, changelog, and 22 more developer resources.'
plans:
- name: Guestready Plans Pricing
  plan_count: 0
  slug: guestready-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Guestready Rate Limits
  slug: guestready-rate-limits
scopes:
- name: Guestready Scopes
  scope_count: 54
  slug: guestready-scopes
  summary_line: 54 scopes · authorizationCode
score:
  band: developing
  composite: 42.6
  delta: 5.2
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 16.7
    contract_quality: 44.4
    developer_ergonomics: 39.9
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 39.5
  previous_composite: 37.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
security:
- kind: authentication
  name: Guestready Authentication
  slug: guestready-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Guestready Domain Security
  slug: guestready-domain-security
  summary_line: TLSv1.3 · DMARC
slug: guestready
tags:
- Property Management
- Short Term Rentals
- Vacation Rentals
- Hospitality
- Travel
- Real Estate
- Channel Management
- Reservations
- Revenue Management
- PMS
- MCP
- OAuth
website: https://www.guestready.com/
---
