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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 81
  human_in_the_loop: 2
  name: University Of Sussex Agentic Access
  operation_count: 157
  slug: university-of-sussex-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: The University of Sussex uses Okta for single sign-on identity and access management, providing OAuth2 / OpenID Connect authentication to enrolled university applications including Sussex Direct. Acce
  name: University of Sussex Single Sign-On (Okta)
  slug: okta-sso
- description: The altmetric API from University of Sussex — 1 operation(s) for altmetric.
  name: University of Sussex altmetric API
  slug: university-of-sussex-altmetric-api
- description: The articles API from University of Sussex — 34 operation(s) for articles.
  name: University of Sussex articles API
  slug: university-of-sussex-articles-api
- description: The authors API from University of Sussex — 2 operation(s) for authors.
  name: University of Sussex authors API
  slug: university-of-sussex-authors-api
- description: The collections API from University of Sussex — 21 operation(s) for collections.
  name: University of Sussex collections API
  slug: university-of-sussex-collections-api
- description: The institutions API from University of Sussex — 20 operation(s) for institutions.
  name: University of Sussex institutions API
  slug: university-of-sussex-institutions-api
- description: The oauth API from University of Sussex — 1 operation(s) for oauth.
  name: University of Sussex oauth API
  slug: university-of-sussex-oauth-api
- description: The other API from University of Sussex — 7 operation(s) for other.
  name: University of Sussex other API
  slug: university-of-sussex-other-api
- description: The profiles API from University of Sussex — 2 operation(s) for profiles.
  name: University of Sussex profiles API
  slug: university-of-sussex-profiles-api
- description: The projects API from University of Sussex — 17 operation(s) for projects.
  name: University of Sussex projects API
  slug: university-of-sussex-projects-api
- description: The symplectic API from University of Sussex — 5 operation(s) for symplectic.
  name: University of Sussex symplectic API
  slug: university-of-sussex-symplectic-api
artifact_total: 28
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-sussex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-sussex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-sussex-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-sussex-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.sussex.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/universityofsussex
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-sussex/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-sussex-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-sussex-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-sussex-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Sussex is a research-intensive public university near Brighton, United Kingdom, ranked #247 in the QS World University Rankings 2025. Its public, machine-readable footprint is limited: the university''s research outputs (publications, data, theses) are hosted on Figshare, which exposes a public REST API, while identity and access are managed through Okta single sign-on (OAuth2/OpenID Connect) for staff and students. The former Sussex Research Online EPrints repository and its OAI-PMH endpoint have been decommissioned and now redirect to the Figshare-backed publications service. A GitHub organization exists but currently publishes no public repositories.'
examples:
- key_count: 2
  name: University Of Sussex Articles List Example
  slug: university-of-sussex-articles-list-example
- key_count: 2
  name: University Of Sussex Articles Search Example
  slug: university-of-sussex-articles-search-example
finops:
- name: University Of Sussex Finops
  service_category: Education
  slug: university-of-sussex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-sussex.png
json_schemas:
- name: Figshare Article
  property_count: 16
  slug: university-of-sussex-article
- name: Figshare Collection
  property_count: 6
  slug: university-of-sussex-collection
- name: Figshare Project
  property_count: 5
  slug: university-of-sussex-project
json_structures:
- name: University Of Sussex Article Structure
  property_count: 16
  slug: university-of-sussex-article-structure
- name: University Of Sussex Collection Structure
  property_count: 6
  slug: university-of-sussex-collection-structure
jsonld:
- class_count: 10
  name: University Of Sussex Context
  property_count: 10
  slug: university-of-sussex-context
layout: provider
modified: '2026-06-03'
name: University of Sussex
nav: Providers
network: true
overview: 'University of Sussex publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The University of Sussex catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Sussex''s developer surface includes authentication, GitHub presence, and 9 more developer resources.'
plans:
- name: University Of Sussex Plans Pricing
  plan_count: 2
  slug: university-of-sussex-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 1
  name: University Of Sussex Rate Limits
  slug: university-of-sussex-rate-limits
rules:
- name: University of Sussex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-sussex-jsonschema-spectral-rules
- name: University of Sussex API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: university-of-sussex-rules
scopes:
- name: University Of Sussex Scopes
  scope_count: 1
  slug: university-of-sussex-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 41.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 65.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-sussex/refs/heads/main/screenshots/university-of-sussex-2026-06-20T200307.png
security:
- kind: authentication
  name: University Of Sussex Authentication
  slug: university-of-sussex-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: University Of Sussex Domain Security
  slug: university-of-sussex-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: university-of-sussex
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- United Kingdom
website: https://www.sussex.ac.uk/
---
