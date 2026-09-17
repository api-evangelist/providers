---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://fasab.gov/wp-json
  baseurl_source: declared
  description: Public author records for FASAB staff who publish content.
  name: Federal Accounting Standards Advisory Board Authors API
  slug: federal-accounting-standards-advisory-board-authors-api
- baseURL: https://fasab.gov/wp-json
  baseurl_source: declared
  description: Route index, content types, taxonomies, statuses and oEmbed.
  name: Federal Accounting Standards Advisory Board Discovery API
  slug: federal-accounting-standards-advisory-board-discovery-api
- baseURL: https://fasab.gov/wp-json
  baseurl_source: declared
  description: The media library of uploaded files and images.
  name: Federal Accounting Standards Advisory Board Documents API
  slug: federal-accounting-standards-advisory-board-documents-api
- baseURL: https://fasab.gov/wp-json
  baseurl_source: declared
  description: Posts and comments.
  name: Federal Accounting Standards Advisory Board News API
  slug: federal-accounting-standards-advisory-board-news-api
- baseURL: https://fasab.gov/wp-json
  baseurl_source: declared
  description: FASAB site pages — standards and guidance, projects, board meetings, ASIC, training, resources.
  name: Federal Accounting Standards Advisory Board Pages API
  slug: federal-accounting-standards-advisory-board-pages-api
- baseURL: https://fasab.gov/wp-json
  baseurl_source: declared
  description: Cross-type site search.
  name: Federal Accounting Standards Advisory Board Search API
  slug: federal-accounting-standards-advisory-board-search-api
- baseURL: https://fasab.gov/wp-json
  baseurl_source: declared
  description: Categories, tags and the Link Library taxonomies.
  name: Federal Accounting Standards Advisory Board Taxonomy API
  slug: federal-accounting-standards-advisory-board-taxonomy-api
artifact_total: 12
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/security/federal-accounting-standards-advisory-board-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/openapi/_original/federal-accounting-standards-advisory-board-wp-content-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/federal-accounting-standards-advisory-board-wp-content-openapi.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/authentication/federal-accounting-standards-advisory-board-authentication.yml
  title: ''
  type: Authentication
  url: authentication/federal-accounting-standards-advisory-board-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/conventions/federal-accounting-standards-advisory-board-conventions.yml
  title: ''
  type: Conventions
  url: conventions/federal-accounting-standards-advisory-board-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/errors/federal-accounting-standards-advisory-board-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/federal-accounting-standards-advisory-board-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/lifecycle/federal-accounting-standards-advisory-board-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/federal-accounting-standards-advisory-board-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/conformance/federal-accounting-standards-advisory-board-conformance.yml
  title: ''
  type: Conformance
  url: conformance/federal-accounting-standards-advisory-board-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/data-model/federal-accounting-standards-advisory-board-data-model.yml
  title: ''
  type: DataModel
  url: data-model/federal-accounting-standards-advisory-board-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/rate-limits/federal-accounting-standards-advisory-board-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/federal-accounting-standards-advisory-board-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/plans/federal-accounting-standards-advisory-board-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/federal-accounting-standards-advisory-board-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/packages/federal-accounting-standards-advisory-board-packages.yml
  title: ''
  type: Packages
  url: packages/federal-accounting-standards-advisory-board-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/mcp/federal-accounting-standards-advisory-board-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/federal-accounting-standards-advisory-board-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/llms/federal-accounting-standards-advisory-board-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/federal-accounting-standards-advisory-board-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/overlays/federal-accounting-standards-advisory-board-wp-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/federal-accounting-standards-advisory-board-wp-content-overlay.yaml
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
overview: 'Federal Accounting Standards Advisory Board publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authors API, Discovery API, Documents API, and 4 more. Tagged areas include Accounting, Federal-Government, Standards, Financial Reporting, and Government.


  Federal Accounting Standards Advisory Board''s developer surface includes authentication, engineering blog, support, and 17 more developer resources.'
plans:
- name: Federal Accounting Standards Advisory Board Plans Pricing
  plan_count: 0
  slug: federal-accounting-standards-advisory-board-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Federal Accounting Standards Advisory Board Rate Limits
  slug: federal-accounting-standards-advisory-board-rate-limits
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 16.5
    developer_ergonomics: 20.8
    discoverability: 75.9
    operational_transparency: 0.0
  previous_composite: 17.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-accounting-standards-advisory-board/refs/heads/main/screenshots/federal-accounting-standards-advisory-board-2026-06-20T181109.png
security:
- kind: authentication
  name: Federal Accounting Standards Advisory Board Authentication
  slug: federal-accounting-standards-advisory-board-authentication
  summary_line: none/basic · 2 schemes
- kind: domain-security
  name: Federal Accounting Standards Advisory Board Domain Security
  slug: federal-accounting-standards-advisory-board-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: federal-accounting-standards-advisory-board
tags:
- Accounting
- Federal-Government
- Standards
- Financial Reporting
- Government
- Regulations
- Content
- Publications
website: https://fasab.gov/
---
