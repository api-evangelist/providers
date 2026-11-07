---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wugen Agentic Access
  operation_count: 38
  slug: wugen-agentic-access
  summary_line: 38 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Wugen website at alloteratx.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Wugen Website (WordPress REST)
  slug: alloteratx-com-website-wordpress-rest
artifact_total: 7
common:
- group: other
  href: https://artifacts.apis.io/wugen/overlays/wugen-allotera-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wugen-allotera-content-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/wugen/agentic-access/wugen-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wugen-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/wugen/security/wugen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wugen-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/wugen/authentication/wugen-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wugen-authentication.yml
- group: design
  href: https://artifacts.apis.io/wugen/conventions/wugen-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wugen-conventions.yml
- group: design
  href: https://artifacts.apis.io/wugen/conformance/wugen-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wugen-conformance.yml
- group: design
  href: https://artifacts.apis.io/wugen/lifecycle/wugen-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wugen-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wugen/errors/wugen-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wugen-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wugen/data-model/wugen-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wugen-data-model.yml
- group: build
  href: https://artifacts.apis.io/wugen/examples/wugen-examples.yml
  title: ''
  type: Examples
  url: examples/wugen-examples.yml
- group: agent
  href: https://artifacts.apis.io/wugen/well-known/wugen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wugen-well-known.yml
- group: agent
  href: https://artifacts.apis.io/wugen/llms/wugen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wugen-llms.txt
- group: agent
  href: https://artifacts.apis.io/wugen/skills/_index.yml
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
overview: 'Wugen is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Cell Therapy, Oncology, and Life Sciences.


  Wugen''s developer surface includes authentication, code examples, product news, support, and 27 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 7.3
    developer_ergonomics: 23.2
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 16.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wugen/wugen-2026-09-02T171015.png
security:
- kind: authentication
  name: Wugen Authentication
  slug: wugen-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Wugen Domain Security
  slug: wugen-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Read Allotera corporate, pipeline and patient-facing pages
  slug: wugen-read-corporate-pages
- name: Search Allotera content and mirror the full Wugen-era archive
  slug: wugen-search-and-archive
- name: Track Wugen/Allotera press releases and scientific publications
  slug: wugen-track-press-releases
slug: wugen
tags:
- Company
- Biotechnology
- Cell Therapy
- Oncology
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- CAR-T
- CRISPR
- Immunotherapy
- Research
- Content
website: https://alloteratx.com/
---
