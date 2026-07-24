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
  name: Uon Agentic Access
  operation_count: 157
  slug: uon-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: Open Research Newcastle, on the Figshare platform, exposes an OAI-PMH metadata harvesting endpoint for its open access records. The endpoint is reachable at openresearch.newcastle.edu.au/oai; automate
  name: Open Research Newcastle (OAI-PMH)
  slug: open-research-oai
- description: The altmetric API from University of Newcastle Australia — 1 operation(s) for altmetric.
  name: University of Newcastle Australia altmetric API
  slug: uon-altmetric-api
- description: The articles API from University of Newcastle Australia — 34 operation(s) for articles.
  name: University of Newcastle Australia articles API
  slug: uon-articles-api
- description: The authors API from University of Newcastle Australia — 2 operation(s) for authors.
  name: University of Newcastle Australia authors API
  slug: uon-authors-api
- description: The collections API from University of Newcastle Australia — 21 operation(s) for collections.
  name: University of Newcastle Australia collections API
  slug: uon-collections-api
- description: The institutions API from University of Newcastle Australia — 20 operation(s) for institutions.
  name: University of Newcastle Australia institutions API
  slug: uon-institutions-api
- description: The oauth API from University of Newcastle Australia — 1 operation(s) for oauth.
  name: University of Newcastle Australia oauth API
  slug: uon-oauth-api
- description: The other API from University of Newcastle Australia — 7 operation(s) for other.
  name: University of Newcastle Australia other API
  slug: uon-other-api
- description: The profiles API from University of Newcastle Australia — 2 operation(s) for profiles.
  name: University of Newcastle Australia profiles API
  slug: uon-profiles-api
- description: The projects API from University of Newcastle Australia — 17 operation(s) for projects.
  name: University of Newcastle Australia projects API
  slug: uon-projects-api
- description: The symplectic API from University of Newcastle Australia — 5 operation(s) for symplectic.
  name: University of Newcastle Australia symplectic API
  slug: uon-symplectic-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/uon-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.newcastle.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/university-of-newcastle-research
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-newcastle/
- group: commercial
  title: ''
  type: Plans
  url: plans/uon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uon-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Newcastle (UON) is a public research university based in Newcastle, New South Wales, Australia, ranked #179 in the QS World University Rankings 2025. Like most Australian universities, UON does not operate a dedicated public API developer portal; the bulk of its student, staff, and enterprise systems (myUni, online tools, ServiceNow) sit behind institutional SSO and are not openly documented. Its most accessible programmatic footprint is research-oriented: Open Research Newcastle, the institutional open access repository hosted on the Figshare platform, exposes machine-readable access via the Figshare public REST API and an OAI-PMH endpoint, and the University maintains a research code presence on GitHub.'
examples:
- key_count: 2
  name: Uon Article Detail Example
  slug: uon-article-detail-example
- key_count: 2
  name: Uon Article List Example
  slug: uon-article-list-example
finops:
- name: Uon Finops
  service_category: Education
  slug: uon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uon.png
json_schemas:
- name: Figshare Article
  property_count: 19
  slug: uon-article
- name: Figshare Author
  property_count: 7
  slug: uon-author
- name: Figshare PublicFile
  property_count: 8
  slug: uon-file
json_structures:
- name: Uon Article Structure
  property_count: 19
  slug: uon-article-structure
jsonld:
- class_count: 4
  name: Uon Context
  property_count: 3
  slug: uon-context
layout: provider
modified: '2026-06-03'
name: University of Newcastle Australia
nav: Providers
network: true
overview: 'University of Newcastle Australia publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research, and Open Research.


  The University of Newcastle Australia catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Newcastle Australia''s developer surface includes authentication, GitHub presence, and 9 more developer resources.'
plans:
- name: Uon Plans Pricing
  plan_count: 2
  slug: uon-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 1
  name: Uon Rate Limits
  slug: uon-rate-limits
rules:
- name: University of Newcastle Australia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: uon-jsonschema-spectral-rules
- name: University of Newcastle Australia API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: uon-rules
scopes:
- name: Uon Scopes
  scope_count: 1
  slug: uon-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 47.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 67.4
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 47.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uon/refs/heads/main/screenshots/uon-2026-06-20T200428.png
security:
- kind: authentication
  name: Uon Authentication
  slug: uon-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Uon Domain Security
  slug: uon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uon
tags:
- Education
- Higher Education
- University
- Research
- Open Research
- Open Access
- Repository
- OAI-PMH
- Australia
website: https://www.newcastle.edu.au/
---
