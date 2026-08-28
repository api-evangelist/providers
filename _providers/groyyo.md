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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/groyyo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://groyyo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://groyyo.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://groyyo.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://groyyo.com/kyc-login
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/groyyo-llms.txt
coverage:
  checked: '2026-08-22'
  detail: 'Groyyo builds real software — the Groyyo + factory-management Android app and an internal factory ERP — but ships it only as apps to contracted brands and factories, with no developer program behind it: developer.groyyo.com, docs.groyyo.com and api.groyyo.com all 404, the site''s own Next.js route manifest lists no /developers, /docs or /api route, and every /.well-known/ and spec path (openapi.json, swagger.json, /graphql, agent-card.json) returns a true 404 verified against a bogus control path.'
  evidence:
  - status: 404
    url: https://developer.groyyo.com/
  - status: 404
    url: https://docs.groyyo.com/
  - status: 404
    url: https://api.groyyo.com/
  - status: 404
    url: https://groyyo.com/openapi.json
  - status: 404
    url: https://groyyo.com/.well-known/agent-card.json
  - status: 200
    url: https://groyyo.com/
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Groyyo is a Gurugram, India based B2B manufacturing and supply-chain company for the fashion, apparel and lifestyle industry, founded in July 2021 by Subin Mitra and Pratik Tiwari. It connects global brands with a vetted network of small and mid-sized Asian factories and gives those factories production software — sales-order management, bill-of-materials creation, production tracking, quality control and business reporting — delivered as the Groyyo and Groyyo + mobile apps and an internal factory ERP rather than as a public developer platform. The company also runs sourcing, fabric and consulting lines, plus RFQ and supplier-KYC intake on its own website. As of August 2026 Groyyo publishes no developer portal, no API documentation and no machine-readable API contract on any host it controls.
image: https://groyyo.com/images/logo-black.png
layout: provider
modified: '2026-08-22'
name: Groyyo
nav: Providers
network: true
overview: 'Groyyo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Supply Chain, Apparel, and Fashion.


  Groyyo''s developer surface includes support and 5 more developer resources.'
plans:
- name: Groyyo Plans Pricing
  plan_count: 0
  slug: groyyo-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Groyyo Rate Limits
  slug: groyyo-rate-limits
score:
  band: minimal
  composite: 9.4
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Groyyo Domain Security
  slug: groyyo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: groyyo
tags:
- Company
- Manufacturing
- Supply Chain
- Apparel
- Fashion
- Sourcing
- B2B
- ERP
- Quality Control
- India
website: https://groyyo.com/
---
