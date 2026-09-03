---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-03'
api_count: 7
apis:
- baseURL: https://dalcorpharma.com/wp-json
  baseurl_source: declared
  description: Post categories
  name: DalCor Pharmaceuticals Categories API
  slug: dalcor-pharmaceuticals-categories-api
- baseURL: https://dalcorpharma.com/wp-json
  baseurl_source: declared
  description: Comments on posts (collection is empty on this site)
  name: DalCor Pharmaceuticals Comments API
  slug: dalcor-pharmaceuticals-comments-api
- baseURL: https://dalcorpharma.com/wp-json
  baseurl_source: declared
  description: Site index, namespace route index, content types, taxonomies and statuses
  name: DalCor Pharmaceuticals Discovery API
  slug: dalcor-pharmaceuticals-discovery-api
- baseURL: https://dalcorpharma.com/wp-json
  baseurl_source: declared
  description: Media library items (logos, poster PDFs/JPEGs, trial imagery)
  name: DalCor Pharmaceuticals Media API
  slug: dalcor-pharmaceuticals-media-api
- baseURL: https://dalcorpharma.com/wp-json
  baseurl_source: declared
  description: Corporate, science and clinical-trial pages
  name: DalCor Pharmaceuticals Pages API
  slug: dalcor-pharmaceuticals-pages-api
- baseURL: https://dalcorpharma.com/wp-json
  baseurl_source: declared
  description: DalCor press releases and corporate news
  name: DalCor Pharmaceuticals Posts API
  slug: dalcor-pharmaceuticals-posts-api
- baseURL: https://dalcorpharma.com/wp-json
  baseurl_source: declared
  description: Cross-content search
  name: DalCor Pharmaceuticals Search API
  slug: dalcor-pharmaceuticals-search-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DalCor Pharmaceuticals Content API (WordPress REST API) Categories API
  slug: open-dalcor-pharmaceuticals-categories-api
- collection_type: open
  name: DalCor Pharmaceuticals Content API (WordPress REST API) Comments API
  slug: open-dalcor-pharmaceuticals-comments-api
- collection_type: open
  name: DalCor Pharmaceuticals Content API (WordPress REST API) Discovery API
  slug: open-dalcor-pharmaceuticals-discovery-api
- collection_type: open
  name: DalCor Pharmaceuticals Content API (WordPress REST API) Media API
  slug: open-dalcor-pharmaceuticals-media-api
- collection_type: open
  name: DalCor Pharmaceuticals Content API (WordPress REST API) Pages API
  slug: open-dalcor-pharmaceuticals-pages-api
- collection_type: open
  name: DalCor Pharmaceuticals Content API (WordPress REST API) Posts API
  slug: open-dalcor-pharmaceuticals-posts-api
- collection_type: open
  name: DalCor Pharmaceuticals Content API (WordPress REST API) Search API
  slug: open-dalcor-pharmaceuticals-search-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/dalcor-pharmaceuticals-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://dalcorpharma.com/
- group: company
  title: ''
  type: About
  url: https://dalcorpharma.com/about/
- group: other
  title: ''
  type: Management
  url: https://dalcorpharma.com/about/management/
- group: other
  title: ''
  type: BoardOfDirectors
  url: https://dalcorpharma.com/about/board-of-directors/
- group: company
  title: ''
  type: Partners
  url: https://dalcorpharma.com/about/partners/
- group: other
  title: ''
  type: Science
  url: https://dalcorpharma.com/science/cardiovascular-diseases/
- group: other
  title: ''
  type: Publications
  url: https://dalcorpharma.com/science/publications/
- group: operate
  title: ''
  type: PressReleases
  url: https://dalcorpharma.com/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://dalcorpharma.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://dalcorpharma.com/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://dalcorpharma.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dalcorpharma.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dalcor-pharmaceuticals/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/dalcor-pharmaceuticals_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/dalcor-pharmaceuticals-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dalcor-pharmaceuticals-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dalcor-pharmaceuticals-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dalcor-pharmaceuticals-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dalcor-pharmaceuticals-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dalcor-pharmaceuticals-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dalcor-pharmaceuticals-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dalcor-pharmaceuticals-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dalcor-pharmaceuticals-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: DalCor Pharmaceuticals is a clinical-stage biopharmaceutical company founded in 2015 and headquartered in Montreal, Quebec, with offices in Zug, Switzerland, Leatherhead in the United Kingdom, and Sarasota, Florida. It is developing dalcetrapib, positioned as the first pharmacogenetic precision medicine in cardiovascular disease, targeted specifically at patients carrying the AA genotype at the rs1967309 variant of the ADCY9 gene — a genotype present in up to 20% of the general population and in more than 40% of populations of African ancestry. DalCor holds the worldwide exclusive license to develop, manufacture and commercialise dalcetrapib together with rights to the companion genetic marker. The compound is being evaluated in Dal-GenE-2 (DAL-302), a Phase 3 double-blind randomized placebo-controlled cardiovascular outcomes confirmatory trial in 2,000 post-acute-coronary-syndrome patients with the ADCY9 AA genotype, coordinated by the Montreal Health Innovations Coordinating
  Centre and following the dal-GenE (DAL-301) trial, which showed a 21% relative risk reduction in fatal and non-fatal myocardial infarction across 6,149 patients in 34 countries. DalCor runs no developer program and publishes no product API; the only machine-readable surface it exposes is the anonymously readable WordPress REST content API behind dalcorpharma.com, which serves the bilingual English/French corporate site.
image: https://dalcorpharma.com/kicmeefo/2023/09/dalcor-logo.png
layout: provider
modified: '2026-08-04'
name: DalCor Pharmaceuticals
nav: Providers
network: true
overview: 'DalCor Pharmaceuticals publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Comments API, Discovery API, and 4 more. Tagged areas include Company, Pharmaceuticals, Biotechnology, Cardiovascular, and Precision Medicine.


  DalCor Pharmaceuticals'' developer surface includes support, authentication, and 23 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 13.5
    developer_ergonomics: 18.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 19.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dalcor-pharmaceuticals/refs/heads/main/screenshots/dalcor-pharmaceuticals-2026-08-07T164031.png
security:
- kind: authentication
  name: Dalcor Pharmaceuticals Authentication
  slug: dalcor-pharmaceuticals-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dalcor Pharmaceuticals Domain Security
  slug: dalcor-pharmaceuticals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dalcor-pharmaceuticals
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Cardiovascular
- Precision Medicine
- Pharmacogenomics
- Clinical Trials
- Life Sciences
- content-api
website: https://dalcorpharma.com/
---
