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
api_count: 1
apis:
- description: Live JSON API host for Pax AI (api.paxai.com). A health endpoint is publicly reachable; no public OpenAPI, reference documentation, or developer program was discoverable at enrichment time.
  name: Pax API
  slug: pax-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pax-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pax-llms.txt
- group: company
  title: ''
  type: Website
  url: https://paxai.com/
- group: company
  title: ''
  type: Blog
  url: https://paxai.com/blog
created: '2026-07-17'
description: Pax (Pax AI) is a San Francisco-based artificial intelligence company that automates U.S. duty drawback claims, letting importers, retailers, and manufacturers reclaim overpaid tariffs and import duties. Branding itself the "AI Broker for Tariff Refunds" and "TurboTax for import duty rebate," Pax uses proprietary AI to automate data extraction, validation, transaction matching, refund calculation, and electronic claim submission to U.S. Customs and Border Protection with minimal manual effort. Founded by former duty-drawback experts and engineers from Charter Brokerage, MIT, Amazon, Flexport, and Brex, Pax is backed by Y Combinator, Initialized Capital, General Catalyst, Flexport, Soma Capital, Basis Set Ventures, and others. This profile was enriched by the API Evangelist pipeline.
image: https://paxai.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Pax
nav: Providers
network: true
overview: 'Pax publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Saas, Artificial Intelligence, Trade Finance, and Customs.


  Pax''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pax/refs/heads/main/screenshots/pax-2026-08-07T191617.png
security:
- kind: domain-security
  name: Pax Domain Security
  slug: pax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pax
tags:
- Company
- Enterprise Saas
- Artificial Intelligence
- Trade Finance
- Customs
- Duty Drawback
- Tariffs
- Fintech
- Supply Chain
website: https://paxai.com/
---
