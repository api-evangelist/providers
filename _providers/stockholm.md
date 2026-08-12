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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 81
  human_in_the_loop: 2
  name: Stockholm Agentic Access
  operation_count: 157
  slug: stockholm-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: Stockholm University participates in DiVA (Academic Archive On-line), the shared Swedish publishing system and digital archive for research and student publications. DiVA exposes bibliographic metadat
  name: DiVA Institutional Repository (OAI-PMH)
  slug: diva-oai
- description: Open-source utility from the Stockholm University GitHub organization that generates Shibboleth SP/SAML2 metadata X.509 certificates and keys and stores them (e.g. in HashiCorp Vault). Reflects the un
  name: shib-keygen-api (Shibboleth SP Metadata Tooling)
  slug: shib-keygen-api
- description: The altmetric API from Stockholm University — 1 operation(s) for altmetric.
  name: Stockholm University altmetric API
  slug: stockholm-altmetric-api
- description: The articles API from Stockholm University — 34 operation(s) for articles.
  name: Stockholm University articles API
  slug: stockholm-articles-api
- description: The authors API from Stockholm University — 2 operation(s) for authors.
  name: Stockholm University authors API
  slug: stockholm-authors-api
- description: The collections API from Stockholm University — 21 operation(s) for collections.
  name: Stockholm University collections API
  slug: stockholm-collections-api
- description: The institutions API from Stockholm University — 20 operation(s) for institutions.
  name: Stockholm University institutions API
  slug: stockholm-institutions-api
- description: The oauth API from Stockholm University — 1 operation(s) for oauth.
  name: Stockholm University oauth API
  slug: stockholm-oauth-api
- description: The other API from Stockholm University — 7 operation(s) for other.
  name: Stockholm University other API
  slug: stockholm-other-api
- description: The profiles API from Stockholm University — 2 operation(s) for profiles.
  name: Stockholm University profiles API
  slug: stockholm-profiles-api
- description: The projects API from Stockholm University — 17 operation(s) for projects.
  name: Stockholm University projects API
  slug: stockholm-projects-api
- description: The symplectic API from Stockholm University — 5 operation(s) for symplectic.
  name: Stockholm University symplectic API
  slug: stockholm-symplectic-api
artifact_total: 30
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stockholm-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stockholm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stockholm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stockholm-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stockholm-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.su.se/english/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/stockholmuniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/stockholm-university/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/stockholmuniversity
- group: auth
  title: ''
  type: Authentication
  url: https://www.swamid.se/
- group: commercial
  title: ''
  type: Plans
  url: plans/stockholm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stockholm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stockholm-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Stockholm University (Stockholms universitet) is a public research university in Sweden, ranked #128 in the QS World University Rankings 2025. Like most Nordic public universities, it does not operate a single consolidated developer portal; its public, machine-readable footprint is distributed across standards-based and third-party services. Confirmed interfaces include the DiVA institutional repository OAI-PMH metadata endpoint, the Figshare-hosted research data repository (su.figshare.com) backed by the Figshare public REST API, and the public GitHub organization (stockholmuniversity) where IT operations and infrastructure tooling is maintained. Identity is federated through SWAMID/Shibboleth (SAML2), reflected in the org''s shib-keygen-api project. No general-purpose open course or student-information API was found publicly documented.'
examples:
- key_count: 2
  name: Stockholm Article Detail Example
  slug: stockholm-article-detail-example
- key_count: 2
  name: Stockholm List Articles Example
  slug: stockholm-list-articles-example
finops:
- name: Stockholm Finops
  service_category: Education
  slug: stockholm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stockholm.png
json_schemas:
- name: Figshare Article
  property_count: 19
  slug: stockholm-article
- name: Figshare Author
  property_count: 7
  slug: stockholm-author
- name: Figshare Collection
  property_count: 6
  slug: stockholm-collection
json_structures:
- name: Stockholm Article Structure
  property_count: 15
  slug: stockholm-article-structure
- name: Stockholm Author Structure
  property_count: 7
  slug: stockholm-author-structure
jsonld:
- class_count: 16
  name: Stockholm Context
  property_count: 11
  slug: stockholm-context
layout: provider
modified: '2026-06-03'
name: Stockholm University
nav: Providers
network: true
overview: 'Stockholm University publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Stockholm University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stockholm University''s developer surface includes authentication, GitHub presence, and 12 more developer resources.'
plans:
- name: Stockholm Plans Pricing
  plan_count: 2
  slug: stockholm-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 1
  name: Stockholm Rate Limits
  slug: stockholm-rate-limits
rules:
- name: Stockholm University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: stockholm-jsonschema-spectral-rules
- name: Stockholm University API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 3
  slug: stockholm-rules
scopes:
- name: Stockholm Scopes
  scope_count: 1
  slug: stockholm-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 43.3
  delta: -0.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 73.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stockholm/refs/heads/main/screenshots/stockholm-2026-06-20T194559.png
security:
- kind: authentication
  name: Stockholm Authentication
  slug: stockholm-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Stockholm Domain Security
  slug: stockholm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stockholm Vulnerability Disclosure
  slug: stockholm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: stockholm
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Repository
- Sweden
- Europe
website: https://www.su.se/english/
---
