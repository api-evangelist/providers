---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-03'
api_count: 9
apis:
- baseURL: https://leafforlife.com/wp-json
  baseurl_source: declared
  description: 'The page collection behind leafforlife.com — 8 published pages covering the mission, the science, leadership, the advisory board and contact. Anonymously readable. Verified 2026-08-25: content.rendere'
  name: LEAF4Life Content Pages API
  slug: leaf4life-pages-api
- baseURL: https://leafforlife.com/wp-json
  baseurl_source: declared
  description: The WordPress media library behind leafforlife.com — 59 image attachments (43 PNG, 16 JPEG) spanning September 2020 to July 2026, including the brand marks, leadership headshots and the figure artwork
  name: LEAF4Life Media API
  slug: leaf4life-media-api
- baseURL: https://leafforlife.com/wp-json
  baseurl_source: declared
  description: Category and tag terms. Registered and anonymously reachable but effectively unused — one category (the WordPress default `uncategorized`) and 21 tags, every one with an item count of zero, and the ta
  name: LEAF4Life Taxonomy API
  slug: leaf4life-taxonomy-api
- baseURL: https://leafforlife.com/wp-json
  baseurl_source: declared
  description: The self-describing routes of the deployment — registered post types, taxonomies and post statuses, plus the route index at the server root that publishes name, description, namespaces, all 150 routes
  name: LEAF4Life API Discovery
  slug: leaf4life-discovery-api
- baseURL: https://leafforlife.com/wp-json
  baseurl_source: declared
  description: Cross-type site search returning lightweight result stubs. Live and correct, but it returns zero for every site term tried — including with subtype=page — because WordPress indexes post_content and th
  name: LEAF4Life Search API
  slug: leaf4life-search-api
- baseURL: https://leafforlife.com/wp-json
  baseurl_source: declared
  description: Published authors. One entry — a shared editorial account, `leaf4l` — exposing only id, name, slug, link, description and avatar URLs anonymously. No personal names, e-mail addresses or roles are disc
  name: LEAF4Life Authors API
  slug: leaf4life-users-api
- baseURL: https://leafforlife.com/wp-json
  baseurl_source: declared
  description: Post and comment collections. Registered and anonymously reachable, both empty — LEAF4Life publishes no news archive, press-release feed or blog through WordPress, so the /feed/ RSS endpoint the theme
  name: LEAF4Life Posts and Comments API
  slug: leaf4life-posts-api
- baseURL: https://leafforlife.com/wp-json
  baseurl_source: declared
  description: oEmbed 1.0 provider endpoint for URLs on leafforlife.com. Verified anonymously against the site root — provider_name "LEAF4life". This is the only formally standardised interface the deployment implem
  name: LEAF4Life oEmbed API
  slug: leaf4life-oembed-api
- baseURL: https://leafforlife.com/wp-json
  baseurl_source: declared
  description: Comment collection — registered, zero items.
  name: LEAF4Life Comments API
  slug: leaf4life-comments-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://leafforlife.com/
- group: company
  title: ''
  type: About
  url: https://leafforlife.com/our-science/
- group: other
  title: ''
  type: Leadership
  url: https://leafforlife.com/management-team/
- group: other
  title: ''
  type: AdvisoryBoard
  url: https://leafforlife.com/advisory-board/
- group: operate
  title: ''
  type: Contact
  url: https://leafforlife.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leaf4life-inc
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/leaf4life/
- group: other
  title: ''
  type: Overlay
  url: overlays/leaf4life-content-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leaf4life-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leaf4life-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leaf4life-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leaf4life-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leaf4life-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leaf4life-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leaf4life-domain-security.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leaf4life-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/leaf4life-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leaf4life-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-25'
description: LEAF4Life Inc. is a privately held, clinical-stage biopharmaceutical company headquartered in Woburn, Massachusetts, founded in 2018 by Dr. Clet Niyikiza to develop transformative therapies for hypoxia — insufficient oxygen at the tissue and cellular level — which the company describes as implicated in the world's ten leading causes of death and more than 30 million deaths a year. Its lead asset, KizaVie™ (LEAF-4L6715), is a proprietary liposomal formulation of transcrocetin, a naturally occurring carotenoid from saffron and cape jasmine, designed to enhance oxygen diffusion in plasma and interstitium, restore microcirculatory oxygen delivery and repair hypoxia-driven microvascular and tissue damage, thereby improving the effectiveness of standard-of-care treatment. KizaVie™ is in three Phase 3 registrational studies in Europe — acute respiratory distress syndrome (ARDS), glioblastoma and sarcoma — and has received Compassionate Use Authorization in France for ARDS. The company
  also describes application to shock and trauma, cardiovascular disease, neurodegenerative disorders and aging. LEAF4Life runs no developer program and publishes no product API, developer portal, API reference, SDK or OpenAPI definition. The only machine-readable surface reachable without credentials is the WordPress REST content API behind leafforlife.com, catalogued here, and even that returns page identity and media only — every page body is empty over the API because the site is assembled by a page builder.
image: https://leafforlife.com/wp-content/uploads/2025/11/LEAF4Life_logo_cropped_final.png
layout: provider
modified: '2026-08-25'
name: LEAF4Life
nav: Providers
network: true
overview: 'LEAF4Life publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Content Pages API, Media API, Taxonomy API, and 6 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Clinical Trials, and Oncology.


  LEAF4Life''s developer surface includes authentication and 18 more developer resources.'
plans:
- name: Leaf4Life Plans Pricing
  plan_count: 0
  slug: leaf4life-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Leaf4Life Rate Limits
  slug: leaf4life-rate-limits
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 52.4
    developer_ergonomics: 13.7
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 24.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leaf4life/refs/heads/main/screenshots/leaf4life-2026-09-02T150230.png
security:
- kind: authentication
  name: Leaf4Life Authentication
  slug: leaf4life-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Leaf4Life Domain Security
  slug: leaf4life-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: leaf4life
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Clinical Trials
- Oncology
- Critical Care
- Drug Development
- Life Sciences
- Rare Disease
- content-api
website: https://leafforlife.com/
---
