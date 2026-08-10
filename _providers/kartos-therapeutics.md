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
  scored_at: '2026-08-10'
api_count: 7
apis:
- description: Published pages and the site-wide search index.
  name: Kartos Therapeutics Content API
  slug: kartos-therapeutics-content-api
- description: The route index and namespace descriptors the site publishes about itself.
  name: Kartos Therapeutics Discovery API
  slug: kartos-therapeutics-discovery-api
- description: The media library — scientific figures, investor logos and presentation PDFs.
  name: Kartos Therapeutics Media API
  slug: kartos-therapeutics-media-api
- description: The oEmbed 1.0 provider endpoint for kartosthera.com URLs.
  name: Kartos Therapeutics Oembed API
  slug: kartos-therapeutics-oembed-api
- description: The leadership, board and advisor team custom post type.
  name: Kartos Therapeutics People API
  slug: kartos-therapeutics-people-api
- description: The navtemadlin congress presentations and publications custom post type.
  name: Kartos Therapeutics Science API
  slug: kartos-therapeutics-science-api
- description: Registered post types, statuses, taxonomies and terms.
  name: Kartos Therapeutics Taxonomy API
  slug: kartos-therapeutics-taxonomy-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://kartosthera.com/
- group: company
  title: ''
  type: About
  url: https://kartosthera.com/about/
- group: other
  title: ''
  type: Science
  url: https://kartosthera.com/science/
- group: other
  title: ''
  type: Research
  url: https://kartosthera.com/research/
- group: other
  title: ''
  type: Presentations
  url: https://kartosthera.com/presentations/
- group: other
  title: ''
  type: PatientResources
  url: https://kartosthera.com/advocacy/
- group: operate
  title: ''
  type: Contact
  url: https://kartosthera.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://kartosthera.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kartosthera.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kartos-therapeutics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/kartos-therapeutics_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/kartos-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kartos-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kartos-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kartos-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kartos-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kartos-therapeutics-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kartos-therapeutics-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kartos-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kartos-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: Kartos Therapeutics, Inc. is a privately held, clinical-stage biopharmaceutical company headquartered at 275 Shoreline Drive, Redwood City, California, developing navtemadlin (KRT-232), an orally administered, potent and selective small-molecule inhibitor of MDM2. The company was founded in 2016 by Wayne Rothbaum, president of Quogue Capital and co-founder of Acerta Pharma, around an MDM2 inhibitor in-licensed from Amgen. Navtemadlin blocks the MDM2 protein that suppresses p53, restoring p53 function in tumours that retain wild-type TP53 and driving cell-cycle arrest through p21 and apoptosis through pro-apoptotic Bcl-2 family proteins. The clinical programme is centred on myelofibrosis and includes the enrolling global Phase 3 POIESIS trial of navtemadlin added to ruxolitinib (NCT06479135), the Phase 1b/2 KRT-232-109 combination study (NCT04485260), and the completed Phase 3 BOREAS study of navtemadlin versus best available therapy in JAK-inhibitor relapsed or refractory myelofibrosis
  (NCT03662126), with reported activity also in acute myeloid leukaemia and Merkel cell carcinoma. Kartos is led by CEO Jesse McGreivy, MD, with Srdan Verstovsek, MD, PhD as chief medical officer, and is backed by Quogue Capital, OrbiMed Advisors, Amgen, SR One, Fidelity, BlackRock, T. Rowe Price, Invus and Soleus Capital. Kartos Therapeutics runs no developer program and publishes no product API, no developer portal and no API documentation; the only machine-readable surface reachable without credentials is the WordPress REST content API behind kartosthera.com, catalogued here.
image: https://kartosthera.com/wp-content/uploads/2025/10/og_kartos-therapeutics.jpg
layout: provider
modified: '2026-08-04'
name: Kartos Therapeutics
nav: Providers
network: true
overview: 'Kartos Therapeutics publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Content API, Discovery API, Media API, and 4 more. Tagged areas include Company, biotechnology, pharmaceuticals, oncology, and hematology.


  Kartos Therapeutics'' developer surface includes support, authentication, and 19 more developer resources.'
random_paper: 30
score:
  band: emerging
  composite: 19.6
  delta: 0.6
  facets:
    commercial_clarity: 10.5
    contract_quality: 14.0
    developer_ergonomics: 16.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 19.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kartos-therapeutics/refs/heads/main/screenshots/kartos-therapeutics-2026-08-07T171100.png
security:
- kind: authentication
  name: Kartos Therapeutics Authentication
  slug: kartos-therapeutics-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kartos Therapeutics Domain Security
  slug: kartos-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kartos-therapeutics
tags:
- Company
- biotechnology
- pharmaceuticals
- oncology
- hematology
- rare-disease
- precision-medicine
- clinical-trials
- life-sciences
- content-api
website: https://kartosthera.com/
---
