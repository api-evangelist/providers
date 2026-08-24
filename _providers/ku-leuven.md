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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 254
  human_in_the_loop: 7
  name: Ku Leuven Agentic Access
  operation_count: 536
  slug: ku-leuven-agentic-access
  summary_line: 536 operations · 254 acting · 7 human-in-the-loop
api_count: 49
apis:
- description: ICTS Data Services REST API exposing public personnel / who-is-who person information. An expanded intranet variant requires a service account.
  name: KU Leuven Person Information API
  slug: person
- description: ICTS Data Services REST API exposing public educational offering data, including programs (opleidingen) and course components.
  name: KU Leuven Educational Offering (Onderwijsaanbod) API
  slug: program
- description: ICTS Data Services REST API exposing public organizational-structure information matching the institutional organizational chart. An expanded intranet variant is available via service account.
  name: KU Leuven Organizational Chart (Organigram) API
  slug: organigram
- description: ICTS Data Services REST API exposing public job vacancy / job posting data.
  name: KU Leuven Vacancies (Vacatures) API
  slug: vacancies
- description: ICTS Data Services API exposing an individual's personal timetable. Protected by OAuth 2.0 (authorization code grant) with SAML as a fallback; OAuth client credentials are issued by KU Leuven on reque
  name: KU Leuven Individual Timetable (Uurrooster) API
  slug: timetable
- description: The Access API from KU Leuven — 23 operation(s) for access.
  name: KU Leuven Access API
  slug: ku-leuven-access-api
- description: Uploads a set of files to a dataset
  name: KU Leuven addFilesToDataset API
  slug: ku-leuven-addfilestodataset-api
- description: Uploads a file for a dataset
  name: KU Leuven addFileToDataset API
  slug: ku-leuven-addfiletodataset-api
- description: Uploads a Globus file for a dataset
  name: KU Leuven addGlobusFilesToDataset API
  slug: ku-leuven-addglobusfilestodataset-api
- description: The Admin API from KU Leuven — 131 operation(s) for admin.
  name: KU Leuven Admin API
  slug: ku-leuven-admin-api
- description: The Batch API from KU Leuven — 3 operation(s) for batch.
  name: KU Leuven Batch API
  slug: ku-leuven-batch-api
- description: The Builtin Users API from KU Leuven — 4 operation(s) for builtin users.
  name: KU Leuven Builtin Users API
  slug: ku-leuven-builtin-users-api
- description: The Datasetfields API from KU Leuven — 1 operation(s) for datasetfields.
  name: KU Leuven Datasetfields API
  slug: ku-leuven-datasetfields-api
- description: The Datasets API from KU Leuven — 92 operation(s) for datasets.
  name: KU Leuven Datasets API
  slug: ku-leuven-datasets-api
- description: The Datatags API from KU Leuven — 1 operation(s) for datatags.
  name: KU Leuven Datatags API
  slug: ku-leuven-datatags-api
- description: The DataverseFeaturedItems API from KU Leuven — 1 operation(s) for dataversefeatureditems.
  name: KU Leuven DataverseFeaturedItems API
  slug: ku-leuven-dataversefeatureditems-api
- description: The Dataverses API from KU Leuven — 39 operation(s) for dataverses.
  name: KU Leuven Dataverses API
  slug: ku-leuven-dataverses-api
- description: The Edit API from KU Leuven — 1 operation(s) for edit.
  name: KU Leuven Edit API
  slug: ku-leuven-edit-api
- description: The ExternalTools API from KU Leuven — 2 operation(s) for externaltools.
  name: KU Leuven ExternalTools API
  slug: ku-leuven-externaltools-api
- description: The Files API from KU Leuven — 20 operation(s) for files.
  name: KU Leuven Files API
  slug: ku-leuven-files-api
- description: The Harvest API from KU Leuven — 7 operation(s) for harvest.
  name: KU Leuven Harvest API
  slug: ku-leuven-harvest-api
- description: The Inbox API from KU Leuven — 1 operation(s) for inbox.
  name: KU Leuven Inbox API
  slug: ku-leuven-inbox-api
- description: The Info API from KU Leuven — 49 operation(s) for info.
  name: KU Leuven Info API
  slug: ku-leuven-info-api
- description: The Ingest API from KU Leuven — 1 operation(s) for ingest.
  name: KU Leuven Ingest API
  slug: ku-leuven-ingest-api
- description: The Licenses API from KU Leuven — 6 operation(s) for licenses.
  name: KU Leuven Licenses API
  slug: ku-leuven-licenses-api
- description: The Localcontexts API from KU Leuven — 2 operation(s) for localcontexts.
  name: KU Leuven Localcontexts API
  slug: ku-leuven-localcontexts-api
