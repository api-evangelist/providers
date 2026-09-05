---
access_model:
  confidence: high
  label: Free · Register an application client in the developer portal
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - authentication
  - probed
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://apis.auckland.ac.nz/courses/v3
  baseurl_source: declared
  description: Read-only access to the University of Auckland course catalogue, described by the University as "Exposes some course information by querying CS9 views" — CS9 being its PeopleSoft Campus Solutions inst
  name: University of Auckland Course Catalog Api V3
  slug: course-catalog-v3
- baseURL: https://apis.auckland.ac.nz/classes/v2
  baseurl_source: declared
  description: Search for scheduled class offerings at the University of Auckland — "Class API is intended to provide access to Class attributes, such as ID, Name, Description, Definition etc". A single GET /classes
  name: University of Auckland Classes Api V2
  slug: classes-v2
- description: Live OAI-PMH 2.0 metadata harvesting endpoint for ResearchSpace, the University's self-hosted DSpace institutional repository. Verified 2026-08-30 - Identify returns protocolVersion 2.0 and granularit
  name: ResearchSpace OAI-PMH 2.0 Service
  slug: researchspace-oai
- description: The HAL+JSON REST API of the University's self-hosted DSpace 7 instance. /server/api/core/communities returns the live community tree (A1 Research Outputs Online and its siblings) anonymously as appli
  name: ResearchSpace DSpace REST API
  slug: researchspace-rest
- description: The University's institutional identity provider, publishing SAML 2.0 metadata at https://iam.auckland.ac.nz/shibboleth (200, application/xml). The IDPSSODescriptor declares support for urn:oasis:name
  name: University of Auckland Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: identity-federation
- description: The University of Auckland's Figshare research data repository, a vendor tenancy on the Figshare platform (institution id 12). Live - the landing page returns HTTP 202 behind an AWS WAF challenge, and
  name: University of Auckland Figshare Research Data Repository (tenant)
  slug: figshare-tenant
- description: The University of Auckland Library's discovery layer, an Ex Libris Primo VE tenancy (vid=64UAUCK_INST:UOA, HTTP 200 verified 2026-08-30). No institution-published catalogue API or specification exists
  name: University of Auckland Library Discovery (Ex Libris Primo tenant)
  slug: primo-tenant
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.auckland.ac.nz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.auckland.ac.nz/prd/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.auckland.ac.nz/prd/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://developer.auckland.ac.nz/prd/guides
- group: build
  title: ''
  type: GitHub
  url: https://github.com/university-of-auckland
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UoA-eResearch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-auckland/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auckland.ac.nz/en/about-us/about-the-university/policy-hub/university-governance/privacy/privacy-policy.html
- group: other
  title: ''
  type: Copyright
  url: https://www.auckland.ac.nz/en/copyright.html
- group: other
  title: ''
  type: Policies
  url: https://www.auckland.ac.nz/en/about-us/about-the-university/policy-hub.html
- group: other
  title: ''
  type: ResearchRepository
  url: https://researchspace.auckland.ac.nz/
- group: other
  title: ''
  type: ResearchRepository
  url: https://auckland.figshare.com/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://auckland.primo.exlibrisgroup.com/discovery/search?vid=64UAUCK_INST:UOA
- group: other
  title: ''
  type: IdentityFederation
  url: https://iam.auckland.ac.nz/shibboleth
- group: learn
  title: ''
  type: CourseCatalog
  url: https://developer.auckland.ac.nz/prd/documentation/api-course-catalog-v3
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.eresearch.auckland.ac.nz/research-computing/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.auckland.ac.nz/en/about-us/about-the-university/policy-hub/research-innovation/doctoral-study/undertaking-research/generative-artificial-intelligence-in-doctoral-research-guidelines.html
- group: operate
  title: ''
  type: Support
  url: https://www.eresearch.auckland.ac.nz/getting-in-touch/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-auckland-course-catalog-v3-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-auckland-classes-v2-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-auckland-course-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-auckland-term-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-auckland-class-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/university-of-auckland-terms-list-example.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-auckland-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-auckland-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-auckland-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-auckland-lifecycle.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-auckland-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-auckland-vocabulary.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-auckland-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-auckland-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-auckland-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-auckland-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Waipapa Taumata Rau | The University of Auckland is New Zealand''s largest and highest-ranked university. Unlike most of this cohort it genuinely operates an API programme of its own: a Kong gateway at apis.auckland.ac.nz fronted by a public developer portal at developer.auckland.ac.nz, which publishes two OpenAPI 3.1.0 contracts — Course Catalog Api V3 and Classes Api V2 — over its PeopleSoft Campus Solutions (CS9) student records, plus guides for registering an application client and calling with the client-credentials flow. Both routes are live and return HTTP 401 without a key, so the contracts are public while the data is registered-developer only. The University also self-hosts ResearchSpace (DSpace) on its own domain with a live OAI-PMH 2.0 service advertising thirteen metadata formats, and runs its own Shibboleth identity provider at iam.auckland.ac.nz publishing SAML 2.0 metadata scoped to auckland.ac.nz. Its research data repository (auckland.figshare.com) and library
  discovery layer (Ex Libris Primo) are vendor tenancies: the data and the DOIs are the University''s, the contracts are not, and no vendor specification is saved under this slug. The previously catalogued unidirectory.auckland.ac.nz staff directory API no longer resolves in DNS and has been removed. There is no open data portal and no llms.txt, security.txt, status page, changelog or deprecation policy on any institution host.'
examples:
- key_count: 7
  name: University Of Auckland Terms List Example
  slug: university-of-auckland-terms-list-example
finops:
- name: University Of Auckland Finops
  service_category: Education
  slug: university-of-auckland-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-auckland.png
json_schemas:
- name: University of Auckland ClassModel
  property_count: 36
  slug: university-of-auckland-class
- name: University of Auckland Course
  property_count: 29
  slug: university-of-auckland-course
- name: University of Auckland Term
  property_count: 7
  slug: university-of-auckland-term
layout: provider
modified: '2026-08-30'
name: University of Auckland
nav: Providers
network: true
overview: 'University of Auckland publishes 2 APIs on the [APIs.io](https://apis.io/) network: Course Catalog Api V3 and Classes Api V2. Tagged areas include University, Higher Education, Education, New Zealand, and Public Research University.


  The University of Auckland catalog on APIs.io includes 1 Spectral governance ruleset.


  University of Auckland''s developer surface includes API reference, documentation, GitHub presence, support, code examples, authentication, and 29 more developer resources.'
plans:
- name: University Of Auckland Plans Pricing
  plan_count: 2
  slug: university-of-auckland-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: University Of Auckland Rate Limits
  slug: university-of-auckland-rate-limits
rules:
- effective_rule_count: 15
  extends: []
  name: University of Auckland API Rules
  rule_count: 15
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 9
  slug: university-of-auckland-rules
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 72.3
    catalog_earned_first_party: 8.0
    catalog_gap: 42.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 34.1
    contract_quality: 62.2
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 34.1
    operational_transparency: 23.7
  previous_composite: 46.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-auckland/refs/heads/main/screenshots/university-of-auckland-2026-06-20T200126.png
security:
- kind: authentication
  name: University Of Auckland Authentication
  slug: university-of-auckland-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: University Of Auckland Domain Security
  slug: university-of-auckland-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-auckland
tags:
- University
- Higher Education
- Education
- New Zealand
- Public Research University
- Universitas 21
- Course Catalog
- Student Records
- Research Data
- Research Repository
- Identity Federation
- OAI-PMH
website: https://www.auckland.ac.nz/
---
