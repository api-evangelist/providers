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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.7
  scored_at: '2026-09-01'
api_count: 12
apis:
- description: Campus location, building and room reference data. 3 operations, OAuth 2.0 client credentials, maintained by the DoIT EBS/IBS API team (locations-api@doit.wisc.edu).
  name: Locations API
  slug: locations-api
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
- description: The Academic Units API from University of Wisconsin-Madison — 2 operation(s) for academic units.
  name: University of Wisconsin-Madison Academic Units API
  slug: university-of-wisconsin-madison-academic-units-api
- description: The academicAppointments API from University of Wisconsin-Madison — 1 operation(s) for academicappointments.
  name: University of Wisconsin-Madison Academic Appointments API
  slug: university-of-wisconsin-madison-academicappointments-api
- description: The addresses API from University of Wisconsin-Madison — 1 operation(s) for addresses.
  name: University of Wisconsin-Madison Addresses API
  slug: university-of-wisconsin-madison-addresses-api
- description: The affiliations API from University of Wisconsin-Madison — 1 operation(s) for affiliations.
  name: University of Wisconsin-Madison Affiliations API
  slug: university-of-wisconsin-madison-affiliations-api
- description: The Aggregate API from University of Wisconsin-Madison — 1 operation(s) for aggregate.
  name: University of Wisconsin-Madison Aggregate API
  slug: university-of-wisconsin-madison-aggregate-api
- description: The Billing Batch Delete API from University of Wisconsin-Madison — 1 operation(s) for billing batch delete.
  name: University of Wisconsin-Madison Billing Batch Delete API
  slug: university-of-wisconsin-madison-billing-batch-delete-api
- description: The Billing Batch Information API from University of Wisconsin-Madison — 1 operation(s) for billing batch information.
  name: University of Wisconsin-Madison Billing Batch Information API
  slug: university-of-wisconsin-madison-billing-batch-information-api
- description: The Billing Batches API from University of Wisconsin-Madison — 1 operation(s) for billing batches.
  name: University of Wisconsin-Madison Billing Batches API
  slug: university-of-wisconsin-madison-billing-batches-api
- description: The BillingCustomers API from University of Wisconsin-Madison — 1 operation(s) for billingcustomers.
  name: University of Wisconsin-Madison Billing Customers API
  slug: university-of-wisconsin-madison-billingcustomers-api
- description: The Bulk Job Failed Results API from University of Wisconsin-Madison — 1 operation(s) for bulk job failed results.
  name: University of Wisconsin-Madison Bulk Job Failed Results API
  slug: university-of-wisconsin-madison-bulk-job-failed-results-api
- description: The Bulk Job Status API from University of Wisconsin-Madison — 1 operation(s) for bulk job status.
  name: University of Wisconsin-Madison Bulk Job Status API
  slug: university-of-wisconsin-madison-bulk-job-status-api
- description: The Bulkjob BillingTrans API from University of Wisconsin-Madison — 1 operation(s) for bulkjob billingtrans.
  name: University of Wisconsin-Madison Bulkjob BillingTrans API
  slug: university-of-wisconsin-madison-bulkjob-billingtrans-api
- description: The certificates API from University of Wisconsin-Madison — 2 operation(s) for certificates.
  name: University of Wisconsin-Madison Certificates API
  slug: university-of-wisconsin-madison-certificates-api
- description: The degrees API from University of Wisconsin-Madison — 1 operation(s) for degrees.
  name: University of Wisconsin-Madison Degrees API
  slug: university-of-wisconsin-madison-degrees-api
- description: The emailAddresses API from University of Wisconsin-Madison — 1 operation(s) for emailaddresses.
  name: University of Wisconsin-Madison Email Addresses API
  slug: university-of-wisconsin-madison-emailaddresses-api
- description: The exports API from University of Wisconsin-Madison — 2 operation(s) for exports.
  name: University of Wisconsin-Madison Exports API
  slug: university-of-wisconsin-madison-exports-api
- description: The groups API from University of Wisconsin-Madison — 3 operation(s) for groups.
  name: University of Wisconsin-Madison Groups API
  slug: university-of-wisconsin-madison-groups-api
- description: The identifiers API from University of Wisconsin-Madison — 1 operation(s) for identifiers.
  name: University of Wisconsin-Madison Identifiers API
  slug: university-of-wisconsin-madison-identifiers-api
- description: The jobs API from University of Wisconsin-Madison — 5 operation(s) for jobs.
  name: University of Wisconsin-Madison Jobs API
  slug: university-of-wisconsin-madison-jobs-api