- description: The Logout API from KU Leuven — 1 operation(s) for logout.
  name: KU Leuven Logout API
  slug: ku-leuven-logout-api
- description: The Mail API from KU Leuven — 1 operation(s) for mail.
  name: KU Leuven Mail API
  slug: ku-leuven-mail-api
- description: The Meta API from KU Leuven — 2 operation(s) for meta.
  name: KU Leuven Meta API
  slug: ku-leuven-meta-api
- description: The Metadatablocks API from KU Leuven — 2 operation(s) for metadatablocks.
  name: KU Leuven Metadatablocks API
  slug: ku-leuven-metadatablocks-api
- description: The Mydata API from KU Leuven — 1 operation(s) for mydata.
  name: KU Leuven Mydata API
  slug: ku-leuven-mydata-api
- description: The Notifications API from KU Leuven — 6 operation(s) for notifications.
  name: KU Leuven Notifications API
  slug: ku-leuven-notifications-api
- description: The Pids API from KU Leuven — 6 operation(s) for pids.
  name: KU Leuven Pids API
  slug: ku-leuven-pids-api
- description: Replace a file to a dataset
  name: KU Leuven replaceFilesInDataset API
  slug: ku-leuven-replacefilesindataset-api
- description: The Roles API from KU Leuven — 3 operation(s) for roles.
  name: KU Leuven Roles API
  slug: ku-leuven-roles-api
- description: Save Auxiliary File With Version
  name: KU Leuven saveAuxiliaryFileWithVersion API
  slug: ku-leuven-saveauxiliaryfilewithversion-api
- description: The Search API from KU Leuven — 2 operation(s) for search.
  name: KU Leuven Search API
  slug: ku-leuven-search-api
- description: The Sendfeedback API from KU Leuven — 1 operation(s) for sendfeedback.
  name: KU Leuven Sendfeedback API
  slug: ku-leuven-sendfeedback-api
- description: Uploads a logo for a dataset
  name: KU Leuven uploadDatasetLogo API
  slug: ku-leuven-uploaddatasetlogo-api
- description: The Users API from KU Leuven — 10 operation(s) for users.
  name: KU Leuven Users API
  slug: ku-leuven-users-api
- description: The Workflows API from KU Leuven — 1 operation(s) for workflows.
  name: KU Leuven Workflows API
  slug: ku-leuven-workflows-api
- description: The institution's central programmable surface, operated by KU Leuven ICTS on its own host and its own address space. dataservice.kuleuven.be fronts eight public OpenSearch index families — employee (
  name: KU Leuven ICTS Data Services API (OpenSearch gateway)
  slug: data-services
- description: ICTS Data Services index of academic curriculum and CV records — discipline codes, research topics and the researcher's ORCID iD in the `orcId` field. Confirmed live 2026-08-19. This is the surface th
  name: KU Leuven Curriculum Information (Curriculuminformatie) API
  slug: curriculum
- description: ICTS Data Services index over the KU Leuven research database, the richest surface in the estate. Beyond free search it publishes three stored search templates — projectsbyou (by organigram unit code)
  name: KU Leuven Research Projects (Onderzoeksprojecten) API
  slug: research-projects
- description: ICTS Data Services index of research groups, 740 records live on 2026-08-19, joined to projects and to the organisational chart by unit code. Supports _search and _doc/{id} retrieval with _source fiel
  name: KU Leuven Research Teams (Onderzoeksteams) API
  slug: research-teams
- description: ICTS Data Services index of core facilities and shared research equipment, 379 records live on 2026-08-19. A machine-readable research-facility catalogue is an uncommon institutional surface and one o
  name: KU Leuven Research Infrastructure (Onderzoeksinfrastructuur) API
  slug: research-infrastructure
- description: OAI-PMH 2.0 interface of the Research Data Repository, served from KU Leuven's own host. Identify returned repositoryName "KU Leuven RDR Dataverse OAI Archive", adminEmail rdm@kuleuven.be, earliestDat
  name: KU Leuven RDR OAI-PMH Harvesting Interface
  slug: rdr-oai-pmh
- description: 'Lirias is the institutional publication repository of the KU Leuven Association, running on KU Leuven''s own host and address space. Its OAI-PMH 2.0 Identify response returned repositoryName "Lirias - '
  name: Lirias OAI-PMH Harvesting Interface
  slug: lirias-oai-pmh
- description: KU Leuven serves its own SAML 2.0 federation metadata from idp.kuleuven.be, which resolves to 134.58.64.219 inside the university's own address space — institution-operated, not a hosted IdP tenant. e
  name: KU Leuven Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: identity-federation
