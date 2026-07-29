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
  name: University Of The Witwatersrand Agentic Access
  operation_count: 166
  slug: university-of-the-witwatersrand-agentic-access
  summary_line: 166 operations · 81 acting · 2 human-in-the-loop
api_count: 15
apis:
- description: The altmetric API from University of the Witwatersrand — 1 operation(s) for altmetric.
  name: University of the Witwatersrand altmetric API
  slug: university-of-the-witwatersrand-altmetric-api
- description: The articles API from University of the Witwatersrand — 34 operation(s) for articles.
  name: University of the Witwatersrand articles API
  slug: university-of-the-witwatersrand-articles-api
- description: The authors API from University of the Witwatersrand — 2 operation(s) for authors.
  name: University of the Witwatersrand authors API
  slug: university-of-the-witwatersrand-authors-api
- description: The collections API from University of the Witwatersrand — 23 operation(s) for collections.
  name: University of the Witwatersrand collections API
  slug: university-of-the-witwatersrand-collections-api
- description: Top-level and sub-community containers
  name: University of the Witwatersrand Communities API
  slug: university-of-the-witwatersrand-communities-api
- description: Browse and search/discovery endpoints
  name: University of the Witwatersrand Discovery API
  slug: university-of-the-witwatersrand-discovery-api
- description: The institutions API from University of the Witwatersrand — 20 operation(s) for institutions.
  name: University of the Witwatersrand institutions API
  slug: university-of-the-witwatersrand-institutions-api
- description: Repository items (records)
  name: University of the Witwatersrand Items API
  slug: university-of-the-witwatersrand-items-api
- description: The oauth API from University of the Witwatersrand — 1 operation(s) for oauth.
  name: University of the Witwatersrand oauth API
  slug: university-of-the-witwatersrand-oauth-api
- description: The other API from University of the Witwatersrand — 7 operation(s) for other.
  name: University of the Witwatersrand other API
  slug: university-of-the-witwatersrand-other-api
- description: The profiles API from University of the Witwatersrand — 2 operation(s) for profiles.
  name: University of the Witwatersrand profiles API
  slug: university-of-the-witwatersrand-profiles-api
- description: The projects API from University of the Witwatersrand — 17 operation(s) for projects.
  name: University of the Witwatersrand projects API
  slug: university-of-the-witwatersrand-projects-api
- description: The Request API from University of the Witwatersrand — 1 operation(s) for request.
  name: University of the Witwatersrand Request API
  slug: university-of-the-witwatersrand-request-api
- description: HAL/JSON API root document
  name: University of the Witwatersrand Root API
  slug: university-of-the-witwatersrand-root-api
- description: The symplectic API from University of the Witwatersrand — 5 operation(s) for symplectic.
  name: University of the Witwatersrand symplectic API
  slug: university-of-the-witwatersrand-symplectic-api
artifact_total: 32
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-the-witwatersrand-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-the-witwatersrand-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-the-witwatersrand-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-the-witwatersrand-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.wits.ac.za/
- group: build
  title: ''
  type: Library
  url: https://www.wits.ac.za/library/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/WitsSoftDev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-the-witwatersrand/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-the-witwatersrand-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-the-witwatersrand-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-the-witwatersrand-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-the-witwatersrand-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-the-witwatersrand-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-the-witwatersrand-context.jsonld
created: '2026-06-03'
description: 'The University of the Witwatersrand (Wits) is a leading public research university in Johannesburg, South Africa, ranked #268 in the QS World University Rankings 2025. Wits does not operate a central, branded developer portal, but it exposes standards-based machine-readable interfaces through its library and open-research infrastructure. The most clearly public surfaces are the WIReDSpace institutional repository (DSpace 9.2), which offers both a REST API and an OAI-PMH metadata harvesting endpoint, and the Wits Open Data Vault, a Figshare-powered research data repository carrying DOIs for datasets. Other systems (Springshare LibGuides/LibCal, identity/SSO, and student services) are vendor-hosted and generally gated rather than openly documented.'
examples:
- key_count: 16
  name: University Of The Witwatersrand Getarticle Example
  slug: university-of-the-witwatersrand-getArticle-example
- key_count: 8
  name: University Of The Witwatersrand Getcommunity Example
  slug: university-of-the-witwatersrand-getCommunity-example
- key_count: 3
  name: University Of The Witwatersrand Oai Identify Example
  slug: university-of-the-witwatersrand-oai-identify-example
finops:
- name: University Of The Witwatersrand Finops
  service_category: Education
  slug: university-of-the-witwatersrand-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-the-witwatersrand.png
json_schemas:
- name: Figshare Article
  property_count: 16
  slug: university-of-the-witwatersrand-article
- name: WIReDSpace Community
  property_count: 8
  slug: university-of-the-witwatersrand-community
json_structures:
- name: University Of The Witwatersrand Article Structure
  property_count: 14
  slug: university-of-the-witwatersrand-article-structure
- name: University Of The Witwatersrand Community Structure
  property_count: 6
  slug: university-of-the-witwatersrand-community-structure
jsonld:
- class_count: 16
  name: University Of The Witwatersrand Context
  property_count: 5
  slug: university-of-the-witwatersrand-context
layout: provider
modified: '2026-06-03'
name: University of the Witwatersrand
nav: Providers
network: true
overview: 'University of the Witwatersrand publishes 15 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 12 more. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The University of the Witwatersrand catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of the Witwatersrand''s developer surface includes authentication, GitHub presence, and 13 more developer resources.'
plans:
- name: University Of The Witwatersrand Plans Pricing
  plan_count: 2
  slug: university-of-the-witwatersrand-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: University Of The Witwatersrand Rate Limits
  slug: university-of-the-witwatersrand-rate-limits
rules:
- name: University of the Witwatersrand API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-the-witwatersrand-jsonschema-spectral-rules
- name: University of the Witwatersrand API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: university-of-the-witwatersrand-rules
scopes:
- name: University Of The Witwatersrand Scopes
  scope_count: 1
  slug: university-of-the-witwatersrand-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 45.9
  delta: -5.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 72.7
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: University Of The Witwatersrand Authentication
  slug: university-of-the-witwatersrand-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: University Of The Witwatersrand Domain Security
  slug: university-of-the-witwatersrand-domain-security
  summary_line: TLSv1.2 · DMARC
slug: university-of-the-witwatersrand
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Library
- Institutional Repository
- South Africa
- Africa
website: https://www.wits.ac.za/
---
