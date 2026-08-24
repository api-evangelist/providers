---
access_model:
  confidence: high
  label: Free · Affiliate-gated, key issued on request
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - probes
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Johns Hopkins University Agentic Access
  operation_count: 7
  slug: johns-hopkins-university-agentic-access
  summary_line: 7 operations
api_count: 8
apis:
- description: REST API over the Hub database, the central repository of news articles, announcements, photo galleries, faculty experts and events at Johns Hopkins. Built to power hub.jhu.edu and reused across JHU s
  name: JHU Hub API
  slug: hub
- description: Course and section lookup and advanced search against the Self-Service Public Course Search API, which returns the Johns Hopkins course catalog as JSON. Filterable by school, department, course number
  name: Johns Hopkins University SIS Classes API
  slug: johns-hopkins-university-classes-api
- description: Reference code lists — schools, terms and departments — from the Self-Service Public Course Search API. The lookup vocabulary that makes the Classes API's filters usable. Requires an API key on the `k
  name: Johns Hopkins University SIS Codes API
  slug: johns-hopkins-university-codes-api
- description: Central API management platform built on MuleSoft Anypoint, where Johns Hopkins developers and consumers view and request access to enterprise integration APIs. The portal answers 200 but its asset ca
  name: JHU API Portal (MuleSoft Anypoint)
  slug: api-portal
- description: Johns Hopkins operates its own Shibboleth SAML 2.0 identity provider and publishes the entity metadata itself at login.jh.edu, scoped to johnshopkins.edu and jh.edu. The same identity is registered in
  name: Johns Hopkins Shibboleth Identity Provider
  slug: identity-federation
- description: 'Project MUSE, operated by Johns Hopkins University Press, exposes an OAI-PMH 2.0 harvesting endpoint that answers Identify, ListMetadataFormats, ListSets and ListRecords with no authentication at all '
  name: Project MUSE OAI-PMH Repository
  slug: project-muse-oai
- description: Institutional research data repository at archive.data.jhu.edu, administered by Johns Hopkins University Data Services within the Sheridan Libraries, running Dataverse software and minting DOIs throug
  name: Johns Hopkins Research Data Repository
  slug: research-data-repository
- description: 'The Johns Hopkins research information portal at pure.johnshopkins.edu, which CNAMEs to jhu.elsevierpure.com. This is an Elsevier Pure tenancy: the researcher profiles, publications and organizational'
  name: Johns Hopkins Research Portal (Elsevier Pure tenancy)
  slug: pure-research-portal
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Self-Service Public Course Search API (SIS) Classes API
  slug: open-johns-hopkins-university-classes-api
- collection_type: open
  name: Self-Service Public Course Search API (SIS) Classes Codes API
  slug: open-johns-hopkins-university-codes-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.jhu.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.jh.edu/
- group: docs
  title: ''
  type: APIReference
  url: https://api.hub.jhu.edu/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://sis.jhu.edu/api/help
- group: learn
  title: ''
  type: CourseCatalog
  url: https://sis.jhu.edu/api/help
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/johns-hopkins-university-identity-federation.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://archive.data.jhu.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.arch.jhu.edu/
- group: other
  title: ''
  type: OpenData
  url: https://dataservices.library.jhu.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://guides.library.jhu.edu/open-access/repositories
- group: other
  title: ''
  type: AIPolicy
  url: https://teaching.jhu.edu/university-teaching-policies/generative-ai/guidelines/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/johnshopkins
- group: build
  title: ''
  type: GitHub
  url: https://github.com/jhu-data-services
- group: build
  title: ''
  type: GitHub
  url: https://github.com/JHUAPL
- group: company
  title: ''
  type: Blog
  url: https://hub.jhu.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/johns-hopkins-university/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/johns-hopkins-university-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/johns-hopkins-university-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/johns-hopkins-university-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/johns-hopkins-university-education-standards-conformance.yml
