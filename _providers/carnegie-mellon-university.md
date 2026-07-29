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
  name: Carnegie Mellon University Agentic Access
  operation_count: 157
  slug: carnegie-mellon-university-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: Public, anonymously accessible HTTP/JSON API maintained by the Carnegie Mellon University Delphi research group providing real-time and historical epidemiological surveillance data, including the COVI
  name: Delphi Epidata API
  slug: delphi-epidata
- description: 'Carnegie Mellon''s campus-wide single sign-on identity service based on Shibboleth/SAML, used by service providers to authenticate authorized users. The identity provider metadata endpoint is publicly '
  name: CMU Web Login (Shibboleth SSO)
  slug: web-login-sso
- description: The altmetric API from Carnegie Mellon University — 1 operation(s) for altmetric.
  name: Carnegie Mellon University altmetric API
  slug: carnegie-mellon-university-altmetric-api
- description: The articles API from Carnegie Mellon University — 34 operation(s) for articles.
  name: Carnegie Mellon University articles API
  slug: carnegie-mellon-university-articles-api
- description: The authors API from Carnegie Mellon University — 2 operation(s) for authors.
  name: Carnegie Mellon University authors API
  slug: carnegie-mellon-university-authors-api
- description: The collections API from Carnegie Mellon University — 21 operation(s) for collections.
  name: Carnegie Mellon University collections API
  slug: carnegie-mellon-university-collections-api
- description: The institutions API from Carnegie Mellon University — 20 operation(s) for institutions.
  name: Carnegie Mellon University institutions API
  slug: carnegie-mellon-university-institutions-api
- description: The oauth API from Carnegie Mellon University — 1 operation(s) for oauth.
  name: Carnegie Mellon University oauth API
  slug: carnegie-mellon-university-oauth-api
- description: The other API from Carnegie Mellon University — 7 operation(s) for other.
  name: Carnegie Mellon University other API
  slug: carnegie-mellon-university-other-api
- description: The profiles API from Carnegie Mellon University — 2 operation(s) for profiles.
  name: Carnegie Mellon University profiles API
  slug: carnegie-mellon-university-profiles-api
- description: The projects API from Carnegie Mellon University — 17 operation(s) for projects.
  name: Carnegie Mellon University projects API
  slug: carnegie-mellon-university-projects-api
- description: The symplectic API from Carnegie Mellon University — 5 operation(s) for symplectic.
  name: Carnegie Mellon University symplectic API
  slug: carnegie-mellon-university-symplectic-api
artifact_total: 26
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/carnegie-mellon-university-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carnegie-mellon-university-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carnegie-mellon-university-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/carnegie-mellon-university-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.cmu.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cmu-delphi
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cmu-lib
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/carnegie-mellon-university/
- group: auth
  title: ''
  type: Authentication
  url: https://www.cmu.edu/computing/services/security/identity-access/authentication/sso-provider.html
- group: commercial
  title: ''
  type: Plans
  url: plans/carnegie-mellon-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/carnegie-mellon-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/carnegie-mellon-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Carnegie Mellon University is a private research university in Pittsburgh, Pennsylvania, United States, ranked #50 in the QS World University Rankings 2025. Its public developer and API footprint is concentrated in research and library infrastructure rather than a single central developer portal. The most prominent public API is the Delphi Epidata API, a real-time epidemiological data API maintained by CMU''s Delphi research group. The University Libraries operate the KiltHub institutional repository (hosted on figshare) which exposes research data and scholarly outputs via OAI-PMH and the figshare REST API, and CMU runs a campus-wide Shibboleth/Web Login single sign-on identity service.'
examples:
- key_count: 30
  name: Carnegie Mellon University Get Article Example
  slug: carnegie-mellon-university-get-article-example
- key_count: 2
  name: Carnegie Mellon University Search Articles Example
  slug: carnegie-mellon-university-search-articles-example
finops:
- name: Carnegie Mellon University Finops
  service_category: Education
  slug: carnegie-mellon-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carnegie-mellon-university.png
json_schemas:
- name: KiltHub Article (figshare public research output)
  property_count: 34
  slug: carnegie-mellon-university-article
json_structures:
- name: Carnegie Mellon University Article Structure
  property_count: 25
  slug: carnegie-mellon-university-article-structure
jsonld:
- class_count: 25
  name: Carnegie Mellon University Context
  property_count: 9
  slug: carnegie-mellon-university-context
layout: provider
modified: '2026-06-03'
name: Carnegie Mellon University
nav: Providers
network: true
overview: 'Carnegie Mellon University publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, United States, and Research.


  The Carnegie Mellon University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Carnegie Mellon University''s developer surface includes authentication, GitHub presence, and 11 more developer resources.'
plans:
- name: Carnegie Mellon University Plans Pricing
  plan_count: 2
  slug: carnegie-mellon-university-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 1
  name: Carnegie Mellon University Rate Limits
  slug: carnegie-mellon-university-rate-limits
rules:
- name: Carnegie Mellon University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: carnegie-mellon-university-jsonschema-spectral-rules
- name: Carnegie Mellon University API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: carnegie-mellon-university-rules
scopes:
- name: Carnegie Mellon University Scopes
  scope_count: 1
  slug: carnegie-mellon-university-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 44.1
  delta: -5.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 69.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 49.4
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
    score: 50.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/carnegie-mellon-university/refs/heads/main/screenshots/carnegie-mellon-university-2026-06-20T174011.png
security:
- kind: authentication
  name: Carnegie Mellon University Authentication
  slug: carnegie-mellon-university-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Carnegie Mellon University Domain Security
  slug: carnegie-mellon-university-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: carnegie-mellon-university
tags:
- Education
- Higher Education
- University
- United States
- Research
- Epidemiology
- Open Data
- Library
- Institutional Repository
website: https://www.cmu.edu/
---
