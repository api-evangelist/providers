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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 25.9
  scored_at: '2026-08-26'
api_count: 7
apis:
- description: Live OAI-PMH 2.0 metadata harvesting endpoint for Deep Blue Documents, the University of Michigan Library's DSpace institutional repository of articles, dissertations, theses and archival collections.
  name: Deep Blue Documents OAI-PMH
  slug: deep-blue-documents-oai
- description: The University of Michigan's own Shibboleth SAML 2.0 identity provider, and the most unambiguously institution-operated machine-readable surface U-M publishes. GET https://shibboleth.umich.edu/idp/shi
  name: U-M Shibboleth Identity Provider (InCommon)
  slug: shibboleth-idp
- description: Enterprise API directory and gateway operated by U-M Information and Technology Services on Google Apigee X (migrated from IBM API Connect v5 in 2024), exposing institutional data APIs across teaching
  name: U-M ITS API Directory
  slug: api-directory
- description: Public REST API for Deep Blue Data, the University of Michigan Library's open repository for research datasets produced by U-M researchers, with DataCite DOI persistent identifiers. Documented publicl
  name: Deep Blue Data REST API
  slug: deep-blue-data
- description: Real-time campus transit API for U-M's Magic Bus service, served from a U-M host on Clever Devices BusTime. Live and gated by an API access key — GET /bustime/api/v3/getroutes and /bustime/api/v3/gett
  name: Magic Bus (U-M Transit) BusTime API
  slug: magic-bus
- description: 'Materials-science data repository for storing, sharing and publishing research datasets and workflows, operated by the PRISMS Center at the University of Michigan. It advertises a CLI and an API, but '
  name: Materials Commons
  slug: materials-commons
- description: The University of Michigan's Canvas learning management system tenancy. The courses, the enrollments and the data are U-M's; the API contract is Instructure's, published once for every Canvas customer
  name: Canvas LMS (U-M tenancy on Instructure)
  slug: canvas-lms
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://umich.edu
- group: company
  title: ''
  type: Website
  url: https://www.lib.umich.edu
- group: start
  title: ''
  type: DeveloperPortal
  url: https://its.umich.edu/data/data-database/api-directory
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.its.umich.edu/api-directory
- group: operate
  title: ''
  type: Support
  url: https://its.umich.edu/data/data-database/api-directory/support
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-michigan-ann-arbor-authentication.yml
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibboleth.umich.edu/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/https%3A%2F%2Fshibboleth.umich.edu%2Fidp%2Fshibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.lib.umich.edu/collections/deep-blue-repositories
- group: other
  title: ''
  type: ResearchRepository
  url: https://deepblue.lib.umich.edu/data/rest-api
- group: build
  title: ''
  type: LibraryCatalog
  url: https://search.lib.umich.edu
- group: learn
  title: ''
  type: CourseCatalog
  url: https://atlas.ai.umich.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://arc.umich.edu/
- group: build
  title: ''
  type: AITooling
  url: https://genai.umich.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://safecomputing.umich.edu/information-security-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lib.umich.edu/about-us/policies/library-privacy-statement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/umich
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mlibrary
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/umich-iam
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/umich-arc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-michigan/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-michigan-ann-arbor-deep-blue-documents-oai-pmh-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-michigan-ann-arbor-oai-pmh-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/deep-blue-documents-oai-identify.xml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-michigan-ann-arbor-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-michigan-ann-arbor-rules.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/university-of-michigan-ann-arbor-errors.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-michigan-ann-arbor-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-michigan-ann-arbor-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-michigan-ann-arbor-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-michigan-ann-arbor-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-michigan-ann-arbor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-michigan-ann-arbor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-michigan-ann-arbor-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-michigan-ann-arbor-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
coverage:
  detail: 'U-M''s programmable footprint is real and mostly unreachable, for two different reasons that must not be conflated. FIRST, and this is the finding about the institution: the enterprise API estate — MCommunity, Schedule of Classes, class rosters, room scheduling — lives in the ITS API Directory on Apigee X and requires a U-M uniqname, Duo two-factor authentication and U-M network/VPN presence to even browse. There is no public developer registration path, so no endpoint in it could be probed or described, and none has been. SECOND, and this is a limit on us rather than on them: most of the umich.edu estate sits behind a Cloudflare managed challenge and returns HTTP 403 "Just a moment..." to automated clients — umich.edu, its.umich.edu, documentation.its.umich.edu, deepblue.lib.umich.edu, search.lib.umich.edu, arc.umich.edu, genai.umich.edu, safecomputing.umich.edu, ro.umich.edu and www.icpsr.umich.edu among them. Those pointers are live and real; they are just not readable by us,
    and they should be re-probed with a browser-grade client. Deep Blue Data in particular is a documented public REST API that we could not read, so no contract was written for it. What WAS fully readable is genuinely U-M''s and is described here in full: the Deep Blue Documents OAI-PMH endpoint (all six verbs, twelve metadata formats, 726 sets, four error codes reproduced) and the U-M Shibboleth SAML 2.0 identity provider registered in InCommon. One vendor tenancy is recorded rather than absorbed: Canvas at umich.instructure.com. A suspected Figshare tenancy at umich.figshare.com was REJECTED — a nonsense control subdomain returns the identical AWS WAF 202, so the response is a wildcard artefact and not evidence of a U-M account.'
  evidence:
  - status: 200
    url: https://backend.production.deepblue-documents.lib.umich.edu/server/oai/request?verb=Identify
  - status: 200
    url: https://backend.production.deepblue-documents.lib.umich.edu/server/oai/request?verb=ListMetadataFormats
  - status: 200
    url: https://backend.production.deepblue-documents.lib.umich.edu/server/oai/request?verb=ListSets
  - status: 200
    url: https://backend.production.deepblue-documents.lib.umich.edu/server/oai/request?verb=GetRecord&identifier=oai:deepblue.lib.umich.edu:2027.42/61022&metadataPrefix=oai_dc
  - status: 200
    url: https://shibboleth.umich.edu/idp/shibboleth
  - status: 200
    url: https://mdq.incommon.org/entities/https%3A%2F%2Fshibboleth.umich.edu%2Fidp%2Fshibboleth
  - status: 200
    url: https://api.datacite.org/providers/umich
  - status: 200
    url: https://mbus.ltp.umich.edu/bustime/api/v3/getroutes
  - status: 401
    url: https://umich.instructure.com/api/v1/accounts
  - status: 404
    url: https://zzznotarealtenant.instructure.com/api/v1/accounts
  - status: 202
    url: https://umich.figshare.com/
  - status: 202
    url: https://zzznotarealtenant.figshare.com/
  - status: 200
    url: https://www.lib.umich.edu
  - status: 200
    url: https://atlas.ai.umich.edu/
  - status: 200
    url: https://materialscommons.org/
  - status: 200
    url: https://github.com/umich-iam
  - status: 403
    url: https://its.umich.edu/data/data-database/api-directory
  - status: 403
    url: https://deepblue.lib.umich.edu/data/rest-api
  - status: 403
    url: https://umich.edu
  - status: 403
    url: https://arc.umich.edu/
  - status: 403
    url: https://genai.umich.edu/
  - status: 0
    url: https://api.umich.edu/
  reason: institution_api_estate_behind_sso
  state: gated
