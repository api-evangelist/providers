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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 101
  human_in_the_loop: 1
  name: University Of Chicago Agentic Access
  operation_count: 176
  slug: university-of-chicago-agentic-access
  summary_line: 176 operations · 101 acting · 1 human-in-the-loop
api_count: 44
apis:
- description: The University of Chicago's Shibboleth identity provider publishes its SAML 2.0 metadata document publicly. entityID urn:mace:incommon:uchicago.edu places the institution in the InCommon federation an
  name: University of Chicago Shibboleth Identity Provider — InCommon SAML Metadata
  slug: shibboleth-idp-metadata
- description: 'Knowledge@UChicago is the University''s institutional repository, running self-hosted InvenioRDM 13.1 on the institution''s own domain. Its REST API returns records, communities and files as JSON, with '
  name: Knowledge@UChicago Repository REST API
  slug: knowledge-invenio-rest
- description: OAI-PMH 2.0 harvesting endpoint for the University of Chicago institutional repository. ?verb=Identify returns repositoryName "UChicago Knowledge", protocolVersion 2.0, granularity YYYY-MM-DDThh:mm:ss
  name: Knowledge@UChicago OAI-PMH Endpoint
  slug: knowledge-oai-pmh
- description: OCHRE (Online Cultural and Historical Research Environment) is the University of Chicago's item-level research database for ancient studies, maintained by the OCHRE Data Service at the Institute for t
  name: OCHRE Data Service API
  slug: ochre-data-service
- description: IIIF Presentation API 3.0 manifests for the University of Chicago Library's digital collections, addressed by ARK (naming authority 61001) at iiif-collection.lib.uchicago.edu/object/ark:61001/{arkid}.
  name: University of Chicago Library IIIF Presentation API
  slug: library-iiif-presentation
- description: 'IIIF Image API Level 2 service for the University of Chicago Library, running Loris. The service root self-identifies: "This is Loris, an image server that implements the IIIF Image API Level 2." Veri'
  name: University of Chicago Library IIIF Image API
  slug: library-iiif-image
- description: The Library's discovery layer is VuFind, self-hosted at catalog.lib.uchicago.edu and forked in the institution's own GitHub organization (uchicago-library/vufind). VuFind ships a REST search API at /v
  name: University of Chicago Library Catalog API (VuFind)
  slug: vufind-catalog-api
- description: The admin/user API from University of Chicago — 4 operation(s) for admin/user.
  name: University of Chicago Gen3 Fence — admin/user API
  slug: university-of-chicago-admin-user-api
- description: create an alias for an entity stored in an external system managed by some other authority
  name: University of Chicago Gen3 indexd — alias API
  slug: university-of-chicago-alias-api
- description: bulk endpoints
  name: University of Chicago Gen3 indexd — bulk API
  slug: university-of-chicago-bulk-api
- description: Bundle endpoints.
  name: University of Chicago Gen3 indexd — bundle API
  slug: university-of-chicago-bundle-api
- description: The core metadata API from University of Chicago — 1 operation(s) for core metadata.
  name: University of Chicago Gen3 Peregrine — core metadata API
  slug: university-of-chicago-core-metadata-api
- description: API Credentials
  name: University of Chicago Gen3 Fence — credentials/api API
  slug: university-of-chicago-credentials-api-api
- description: Access credentials
  name: University of Chicago Gen3 Fence — credentials API
  slug: university-of-chicago-credentials-api
- description: Deprecated! Use credentials/api
  name: University of Chicago Gen3 Fence — credentials/cdis API
  slug: university-of-chicago-credentials-cdis-api
- description: Google Credentials
  name: University of Chicago Gen3 Fence — credentials/google API
  slug: university-of-chicago-credentials-google-api
- description: Other provider credentials
  name: University of Chicago Gen3 Fence — credentials/{provider} API
  slug: university-of-chicago-credentials-provider-api
- description: Generate signed URLs
  name: University of Chicago Gen3 Fence — data API
  slug: university-of-chicago-data-api
- description: The datasets API from University of Chicago — 2 operation(s) for datasets.
  name: University of Chicago Gen3 Peregrine — datasets API
  slug: university-of-chicago-datasets-api
