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
- group: company
  title: ''
  type: Website
  url: https://www.plantiblefoods.com/
- group: company
  title: ''
  type: About
  url: https://www.plantiblefoods.com/our-story
- group: other
  title: ''
  type: Team
  url: https://www.plantiblefoods.com/our-team
- group: other
  title: ''
  type: Products
  url: https://www.plantiblefoods.com/applications
- group: company
  title: ''
  type: Careers
  url: https://www.plantiblefoods.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.plantiblefoods.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.plantiblefoods.com/newsroom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.plantiblefoods.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plantiblefoods.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/plantible/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/plantible
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/plantiblefoods/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plantible-foods-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plantible-foods-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Plantible Foods manufactures physical food ingredients — RuBisCO protein extracted from duckweed at a Texas aquafarm — and sells them to food manufacturers, so there is no software product to expose; plantiblefoods.com is a 23-page Webflow marketing site whose sitemap contains no developer, API, or documentation page, and no api./developer./docs. subdomain resolves in DNS at all.
  evidence:
  - status: 404
    url: https://www.plantiblefoods.com/openapi.json
  - status: 404
    url: https://www.plantiblefoods.com/graphql
  - status: 404
    url: https://www.plantiblefoods.com/llms.txt
  - status: 404
    url: https://www.plantiblefoods.com/.well-known/agent-card.json
  - status: 404
    url: https://www.plantiblefoods.com/.well-known/api-catalog
  - status: 200
    url: https://www.plantiblefoods.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Plantible Foods is a business-to-business food-ingredient company founded in 2018 by Dutch entrepreneurs Tony and Maurits, with its first commercial production facility in Schleicher County, Texas. The company cultivates lemna (duckweed) in controlled, automated aquafarms and uses a proprietary water-based extraction process to isolate RuBisCO, sold as Rubi Protein — roughly 85% protein by weight with a PDCAAS of 1.0 — alongside Lemna Leaf Greens and application-specific systems such as RubiWhisk and RubiPrime. It sells to food manufacturers and ingredient companies rather than consumers, and in February 2026 became the first company to receive an FDA "no questions" GRAS letter for isolated RuBisCO protein in food. Investors include RA Capital, Nourish Ventures, Chipotle, Kellogg''s and CJ Group. Plantible is an agricultural manufacturing business: it publishes no public API, developer portal, SDK, or machine-readable contract of any kind, and plantiblefoods.com is a Webflow
  marketing site with no developer surface.'
image: https://cdn.prod.website-files.com/62bc3dbdb2ef9473c0480324/62c5ea25382a7e543203d152_meta-image.jpg
layout: provider
modified: '2026-08-26'
name: Plantible Foods
nav: Providers
network: true
overview: 'Plantible Foods is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Food Ingredients, Alternative Protein, and Plant-Based.


  Plantible Foods'' developer surface includes engineering blog and 13 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Plantible Foods Domain Security
  slug: plantible-foods-domain-security
  summary_line: TLSv1.3 · HSTS
slug: plantible-foods
tags:
- Company
- Food
- Food Ingredients
- Alternative Protein
- Plant-Based
- Agriculture
- Biotechnology
- Manufacturing
- Sustainability
- Texas
website: https://www.plantiblefoods.com/
---