created: '2026-06-03'
description: 'The University of Michigan-Ann Arbor is a public research university (QS World University Rankings 2025 #20-21, United States), a member of the Association of American Universities and the Big Ten Academic Alliance. Its programmable footprint is large in aggregate and almost entirely closed to the public. The enterprise estate — MCommunity directory, Schedule of Classes, class rosters, room scheduling and other institutional data — sits behind the U-M ITS API Directory on Google Apigee X, which cannot be browsed, let alone called, without a U-M uniqname, Duo two-factor authentication and presence on the U-M network or VPN. What is genuinely open and genuinely U-M''s own is library and identity infrastructure: the Deep Blue Documents DSpace repository publishes a fully working OAI-PMH 2.0 harvesting endpoint on a umich.edu host (all six verbs verified live, twelve metadata formats, 726 sets, records back to 2005), and U-M ITS Identity and Access Management operates its own Shibboleth
  SAML 2.0 identity provider registered in InCommon, with public SAML and OIDC integration examples on GitHub. U-M Library is a DataCite direct member (symbol UMICH, five repositories) and a Crossref member (prefix 10.3998). Around those sit smaller institution-run surfaces — the Magic Bus transit API and Deep Blue Data — and one large vendor tenancy, Canvas at umich.instructure.com, whose contract belongs to Instructure and is not stored here. U-M publishes no public developer portal, no OpenAPI, no changelog and no API terms of service. Most of the umich.edu estate returns a Cloudflare bot challenge to automated clients, so several pointers below are documented-and-live rather than machine-readable.'
finops:
- name: University Of Michigan Ann Arbor Finops
  service_category: Education
  slug: university-of-michigan-ann-arbor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-michigan-ann-arbor.png
json_schemas:
- name: Deep Blue Documents OAI-PMH Response
  property_count: 10
  slug: university-of-michigan-ann-arbor-oai-pmh
jsonld:
- class_count: 28
  name: University Of Michigan Ann Arbor Context
  property_count: 1
  slug: university-of-michigan-ann-arbor-context
layout: provider
modified: '2026-08-19'
name: University of Michigan-Ann Arbor
nav: Providers
network: true
overview: 'University of Michigan-Ann Arbor publishes 1 API on the [APIs.io](https://apis.io/) network: Deep Blue Documents OAI-PMH. Tagged areas include University, Higher Education, Education, Public Research University, and United States.


  The University of Michigan-Ann Arbor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Michigan-Ann Arbor''s developer surface includes documentation, support, authentication, code examples, engineering blog, and 32 more developer resources.'
plans:
- name: University Of Michigan Ann Arbor Plans Pricing
  plan_count: 2
  slug: university-of-michigan-ann-arbor-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: University Of Michigan Ann Arbor Rate Limits
  slug: university-of-michigan-ann-arbor-rate-limits
rules:
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: University of Michigan-Ann Arbor API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 0
    warn: 3
  slug: university-of-michigan-ann-arbor-rules
scopes:
- name: University Of Michigan Ann Arbor Scopes
  scope_count: 0
  slug: university-of-michigan-ann-arbor-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.3
  delta: 2.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 78.8
    contract_quality: 66.7
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 78.8
    operational_transparency: 23.7
  previous_composite: 57.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 72.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: University Of Michigan Ann Arbor Authentication
  slug: university-of-michigan-ann-arbor-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Michigan Ann Arbor Domain Security
  slug: university-of-michigan-ann-arbor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-michigan-ann-arbor
tags:
- University
- Higher Education
- Education
- Public Research University
- United States
- Michigan
- Big Ten
- Association of American Universities
- Research Data
- Institutional Repository
- Identity Federation
- OAI-PMH
- Library
- Research Computing
website: https://umich.edu
---
