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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adstruc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adstruc.com/
- group: start
  title: ''
  type: Login
  url: https://www.adstruc.com/login
- group: commercial
  title: ''
  type: Plans
  url: plans/adstruc-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adstruc-llms.txt
coverage:
  checked: '2026-08-12'
  detail: www.adstruc.com has been reduced to a single 3KB splash page since the Vistar Media acquisition — /about, /product, /pricing, /contact, /blog, /docs and /developers all return a Symfony JSON 404, no api./docs./developer./app. subdomain resolves, and the working product now lives at vistarmedia.com/adstruc under the acquirer's brand.
  evidence:
  - status: 200
    url: https://www.adstruc.com/
  - status: 404
    url: https://www.adstruc.com/developers
  - status: 404
    url: https://www.adstruc.com/openapi.json
  - status: 404
    url: https://www.adstruc.com/.well-known/agent-card.json
  - status: 200
    url: https://www.vistarmedia.com/adstruc
  reason: defunct
  state: none
created: '2026-07-17'
description: ADstruc is a technology platform for the out-of-home (OOH) advertising industry, founded in 2010 in New York City by John Laramie and Sam Herbert. It provides workflow-automation software, including its Drive product, that lets brands and agencies plan, buy, and manage traditional and digital out-of-home media campaigns, and gives OOH operators cloud-based tools to manage and promote their inventory and interact with clients in real time. ADstruc was acquired by Vistar Media in April 2024 (from PJX Media) and the product is now sold as "Adstruc by Vistar Media" as part of that company's out-of-home advertising stack. ADstruc publishes no public developer API, portal, SDK or machine-readable contract of its own. The www.adstruc.com site is now a splash page whose only live routes are / and /login, and every developer and /.well-known/ path returns 404. The SSP and DSP APIs at developers.vistarmedia.com belong to Vistar Media, name Vistar hosts, and never mention ADstruc, so they
  are profiled under Vistar Media rather than credited here.
image: https://www.adstruc.com/images/homepage/pigeon_favicon.ico
layout: provider
modified: '2026-08-12'
name: ADstruc
nav: Providers
network: true
overview: ADstruc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Out-of-Home, OOH, and AdTech.
plans:
- name: Adstruc Plans Pricing
  plan_count: 0
  slug: adstruc-plans-pricing
random_paper: 38
score:
  band: minimal
  composite: 8.4
  delta: 0.8
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adstruc/refs/heads/main/screenshots/adstruc-2026-07-25T181703.png
security:
- kind: domain-security
  name: Adstruc Domain Security
  slug: adstruc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adstruc
tags:
- Company
- Advertising
- Out-of-Home
- OOH
- AdTech
- Digital Out-of-Home
- Media Buying
- Marketing
website: https://adstruc.com/
---
