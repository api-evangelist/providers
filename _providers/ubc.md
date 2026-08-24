---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 177
  human_in_the_loop: 5
  name: Ubc Agentic Access
  operation_count: 378
  slug: ubc-agentic-access
  summary_line: 378 operations · 177 acting · 5 human-in-the-loop
api_count: 7
apis:
- description: Public REST/JSON API over UBC Library's Open Collections — the university's digitized historical, archival and research holdings. Operated by UBC Library on UBC's own infrastructure; the search resour
  name: UBC Library Open Collections API
  slug: open-collections
- description: 'IIIF Presentation manifests for Open Collections items, served from UBC Library''s own host. Verified live 2026-08-19: a 10,560-byte JSON manifest returned for an item in the UBC Archives Photograph Co'
  name: UBC Library Open Collections IIIF Presentation API
  slug: open-collections-iiif
- description: The REST API of Abacus, UBC Library's research-data repository, running Dataverse 5.9 on UBC's own infrastructure at abacus.library.ubc.ca. UBC operates the deployment and the data is UBC's and its BC
  name: UBC Library Abacus Dataverse API
  slug: abacus-dataverse
- description: 'A working OAI-PMH 2.0 archive on UBC Library''s own host. Verified live 2026-08-19: verb=Identify returns repositoryName "Abacus Data Network Dataverse OAI Archive", adminEmail abacus-support@lists.ubc'
  name: Abacus OAI-PMH Metadata Harvesting Endpoint
  slug: abacus-oai-pmh
- description: UBC's own SAML 2.0 identity provider metadata, entityID https://authentication.ubc.ca, asserting the ubc.ca scope. Institution-operated by definition — no vendor can publish this on UBC's behalf — and
  name: UBC Shibboleth Identity Provider Metadata
  slug: shibboleth-idp
- description: 'UBC''s enterprise API gateway, run by the Office of the CIO''s Integration Enablement Centre against the University Data Model. The host is real and answers — api.ubc.ca returns a flat nginx 403 to any '
  name: UBC Integration Enablement Centre API Gateway
  slug: iec-api-gateway
- description: Machine-readable service status for UBC IT at status.it.ubc.ca, on UBC's own hostname but CNAMEd to stspg-customer.com — UBC's tenant of Atlassian Statuspage. The status data is UBC's; the API, its pa
  name: UBC IT Service Status API
  slug: it-status
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UBC Abacus Dataverse Access API
  slug: open-ubc-access-api
- collection_type: open
  name: UBC Abacus Dataverse Access Admin API
  slug: open-ubc-admin-api
- collection_type: open
  name: UBC Abacus Dataverse Access Batch API
  slug: open-ubc-batch-api
- collection_type: open
  name: UBC Abacus Dataverse Access Builtin Users API
  slug: open-ubc-builtin-users-api
- collection_type: open
  name: UBC Abacus Dataverse Access Datasets API
  slug: open-ubc-datasets-api
- collection_type: open
  name: UBC Abacus Dataverse Access Datatags API
  slug: open-ubc-datatags-api
- collection_type: open
  name: UBC Abacus Dataverse Access Dataverses API
  slug: open-ubc-dataverses-api
- collection_type: open
  name: UBC Abacus Dataverse Access Edit API
  slug: open-ubc-edit-api
- collection_type: open
  name: UBC Abacus Dataverse Access Files API
  slug: open-ubc-files-api
- collection_type: open
  name: UBC Abacus Dataverse Access Harvest API
  slug: open-ubc-harvest-api
- collection_type: open
  name: UBC Abacus Dataverse Access Info API
  slug: open-ubc-info-api
- collection_type: open
  name: UBC Abacus Dataverse Access Ingest API
  slug: open-ubc-ingest-api
- collection_type: open
  name: UBC Abacus Dataverse Access Mail API
  slug: open-ubc-mail-api
- collection_type: open
  name: UBC Abacus Dataverse Access Meta API
  slug: open-ubc-meta-api
- collection_type: open
  name: UBC Abacus Dataverse Access Metadatablocks API
  slug: open-ubc-metadatablocks-api
- collection_type: open
  name: UBC Abacus Dataverse Access Mydata API
  slug: open-ubc-mydata-api
- collection_type: open
  name: UBC Abacus Dataverse Access Notifications API
  slug: open-ubc-notifications-api
- collection_type: open
  name: UBC Abacus Dataverse Access Pids API
  slug: open-ubc-pids-api
- collection_type: open
  name: UBC Abacus Dataverse Access Roles API
  slug: open-ubc-roles-api
- collection_type: open
  name: UBC Abacus Dataverse Access Search API
  slug: open-ubc-search-api
- collection_type: open
  name: UBC Abacus Dataverse Access Users API
  slug: open-ubc-users-api
- collection_type: open
  name: UBC Abacus Dataverse Access Workflows API
  slug: open-ubc-workflows-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.ubc.ca/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.library.ubc.ca/docs
- group: docs
  title: ''
  type: Documentation
  url: https://open.library.ubc.ca/docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/ubc-library/docs-open-collections-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ubc-library
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ubc/
- group: company
  title: ''
  type: Blog
  url: https://news.ubc.ca/feed/
