---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
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
  score: 17.6
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/liqid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liqid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.liqid.de/
- group: start
  title: ''
  type: SignUp
  url: https://www.liqid.de/kunde-werden
- group: start
  title: ''
  type: Login
  url: https://authentication.liqid.de/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liqid.de/datenschutz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liqid.de/ueber-uns/impressum
- group: operate
  title: ''
  type: Support
  url: https://www.liqid.de/ueber-uns/kontakt
- group: company
  title: ''
  type: Blog
  url: https://www.liqid.de/wissen/liqid-smart-letter
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LIQIDTechnology
- group: commercial
  title: ''
  type: Pricing
  url: https://www.liqid.de/loesungen/wealth-management/ueberblick
- group: agent
  title: ''
  type: WellKnown
  url: well-known/liqid-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/liqid-security.txt
- group: auth
  title: ''
  type: Security
  url: security/liqid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liqid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/liqid-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/liqid-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/liqid-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/liqid-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/liqid-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/liqid-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/liqid-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liqid-llms.txt
coverage:
  checked: '2026-08-25'
  detail: LIQID sells discretionary wealth management to private clients through a web dashboard and a mobile app and runs no developer program at all - developer.liqid.de and docs.liqid.de do not resolve, and its own backend api.liqid.de returns {"message":"unauthorized"} with HTTP 401 on every path probed except /health.
  evidence:
  - status: 401
    url: https://api.liqid.de/openapi.json
  - status: 200
    url: https://api.liqid.de/health
  - status: 404
    url: https://www.liqid.de/openapi.json
  - status: 404
    url: https://www.liqid.de/.well-known/api-catalog
  - status: 404
    url: https://www.liqid.de/.well-known/agent-card.json
  - status: 200
    url: https://www.liqid.de/.well-known/security.txt
  - status: 200
    url: https://authentication.liqid.de/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'LIQID Investments GmbH (Berlin, founded 2016) is one of Europe''s largest digital wealth managers, serving affluent private clients with more than EUR 4 billion in assets under management and 12,000+ customers. Through its regulated subsidiary LIQID Asset Management GmbH — a securities institution supervised by BaFin and the Deutsche Bundesbank — it offers digitally delivered discretionary portfolio management (LIQID Global, Global Future, Select and Income ETF strategies from EUR 100,000), cash management, and access to private markets: Private Markets NXT from EUR 20,000 and Private Equity PRO / Venture PRO from EUR 200,000 for semi-professional investors. Custody sits with V-Bank. LIQID delivers the product through a web dashboard and a mobile app, not through a public developer program: it publishes no OpenAPI, no developer portal and no SDKs. The public machine-readable surface it does serve is a security.txt pointing at a vulnerability disclosure policy and OpenID Connect
  discovery metadata for its Auth0-backed customer login; its own application API at api.liqid.de answers 401 on every path.'
image: https://cdn.prod.website-files.com/64ef741eda12a184cd3a1b42/69397469b5838bd712bbb8bb_LIQID-HOME_OpenGraph_1200x630_small.png
layout: provider
modified: '2026-08-25'
name: LIQID Investments
nav: Providers
network: true
overview: 'LIQID Investments is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wealth Management, Investing, Financial Services, and Private Equity.


  LIQID Investments'' developer surface includes signup flow, support, engineering blog, pricing, authentication, and 18 more developer resources.'
plans:
- name: Liqid Plans Pricing
  plan_count: 6
  slug: liqid-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Liqid Rate Limits
  slug: liqid-rate-limits
scopes:
- name: Liqid Scopes
  scope_count: 0
  slug: liqid-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.4
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 13.2
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Liqid Authentication
  slug: liqid-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Liqid Domain Security
  slug: liqid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Liqid Vulnerability Disclosure
  slug: liqid-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Liqid Trust Center
  slug: liqid-trust-center
  summary_line: BaFin / Deutsche Bundesbank supervision, B Corp certification, IVA-Zertifizierung, VuV membership
slug: liqid
tags:
- Company
- Wealth Management
- Investing
- Financial Services
- Private Equity
- Venture Capital
- Asset Management
- Fintech
- Germany
- BaFin
website: https://www.liqid.de/
---
