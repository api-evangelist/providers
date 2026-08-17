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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/darrow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.darrow.ai/
- group: company
  title: ''
  type: About
  url: https://www.darrow.ai/company/about
- group: company
  title: ''
  type: Blog
  url: https://www.darrow.ai/resources
- group: company
  title: ''
  type: Newsroom
  url: https://www.darrow.ai/company/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.darrow.ai/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.darrow.ai/faq
- group: start
  title: ''
  type: Login
  url: https://portal.darrow.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.darrow.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.darrow.ai/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.darrow.ai/cookie-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/darrow-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/darrow-ai/
- group: company
  title: ''
  type: Partners
  url: https://www.darrow.ai/partnerships
- group: agent
  title: ''
  type: WellKnown
  url: well-known/darrow-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/darrow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/darrow-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/darrow-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/darrow-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/darrow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/darrow-rate-limits.yml
coverage:
  checked: '2026-08-11'
  detail: Darrow markets no API anywhere on darrow.ai — docs., developers. and api.darrow.ai do not resolve in DNS, the 248-URL sitemap contains no developer, docs or pricing page, the GitHub org holds two repos and neither is a client library, and the only HTTP API reachable on the public internet is the customer application's own backend at platform.darrow.ai/api/*, which answers 401 Unauthorized to anonymous callers.
  evidence:
  - status: 404
    url: https://www.darrow.ai/developers
  - status: 401
    url: https://platform.darrow.ai/api/openapi.json
  - status: 404
    url: https://www.darrow.ai/.well-known/agent-card.json
  - status: 200
    url: https://auth.darrow.ai/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-08-11'
description: 'Darrow is an AI legal-intelligence company (founded 2020, offices in New York, Miami, Arizona and Tel Aviv) that scans public real-world signals — regulatory filings, court dockets, incident reports, corporate disclosures and web behavior — to detect legal violations at scale, size the affected class, predict outcomes and value the resulting cases. Its platform serves plaintiff law firms (case origination, predictive litigation analytics, portfolio management, PlaintiffLink intake), insurers (predictive underwriting) and corporate compliance teams (Privacy Radar, listed in the Microsoft Marketplace). Darrow publishes no public developer program: the product is delivered through an Auth0-protected customer portal at portal.darrow.ai, and the only machine-readable surface reachable without credentials is the OpenID Connect discovery document served by its identity tenant.'
image: https://cdn.prod.website-files.com/66c2f6a7d0f70f91592bbaa7/69d55692cb9358ee200d9517_home-OG.png
layout: provider
modified: '2026-08-11'
name: Darrow
nav: Providers
network: true
overview: 'Darrow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal, Legal Intelligence, Litigation, and Artificial Intelligence.


  Darrow''s developer surface includes engineering blog, support, FAQ, authentication, and 17 more developer resources.'
plans:
- name: Darrow Plans Pricing
  plan_count: 0
  slug: darrow-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 0
  name: Darrow Rate Limits
  slug: darrow-rate-limits
scopes:
- name: Darrow Scopes
  scope_count: 0
  slug: darrow-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 26.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Darrow Authentication
  slug: darrow-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Darrow Domain Security
  slug: darrow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: darrow
tags:
- Company
- Legal
- Legal Intelligence
- Litigation
- Artificial Intelligence
- Compliance
- Risk Management
- Insurance
- Data Analytics
website: https://www.darrow.ai/
---
