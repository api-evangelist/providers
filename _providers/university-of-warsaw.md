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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Warsaw Agentic Access
  operation_count: 8
  slug: university-of-warsaw-agentic-access
  summary_line: 8 operations
api_count: 3
apis:
- description: 'The University of Warsaw Research Data Repository (Dane Badawcze UW) is a Dataverse-based institutional repository for long-term storage and open sharing of research data across all disciplines, with '
  name: Dane Badawcze UW Research Data Repository REST API
  slug: rdr-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for the University of Warsaw Research Data Repository (Dataverse). The repository identifies itself as the "Dane Badawcze UW Dataverse OAI Archive" and support
  name: Dane Badawcze UW OAI-PMH Endpoint
  slug: rdr-oai-pmh
- baseURL: https://usosapps.uw.edu.pl/services/
  baseurl_source: declared
  description: Machine-readable method reference
  name: University of Warsaw apiref API
  slug: university-of-warsaw-apiref-api
- baseURL: https://usosapps.uw.edu.pl/services/
  baseurl_source: declared
  description: USOS API server information and time
  name: University of Warsaw apisrv API
  slug: university-of-warsaw-apisrv-api
- baseURL: https://usosapps.uw.edu.pl/services/
  baseurl_source: declared
  description: Academic calendar events
  name: University of Warsaw calendar API
  slug: university-of-warsaw-calendar-api
- baseURL: https://usosapps.uw.edu.pl/services/
  baseurl_source: declared
  description: Courses and course editions
  name: University of Warsaw courses API
  slug: university-of-warsaw-courses-api
- baseURL: https://usosapps.uw.edu.pl/services/
  baseurl_source: declared
  description: Faculties and organizational units
  name: University of Warsaw fac API
  slug: university-of-warsaw-fac-api
- baseURL: https://api.jaskier.uw.edu.pl
  baseurl_source: declared
  description: Jaskier is the University of Warsaw's central institutional data and services API — the backend behind MyUW and the university's in-house applications, built and operated by the university's own IT de
  name: Jaskier API
  slug: jaskier-api
- baseURL: https://api.sp4eu.uw.edu.pl
  baseurl_source: declared
  description: The REST API behind the Student Portal 4EU+, the shared student services portal of the 4EU+ European University Alliance, built and operated by the University of Warsaw. It publishes its own springdoc
  name: Student Portal 4EU+ API
  slug: sp4eu-api
- description: The Institutional Repository of the University of Warsaw (ReIn UW, Repozytorium Instytucjonalne Uniwersytetu Warszawskiego) runs DSpace-CRIS 8.1 (cris-2024.02.01) on the university's own host and expo
  name: ReIn UW Institutional Repository REST API
  slug: rein-uw-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for the Institutional Repository of the University of Warsaw. verb=Identify returns repositoryName "The Institutional Repository of the University of Warsaw (R
  name: ReIn UW OAI-PMH Endpoint
  slug: rein-uw-oai-pmh
- description: The university's own Shibboleth SAML 2.0 identity provider, entityID https://login.uw.edu.pl/idp, fronted by an Apereo CAS login at logowanie.uw.edu.pl. Its metadata is machine-readable at the entityI
  name: University of Warsaw SAML Identity Provider (eduGAIN / PIONIER.Id)
  slug: saml-idp
- description: 'The University of Warsaw registers DOIs through DataCite. Its DataCite provider is `repod` — "University of Warsaw – Interdisciplinary Centre for Mathematical and Computational Modelling", memberType '
  name: DataCite DOI Registration (REPOD / REPOD.DBUW)
  slug: datacite-membership
- description: The University of Warsaw is Crossref member 4211, holding 31 DOI prefixes used across its journals and press imprints (10.7311, 10.14394, 10.7172, 10.55226, 10.67180 and others). The membership is a f
  name: Crossref Membership (member 4211)
  slug: crossref-membership
- description: The Research Organization Registry record for the University of Warsaw, https://ror.org/039bjqg32, resolvable through the ROR API. It is the identifier the DataCite provider record for the university'
  name: ROR Registration (039bjqg32)
  slug: ror-registration
- description: The University of Warsaw Library (BUW) migrated off NUKAT to Ex Libris Alma with Primo discovery in December 2024, joining the national OMNIS shared catalogue. The discovery view is the institution-sp
  name: BUW Library Discovery (Ex Libris Alma / Primo, OMNIS)
  slug: buw-primo
- description: RepOD is Poland's general-purpose repository for open research data, running the same Dataverse build (1.3.2) as Dane Badawcze UW and operated by the Interdisciplinary Centre for Mathematical and Comp
  name: RepOD — Repository for Open Data (ICM UW)
  slug: repod
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USOS API (University of Warsaw) apiref API
  slug: open-university-of-warsaw-apiref-api
- collection_type: open
  name: USOS API (University of Warsaw) apiref apisrv API
  slug: open-university-of-warsaw-apisrv-api
- collection_type: open
  name: USOS API (University of Warsaw) apiref calendar API
  slug: open-university-of-warsaw-calendar-api
- collection_type: open
  name: USOS API (University of Warsaw) apiref courses API
  slug: open-university-of-warsaw-courses-api
- collection_type: open
  name: USOS API (University of Warsaw) apiref fac API
  slug: open-university-of-warsaw-fac-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/university-of-warsaw-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-warsaw-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-warsaw-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-warsaw-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://en.uw.edu.pl/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/icm-uw
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uniwersytet-warszawski
- group: start
  title: ''
  type: DeveloperPortal
  url: https://usosapps.uw.edu.pl/developers/
