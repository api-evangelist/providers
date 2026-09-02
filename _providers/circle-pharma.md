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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
api_count: 10
apis:
- description: Post categories
  name: Circle Pharma Categories API
  slug: circle-pharma-categories-api
- description: Comments on posts
  name: Circle Pharma Comments API
  slug: circle-pharma-comments-api
- description: Route index, content types, taxonomies and statuses
  name: Circle Pharma Discovery API
  slug: circle-pharma-discovery-api
- description: Upcoming and past events
  name: Circle Pharma Events API
  slug: circle-pharma-events-api
- description: Media library items
  name: Circle Pharma Media API
  slug: circle-pharma-media-api
- description: Static site pages (pipeline, science, clinical trials)
  name: Circle Pharma Pages API
  slug: circle-pharma-pages-api
- description: Press releases, publications and in-the-news items
  name: Circle Pharma Posts API
  slug: circle-pharma-posts-api
- description: Cross-content search
  name: Circle Pharma Search API
  slug: circle-pharma-search-api
- description: Post tags
  name: Circle Pharma Tags API
  slug: circle-pharma-tags-api
- description: Leadership, board and team member records
  name: Circle Pharma Team API
  slug: circle-pharma-team-api
artifact_total: 13
collections:
- collection_type: open
  name: Circle Pharma Content API (WordPress REST API)
  slug: open-circle-pharma-content
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/circle-pharma-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://circlepharma.com/
- group: company
  title: ''
  type: About
  url: https://circlepharma.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://circlepharma.com/whats-new
- group: company
  title: ''
  type: BlogRSS
  url: https://circlepharma.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://circlepharma.com/press-releases
- group: other
  title: ''
  type: Publications
  url: https://circlepharma.com/publications
- group: other
  title: ''
  type: Events
  url: https://circlepharma.com/upcoming-events
- group: company
  title: ''
  type: Careers
  url: https://circlepharma.com/work-with-us
- group: operate
  title: ''
  type: Contact
  url: https://circlepharma.com/contact-us
- group: company
  title: ''
  type: Investors
  url: https://circlepharma.com/investors
- group: operate
  title: ''
  type: Support
  url: https://circlepharma.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://circlepharma.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://circlepharma.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/circle-pharma-inc-/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/circle-pharma_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/circle-pharma-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/circle-pharma-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/circle-pharma-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/circle-pharma-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/circle-pharma-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/circle-pharma-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/circle-pharma-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/circle-pharma-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/circle-pharma-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: 'Circle Pharma is a clinical-stage biopharmaceutical company in South San Francisco, California, developing cell-permeable, orally bioavailable macrocycle therapies for cancer. Founded in 2013 by Matthew P. Jacobson and Scott Lokey out of work on predicting synthetic macrocycle cell permeability, the company applies its proprietary MXMO structure-based design platform to protein-protein interactions that conventional small molecules cannot reach. Its pipeline targets cyclins, the regulators of the cell cycle that drive many cancers: lead program CID-078, a first-in-class oral cyclin A/B RxL inhibitor, is in Phase 1 for advanced solid tumors, followed by a preclinical cyclin D1 RxL inhibitor and undisclosed cyclin programs partnered with Boehringer Ingelheim. Circle Pharma closed a $90M Series D led by The Column Group in 2024 and has an agreement with Eli Lilly to use Lilly TuneLab to strengthen the AI/ML side of the MXMO platform. Circle Pharma runs no developer program and
  publishes no product API; the only machine-readable surface it exposes is the anonymously readable WordPress REST content API behind circlepharma.com.'
image: https://circlepharma.com/wp-content/uploads/2024/01/Asset-2@2x.png
layout: provider
modified: '2026-08-01'
name: Circle Pharma
nav: Providers
network: true
overview: 'Circle Pharma publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Comments API, Discovery API, and 7 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Drug Discovery.


  Circle Pharma''s developer surface includes engineering blog, support, authentication, and 23 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -9.9
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 13.3
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/circle-pharma/refs/heads/main/screenshots/circle-pharma-2026-08-07T163423.png
security:
- kind: authentication
  name: Circle Pharma Authentication
  slug: circle-pharma-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Circle Pharma Domain Security
  slug: circle-pharma-domain-security
  summary_line: TLSv1.3 · DMARC
slug: circle-pharma
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Drug Discovery
- Macrocycles
- Clinical Trials
- Life Sciences
- content-api
website: https://circlepharma.com/
---
