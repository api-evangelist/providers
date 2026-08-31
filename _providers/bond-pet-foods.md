---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The wc/store/v1 API from Bond Pet Foods — 31 operation(s) for wc/store/v1.
  name: Bond Pet Foods Wc/store/v1 API
  slug: bond-pet-foods-wc-store-v1-api
- description: The wp/v2 API from Bond Pet Foods — 134 operation(s) for wp/v2.
  name: Bond Pet Foods Wp/v2 API
  slug: bond-pet-foods-wp-v2-api
artifact_total: 9
asyncapis:
- description: ''
  name: Bond Pet Foods Webhooks
  slug: bond-pet-foods-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bond Pet Foods Store API (WooCommerce Store API) Wc/store/v1 API
  slug: open-bond-pet-foods-wc-store-v1-api
- collection_type: open
  name: API Collection
  slug: open-bond-pet-foods-wp-rest-index-original
- collection_type: open
  name: Bond Pet Foods Content API (WordPress REST API) Wp/v2 API
  slug: open-bond-pet-foods-wp-v2-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/bond-pet-foods-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.bondpets.com/
- group: other
  title: ''
  type: Company
  url: https://www.bondpets.com/our-mission/
- group: other
  title: ''
  type: Team
  url: https://www.bondpets.com/our-team/
- group: other
  title: ''
  type: Products
  url: https://www.bondpets.com/shop/
- group: operate
  title: ''
  type: Support
  url: https://www.bondpets.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://www.bondpets.com/faqs/
- group: company
  title: ''
  type: Blog
  url: https://www.bondpets.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.bondpets.com/feed/
- group: company
  title: ''
  type: Press
  url: https://www.bondpets.com/press/
- group: company
  title: ''
  type: Careers
  url: https://www.bondpets.com/careers/
- group: company
  title: ''
  type: Newsletter
  url: https://www.bondpets.com/newsletter/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bondpets.com/privacy-policy/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/bond-pet-foods-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bond-pet-foods-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bond-pet-foods-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bond-pet-foods-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bond-pet-foods-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bond-pet-foods-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bond-pet-foods-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bond-pet-foods-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-08'
description: Bond Pet Foods is a Boulder, Colorado food-biotechnology company that makes animal proteins for pet food by precision fermentation rather than by farming animals. Its process pairs a chicken DNA sequence with brewer's yeast and runs it through a roughly 48-hour controlled fermentation, after which the protein is harvested, dried and milled into a powder that pet food makers formulate into finished products. The company operates a 15,000 square-foot food lab in central Boulder, is led by founder and CEO Rich Kelleman, markets itself as an "Ally For All Animals", and has announced a $17.5M Series A, an investment from Symrise AG, and development partnerships with Hill's Pet Nutrition and Wilbur-Ellis Nutrition. Bond Pet Foods runs no developer program and publishes no API documentation, but its own site at www.bondpets.com runs on WordPress and WooCommerce and exposes a genuinely public, machine-readable API surface - a WordPress REST API discovery index advertising 970 routes
  across 57 namespaces, and an anonymously readable WooCommerce Store API covering the merchandise catalog, categories and cart.
image: https://www.bondpets.com/wp-content/uploads/2022/09/Bond_SocialShare_1_Home_Mission.jpg
layout: provider
modified: '2026-08-08'
name: Bond Pet Foods
nav: Providers
network: true
overview: 'Bond Pet Foods publishes 2 APIs on the [APIs.io](https://apis.io/) network: Wc/store/v1 API and Wp/v2 API. Tagged areas include Pet Food, Alternative Protein, Precision Fermentation, Food Technology, and Biotechnology.


  The Bond Pet Foods catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bond Pet Foods'' developer surface includes support, FAQ, engineering blog, authentication, and 19 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 64.6
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 29.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Bond Pet Foods Authentication
  slug: bond-pet-foods-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Bond Pet Foods Domain Security
  slug: bond-pet-foods-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bond-pet-foods
tags:
- Pet Food
- Alternative Protein
- Precision Fermentation
- Food Technology
- Biotechnology
- Animal Nutrition
- Sustainability
- E-Commerce
- WooCommerce
- WordPress
website: https://www.bondpets.com/
---
