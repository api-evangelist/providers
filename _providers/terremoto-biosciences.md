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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terremoto-biosciences-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terremoto-biosciences-llms.txt
- group: company
  title: ''
  type: Website
  url: https://terremotobio.com/
- group: company
  title: ''
  type: About
  url: https://terremotobio.com/about/
- group: company
  title: ''
  type: Blog
  url: https://terremotobio.com/news/
- group: operate
  title: ''
  type: Support
  url: https://terremotobio.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terremotobio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://terremotobio.com/privacy/privacy-policy/
coverage:
  checked: '2026-08-30'
  detail: Terremoto Biosciences is a clinical-stage covalent small-molecule drug developer whose entire public surface is a WordPress marketing site (science, pipeline, news, careers) — every contract probe missed (no OpenAPI/Swagger at the root, no /graphql, no /mcp, no agent card, and none of api./developers./docs./portal.terremotobio.com resolve in DNS), leaving only the WordPress CMS's own incidental /wp-json/ route index and an All in One SEO-generated llms.txt, neither of which is a product API.
  evidence:
  - status: 404
    url: https://terremotobio.com/openapi.json
  - status: 404
    url: https://terremotobio.com/graphql
  - status: 404
    url: https://terremotobio.com/.well-known/agent-card.json
  - status: 0
    url: https://api.terremotobio.com/
  - status: 200
    url: https://terremotobio.com/llms.txt
  - status: 200
    url: https://terremotobio.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: 'Terremoto Biosciences is a privately held, clinical-stage biotechnology company based in South San Francisco, California, building a covalent drug discovery and development engine around lysine-based covalency. Founded in 2022 by veterans of Principia Biopharma and backed by OrbiMed and Third Rock Ventures across Series A ($75M), Series B ($175M) and Series C ($108M) financings, the company designs highly selective small-molecule medicines aimed both at improving on known drug targets and at reaching targets previously considered undruggable. Its lead program, TER-2013, is an AKT1-selective inhibitor granted FDA Fast Track designation for breast cancer, with additional work in oncology and hereditary hemorrhagic telangiectasia. Terremoto is a therapeutics developer, not a software vendor: it publishes no public API, developer portal, SDK or machine-readable API contract, and its public web surface is a corporate marketing site covering science, pipeline, news and careers.'
image: https://terremotobio.com/wp-content/uploads/Terremoto_Footer_Logo.png
layout: provider
modified: '2026-08-30'
name: Terremoto Biosciences
nav: Providers
network: true
overview: 'Terremoto Biosciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Life Sciences.


  Terremoto Biosciences'' developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
security:
- kind: domain-security
  name: Terremoto Biosciences Domain Security
  slug: terremoto-biosciences-domain-security
  summary_line: TLSv1.3 · DMARC
slug: terremoto-biosciences
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Life Sciences
- Oncology
- Healthcare
- Clinical Stage
- Small Molecule
website: https://terremotobio.com/
---
