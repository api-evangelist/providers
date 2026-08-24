---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - openapi
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.7
  scored_at: '2026-08-24'
api_count: 16
apis:
- description: Authoritative person and identity data for UW-Madison — names, populations, affiliations, contact points, exports and webhooks. 47 operations over 31 paths, JSON:API envelopes, OAuth 2.0 client creden
  name: Person API
  slug: person-api
- description: Openly published mock of the Person API on mock.api.wisc.edu, mirroring all 47 operations so the contract and data shape are public even though production data is not. An unusually good practice for a
  name: Mock Person API
  slug: mock-person-api
- description: Certificate-authentication variant of the Mock Person API — 39 operations over 23 paths, published for testing the mTLS/certificate access path documented on the portal.
  name: Mock Person API (Certificates)
  slug: mock-person-api-certificates
- description: Institutional HR data — academic units, supervisory organizations, job profiles, positions and full-time-equivalent data, surfacing Workday-derived concepts under UW-Madison's own JSON:API contract. 9
  name: HR API
  slug: hr-api
- description: Openly published mock of the HR API on mock.api.wisc.edu, mirroring all 9 operations.
  name: Mock HR API
  slug: mock-hr-api
- description: Group and membership data for UW-Madison's Manifest service, backed by Internet2 Grouper Web Services. 5 operations, JSON:API, OAuth 2.0 client credentials, manual approval. Together with the Person A
  name: Manifest API
  slug: manifest-api
- description: Openly published mock of the Manifest API on mock.api.wisc.edu.
  name: Mock Manifest API
  slug: mock-manifest-api
- description: 'The largest contract in the estate — 73 operations covering sponsored research and financial administration: awards, award lines and tasks, grants, gifts, funds, cost centers, budget lines, billing sc'
  name: Finance API
  slug: finance-api
- description: Campus location, building and room reference data. 3 operations, OAuth 2.0 client credentials, maintained by the DoIT EBS/IBS API team (locations-api@doit.wisc.edu).
  name: Locations API
  slug: locations-api
- description: 'Service-provider billing transaction submission and lookup, backed by Salesforce. 7 operations. Recorded as published, with a defect noted honestly: the contract listed in the PRODUCTION portal declar'
  name: Enterprise Billing API
  slug: enterprise-billing-api
- description: The token endpoint for the whole gateway — POST https://api.wisc.edu/oauth/token, HTTP Basic presentation of client_id/client_secret, returning the bearer access token every other UW-Madison API requi
  name: OAuth API
  slug: oauth-api
- description: 'UW-Madison''s only openly callable API — the unauthenticated JSON search behind public.enroll.wisc.edu/search. Verified live on 2026-08-19: GET /terms returns the open term codes, GET /aggregate return'
  name: Public Course Search API
  slug: course-search-api
- description: Institution-operated Shibboleth IdP at login.wisc.edu, machine-readable on two protocols and almost never catalogued for a university. https://login.wisc.edu/idp/shibboleth returns SAML 2.0 metadata (
  name: UW-Madison Identity Provider (Shibboleth)
  slug: identity-federation
- description: Live OAI-PMH 2.0 harvesting endpoint for MINDS@UW, UW-Madison's institutional repository. Confirmed with ?verb=Identify — repositoryName 'MINDS@UW', protocolVersion 2.0, adminEmail dspace-help@library
  name: MINDS@UW OAI-PMH Endpoint
  slug: minds-oai-pmh
- description: UW-Madison's curricular data model (v1.5), published as generated Javadoc-style reference documentation on the DoIT WAMS host. Verified live and genuinely institution-operated, but it is reference doc
  name: Curricular Data Model
  slug: curricular-data-model
- description: UW-Madison's learning management system runs on an Instructure Canvas tenant at canvas.wisc.edu, gated behind the institution's own Shibboleth IdP — an unauthenticated request 302-redirects to login.w
  name: Canvas LMS (tenant)
  slug: canvas-lms
artifact_total: 38
common:
- group: company
  title: ''
  type: Website
  url: https://www.wisc.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wisc.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://kb.wisc.edu/uw-apis/
- group: build
  title: ''
  type: SourceCode
  url: https://git.doit.wisc.edu/interop/external-docs/api-publisher-documentation
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-wisconsin-madison-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-wisconsin-madison-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-wisconsin-madison-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-wisconsin-madison-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-wisconsin-madison-conformance.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-wisconsin-madison-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-wisconsin-madison-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-wisconsin-madison-context.jsonld
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.wisc.edu/idp/shibboleth
- group: learn
  title: ''
  type: CourseCatalog
  url: https://public.enroll.wisc.edu/search
- group: other
  title: ''
  type: ResearchRepository
  url: https://minds.wisc.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://search.library.wisc.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://chtc.cs.wisc.edu/
- group: other
  title: ''
  type: OpenData
  url: https://data.wisc.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://it.wisc.edu/ai/generative-ai-uw-madison-use-policies/
- group: build
  title: ''
  type: AITooling
  url: https://it.wisc.edu/ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UW-Madison-DoIT
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wisc.edu/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policy.wisc.edu/
- group: operate
  title: ''
  type: Status
  url: https://outages.doit.wisc.edu/
- group: operate
  title: ''
  type: Support
  url: https://kb.wisc.edu/
