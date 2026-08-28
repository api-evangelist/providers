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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 81
  human_in_the_loop: 2
  name: Loughborough Agentic Access
  operation_count: 157
  slug: loughborough-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: OAI-PMH metadata harvesting endpoint for the Loughborough Research Repository, served via figshare and scoped to the Loughborough portal set. Supports Open Archives Initiative Protocol for Metadata Ha
  name: Loughborough Research Repository OAI-PMH
  slug: research-repository-oai
- description: The altmetric API from Loughborough University — 1 operation(s) for altmetric.
  name: Loughborough University altmetric API
  slug: loughborough-altmetric-api
- description: The articles API from Loughborough University — 34 operation(s) for articles.
  name: Loughborough University articles API
  slug: loughborough-articles-api
- description: The authors API from Loughborough University — 2 operation(s) for authors.
  name: Loughborough University authors API
  slug: loughborough-authors-api
- description: The collections API from Loughborough University — 21 operation(s) for collections.
  name: Loughborough University collections API
  slug: loughborough-collections-api
- description: The institutions API from Loughborough University — 20 operation(s) for institutions.
  name: Loughborough University institutions API
  slug: loughborough-institutions-api
- description: The oauth API from Loughborough University — 1 operation(s) for oauth.
  name: Loughborough University oauth API
  slug: loughborough-oauth-api
- description: The other API from Loughborough University — 7 operation(s) for other.
  name: Loughborough University other API
  slug: loughborough-other-api
- description: The profiles API from Loughborough University — 2 operation(s) for profiles.
  name: Loughborough University profiles API
  slug: loughborough-profiles-api
- description: The projects API from Loughborough University — 17 operation(s) for projects.
  name: Loughborough University projects API
  slug: loughborough-projects-api
- description: The symplectic API from Loughborough University — 5 operation(s) for symplectic.
  name: Loughborough University symplectic API
  slug: loughborough-symplectic-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Loughborough Research Repository (figshare API) altmetric API
  slug: open-loughborough-altmetric-api
- collection_type: open
  name: Loughborough Research Repository (figshare API) altmetric articles API
  slug: open-loughborough-articles-api
- collection_type: open
  name: Loughborough Research Repository (figshare API) altmetric authors API
  slug: open-loughborough-authors-api
- collection_type: open
  name: Loughborough Research Repository (figshare API) altmetric collections API
  slug: open-loughborough-collections-api
- collection_type: open
  name: Loughborough Research Repository (figshare API) altmetric institutions API
  slug: open-loughborough-institutions-api
- collection_type: open
  name: Loughborough Research Repository (figshare API) altmetric oauth API
  slug: open-loughborough-oauth-api
- collection_type: open
  name: Loughborough Research Repository (figshare API) altmetric other API
  slug: open-loughborough-other-api
- collection_type: open
  name: Loughborough Research Repository (figshare API) altmetric profiles API
  slug: open-loughborough-profiles-api
- collection_type: open
  name: Loughborough Research Repository (figshare API) altmetric projects API
  slug: open-loughborough-projects-api
- collection_type: open
  name: Loughborough Research Repository (figshare API) altmetric symplectic API
  slug: open-loughborough-symplectic-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loughborough-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loughborough-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loughborough-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/loughborough-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.lboro.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/LoughboroughUniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/school/loughborough-university/
- group: other
  title: ''
  type: Repository
  url: https://repository.lboro.ac.uk/
- group: commercial
  title: ''
  type: Plans
  url: plans/loughborough-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loughborough-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loughborough-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lboro.ac.uk/news-events/rss/
- group: other
  title: ''
  type: ProductPage
  url: https://www.lboro.ac.uk/services/it/topics/student-account/
created: '2026-06-03'
description: 'Loughborough University is a public research university in Leicestershire, United Kingdom, ranked #224 in the QS World University Rankings 2025. It is well known for sport, engineering, and design programmes and operates a campus in London alongside its main Loughborough campus. The university does not publish a first-party developer portal or open-data API; its public programmatic footprint is limited to its figshare-powered Loughborough Research Repository (which exposes the standard figshare REST API and an OAI-PMH metadata harvesting endpoint scoped to the institution) and a Shibboleth/SAML identity provider used for federated single sign-on.'
examples:
- key_count: 2
  name: Loughborough Get Article Example
  slug: loughborough-get-article-example
- key_count: 2
  name: Loughborough List Articles Example
  slug: loughborough-list-articles-example
finops:
- name: Loughborough Finops
  service_category: Education
  slug: loughborough-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loughborough.png
json_schemas:
- name: Loughborough Research Repository Article
  property_count: 29
  slug: loughborough-article
- name: Loughborough Research Repository Author
  property_count: 7
  slug: loughborough-author
json_structures:
- name: Loughborough Article Structure
  property_count: 28
  slug: loughborough-article-structure
jsonld:
- class_count: 20
  name: Loughborough Context
  property_count: 12
  slug: loughborough-context
layout: provider
modified: '2026-07-25'
name: Loughborough University
nav: Providers
network: true
overview: 'Loughborough University publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, United Kingdom, and Research Data.


  The Loughborough University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Loughborough University''s developer surface includes authentication, GitHub presence, engineering blog, and 11 more developer resources.'
plans:
- name: Loughborough Plans Pricing
  plan_count: 2
  slug: loughborough-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Loughborough Rate Limits
  slug: loughborough-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Loughborough University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: loughborough-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Loughborough University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: loughborough-rules
scopes:
- name: Loughborough Scopes
  scope_count: 1
  slug: loughborough-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 43.9
  delta: 1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 70.3
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 42.0
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
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loughborough/refs/heads/main/screenshots/loughborough-2026-06-20T184729.png
security:
- kind: authentication
  name: Loughborough Authentication
  slug: loughborough-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Loughborough Domain Security
  slug: loughborough-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: loughborough
tags:
- Education
- Higher Education
- University
- United Kingdom
- Research Data
- Open Access
- Repository
- Identity
website: https://www.lboro.ac.uk/
---
