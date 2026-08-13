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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://storytellit.com
- group: start
  title: ''
  type: Login
  url: https://app.storytellit.com/
- group: operate
  title: ''
  type: Support
  url: https://storytellit.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://storytellit.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LikeableLocal
- group: auth
  title: ''
  type: DomainSecurity
  url: security/likeable-local-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/likeable-local-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/likeable-local-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/likeable-local-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: 'A live production API answers at api.storytellit.com and api.likeablelocal.com — the same host the company''s own app bundle calls — but it is the login-gated Storytellit application''s private backend: /users returns 401 NotAuthenticated, /graphql refuses introspection with its own 401, and no reference, portal, or specification is published for it anywhere, not even to customers.'
  evidence:
  - status: 401
    url: https://api.storytellit.com/users
  - status: 401
    url: https://api.storytellit.com/graphql
  - status: 404
    url: https://api.storytellit.com/openapi.json
  - status: 404
    url: https://storytellit.com/developers/
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Likeable Local is a social media marketing company that now operates publicly as Storytellit — likeablelocal.com and www.likeablelocal.com both redirect to storytellit.com, while the product application at app.likeablelocal.com and app.storytellit.com still identifies itself as "Likeable Local" in its web app manifest. Storytellit sells social media management as a white-label service to digital agencies — strategy, custom content creation and publishing, paid social advertising, lead capture, and monthly performance reporting for the agency's clients, across verticals including dental, medical, legal, real estate, insurance, finance, eCommerce, and local business. The company is based in Portland, Maine, and was surfaced in the API Evangelist network as a 500 Global portfolio company. As of this enrichment pass Likeable Local / Storytellit publishes no public API, no developer portal, no API documentation, and no machine-readable specification; the public web surface is a four-page
  marketing site plus a private, login-gated React application. A production API does exist but is an internal application backend rather than a developer product — api.storytellit.com and api.likeablelocal.com both resolve to the same Amazon load balancer and run Express over FeathersJS, and every service path, including a GraphQL endpoint, rejects anonymous callers with HTTP 401 while serving no specification and no documentation of any kind.
image: https://app.storytellit.com/apple-touch-icon.png
layout: provider
modified: '2026-08-12'
name: Likeable Local
nav: Providers
network: true
overview: 'Likeable Local is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Media, Marketing, Social Media Management, and Advertising.


  Likeable Local''s developer surface includes support and 8 more developer resources.'
plans:
- name: Likeable Local Plans Pricing
  plan_count: 0
  slug: likeable-local-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 0
  name: Likeable Local Rate Limits
  slug: likeable-local-rate-limits
score:
  band: minimal
  composite: 12.0
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/likeable-local/refs/heads/main/screenshots/likeable-local-2026-07-25T225142.png
security:
- kind: authentication
  name: Likeable Local Authentication
  slug: likeable-local-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Likeable Local Domain Security
  slug: likeable-local-domain-security
  summary_line: TLSv1.3 · HSTS
slug: likeable-local
tags:
- Company
- Social Media
- Marketing
- Social Media Management
- Advertising
- Small Business
- Agencies
- SaaS
website: https://storytellit.com
---
