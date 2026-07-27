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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Michigan State University Agentic Access
  operation_count: 6
  slug: michigan-state-university-agentic-access
  summary_line: 6 operations
api_count: 5
apis:
- description: OAI-PMH 2.0 metadata harvesting endpoint for the "Michigan State University Libraries Catalog" repository, exposing bibliographic metadata for harvesting.
  name: MSU Libraries Catalog OAI-PMH
  slug: catalog-oai
- description: OAI-PMH 2.0 metadata harvesting endpoint for the "MSU Libraries Digital Repository" (d.lib.msu.edu), exposing descriptive metadata for digital collections.
  name: MSU Libraries Digital Repository OAI-PMH
  slug: dlib-oai
- description: MSU's federated single sign-on service. The Shibboleth Identity Provider issues SAML 2.0 assertions and the institution also supports OAuth 2.0 for application authentication and authorization. Access
  name: MSU Identity Provider (Shibboleth / SAML / OAuth 2.0)
  slug: idp
- description: The Record API from Michigan State University — 3 operation(s) for record.
  name: Michigan State University Record API
  slug: michigan-state-university-record-api
- description: The Search API from Michigan State University — 3 operation(s) for search.
  name: Michigan State University Search API
  slug: michigan-state-university-search-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/michigan-state-university-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/michigan-state-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.msu.edu
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Michigan-State-University
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/MSU-Libraries
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/michigan-state-university/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tech.msu.edu/network/authentication-authorization/
- group: auth
  title: ''
  type: Authentication
  url: https://idp.idm.msu.edu/idp/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/michigan-state-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/michigan-state-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/michigan-state-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://msutoday.msu.edu/rss
created: '2026-06-03'
description: 'Michigan State University (MSU) is a public land-grant research university in East Lansing, Michigan, United States, ranked #89 in the QS World University Rankings 2025. Like most large research institutions, MSU does not operate a single consolidated public developer portal; its confirmed public API footprint is concentrated in the MSU Libraries platforms, which expose a VuFind REST API (OpenAPI 3.0) for the library catalog and OAI-PMH 2.0 endpoints for the catalog and the digital repository. Identity is provided through a Shibboleth/SAML Identity Provider with OAuth 2.0 support, and MSU maintains official GitHub organizations for the university and for MSU Libraries. Most administrative, student, and research-profile interfaces are gated behind institutional affiliation rather than offered as open self-service APIs.'
examples:
- key_count: 2
  name: Michigan State University Record Example
  slug: michigan-state-university-record-example
- key_count: 2
  name: Michigan State University Search Example
  slug: michigan-state-university-search-example
finops:
- name: Michigan State University Finops
  service_category: Education
  slug: michigan-state-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/michigan-state-university.png
json_schemas:
- name: MSU Libraries Catalog Record
  property_count: 35
  slug: michigan-state-university-record
- name: MSU Libraries Catalog Search Response
  property_count: 5
  slug: michigan-state-university-searchresponse
json_structures:
- name: Michigan State University Record Structure
  property_count: 31
  slug: michigan-state-university-record-structure
- name: Michigan State University Searchresponse Structure
  property_count: 5
  slug: michigan-state-university-searchresponse-structure
jsonld:
- class_count: 38
  name: Michigan State University Context
  property_count: 5
  slug: michigan-state-university-context
layout: provider
modified: '2026-06-03'
name: Michigan State University
nav: Providers
network: true
overview: 'Michigan State University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Record API and Search API. Tagged areas include Education, Higher Education, University, Library, and Open Data.


  The Michigan State University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Michigan State University''s developer surface includes GitHub presence, authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Michigan State University Plans Pricing
  plan_count: 2
  slug: michigan-state-university-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Michigan State University Rate Limits
  slug: michigan-state-university-rate-limits
rules:
- name: Michigan State University API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: michigan-state-university-jsonschema-spectral-rules
- name: Michigan State University API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 3
  slug: michigan-state-university-rules
score:
  band: thin
  composite: 43.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 48.7
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 43.4
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/michigan-state-university/refs/heads/main/screenshots/michigan-state-university-2026-06-20T185328.png
security:
- kind: domain-security
  name: Michigan State University Domain Security
  slug: michigan-state-university-domain-security
  summary_line: TLSv1.3 · DMARC
slug: michigan-state-university
tags:
- Education
- Higher Education
- University
- Library
- Open Data
- Metadata
- United States
- Michigan
website: https://www.msu.edu
---