- description: The dictionary API from University of Chicago — 8 operation(s) for dictionary.
  name: University of Chicago Gen3 Sheepdog — dictionary API
  slug: university-of-chicago-dictionary-api
- description: Data Object Service Retrieval Endpoints
  name: University of Chicago Gen3 indexd — DOS API
  slug: university-of-chicago-dos-api
- description: Data Repository Service Retrieval Endpoints
  name: University of Chicago Gen3 indexd — DRS API
  slug: university-of-chicago-drs-api
- description: The dry run API from University of Chicago — 12 operation(s) for dry run.
  name: University of Chicago Gen3 Sheepdog — dry run API
  slug: university-of-chicago-dry-run-api
- description: The entity API from University of Chicago — 7 operation(s) for entity.
  name: University of Chicago Gen3 Sheepdog — entity API
  slug: university-of-chicago-entity-api
- description: The export API from University of Chicago — 1 operation(s) for export.
  name: University of Chicago Gen3 Sheepdog — export API
  slug: university-of-chicago-export-api
- description: The file API from University of Chicago — 5 operation(s) for file.
  name: University of Chicago Gen3 Sheepdog — file API
  slug: university-of-chicago-file-api
- description: Search for an alias or index, potentially even a distributed search.
  name: University of Chicago Gen3 indexd — global API
  slug: university-of-chicago-global-api
- description: Google functionality
  name: University of Chicago Gen3 Fence — google API
  slug: university-of-chicago-google-api
- description: GraphQL Queries
  name: University of Chicago Gen3 Peregrine — graphql API
  slug: university-of-chicago-graphql-api
- description: Endpoints for generation of Gen3 GUIDs
  name: University of Chicago Gen3 indexd — GUID API
  slug: university-of-chicago-guid-api
- description: Associate a file (object) with a unique id, and store some basic metadata.
  name: University of Chicago Gen3 indexd — index API
  slug: university-of-chicago-index-api
- description: Get public keys used to validate JWTs issued by fence
  name: University of Chicago Gen3 Fence — keys API
  slug: university-of-chicago-keys-api
- description: Link access identities
  name: University of Chicago Gen3 Fence — link API
  slug: university-of-chicago-link-api
- description: The login API from University of Chicago — 2 operation(s) for login.
  name: University of Chicago Gen3 Fence — login API
  slug: university-of-chicago-login-api
- description: Log out the current user
  name: University of Chicago Gen3 Fence — logout API
  slug: university-of-chicago-logout-api
- description: Authorization and token management
  name: University of Chicago Gen3 Fence — oauth2 API
  slug: university-of-chicago-oauth2-api
- description: The OIDC API from University of Chicago — 1 operation(s) for oidc.
  name: University of Chicago Gen3 Fence — OIDC API
  slug: university-of-chicago-oidc-api
- description: The privacy-policy API from University of Chicago — 1 operation(s) for privacy-policy.
  name: University of Chicago Gen3 Fence — privacy-policy API
  slug: university-of-chicago-privacy-policy-api
- description: The program API from University of Chicago — 2 operation(s) for program.
  name: University of Chicago Gen3 Sheepdog — program API
  slug: university-of-chicago-program-api
- description: The project API from University of Chicago — 6 operation(s) for project.
  name: University of Chicago Gen3 Sheepdog — project API
  slug: university-of-chicago-project-api
- description: query endpoints
  name: University of Chicago Gen3 indexd — query API
  slug: university-of-chicago-query-api
- description: The register API from University of Chicago — 1 operation(s) for register.
  name: University of Chicago Gen3 Fence — register API
  slug: university-of-chicago-register-api
- description: System endpoints
  name: University of Chicago Gen3 indexd — system API
  slug: university-of-chicago-system-api
- description: User information
  name: University of Chicago Gen3 Fence — user API
  slug: university-of-chicago-user-api
