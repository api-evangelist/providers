---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 29.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wugen Agentic Access
  operation_count: 38
  slug: wugen-agentic-access
  summary_line: 38 operations
api_count: 7
apis:
- baseURL: https://alloteratx.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Comments API from Wugen — 2 operation(s) for comments.
  name: Wugen Comments API
  slug: wugen-comments-api
- baseURL: https://alloteratx.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Discovery API from Wugen — 7 operation(s) for discovery.
  name: Wugen Discovery API
  slug: wugen-discovery-api
- baseURL: https://alloteratx.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Media API from Wugen — 2 operation(s) for media.
  name: Wugen Media API
  slug: wugen-media-api
- baseURL: https://alloteratx.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Pages API from Wugen — 2 operation(s) for pages.
  name: Wugen Pages API
  slug: wugen-pages-api
- baseURL: https://alloteratx.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Posts API from Wugen — 2 operation(s) for posts.
  name: Wugen Posts API
  slug: wugen-posts-api
- baseURL: https://alloteratx.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Search API from Wugen — 1 operation(s) for search.
  name: Wugen Search API
  slug: wugen-search-api
- baseURL: https://alloteratx.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Taxonomy API from Wugen — 4 operation(s) for taxonomy.
  name: Wugen Taxonomy API
  slug: wugen-taxonomy-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Allotera (formerly Wugen) Content API (WordPress REST wp/v2) Comments API
  slug: open-wugen-comments-api
- collection_type: open
  name: Wugen Discovery API
  slug: open-wugen-discovery-api
- collection_type: open
  name: Wugen Media API
  slug: open-wugen-media-api
- collection_type: open
  name: Wugen Pages API
  slug: open-wugen-pages-api
- collection_type: open
  name: Wugen Posts API
  slug: open-wugen-posts-api
- collection_type: open
  name: Wugen Search API
  slug: open-wugen-search-api
- collection_type: open
  name: Wugen Taxonomy API
  slug: open-wugen-taxonomy-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/wugen-allotera-content-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wugen-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wugen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wugen-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wugen-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wugen-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wugen-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wugen-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wugen-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/wugen-examples.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wugen-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wugen-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://alloteratx.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://alloteratx.com/feed/
- group: company
  title: ''
  type: FormerWebsite
  url: https://wugen.com/
- group: company
  title: ''
  type: About
  url: https://alloteratx.com/about-us/
- group: other
  title: ''
  type: Technology
  url: https://alloteratx.com/science/
- group: other
  title: ''
  type: Pipeline
  url: https://alloteratx.com/pipeline/
- group: company
  title: ''
  type: News
  url: https://alloteratx.com/press-releases/
- group: other
  title: ''
  type: Publications
  url: https://alloteratx.com/scientific-publications/
- group: other
  title: ''
  type: Team
  url: https://alloteratx.com/leadership/
- group: other
  title: ''
  type: Board
  url: https://alloteratx.com/board-of-directors/
- group: company
  title: ''
  type: Investors
  url: https://alloteratx.com/investors/
- group: company
  title: ''
  type: Partners
  url: https://alloteratx.com/partners/
- group: company
  title: ''
  type: Careers
  url: https://alloteratx.com/career-opportunities/
- group: operate
  title: ''
  type: Support
  url: https://alloteratx.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alloteratx.com/privacy-notice/
- group: other
  title: ''
  type: Accessibility
  url: https://alloteratx.com/accessibility/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wugen
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/wugen_stock/
created: '2026-08-05'
description: Wugen, Inc. is a St. Louis, Missouri clinical-stage cell-therapy company founded in 2018 out of Washington University in St. Louis that develops off-the-shelf, allogeneic CAR-T and memory NK cell therapies for blood cancers, using CRISPR deletion of the T-cell receptor so cells from healthy donors can be given without graft-versus-host disease. In July 2026 the company renamed itself Allotera Therapeutics, Inc. and moved to alloteratx.com, closing a $35M financing that brought total capital raised to roughly $150M on top of its $115M Series C; its lead program, soficabtagene geleucel (sofi-cel, formerly WU-CART-007), is a CD7-targeted allogeneic CAR-T in a global pivotal study for relapsed or refractory T-cell acute lymphoblastic leukemia and T-cell lymphoblastic lymphoma, holds FDA Breakthrough Therapy designation, and was selected for the FDA CMC Development and Readiness Pilot Program. Wugen/Allotera publishes no product or developer API, no OpenAPI, no llms.txt and no agent
  card. The only machine-readable surface either domain exposes is the WordPress REST API (wp/v2), anonymously readable on both the current alloteratx.com site and the retired wugen.com brand domain, which still serves the complete historical press-release and scientific-publication archive as JSON even though its human-facing site is now a single splash page.
image: https://alloteratx.com/wp-content/uploads/2026/06/Asset-1.svg
layout: provider
modified: '2026-08-05'
name: Wugen
nav: Providers
network: true
overview: 'Wugen publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Discovery API, Media API, and 4 more. Tagged areas include Company, Biotechnology, Cell Therapy, Oncology, and Life Sciences.


  Wugen''s developer surface includes authentication, code examples, product news, support, and 27 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 4.5
    contract_quality: 37.7
    developer_ergonomics: 18.5
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 27.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 33.3
      total: 9
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wugen/refs/heads/main/screenshots/wugen-2026-09-02T171015.png
security:
- kind: authentication
  name: Wugen Authentication
  slug: wugen-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Wugen Domain Security
  slug: wugen-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wugen
tags:
- Company
- Biotechnology
- Cell Therapy
- Oncology
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Cart
- CRISPR
- Immunotherapy
- Research
- Content
website: https://alloteratx.com/
---
