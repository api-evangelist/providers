---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Dock's financial infrastructure API, branded Caradhras, covering card issuing and processing, digital accounts, transfers, Pix, bank slips and acquiring. The gateway is live at api.caradhras.io (AWS A
  name: Dock Caradhras API
  slug: caradhras
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dock.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.dock.tech/
- group: company
  title: ''
  type: Blog
  url: https://dock.tech/fluid/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dock-tech
- group: operate
  title: ''
  type: Support
  url: https://dock.tech/sac/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dock.tech/privacidade/politica-de-privacidade/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/dock-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dock-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/dock-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/dock-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dock-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dock-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dock-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/dock-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dock-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dock-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: Every path on Dock's developer hub developers.dock.tech 302s to the ReadMe dashboard login (dash.readme.com/to/dock-tech), and the formerly public Caradhras reference at lighthouse.dock.tech is now NXDOMAIN, so no OpenAPI or reference page is readable without a Dock-issued account.
  evidence:
  - status: 302
    url: https://developers.dock.tech/reference/
  - status: 0
    url: https://lighthouse.dock.tech/
  - status: 430
    url: https://api.caradhras.io/openapi.json
  - status: 200
    url: https://dock.tech/llms.txt
  reason: partner-login
  state: gated
created: '2026-08-12'
description: Dock is a Latin American financial technology infrastructure provider — formerly Conductor Technology — that delivers card issuing and processing, core banking, digital accounts and wallets, Pix instant payments, bank slips, acquiring, loyalty/benefits and transactional anti-fraud from a single cloud-native platform marketed as Dock One. Dock operates in Brazil as a payment institution regulated by the Banco Central do Brasil (bank code 301) and states that it serves more than 400 companies across 11 countries, processes roughly R$1.4 trillion in annual card volume and supports around 70 million active digital accounts. Its API estate is branded Caradhras and is reached through the api.caradhras.io gateway; the developer reference at developers.dock.tech is a private ReadMe hub that redirects anonymous visitors to a login, and the previously public Caradhras reference at lighthouse.dock.tech no longer resolves.
image: https://dock.tech/wp-content/uploads/2024/08/icone-dock.svg
layout: provider
modified: '2026-08-12'
name: Dock
nav: Providers
network: true
overview: 'Dock publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Payments, Cards, Card Issuing, and Banking as a Service.


  Dock''s developer surface includes engineering blog, support, and 15 more developer resources.'
plans:
- name: Dock Plans Pricing
  plan_count: 0
  slug: dock-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 0
  name: Dock Rate Limits
  slug: dock-rate-limits
score:
  band: emerging
  composite: 17.4
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Dock Authentication
  slug: dock-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Dock Domain Security
  slug: dock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dock
tags:
- Banking
- Payments
- Cards
- Card Issuing
- Banking as a Service
- Financial Services
- Fintech
- Pix
- Digital Accounts
- Acquiring
- Anti-Fraud
- Embedded Finance
- Brazil
- Latin America
website: https://dock.tech/
---
