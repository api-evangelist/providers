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
  name: Erasmus University Rotterdam Agentic Access
  operation_count: 157
  slug: erasmus-university-rotterdam-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: OAI-PMH 2.0 metadata harvesting interface for RePub, the Erasmus University institutional repository. Verified live; the Identify response self-reports as "Erasmus University OAIPMH Feed" and supports
  name: RePub OAI-PMH Metadata Feed
  slug: repub-oai
- description: 'OAI-PMH metadata service for the EUR & Erasmus MC Research Information Portal, which runs on Elsevier Pure (CRIS). The web portal resolves (HTTP 200) and the documented OAI service path is reachable; '
  name: Pure Research Portal OAI-PMH
  slug: pure-oai
- description: The altmetric API from Erasmus University Rotterdam — 1 operation(s) for altmetric.
  name: Erasmus University Rotterdam altmetric API
  slug: erasmus-university-rotterdam-altmetric-api
- description: The articles API from Erasmus University Rotterdam — 34 operation(s) for articles.
  name: Erasmus University Rotterdam articles API
  slug: erasmus-university-rotterdam-articles-api
- description: The authors API from Erasmus University Rotterdam — 2 operation(s) for authors.
  name: Erasmus University Rotterdam authors API
  slug: erasmus-university-rotterdam-authors-api
- description: The collections API from Erasmus University Rotterdam — 21 operation(s) for collections.
  name: Erasmus University Rotterdam collections API
  slug: erasmus-university-rotterdam-collections-api
- description: The institutions API from Erasmus University Rotterdam — 20 operation(s) for institutions.
  name: Erasmus University Rotterdam institutions API
  slug: erasmus-university-rotterdam-institutions-api
- description: The oauth API from Erasmus University Rotterdam — 1 operation(s) for oauth.
  name: Erasmus University Rotterdam oauth API
  slug: erasmus-university-rotterdam-oauth-api
- description: The other API from Erasmus University Rotterdam — 7 operation(s) for other.
  name: Erasmus University Rotterdam other API
  slug: erasmus-university-rotterdam-other-api
- description: The profiles API from Erasmus University Rotterdam — 2 operation(s) for profiles.
  name: Erasmus University Rotterdam profiles API
  slug: erasmus-university-rotterdam-profiles-api
- description: The projects API from Erasmus University Rotterdam — 17 operation(s) for projects.
  name: Erasmus University Rotterdam projects API
  slug: erasmus-university-rotterdam-projects-api
- description: The symplectic API from Erasmus University Rotterdam — 5 operation(s) for symplectic.
  name: Erasmus University Rotterdam symplectic API
  slug: erasmus-university-rotterdam-symplectic-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Figshare altmetric API
  slug: open-erasmus-university-rotterdam-altmetric-api
- collection_type: open
  name: Figshare altmetric articles API
  slug: open-erasmus-university-rotterdam-articles-api
- collection_type: open
  name: Figshare altmetric authors API
  slug: open-erasmus-university-rotterdam-authors-api
- collection_type: open
  name: Figshare altmetric collections API
  slug: open-erasmus-university-rotterdam-collections-api
- collection_type: open
  name: Figshare altmetric institutions API
  slug: open-erasmus-university-rotterdam-institutions-api
- collection_type: open
  name: Figshare altmetric oauth API
  slug: open-erasmus-university-rotterdam-oauth-api
- collection_type: open
  name: Figshare altmetric other API
  slug: open-erasmus-university-rotterdam-other-api
- collection_type: open
  name: Figshare altmetric profiles API
  slug: open-erasmus-university-rotterdam-profiles-api
- collection_type: open
  name: Figshare altmetric projects API
  slug: open-erasmus-university-rotterdam-projects-api
