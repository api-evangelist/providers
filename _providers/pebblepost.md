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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: The PebblePost JavaScript tag is the provider's public client-side integration surface. Brands drop a script on their site that populates a window._pp array with a Brand ID (brid) and Brand Customer I
  name: PebblePost JavaScript Tag
  slug: pebblepost-javascript-tag
- description: 'A live but publicly undocumented platform API surface behind the PebblePost PDM Manager application. Two hosts respond: api.pebblepost.com (an Express service that answers GET /health with {"status":"'
  name: PebblePost Platform API
  slug: pebblepost-platform-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pebblepost-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pebblepost.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pebblepost.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pebblepost.com/collection/1-getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.pebblepost.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pebblepost.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PebblePost
- group: start
  title: ''
  type: Login
  url: https://pdm.pebblepost.com/#/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pebblepost.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pebblepost.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pebblepost-llms.txt
- group: design
  title: ''
  type: Components
  url: components/pebblepost-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pebblepost-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pebblepost-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pebblepost-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.pebblepost.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/pebblepost-trust-center.yml
coverage:
  checked: '2026-08-04'
  detail: PebblePost runs live API hosts but publishes no developer program at all — api.pbbl.co is an AWS API Gateway that answers every path, including /openapi.json, with HTTP 403 "Missing Authentication Token", and the only public docs site (docs.pebblepost.com, a Help Scout help center) covers dashboard reporting and creative specs, telling integrators to hand Shopify credentials to "your PebblePost Account Manager" instead of documenting an API.
  evidence:
  - status: 403
    url: https://api.pbbl.co/openapi.json
  - status: 404
    url: https://api.pebblepost.com/openapi.json
  - status: 200
    url: https://api.pebblepost.com/health
  - status: 200
    url: https://docs.pebblepost.com/article/36-connect-pebblepost-to-shopify
  - status: 404
    url: https://www.pebblepost.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-08-04'
description: PebblePost is a New York-based commerce marketing platform that pioneered Programmatic Direct Mail (PDM) and now also operates a Performance CTV product. Its Performance Marketing Engine turns first-party website intent signals, household identity and transaction data — surfaced through the PebblePost Graph — into targeted physical mail and connected-TV campaigns for retail and direct-to-consumer brands, with conversion measurement reported through a Performance Dashboard. Brands integrate by installing the PebblePost JavaScript tag (a window._pp client-side collector served from cdn.pbbl.co) and by syncing commerce data through connectors such as Shopify. Live API hosts run at api.pebblepost.com and api.pbbl.co, but PebblePost publishes no public developer portal, API reference, OpenAPI definition or self-serve API keys — API access is arranged through a PebblePost account team.
image: https://www.pebblepost.com/wp-content/themes/pebblepost/assets/static/img/logo.svg
layout: provider
modified: '2026-08-04'
name: PebblePost
nav: Providers
network: true
overview: 'PebblePost publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Advertising, Direct Mail, and Connected TV.


  PebblePost''s developer surface includes documentation, getting-started guide, support, engineering blog, authentication, and 12 more developer resources.'
random_paper: 28
score:
  band: emerging
  composite: 27.2
  delta: -1.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 28.3
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Pebblepost Authentication
  slug: pebblepost-authentication
  summary_line: account-issued-identifier/out-of-band-credential-exchange/interactive-login · 5 schemes
- kind: domain-security
  name: Pebblepost Domain Security
  slug: pebblepost-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Pebblepost Trust Center
  slug: pebblepost-trust-center
  summary_line: SOC 2
slug: pebblepost
tags:
- Company
- Marketing
- Advertising
- Direct Mail
- Connected TV
- Retail
- Commerce
- Identity
- Analytics
website: https://www.pebblepost.com/
---
