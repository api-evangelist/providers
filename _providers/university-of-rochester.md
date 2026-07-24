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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 81
  human_in_the_loop: 2
  name: University Of Rochester Agentic Access
  operation_count: 157
  slug: university-of-rochester-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: 'The legacy UR Research institutional repository exposes a live OAI-PMH interface for harvesting Dublin Core metadata of deposited research outputs (papers, theses, datasets). The endpoint responds to '
  name: UR Research Institutional Repository OAI-PMH
  slug: urresearch-oai
- description: The altmetric API from University of Rochester — 1 operation(s) for altmetric.
  name: University of Rochester altmetric API
  slug: university-of-rochester-altmetric-api
- description: The articles API from University of Rochester — 34 operation(s) for articles.
  name: University of Rochester articles API
  slug: university-of-rochester-articles-api
- description: The authors API from University of Rochester — 2 operation(s) for authors.
  name: University of Rochester authors API
  slug: university-of-rochester-authors-api
- description: The collections API from University of Rochester — 21 operation(s) for collections.
  name: University of Rochester collections API
  slug: university-of-rochester-collections-api
- description: The institutions API from University of Rochester — 20 operation(s) for institutions.
  name: University of Rochester institutions API
  slug: university-of-rochester-institutions-api
- description: The oauth API from University of Rochester — 1 operation(s) for oauth.
  name: University of Rochester oauth API
  slug: university-of-rochester-oauth-api
- description: The other API from University of Rochester — 7 operation(s) for other.
  name: University of Rochester other API
  slug: university-of-rochester-other-api
- description: The profiles API from University of Rochester — 2 operation(s) for profiles.
  name: University of Rochester profiles API
  slug: university-of-rochester-profiles-api
- description: The projects API from University of Rochester — 17 operation(s) for projects.
  name: University of Rochester projects API
  slug: university-of-rochester-projects-api
- description: The symplectic API from University of Rochester — 5 operation(s) for symplectic.
  name: University of Rochester symplectic API
  slug: university-of-rochester-symplectic-api
artifact_total: 28
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-rochester-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-rochester-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-rochester-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-rochester-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.rochester.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rochester-rcl
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-rochester/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-rochester-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-rochester-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-rochester-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.rochester.edu/newscenter/feed/
created: '2026-06-03'
description: 'The University of Rochester is a private research university in Rochester, New York, ranked #236 in the QS World University Rankings 2025. It does not operate a single official, centralized public developer portal; its publicly reachable programmatic surface is found across library and research-data infrastructure. The University of Rochester Research Repository (URRR) runs on the Figshare platform, which exposes a public REST API and an OAI-PMH endpoint, and the legacy UR Research institutional repository still serves a live OAI-PMH interface. The River Campus Libraries also maintain an active public GitHub organization with digital-library tooling. Most enterprise systems (SIS, identity/SSO, course/catalog) are gated and not publicly documented.'
examples:
- key_count: 3
  name: University Of Rochester Article Get Example
  slug: university-of-rochester-article-get-example
- key_count: 3
  name: University Of Rochester Articles Search Example
  slug: university-of-rochester-articles-search-example
- key_count: 3
  name: University Of Rochester Collection Get Example
  slug: university-of-rochester-collection-get-example
finops:
- name: University Of Rochester Finops
  service_category: Education
  slug: university-of-rochester-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-rochester.png
json_schemas:
- name: Figshare Article
  property_count: 16
  slug: university-of-rochester-article
- name: Figshare Collection
  property_count: 6
  slug: university-of-rochester-collection
json_structures:
- name: University Of Rochester Article Structure
  property_count: 16
  slug: university-of-rochester-article-structure
- name: University Of Rochester Collection Structure
  property_count: 6
  slug: university-of-rochester-collection-structure
jsonld:
- class_count: 15
  name: University Of Rochester Context
  property_count: 10
  slug: university-of-rochester-context
layout: provider
modified: '2026-06-03'
name: University of Rochester
nav: Providers
network: true
overview: 'University of Rochester publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research, and Library.


  The University of Rochester catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Rochester''s developer surface includes authentication, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: University Of Rochester Plans Pricing
  plan_count: 2
  slug: university-of-rochester-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: University Of Rochester Rate Limits
  slug: university-of-rochester-rate-limits
rules:
- name: University of Rochester API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-rochester-jsonschema-spectral-rules
- name: University of Rochester API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-rochester-rules
scopes:
- name: University Of Rochester Scopes
  scope_count: 1
  slug: university-of-rochester-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 49.2
  delta: 1.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 67.4
    developer_ergonomics: 13.0
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 47.5
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 58.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-rochester/refs/heads/main/screenshots/university-of-rochester-2026-06-20T200223.png
security:
- kind: authentication
  name: University Of Rochester Authentication
  slug: university-of-rochester-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: University Of Rochester Domain Security
  slug: university-of-rochester-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: university-of-rochester
tags:
- Education
- Higher Education
- University
- Research
- Library
- Institutional Repository
- Open Data
- United States
website: https://www.rochester.edu/
---
