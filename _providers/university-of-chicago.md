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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 101
  human_in_the_loop: 1
  name: University Of Chicago Agentic Access
  operation_count: 176
  slug: university-of-chicago-agentic-access
  summary_line: 176 operations · 101 acting · 1 human-in-the-loop
api_count: 39
apis:
- description: University of Chicago identity and authentication integrations published on the official uchicago GitHub organization, including Shibboleth Identity Provider extensions and OpenID Connect (OIDC) examp
  name: CNetID OpenID Connect / Shibboleth Identity
  slug: cnetid-oidc
- description: The University of Chicago Library exposes International Image Interoperability Framework (IIIF) image and presentation endpoints for its digital collections, with related code published in the uchicag
  name: University of Chicago Library IIIF
  slug: library-iiif
- description: The admin/user API from University of Chicago — 4 operation(s) for admin/user.
  name: University of Chicago admin/user API
  slug: university-of-chicago-admin-user-api
- description: create an alias for an entity stored in an external system managed by some other authority
  name: University of Chicago alias API
  slug: university-of-chicago-alias-api
- description: bulk endpoints
  name: University of Chicago bulk API
  slug: university-of-chicago-bulk-api
- description: Bundle endpoints.
  name: University of Chicago bundle API
  slug: university-of-chicago-bundle-api
- description: The core metadata API from University of Chicago — 1 operation(s) for core metadata.
  name: University of Chicago core metadata API
  slug: university-of-chicago-core-metadata-api
- description: API Credentials
  name: University of Chicago credentials/api API
  slug: university-of-chicago-credentials-api-api
- description: Access credentials
  name: University of Chicago credentials API
  slug: university-of-chicago-credentials-api
- description: Deprecated! Use credentials/api
  name: University of Chicago credentials/cdis API
  slug: university-of-chicago-credentials-cdis-api
- description: Google Credentials
  name: University of Chicago credentials/google API
  slug: university-of-chicago-credentials-google-api
- description: Other provider credentials
  name: University of Chicago credentials/{provider} API
  slug: university-of-chicago-credentials-provider-api
- description: Generate signed URLs
  name: University of Chicago data API
  slug: university-of-chicago-data-api
- description: The datasets API from University of Chicago — 2 operation(s) for datasets.
  name: University of Chicago datasets API
  slug: university-of-chicago-datasets-api
- description: The dictionary API from University of Chicago — 8 operation(s) for dictionary.
  name: University of Chicago dictionary API
  slug: university-of-chicago-dictionary-api
- description: Data Object Service Retrieval Endpoints
  name: University of Chicago DOS API
  slug: university-of-chicago-dos-api
- description: Data Repository Service Retrieval Endpoints
  name: University of Chicago DRS API
  slug: university-of-chicago-drs-api
- description: The dry run API from University of Chicago — 12 operation(s) for dry run.
  name: University of Chicago dry run API
  slug: university-of-chicago-dry-run-api
- description: The entity API from University of Chicago — 7 operation(s) for entity.
  name: University of Chicago entity API
  slug: university-of-chicago-entity-api
- description: The export API from University of Chicago — 1 operation(s) for export.
  name: University of Chicago export API
  slug: university-of-chicago-export-api
- description: The file API from University of Chicago — 5 operation(s) for file.
  name: University of Chicago file API
  slug: university-of-chicago-file-api
- description: Search for an alias or index, potentially even a distributed search.
  name: University of Chicago global API
  slug: university-of-chicago-global-api
- description: Google functionality
  name: University of Chicago google API
  slug: university-of-chicago-google-api
- description: GraphQL Queries
  name: University of Chicago graphql API
  slug: university-of-chicago-graphql-api
- description: Endpoints for generation of Gen3 GUIDs
  name: University of Chicago GUID API
  slug: university-of-chicago-guid-api
- description: Associate a file (object) with a unique id, and store some basic metadata.
  name: University of Chicago index API
  slug: university-of-chicago-index-api
- description: Get public keys used to validate JWTs issued by fence
  name: University of Chicago keys API
  slug: university-of-chicago-keys-api
- description: Link access identities
  name: University of Chicago link API
  slug: university-of-chicago-link-api
- description: The login API from University of Chicago — 2 operation(s) for login.
  name: University of Chicago login API
  slug: university-of-chicago-login-api
- description: Log out the current user
  name: University of Chicago logout API
  slug: university-of-chicago-logout-api
- description: Authorization and token management
  name: University of Chicago oauth2 API
  slug: university-of-chicago-oauth2-api
- description: The OIDC API from University of Chicago — 1 operation(s) for oidc.
  name: University of Chicago OIDC API
  slug: university-of-chicago-oidc-api
- description: The privacy-policy API from University of Chicago — 1 operation(s) for privacy-policy.
  name: University of Chicago privacy-policy API
  slug: university-of-chicago-privacy-policy-api
- description: The program API from University of Chicago — 2 operation(s) for program.
  name: University of Chicago program API
  slug: university-of-chicago-program-api
- description: The project API from University of Chicago — 6 operation(s) for project.
  name: University of Chicago project API
  slug: university-of-chicago-project-api
- description: query endpoints
  name: University of Chicago query API
  slug: university-of-chicago-query-api
- description: The register API from University of Chicago — 1 operation(s) for register.
  name: University of Chicago register API
  slug: university-of-chicago-register-api
- description: System endpoints
  name: University of Chicago system API
  slug: university-of-chicago-system-api
- description: User information
  name: University of Chicago user API
  slug: university-of-chicago-user-api
artifact_total: 58
common:
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
- group: company
  title: ''
  type: Website
  url: https://www.uchicago.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uchicago
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uchicago/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/UChicago
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/uc-cdis
- group: auth
  title: ''
  type: Authentication
  url: https://github.com/uchicago
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
description: 'The University of Chicago is a private research university in Chicago, Illinois, founded in 1890 and ranked #14 in the QS World University Rankings 2025. Its public developer and API footprint is anchored in research data infrastructure rather than a single central developer portal: the Center for Translational Data Science (CTDS) maintains the open-source Gen3 data platform (uc-cdis on GitHub), which auto-generates FAIR APIs for accessing biomedical data commons. The University also publishes Shibboleth/OpenID Connect identity integrations for CNetID authentication, and the University of Chicago Library operates IIIF image and presentation endpoints plus a VuFind-based catalog. A faculty/staff-facing AI API portal (Azure OpenAI via API Management) exists but is gated and not publicly accessible.'
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
modified: '2026-06-03'
name: University of Chicago
nav: Providers
network: true
overview: 'University of Chicago publishes 37 APIs on the [APIs.io](https://apis.io/) network, including admin/user API, alias API, bulk API, and 34 more. Tagged areas include Education, Higher Education, University, Research Data, and Open Source.


  The University of Chicago catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Chicago''s developer surface includes authentication, GitHub presence, and 12 more developer resources.'
plans:
- name: University Of Chicago Plans Pricing
  plan_count: 2
  slug: university-of-chicago-plans-pricing
random_paper: 103
rate_limits:
- limit_count: 1
  name: University Of Chicago Rate Limits
  slug: university-of-chicago-rate-limits
rules:
- name: University of Chicago API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-chicago-jsonschema-spectral-rules
- name: University of Chicago API Rules
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
  band: thin
  composite: 40.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.6
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
  schema_version: 0.11.0
  scored_at: '2026-08-12'
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
- Education
- Higher Education
- University
- Research Data
- Open Source
- IIIF
- Identity
- United States
website: https://www.uchicago.edu/
---
