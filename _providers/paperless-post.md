---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: 'The Paperless Post Party Shop storefront is the only machine-callable surface on any paperlesspost.com host. It is Shopify-hosted and implements the Universal Commerce Protocol (UCP) for agent-driven '
  name: Paperless Post Party Shop Agent Commerce Surface
  slug: party-shop
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paperless-post-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.paperlesspost.com/
- group: company
  title: ''
  type: About
  url: https://www.paperlesspost.com/about
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paperlesspost.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.paperlesspost.com/accounts/new
- group: start
  title: ''
  type: Login
  url: https://www.paperlesspost.com/session/new
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paperlesspost.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paperlesspost.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://paperlesspost.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.paperlesspost.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paperlesspost
- group: company
  title: ''
  type: Careers
  url: https://www.paperlesspost.com/about/careers
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paperlesspost.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paperless-post-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paperless-post-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paperless-post-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paperless-post-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paperless-post-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paperless-post-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paperless-post-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paperless-post-conventions.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/paperless-post_stock/
created: '2026-08-04'
description: Paperless Post is a New York City based digital and print stationery company whose platform lets people design, send, and manage online invitations, greeting cards, save-the-dates, and free Flyers for weddings, birthdays, holidays, business events, and other occasions. Founded in 2008 by siblings James and Alexa Hirschfeld, it pairs an in-house design studio with licensed designer collections (Oscar de la Renta, Rifle Paper Co., Marimekko and others) and adds RSVP tracking, guest messaging, event websites, mobile apps, and a Party Shop. Paperless Post publishes no public developer program, API reference, or machine-readable specification; the /api/v1 endpoints named in its robots.txt serve its own first-party web and mobile clients only.
image: https://avatars.githubusercontent.com/u/282691?v=4
layout: provider
mcp_servers:
- description: ''
  name: paperless-post-mcp.yml
  slug: paperless-post-mcpyml
modified: '2026-08-04'
name: Paperless Post
nav: Providers
network: true
overview: 'Paperless Post publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Invitations, Events, Greeting Cards, and Stationery.


  Paperless Post''s developer surface includes pricing, signup flow, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 34
scopes:
- name: Paperless Post Scopes
  scope_count: 4
  slug: paperless-post-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 31.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 31.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Paperless Post Authentication
  slug: paperless-post-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Paperless Post Domain Security
  slug: paperless-post-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paperless-post
tags:
- Company
- Invitations
- Events
- Greeting Cards
- Stationery
- Consumer
- E-Commerce
- RSVP
- Design
website: https://www.paperlesspost.com/
---
