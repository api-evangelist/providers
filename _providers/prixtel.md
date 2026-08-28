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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.prixtel.com/
- group: company
  title: ''
  type: About
  url: https://www.prixtel.com/qui-sommes-nous
- group: company
  title: ''
  type: Blog
  url: https://www.prixtel.com/decouvrir-prixtel/
- group: company
  title: ''
  type: BlogFeeds
  url: https://www.prixtel.com/decouvrir-prixtel/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.prixtel.com/decouvrir-prixtel/category/espace-presse/
- group: operate
  title: ''
  type: Support
  url: https://assistance.prixtel.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.prixtel.com/forfait-mobile/
- group: start
  title: ''
  type: Login
  url: https://espaceclient.prixtel.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://short.prixtel.com/cgv-cga
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pxtl.fr/docs/charte/res
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prixtel/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/prixtel
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prixtel-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/prixtel-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/prixtel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prixtel-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prixtel-llms.txt
coverage:
  checked: '2026-08-17'
  detail: Prixtel is a retail MVNO that sells flexible mobile subscriptions to human consumers and ships software only as an end-user phone app — there is no /developpeurs, /developers, /api or /docs page, no GitHub organization (api.github.com/orgs/prixtel is 404), and zero first-party packages across nine registries; api.prixtel.com resolves to a live nginx origin that serves the mobile app but answers 404 on its root and on every spec, GraphQL, MCP and well-known path probed against it.
  evidence:
  - status: 404
    url: https://www.prixtel.com/developpeurs
  - status: 404
    url: https://www.prixtel.com/api
  - status: 404
    url: https://www.prixtel.com/llms.txt
  - status: 404
    url: https://api.prixtel.com/
  - status: 404
    url: https://api.prixtel.com/openapi.json
  - status: 404
    url: https://api.prixtel.com/graphql
  - status: 404
    url: https://api.prixtel.com/.well-known/agent-card.json
  - status: 503
    url: https://www.prixtel.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/prixtel
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: Prixtel is a French mobile virtual network operator (MVNO) founded in 2004 by David Charles and headquartered in Aix-en-Provence. It is known for "forfaits flexibles" — mobile plans whose monthly price moves automatically between published tiers according to the data a subscriber actually consumed, with the ceiling known in advance — and it rides the SFR (historically also Orange) radio network rather than owning spectrum. Prixtel serves roughly 300,000 to 500,000 subscribers, reported about EUR 63.5M revenue in 2024, and was acquired by Altice France, the owner of SFR, in June 2021 for approximately EUR 415M while continuing to trade under its own brand; the Serena venture attribution that surfaced this profile is therefore a realized exit rather than a current holding. Prixtel publishes no public API, no developer portal, no SDK, no webhook catalog, and no machine-readable contract of any kind. Its only first-party software distribution is an end-user iOS/Android app for consumption
  tracking, invoices and line management; api.prixtel.com is that app's private backend and returns HTTP 404 on every probed path, including its own root.
image: https://cdn.prixtel.com/sources/prixtel/images/assets/logo-prixtel.svg
layout: provider
modified: '2026-08-17'
name: Prixtel
nav: Providers
network: true
overview: 'Prixtel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Telecommunications, Mobile, and MVNO.


  Prixtel''s developer surface includes engineering blog, support, pricing, and 14 more developer resources.'
plans:
- name: Prixtel Plans Pricing
  plan_count: 0
  slug: prixtel-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Prixtel Rate Limits
  slug: prixtel-rate-limits
score:
  band: emerging
  composite: 12.5
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Prixtel Domain Security
  slug: prixtel-domain-security
  summary_line: TLSv1.2 · DMARC
slug: prixtel
tags:
- Company
- Consumer
- Telecommunications
- Mobile
- MVNO
- Mobile Network Operator
- Mobile Plans
- Wireless
- Telecom
- France
- Europe
website: https://www.prixtel.com/
---
