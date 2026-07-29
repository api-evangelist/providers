---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 81
  human_in_the_loop: 2
  name: Monash Agentic Access
  operation_count: 157
  slug: monash-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: Monash eResearch operates the Cloud Resource Allocation and Management System (CRAMS), which exposes an API portal used to manage research cloud resource allocations. Access is institutional/gated; no
  name: CRAMS API (Cloud Resource Allocation and Management System)
  slug: crams
- description: The altmetric API from Monash University — 1 operation(s) for altmetric.
  name: Monash University altmetric API
  slug: monash-altmetric-api
- description: The articles API from Monash University — 34 operation(s) for articles.
  name: Monash University articles API
  slug: monash-articles-api
- description: The authors API from Monash University — 2 operation(s) for authors.
  name: Monash University authors API
  slug: monash-authors-api
- description: The collections API from Monash University — 21 operation(s) for collections.
  name: Monash University collections API
  slug: monash-collections-api
- description: The institutions API from Monash University — 20 operation(s) for institutions.
  name: Monash University institutions API
  slug: monash-institutions-api
- description: The oauth API from Monash University — 1 operation(s) for oauth.
  name: Monash University oauth API
  slug: monash-oauth-api
- description: The other API from Monash University — 7 operation(s) for other.
  name: Monash University other API
  slug: monash-other-api
- description: The profiles API from Monash University — 2 operation(s) for profiles.
  name: Monash University profiles API
  slug: monash-profiles-api
- description: The projects API from Monash University — 17 operation(s) for projects.
  name: Monash University projects API
  slug: monash-projects-api
- description: The symplectic API from Monash University — 5 operation(s) for symplectic.
  name: Monash University symplectic API
  slug: monash-symplectic-api
artifact_total: 29
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monash-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/monash-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monash-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monash-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/monash-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.monash.edu/
- group: other
  title: ''
  type: Research
  url: https://research.monash.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/monash-university
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/MonashStudentInnovation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/monash-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/monash-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/monash-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/monash-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Monash University is a public research university based in Melbourne, Australia, and a member of the Group of Eight. It ranked #42 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is modest and largely indirect: research data is published through monash.figshare on the figshare platform (which exposes a versioned REST API and an OAI-PMH endpoint), and Monash eResearch operates a Cloud Resource Allocation and Management System (CRAMS) API portal. Monash maintains a GitHub organization (currently with no public repositories) alongside team and student-innovation orgs. No central, openly documented institutional developer portal for course, catalog, timetable, or SIS APIs was found to be publicly available.'
examples:
- key_count: 4
  name: Monash Article Detail Example
  slug: monash-article-detail-example
- key_count: 4
  name: Monash Articles List Example
  slug: monash-articles-list-example
finops:
- name: Monash Finops
  service_category: Education
  slug: monash-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monash.png
json_schemas:
- name: Figshare Article
  property_count: 20
  slug: monash-article
- name: Figshare Author
  property_count: 7
  slug: monash-author
- name: Figshare Collection
  property_count: 6
  slug: monash-collection
json_structures:
- name: Monash Article Structure
  property_count: 15
  slug: monash-article-structure
- name: Monash Collection Structure
  property_count: 6
  slug: monash-collection-structure
jsonld:
- class_count: 22
  name: Monash Context
  property_count: 3
  slug: monash-context
layout: provider
modified: '2026-06-03'
name: Monash University
nav: Providers
network: true
overview: 'Monash University publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Monash University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Monash University''s developer surface includes authentication, GitHub presence, and 12 more developer resources.'
plans:
- name: Monash Plans Pricing
  plan_count: 2
  slug: monash-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Monash Rate Limits
  slug: monash-rate-limits
rules:
- name: Monash University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: monash-jsonschema-spectral-rules
- name: Monash University API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 4
  slug: monash-rules
scopes:
- name: Monash Scopes
  scope_count: 1
  slug: monash-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 46.9
  delta: -5.4
  facets:
    commercial_clarity: 36.8
    contract_quality: 69.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 59.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/monash/refs/heads/main/screenshots/monash-2026-06-20T185718.png
security:
- kind: authentication
  name: Monash Authentication
  slug: monash-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Monash Domain Security
  slug: monash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Monash Trust Center
  slug: monash-trust-center
  summary_line: ISO 27001, PCI DSS
slug: monash
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Australia
website: https://www.monash.edu/
---
