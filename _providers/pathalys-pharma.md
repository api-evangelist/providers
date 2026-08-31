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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-08-30'
api_count: 7
apis:
- description: Pathalys Pharma news, press releases and scientific updates
  name: Pathalys Pharma Posts API
  slug: pathalys-pharma-posts-api
- description: Corporate pages — company, team, science, contact and legal
  name: Pathalys Pharma Pages API
  slug: pathalys-pharma-pages-api
- description: Media library — logos, team photography and press imagery
  name: Pathalys Pharma Media API
  slug: pathalys-pharma-media-api
- description: Post categories and tags taxonomy
  name: Pathalys Pharma Categories API
  slug: pathalys-pharma-categories-api
- description: Comments on posts (collection is empty on this site)
  name: Pathalys Pharma Comments API
  slug: pathalys-pharma-comments-api
- description: Cross-content search over posts and pages
  name: Pathalys Pharma Search API
  slug: pathalys-pharma-search-api
- description: Site index, route/namespace table, content types, taxonomies, statuses and oEmbed
  name: Pathalys Pharma Discovery API
  slug: pathalys-pharma-discovery-api
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://pathalys.com/
- group: other
  title: ''
  type: Team
  url: https://pathalys.com/team/
- group: company
  title: ''
  type: News
  url: https://pathalys.com/news/
- group: other
  title: ''
  type: Science
  url: https://pathalys.com/scientific-updates/
- group: company
  title: ''
  type: Blog
  url: https://pathalys.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://pathalys.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://pathalys.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://pathalys.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pathalys.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pathalys.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pathalys
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/pathalys-pharma_stock/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wordpress.org/rest-api/
- group: other
  title: ''
  type: Overlay
  url: overlays/pathalys-pharma-content-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pathalys-pharma-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pathalys-pharma-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pathalys-pharma-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pathalys-pharma-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pathalys-pharma-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pathalys-pharma-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pathalys-pharma-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pathalys-pharma-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pathalys-pharma-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pathalys-pharma-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: Pathalys Pharma, Inc. is a private, late-stage clinical biopharmaceutical company headquartered at 4000 Center at North Hills Street, Raleigh, North Carolina, in the Research Triangle Park region. It was created with initial funding from Catalys Pacific and the DaVita Venture Group to be a multi-asset biopharmaceutical company focused on the needs of patients with end-stage kidney disease, and it develops advanced therapeutics addressing unmet needs in the management of late-stage chronic kidney disease (CKD). Its lead asset is upacicalcet, a novel non-peptide calcimimetic delivered intravenously by pre-filled syringe at the end of a hemodialysis session for the treatment of secondary hyperparathyroidism (SHPT) in patients with end-stage kidney disease on hemodialysis; it is an investigational product candidate in the United States, subject to FDA review. Pathalys raised $150 million in secured product financing and equity led by Abingworth in January 2023 alongside a development
  collaboration with Launch Therapeutics to run the pivotal PATH Phase 3 program, and closed an oversubscribed $105 million Series B in August 2024 to fund NDA submission and pre-commercialization. Pathalys runs no developer program and publishes no product API; the only machine-readable surface it exposes is the anonymously readable WordPress REST content API behind pathalys.com, which serves the corporate site, the news and scientific-updates stream, and the media library.
image: https://pathalys.com/wp-content/uploads/2021/09/pathalys_logo.svg
layout: provider
modified: '2026-08-26'
name: Pathalys Pharma
nav: Providers
network: true
overview: 'Pathalys Pharma publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 4 more. Tagged areas include Company, pharmaceuticals, biotechnology, nephrology, and chronic-kidney-disease.


  Pathalys Pharma''s developer surface includes product news, engineering blog, support, documentation, authentication, and 20 more developer resources.'
plans:
- name: Pathalys Pharma Plans Pricing
  plan_count: 0
  slug: pathalys-pharma-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Pathalys Pharma Rate Limits
  slug: pathalys-pharma-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 56.4
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 35.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Pathalys Pharma Authentication
  slug: pathalys-pharma-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pathalys Pharma Domain Security
  slug: pathalys-pharma-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: pathalys-pharma
tags:
- Company
- pharmaceuticals
- biotechnology
- nephrology
- chronic-kidney-disease
- clinical-trials
- life-sciences
- content-api
website: https://pathalys.com/
---
