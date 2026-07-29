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
  name: University Of Auckland Agentic Access
  operation_count: 157
  slug: university-of-auckland-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: 'OAI-PMH metadata harvesting endpoint for the University of Auckland Figshare research repository. Supports standard OAI-PMH verbs and multiple metadata schemas (Dublin Core, DataCite, RDF, CERIF XML, '
  name: University of Auckland Figshare OAI-PMH Service
  slug: figshare-oai
- description: A set of public University Directory APIs that allow anyone to search for University of Auckland staff and retrieve a summary profile or a full profile of a staff member. Documented as available exter
  name: University Directory API
  slug: unidirectory
- description: The altmetric API from University of Auckland — 1 operation(s) for altmetric.
  name: University of Auckland altmetric API
  slug: university-of-auckland-altmetric-api
- description: The articles API from University of Auckland — 34 operation(s) for articles.
  name: University of Auckland articles API
  slug: university-of-auckland-articles-api
- description: The authors API from University of Auckland — 2 operation(s) for authors.
  name: University of Auckland authors API
  slug: university-of-auckland-authors-api
- description: The collections API from University of Auckland — 21 operation(s) for collections.
  name: University of Auckland collections API
  slug: university-of-auckland-collections-api
- description: The institutions API from University of Auckland — 20 operation(s) for institutions.
  name: University of Auckland institutions API
  slug: university-of-auckland-institutions-api
- description: The oauth API from University of Auckland — 1 operation(s) for oauth.
  name: University of Auckland oauth API
  slug: university-of-auckland-oauth-api
- description: The other API from University of Auckland — 7 operation(s) for other.
  name: University of Auckland other API
  slug: university-of-auckland-other-api
- description: The profiles API from University of Auckland — 2 operation(s) for profiles.
  name: University of Auckland profiles API
  slug: university-of-auckland-profiles-api
- description: The projects API from University of Auckland — 17 operation(s) for projects.
  name: University of Auckland projects API
  slug: university-of-auckland-projects-api
- description: The symplectic API from University of Auckland — 5 operation(s) for symplectic.
  name: University of Auckland symplectic API
  slug: university-of-auckland-symplectic-api
artifact_total: 26
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-auckland-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-auckland-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-auckland-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-auckland-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.auckland.ac.nz/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/university-of-auckland
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-auckland/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-auckland-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-auckland-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-auckland-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-auckland-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-auckland-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-auckland-context.jsonld
created: '2026-06-03'
description: 'The University of Auckland is New Zealand''s largest and highest-ranked university, placed #92 in the QS World University Rankings 2025. Its public developer and API footprint is modest and decentralized rather than a single unified developer portal. The most clearly documented machine-readable interfaces are its institutional Figshare research data repository (REST API and OAI-PMH, institution id 12) and a public University Directory staff-search API. The University also maintains a domain-verified GitHub organization where it publishes open-source projects spanning data engineering, identity integration, and research tooling.'
examples:
- key_count: 2
  name: University Of Auckland Articles List Example
  slug: university-of-auckland-articles-list-example
finops:
- name: University Of Auckland Finops
  service_category: Education
  slug: university-of-auckland-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-auckland.png
json_schemas:
- name: Figshare Article
  property_count: 16
  slug: university-of-auckland-article
- name: Figshare Collection
  property_count: 6
  slug: university-of-auckland-collection
json_structures:
- name: University Of Auckland Article Structure
  property_count: 16
  slug: university-of-auckland-article-structure
jsonld:
- class_count: 3
  name: University Of Auckland Context
  property_count: 4
  slug: university-of-auckland-context
layout: provider
modified: '2026-06-03'
name: University of Auckland
nav: Providers
network: true
overview: 'University of Auckland publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The University of Auckland catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Auckland''s developer surface includes authentication, GitHub presence, and 12 more developer resources.'
plans:
- name: University Of Auckland Plans Pricing
  plan_count: 2
  slug: university-of-auckland-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 1
  name: University Of Auckland Rate Limits
  slug: university-of-auckland-rate-limits
rules:
- name: University of Auckland API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-auckland-jsonschema-spectral-rules
- name: University of Auckland API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 3
  slug: university-of-auckland-rules
scopes:
- name: University Of Auckland Scopes
  scope_count: 1
  slug: university-of-auckland-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 43.9
  delta: -5.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 66.6
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 49.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-auckland/refs/heads/main/screenshots/university-of-auckland-2026-06-20T200126.png
security:
- kind: authentication
  name: University Of Auckland Authentication
  slug: university-of-auckland-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: University Of Auckland Domain Security
  slug: university-of-auckland-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-auckland
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- New Zealand
website: https://www.auckland.ac.nz/
---
