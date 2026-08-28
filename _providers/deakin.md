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
  name: Deakin Agentic Access
  operation_count: 157
  slug: deakin-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: 'Deakin Research Online is the university''s research repository, now hosted on the figshare platform. It exposes research-output metadata for harvesting via the OAI-PMH protocol. The DRO host issues a '
  name: Deakin Research Online (DRO) OAI-PMH
  slug: dro-oai
- description: The altmetric API from Deakin University — 1 operation(s) for altmetric.
  name: Deakin University altmetric API
  slug: deakin-altmetric-api
- description: The articles API from Deakin University — 34 operation(s) for articles.
  name: Deakin University articles API
  slug: deakin-articles-api
- description: The authors API from Deakin University — 2 operation(s) for authors.
  name: Deakin University authors API
  slug: deakin-authors-api
- description: The collections API from Deakin University — 21 operation(s) for collections.
  name: Deakin University collections API
  slug: deakin-collections-api
- description: The institutions API from Deakin University — 20 operation(s) for institutions.
  name: Deakin University institutions API
  slug: deakin-institutions-api
- description: The oauth API from Deakin University — 1 operation(s) for oauth.
  name: Deakin University oauth API
  slug: deakin-oauth-api
- description: The other API from Deakin University — 7 operation(s) for other.
  name: Deakin University other API
  slug: deakin-other-api
- description: The profiles API from Deakin University — 2 operation(s) for profiles.
  name: Deakin University profiles API
  slug: deakin-profiles-api
- description: The projects API from Deakin University — 17 operation(s) for projects.
  name: Deakin University projects API
  slug: deakin-projects-api
- description: The symplectic API from Deakin University — 5 operation(s) for symplectic.
  name: Deakin University symplectic API
  slug: deakin-symplectic-api
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Figshare altmetric API
  slug: open-deakin-altmetric-api
- collection_type: open
  name: Figshare altmetric articles API
  slug: open-deakin-articles-api
- collection_type: open
  name: Figshare altmetric authors API
  slug: open-deakin-authors-api
- collection_type: open
  name: Figshare altmetric collections API
  slug: open-deakin-collections-api
- collection_type: open
  name: Figshare altmetric institutions API
  slug: open-deakin-institutions-api
- collection_type: open
  name: Figshare altmetric oauth API
  slug: open-deakin-oauth-api
- collection_type: open
  name: Figshare altmetric other API
  slug: open-deakin-other-api
- collection_type: open
  name: Figshare altmetric profiles API
  slug: open-deakin-profiles-api
- collection_type: open
  name: Figshare altmetric projects API
  slug: open-deakin-projects-api
- collection_type: open
  name: Figshare altmetric symplectic API
  slug: open-deakin-symplectic-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deakin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deakin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deakin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/deakin-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.deakin.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Deakin
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/deakin-university/
- group: auth
  title: ''
  type: Authentication
  url: https://signon.deakin.edu.au/
- group: commercial
  title: ''
  type: Plans
  url: plans/deakin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deakin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/deakin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: other
  title: ''
  type: ProductPage
  url: https://dataportal.deakin.edu.au/
created: '2026-06-03'
description: 'Deakin University is a public research university in Victoria, Australia, with campuses in Geelong, Warrnambool and Melbourne, ranked #197 in the QS World University Rankings 2025. Like most universities, Deakin operates an integration-heavy IT estate (its SSO is a Shibboleth/SAML2 identity provider) but does not publish a public, self-service developer API portal. Its confirmed public, machine-readable footprint is concentrated in research infrastructure: the Deakin Research Online (DRO) repository runs on figshare (which exposes a public OAI-PMH and REST API), a public Data Portal for sharing research datasets, and an active GitHub organization. Most catalogued surfaces below are third-party-hosted or gated rather than first-party, documented APIs.'
examples:
- key_count: 48
  name: Deakin Get Article Example
  slug: deakin-get-article-example
- key_count: 4
  name: Deakin Search Articles Example
  slug: deakin-search-articles-example
finops:
- name: Deakin Finops
  service_category: Education
  slug: deakin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deakin.png
json_schemas:
- name: figshare Article
  property_count: 16
  slug: deakin-article
- name: figshare Author
  property_count: 7
  slug: deakin-author
- name: figshare Collection
  property_count: 6
  slug: deakin-collection
- name: figshare Project
  property_count: 5
  slug: deakin-project
json_structures:
- name: Deakin Article Structure
  property_count: 16
  slug: deakin-article-structure
- name: Deakin Author Structure
  property_count: 7
  slug: deakin-author-structure
- name: Deakin Collection Structure
  property_count: 6
  slug: deakin-collection-structure
- name: Deakin Project Structure
  property_count: 5
  slug: deakin-project-structure
jsonld:
- class_count: 20
  name: Deakin Context
  property_count: 8
  slug: deakin-context
layout: provider
modified: '2026-07-25'
name: Deakin University
nav: Providers
network: true
overview: 'Deakin University publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Deakin University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Deakin University''s developer surface includes authentication, GitHub presence, and 11 more developer resources.'
plans:
- name: Deakin Plans Pricing
  plan_count: 2
  slug: deakin-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Deakin Rate Limits
  slug: deakin-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Deakin University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: deakin-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Deakin University API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: deakin-rules
scopes:
- name: Deakin Scopes
  scope_count: 1
  slug: deakin-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 42.7
  delta: 4.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 25.0
    contract_quality: 71.3
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 38.2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/deakin/refs/heads/main/screenshots/deakin-2026-06-20T175744.png
security:
- kind: authentication
  name: Deakin Authentication
  slug: deakin-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Deakin Domain Security
  slug: deakin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deakin
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Australia
website: https://www.deakin.edu.au/
---
