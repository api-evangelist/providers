---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The anonymously readable WordPress REST API behind kriyatherapeutics.com. It exposes the company's 28-item `news` custom post type (the full press-release archive back to the May 2020 Series A announc
  name: Kriya Therapeutics Content API
  slug: kriya-therapeutics-content-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kriya-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kriyatherapeutics.com/
- group: other
  title: ''
  type: Pipeline
  url: https://kriyatherapeutics.com/pipeline/
- group: other
  title: ''
  type: ProductDesign
  url: https://kriyatherapeutics.com/product-design/
- group: other
  title: ''
  type: Research
  url: https://kriyatherapeutics.com/research-development/
- group: other
  title: ''
  type: Manufacturing
  url: https://kriyatherapeutics.com/manufacturing/
- group: other
  title: ''
  type: Team
  url: https://kriyatherapeutics.com/our-team/
- group: company
  title: ''
  type: News
  url: https://kriyatherapeutics.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://kriyatherapeutics.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://kriyatherapeutics.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://kriyatherapeutics.com/connect/
- group: operate
  title: ''
  type: Support
  url: https://kriyatherapeutics.com/connect/
- group: other
  title: ''
  type: SiteMap
  url: https://kriyatherapeutics.com/site-map/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kriyatherapeutics.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kriyatherapeutics.com/terms-of-use
- group: commercial
  title: ''
  type: DataPrivacyTerms
  url: https://kriyatherapeutics.com/data-privacy-terms/
- group: commercial
  title: ''
  type: PrivacyNotices
  url: https://kriyatherapeutics.com/privacy-notices/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kriyatx/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/kriyatx
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/kriya-therapeutics_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/kriya-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kriya-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kriya-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kriya-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kriya-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kriya-therapeutics-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kriya-therapeutics-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kriya-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Kriya Therapeutics, Inc. is a clinical-stage biopharmaceutical company founded in 2019 that designs, develops and manufactures one-time AAV gene therapies for chronic diseases that affect large patient populations, rather than for ultra-rare indications alone. It is headquartered at 1219 Shiloh Glenn Drive in Durham, North Carolina, inside Research Triangle Park, with additional operations in Palo Alto, California, and has raised more than $900 million across Series A ($80M, 2020), Series B ($100M, 2021), Series C (over $430M including a $150M extension, 2022-2023) and Series D ($320M, September 2025). Its pipeline spans three therapeutic areas: ophthalmology (geographic atrophy, thyroid eye disease including KRIYA-586), metabolic disease (Type 1 diabetes, MASH/NASH, an investigational AAV-FGF21 program) and neurology (trigeminal neuralgia, added through the 2022 acquisition of Redpin Therapeutics). The company operates a vertically integrated engine that pairs computational
  product design with in-house GMP manufacturing — the same unit operations from 1L research scale through 50L, 500L and 3,000L bioreactor scale, with Akta chromatography purification, vial filling and in-house analytical characterization of critical quality attributes. It was selected for the FDA PreCheck Pilot Program in June 2026. Kriya Therapeutics runs no developer program and publishes no product API, no developer portal and no API documentation; the only machine-readable surface reachable without credentials is the WordPress REST content API behind kriyatherapeutics.com, catalogued here.'
image: https://kriyatherapeutics.com/wp-content/uploads/2023/03/Kriya-Logo-Bl.png
layout: provider
modified: '2026-08-04'
name: Kriya Therapeutics
nav: Providers
network: true
overview: 'Kriya Therapeutics publishes 1 API on the [APIs.io](https://apis.io/) network: Content API. Tagged areas include Company, biotechnology, pharmaceuticals, gene-therapy, and aav.


  Kriya Therapeutics'' developer surface includes product news, support, authentication, and 26 more developer resources.'
random_paper: 78
score:
  band: thin
  composite: 30.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 52.2
    developer_ergonomics: 16.8
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 30.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Kriya Therapeutics Authentication
  slug: kriya-therapeutics-authentication
  summary_line: none/apiKey/http · 3 schemes
- kind: domain-security
  name: Kriya Therapeutics Domain Security
  slug: kriya-therapeutics-domain-security
  summary_line: TLSv1.3
slug: kriya-therapeutics
tags:
- Company
- biotechnology
- pharmaceuticals
- gene-therapy
- aav
- ophthalmology
- metabolic-disease
- neurology
- life-sciences
- clinical-trials
- biomanufacturing
- content-api
website: https://kriyatherapeutics.com/
---
