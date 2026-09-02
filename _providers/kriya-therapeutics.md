---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Route, type, taxonomy and status discovery documents.
  name: Kriya Therapeutics Discovery API
  slug: kriya-therapeutics-discovery-api
- description: The `gutena_forms` custom post type used for the site contact form.
  name: Kriya Therapeutics Forms API
  slug: kriya-therapeutics-forms-api
- description: Media library (304 attachments at harvest time).
  name: Kriya Therapeutics Media API
  slug: kriya-therapeutics-media-api
- description: The `news` custom post type — the company press-release archive (28 items at harvest, back to May 2020).
  name: Kriya Therapeutics News API
  slug: kriya-therapeutics-news-api
- description: oEmbed 1.0 provider endpoint for kriyatherapeutics.com URLs.
  name: Kriya Therapeutics Oembed API
  slug: kriya-therapeutics-oembed-api
- description: Corporate and pipeline pages (18 published at harvest time).
  name: Kriya Therapeutics Pages API
  slug: kriya-therapeutics-pages-api
- description: Core blog/post collection (33 items at harvest).
  name: Kriya Therapeutics Posts API
  slug: kriya-therapeutics-posts-api
- description: Cross-content search across published objects.
  name: Kriya Therapeutics Search API
  slug: kriya-therapeutics-search-api
- description: Categories, tags, news categories and team keywords.
  name: Kriya Therapeutics Taxonomy API
  slug: kriya-therapeutics-taxonomy-api
- description: The `team` custom post type. Registered and reachable, but empty (X-WP-Total 0) — the Team page is authored as page markup.
  name: Kriya Therapeutics Team API
  slug: kriya-therapeutics-team-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kriya Therapeutics Content Discovery API
  slug: open-kriya-therapeutics-discovery-api
- collection_type: open
  name: Kriya Therapeutics Content Forms API
  slug: open-kriya-therapeutics-forms-api
- collection_type: open
  name: Kriya Therapeutics Content Media API
  slug: open-kriya-therapeutics-media-api
- collection_type: open
  name: Kriya Therapeutics Content News API
  slug: open-kriya-therapeutics-news-api
- collection_type: open
  name: Kriya Therapeutics Content Oembed API
  slug: open-kriya-therapeutics-oembed-api
- collection_type: open
  name: Kriya Therapeutics Content Pages API
  slug: open-kriya-therapeutics-pages-api
- collection_type: open
  name: Kriya Therapeutics Content Posts API
  slug: open-kriya-therapeutics-posts-api
- collection_type: open
  name: Kriya Therapeutics Content Search API
  slug: open-kriya-therapeutics-search-api
- collection_type: open
  name: Kriya Therapeutics Content Taxonomy API
  slug: open-kriya-therapeutics-taxonomy-api
- collection_type: open
  name: Kriya Therapeutics Content Team API
  slug: open-kriya-therapeutics-team-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/kriya-therapeutics-content-overlay.yaml
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
overview: 'Kriya Therapeutics publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Forms API, Media API, and 7 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Gene Therapy, and AAV.


  Kriya Therapeutics'' developer surface includes product news, support, authentication, and 27 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 63.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 48.6
    developer_ergonomics: 18.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 36.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kriya-therapeutics/refs/heads/main/screenshots/kriya-therapeutics-2026-08-07T171340.png
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
- Biotechnology
- Pharmaceuticals
- Gene Therapy
- AAV
- Ophthalmology
- Metabolic Disease
- Neurology
- Life Sciences
- Clinical Trials
- Biomanufacturing
- content-api
website: https://kriyatherapeutics.com/
---