- group: operate
  title: ''
  type: Status
  url: https://status.it.ubc.ca
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ubc.ca/site/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacymatters.ubc.ca/
- group: operate
  title: ''
  type: Support
  url: https://cio.ubc.ca/data-governance/data-governance-services/access-ubc-data
- group: other
  title: ''
  type: OpenData
  url: https://abacus.library.ubc.ca/dataverse/ubc_open
- group: other
  title: ''
  type: ResearchRepository
  url: https://abacus.library.ubc.ca/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.library.ubc.ca/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://calendar.ubc.ca/
- group: other
  title: ''
  type: IdentityFederation
  url: https://authentication.ubc.ca/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://arc.ubc.ca/
- group: other
  title: ''
  type: AIPolicy
  url: https://genai.ubc.ca/guidance/principles/
- group: build
  title: ''
  type: AITooling
  url: https://genai.ubc.ca/
- group: design
  title: ''
  type: Conformance
  url: conformance/ubc-domain-standards-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ubc-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/ubc-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/ubc-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ubc-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ubc-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ubc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubc-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ubc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ubc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ubc-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of British Columbia is a public research university with campuses in Vancouver and Kelowna, British Columbia, and a member of Canada''s U15 research group. Its programmable footprint is real but narrow, and almost all of it sits in UBC Library rather than in central IT. UBC Library operates the Open Collections API over the university''s digitized archival and research collections, a IIIF Presentation endpoint over the same items, and the Abacus research-data repository — a Dataverse 5.9 deployment on UBC''s own infrastructure that also serves a live OAI-PMH archive emitting DataCite kernel-4 and DDI Codebook metadata. Central IT publishes exactly one machine-readable artifact to the open internet: the SAML metadata for UBC''s own Shibboleth identity provider at authentication.ubc.ca. Everything else the Office of the CIO runs is deliberately closed — the Integration Enablement Centre''s MuleSoft gateway answers at api.ubc.ca with a flat 403, its API catalogue
  sits behind UBC''s Confluence login, and entitlement is granted per-API through a Data Access Framework request rather than a developer portal. There is no public course, timetable or registrar API; course planning moved into Workday and the community projects that fill the gap are student-built and not endorsed by the university. UBC has no central developer portal, no API changelog and no deprecation policy, and every ubc.ca host sits behind a bot defence that answers automated clients with an HTML block page carrying HTTP 200.'
examples:
- key_count: 4
  name: Ubc Get Dataverse Example
  slug: ubc-get-dataverse-example
- key_count: 2
  name: Ubc Open Collections Collection Example
  slug: ubc-open-collections-collection-example
- key_count: 2
  name: Ubc Open Collections Items Example
  slug: ubc-open-collections-items-example
- key_count: 2
  name: Ubc Open Collections Search Example
  slug: ubc-open-collections-search-example
- key_count: 4
  name: Ubc Search Datasets Example
  slug: ubc-search-datasets-example
finops:
- name: Ubc Finops
  service_category: Education
  slug: ubc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ubc.png
json_schemas:
- name: UBC Abacus Dataverse DataFile
  property_count: 14
  slug: ubc-datafile
- name: UBC Abacus Dataverse Dataset
  property_count: 16
  slug: ubc-dataset
- name: UBC Abacus Dataverse Collection
  property_count: 11
  slug: ubc-dataverse
json_structures:
- name: Ubc Dataset Structure
  property_count: 13
  slug: ubc-dataset-structure
- name: Ubc Dataverse Structure
  property_count: 8
  slug: ubc-dataverse-structure
jsonld:
- class_count: 15
  name: Ubc Context
  property_count: 9
  slug: ubc-context
layout: provider
modified: '2026-08-19'
name: University of British Columbia
nav: Providers
network: true
overview: 'University of British Columbia publishes 2 APIs on the [APIs.io](https://apis.io/) network: UBC Library Open Collections API and UBC Library Abacus Dataverse API. Tagged areas include Education, Higher Education, University, Public Research University, and Canada.


  The University of British Columbia catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of British Columbia''s developer surface includes documentation, API reference, engineering blog, status page, support, authentication, and 25 more developer resources.'
plans:
- name: Ubc Plans Pricing
  plan_count: 2
  slug: ubc-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Ubc Rate Limits
  slug: ubc-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of British Columbia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ubc-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: University of British Columbia API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: ubc-rules
scopes:
- name: Ubc Scopes
  scope_count: 0
  slug: ubc-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.0
  delta: -0.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 61.0
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 34.2
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 75.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ubc/refs/heads/main/screenshots/ubc-2026-06-20T195923.png
security:
- kind: authentication
  name: Ubc Authentication
  slug: ubc-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ubc Domain Security
  slug: ubc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ubc Vulnerability Disclosure
  slug: ubc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ubc
tags:
- Education
- Higher Education
- University
- Public Research University
- Canada
- British Columbia
- U15
- Library
- Digital Collections
- Research Data
- Research Repository
- Open Data
- Identity Federation
- OAI-PMH
- IIIF
- Dataverse
website: https://www.ubc.ca/
---
