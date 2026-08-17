---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-17'
api_count: 12
apis:
- description: Post categories.
  name: EDDA Technology categories API
  slug: edda-categories-api
- description: Approved comments.
  name: EDDA Technology comments API
  slug: edda-comments-api
- description: The embed API from EDDA Technology — 1 operation(s) for embed.
  name: EDDA Technology embed API
  slug: edda-embed-api
- description: Images, manuals and video assets.
  name: EDDA Technology media API
  slug: edda-media-api
- description: Product, company and event pages.
  name: EDDA Technology pages API
  slug: edda-pages-api
- description: Press releases and news announcements.
  name: EDDA Technology posts API
  slug: edda-posts-api
- description: Cross-content search.
  name: EDDA Technology search API
  slug: edda-search-api
- description: Post statuses.
  name: EDDA Technology statuses API
  slug: edda-statuses-api
- description: Post tags.
  name: EDDA Technology tags API
  slug: edda-tags-api
- description: Registered taxonomies.
  name: EDDA Technology taxonomies API
  slug: edda-taxonomies-api
- description: Registered content types.
  name: EDDA Technology types API
  slug: edda-types-api
- description: Public post authors.
  name: EDDA Technology users API
  slug: edda-users-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EDDA Technology WordPress REST categories API
  slug: open-edda-categories-api
- collection_type: open
  name: EDDA Technology WordPress REST categories comments API
  slug: open-edda-comments-api
- collection_type: open
  name: EDDA Technology WordPress REST categories embed API
  slug: open-edda-embed-api
- collection_type: open
  name: EDDA Technology WordPress REST categories media API
  slug: open-edda-media-api
- collection_type: open
  name: EDDA Technology WordPress REST categories pages API
  slug: open-edda-pages-api
- collection_type: open
  name: EDDA Technology WordPress REST categories posts API
  slug: open-edda-posts-api
- collection_type: open
  name: EDDA Technology WordPress REST categories search API
  slug: open-edda-search-api
- collection_type: open
  name: EDDA Technology WordPress REST categories statuses API
  slug: open-edda-statuses-api
- collection_type: open
  name: EDDA Technology WordPress REST categories tags API
  slug: open-edda-tags-api
- collection_type: open
  name: EDDA Technology WordPress REST categories taxonomies API
  slug: open-edda-taxonomies-api
- collection_type: open
  name: EDDA Technology WordPress REST categories types API
  slug: open-edda-types-api
- collection_type: open
  name: EDDA Technology WordPress REST categories users API
  slug: open-edda-users-api
- collection_type: open
  name: API Collection
  slug: open-edda-wordpress-rest-discovery
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/edda-wordpress-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eddatech.com/
- group: company
  title: ''
  type: About
  url: https://www.eddatech.com/about/
- group: other
  title: ''
  type: Products
  url: https://www.eddatech.com/products/
- group: company
  title: ''
  type: Blog
  url: https://www.eddatech.com/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.eddatech.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.eddatech.com/contact-us/
- group: other
  title: ''
  type: Events
  url: https://www.eddatech.com/events/
- group: company
  title: ''
  type: Careers
  url: https://www.eddatech.com/about/careers/
- group: other
  title: ''
  type: Team
  url: https://www.eddatech.com/about/management-team/
- group: other
  title: ''
  type: Publications
  url: https://www.eddatech.com/talks-publications/
- group: auth
  title: ''
  type: Authentication
  url: authentication/edda-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/edda-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/edda-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/edda-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/edda-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/edda-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/edda-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/edda-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/edda-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: EDDA Technology, Inc. is a Princeton, New Jersey medical imaging software company behind the IQQA platform for computer-assisted radiology and surgery. IQQA delivers 3D quantitative image analysis, automated segmentation and volumetric measurement over CT and MR studies, supporting pre-surgical planning and simulation, intra-operative guidance and monitoring, post-operative follow-up evaluation, and clinical training across liver, lung, kidney and interventional oncology. Products include IQQA-BodyImaging, IQQA-Guide, IQQA-Chest, IQQA-Liver, IQQA-Liver Function, IQQA-eQMR and the IQQA-eFusion edge-AI surgical navigation system. The company is FDA cleared and CE marked under EU MDR 2017/745, and raised a US$150 million round led by SoftBank Vision Fund 2 with OrbiMed participation in April 2021. EDDA publishes no developer API for IQQA — it is regulated medical device software deployed on-premises in hospitals — so the only public API surface catalogued here is the WordPress
  REST API serving eddatech.com content.
image: https://www.eddatech.com/wp-content/uploads/2019/10/cropped-EDDA-Technology-Icon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: edda-mcp.yml
  slug: edda-mcpyml
modified: '2026-07-20'
name: EDDA Technology
nav: Providers
network: true
overview: 'EDDA Technology publishes 12 APIs on the [APIs.io](https://apis.io/) network, including categories API, comments API, embed API, and 9 more. Tagged areas include Company, Health Tech, Medical Imaging, Radiology, and Surgery.


  EDDA Technology''s developer surface includes engineering blog, support, authentication, and 19 more developer resources.'
random_paper: 100
score:
  band: emerging
  composite: 18.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 15.7
    developer_ergonomics: 21.2
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 18.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edda/refs/heads/main/screenshots/edda-2026-07-25T212816.png
security:
- kind: authentication
  name: Edda Authentication
  slug: edda-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Edda Domain Security
  slug: edda-domain-security
  summary_line: TLSv1.2
slug: edda
tags:
- Company
- Health Tech
- Medical Imaging
- Radiology
- Surgery
- Oncology
- Artificial Intelligence
- Medical Devices
- Healthcare
- Clinical Software
website: https://www.eddatech.com/
---