artifact_total: 101
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fence OpenAPI Specification admin/user API
  slug: open-university-of-chicago-admin-user-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user alias API
  slug: open-university-of-chicago-alias-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user bulk API
  slug: open-university-of-chicago-bulk-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user bundle API
  slug: open-university-of-chicago-bundle-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user core metadata API
  slug: open-university-of-chicago-core-metadata-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user credentials/api API
  slug: open-university-of-chicago-credentials-api-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user credentials API
  slug: open-university-of-chicago-credentials-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user credentials/cdis API
  slug: open-university-of-chicago-credentials-cdis-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user credentials/google API
  slug: open-university-of-chicago-credentials-google-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user credentials/{provider} API
  slug: open-university-of-chicago-credentials-provider-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user data API
  slug: open-university-of-chicago-data-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user datasets API
  slug: open-university-of-chicago-datasets-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user dictionary API
  slug: open-university-of-chicago-dictionary-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user DOS API
  slug: open-university-of-chicago-dos-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user DRS API
  slug: open-university-of-chicago-drs-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user dry run API
  slug: open-university-of-chicago-dry-run-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user entity API
  slug: open-university-of-chicago-entity-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user export API
  slug: open-university-of-chicago-export-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user file API
  slug: open-university-of-chicago-file-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user global API
  slug: open-university-of-chicago-global-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user google API
  slug: open-university-of-chicago-google-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user graphql API
  slug: open-university-of-chicago-graphql-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user GUID API
  slug: open-university-of-chicago-guid-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user index API
  slug: open-university-of-chicago-index-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user keys API
  slug: open-university-of-chicago-keys-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user link API
  slug: open-university-of-chicago-link-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user login API
  slug: open-university-of-chicago-login-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user logout API
  slug: open-university-of-chicago-logout-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user oauth2 API
  slug: open-university-of-chicago-oauth2-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user OIDC API
  slug: open-university-of-chicago-oidc-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user privacy-policy API
  slug: open-university-of-chicago-privacy-policy-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user program API
  slug: open-university-of-chicago-program-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user project API
  slug: open-university-of-chicago-project-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user query API
  slug: open-university-of-chicago-query-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user register API
  slug: open-university-of-chicago-register-api
- collection_type: open
  name: Fence OpenAPI Specification admin/user system API
  slug: open-university-of-chicago-system-api
- collection_type: open
  name: Fence OpenAPI Specification admin/ user API
  slug: open-university-of-chicago-user-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.uchicago.edu/
- group: company
  title: ''
  type: Blog
  url: https://news.uchicago.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uchicago
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uc-cdis
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/uchicago-library
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uchicago/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/UChicago
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.uchicago.edu/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://uchicago.service-now.com/it
- group: docs
  title: ''
  type: Documentation
  url: https://uc-cdis.github.io/gen3-user-doc/appendices/api-gen3/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gen3.datacommons.io/
- group: docs
  title: ''
  type: APIReference
  url: https://gen3.datacommons.io/.well-known/openid-configuration
- group: other
  title: ''
  type: IdentityFederation
  url: https://shibboleth2.uchicago.edu/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://knowledge.uchicago.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalog.lib.uchicago.edu/vufind/
- group: other
  title: ''
  type: ResearchComputing
  url: https://rcc.uchicago.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://genai.uchicago.edu/
