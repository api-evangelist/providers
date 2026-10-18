---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Unity Catalog Agentic Access
  operation_count: 54
  slug: unity-catalog-agentic-access
  summary_line: 54 operations · 33 acting
api_count: 1
apis:
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: A catalog is the first layer of Unity Catalog’s three-level namespace. It’s used to organize your data assets.
  name: Unity Catalog Catalogs API
  slug: unity-catalog-catalogs-api
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: The Credentials API from Unity Catalog — 2 operation(s) for credentials.
  name: Unity Catalog Credentials API
  slug: unity-catalog-credentials-api
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: '"Delta commits" is a Delta tables feature that allows Delta tables to designate a coordinator to coordinate commits. This is Unity Catalog''s API to allow Unity Catalog be the commit coordinator for ma'
  name: Unity Catalog Delta Commits API
  slug: unity-catalog-deltacommits-api
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: The External Locations API from Unity Catalog — 2 operation(s) for external locations.
  name: Unity Catalog External Locations API
  slug: unity-catalog-external-locations-api
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: 'Functions implement User-Defined Functions (UDFs) in Unity Catalog. The function implementation can be a SQL expression/query or a python function, and it can be invoked wherever a table reference is '
  name: Unity Catalog Functions API
  slug: unity-catalog-functions-api
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: The Grants API from Unity Catalog — 1 operation(s) for grants.
  name: Unity Catalog Grants API
  slug: unity-catalog-grants-api
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: A metastore is the top-level container of objects in Unity Catalog that stores all UC assets.
  name: Unity Catalog Metastores API
  slug: unity-catalog-metastores-api
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: A schema (also called a database) is the second layer of Unity Catalog’s three-level namespace. A schema organizes tables, volumes and functions.
  name: Unity Catalog Schemas API
  slug: unity-catalog-schemas-api
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: A table resides in the third layer of Unity Catalog’s three-level namespace. It contains rows of data. A table can be managed or external.
  name: Unity Catalog Tables API
  slug: unity-catalog-tables-api
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: Temporary credentials are used to access storage locations or assets for a limited lifetime.
  name: Unity Catalog Temporary Credentials API
  slug: unity-catalog-temporarycredentials-api
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: 'Volumes are a Unity Catalog capability for accessing, storing, governing, organizing and processing files. Use cases include running machine learning on unstructured data such as image, audio, video, '
  name: Unity Catalog Volumes API
  slug: unity-catalog-volumes-api
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: Model versions contain all artifact files associated with an individual machine learning model. They are associated with a single parent model and have an integer identifier, indicating the version nu
  name: Unity Catalog Model Versions API
  slug: unity-catalog-model-versions-api
- baseURL: https://api.unitycatalog.io
  baseurl_source: declared
  description: Registered models are machine learning models that are stored within the Unity Catalog model registry. They are comprised of all versions of a single model that a user wishes to keep. A registered mod
  name: Unity Catalog Registered Models API
  slug: unity-catalog-registered-models-api
artifact_total: 24
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/unity-catalog/refs/heads/main/agentic-access/unity-catalog-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/unity-catalog-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unity-catalog/refs/heads/main/rules/unity-catalog-rules.yml
  title: ''
  type: Spectral
  url: rules/unity-catalog-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unity-catalog/refs/heads/main/json-ld/unity-catalog-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/unity-catalog-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unity-catalog/refs/heads/main/vocabulary/unity-catalog-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/unity-catalog-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unity-catalog/refs/heads/main/data-model/unity-catalog-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unity-catalog-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unity-catalog/refs/heads/main/authentication/unity-catalog-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unity-catalog-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unity-catalog/refs/heads/main/errors/unity-catalog-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/unity-catalog-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/unity-catalog/refs/heads/main/conformance/unity-catalog-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unity-catalog-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/unity-catalog/refs/heads/main/hosts/unity-catalog-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unity-catalog-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/unity-catalog/refs/heads/main/vendors/unity-catalog-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unity-catalog-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unitycatalog.io/quickstart/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/unity-catalog/refs/heads/main/security/unity-catalog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unity-catalog-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unitycatalog.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unitycatalog.io
- group: docs
  title: ''
  type: APIReference
  url: https://go.unitycatalog.io/apidocs
- group: company
  title: ''
  type: Blog
  url: https://unitycatalog.io/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unitycatalog
- group: operate
  title: ''
  type: SlackCommunity
  url: https://join.slack.com/t/unitycatalog/shared_invite/zt-3f93k8flt-Ent43H6MQQYNN52Ca_eRMQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unitycatalog
created: '2026-10-13'
description: Unity Catalog provides an industry‑first universal catalog for data and AI, enabling organizations to manage, discover, and govern data assets across multiple formats, engines, and environments. The platform offers multimodal interfaces, extensive integrations with tools like Spark, DuckDB, and LangChain, and supports AI workloads through dedicated APIs. It includes features for tables, functions, models, and user privileges, along with robust security and governance capabilities.
image: https://unitycatalog.netlify.app/images/default-image.jpg
json_schemas:
- name: DeltaCommit
  property_count: 6
  slug: unity-catalog-delta-commit
- name: FunctionInfo
  property_count: 26
  slug: unity-catalog-function-info
- name: ModelVersionInfo
  property_count: 14
  slug: unity-catalog-model-version-info
- name: RegisteredModelInfo
  property_count: 12
  slug: unity-catalog-registered-model-info
- name: SchemaInfo
  property_count: 13
  slug: unity-catalog-schema-info
- name: TableInfo
  property_count: 17
  slug: unity-catalog-table-info
jsonld:
- class_count: 84
  name: Unity Catalog Context
  property_count: 118
  slug: unity-catalog-context
layout: provider
modified: '2026-10-13'
name: Unity Catalog
nav: Providers
network: true
overview: 'Unity Catalog publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalogs API, Credentials API, Delta Commits API, and 10 more. Tagged areas include Data, Artificial Intelligence, Catalog, Governance, and Multi-Modal.


  The Unity Catalog catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Unity Catalog''s developer surface includes authentication, getting-started guide, documentation, API reference, engineering blog, and 14 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Unity Catalog API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: unity-catalog-rules
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 54.3
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 15.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Unity Catalog Authentication
  slug: unity-catalog-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Unity Catalog Domain Security
  slug: unity-catalog-domain-security
  summary_line: TLSv1.3 · HSTS
slug: unity-catalog
tags:
- Data
- Artificial Intelligence
- Catalog
- Governance
- Multi-Modal
website: https://www.unitycatalog.io
---