- group: design
  title: ''
  type: Errors
  url: errors/johns-hopkins-university-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/johns-hopkins-university-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/johns-hopkins-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/johns-hopkins-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/johns-hopkins-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Johns Hopkins University is a private research university in Baltimore, Maryland, founded in 1876 and ranked #21 in the QS World University Rankings 2026. Its programmable footprint is small but real and, unusually for this cohort, it is genuinely its own: Johns Hopkins operates three APIs on hosts under its own registrable domains and publishes two live machine-readable identity artifacts. The Hub API (api.hub.jhu.edu) serves news, announcements, events, photo galleries and faculty experts from the Hub database across fifteen resource families, and the Self-Service Public Course Search API (sis.jhu.edu/api) returns course catalog data as JSON; both are documented in public but issue keys only to Johns Hopkins affiliates. A MuleSoft Anypoint portal at api.jh.edu fronts integration APIs and is gated entirely. Beyond those, the institution runs a Shibboleth SAML 2.0 identity provider whose metadata it publishes itself at login.jh.edu and which is registered in the InCommon Federation
  with Research and Scholarship and SIRTFI attributes; Project MUSE, operated by Johns Hopkins University Press, answers OAI-PMH 2.0 over 897,938 harvestable records with no authentication at all — the only fully open machine-readable surface the university has. The Johns Hopkins Research Data Repository (archive.data.jhu.edu) is Dataverse software administered by JHU Data Services, and the university''s research portal at pure.johnshopkins.edu is an Elsevier Pure tenancy: both hold Johns Hopkins data, and neither contract is Johns Hopkins engineering. No central public developer portal, no changelog, no deprecation policy and no working status page exist for any of it.'
examples:
- key_count: 3
  name: Johns Hopkins University Advanced Search Example
  slug: johns-hopkins-university-advanced-search-example
- key_count: 4
  name: Johns Hopkins University Hub Article Example
  slug: johns-hopkins-university-hub-article-example
- key_count: 3
  name: Johns Hopkins University Schools Example
  slug: johns-hopkins-university-schools-example
finops:
- name: Johns Hopkins University Finops
  service_category: Education
  slug: johns-hopkins-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/johns-hopkins-university.png
json_schemas:
- name: Course
  property_count: 36
  slug: johns-hopkins-university-course
json_structures:
- name: Johns Hopkins University Course Structure
  property_count: 36
  slug: johns-hopkins-university-course-structure
jsonld:
- class_count: 19
  name: Johns Hopkins University Context
  property_count: 4
  slug: johns-hopkins-university-context
layout: provider
modified: '2026-08-19'
name: Johns Hopkins University
nav: Providers
network: true
overview: 'Johns Hopkins University publishes 3 APIs on the [APIs.io](https://apis.io/) network: JHU Hub API, SIS Classes API, and SIS Codes API. Tagged areas include University, Higher Education, Education, United States, and Private Research University.


  The Johns Hopkins University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Johns Hopkins University''s developer surface includes API reference, documentation, GitHub presence, engineering blog, authentication, and 21 more developer resources.'
plans:
- name: Johns Hopkins University Plans Pricing
  plan_count: 2
  slug: johns-hopkins-university-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Johns Hopkins University Rate Limits
  slug: johns-hopkins-university-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Johns Hopkins University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: johns-hopkins-university-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Johns Hopkins University API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 2
  slug: johns-hopkins-university-rules
score:
  band: thin
  composite: 37.0
  delta: -0.4
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 64.3
    developer_ergonomics: 40.5
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/johns-hopkins-university/refs/heads/main/screenshots/johns-hopkins-university-2026-06-20T183755.png
security:
- kind: authentication
  name: Johns Hopkins University Authentication
  slug: johns-hopkins-university-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Johns Hopkins University Domain Security
  slug: johns-hopkins-university-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: johns-hopkins-university
tags:
- University
- Higher Education
- Education
- United States
- Private Research University
- Association of American Universities
- Research
- Research Data
- Course Catalog
- Identity Federation
- OAI-PMH
- Research Repository
- News
website: https://www.jhu.edu/
---
