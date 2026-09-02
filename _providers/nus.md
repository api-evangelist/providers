---
access_model:
  confidence: high
  label: Affiliation-gated
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 3
  name: Nus Agentic Access
  operation_count: 8
  slug: nus-agentic-access
  summary_line: 8 operations · 3 human-in-the-loop
api_count: 10
apis:
- description: The API behind the NUS internal shuttle bus service — bus stops, services and arrival times across the Kent Ridge and Bukit Timah campuses. Institution-operated and live, but gated behind HTTP Basic c
  name: NUS NextBus (Internal Shuttle Bus) API
  slug: nextbus
- description: The HAL-style REST API of ScholarBank@NUS, the university's institutional repository — communities, collections, items, bitstreams and a 485-field metadata registry covering the university's scholarly
  name: ScholarBank@NUS DSpace REST API
  slug: scholarbank-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for ScholarBank@NUS, advertising twelve metadata formats including oai_dc, qdc, mods, mets, marc, etdms and uketd_dc, with an earliest datestamp of 2006-11-09.
  name: ScholarBank@NUS OAI-PMH Interface
  slug: scholarbank-oai
- description: The learning management system for NUS courses, running on Instructure's Canvas as a vanity tenant. The REST API is live and returns a structured 401 to unauthenticated callers; the LTI 1.3 tool-platf
  name: NUS Canvas LMS API
  slug: canvas
- description: 'The NUS academic, educational, research and administrative blogging platform exposes a full WordPress REST API with eleven namespaces and 190 routes, anonymously readable. Runs on CampusPress managed '
  name: Blog.nus WordPress REST API
  slug: blog-wp
- description: The only public machine-readable description of NUS course data that exists — module lists, module information, prerequisite trees, timetables and venue occupancy, published as an OpenAPI 3.0.1 docume
  name: NUSMods API (student-operated, not endorsed)
  slug: nusmods
- description: NUS is one of fourteen identity providers registered in the Singapore Access Federation, which SingAREN operates and which interfederates with eduGAIN. The entityID NUS is registered under is a Simple
  name: NUS entry in the Singapore Access Federation
  slug: sgaf
- description: OAuth 2.0 / OpenID Connect authorization and token issuance.
  name: National University of Singapore Authorization API
  slug: nus-authorization-api
- description: Machine-readable metadata describing the identity service and its signing keys.
  name: National University of Singapore Discovery API
  slug: nus-discovery-api
- description: End-user claims and session termination.
  name: National University of Singapore Session API
  slug: nus-session-api
artifact_total: 24
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nus-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://nus.edu.sg/
- group: other
  title: ''
  type: IdentityFederation
  url: https://vafs.nus.edu.sg/FederationMetadata/2007-06/FederationMetadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholarbank.nus.edu.sg/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://nusmods.com/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://libguides.nus.edu.sg/
- group: other
  title: ''
  type: AIPolicy
  url: https://libguides.nus.edu.sg/new2nus/acadintegrity
- group: build
  title: ''
  type: AITooling
  url: https://news.nus.edu.sg/nus-makes-ai-courses-compulsory-gives-free-access-to-chatgpt-edu/
- group: company
  title: ''
  type: Blog
  url: https://news.nus.edu.sg/
- group: company
  title: ''
  type: BlogRSS
  url: https://news.nus.edu.sg/feed/
- group: other
  title: ''
  type: SingleSignOn
  url: https://vafs.nus.edu.sg/adfs/ls/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/national-university-of-singapore/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/NUSingapore
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/nus-identity-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/nus-openid-configuration-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/index.yml
- group: design
  title: ''
  type: Rules
  url: rules/nus-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/nus-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/nus-context.jsonld