artifact_total: 110
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access API
  slug: open-ku-leuven-access-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access addFilesToDataset API
  slug: open-ku-leuven-addfilestodataset-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access addFileToDataset API
  slug: open-ku-leuven-addfiletodataset-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access addGlobusFilesToDataset API
  slug: open-ku-leuven-addglobusfilestodataset-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Admin API
  slug: open-ku-leuven-admin-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Batch API
  slug: open-ku-leuven-batch-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Builtin Users API
  slug: open-ku-leuven-builtin-users-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Datasetfields API
  slug: open-ku-leuven-datasetfields-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Datasets API
  slug: open-ku-leuven-datasets-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Datatags API
  slug: open-ku-leuven-datatags-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access DataverseFeaturedItems API
  slug: open-ku-leuven-dataversefeatureditems-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Dataverses API
  slug: open-ku-leuven-dataverses-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Edit API
  slug: open-ku-leuven-edit-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access ExternalTools API
  slug: open-ku-leuven-externaltools-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Files API
  slug: open-ku-leuven-files-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Harvest API
  slug: open-ku-leuven-harvest-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Inbox API
  slug: open-ku-leuven-inbox-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Info API
  slug: open-ku-leuven-info-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Ingest API
  slug: open-ku-leuven-ingest-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Licenses API
  slug: open-ku-leuven-licenses-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Localcontexts API
  slug: open-ku-leuven-localcontexts-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Logout API
  slug: open-ku-leuven-logout-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Mail API
  slug: open-ku-leuven-mail-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Meta API
  slug: open-ku-leuven-meta-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Metadatablocks API
  slug: open-ku-leuven-metadatablocks-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Mydata API
  slug: open-ku-leuven-mydata-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Notifications API
  slug: open-ku-leuven-notifications-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Pids API
  slug: open-ku-leuven-pids-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access replaceFilesInDataset API
  slug: open-ku-leuven-replacefilesindataset-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Roles API
  slug: open-ku-leuven-roles-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access saveAuxiliaryFileWithVersion API
  slug: open-ku-leuven-saveauxiliaryfilewithversion-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Search API
  slug: open-ku-leuven-search-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Sendfeedback API
  slug: open-ku-leuven-sendfeedback-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access uploadDatasetLogo API
  slug: open-ku-leuven-uploaddatasetlogo-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Users API
  slug: open-ku-leuven-users-api
- collection_type: open
  name: KU Leuven Research Data Repository (RDR) Access Workflows API
  slug: open-ku-leuven-workflows-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ku-leuven-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ku-leuven-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ku-leuven-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kuleuven.be
- group: start
  title: ''
  type: DeveloperPortal
  url: https://admin.kuleuven.be/icts/services/dataservices
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kuleuven
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ku-leuven/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/KU-Leuven-Libraries
- group: commercial
  title: ''
  type: Plans
  url: plans/ku-leuven-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ku-leuven-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ku-leuven-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: docs
  title: ''
  type: APIReference
  url: https://rdr.kuleuven.be/openapi
- group: docs
  title: ''
  type: Documentation
  url: https://www.kuleuven.be/rdm/en/rdr/api-documentation
- group: other
  title: ''
  type: OpenData
  url: https://admin.kuleuven.be/icts/services/dataservices
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.kuleuven.be/rdm/en/rdr
- group: other
  title: ''
  type: ResearchRepository
  url: https://lirias.kuleuven.be
- group: learn
  title: ''
  type: CourseCatalog
  url: https://onderwijsaanbod.kuleuven.be
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.kuleuven.be/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://admin.kuleuven.be/icts/onderzoek/hpc
- group: build
  title: ''
  type: LibraryCatalog
  url: https://bib.kuleuven.be
- group: other
  title: ''
  type: AIPolicy
  url: https://www.kuleuven.be/english/genai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://admin.kuleuven.be/icts/services/dataservices/gebruiksvoorwaarden.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kuleuven.be/privacy
- group: operate
  title: ''
  type: Support
  url: https://admin.kuleuven.be/icts/services/dataservices/data-service-vraag
- group: auth
  title: ''
  type: Security
  url: https://admin.kuleuven.be/icts/english/responsible-disclosure
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.kuleuven.be/.well-known/security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/ku-leuven-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ku-leuven-education-standards.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ku-leuven-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ku-leuven-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ku-leuven-scopes.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ku-leuven-vocabulary.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ku-leuven-data-services-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ku-leuven-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ku-leuven-data-services-search-response-schema.json
- group: design
  title: ''
  type: Rules
  url: rules/ku-leuven-rules.yml
