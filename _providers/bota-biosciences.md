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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bota-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bota.bio/
- group: company
  title: ''
  type: About
  url: https://bota.bio/about-bota/
- group: other
  title: ''
  type: Technology
  url: https://bota.bio/bota-biofoundry/
- group: other
  title: ''
  type: Product
  url: https://bota.bio/performance-protein-solutions/
- group: other
  title: ''
  type: Brand
  url: https://www.heliagenesis.com/
- group: other
  title: ''
  type: Brand
  url: https://www.yuccaelements.com/
- group: operate
  title: ''
  type: Contact
  url: https://bota.bio/contact/
- group: company
  title: ''
  type: Blog
  url: https://bota.bio/bota-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://bota.bio/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/botabio
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/bota-biosciences-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bota-biosciences-llms.txt
coverage:
  checked: '2026-08-08'
  detail: Bota's only software product, the SAION AI platform at saion.ai, is a Flutter canvas application behind a login whose backend enforces an administrator-managed email and domain whitelist, so no reference, spec or signup is reachable without an approved account — saion.ai/openapi.json answers 200 but returns the same single-page-app shell as a nonsense control path, not a specification — while the corporate site bota.bio publishes marketing and news pages only.
  evidence:
  - status: 404
    url: https://bota.bio/openapi.json
  - status: 404
    url: https://bota.bio/.well-known/agent-card.json
  - status: 200
    url: https://saion.ai/openapi.json
  - status: 200
    url: https://saion.ai/robots.txt
  - status: 404
    url: https://api.github.com/orgs/botabio
  reason: customer-only-docs
  state: gated
created: '2026-08-08'
description: 'Bota Biosciences (Bota Bio, 恩和科技) is an industrial and synthetic biology company that applies AI-driven computation and laboratory automation to bio-manufacturing. Its in-house Bota Biofoundry and Cell2Cloud platforms combine computational algorithms, non-model industrial strain engineering, rapid iterative enzyme engineering and performance protein design to shorten design-build-test-learn cycles, and in March 2026 it launched SAION AI, a three-layer "Physical AI" platform (cognition, orchestration, execution) that drives laboratory hardware through a proprietary Biological Protocol Language. Bota commercializes this work as physical ingredients rather than software: Purtect bio-preservatives (nisin, natamycin, ε-poly-lysine, lysozyme), Prorylia biomimetic proteins and Re² Coffea Arabica peptides, sold through its HeliaGenesis food and nutrition brand and its YuccaElements personal care brand, with partnerships including BASF, Proya, Syensqo and Puratos. Founded in 2019 with
  operations in Hangzhou, China and the San Francisco Bay Area, Bota publishes no developer portal, no public API documentation, no SDKs and no machine-readable specification; its computational software is internal laboratory tooling and its SAION AI application is reachable only through a login with an administrator-managed account whitelist.'
image: https://bota.bio/wp-content/uploads/2024/08/bota-logo.png
layout: provider
modified: '2026-08-08'
name: Bota Biosciences
nav: Providers
network: true
overview: 'Bota Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Synthetic Biology, Biomanufacturing, and Industrial Biotechnology.


  Bota Biosciences'' developer surface includes engineering blog and 12 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Bota Biosciences Domain Security
  slug: bota-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bota-biosciences
tags:
- Company
- Biotechnology
- Synthetic Biology
- Biomanufacturing
- Industrial Biotechnology
- Enzyme Engineering
- Ingredients
- Food and Nutrition
- Personal Care
- Artificial Intelligence
- China
website: https://bota.bio/
---
