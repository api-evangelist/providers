---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Federal Accounting Standards Advisory Board website at fasab.gov: the route index of the site''s content management system, catalogued as one site surface'
  name: Federal Accounting Standards Advisory Board Website (WordPress REST)
  slug: fasab-gov-website-wordpress-rest
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/security/federal-accounting-standards-advisory-board-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/federal-accounting-standards-advisory-board-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-accounting-standards-advisory-board
- group: company
  title: ''
  type: Website
  url: https://fasab.gov/
- group: docs
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/openapi/_original/federal-accounting-standards-advisory-board-wp-content-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/federal-accounting-standards-advisory-board-wp-content-openapi.yml
- group: auth
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/authentication/federal-accounting-standards-advisory-board-authentication.yml
  title: ''
  type: Authentication
  url: authentication/federal-accounting-standards-advisory-board-authentication.yml
- group: design
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/conventions/federal-accounting-standards-advisory-board-conventions.yml
  title: ''
  type: Conventions
  url: conventions/federal-accounting-standards-advisory-board-conventions.yml
- group: design
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/errors/federal-accounting-standards-advisory-board-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/federal-accounting-standards-advisory-board-problem-types.yml
- group: design
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/lifecycle/federal-accounting-standards-advisory-board-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/federal-accounting-standards-advisory-board-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/conformance/federal-accounting-standards-advisory-board-conformance.yml
  title: ''
  type: Conformance
  url: conformance/federal-accounting-standards-advisory-board-conformance.yml
- group: design
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/data-model/federal-accounting-standards-advisory-board-data-model.yml
  title: ''
  type: DataModel
  url: data-model/federal-accounting-standards-advisory-board-data-model.yml
- group: operate
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/rate-limits/federal-accounting-standards-advisory-board-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/federal-accounting-standards-advisory-board-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/plans/federal-accounting-standards-advisory-board-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/federal-accounting-standards-advisory-board-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/packages/federal-accounting-standards-advisory-board-packages.yml
  title: ''
  type: Packages
  url: packages/federal-accounting-standards-advisory-board-packages.yml
- group: agent
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/mcp/federal-accounting-standards-advisory-board-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/federal-accounting-standards-advisory-board-mcp.yml
- group: agent
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/llms/federal-accounting-standards-advisory-board-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/federal-accounting-standards-advisory-board-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://fasab.gov/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://fasab.gov/feed/
- group: operate
  title: ''
  type: Support
  url: https://fasab.gov/about-fasab/contact-information/
- group: build
  href: https://artifacts.apis.io/federal-accounting-standards-advisory-board/examples/federal-accounting-standards-advisory-board-error-401.json
  title: ''
  type: Examples
  url: examples/federal-accounting-standards-advisory-board-error-401.json
created: '2024-12-25'
description: The Federal Accounting Standards Advisory Board (FASAB) is the U.S. federal advisory body designated to set generally accepted accounting principles for the federal government and its component reporting entities. FASAB issues Statements of Federal Financial Accounting Standards (SFFAS), technical releases, interpretations and staff implementation guidance, consolidates them into the FASAB Handbook, and runs the public due-process cycle of board and ASIC meetings, active projects and exposure drafts open for comment. FASAB publishes no developer program or specification, but fasab.gov runs on WordPress and serves the WordPress REST API anonymously at https://fasab.gov/wp-json/ — a read-only surface over 402 pages, 214 media records, the site taxonomies and search, whose OpenAPI here was derived from that live route index. The authoritative pronouncements remain PDFs on files.fasab.gov.
examples:
- key_count: 3
  name: Federal Accounting Standards Advisory Board Error 401
  slug: federal-accounting-standards-advisory-board-error-401
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-accounting-standards-advisory-board.png
layout: provider
modified: '2026-09-16'
name: Federal Accounting Standards Advisory Board
nav: Providers
network: true
overview: 'Federal Accounting Standards Advisory Board publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Website (WordPress REST). Tagged areas include Accounting, Federal Government, Standards, Financial Reporting, and Government.


  The Federal Accounting Standards Advisory Board catalog on APIs.io includes 1 Spectral governance ruleset.


  Federal Accounting Standards Advisory Board''s developer surface includes authentication, engineering blog, support, code examples, and 16 more developer resources.'
plans:
- name: Federal Accounting Standards Advisory Board Plans Pricing
  plan_count: 0
  slug: federal-accounting-standards-advisory-board-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Federal Accounting Standards Advisory Board Rate Limits
  slug: federal-accounting-standards-advisory-board-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Federal Accounting Standards Advisory Board API Rules
  rule_count: 65
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 4
  slug: federal-accounting-standards-advisory-board-rules
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 30.5
    developer_ergonomics: 25.6
    discoverability: 64.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 22.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/federal-accounting-standards-advisory-board/federal-accounting-standards-advisory-board-2026-06-20T181109.png
security:
- kind: authentication
  name: Federal Accounting Standards Advisory Board Authentication
  slug: federal-accounting-standards-advisory-board-authentication
  summary_line: none/basic · 2 schemes
- kind: domain-security
  name: Federal Accounting Standards Advisory Board Domain Security
  slug: federal-accounting-standards-advisory-board-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Find a FASAB standard or guidance page
  slug: federal-accounting-standards-advisory-board-find-a-standard
- name: Track FASAB board activity and documents for comment
  slug: federal-accounting-standards-advisory-board-track-board-activity
slug: federal-accounting-standards-advisory-board
tags:
- Accounting
- Federal Government
- Standards
- Financial Reporting
- Government
- Regulations
- Content
- Publications
website: https://fasab.gov/
---
