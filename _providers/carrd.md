---
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carrd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carrd.co/
- group: docs
  title: ''
  type: Documentation
  url: https://carrd.co/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://carrd.co/docs/building/basics
- group: operate
  title: ''
  type: Support
  url: https://carrd.co/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://carrd.co/pro
- group: start
  title: ''
  type: SignUp
  url: https://carrd.co/signup
- group: start
  title: ''
  type: Login
  url: https://carrd.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carrd.co/docs/general/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carrd.co/docs/general/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://carrd.co/docs/general/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/carrd-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/carrd-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carrd-llms.txt
coverage:
  checked: '2026-08-12'
  detail: 'Carrd is a consumer/creator one-page site builder with no developer program at all: carrd.co/api, /docs/api and /developers all return a hard 404, the documentation index has six sections (General, Sites, Building, Forms, Account, Pro) and not one of them mentions an API, and the only HTTP surface documented is outbound — Pro-tier forms posting submissions into partner APIs or to a URL the site owner supplies.'
  evidence:
  - status: 404
    url: https://carrd.co/developers
  - status: 404
    url: https://carrd.co/docs/api
  - status: 404
    url: https://carrd.co/openapi.json
  - status: 404
    url: https://carrd.co/.well-known/agent-card.json
  - status: 200
    url: https://carrd.co/docs
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: Carrd is a hosted no-code website builder for simple, fully responsive one-page sites — personal profiles, landing pages, portfolios, link pages and small campaign sites. Started as a side project by AJ (@ajlkn) and now operated by Carrd Inc., it offers a free tier of three sites and sixteen paid annual Pro tiers banded Lite, Standard and Plus, topping out at 1,000 sites. Carrd publishes no public API, no developer portal, no SDKs and no machine-readable specification; its only HTTP integration surface points outward, with Pro-tier form elements delivering submissions into twenty email/CRM platforms, Zapier, Make, n8n and Airtable, or to a URL the site owner supplies. Carrd is best understood as an API consumer rather than an API provider.
image: https://carrd.co/assets/docs/images/brand/png/logo-color-light.png
layout: provider
modified: '2026-08-12'
name: Carrd
nav: Providers
network: true
overview: 'Carrd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Website Builder, No-Code, Landing Pages, and Web Hosting.


  Carrd''s developer surface includes documentation, getting-started guide, support, pricing, signup flow, changelog, and 8 more developer resources.'
plans:
- name: Carrd Plans Pricing
  plan_count: 17
  slug: carrd-plans-pricing
random_paper: 20
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 27.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Carrd Domain Security
  slug: carrd-domain-security
  summary_line: TLSv1.3 · DMARC
slug: carrd
tags:
- Company
- Website Builder
- No-Code
- Landing Pages
- Web Hosting
- Site Builder
- Forms
- Software-as-a-Service
website: https://carrd.co/
---
