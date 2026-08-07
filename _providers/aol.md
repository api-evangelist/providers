---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aol Agentic Access
  operation_count: 4
  slug: aol-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 3
apis:
- description: Following AOL's acquisition by Verizon and subsequent merger with Yahoo, AOL developer APIs have been consolidated into the Yahoo Developer Network. Yahoo/AOL APIs provide access to advertising servic
  name: Yahoo Developer Network (formerly AOL Developer)
  slug: yahoo-developer-network-formerly-aol-developer
- description: OAuth 2.0 Authorization Code grant endpoints
  name: AOL OAuth2 API
  slug: aol-oauth2-api
- description: OpenID Connect userinfo and JWKS endpoints
  name: AOL OpenID Connect API
  slug: aol-openid-connect-api
artifact_total: 12
collections:
- collection_type: open
  name: Yahoo (formerly AOL) OAuth 2.0 and OpenID Connect API
  slug: open-aol
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aol-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aol-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aol-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aol-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aol-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aol
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aol
- group: start
  title: ''
  type: Portal
  url: https://www.aol.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.yahoo.com/us/en/yahoo/privacy/index.html
created: '2026-03-23'
description: AOL (America Online) is a digital media company and a division of Verizon Media (now Yahoo). AOL operates news and entertainment properties including AOL.com, Engadget, and TechCrunch. Historically, AOL provided developer APIs for advertising, content, and identity services that have since been consolidated into the Yahoo/Verizon Media API ecosystem.
finops:
- name: Aol Finops
  service_category: API
  slug: aol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aol.png
layout: provider
modified: '2026-04-19'
name: AOL
nav: Providers
network: true
overview: 'AOL publishes 2 APIs on the [APIs.io](https://apis.io/) network: OAuth2 API and OpenID Connect API. Tagged areas include Advertising, Digital Media, Entertainment, News, and Fortune 1000.


  AOL''s developer surface includes authentication, developer portal, and 8 more developer resources.'
plans:
- name: Aol Plans Pricing
  plan_count: 3
  slug: aol-plans-pricing
press:
- date: '2026-05-25'
  title: Bending Spoons' Post
  url: https://www.linkedin.com/posts/bendingspoons_big-news-were-acquiring-aol-the-iconic-activity-7389337958274846720-grwP
- date: '2026-05-25'
  title: Preparing for the workforce in the age of AI
  url: https://www.aol.com/news/preparing-workforce-age-ai-033320503.html
- date: '2026-05-25'
  title: AOL is sold in reputed $1.5B deal to tech conglomerate
  url: https://www.aol.com/articles/ve-got-owner-aol-sold-201343341.html
- date: '2026-05-25'
  title: Bending Spoons' acquisition of AOL shows the value ...
  url: https://www.artificialintelligence-news.com/news/bending-spoons-acquisition-of-aol-shows-the-value-of-legacy-platforms/
- date: '2026-05-25'
  title: BBB warns about AI search use, details how to use it smartly
  url: https://www.aol.com/news/bbb-warns-ai-search-details-201446520.html
random_paper: 90
rate_limits:
- limit_count: 5
  name: Aol Rate Limits
  slug: aol-rate-limits
scopes:
- name: Aol Scopes
  scope_count: 3
  slug: aol-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 44.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 63.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aol/refs/heads/main/screenshots/aol-2026-06-20T172055.png
security:
- kind: authentication
  name: Aol Authentication
  slug: aol-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Aol Domain Security
  slug: aol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aol Vulnerability Disclosure
  slug: aol-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aol
tags:
- Advertising
- Digital Media
- Entertainment
- News
- Fortune 1000
website: https://www.aol.com
---
