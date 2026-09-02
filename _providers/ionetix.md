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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-01'
api_count: 9
apis:
- description: News releases, careers postings, conference listings, case studies, presentations and publications published on ionetix.com, served as JSON by the WordPress REST wp/v2 namespace. 66 posts across 10 ca
  name: Ionetix Posts API
  slug: ionetix-posts-api
- description: The ionetix.com marketing and product page tree — Cardiac PET, N-13 Ammonia, N-13 Ammonia Sites, Actinium-225, Astatine-211, Alpha Therapy, PSMA PET, Cyclotron Solutions, Education, Careers, About and
  name: Ionetix Pages API
  slug: ionetix-pages-api
- description: The ionetix.com media library as JSON — 291 attachments including product photography, leadership portraits and the IONETIX ION-12SC Cyclotron System data sheet PDFs, with rendered source URLs and gen
  name: Ionetix Media API
  slug: ionetix-media-api
- description: Categories, tags and taxonomy registrations that classify ionetix.com content — News, Case Studies, Conferences, Presentations, Publications, Education and Careers.
  name: Ionetix Taxonomy API
  slug: ionetix-taxonomy-api
- description: Site-wide search across ionetix.com posts and pages, returning id, title, url, type and subtype for each match with X-WP-Total / X-WP-TotalPages result counts.
  name: Ionetix Search API
  slug: ionetix-search-api
- description: The authors publishing content on ionetix.com, exposed anonymously by the WordPress REST wp/v2 namespace with name, slug, author archive link and avatar URLs.
  name: Ionetix Users API
  slug: ionetix-users-api
- description: Comment threads attached to ionetix.com posts, served by the WordPress REST wp/v2 namespace.
  name: Ionetix Comments API
  slug: ionetix-comments-api
- description: Route, content-type and post-status discovery for the ionetix.com content API — the wp/v2 namespace index, registered post types and registered statuses.
  name: Ionetix Discovery API
  slug: ionetix-discovery-api
- description: oEmbed 1.0 discovery for ionetix.com URLs, returning embeddable representations of posts and pages.
  name: Ionetix oEmbed API
  slug: ionetix-oembed-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://ionetix.com/
- group: company
  title: ''
  type: Blog
  url: https://ionetix.com/news-events/
- group: company
  title: ''
  type: BlogRSS
  url: https://ionetix.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://ionetix.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ionetix.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ionetix-corporation
- group: company
  title: ''
  type: Careers
  url: https://ionetix.com/careers/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ionetix-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ionetix-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ionetix-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ionetix-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ionetix-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ionetix-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/ionetix-examples.yml
- group: build
  title: ''
  type: Packages
  url: packages/ionetix-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ionetix-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ionetix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ionetix-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ionetix-domain-security.yml
created: '2026-08-23'
description: Ionetix (IONETIX Corporation) is a Lansing, Michigan radiopharmaceutical and cyclotron company founded in 2009 out of technology developed at the MIT Plasma Science and Fusion Center. It built the first commercial compact superconducting cyclotron, the ION-12SC, and operates a distributed network of those cyclotrons installed on or near the campuses of hospital PET programs to produce N-13 Ammonia, a short-half-life PET tracer used for cardiac perfusion imaging and the detection of coronary artery disease, sold to providers on a pay-by-the-dose basis. Alongside the cardiac PET network the company runs an alpha isotope manufacturing facility in Lansing built around a 30 MeV cyclotron for commercial-scale production of Actinium-225 and Astatine-211 for targeted alpha therapy, has an approved ANDA for Gallium Ga-68 Gozetotide (PSMA-11), and supply and development partnerships with AlfaRim Medical and Cellectar Biosciences. Ionetix completed a $30M+ financing and go-public transaction
  in April 2026. Ionetix publishes no developer platform, no API documentation, no SDK and no developer portal; the only machine-readable surface on ionetix.com is the WordPress REST API at /wp-json/, whose wp/v2 namespace is anonymously readable and serves the company newsroom, careers postings, conference and case-study archives, product pages, leadership profiles, the media library (including the ION-12SC cyclotron data sheet PDFs) and a site-wide search endpoint as JSON. The WordPress Abilities API namespace (wp-abilities/v1) is registered on the site but returns HTTP 401 to anonymous callers, and no MCP namespace is registered.
image: https://ionetix.com/wp-content/uploads/2021/10/favicon180-1.png
json_schemas:
- name: comment
  property_count: 17
  slug: ionetix-comments.schema
- name: attachment
  property_count: 33
  slug: ionetix-media.schema
- name: page
  property_count: 29
  slug: ionetix-pages.schema
- name: post
  property_count: 31
  slug: ionetix-posts.schema
- name: search-result
  property_count: 5
  slug: ionetix-search.schema
- name: category
  property_count: 9
  slug: ionetix-taxonomy.schema
- name: user
  property_count: 19
  slug: ionetix-users.schema
layout: provider
modified: '2026-08-23'
name: Ionetix
nav: Providers
network: true
overview: 'Ionetix publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 6 more. Tagged areas include Company, Healthcare, Life Sciences, Radiopharmaceuticals, and Nuclear Medicine.


  Ionetix''s developer surface includes engineering blog, support, authentication, code examples, and 16 more developer resources.'
plans:
- name: Ionetix Plans Pricing
  plan_count: 0
  slug: ionetix-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Ionetix Rate Limits
  slug: ionetix-rate-limits
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 21.1
    developer_ergonomics: 20.8
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 20.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Ionetix Authentication
  slug: ionetix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ionetix Domain Security
  slug: ionetix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ionetix
tags:
- Company
- Healthcare
- Life Sciences
- Radiopharmaceuticals
- Nuclear Medicine
- Medical Imaging
- Cardiology
- Oncology
- Isotopes
- Manufacturing
- Content
website: https://ionetix.com/
---
