---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kuehnle-agrosystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kuehnleagro.com/
- group: other
  title: ''
  type: Technology
  url: https://www.kuehnleagro.com/technology
- group: other
  title: ''
  type: Product
  url: https://www.kuehnleagro.com/astaxanthin
- group: other
  title: ''
  type: Product
  url: https://www.kuehnleagro.com/protein
- group: other
  title: ''
  type: Process
  url: https://www.kuehnleagro.com/dark-fermentation
- group: operate
  title: ''
  type: Contact
  url: https://www.kuehnleagro.com/contact
- group: operate
  title: ''
  type: Support
  url: https://www.kuehnleagro.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kuehnle-agrosystems-inc.
- group: company
  title: ''
  type: Partners
  url: https://www.corbion.com/media/press-release/3135449?language=English
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kuehnle-agrosystems-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Kuehnle AgroSystems sells microalgae-derived ingredients — natural astaxanthin and algal protein produced by a patented dark-fermentation process — so software is not the product; kuehnleagro.com is a six-page Squarespace marketing site whose sitemap lists six URLs and no developer, docs or API page, there is no GitHub organization or npm/PyPI package under the company name, and api./docs./developer..kuehnleagro.com are wildcard DNS to a Squarespace address whose TLS certificate does not cover them, so no HTTPS connection to them is possible.
  evidence:
  - status: 404
    url: https://www.kuehnleagro.com/openapi.json
  - status: 404
    url: https://www.kuehnleagro.com/api-docs
  - status: 404
    url: https://www.kuehnleagro.com/developers
  - status: 404
    url: https://www.kuehnleagro.com/llms.txt
  - status: 404
    url: https://www.kuehnleagro.com/.well-known/agent-card.json
  - status: 404
    url: https://www.kuehnleagro.com/.well-known/security.txt
  - status: 0
    url: https://api.kuehnleagro.com/
  - status: 404
    url: https://api.github.com/orgs/kuehnleagro
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Kuehnle AgroSystems, Inc. (KAS) is a Honolulu, Hawaii microalgae biotechnology company founded in 2007 by Dr. Adelheid "Heidi" Kuehnle, with a second site in Cork, Ireland. KAS produces high-value natural products from microalgae for the food, feed and health markets using a patented heterotrophic "dark fermentation" process and proprietary non-GMO Hawaiian algal strains that run in standard fermentation equipment rather than open ponds or photobioreactors, compressing production from weeks to days with substantially lower cost, land, water and energy use. Its lead products are natural astaxanthin and algal protein, sold into nutraceuticals, cosmetics and skincare, functional foods and beverages, and aquaculture and animal feed; in August 2025 KAS entered a development and commercialization partnership with Corbion for an esterified natural astaxanthin. KAS sells ingredients, strains and fermentation process technology rather than software: it publishes no API, developer program,
  SDK, or machine-readable contract, and kuehnleagro.com is a six-page Squarespace marketing site.'
image: https://static1.squarespace.com/static/641fd5cedcca7622021a7b58/t/6622e938ae3f8f1f752d2240/1713563960811/KAS%2Blogo_white_gray-3.png?format=1500w
layout: provider
modified: '2026-08-23'
name: Kuehnle AgroSystems
nav: Providers
network: true
overview: 'Kuehnle AgroSystems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Microalgae, Fermentation, and Astaxanthin.


  Kuehnle AgroSystems'' developer surface includes support and 10 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 6.0
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kuehnle-agrosystems/refs/heads/main/screenshots/kuehnle-agrosystems-2026-09-02T150157.png
security:
- kind: domain-security
  name: Kuehnle Agrosystems Domain Security
  slug: kuehnle-agrosystems-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kuehnle-agrosystems
tags:
- Company
- Biotechnology
- Microalgae
- Fermentation
- Astaxanthin
- Ingredients
- Food and Beverage
- Aquaculture
- Nutraceuticals
- AgTech
- Hawaii
website: https://www.kuehnleagro.com/
---
