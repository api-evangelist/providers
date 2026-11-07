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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lendis Agentic Access
  operation_count: 28
  slug: lendis-agentic-access
  summary_line: 28 operations
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Lendis website at www.lendis.io: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Lendis Website (WordPress REST)
  slug: lendis-io-website-wordpress-rest
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/lendis/skills/lendis-harvest-catalog.md
  title: ''
  type: AgentSkill
  url: skills/lendis-harvest-catalog.md
- group: agent
  href: https://artifacts.apis.io/lendis/mcp/lendis-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lendis-mcp.yml
- group: other
  href: https://artifacts.apis.io/lendis/overlays/lendis-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lendis-content-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/lendis/agentic-access/lendis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lendis-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.lendis.io
- group: company
  title: ''
  type: Blog
  url: https://www.lendis.io/magazin/
- group: operate
  title: ''
  type: Support
  url: https://www.lendis.io/kontakt/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.lendis.io/faq/
- group: start
  title: ''
  type: Login
  url: https://app.lendis.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lendis.io/agb/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lendis.io/datenschutz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lendis-tech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lendis/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@lendis_io
- group: company
  title: ''
  type: Careers
  url: https://www.lendis.io/karriere/
- group: agent
  href: https://artifacts.apis.io/lendis/llms/lendis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lendis-llms.txt
- group: agent
  href: https://artifacts.apis.io/lendis/well-known/lendis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lendis-well-known.yml
- group: build
  href: https://artifacts.apis.io/lendis/packages/lendis-packages.yml
  title: ''
  type: Packages
  url: packages/lendis-packages.yml
- group: design
  href: https://artifacts.apis.io/lendis/conformance/lendis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lendis-conformance.yml
- group: auth
  href: https://artifacts.apis.io/lendis/security/lendis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lendis-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lendis/authentication/lendis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lendis-authentication.yml
- group: design
  href: https://artifacts.apis.io/lendis/conventions/lendis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lendis-conventions.yml
- group: design
  href: https://artifacts.apis.io/lendis/errors/lendis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lendis-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lendis/data-model/lendis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lendis-data-model.yml
- group: design
  href: https://artifacts.apis.io/lendis/lifecycle/lendis-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lendis-lifecycle.yml
created: '2026-07-17'
description: Lendis GmbH is a Berlin-based B2B technology company, founded in 2018, that rents IT hardware to German small and mid-sized businesses under a Device-as-a-Service (DaaS) model. Lendis bundles hardware procurement, configuration and staging, delivery logistics, financing, IT support, lifecycle management and device offboarding into a single monthly rental rate, and manages the whole estate through LendisOS, a web platform covering a self-service shop, order tracking, asset inventory and contract management. The company targets organisations of roughly 50 to 500 employees that want to avoid tying up capital in laptops, smartphones, monitors and accessories. Lendis publishes no public developer program; its commercial platform runs on a private AWS API Gateway at api.lendis.io. Its marketing site does expose a public read-only WordPress REST content API, and Lendis publishes a machine-readable llms.txt for AI agents.
image: https://res.cloudinary.com/lendis-gmbh/images/f_svg,q_auto/fl_sanitize/v1774942862/www.lendis.io/lendis-logo-it/lendis-logo-it.svg
layout: provider
modified: '2026-07-19'
name: Lendis
nav: Providers
network: true
overview: 'Lendis is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Enterprise Software, Device As A Service, IT Hardware, and Leasing.


  Lendis'' developer surface includes engineering blog, support, YouTube channel, authentication, and 21 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 1.7
    developer_ergonomics: 25.6
    discoverability: 64.3
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 20.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lendis/lendis-2026-07-25T224902.png
security:
- kind: authentication
  name: Lendis Authentication
  slug: lendis-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Lendis Domain Security
  slug: lendis-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: Harvest the Lendis site catalog
  slug: lendis-harvest-catalog
- name: Research Lendis content
  slug: lendis-research-content
slug: lendis
tags:
- Company
- Ai Enterprise Software
- Device As A Service
- IT Hardware
- Leasing
- Asset Management
- Workplace Technology
- Procurement
- Germany
- Software-as-a-Service
website: https://www.lendis.io
---
