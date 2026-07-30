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
  name: Macquarie Agentic Access
  operation_count: 157
  slug: macquarie-agentic-access
  summary_line: 157 operations · 81 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: The Figshare-backed Research Data Repository exposes metadata for harvest via the OAI-PMH protocol through the Figshare OAI-PMH endpoint, supporting standards-based metadata harvesting of Macquarie re
  name: Macquarie University Research Data Repository (OAI-PMH)
  slug: rdr-oai-pmh
- description: The Macquarie University Library publishes public open-source utilities on GitHub that integrate with the Ex Libris Alma library services platform (for example an Alma toolkit and resource-sharing par
  name: Macquarie University Library Open-Source Tooling
  slug: library-alma-tools
- description: The altmetric API from Macquarie University — 1 operation(s) for altmetric.
  name: Macquarie University altmetric API
  slug: macquarie-altmetric-api
- description: The articles API from Macquarie University — 34 operation(s) for articles.
  name: Macquarie University articles API
  slug: macquarie-articles-api
- description: The authors API from Macquarie University — 2 operation(s) for authors.
  name: Macquarie University authors API
  slug: macquarie-authors-api
- description: The collections API from Macquarie University — 21 operation(s) for collections.
  name: Macquarie University collections API
  slug: macquarie-collections-api
- description: The institutions API from Macquarie University — 20 operation(s) for institutions.
  name: Macquarie University institutions API
  slug: macquarie-institutions-api
- description: The oauth API from Macquarie University — 1 operation(s) for oauth.
  name: Macquarie University oauth API
  slug: macquarie-oauth-api
- description: The other API from Macquarie University — 7 operation(s) for other.
  name: Macquarie University other API
  slug: macquarie-other-api
- description: The profiles API from Macquarie University — 2 operation(s) for profiles.
  name: Macquarie University profiles API
  slug: macquarie-profiles-api
- description: The projects API from Macquarie University — 17 operation(s) for projects.
  name: Macquarie University projects API
  slug: macquarie-projects-api
- description: The symplectic API from Macquarie University — 5 operation(s) for symplectic.
  name: Macquarie University symplectic API
  slug: macquarie-symplectic-api
artifact_total: 28
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/macquarie-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/macquarie-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/macquarie-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/macquarie-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.mq.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/macquarie-university
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mqlibrary
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/macquarie-university/
- group: auth
  title: ''
  type: Authentication
  url: https://idp.mq.edu.au/idp/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/macquarie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/macquarie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/macquarie-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Macquarie University is a public research university in Sydney, Australia, ranked #133 in the QS World University Rankings 2025. Its public, developer-relevant API footprint is concentrated in research-data and library infrastructure rather than a single branded developer portal. The Macquarie University Research Data Repository (RDR) runs on Figshare for Institutions, which exposes content through the public Figshare REST API v2 and an OAI-PMH metadata endpoint; the university Library maintains public open-source tooling on GitHub built around Ex Libris Alma. Authentication for institutional systems is provided via a Shibboleth/SAML identity provider. No dedicated, publicly documented Macquarie University developer portal or open-data API platform was found during this review.'
examples:
- key_count: 2
  name: Macquarie Author Example
  slug: macquarie-author-example
- key_count: 2
  name: Macquarie List Articles Example
  slug: macquarie-list-articles-example
finops:
- name: Macquarie Finops
  service_category: Education
  slug: macquarie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/macquarie.png
json_schemas:
- name: Figshare Article
  property_count: 16
  slug: macquarie-article
- name: Figshare Author
  property_count: 7
  slug: macquarie-author
json_structures:
- name: Macquarie Article Structure
  property_count: 16
  slug: macquarie-article-structure
- name: Macquarie Author Structure
  property_count: 7
  slug: macquarie-author-structure
jsonld:
- class_count: 18
  name: Macquarie Context
  property_count: 4
  slug: macquarie-context
layout: provider
modified: '2026-06-03'
name: Macquarie University
nav: Providers
network: true
overview: 'Macquarie University publishes 10 APIs on the [APIs.io](https://apis.io/) network, including altmetric API, articles API, authors API, and 7 more. Tagged areas include Education, Higher Education, University, Research Data, and Library.


  The Macquarie University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Macquarie University''s developer surface includes authentication, GitHub presence, and 11 more developer resources.'
plans:
- name: Macquarie Plans Pricing
  plan_count: 2
  slug: macquarie-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 1
  name: Macquarie Rate Limits
  slug: macquarie-rate-limits
rules:
- name: Macquarie University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: macquarie-jsonschema-spectral-rules
- name: Macquarie University API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: macquarie-rules
scopes:
- name: Macquarie Scopes
  scope_count: 1
  slug: macquarie-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 43.4
  delta: -4.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 74.1
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 47.7
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
screenshot: https://raw.githubusercontent.com/api-evangelist/macquarie/refs/heads/main/screenshots/macquarie-2026-06-20T184829.png
security:
- kind: authentication
  name: Macquarie Authentication
  slug: macquarie-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Macquarie Domain Security
  slug: macquarie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: macquarie
tags:
- Education
- Higher Education
- University
- Research Data
- Library
- Australia
website: https://www.mq.edu.au/
---