- group: auth
  title: ''
  type: Authentication
  url: authentication/nus-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/nus-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/nus-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nus-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nus-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nus-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nus-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: NUS operates real institution-owned API surfaces, but none of them can be consumed by an unaffiliated caller. The federated identity service at vafs.nus.edu.sg publishes anonymously readable OIDC and SAML metadata, yet a client_id exists only if NUS Information Technology creates one and there is no public or dynamic registration endpoint. The NUS shuttle bus API at nnextbus.nus.edu.sg answers 401 with an HTTP Basic challenge and NUS issues no public credentials for it. The api.nus.edu.sg gateway is live on an NUS-issued certificate and returns HTTP 500 on every probed path, publishing no route at all. Two secondary limits apply and are recorded rather than treated as findings about NUS - the main nus.edu.sg web estate sits behind an Imperva bot challenge that returns 200 with a JavaScript shell for every deep path, so terms-of-use, IT and library pages could not be read and are not claimed as pointers; and nusit.nus.edu.sg answered 403 to the HPC documentation path. Everything
    else that is publicly readable belongs to a platform NUS rents. This is a correct thin profile, not a failed probe - 40+ URLs were fetched successfully across nine hosts.
  evidence:
  - status: 200
    url: https://vafs.nus.edu.sg/adfs/.well-known/openid-configuration
  - status: 200
    url: https://vafs.nus.edu.sg/FederationMetadata/2007-06/FederationMetadata.xml
  - status: 200
    url: https://vafs.nus.edu.sg/adfs/discovery/keys
  - status: 401
    url: https://nnextbus.nus.edu.sg/BusStops
  - status: 500
    url: https://api.nus.edu.sg/
  - status: 500
    url: https://api.nus.edu.sg/swagger.json
  - status: 200
    url: https://scholarbank.nus.edu.sg/oai/request?verb=Identify
  - status: 200
    url: https://scholarbank.nus.edu.sg/server/api
  - status: 401
    url: https://canvas.nus.edu.sg/api/v1/accounts
  - status: 200
    url: https://canvas.nus.edu.sg/api/lti/security/jwks
  - status: 200
    url: https://blog.nus.edu.sg/wp-json/
  - status: 404
    url: https://vafs.nus.edu.sg/scim/v2/ServiceProviderConfig
  - note: soft-404 - HTML body, not an llms.txt; not credited
    status: 200
    url: https://nus.edu.sg/llms.txt
  - note: soft-404 - HTML body behind Imperva; not credited
    status: 200
    url: https://www.nus.edu.sg/robots.txt
  - note: Imperva JavaScript challenge shell, content unreadable; not claimed as a pointer
    status: 200
    url: https://nus.edu.sg/about-nus/terms-of-use
  - note: bot-challenged; research computing documentation not readable
    status: 403
    url: https://nusit.nus.edu.sg/hpc/
  - note: decommissioned in-house LMS; DNS and NUS certificate remain, host does not connect
    status: 0
    url: https://luminus.nus.edu.sg/
  reason: no_public_developer_program
  state: gated
created: '2026-06-03'
description: 'The National University of Singapore is Singapore''s flagship public research university, ranked eighth in the QS World University Rankings 2025, and it is a near-perfect illustration of why a university is a federation of buyers rather than a producer. NUS operates exactly one substantial machine-readable API surface of its own: the federated identity service at vafs.nus.edu.sg, which publishes a live OpenID Connect discovery document, a JWKS, and signed SAML 2.0 metadata for entityID https://vafs.nus.edu.sg/adfs/services/trust, and which registers NUS as an identity provider in the Singapore Access Federation. Everything else that looks like an NUS API belongs to a platform NUS rents — ScholarBank@NUS is Atmire''s DSpace, the learning management system is Instructure''s Canvas, the blogs are CampusPress, the library guides are Springshare. NUS has an API gateway hostname at api.nus.edu.sg on a certificate issued to the university, and it returns HTTP 500 on every path. The
  campus shuttle bus API at nnextbus.nus.edu.sg is genuinely NUS''s and genuinely live, but sits behind HTTP Basic credentials the university does not issue publicly. Most strikingly, NUS''s own course vocabulary — modules, modular credits, prerequisite trees — has no public machine-readable expression from the university at all; the only OpenAPI describing NUS course data is published by NUSMods, a student organisation, from a non-NUS domain. There is no NUS developer portal, no institution-wide GitHub organisation, no public open-data portal, no llms.txt, and no self-service registration path to any NUS API.'
examples:
- key_count: 1
  name: Nus Jwks Example
  slug: nus-jwks-example
- key_count: 26
  name: Nus Openid Configuration Example
  slug: nus-openid-configuration-example
- key_count: 6
  name: Nus Scholarbank Dspace Root Example
  slug: nus-scholarbank-dspace-root-example
finops:
- name: Nus Finops
  service_category: Education
  slug: nus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nus.png
json_schemas:
- name: NUS JSON Web Key Set
  property_count: 1
  slug: nus-jwks
- name: NUS OpenID Provider Metadata
  property_count: 26
  slug: nus-openid-configuration
jsonld:
- class_count: 3
  name: Nus Context
  property_count: 0
  slug: nus-context
layout: provider
modified: '2026-08-19'
name: National University of Singapore
nav: Providers
network: true
overview: 'National University of Singapore publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authorization API, Discovery API, and Session API. Tagged areas include University, Higher Education, Education, Singapore, and Research.


  The National University of Singapore catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  National University of Singapore''s developer surface includes engineering blog, code examples, authentication, and 27 more developer resources.'
plans:
- name: Nus Plans Pricing
  plan_count: 2
  slug: nus-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Nus Rate Limits
  slug: nus-rate-limits
rules:
- effective_rule_count: 11
  extends: []
  name: National University of Singapore API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 4
  slug: nus-rules
scopes:
- name: Nus Scopes
  scope_count: 0
  slug: nus-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 41.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -9.8
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 11.4
    contract_quality: 25.1
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 11.4
    operational_transparency: 23.7
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/nus/refs/heads/main/screenshots/nus-2026-06-20T190528.png
security:
- kind: authentication
  name: Nus Authentication
  slug: nus-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Nus Domain Security
  slug: nus-domain-security
  summary_line: TLSv1.2 · HSTS
slug: nus
tags:
- University
- Higher Education
- Education
- Singapore
- Research
- Identity Federation
- Research Repository
- Course Catalog
- Open Access
- Learning Management
website: https://nus.edu.sg/
---
