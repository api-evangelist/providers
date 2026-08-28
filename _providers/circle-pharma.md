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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'The anonymously readable WordPress REST API behind circlepharma.com. It exposes Circle Pharma press releases, publications and in-the-news items (posts), site pages, the media library, the leadership '
  name: Circle Pharma Content API
  slug: circle-pharma-content-api
artifact_total: 4
collections:
- collection_type: open
  name: Circle Pharma Content API (WordPress REST API)
  slug: open-circle-pharma-content
common:
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
overview: 'Circle Pharma publishes 1 API on the [APIs.io](https://apis.io/) network: Content API. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Drug Discovery.


  Circle Pharma''s developer surface includes engineering blog, support, authentication, and 22 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 32.9
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 55.1
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 32.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
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
