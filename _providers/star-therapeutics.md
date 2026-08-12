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
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-11'
api_count: 9
apis:
- description: Comment collection. Registered and reachable, but empty — no post on this deployment carries comments.
  name: Star Therapeutics Comments API
  slug: star-therapeutics-comments-api
- description: Avada theme custom post types (avada_faq, avada_portfolio). Registered and anonymously reachable, but both report zero published items.
  name: Star Therapeutics Custom Types API
  slug: star-therapeutics-custom-types-api
- description: Route, type, taxonomy and status discovery documents.
  name: Star Therapeutics Discovery API
  slug: star-therapeutics-discovery-api
- description: Media library (661 attachments at harvest time).
  name: Star Therapeutics Media API
  slug: star-therapeutics-media-api
- description: oEmbed 1.0 provider endpoint for star-therapeutics.com URLs.
  name: Star Therapeutics Oembed API
  slug: star-therapeutics-oembed-api
- description: Corporate pages (11 published at harvest time).
  name: Star Therapeutics Pages API
  slug: star-therapeutics-pages-api
- description: News archive — press releases, news coverage and scientific presentations (28 published at harvest time).
  name: Star Therapeutics Posts API
  slug: star-therapeutics-posts-api
- description: Cross-content search across published objects.
  name: Star Therapeutics Search API
  slug: star-therapeutics-search-api
- description: Categories and tags. Five categories are registered; the post_tag taxonomy is registered but empty.
  name: Star Therapeutics Taxonomy API
  slug: star-therapeutics-taxonomy-api
artifact_total: 11
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/star-therapeutics-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://star-therapeutics.com/
- group: company
  title: ''
  type: About
  url: https://star-therapeutics.com/our-approach/
- group: other
  title: ''
  type: Leadership
  url: https://star-therapeutics.com/our-leadership/
- group: company
  title: ''
  type: News
  url: https://star-therapeutics.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://star-therapeutics.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://star-therapeutics.com/our-careers/
- group: other
  title: ''
  type: PatientResources
  url: https://star-therapeutics.com/share-your-story/
- group: other
  title: ''
  type: ConsumerHealth
  url: https://star-therapeutics.com/consumer-health-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://star-therapeutics.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://star-therapeutics.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/star-tx
- group: other
  title: ''
  type: SubsidiaryCompany
  url: https://vegatherapeutics.com/
- group: other
  title: ''
  type: SubsidiaryCompany
  url: https://electra-therapeutics.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/star-therapeutics_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/star-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/star-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/star-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/star-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/star-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/star-therapeutics-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/star-therapeutics-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/star-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/star-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: Star Therapeutics is a clinical-stage biotechnology company headquartered at 201 Haskins Way in South San Francisco, California, that transforms the lives of patients with serious diseases by discovering and developing best-in-class antibody therapies, with an initial focus on hematology and immunology. It operates a hub-and-spoke model, building a family of companies that each pursue a distinct area of novel biology, and it develops each programme under a pipeline-in-a-product strategy in which a single antibody is advanced across multiple related indications rather than one. The company emerged from stealth in February 2022 having raised $100 million since inception, added a $90 million round in September 2023, and closed an oversubscribed $125 million Series D in September 2025 to move its lead asset into a registrational programme. Its two named spokes are Vega Therapeutics, whose VGA039 is a first-in-class monoclonal antibody against Protein S developed as a subcutaneous
  therapy for von Willebrand disease and other bleeding disorders, and Electra Therapeutics, which targets SIRP proteins with ELA-026 in secondary hemophagocytic lymphohistiocytosis. VGA039 has received FDA Orphan Drug, Fast Track, Rare Pediatric Disease and Breakthrough Therapy designations; Incyte completed its acquisition of Vega Therapeutics, a wholly owned subsidiary of Star Therapeutics, in July 2026. Star Therapeutics runs no developer program and publishes no product API, developer portal, or API documentation. The only machine-readable surface reachable without credentials is the WordPress REST content API behind star-therapeutics.com, catalogued here.
image: https://star-therapeutics.com/wp-content/uploads/2022/02/Group-6210.png
layout: provider
modified: '2026-08-05'
name: Star Therapeutics
nav: Providers
network: true
overview: 'Star Therapeutics publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Custom Types API, Discovery API, and 6 more. Tagged areas include Company, biotechnology, pharmaceuticals, hematology, and immunology.


  Star Therapeutics'' developer surface includes product news, authentication, and 23 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 30.9
  delta: -0.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 58.2
    developer_ergonomics: 12.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 31.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Star Therapeutics Authentication
  slug: star-therapeutics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Star Therapeutics Domain Security
  slug: star-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: star-therapeutics
tags:
- Company
- biotechnology
- pharmaceuticals
- hematology
- immunology
- rare-disease
- antibody-therapeutics
- clinical-trials
- life-sciences
- content-api
website: https://star-therapeutics.com/
---
