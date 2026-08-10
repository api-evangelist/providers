---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Membership, subscription, library and course operations.
  name: Next Big Idea Club members API
  slug: next-big-idea-club-members-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://nextbigideaclub.com/
- group: start
  title: ''
  type: Login
  url: https://nextbigideaclub.com/login/
- group: operate
  title: ''
  type: Support
  url: https://nextbigideaclub.com/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nextbigideaclub.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nextbigideaclub.com/data-privacy/
- group: company
  title: ''
  type: Blog
  url: https://nextbigideaclub.com/magazine/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/next-big-idea-club-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/next-big-idea-club-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/next-big-idea-club-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/next-big-idea-club-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/next-big-idea-club-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/next-big-idea-club-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/next-big-idea-club-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/next-big-idea-club-domain-security.yml
created: '2026-07-17'
description: Next Big Idea Club is a nonfiction book subscription club and podcast that curates the most important new nonfiction, chosen by a selection committee of Malcolm Gladwell, Adam Grant, Susan Cain, and Daniel Pink. Members receive curated new nonfiction, an in-app library, courses, and author interviews across the web and native iOS/Android apps. The consumer experience is powered by a first-party WordPress REST API (the members/v1 namespace) secured with OAuth 2.0 / OpenID Connect via the WP OAuth Server, with Stripe integration for subscription billing. This profile was seeded as a Bloomberg Beta portfolio lead and enriched from the provider's public /wp-json/ discovery and /.well-known/ OAuth surface.
image: https://nextbigideaclub.com/wp-content/plugins/helium/themes/helium/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: next-big-idea-club-mcp.yml
  slug: next-big-idea-club-mcpyml
modified: '2026-07-20'
name: Next Big Idea Club
nav: Providers
network: true
overview: 'Next Big Idea Club publishes 1 API on the [APIs.io](https://apis.io/) network: members API. Tagged areas include Company, Books, Media, Subscription, and Nonfiction.


  Next Big Idea Club''s developer surface includes support, engineering blog, authentication, and 11 more developer resources.'
random_paper: 89
scopes:
- name: Next Big Idea Club Scopes
  scope_count: 4
  slug: next-big-idea-club-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 34.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 55.8
    developer_ergonomics: 19.6
    discoverability: 87.0
    governance: 8.3
    operational_transparency: 0.0
  previous_composite: 34.4
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/next-big-idea-club/refs/heads/main/screenshots/next-big-idea-club-2026-08-07T185200.png
security:
- kind: authentication
  name: Next Big Idea Club Authentication
  slug: next-big-idea-club-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Next Big Idea Club Domain Security
  slug: next-big-idea-club-domain-security
  summary_line: TLSv1.3 · DMARC
slug: next-big-idea-club
tags:
- Company
- Books
- Media
- Subscription
- Nonfiction
- Podcast
- Education
- Membership
website: https://nextbigideaclub.com/
---
