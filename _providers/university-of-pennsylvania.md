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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 30
  human_in_the_loop: 2
  name: University Of Pennsylvania Agentic Access
  operation_count: 68
  slug: university-of-pennsylvania-agentic-access
  summary_line: 68 operations · 30 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: 'One API, four student-facing products: Penn Course Alert (PCA), Penn Course Plan (PCP), Penn Course Review (PCR) and Penn Degree Plan (PDP), plus a shared Accounts resource. The live OpenAPI 3.0.2 doc'
  name: Penn Courses API (Penn Course Alert / Plan / Review / Degree Plan)
  slug: penn-courses
- description: JSON API behind Penn Clubs, the student-organization directory that Penn's Office of Student Affairs adopted as its official student-group registration system. /api/clubs returned HTTP 200 JSON anonym
  name: Penn Clubs API
  slug: penn-clubs
- description: Open-source Python client maintained by Penn Labs wrapping Penn data services. Published documentation at penn-sdk.readthedocs.io returned HTTP 200. An SDK is a client, not an institution-operated sur
  name: Penn SDK (Python)
  slug: penn-sdk-python
- description: 'Open-source JavaScript/Node client from Penn Labs. Documentation is hosted on js.org, a community subdomain service, at penn-sdk.js.org (HTTP 200) — a code/docs host, not a vendor platform, but not a '
  name: Penn SDK (JavaScript / Node)
  slug: penn-sdk-js
- description: Penn's Shibboleth identity provider publishes a signed SAML 2.0 EntityDescriptor at a well-known location (HTTP 200, application/xml, entityID https://idp.pennkey.upenn.edu/idp/shibboleth), carrying t
  name: PennKey Identity Provider — SAML 2.0 / Shibboleth Metadata
  slug: pennkey-identity-provider
- description: DSpace 7.6 HAL+JSON REST API on Penn's own host. The API root returned HTTP 200 advertising dspaceName "ScholarlyCommons at Penn" and the full DSpace link relation set; content endpoints require authe
  name: ScholarlyCommons at Penn — DSpace REST API
  slug: scholarlycommons-rest
- description: 'Penn Libraries'' digital repository at colenda.library.upenn.edu exposes a Blacklight/Solr JSON search response (/catalog.json returned HTTP 200, ~59 KB, anonymous). Institution-operated on Penn''s own '
  name: Colenda Digital Repository — Search JSON
  slug: colenda
- description: Penn Libraries' bulk open-data site publishing high-resolution manuscript images and TEI/XML descriptions in the public domain, laid out as a plainly-navigable directory tree (openn.library.upenn.edu/
  name: OPenn — Open Manuscript Data
  slug: openn
- description: Bibliographic search and record retrieval.
  name: University of Pennsylvania Catalog API
  slug: university-of-pennsylvania-catalog-api
- description: The Request API from University of Pennsylvania — 1 operation(s) for request.
  name: University of Pennsylvania Request API
  slug: university-of-pennsylvania-request-api
artifact_total: 52
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [Accounts] User API
  slug: open-university-of-pennsylvania-accounts-user-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCA] Registration API
  slug: open-university-of-pennsylvania-pca-registration-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCA] Registration History API
  slug: open-university-of-pennsylvania-pca-registration-history-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCP] Break API
  slug: open-university-of-pennsylvania-pcp-break-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCP] Calendar API
  slug: open-university-of-pennsylvania-pcp-calendar-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCP] Course Recommendations API
  slug: open-university-of-pennsylvania-pcp-course-recommendations-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCP] Primary Schedule API
  slug: open-university-of-pennsylvania-pcp-primary-schedule-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCP] Schedule API
  slug: open-university-of-pennsylvania-pcp-schedule-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCR] Autocomplete Dump API
  slug: open-university-of-pennsylvania-pcr-autocomplete-dump-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCR] Plots API
  slug: open-university-of-pennsylvania-pcr-plots-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCx] Attributes API
  slug: open-university-of-pennsylvania-pcx-attributes-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCx] Course API
  slug: open-university-of-pennsylvania-pcx-course-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCx] Friendship API
  slug: open-university-of-pennsylvania-pcx-friendship-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCx] Healths API
  slug: open-university-of-pennsylvania-pcx-healths-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCx] NGSS Restrictions API
  slug: open-university-of-pennsylvania-pcx-ngss-restrictions-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCx] Pre-NGSS Requirements API
  slug: open-university-of-pennsylvania-pcx-pre-ngss-requirements-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCx] Section API
  slug: open-university-of-pennsylvania-pcx-section-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PCx] Status Updates API
  slug: open-university-of-pennsylvania-pcx-status-updates-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PDP] Degree API
  slug: open-university-of-pennsylvania-pdp-degree-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PDP] Degree Plan Detail API
  slug: open-university-of-pennsylvania-pdp-degree-plan-detail-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PDP] Degree Plan Lists API
  slug: open-university-of-pennsylvania-pdp-degree-plan-lists-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PDP] Docked Course API
  slug: open-university-of-pennsylvania-pdp-docked-course-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PDP] Fulfillment API
  slug: open-university-of-pennsylvania-pdp-fulfillment-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PDP] Onboard From Transcript API
  slug: open-university-of-pennsylvania-pdp-onboard-from-transcript-api
