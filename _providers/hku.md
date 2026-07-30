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
  name: Hku Agentic Access
  operation_count: 157
  slug: hku-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: HKU Information Technology Services API developer portal, powered by Azure API Management. Developers can discover APIs, read documentation, try them interactively, and sign up for keys. Access is gat
  name: HKU ITS API Developer Portal
  slug: developer-portal
- description: 'HKU Scholars Hub is the University''s DSpace-based open-access institutional repository and current research information system (CRIS), collecting and disseminating HKU research outputs. It exposes an '
  name: HKU Scholars Hub OAI-PMH
  slug: scholars-hub-oai
- description: The altmetric API from University of Hong Kong — 1 operation(s) for altmetric.
  name: University of Hong Kong altmetric API
  slug: hku-altmetric-api
- description: The articles API from University of Hong Kong — 34 operation(s) for articles.
  name: University of Hong Kong articles API
  slug: hku-articles-api
- description: The authors API from University of Hong Kong — 2 operation(s) for authors.
  name: University of Hong Kong authors API
  slug: hku-authors-api
- description: The collections API from University of Hong Kong — 21 operation(s) for collections.
  name: University of Hong Kong collections API
  slug: hku-collections-api
- description: The institutions API from University of Hong Kong — 20 operation(s) for institutions.
  name: University of Hong Kong institutions API
  slug: hku-institutions-api
- description: The oauth API from University of Hong Kong — 1 operation(s) for oauth.
  name: University of Hong Kong oauth API
  slug: hku-oauth-api
- description: The other API from University of Hong Kong — 7 operation(s) for other.
  name: University of Hong Kong other API
  slug: hku-other-api
- description: The profiles API from University of Hong Kong — 2 operation(s) for profiles.
  name: University of Hong Kong profiles API
  slug: hku-profiles-api
- description: The projects API from University of Hong Kong — 17 operation(s) for projects.
  name: University of Hong Kong projects API
  slug: hku-projects-api
- description: The symplectic API from University of Hong Kong — 5 operation(s) for symplectic.
  name: University of Hong Kong symplectic API
  slug: hku-symplectic-api
artifact_total: 31
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hku-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hku-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hku-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hku-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.hku.hk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hku.hk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/hku-official
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-hong-kong/
- group: commercial
  title: ''
  type: Plans
  url: plans/hku-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hku-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hku-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hku.hk/press
created: '2026-06-03'
description: 'The University of Hong Kong (HKU) is a public research university in Hong Kong SAR, ranked #27 in the QS World University Rankings 2025. Its public developer and API footprint centers on an ITS API developer portal powered by Azure API Management (gated behind institutional sign-in), the Figshare-powered HKU DataHub research-data repository, and the DSpace-based HKU Scholars Hub institutional repository exposing an OAI-PMH metadata interface. Most administrative and identity interfaces are not openly self-service and require institutional affiliation.'
examples:
- key_count: 2
  name: Hku Get Article Example
  slug: hku-get-article-example
- key_count: 2
  name: Hku List Articles Example
  slug: hku-list-articles-example
- key_count: 2
  name: Hku Search Articles Example
  slug: hku-search-articles-example
finops:
- name: Hku Finops
  service_category: Education
  slug: hku-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hku.png
json_schemas:
- name: Figshare Article
  property_count: 16
  slug: hku-article
- name: Figshare Author
  property_count: 7
  slug: hku-author
- name: Figshare Project
  property_count: 5
  slug: hku-project
- name: Figshare PublicFile
  property_count: 8
  slug: hku-publicfile
json_structures:
- name: Hku Article Structure
  property_count: 16
  slug: hku-article-structure
- name: Hku Author Structure
  property_count: 7
  slug: hku-author-structure
jsonld:
- class_count: 16
  name: Hku Context
  property_count: 11
  slug: hku-context
layout: provider
modified: '2026-06-03'
name: University of Hong Kong
nav: Providers
network: true
overview: 'University of Hong Kong publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research Data, and Open Access.


  The University of Hong Kong catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Hong Kong''s developer surface includes authentication, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Hku Plans Pricing
  plan_count: 2
  slug: hku-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Hku Rate Limits
  slug: hku-rate-limits
rules:
- name: University of Hong Kong API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hku-jsonschema-spectral-rules
- name: University of Hong Kong API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 2
  slug: hku-rules
scopes:
- name: Hku Scopes
  scope_count: 1
  slug: hku-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 46.5
  delta: -4.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 74.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 51.3
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
screenshot: https://raw.githubusercontent.com/api-evangelist/hku/refs/heads/main/screenshots/hku-2026-06-20T182806.png
security:
- kind: authentication
  name: Hku Authentication
  slug: hku-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hku Domain Security
  slug: hku-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hku
tags:
- Education
- Higher Education
- University
- Research Data
- Open Access
- Hong Kong
website: https://www.hku.hk/
---