created: '2026-06-03'
description: 'KU Leuven (Katholieke Universiteit Leuven) is a Flemish public research university in Leuven, Belgium, founded in 1425 and ranked in the QS world top 50. Re-profiled on 2026-08-19 with operator attribution settled before anything was saved, it is one of the few universities in this cohort whose machine-readable surface is genuinely its own: every host below resolves inside KU Leuven''s own 134.58.0.0/16 address space, and no Figshare, Elsevier Pure, Ex Libris or Symplectic contract is attributed here. Its central programmable surface is the ICTS Data Services gateway at dataservice.kuleuven.be — an unauthenticated OpenSearch query API over eight public index families covering the staff directory, academic CVs, the organisational chart, the programme guide, research projects, research teams, research infrastructure and job vacancies — documented in Dutch at admin.kuleuven.be and confirmed live returning real records. It also runs the Research Data Repository (RDR), a self-hosted
  Dataverse 6.7.1 installation at rdr.kuleuven.be that serves its own OpenAPI publicly, mints DOIs as DataCite repository client BRVZ.RDR, and exposes OAI-PMH; the Lirias institutional repository exposes a second OAI-PMH endpoint; and idp.kuleuven.be serves SAML 2.0 Shibboleth metadata registered in the Belnet federation with REFEDS SIRTFI and Research & Scholarship assurance. Honest caveats: the 36 RDR entries below are tag-splits of ONE Dataverse deployment, and that contract is upstream open-source Dataverse''s work — KU Leuven operates the deployment and owns the data, it does not author the API. There is no unified developer portal, no self-serve credential anywhere in the estate, no versioning on the data services gateway, and the personal timetable API''s production host does not resolve from the public internet.'
examples:
- key_count: 2
  name: Ku Leuven Data Services Error Example
  slug: ku-leuven-data-services-error-example
- key_count: 2
  name: Ku Leuven Data Services Search Example
  slug: ku-leuven-data-services-search-example
- key_count: 2
  name: Ku Leuven Dataset Example
  slug: ku-leuven-dataset-example
- key_count: 2
  name: Ku Leuven Info Version Example
  slug: ku-leuven-info-version-example
- key_count: 2
  name: Ku Leuven Organigram Unit Example
  slug: ku-leuven-organigram-unit-example
finops:
- name: Ku Leuven Finops
  service_category: Education
  slug: ku-leuven-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ku-leuven.png
json_schemas:
- name: KU Leuven ICTS Data Services Search Response
  property_count: 5
  slug: ku-leuven-data-services-search-response
- name: KU Leuven RDR DataFile
  property_count: 12
  slug: ku-leuven-datafile
- name: KU Leuven RDR Dataset
  property_count: 14
  slug: ku-leuven-dataset
- name: KU Leuven RDR DatasetVersion
  property_count: 13
  slug: ku-leuven-datasetversion
- name: KU Leuven RDR Info Version Response
  property_count: 2
  slug: ku-leuven-info-version
json_structures:
- name: Ku Leuven Datafile Structure
  property_count: 11
  slug: ku-leuven-datafile-structure
- name: Ku Leuven Dataset Structure
  property_count: 14
  slug: ku-leuven-dataset-structure
- name: Ku Leuven Datasetversion Structure
  property_count: 12
  slug: ku-leuven-datasetversion-structure
jsonld:
- class_count: 16
  name: Ku Leuven Context
  property_count: 3
  slug: ku-leuven-context
layout: provider
modified: '2026-08-19'
name: KU Leuven
nav: Providers
network: true
overview: 'KU Leuven publishes 37 APIs on the [APIs.io](https://apis.io/) network, including Access API, addFilesToDataset API, addFileToDataset API, and 34 more. Tagged areas include University, Higher Education, Education, Belgium, and Europe.


  The KU Leuven catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  KU Leuven''s developer surface includes API reference, documentation, support, authentication, and 33 more developer resources.'
plans:
- name: Ku Leuven Plans Pricing
  plan_count: 2
  slug: ku-leuven-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Ku Leuven Rate Limits
  slug: ku-leuven-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: KU Leuven API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ku-leuven-jsonschema-spectral-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: KU Leuven API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 2
  slug: ku-leuven-rules
scopes:
- name: Ku Leuven Scopes
  scope_count: 0
  slug: ku-leuven-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.1
  delta: -0.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 17.4
    contract_quality: 50.5
    developer_ergonomics: 42.9
    discoverability: 61.1
    governance: 17.4
    operational_transparency: 34.2
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 2.7
      total: 37
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 75.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ku-leuven/refs/heads/main/screenshots/ku-leuven-2026-06-20T184201.png
security:
- kind: authentication
  name: Ku Leuven Authentication
  slug: ku-leuven-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ku Leuven Domain Security
  slug: ku-leuven-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ku Leuven Vulnerability Disclosure
  slug: ku-leuven-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ku-leuven
tags:
- University
- Higher Education
- Education
- Belgium
- Europe
- Flanders
- Research Data
- Research Repository
- Open Data
- Course Catalog
- Identity Federation
- OAI-PMH
- Dataverse
- OpenSearch
- Public Research University
website: https://www.kuleuven.be
---
