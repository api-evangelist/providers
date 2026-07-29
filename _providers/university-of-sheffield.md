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
  name: University Of Sheffield Agentic Access
  operation_count: 157
  slug: university-of-sheffield-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: White Rose Research Online (WRRO) is the shared open-access research repository for the Universities of Leeds, Sheffield and York, running on EPrints. It exposes an OAI-PMH interface for harvesting me
  name: White Rose Research Online OAI-PMH
  slug: wrro-oai
- description: White Rose eTheses Online (WREO) is the shared electronic theses repository for the Universities of Leeds, Sheffield and York, running on EPrints. It exposes an OAI-PMH interface for harvesting Univer
  name: White Rose eTheses Online OAI-PMH
  slug: wreo-oai
- description: The altmetric API from University of Sheffield — 1 operation(s) for altmetric.
  name: University of Sheffield altmetric API
  slug: university-of-sheffield-altmetric-api
- description: The articles API from University of Sheffield — 34 operation(s) for articles.
  name: University of Sheffield articles API
  slug: university-of-sheffield-articles-api
- description: The authors API from University of Sheffield — 2 operation(s) for authors.
  name: University of Sheffield authors API
  slug: university-of-sheffield-authors-api
- description: The collections API from University of Sheffield — 21 operation(s) for collections.
  name: University of Sheffield collections API
  slug: university-of-sheffield-collections-api
- description: The institutions API from University of Sheffield — 20 operation(s) for institutions.
  name: University of Sheffield institutions API
  slug: university-of-sheffield-institutions-api
- description: The oauth API from University of Sheffield — 1 operation(s) for oauth.
  name: University of Sheffield oauth API
  slug: university-of-sheffield-oauth-api
- description: The other API from University of Sheffield — 7 operation(s) for other.
  name: University of Sheffield other API
  slug: university-of-sheffield-other-api
- description: The profiles API from University of Sheffield — 2 operation(s) for profiles.
  name: University of Sheffield profiles API
  slug: university-of-sheffield-profiles-api
- description: The projects API from University of Sheffield — 17 operation(s) for projects.
  name: University of Sheffield projects API
  slug: university-of-sheffield-projects-api
- description: The symplectic API from University of Sheffield — 5 operation(s) for symplectic.
  name: University of Sheffield symplectic API
  slug: university-of-sheffield-symplectic-api
artifact_total: 28
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-sheffield-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-sheffield-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-sheffield-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-sheffield-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.sheffield.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SheffieldUni
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/rcgsheffield
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-sheffield/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sheffielduni
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-sheffield-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-sheffield-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-sheffield-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Sheffield is a public research university in Sheffield, United Kingdom, ranked #105 in the QS World University Rankings 2025. Its public developer and API footprint is centered on open research infrastructure rather than a single unified developer portal: research data is published through ORDA (the institution''s figshare-backed research data repository, which exposes the standard figshare REST API and an OAI-PMH endpoint), and research outputs and theses are deposited in the White Rose Research Online (EPrints) and White Rose eTheses Online shared repositories, both of which expose OAI-PMH harvesting interfaces. The University also maintains public GitHub organizations for IT Services and research software engineering. No general-purpose, self-service developer portal for course, timetable, or student-information APIs was found publicly documented.'
examples:
- key_count: 2
  name: University Of Sheffield Get Article Example
  slug: university-of-sheffield-get-article-example
- key_count: 2
  name: University Of Sheffield List Articles Example
  slug: university-of-sheffield-list-articles-example
finops:
- name: University Of Sheffield Finops
  service_category: Education
  slug: university-of-sheffield-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-sheffield.png
json_schemas:
- name: Article
  property_count: 16
  slug: university-of-sheffield-article
- name: Author
  property_count: 7
  slug: university-of-sheffield-author
- name: PublicFile
  property_count: 8
  slug: university-of-sheffield-file
json_structures:
- name: University Of Sheffield Article Structure
  property_count: 16
  slug: university-of-sheffield-article-structure
jsonld:
- class_count: 3
  name: University Of Sheffield Context
  property_count: 4
  slug: university-of-sheffield-context
layout: provider
modified: '2026-06-03'
name: University of Sheffield
nav: Providers
network: true
overview: 'University of Sheffield publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research Data, and Open Access.


  The University of Sheffield catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Sheffield''s developer surface includes authentication, GitHub presence, and 11 more developer resources.'
plans:
- name: University Of Sheffield Plans Pricing
  plan_count: 2
  slug: university-of-sheffield-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 1
  name: University Of Sheffield Rate Limits
  slug: university-of-sheffield-rate-limits
rules:
- name: University of Sheffield API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-sheffield-jsonschema-spectral-rules
- name: University of Sheffield API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: university-of-sheffield-rules
scopes:
- name: University Of Sheffield Scopes
  scope_count: 1
  slug: university-of-sheffield-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 43.3
  delta: -4.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 70.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-sheffield/refs/heads/main/screenshots/university-of-sheffield-2026-06-20T200244.png
security:
- kind: authentication
  name: University Of Sheffield Authentication
  slug: university-of-sheffield-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: University Of Sheffield Domain Security
  slug: university-of-sheffield-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-sheffield
tags:
- Education
- Higher Education
- University
- Research Data
- Open Access
- OAI-PMH
- United Kingdom
website: https://www.sheffield.ac.uk/
---