- group: auth
  title: ''
  type: Authentication
  url: https://usosapps.uw.edu.pl/developers/api/authorization/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-warsaw-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-warsaw-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-warsaw-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://en.uw.edu.pl/category/news/feed/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-warsaw-conformance.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://danebadawcze.uw.edu.pl/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repozytorium.uw.edu.pl/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://omnis-buw.primo.exlibrisgroup.com/discovery/search?vid=48OMNIS_UOW:48UOW
- group: learn
  title: ''
  type: CourseCatalog
  url: https://usosapps.uw.edu.pl/developers/api/services/courses/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.uw.edu.pl/idp
- group: other
  title: ''
  type: ResearchComputing
  url: https://kdm.icm.edu.pl/
- group: other
  title: ''
  type: AIPolicy
  url: https://urk.uw.edu.pl/wytyczne_sztuczna_inteligencja/
- group: docs
  title: ''
  type: Documentation
  url: https://usosapps.uw.edu.pl/developers/api/
- group: docs
  title: ''
  type: APIReference
  url: https://api.sp4eu.uw.edu.pl/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uw.edu.pl/informacja-o-przetwarzaniu-danych-osobowych/
- group: operate
  title: ''
  type: Support
  url: https://it.uw.edu.pl/pl/
created: '2026-06-03'
description: 'The University of Warsaw (Uniwersytet Warszawski) is Poland''s largest and highest-ranked university and a member of the 4EU+ European University Alliance. Unusually for this cohort it operates real first-party programmable surfaces rather than only vendor tenancies: the USOS API at usosapps.uw.edu.pl, a documented OAuth 1.0a REST-like protocol over the institution''s own academic database (courses, faculties, calendar, users, payments), and two springdoc services that publish their own OpenAPI and Swagger UI — the Student Portal 4EU+ API at api.sp4eu.uw.edu.pl (OpenAPI 3.1, 74 paths, read endpoints answer anonymously) and Jaskier at api.jaskier.uw.edu.pl, the university''s central institutional API (OpenAPI 3.0.1, 729 paths, 458 schemas, bearer-gated data). Research data is handled by two institution-hosted repositories — Dane Badawcze UW (Dataverse, DOI prefix 10.58132) and ReIn UW (DSpace-CRIS 8.1) — each with a native REST API and an OAI-PMH 2.0 endpoint. The university
  runs its own Shibboleth SAML identity provider at login.uw.edu.pl, registered in eduGAIN through the Polish PIONIER.Id federation, and it is a DataCite repository client and a Crossref member with 31 DOI prefixes. What it does NOT have is a single central developer portal: the USOS developers site is the only signup surface, the library discovery layer is an Ex Libris Alma/Primo tenancy, and the LMS is a Moodle install with no public LTI advertisement.'
examples:
- key_count: 2
  name: University Of Warsaw Course Error Example
  slug: university-of-warsaw-course-error-example
- key_count: 6
  name: University Of Warsaw Installation Example
  slug: university-of-warsaw-installation-example
- key_count: 2
  name: University Of Warsaw Now Example
  slug: university-of-warsaw-now-example
- key_count: 3
  name: University Of Warsaw Sp4Eu Tutorial Example
  slug: university-of-warsaw-sp4eu-tutorial-example
finops:
- name: University Of Warsaw Finops
  service_category: Education
  slug: university-of-warsaw-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-warsaw.png
json_schemas:
- name: USOS Course
  property_count: 14
  slug: university-of-warsaw-course
- name: USOS Faculty
  property_count: 9
  slug: university-of-warsaw-faculty
- name: USOS Installation
  property_count: 9
  slug: university-of-warsaw-installation
- name: Student Portal 4EU+ Course
  property_count: 32
  slug: university-of-warsaw-sp4eu-course
- name: Student Portal 4EU+ Tutorial
  property_count: 16
  slug: university-of-warsaw-sp4eu-tutorial
json_structures:
- name: University Of Warsaw Course Structure
  property_count: 9
  slug: university-of-warsaw-course-structure
- name: University Of Warsaw Installation Structure
  property_count: 9
  slug: university-of-warsaw-installation-structure
jsonld:
- class_count: 23
  name: University Of Warsaw Context
  property_count: 8
  slug: university-of-warsaw-context
layout: provider
modified: '2026-09-01'
name: University of Warsaw
nav: Providers
network: true
overview: 'University of Warsaw publishes 7 APIs on the [APIs.io](https://apis.io/) network, including apiref API, apisrv API, calendar API, and 4 more. Tagged areas include Education, Higher Education, University, Poland, and Europe.


  The University of Warsaw catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Warsaw''s developer surface includes authentication, GitHub presence, engineering blog, documentation, API reference, support, and 20 more developer resources.'
plans:
- name: University Of Warsaw Plans Pricing
  plan_count: 2
  slug: university-of-warsaw-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: University Of Warsaw Rate Limits
  slug: university-of-warsaw-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Warsaw API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-warsaw-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: University of Warsaw API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 4
  slug: university-of-warsaw-rules
score:
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 34.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.7
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 14.4
    contract_quality: 70.2
    developer_ergonomics: 45.2
    discoverability: 74.1
    governance: 14.4
    operational_transparency: 26.3
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 28.6
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 53.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-warsaw/refs/heads/main/screenshots/university-of-warsaw-2026-06-20T200305.png
security:
- kind: authentication
  name: University Of Warsaw Authentication
  slug: university-of-warsaw-authentication
  summary_line: apiKey/oauth1a/bearer/saml · 4 schemes
- kind: domain-security
  name: University Of Warsaw Domain Security
  slug: university-of-warsaw-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: university-of-warsaw
tags:
- Education
- Higher Education
- University
- Poland
- Europe
- 4EU+ Alliance
- Academic Data
- Course Catalog
- Research Data
- Research Repository
- Identity Federation
- Library
- Open Data
website: https://en.uw.edu.pl/
---
