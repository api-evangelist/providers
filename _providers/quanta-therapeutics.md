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
- group: company
  title: ''
  type: Website
  url: https://www.quantatx.com/
- group: company
  title: ''
  type: About
  url: https://www.quantatx.com/#about
- group: other
  title: ''
  type: Team
  url: https://www.quantatx.com/#leadership
- group: other
  title: ''
  type: Science
  url: https://www.quantatx.com/#platform
- group: other
  title: ''
  type: Products
  url: https://www.quantatx.com/#pipeline
- group: other
  title: ''
  type: Research
  url: https://www.quantatx.com/pipeline/investigational-agents/
- group: company
  title: ''
  type: News
  url: https://www.quantatx.com/#news
- group: company
  title: ''
  type: Careers
  url: https://www.quantatx.com/#careers
- group: operate
  title: ''
  type: Contact
  url: https://www.quantatx.com/#contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quanta-therapeutics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/quanta-therapeutics_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quanta-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quanta-therapeutics-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Quanta Therapeutics is a clinical-stage oncology drug developer whose product is a small molecule, not software; its entire corporate presence is one static HTML page served from Apache, where /about/, /platform/, /pipeline/, /news/, /careers/ and /contact/ all return the identical 33,984-byte document, and no api./developer./docs.quantatx.com subdomain resolves in DNS.
  evidence:
  - status: 404
    url: https://www.quantatx.com/openapi.json
  - status: 404
    url: https://www.quantatx.com/llms.txt
  - status: 404
    url: https://www.quantatx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.quantatx.com/graphql
  - status: 404
    url: https://www.quantatx.com/wp-json/
  - status: 0
    url: https://api.quantatx.com/
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Quanta Therapeutics is a privately held, clinical-stage biopharmaceutical company founded in 2018 and headquartered at 2 Tower Place in South San Francisco, California, with a second site in Radnor, Pennsylvania. It develops oral allosteric small-molecule medicines for RAS-driven cancers by targeting the protein-protein interactions that drive oncogenic RAS signaling, an approach the company describes as conformational blockade of RAS. Its discovery engine is a proprietary high-throughput Second Harmonic Generation (SHG) optical platform that detects subtle protein conformational changes and so surfaces allosteric modulators of signaling complexes that conventional binding assays miss. The clinical pipeline is a set of direct multi-KRAS inhibitors: QTX3034, a G12D-preferring oral multi-KRAS inhibitor in Phase 1 as monotherapy and in combination with cetuximab in KRAS G12D-mutant solid tumors; QTX3544, a G12V-preferring multi-KRAS inhibitor cleared for IND in January 2025; and
  QTX3046, which dosed its first patient in a Phase 1/1b trial in June 2024. Indications span pancreatic, colorectal, lung and endometrial cancers. The company announced a $60 million Series C in October 2021 and a Series D of over $50 million in May 2023 led by Avidity Partners alongside Sofinnova Investments, Vida Ventures, Surveyor Capital, Longitude Capital and AbbVie Ventures. Quanta Therapeutics runs no developer program and publishes no public API. Its corporate site is a single static HTML document served from Apache with anchor-based sections; probes for OpenAPI, GraphQL, MCP, llms.txt and every /.well-known/ discovery path returned HTTP 404, and no api./developer./docs. subdomain resolves.'
image: https://www.quantatx.com/themes/default/images/logo.svg
layout: provider
modified: '2026-08-05'
name: Quanta Therapeutics
nav: Providers
network: true
overview: 'Quanta Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Oncology.


  Quanta Therapeutics'' developer surface includes product news and 12 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 3.3
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quanta-therapeutics/refs/heads/main/screenshots/quanta-therapeutics-2026-09-02T152605.png
security:
- kind: domain-security
  name: Quanta Therapeutics Domain Security
  slug: quanta-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quanta-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Oncology
- Drug Discovery
- Precision Medicine
- Clinical Trials
- Healthcare
website: https://www.quantatx.com/
---
