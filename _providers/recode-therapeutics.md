---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-08-17'
api_count: 7
apis:
- description: Press releases, publications, corporate pages and site-specific custom post types.
  name: ReCode Therapeutics Content API
  slug: recode-therapeutics-content-api
- description: Route index and namespace metadata the install publishes about itself.
  name: ReCode Therapeutics Discovery API
  slug: recode-therapeutics-discovery-api
- description: oEmbed 1.0 provider endpoint for recodetx.com URLs.
  name: ReCode Therapeutics Embed API
  slug: recode-therapeutics-embed-api
- description: The media library — images, PDFs, posters and decks attached to the site.
  name: ReCode Therapeutics Media API
  slug: recode-therapeutics-media-api
- description: Author records. Personal data — read the x-personal-data annotation before use.
  name: ReCode Therapeutics People API
  slug: recode-therapeutics-people-api
- description: Cross-content search across every REST-exposed post type.
  name: ReCode Therapeutics Search API
  slug: recode-therapeutics-search-api
- description: Categories, tags, and the registered type/status/taxonomy descriptors.
  name: ReCode Therapeutics Taxonomy API
  slug: recode-therapeutics-taxonomy-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ReCode Therapeutics Content API
  slug: open-recode-therapeutics-content-api
- collection_type: open
  name: ReCode Therapeutics Content Discovery API
  slug: open-recode-therapeutics-discovery-api
- collection_type: open
  name: ReCode Therapeutics Content Embed API
  slug: open-recode-therapeutics-embed-api
- collection_type: open
  name: ReCode Therapeutics Content Media API
  slug: open-recode-therapeutics-media-api
- collection_type: open
  name: ReCode Therapeutics Content People API
  slug: open-recode-therapeutics-people-api
- collection_type: open
  name: ReCode Therapeutics Content Search API
  slug: open-recode-therapeutics-search-api
- collection_type: open
  name: ReCode Therapeutics Content Taxonomy API
  slug: open-recode-therapeutics-taxonomy-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/recode-therapeutics-content-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recode-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://recodetx.com/
- group: company
  title: ''
  type: About
  url: https://recodetx.com/about/
- group: other
  title: ''
  type: Science
  url: https://recodetx.com/science/
- group: other
  title: ''
  type: Pipeline
  url: https://recodetx.com/pipeline/
- group: build
  title: ''
  type: ClinicalStudies
  url: https://recodetx.com/clinical-studies/
- group: other
  title: ''
  type: Patients
  url: https://recodetx.com/patients/
- group: company
  title: ''
  type: Partnering
  url: https://recodetx.com/partnering/
- group: other
  title: ''
  type: Leadership
  url: https://recodetx.com/leadership/
- group: company
  title: ''
  type: Careers
  url: https://recodetx.com/careers-culture/
- group: company
  title: ''
  type: News
  url: https://recodetx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://recodetx.com/feed/
- group: other
  title: ''
  type: Events
  url: https://recodetx.com/events/
- group: build
  title: ''
  type: MediaLibrary
  url: https://recodetx.com/media-library/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://recodetx.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://recodetx.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://recodetx.com/cookie-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recode-therapeutics/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ReCodeTx
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/recodetx/
- group: other
  title: ''
  type: Sitemap
  url: https://recodetx.com/sitemap.xml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/recode-therapeutics_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/recode-therapeutics-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/recode-therapeutics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/recode-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/recode-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/recode-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/recode-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/recode-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/recode-therapeutics-data-model.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/recode-therapeutics-json-ld.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: ReCode Therapeutics is a clinical-stage genetic medicines company headquartered in Menlo Park, California with operations in Dallas, Texas, founded in 2015 out of research at UT Southwestern. Its Selective Organ Targeting (SORT) lipid nanoparticle platform is a delivery technology that directs mRNA and gene-correction payloads to organs, tissues and cells beyond the liver — the constraint that has limited genetic medicines to date — with redosing capability. Its lead programmes are RCT1100, an inhaled DNAI1 mRNA therapy for primary ciliary dyskinesia which has reported first-ever proof of activity in PCD patients, and RCT2100, an inhaled CFTR mRNA therapy for cystic fibrosis now in a Phase 2 combination trial with ivacaftor; both hold U.S. FDA Orphan Drug designation. The company collaborates with Intellia Therapeutics on CRISPR-based gene correction for cystic fibrosis, is funded in part by the Cystic Fibrosis Foundation, and has raised over $260 million in Series B financing.
  ReCode Therapeutics runs no developer program and publishes no product API, developer portal or API documentation; the only machine-readable surface reachable without credentials is the WordPress REST content API behind recodetx.com, catalogued here alongside the llms.txt the site publishes.
image: https://recodetx.com/wp-content/uploads/2022/06/ReCode_Logo_Primary_Web.svg
jsonld:
- class_count: 0
  name: Recode Therapeutics Organization Context
  property_count: 0
  slug: recode-therapeutics-organization
layout: provider
modified: '2026-08-05'
name: ReCode Therapeutics
nav: Providers
network: true
overview: 'ReCode Therapeutics publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Content API, Discovery API, Embed API, and 4 more. Tagged areas include Company, genetic-medicines, biotechnology, biopharmaceuticals, and mrna.


  The ReCode Therapeutics catalog on APIs.io includes 1 JSON-LD context.


  ReCode Therapeutics'' developer surface includes product news, authentication, and 31 more developer resources.'
random_paper: 31
score:
  band: thin
  composite: 30.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 57.4
    developer_ergonomics: 12.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 30.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Recode Therapeutics Authentication
  slug: recode-therapeutics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Recode Therapeutics Domain Security
  slug: recode-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: recode-therapeutics
tags:
- Company
- genetic-medicines
- biotechnology
- biopharmaceuticals
- mrna
- gene-correction
- lipid-nanoparticles
- drug-delivery
- rare-disease
- cystic-fibrosis
- primary-ciliary-dyskinesia
- clinical-trials
- life-sciences
- content-api
website: https://recodetx.com/
---