- group: build
  title: ''
  type: AITooling
  url: https://genai.uchicago.edu/service-requests
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-chicago-domain-standards.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-chicago-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-chicago-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-chicago-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-chicago-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-chicago-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-chicago-scopes.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-chicago-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-chicago-vocabulary.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/university-of-chicago-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-chicago-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-chicago-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-chicago-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Chicago is a private research university in Chicago, Illinois, founded in 1890. It operates no central developer portal and publishes no institution-wide API programme, and the one gated portal it does run — an Azure API Management front end for Azure OpenAI at ai-api-portal-dev.uchicago.edu — serves a certificate that does not match its own hostname and, with verification disabled, answers a bare Azure Application Gateway 404, so it is not a public surface. What it does operate is unusually real for a university, because UChicago is a genuine PRODUCER of open-source data infrastructure rather than only a buyer of it: the Center for Translational Data Science (CTDS, github.com/uc-cdis) authors the Gen3 data-commons platform and runs its own reference commons at gen3.datacommons.io, a domain registered to CDIS at the University. The OpenAPI documents in this repository are CTDS''s own contracts (info.contact cdis@uchicago.edu, termsOfService cdis.uchicago.edu),
  not a vendor''s running under the institution''s name. Alongside that the institution operates a Shibboleth identity provider whose InCommon SAML metadata is public (entityID urn:mace:incommon:uchicago.edu), Knowledge@UChicago on self-hosted InvenioRDM 13.1 with a live REST API and an OAI-PMH 2.0 responder advertising DataCite metadata, the OCHRE ancient-studies data service, and IIIF Presentation 3.0 and Image 2.0 endpoints for library digital collections. Course catalog and registrar data remain behind PeopleSoft authentication, the VuFind catalog API is deployed with its API permissions denied, and there is no open-data portal — data.uchicago.edu is the Office of Institutional Analysis''s reporting site, not a machine-readable catalog.'
examples:
- key_count: 2
  name: University Of Chicago Fence Create Apikey Example
  slug: university-of-chicago-fence-create-apikey-example
- key_count: 2
  name: University Of Chicago Indexd Get Record Example
  slug: university-of-chicago-indexd-get-record-example
- key_count: 2
  name: University Of Chicago Sheepdog Create Program Example
  slug: university-of-chicago-sheepdog-create-program-example
finops:
- name: University Of Chicago Finops
  service_category: Education
  slug: university-of-chicago-finops
graphqls:
- description: Open-source data platform maintained by the University of Chicago Center for Translational Data Science. Gen3 auto-generates FAIR APIs (data submission, GraphQL/Peregrine query, indexing/Indexd, Fence
  name: University of Chicago GraphQL API
  slug: university-of-chicago-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-chicago.png
json_schemas:
- name: Gen3 Indexd Record
  property_count: 16
  slug: university-of-chicago-indexd-record
- name: Gen3 Sheepdog Program
  property_count: 3
  slug: university-of-chicago-sheepdog-program
- name: Gen3 Sheepdog Project
  property_count: 5
  slug: university-of-chicago-sheepdog-project
json_structures:
- name: University Of Chicago Indexd Record Structure
  property_count: 16
  slug: university-of-chicago-indexd-record-structure
- name: University Of Chicago Sheepdog Program Structure
  property_count: 3
  slug: university-of-chicago-sheepdog-program-structure
jsonld:
- class_count: 34
  name: University Of Chicago Context
  property_count: 0
  slug: university-of-chicago-context
layout: provider
modified: '2026-08-19'
name: University of Chicago
nav: Providers
network: true
overview: 'University of Chicago publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Knowledge@UChicago Repository REST API, Gen3 Fence — admin/user API, Gen3 indexd — alias API, and 35 more. Tagged areas include University, Higher Education, Education, Private Research University, and United States.


  The University of Chicago catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Chicago''s developer surface includes engineering blog, GitHub presence, support, documentation, API reference, authentication, and 26 more developer resources.'
plans:
- name: University Of Chicago Plans Pricing
  plan_count: 2
  slug: university-of-chicago-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: University Of Chicago Rate Limits
  slug: university-of-chicago-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Chicago API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-chicago-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: University of Chicago API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 2
  slug: university-of-chicago-rules
scopes:
- name: University Of Chicago Scopes
  scope_count: 3
  slug: university-of-chicago-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 44.4
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 25.0
    contract_quality: 56.8
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 23.7
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 2.6
      total: 38
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-chicago/refs/heads/main/screenshots/university-of-chicago-2026-06-20T200146.png
security:
- kind: authentication
  name: University Of Chicago Authentication
  slug: university-of-chicago-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: University Of Chicago Domain Security
  slug: university-of-chicago-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: university-of-chicago
tags:
- University
- Higher Education
- Education
- Private Research University
- United States
- Illinois
- Research Data
- Research Repository
- Identity Federation
- OAI-PMH
- IIIF
- Open-Source
- Data Commons
- Digital Collections
- Research Computing
website: https://www.uchicago.edu/
---