- description: The Journals API from University of Wisconsin-Madison — 4 operation(s) for journals.
  name: University of Wisconsin-Madison Journals API
  slug: university-of-wisconsin-madison-journals-api
- description: The members API from University of Wisconsin-Madison — 2 operation(s) for members.
  name: University of Wisconsin-Madison Members API
  slug: university-of-wisconsin-madison-members-api
- description: The names API from University of Wisconsin-Madison — 2 operation(s) for names.
  name: University of Wisconsin-Madison Names API
  slug: university-of-wisconsin-madison-names-api
- description: The organizationStructures API from University of Wisconsin-Madison — 2 operation(s) for organizationstructures.
  name: University of Wisconsin-Madison Organization Structures API
  slug: university-of-wisconsin-madison-organizationstructures-api
- description: The Other API from University of Wisconsin-Madison — 32 operation(s) for other.
  name: University of Wisconsin-Madison Other API
  slug: university-of-wisconsin-madison-other-api
- description: The people API from University of Wisconsin-Madison — 2 operation(s) for people.
  name: University of Wisconsin-Madison People API
  slug: university-of-wisconsin-madison-people-api
- description: The phoneNumbers API from University of Wisconsin-Madison — 1 operation(s) for phonenumbers.
  name: University of Wisconsin-Madison Phone Numbers API
  slug: university-of-wisconsin-madison-phonenumbers-api
- description: The Research API from University of Wisconsin-Madison — 6 operation(s) for research.
  name: University of Wisconsin-Madison Research API
  slug: university-of-wisconsin-madison-research-api
- description: The Salary Structures API from University of Wisconsin-Madison — 2 operation(s) for salary structures.
  name: University of Wisconsin-Madison Salary Structures API
  slug: university-of-wisconsin-madison-salary-structures-api
- description: The socialSecurityNumbers API from University of Wisconsin-Madison — 1 operation(s) for socialsecuritynumbers.
  name: University of Wisconsin-Madison Social Security Numbers API
  slug: university-of-wisconsin-madison-socialsecuritynumbers-api
- description: The Standard Job Descriptions API from University of Wisconsin-Madison — 3 operation(s) for standard job descriptions.
  name: University of Wisconsin-Madison Standard Job Descriptions API
  slug: university-of-wisconsin-madison-standard-job-descriptions-api
- description: The Supervisory Organizations API from University of Wisconsin-Madison — 2 operation(s) for supervisory organizations.
  name: University of Wisconsin-Madison Supervisory Organizations API
  slug: university-of-wisconsin-madison-supervisory-organizations-api
- description: The Terms API from University of Wisconsin-Madison — 1 operation(s) for terms.
  name: University of Wisconsin-Madison Terms API
  slug: university-of-wisconsin-madison-terms-api
- description: The Token API from University of Wisconsin-Madison — 1 operation(s) for token.
  name: University of Wisconsin-Madison Token API
  slug: university-of-wisconsin-madison-token-api
- description: The UW Madison Public Course Search API API from University of Wisconsin-Madison — 1 operation(s) for uw madison public course search api.
  name: University of Wisconsin-Madison UW Madison Public Course Search API
  slug: university-of-wisconsin-madison-uw-madison-public-course-search-api-api
- description: The webhooks API from University of Wisconsin-Madison — 7 operation(s) for webhooks.
  name: University of Wisconsin-Madison Webhooks API
  slug: university-of-wisconsin-madison-webhooks-api
- description: The wiscard API from University of Wisconsin-Madison — 1 operation(s) for wiscard.
  name: University of Wisconsin-Madison Wiscard API
  slug: university-of-wisconsin-madison-wiscard-api
- description: The Worktags API from University of Wisconsin-Madison — 31 operation(s) for worktags.
  name: University of Wisconsin-Madison Worktags API
  slug: university-of-wisconsin-madison-worktags-api
artifact_total: 64
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/university-of-wisconsin-madison-capability-edges.yml
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
overview: 'University of Wisconsin-Madison publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Locations API, Academic Units API, Academic Appointments API, and 35 more. Tagged areas include University, Higher Education, Education, Public Research University, and United States.


  The University of Wisconsin-Madison catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Wisconsin-Madison''s developer surface includes documentation, authentication, status page, support, engineering blog, and 29 more developer resources.'
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
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 31.8
    contract_quality: 68.0
    developer_ergonomics: 35.7
    discoverability: 50.0
    governance: 31.8
    operational_transparency: 23.7
  previous_composite: 56.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 8.3
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 79.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
