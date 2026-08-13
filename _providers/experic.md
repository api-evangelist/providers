---
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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/experic-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/experic-llms.txt
- group: company
  title: ''
  type: Website
  url: https://expericservices.com/
- group: company
  title: ''
  type: About
  url: https://expericservices.com/the-experic-difference/
- group: operate
  title: ''
  type: Support
  url: https://expericservices.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://expericservices.com/news-events/
- group: company
  title: ''
  type: BlogRSS
  url: https://expericservices.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://expericservices.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/epic-csc-llc/
coverage:
  checked: '2026-08-12'
  detail: Experic is a pharmaceutical CDMO selling physical development, manufacturing and clinical-supply services; its entire 142-URL sitemap is marketing, resource, news and careers pages with no developer, docs, API or portal path, and every contract-discovery probe (openapi.json, swagger.json, api-docs, graphql, llms.txt, all eight /.well-known/ paths) returned 404 from the origin, with the only machine-readable endpoint being the marketing site's own WordPress /wp-json/ CMS surface.
  evidence:
  - status: 404
    url: https://expericservices.com/openapi.json
  - status: 404
    url: https://expericservices.com/graphql
  - status: 404
    url: https://expericservices.com/llms.txt
  - status: 404
    url: https://expericservices.com/.well-known/agent-card.json
  - status: 404
    url: https://expericservices.com/.well-known/security.txt
  - status: 0
    url: https://api.expericservices.com/
  - status: 0
    url: https://developer.expericservices.com/
  - status: 200
    url: https://expericservices.com/page-sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: Experic is a specialist powder-handling contract development and manufacturing organization (CDMO) founded in 2018, headquartered in Cranbury, New Jersey, with an EU clinical supply center in Ireland. The company provides process, analytical and formulation development, clinical and commercial cGMP manufacturing, dry powder inhalation (DPI) and capsule/powder dosing, autoinjector and pen assembly, and clinical trial packaging, labeling, storage and logistics. Experic is a physical-goods manufacturing and clinical supply services business; it publishes no public developer program, API documentation, or machine-readable API contract.
image: https://expericservices.com/wp-content/uploads/2025/02/cropped-favicon-X-270x270.png
layout: provider
modified: '2026-08-12'
name: Experic
nav: Providers
network: true
overview: 'Experic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Life Sciences, Manufacturing, and CDMO.


  Experic''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 32
score:
  band: minimal
  composite: 9.6
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: domain-security
  name: Experic Domain Security
  slug: experic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: experic
tags:
- Company
- Pharmaceuticals
- Life Sciences
- Manufacturing
- CDMO
- Clinical Trials
- Contract Manufacturing
- Drug Delivery
- Supply Chain
- Packaging
website: https://expericservices.com/
---
