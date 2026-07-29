---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Georgia Institute Of Technology Agentic Access
  operation_count: 14
  slug: georgia-institute-of-technology-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 5
apis:
- description: Public OAI-PMH 2.0 metadata harvesting interface for the Georgia Tech Digital Repository (DSpace 7), the institutional repository for theses, dissertations, publications, and other scholarly output. V
  name: GT Digital Repository OAI-PMH
  slug: repository-oai
- description: DSpace 7 REST API for the Georgia Tech Digital Repository, providing programmatic access to communities, collections, items, and bitstreams. The API root at /server/api responds HTTP 200 (public, read
  name: GT Digital Repository REST API
  slug: repository-rest
- description: Documented by the Georgia Tech Research Network Operations Center (RNOC), the GT Places API provides access to campus place information including offices and buildings with names, addresses, phone num
  name: GT Places API
  slug: gt-places
- description: Georgia Tech's enterprise integration API (BuzzAPI v3), operated by the Office of Information Technology at api.gatech.edu with a test environment at test.api.gatech.edu. Access requires institutional
  name: BuzzAPI
  slug: buzzapi
- description: The API API from Georgia Institute of Technology — 14 operation(s) for api.
  name: Georgia Institute of Technology API API
  slug: georgia-institute-of-technology-api-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/georgia-institute-of-technology-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/georgia-institute-of-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gatech.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/gatech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/georgia-institute-of-technology/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rnoc.gatech.edu/api
- group: build
  title: ''
  type: SourceCode
  url: https://ospo.cc.gatech.edu/github-resources/
- group: auth
  title: ''
  type: Authentication
  url: https://sso.gatech.edu/
- group: commercial
  title: ''
  type: Plans
  url: plans/georgia-institute-of-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/georgia-institute-of-technology-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/georgia-institute-of-technology-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Georgia Institute of Technology (Georgia Tech) is a public research university in Atlanta, Georgia, United States, ranked #114 in the QS World University Rankings 2025. Its public developer/API footprint is modest and partly gated: the Georgia Tech Library Digital Repository (DSpace 7) exposes a public OAI-PMH metadata interface and a public DSpace REST API, the Research Network Operations Center (RNOC) documents a public GT Places API for campus building and office data, and the Office of Information Technology operates the credentialed BuzzAPI (api.gatech.edu) plus CAS/Shibboleth single sign-on. The official open-source GitHub organization is github.com/gatech.'
examples:
- key_count: 2
  name: Georgia Institute Of Technology Getusernameandemailbybuzzcardnumber Example
  slug: georgia-institute-of-technology-GetUserNameAndEmailByBuzzCardNumber-example
- key_count: 2
  name: Georgia Institute Of Technology Whologgedin Example
  slug: georgia-institute-of-technology-WhoLoggedIn-example
finops:
- name: Georgia Institute Of Technology Finops
  service_category: Education
  slug: georgia-institute-of-technology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/georgia-institute-of-technology.png
json_schemas:
- name: SUMS Tool Record
  property_count: 19
  slug: georgia-institute-of-technology-tool
- name: SUMS TrainingInfo Record
  property_count: 7
  slug: georgia-institute-of-technology-traininginfo
- name: SUMS WhoLoggedIn Record
  property_count: 5
  slug: georgia-institute-of-technology-whologgedin
json_structures:
- name: Georgia Institute Of Technology Tool Structure
  property_count: 18
  slug: georgia-institute-of-technology-tool-structure
- name: Georgia Institute Of Technology Whologgedin Structure
  property_count: 5
  slug: georgia-institute-of-technology-whologgedin-structure
jsonld:
- class_count: 25
  name: Georgia Institute Of Technology Context
  property_count: 2
  slug: georgia-institute-of-technology-context
layout: provider
modified: '2026-06-03'
name: Georgia Institute of Technology
nav: Providers
network: true
overview: 'Georgia Institute of Technology publishes 1 API on the [APIs.io](https://apis.io/) network: API API. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Georgia Institute of Technology catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Georgia Institute of Technology''s developer surface includes GitHub presence, authentication, and 10 more developer resources.'
plans:
- name: Georgia Institute Of Technology Plans Pricing
  plan_count: 2
  slug: georgia-institute-of-technology-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Georgia Institute Of Technology Rate Limits
  slug: georgia-institute-of-technology-rate-limits
rules:
- name: Georgia Institute of Technology API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: georgia-institute-of-technology-jsonschema-spectral-rules
- name: Georgia Institute of Technology API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 4
  slug: georgia-institute-of-technology-rules
score:
  band: thin
  composite: 36.7
  delta: -4.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 44.3
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/georgia-institute-of-technology/refs/heads/main/screenshots/georgia-institute-of-technology-2026-06-20T181758.png
security:
- kind: domain-security
  name: Georgia Institute Of Technology Domain Security
  slug: georgia-institute-of-technology-domain-security
  summary_line: TLSv1.3 · DMARC
slug: georgia-institute-of-technology
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Library
- United States
website: https://www.gatech.edu/
---