- collection_type: open
  name: Penn Courses API Documentation [Accounts] User [Accounts] User [PDP] Satisfied Rule Lists API
  slug: open-university-of-pennsylvania-pdp-satisfied-rule-lists-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.upenn.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upenn
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pennlabs
- group: docs
  title: ''
  type: Documentation
  url: https://pennlabs.org/resources/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upenn.edu/about/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://penntoday.upenn.edu/rss.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-pennsylvania/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.pennkey.upenn.edu/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.upenn.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://find.library.upenn.edu/
- group: other
  title: ''
  type: OpenData
  url: https://openn.library.upenn.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.upenn.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.med.upenn.edu/pmacs/
- group: other
  title: ''
  type: AIPolicy
  url: https://isc.upenn.edu/security/AI-guidance
- group: build
  title: ''
  type: AITooling
  url: https://cetli.upenn.edu/resources/generative-ai/penn-ai-guidance-and-policies/
- group: company
  title: ''
  type: About
  url: https://www.library.upenn.edu/about/policies/open-metadata
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-pennsylvania-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-pennsylvania-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-pennsylvania-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-pennsylvania-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-pennsylvania-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-conformance
  url: conformance/university-of-pennsylvania-conformance.yml
- group: auth
  title: ''
  type: x-authentication
  url: authentication/university-of-pennsylvania-authentication.yml
- group: design
  title: ''
  type: x-errors
  url: errors/university-of-pennsylvania-errors.yml
- group: design
  title: ''
  type: x-lifecycle
  url: lifecycle/university-of-pennsylvania-lifecycle.yml
created: '2026-06-03'
description: 'The University of Pennsylvania (Penn) is a private Ivy League research university in Philadelphia. Penn operates no central developer portal and publishes no institution-wide API program, and the surface that the 2026-06-03 profile treated as its headline API — the Penn OpenData API on the ISC enterprise service bus — is retired: the host esb.isc-seo.upenn.edu no longer resolves and its documentation page returns a soft-404. What Penn genuinely operates is library and identity infrastructure: the PennKey Shibboleth identity provider, whose signed SAML 2.0 metadata resolves live in the InCommon federation; ScholarlyCommons at Penn, a DSpace 7.6 repository on Penn''s own domain serving a conformant OAI-PMH 2.0 endpoint over real Penn records; the Franklin catalog and the Colenda digital repository, both Blacklight applications with JSON twins on every page under Penn Libraries'' published open-metadata policy; and OPenn, a bulk open-data site of manuscript images and TEI descriptions.
  The far larger and better known surface — Penn Course Alert, Penn Course Plan, Penn Course Review, Penn Degree Plan and Penn Clubs, with a live 45-path OpenAPI at penncourseplan.com/api/openapi/ — is NOT operated by the university. It is built and run by Penn Labs, a non-profit student-run software organization, on domains registered to Penn Labs. Penn''s Office of Student Affairs adopted Penn Clubs as its official student-group registry, which is institutional endorsement of the product, not institutional operation of the API. Those surfaces are recorded here as tenant relationships so the relationship is preserved without crediting Penn for engineering it did not do.'
examples:
- key_count: 2
  name: University Of Pennsylvania Course Detail Example
  slug: university-of-pennsylvania-course-detail-example
- key_count: 2
  name: University Of Pennsylvania Section Detail Example
  slug: university-of-pennsylvania-section-detail-example
finops:
- name: University Of Pennsylvania Finops
  service_category: Education
  slug: university-of-pennsylvania-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-pennsylvania.png
json_schemas:
- name: CourseDetail
  property_count: 16
  slug: university-of-pennsylvania-course
- name: Schedule
  property_count: 7
  slug: university-of-pennsylvania-schedule
- name: SectionDetail
  property_count: 14
  slug: university-of-pennsylvania-section
json_structures:
- name: University Of Pennsylvania Course Structure
  property_count: 11
  slug: university-of-pennsylvania-course-structure
- name: University Of Pennsylvania Section Structure
  property_count: 8
  slug: university-of-pennsylvania-section-structure
jsonld:
- class_count: 18
  name: University Of Pennsylvania Context
  property_count: 5
  slug: university-of-pennsylvania-context
layout: provider
modified: '2026-08-19'
name: University of Pennsylvania
nav: Providers
network: true
overview: 'University of Pennsylvania publishes 3 APIs on the [APIs.io](https://apis.io/) network: Penn Courses API (Penn Course Alert / Plan / Review / Degree Plan), Catalog API, and Request API. Tagged areas include Education, Higher Education, University, Research University, and Ivy League.


  The University of Pennsylvania catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Pennsylvania''s developer surface includes documentation, engineering blog, and 24 more developer resources.'
plans:
- name: University Of Pennsylvania Plans Pricing
  plan_count: 2
  slug: university-of-pennsylvania-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: University Of Pennsylvania Rate Limits
  slug: university-of-pennsylvania-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Pennsylvania API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-pennsylvania-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: University of Pennsylvania API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 3
  slug: university-of-pennsylvania-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 13.6
    contract_quality: 54.2
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 23.7
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 6.5
      total: 31
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 35.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-pennsylvania/refs/heads/main/screenshots/university-of-pennsylvania-2026-06-20T200220.png
security:
- kind: authentication
  name: University Of Pennsylvania Authentication
  slug: university-of-pennsylvania-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Pennsylvania Domain Security
  slug: university-of-pennsylvania-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-pennsylvania
tags:
- Education
- Higher Education
- University
- Research University
- Ivy League
- United States
- Philadelphia
- Open Data
- Library
- Course Catalog
- Research Repository
- Identity Federation
- OAI-PMH
- Student Developers
website: https://www.upenn.edu/
---