- collection_type: open
  name: Figshare altmetric symplectic API
  slug: open-erasmus-university-rotterdam-symplectic-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/erasmus-university-rotterdam-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/erasmus-university-rotterdam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/erasmus-university-rotterdam-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/erasmus-university-rotterdam-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/erasmus-university-rotterdam-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.eur.nl/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/eur-nl
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/erasmus-university-rotterdam/
- group: commercial
  title: ''
  type: Plans
  url: plans/erasmus-university-rotterdam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/erasmus-university-rotterdam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/erasmus-university-rotterdam-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Erasmus University Rotterdam (EUR) is a public research university in Rotterdam, the Netherlands, ranked #158 in the QS World University Rankings 2025. EUR does not operate a single consolidated public developer portal; its discoverable, programmatic surface is concentrated in scholarly and research-data infrastructure. RePub, the institutional repository, exposes a confirmed live OAI-PMH metadata feed, the EUR research data repository is hosted on Figshare (reachable via the Figshare public REST API), and the EUR & Erasmus MC research information portal runs on Pure (CRIS) with an OAI-PMH service path. Most course, timetable, identity, and administrative interfaces are gated behind institutional affiliation rather than openly documented.'
examples:
- key_count: 19
  name: Erasmus University Rotterdam Get Article Example
  slug: erasmus-university-rotterdam-get-article-example
- key_count: 6
  name: Erasmus University Rotterdam Search Articles Request Example
  slug: erasmus-university-rotterdam-search-articles-request-example
finops:
- name: Erasmus University Rotterdam Finops
  service_category: Education
  slug: erasmus-university-rotterdam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/erasmus-university-rotterdam.png
json_schemas:
- name: Figshare Article
  property_count: 16
  slug: erasmus-university-rotterdam-article
- name: Figshare Author
  property_count: 7
  slug: erasmus-university-rotterdam-author
- name: Figshare Collection
  property_count: 6
  slug: erasmus-university-rotterdam-collection
- name: Figshare Project
  property_count: 5
  slug: erasmus-university-rotterdam-project
json_structures:
- name: Erasmus University Rotterdam Article Structure
  property_count: 16
  slug: erasmus-university-rotterdam-article-structure
- name: Erasmus University Rotterdam Collection Structure
  property_count: 6
  slug: erasmus-university-rotterdam-collection-structure
- name: Erasmus University Rotterdam Project Structure
  property_count: 5
  slug: erasmus-university-rotterdam-project-structure
jsonld:
- class_count: 13
  name: Erasmus University Rotterdam Context
  property_count: 11
  slug: erasmus-university-rotterdam-context
layout: provider
modified: '2026-06-03'
name: Erasmus University Rotterdam
nav: Providers
network: true
overview: 'Erasmus University Rotterdam publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research Data, and Open Access.


  The Erasmus University Rotterdam catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Erasmus University Rotterdam''s developer surface includes authentication, GitHub presence, and 10 more developer resources.'
plans:
- name: Erasmus University Rotterdam Plans Pricing
  plan_count: 2
  slug: erasmus-university-rotterdam-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Erasmus University Rotterdam Rate Limits
  slug: erasmus-university-rotterdam-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Erasmus University Rotterdam API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: erasmus-university-rotterdam-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Erasmus University Rotterdam API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: erasmus-university-rotterdam-rules
scopes:
- name: Erasmus University Rotterdam Scopes
  scope_count: 1
  slug: erasmus-university-rotterdam-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 45.5
  delta: 3.8
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 25.0
    contract_quality: 66.2
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 41.7
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
    score: 61.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/erasmus-university-rotterdam/refs/heads/main/screenshots/erasmus-university-rotterdam-2026-06-20T180813.png
security:
- kind: authentication
  name: Erasmus University Rotterdam Authentication
  slug: erasmus-university-rotterdam-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Erasmus University Rotterdam Domain Security
  slug: erasmus-university-rotterdam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Erasmus University Rotterdam Vulnerability Disclosure
  slug: erasmus-university-rotterdam-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: erasmus-university-rotterdam
tags:
- Education
- Higher Education
- University
- Research Data
- Open Access
- Repository
- OAI-PMH
- Netherlands
website: https://www.eur.nl/en
---
