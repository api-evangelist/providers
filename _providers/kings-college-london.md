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
  name: Kings College London Agentic Access
  operation_count: 157
  slug: kings-college-london-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: OAI-PMH metadata harvesting interface for the King's Research Portal, the front end of Pure, King's research information system and institutional repository. The interface returns a live OAI-PMH respo
  name: King's Research Portal (Pure) OAI-PMH
  slug: pure-oai
- description: The altmetric API from King's College London — 1 operation(s) for altmetric.
  name: King's College London altmetric API
  slug: kings-college-london-altmetric-api
- description: The articles API from King's College London — 34 operation(s) for articles.
  name: King's College London articles API
  slug: kings-college-london-articles-api
- description: The authors API from King's College London — 2 operation(s) for authors.
  name: King's College London authors API
  slug: kings-college-london-authors-api
- description: The collections API from King's College London — 21 operation(s) for collections.
  name: King's College London collections API
  slug: kings-college-london-collections-api
- description: The institutions API from King's College London — 20 operation(s) for institutions.
  name: King's College London institutions API
  slug: kings-college-london-institutions-api
- description: The oauth API from King's College London — 1 operation(s) for oauth.
  name: King's College London oauth API
  slug: kings-college-london-oauth-api
- description: The other API from King's College London — 7 operation(s) for other.
  name: King's College London other API
  slug: kings-college-london-other-api
- description: The profiles API from King's College London — 2 operation(s) for profiles.
  name: King's College London profiles API
  slug: kings-college-london-profiles-api
- description: The projects API from King's College London — 17 operation(s) for projects.
  name: King's College London projects API
  slug: kings-college-london-projects-api
- description: The symplectic API from King's College London — 5 operation(s) for symplectic.
  name: King's College London symplectic API
  slug: kings-college-london-symplectic-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kings-college-london-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kings-college-london-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kings-college-london-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kings-college-london-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.kcl.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kcl-eresearch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/king's-college-london/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.er.kcl.ac.uk/
- group: commercial
  title: ''
  type: Plans
  url: plans/kings-college-london-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kings-college-london-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kings-college-london-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/kings-college-london-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.kcl.ac.uk/news
created: '2026-06-03'
description: 'King''s College London (KCL) is a public research university in London, United Kingdom, ranked #41 in the QS World University Rankings 2025. Like most research universities, King''s does not operate a centralized public developer portal; its machine-readable footprint is concentrated in research and library infrastructure. The King''s Research Portal (Pure) exposes a live OAI-PMH metadata interface, and the King''s research data repository is hosted on Figshare, which provides a public REST API and OAI-PMH endpoint. King''s also runs an e-Research group with a large public GitHub organization.'
examples:
- key_count: 24
  name: Kings College London Get Article Example
  slug: kings-college-london-get-article-example
finops:
- name: Kings College London Finops
  service_category: Education
  slug: kings-college-london-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kings-college-london.png
json_schemas:
- name: Figshare Article
  property_count: 18
  slug: kings-college-london-article
- name: Figshare Author
  property_count: 7
  slug: kings-college-london-author
- name: Figshare Collection
  property_count: 6
  slug: kings-college-london-collection
json_structures:
- name: Kings College London Article Structure
  property_count: 15
  slug: kings-college-london-article-structure
- name: Kings College London Collection Structure
  property_count: 6
  slug: kings-college-london-collection-structure
jsonld:
- class_count: 4
  name: Kings College London Context
  property_count: 4
  slug: kings-college-london-context
layout: provider
modified: '2026-06-03'
name: King's College London
nav: Providers
network: true
overview: 'King''s College London publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The King''s College London catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  King''s College London''s developer surface includes authentication, GitHub presence, engineering blog, and 11 more developer resources.'
plans:
- name: Kings College London Plans Pricing
  plan_count: 2
  slug: kings-college-london-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 1
  name: Kings College London Rate Limits
  slug: kings-college-london-rate-limits
rules:
- name: King's College London API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: kings-college-london-jsonschema-spectral-rules
- name: King's College London API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: kings-college-london-rules
scopes:
- name: Kings College London Scopes
  scope_count: 1
  slug: kings-college-london-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 44.3
  delta: -5.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 49.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/kings-college-london/refs/heads/main/screenshots/kings-college-london-2026-06-20T184045.png
security:
- kind: authentication
  name: Kings College London Authentication
  slug: kings-college-london-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Kings College London Domain Security
  slug: kings-college-london-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kings-college-london
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- OAI-PMH
- Library
- United Kingdom
website: https://www.kcl.ac.uk/
---
