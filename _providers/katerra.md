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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/katerra_stock/
coverage:
  checked: '2026-08-23'
  detail: Katerra shut down and filed Chapter 11 on 6 June 2021 and its Apollo software was sold to Builders FirstSource that September; katerra.com now answers Cloudflare error 1001 (HTTP 409) on every path and refuses a TLS handshake entirely, api/docs/developer/apollo subdomains no longer resolve, and 4,068 archived katerra.com URLs contain no developer portal, OpenAPI, Swagger or SDK — only Adobe Experience Manager site JSON such as /bin/www/projects.json — so there is no API surface to profile.
  evidence:
  - status: 409
    url: http://katerra.com/
  - status: 409
    url: http://katerra.com/openapi.json
  - status: 409
    url: http://katerra.com/.well-known/agent-card.json
  - status: 409
    url: http://katerra.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/katerrainc
  reason: defunct
  state: none
created: '2026-08-23'
description: 'Katerra was a Menlo Park, California off-site construction and building-technology company founded in 2015 by former Flextronics chief executive Michael Marks with Fritz Wolff and Jim Davidson, built on the thesis that a single vertically integrated firm could design, engineer, manufacture and assemble buildings end to end — running its own architecture practice, factories in Phoenix, Tracy and Spokane producing cross-laminated timber and prefabricated wall, floor and bathroom assemblies, and its own supply chain and general contracting arm. It raised more than $2 billion across a dozen rounds, including an $865M Series D led by the SoftBank Vision Fund in January 2018 at a valuation above $3 billion and a $200M recapitalization in December 2020 that handed SoftBank majority control. Its only software product was Katerra Apollo, announced in February 2019 as a design-to-field platform (Apollo Construct, Apollo Insight, Apollo Connect) whose launch materials promised "open API
  integration" with existing construction workflows — but Apollo was sold to Katerra''s own construction customers and never shipped a public developer portal, API reference, SDK or machine-readable specification. The insolvency of its SoftBank-backed lender Greensill Capital cost Katerra its bonding capacity, and the company shut down and filed Chapter 11 in the Southern District of Texas on 6 June 2021. Its assets were broken up: the Apollo software went to Builders FirstSource for roughly $4.5M on 9 September 2021, and the factories were sold separately. katerra.com no longer serves a site — it answers a Cloudflare error 1001 on every path and cannot complete a TLS handshake at all. This profile is retained as a historical record; there is no API surface left to catalog.'
image: https://web.archive.org/web/20190712083445id_/http://katerra.com/content/dam/katerra/www/en_us/assets/images/logo/katerra.jpg/_jcr_content/renditions/cq5dam.web.1280.1280.jpeg
layout: provider
modified: '2026-08-23'
name: Katerra
nav: Providers
network: true
overview: Katerra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Construction, Construction Technology, and Building Materials.
random_paper: 11
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
slug: katerra
tags:
- Company
- Defunct
- Construction
- Construction Technology
- Building Materials
- Modular Construction
- Prefabrication
- Manufacturing
- Real-Estate
- Supply Chain
---
