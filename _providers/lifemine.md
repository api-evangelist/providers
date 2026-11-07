---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lifemine Agentic Access
  operation_count: 12
  slug: lifemine-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the LifeMine website at lifeminetx.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: LifeMine Website (WordPress REST)
  slug: lifeminetx-com-website-wordpress-rest
- baseURL: https://boards-api.greenhouse.io/v1/boards/lifeminetx
  baseurl_source: declared
  description: Board-level metadata.
  name: LifeMine Board API
  slug: lifemine-board-api
- baseURL: https://boards-api.greenhouse.io/v1/boards/lifeminetx
  baseurl_source: declared
  description: Department taxonomy.
  name: LifeMine Departments API
  slug: lifemine-departments-api
- baseURL: https://boards-api.greenhouse.io/v1/boards/lifeminetx
  baseurl_source: declared
  description: Greenhouse education reference data used by application forms.
  name: LifeMine Education API
  slug: lifemine-education-api
- baseURL: https://boards-api.greenhouse.io/v1/boards/lifeminetx
  baseurl_source: declared
  description: Open roles.
  name: LifeMine Jobs API
  slug: lifemine-jobs-api
- baseURL: https://boards-api.greenhouse.io/v1/boards/lifeminetx
  baseurl_source: declared
  description: Office / location taxonomy.
  name: LifeMine Offices API
  slug: lifemine-offices-api
- baseURL: https://boards-api.greenhouse.io/v1/boards/lifeminetx
  baseurl_source: declared
  description: Board sections (empty on this board).
  name: LifeMine Sections API
  slug: lifemine-sections-api
artifact_total: 30
collections:
- collection_type: open
  name: LifeMine Careers API (Greenhouse Job ) Board API
  slug: open-lifemine-board-api
- collection_type: open
  name: LifeMine Careers API (Greenhouse Job Board) Departments API
  slug: open-lifemine-departments-api
- collection_type: open
  name: LifeMine Careers API (Greenhouse Job Board) Education API
  slug: open-lifemine-education-api
- collection_type: open
  name: LifeMine Careers API (Greenhouse Job Board) Jobs API
  slug: open-lifemine-jobs-api
- collection_type: open
  name: LifeMine Careers API (Greenhouse Job Board) Offices API
  slug: open-lifemine-offices-api
- collection_type: open
  name: LifeMine Careers API (Greenhouse Job Board) Sections API
  slug: open-lifemine-sections-api
common:
- group: operate
  title: ''
  type: Contact
  url: https://lifeminetx.com/contact/
- group: other
  href: https://artifacts.apis.io/lifemine/overlays/lifemine-careers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lifemine-careers-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://lifeminetx.com/
- group: company
  title: ''
  type: About
  url: https://lifeminetx.com/about/
- group: other
  title: ''
  type: Science
  url: https://lifeminetx.com/science/
- group: other
  title: ''
  type: Pipeline
  url: https://lifeminetx.com/pipeline/
- group: company
  title: ''
  type: Blog
  url: https://lifeminetx.com/blog/
- group: company
  title: ''
  type: News
  url: https://lifeminetx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://lifeminetx.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://lifeminetx.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://lifeminetx.com/culture-careers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lifeminetx.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lifemine-therapeutics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/lifemine_stock/
- group: auth
  href: https://artifacts.apis.io/lifemine/authentication/lifemine-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lifemine-authentication.yml
- group: design
  href: https://artifacts.apis.io/lifemine/conventions/lifemine-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lifemine-conventions.yml
- group: design
  href: https://artifacts.apis.io/lifemine/errors/lifemine-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lifemine-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lifemine/lifecycle/lifemine-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lifemine-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/lifemine/conformance/lifemine-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lifemine-conformance.yml
- group: design
  href: https://artifacts.apis.io/lifemine/data-model/lifemine-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lifemine-data-model.yml
- group: agent
  href: https://artifacts.apis.io/lifemine/well-known/lifemine-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lifemine-well-known.yml
- group: auth
  href: https://artifacts.apis.io/lifemine/security/lifemine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lifemine-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/lifemine/agentic-access/lifemine-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lifemine-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/lifemine/mcp/lifemine-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lifemine-mcp.yml
- group: build
  href: https://artifacts.apis.io/lifemine/mcp/lifemine-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lifemine-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/lifemine/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/lifemine/llms/lifemine-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lifemine-llms.txt
created: '2026-08-04'
description: 'LifeMine (LifeMine Therapeutics) is a clinical-stage biopharmaceutical company pioneering Top-Down Drug Discovery, mining the fungal biosphere for genetically encoded small molecules and developing them into precision medicines for immune-mediated disease and organ transplant rejection. Founded in 2017 by Gregory Verdine, Richard Klausner and WeiQing Zhou, the company is headquartered in Watertown, Massachusetts with sites in Gloucester, Massachusetts and Basel, Switzerland, and has raised more than $320 million. Its lead programme, LIFE-001, is a structurally novel calcineurin inhibitor that entered a first-in-human Phase 1 trial in April 2025. LifeMine publishes no developer portal and no API documentation, and its drug-discovery platform is not exposed publicly. It does, however, operate two genuinely public, anonymous, machine-readable read APIs as byproducts of the platforms it runs: a WordPress REST API serving its news, pages, media and a structured leadership/board
  record set, and a Greenhouse job board API serving its open roles, departments and offices.'
examples:
- key_count: 2
  name: Lifemine Careers Jobs Example
  slug: lifemine-careers-jobs-example
- key_count: 1
  name: Lifemine Careers Offices Example
  slug: lifemine-careers-offices-example
- key_count: 3
  name: Lifemine Error 401 Example
  slug: lifemine-error-401-example
image: https://lifeminetx.com/wp-content/uploads/2024/05/cropped-Favicon-B.png
json_schemas:
- name: Lifemine Categories
  property_count: 0
  slug: lifemine-categories
- name: Lifemine Media
  property_count: 0
  slug: lifemine-media
- name: Lifemine Pages
  property_count: 0
  slug: lifemine-pages
- name: Lifemine Posts
  property_count: 0
  slug: lifemine-posts
- name: Lifemine Tags
  property_count: 0
  slug: lifemine-tags
- name: Lifemine Team
  property_count: 0
  slug: lifemine-team
- name: Lifemine Team_Categories
  property_count: 0
  slug: lifemine-team_categories
layout: provider
modified: '2026-08-04'
name: LifeMine
nav: Providers
network: true
overview: 'LifeMine publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Board API, Departments API, Education API, and 4 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Life Sciences.


  The LifeMine catalog on APIs.io includes 1 Spectral governance ruleset.


  LifeMine''s developer surface includes engineering blog, product news, support, authentication, and 23 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: LifeMine API Rules
  rule_count: 57
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 5
  slug: lifemine-rules
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 54.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 28.6
    contract_governance: 18.2
    contract_quality: 21.7
    developer_ergonomics: 25.6
    discoverability: 58.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 26.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/lifemine/lifemine-2026-08-07T171642.png
security:
- kind: authentication
  name: Lifemine Authentication
  slug: lifemine-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Lifemine Domain Security
  slug: lifemine-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Map LifeMine leadership and board
  slug: lifemine-map-leadership
- name: Monitor LifeMine open roles
  slug: lifemine-monitor-open-roles
- name: Track LifeMine company news
  slug: lifemine-track-company-news
slug: lifemine
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Life Sciences
- Clinical Trials
- Genomics
- Content
- Careers
- WordPress
website: https://lifeminetx.com/
---