- group: company
  title: ''
  type: Blog
  url: https://news.wisc.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uw-madison/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/UWMadison
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-wisconsin-madison-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-wisconsin-madison-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-wisconsin-madison-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-wisconsin-madison-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Wisconsin-Madison is a public land-grant research university in Madison, Wisconsin, and one of the very few institutions in this cohort that genuinely operates an API program of its own rather than pointing at a vendor''s. Its Division of Information Technology (DoIT) runs a formal API Program on a UW-owned Google Apigee organization (doit-ipt-apigee-prod-ce29), fronted by a public developer portal at developer.wisc.edu, and publishes eleven OpenAPI 3.0 contracts — 245 operations across Person, HR, Manifest (Grouper groups), Finance, Locations, Enterprise Billing and OAuth — every one of them served from api.wisc.edu or mock.api.wisc.edu with a wisc.edu contact. Nothing in this repository is a vendor contract running under the institution''s name: there is no Figshare, Pure, Ex Libris, Dataverse or Symplectic surface attributed here. Beyond the gateway, UW-Madison operates a fully public unauthenticated course-search API at public.enroll.wisc.edu, its own
  Shibboleth identity provider at login.wisc.edu speaking both SAML 2.0 and OpenID Connect, and a live OAI-PMH 2.0 endpoint for the MINDS@UW institutional repository. The honest limits: production access is gated behind a manual institutional approval per API product and is effectively closed to anyone without a UW NetID, the estate declares zero OAuth scopes, no contract carries a license or terms of service, and the developer portal is a client-rendered single-page app that returns an identical 2,138-byte shell for every URL — including ones that do not exist. Learning management runs on a Canvas tenant, recorded here as a tenant relationship and not as UW-Madison engineering.'
examples:
- key_count: 4
  name: University Of Wisconsin Madison Course Search Aggregate Example
  slug: university-of-wisconsin-madison-course-search-aggregate-example
- key_count: 3
  name: University Of Wisconsin Madison Course Search Search Example
  slug: university-of-wisconsin-madison-course-search-search-example
- key_count: 3
  name: University Of Wisconsin Madison Course Search Terms Example
  slug: university-of-wisconsin-madison-course-search-terms-example
finops:
- name: University Of Wisconsin Madison Finops
  service_category: Education
  slug: university-of-wisconsin-madison-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-wisconsin-madison.png
json_schemas:
- name: UW-Madison Public Course Search API data model
  property_count: 0
  slug: university-of-wisconsin-madison-course-search-api
- name: Enterprise Billing API data model
  property_count: 0
  slug: university-of-wisconsin-madison-enterprise-billing-api
- name: HR API data model
  property_count: 0
  slug: university-of-wisconsin-madison-hr-api
- name: Locations API data model
  property_count: 0
  slug: university-of-wisconsin-madison-locations-api
- name: Manifest API data model
  property_count: 0
  slug: university-of-wisconsin-madison-manifest-api
- name: Mock HR API data model
  property_count: 0
  slug: university-of-wisconsin-madison-mock-hr-api
- name: Mock Manifest API data model
  property_count: 0
  slug: university-of-wisconsin-madison-mock-manifest-api
- name: Mock Person API data model
  property_count: 0
  slug: university-of-wisconsin-madison-mock-person-api-certificates
- name: Mock Person API data model
  property_count: 0
  slug: university-of-wisconsin-madison-mock-person-api
- name: OAuth data model
  property_count: 0
  slug: university-of-wisconsin-madison-oauth-api
- name: Person API data model
  property_count: 0
  slug: university-of-wisconsin-madison-person-api
jsonld:
- class_count: 13
  name: University Of Wisconsin Madison Context
  property_count: 3
  slug: university-of-wisconsin-madison-context
layout: provider
modified: '2026-08-19'
name: University of Wisconsin-Madison
nav: Providers
network: true
overview: 'University of Wisconsin-Madison publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Person API, Mock Person API, Mock Person API (Certificates), and 9 more. Tagged areas include University, Higher Education, Education, Public Research University, and United States.


  The University of Wisconsin-Madison catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Wisconsin-Madison''s developer surface includes documentation, authentication, status page, support, engineering blog, and 28 more developer resources.'
plans:
- name: University Of Wisconsin Madison Plans Pricing
  plan_count: 2
  slug: university-of-wisconsin-madison-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: University Of Wisconsin Madison Rate Limits
  slug: university-of-wisconsin-madison-rate-limits
rules:
- effective_rule_count: 10
  extends: []
  name: University of Wisconsin-Madison API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: university-of-wisconsin-madison-rules
scopes:
- name: University Of Wisconsin Madison Scopes
  scope_count: 0
  slug: university-of-wisconsin-madison-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.9
  delta: -0.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 63.7
    developer_ergonomics: 28.6
    discoverability: 55.6
    governance: 31.8
    operational_transparency: 23.7
  previous_composite: 52.2
  provenance:
    conformance: first-party
    contracts:
      callable: 91.7
      derived: 0
      marker_coverage: 8.3
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 79.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-wisconsin-madison/refs/heads/main/screenshots/university-of-wisconsin-madison-2026-06-20T200421.png
security:
- kind: authentication
  name: University Of Wisconsin Madison Authentication
  slug: university-of-wisconsin-madison-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: University Of Wisconsin Madison Domain Security
  slug: university-of-wisconsin-madison-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: university-of-wisconsin-madison
tags:
- University
- Higher Education
- Education
- Public Research University
- United States
- Wisconsin
- Big Ten
- Association of American Universities
- Identity
- Identity Federation
- Course Catalog
- Research Repository
- Student Information System
- Human Resources
- Finance
- Curriculum
website: https://www.wisc.edu/
---
