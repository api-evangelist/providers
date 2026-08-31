---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - https://get.popmenu.com/developer-api
  - https://get.popmenu.com/pricing
  - https://api.popmenu.com/graphql
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The Popmenu Developer API gives partners access to restaurant data including menus, guests, and orders for building custom integrations with the Popmenu platform. Popmenu also connects with POS and ma
  name: Popmenu Developer API
  slug: rest-api
- description: 'Popmenu integrates with popular restaurant, ordering, delivery, reservation, and marketing applications including Square, Toast, Google Analytics, Google Business Profile, Mailchimp, Yelp, OpenTable, '
  name: Popmenu Integrations
  slug: integrations
artifact_total: 27
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/popmenu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://get.popmenu.com/
- group: other
  title: ''
  type: DeveloperProgram
  url: https://get.popmenu.com/developer-api
- group: operate
  title: ''
  type: Support
  url: https://support.popmenu.com/s/
- group: company
  title: ''
  type: Blog
  url: https://get.popmenu.com/blog
- group: company
  title: ''
  type: Partners
  url: https://get.popmenu.com/partnerships
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Popmenu
- group: commercial
  title: ''
  type: Pricing
  url: https://get.popmenu.com/pricing
- group: start
  title: ''
  type: Login
  url: https://my.popmenu.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://my.popmenu.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://my.popmenu.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.popmenu.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/popmenu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/popmenu-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/popmenu-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/popmenu-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/popmenu-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/popmenu-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/popmenu-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/popmenu-llms.txt
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/popmenu-well-known.yml
- group: agent
  title: ''
  type: MCPProbe
  url: mcp/popmenu-mcp.yml
- group: company
  title: ''
  type: Partners
  url: ''
created: '2026-06-02'
description: 'Popmenu is a restaurant technology platform offering websites, interactive and dynamic menus, online ordering, marketing automation, and menu management designed to turn a restaurant''s web presence into a customer conversion engine. Popmenu promotes a Developer API that gives partners access to data on menus, guests, orders, and more for custom integrations, and it connects to applications such as Square, Toast, Google Analytics, Mailchimp, OpenTable, Resy, DoorDash, and Yelp, plus hundreds of others through partner integrations. That API is GraphQL rather than REST: a live single endpoint was verified at https://api.popmenu.com/graphql on 2026-08-13, mirrored at https://my.popmenu.com/graphql, returning HTTP 200 with vendor popmenu-ratelimit-* headers — but introspection and every query answer "unauthorized" without partner credentials, so the schema cannot be discovered publicly. No OpenAPI, Swagger, AsyncAPI, webhook catalog, MCP server, agent card, llms.txt or /.well-known/
  document exists on any Popmenu host. Authentication, scopes, error codes and rate limits are undocumented, and get.popmenu.com/developer-api is a lead-capture form rather than a reference. Popmenu''s engineering stack is Ruby on Rails with a React front end, and its entire marketing estate returns HTTP 403 to non-browser clients.'
features:
- description: Mobile-responsive restaurant websites with built-in SEO designed to convert visitors into guests.
  name: Restaurant Websites
- description: Photo-rich, followable menu items with guest engagement, reviews, and AI-driven menu recommendations.
  name: Interactive Dynamic Menus
- description: First-party online ordering for pickup, delivery, and dine-in that keeps margins with the restaurant rather than third-party marketplaces.
  name: Online Ordering
- description: Automated email and SMS marketing, social posting, and reputation management driven by guest profile data.
  name: Marketing Automation
- description: Centralized menu management and publishing that syncs across the website, ordering, and partner channels such as OpenTable.
  name: Menu Management
graphqls:
- description: 'generated: ''2026-08-13'''
  name: Popmenu GraphQL API
  slug: popmenu-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/popmenu.png
integrations:
- description: POS integration for menu and order synchronization.
  name: Toast
- description: POS and payments integration.
  name: Square
- description: Preferred menu management and publishing partner for reservations.
  name: OpenTable
- description: Reservation platform embed and integration.
  name: Resy
- description: Third-party delivery integration.
  name: DoorDash
- description: Web analytics integration for restaurant websites.
  name: Google Analytics
- description: Business listing and reputation integration.
  name: Google Business Profile
- description: Email marketing integration.
  name: Mailchimp
- description: Reviews, reputation, and reservation integration.
  name: Yelp
- description: Online payments integration for ordering.
  name: PayPal
- description: Social posting and marketing integration.
  name: Facebook
- description: Social posting and marketing integration.
  name: Instagram
layout: provider
modified: '2026-08-13'
name: Popmenu
nav: Providers
network: true
overview: 'Popmenu publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurant, Menus, Online Ordering, Websites, and Marketing.


  Popmenu''s developer surface includes support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Popmenu Plans Pricing
  plan_count: 4
  slug: popmenu-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Popmenu Rate Limits
  slug: popmenu-rate-limits
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 29.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/popmenu/refs/heads/main/screenshots/popmenu-2026-06-20T191922.png
security:
- kind: authentication
  name: Popmenu Authentication
  slug: popmenu-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Popmenu Domain Security
  slug: popmenu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: popmenu
tags:
- Restaurant
- Menus
- Online Ordering
- Websites
- Marketing
- Integration
- Hospitality
- GraphQL
- Point-of-Sale
- Reservations
- Loyalty
- AI Marketing
use_cases:
- description: Use partner integrations to publish and keep menus consistent across ordering, delivery, and reservation platforms.
  name: Sync Menus to Partner Channels
- description: Centralize guest profile, order, and engagement data to power targeted marketing campaigns.
  name: Unify Guest Data
- description: Connect ordering and POS systems to streamline fulfillment for pickup, delivery, and dine-in.
  name: Streamline Online Ordering
website: https://get.popmenu.com/
---
