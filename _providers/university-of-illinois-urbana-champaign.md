---
access_model:
  confidence: high
  label: Free · Institutional affiliation for authenticated surfaces
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 116
  human_in_the_loop: 3
  name: University Of Illinois Urbana Champaign Agentic Access
  operation_count: 196
  slug: university-of-illinois-urbana-champaign-agentic-access
  summary_line: 196 operations · 116 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.rokwire.illinois.edu/core
  baseurl_source: declared
  description: The identity, account and authorization service at the centre of UIUC's Rokwire platform — accounts, profiles, applications, organizations, service registrations, permissions, roles and scopes. Writte
  name: Rokwire Core Building Block API
  slug: rokwire-core-building-block
- baseURL: https://api.rokwire.illinois.edu/gateway
  baseurl_source: declared
  description: The Rokwire service that fronts external and campus systems for the Illinois app — wayfinding and building/floorplan data, campus data streams, and third-party service integration. University-written,
  name: Rokwire Gateway Building Block API
  slug: rokwire-gateway-building-block
- description: The Course Information Suite API — RESTful resources over Class Schedule and Course Catalog data, organised as Schedule, Catalog, GenEd, Term and Subjects modules and served as XML in a campus-local n
  name: Course Explorer (CISAPI)
  slug: cisapi-course-explorer
- description: The OAI-PMH 2.0 data provider for IDEALS, the Illinois Digital Environment for Access to Learning and Scholarship. Identify reports repositoryName "IDEALS @ University of Illinois Urbana-Champaign", a
  name: IDEALS OAI-PMH
  slug: ideals-oai-pmh
- description: The campus research data repository, built and run in-house by the University Library (github.com/medusa-project/databank, Ruby on Rails) rather than bought from Figshare, Dryad or Dataverse — which m
  name: Illinois Data Bank Dataset Metadata
  slug: illinois-data-bank
- description: The campus SAML identity provider — the one surface a university operates by definition and almost never has catalogued. https://shibboleth.illinois.edu/idp/shibboleth serves a Shibboleth EntityDescri
  name: Illinois Shibboleth Identity Provider (InCommon)
  slug: incommon-shibboleth-idp
- description: TENANT RELATIONSHIP, not a UIUC contract. Illinois Experts is the university's research information and expert-profile portal, and the data in it — people, publications, projects, units — is the unive
  name: Illinois Experts (Elsevier Pure)
  slug: illinois-experts
- description: TENANT RELATIONSHIP, not a UIUC contract. Library discovery at Illinois runs on Ex Libris Primo — search.library.illinois.edu redirects into primo.exlibrisgroup.com/discovery with an Illinois view. Th
  name: University Library Discovery (Ex Libris Primo)
  slug: library-discovery
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rokwire Core Building Block Admin API
  slug: open-university-of-illinois-urbana-champaign-admin-api
- collection_type: open
  name: Rokwire Core Building Block Admin BBs API
  slug: open-university-of-illinois-urbana-champaign-bbs-api
- collection_type: open
  name: Rokwire Core Building Block Admin Client API
  slug: open-university-of-illinois-urbana-champaign-client-api
- collection_type: open
  name: Rokwire Core Building Block Admin Default API
  slug: open-university-of-illinois-urbana-champaign-default-api
- collection_type: open
  name: Rokwire Core Building Block Admin Enc API
  slug: open-university-of-illinois-urbana-champaign-enc-api
- collection_type: open
  name: Rokwire Core Building Block Admin Services API
  slug: open-university-of-illinois-urbana-champaign-services-api
- collection_type: open
  name: Rokwire Core Building Block Admin System API
  slug: open-university-of-illinois-urbana-champaign-system-api
- collection_type: open
  name: Rokwire Core Building Block Admin Third-Party Services API
  slug: open-university-of-illinois-urbana-champaign-third-party-services-api
- collection_type: open
  name: Rokwire Core Building Block Admin TPS API
  slug: open-university-of-illinois-urbana-champaign-tps-api
- collection_type: open
  name: Rokwire Core Building Block Admin UI API
  slug: open-university-of-illinois-urbana-champaign-ui-api
- collection_type: open
  name: Rokwire Core Building Block Admin Version API
  slug: open-university-of-illinois-urbana-champaign-version-api
- collection_type: open
  name: Rokwire Core Building Block Admin .well Known API
  slug: open-university-of-illinois-urbana-champaign-well-known-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/rokwire/core-building-block/blob/develop/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/university-of-illinois-urbana-champaign-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://illinois.edu/
- group: company
  title: ''
  type: About
  url: https://illinois.edu/about
- group: docs
  title: ''
  type: APIReference
  url: https://api.rokwire.illinois.edu/core/doc/ui/
- group: docs
  title: ''
  type: Documentation
  url: https://api.rokwire.illinois.edu/gateway/doc/ui/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rokwire
- group: build
  title: ''
  type: GitHub
  url: https://github.com/illinois
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/medusa-project
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-illinois-at-urbana-champaign/
- group: operate
  title: ''
  type: Status
  url: https://status.illinois.edu/
- group: operate
  title: ''
  type: Support
  url: https://help.uillinois.edu/
- group: company
  title: ''
  type: Blog
  url: https://news.illinois.edu/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.library.illinois.edu/geninfo/policies/p_policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://publish.illinois.edu/experts-help/terms-of-use/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://courses.illinois.edu/cisdocs/api
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.ideals.illinois.edu/
- group: other
  title: ''
  type: OpenData
  url: https://databank.illinois.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://search.library.illinois.edu/discovery
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibboleth.illinois.edu/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://ncsa.illinois.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://genai.illinois.edu/
- group: build
  title: ''
  type: AITooling
  url: https://techservices.illinois.edu/
