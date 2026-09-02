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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pattern-ag-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pattern-ag-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.pattern.ag/
- group: other
  title: ''
  type: ParentCompany
  url: https://earthoptics.com/
- group: company
  title: ''
  type: Blog
  url: https://earthoptics.com/news-insights
- group: operate
  title: ''
  type: Support
  url: https://earthoptics.com/contact-us
coverage:
  checked: '2026-08-26'
  detail: Pattern Ag merged into EarthOptics in August 2024 and the brand was retired — https://www.pattern.ag/ now issues an HTTP 301 to www.earthoptics.com, every Pattern Ag deep link 404s, and the company never published a developer portal or API contract under its own domain before the merger.
  evidence:
  - status: 301
    url: https://www.pattern.ag/
  - status: 404
    url: https://www.pattern.ag/about
  - status: 404
    url: https://www.pattern.ag/.well-known/security.txt
  - status: 404
    url: https://www.pattern.ag/openapi.json
  - status: 200
    url: https://www.linkedin.com/company/pattern-ag/
  reason: defunct
  state: none
created: '2026-08-26'
description: Pattern Ag was a predictive-agronomy company founded in 2018 and headquartered in Emeryville, California, that applied DNA sequencing and soil metagenomics to forecast agronomic outcomes twelve months ahead of a growing season. Its Complete Bio and Pattern 360 products profiled the soil microbiome to predict pest, pathogen and nutrient-deficiency pressure, informing crop-protection, seed-selection and fertility decisions for corn and soybean growers, and in 2023 the company announced what it described as the world's largest single-ecosystem metagenomics database. In August 2024 Pattern Ag merged with soil-sensing company EarthOptics; the combined business operates under the EarthOptics name and the Pattern Ag brand has been retired. As of this profile the pattern.ag website issues an HTTP 301 to www.earthoptics.com, every Pattern Ag deep link returns 404, and the Pattern Ag LinkedIn page redirects to an EarthOptics company page. Pattern Ag never published a public developer
  program, API documentation, SDKs or a machine-readable API contract under its own brand, and no Pattern Ag API surface survives. The successor company's private REST API is profiled separately at all/earth-optics.
layout: provider
modified: '2026-08-26'
name: Pattern Ag
nav: Providers
network: true
overview: 'Pattern Ag is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Soil, and Soil Biology.


  Pattern Ag''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 4
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Pattern Ag Domain Security
  slug: pattern-ag-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pattern-ag
tags:
- Company
- Agriculture
- AgTech
- Soil
- Soil Biology
- Metagenomics
- Predictive Agronomy
- Precision Agriculture
- Agronomy
- Soil Health
- Acquired
- Retired Brand
website: https://www.pattern.ag/
---