- group: other
  title: ''
  type: Policies
  url: https://cio.illinois.edu/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-illinois-urbana-champaign-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-illinois-urbana-champaign-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-illinois-urbana-champaign-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-illinois-urbana-champaign-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-illinois-urbana-champaign-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-illinois-urbana-champaign-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-illinois-urbana-champaign-lifecycle.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-illinois-urbana-champaign-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-illinois-urbana-champaign-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-illinois-urbana-champaign-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-illinois-urbana-champaign-organization-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/university-of-illinois-urbana-champaign-organization-example.json
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-illinois-urbana-champaign-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-illinois-urbana-champaign-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-illinois-urbana-champaign-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Illinois Urbana-Champaign (UIUC) is the public land-grant flagship of the University of Illinois System and a founding Big Ten institution. It is one of the few universities in this cohort that genuinely ENGINEERS a public API estate rather than buying one: the Rokwire platform behind the official Illinois app is UIUC''s own open-source work, published under Apache 2.0 in github.com/rokwire and deployed on the institution''s own host at api.rokwire.illinois.edu, where nine building blocks answer an unauthenticated /version endpoint and two of them (Core 1.62.0, Gateway 2.21.1) publish OpenAPI 3.0 through Swagger UI. Around it sit four more institution-operated machine-readable surfaces: the Course Information Suite (CISAPI) Course Explorer, which serves class schedule and catalog XML with no authentication; the IDEALS institutional repository''s OAI-PMH 2.0 endpoint, running on Illinois Library''s own Rails application rather than a vendor platform; the Illinois
  Data Bank, an in-house research data repository that has minted 1,306 DataCite DOIs under prefix 10.13012 and exposes its catalog as JSON; and the campus Shibboleth identity provider, registered in InCommon as urn:mace:incommon:uiuc.edu. The estate is real but uneven — errors are documented in prose with no schemas, no deprecation policy or Sunset header exists anywhere, seven live Rokwire building blocks ship no contract at all, and illinois.edu answers /llms.txt and /.well-known/security.txt with a soft-404 that returns HTTP 200. Research profiles (Illinois Experts / Elsevier Pure) and library discovery (Ex Libris Primo) are vendor platforms recorded here as tenant relationships: the data is the university''s, the contract is not.'
examples:
- key_count: 17
  name: University Of Illinois Urbana Champaign Building Example
  slug: university-of-illinois-urbana-champaign-building-example
- key_count: 4
  name: University Of Illinois Urbana Champaign Organization Example
  slug: university-of-illinois-urbana-champaign-organization-example
finops:
- name: University Of Illinois Urbana Champaign Finops
  service_category: Education
  slug: university-of-illinois-urbana-champaign-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-illinois-urbana-champaign.png
json_schemas:
- name: Account
  property_count: 9
  slug: university-of-illinois-urbana-champaign-account
- name: Building
  property_count: 17
  slug: university-of-illinois-urbana-champaign-building
- name: Organization
  property_count: 4
  slug: university-of-illinois-urbana-champaign-organization
json_structures:
- name: University Of Illinois Urbana Champaign Building Structure
  property_count: 17
  slug: university-of-illinois-urbana-champaign-building-structure
- name: University Of Illinois Urbana Champaign Organization Structure
  property_count: 4
  slug: university-of-illinois-urbana-champaign-organization-structure
jsonld:
- class_count: 3
  name: University Of Illinois Urbana Champaign Context
  property_count: 5
  slug: university-of-illinois-urbana-champaign-context
layout: provider
modified: '2026-08-19'
name: University of Illinois Urbana-Champaign
nav: Providers
network: true
overview: 'University of Illinois Urbana-Champaign publishes 2 APIs on the [APIs.io](https://apis.io/) network: Rokwire Core Building Block API and Rokwire Gateway Building Block API. Tagged areas include University, Higher Education, Education, Public Research University, and United States.


  The University of Illinois Urbana-Champaign catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Illinois Urbana-Champaign''s developer surface includes API reference, documentation, GitHub presence, status page, support, engineering blog, authentication, and 33 more developer resources.'
plans:
- name: University Of Illinois Urbana Champaign Plans Pricing
  plan_count: 2
  slug: university-of-illinois-urbana-champaign-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: University Of Illinois Urbana Champaign Rate Limits
  slug: university-of-illinois-urbana-champaign-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Illinois Urbana-Champaign API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-illinois-urbana-champaign-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: University of Illinois Urbana-Champaign API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: university-of-illinois-urbana-champaign-rules
scopes:
- name: University Of Illinois Urbana Champaign Scopes
  scope_count: 0
  slug: university-of-illinois-urbana-champaign-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 61.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 61.5
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 31.8
    operational_transparency: 7.9
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 16.7
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 79.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-illinois-urbana-champaign/refs/heads/main/screenshots/university-of-illinois-urbana-champaign-2026-06-20T200155.png
security:
- kind: authentication
  name: University Of Illinois Urbana Champaign Authentication
  slug: university-of-illinois-urbana-champaign-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: University Of Illinois Urbana Champaign Domain Security
  slug: university-of-illinois-urbana-champaign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-illinois-urbana-champaign
tags:
- University
- Higher Education
- Education
- Public Research University
- United States
- Illinois
- Big Ten
- Land-Grant University
- Course Catalog
- Research Data
- Research Repository
- Open Data
- Identity Federation
- OAI-PMH
- Library
- Research Computing
- Open-Source
website: https://illinois.edu/
---
