---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Openeo Agentic Access
  operation_count: 51
  slug: openeo-agentic-access
  summary_line: 51 operations · 20 acting · 1 human-in-the-loop
api_count: 8
apis:
- baseURL_template: https://openeo.example/api/{version}
  baseurl_source: spec_template
  description: The following endpoints handle user profiles, accounting and authentication. See also [Authentication](#section/Authentication). In general, the openEO API only defines a minimum subset of user manage
  name: openEO Account Management API
  slug: openeo-account-management-api
- baseURL_template: https://openeo.example/api/{version}
  baseurl_source: spec_template
  description: Management of batch processing tasks (jobs) and their results.
  name: openEO Batch Jobs API
  slug: openeo-batch-jobs-api
- baseURL_template: https://openeo.example/api/{version}
  baseurl_source: spec_template
  description: General information about the API implementation and other supported capabilities provided by the back-end.
  name: openEO Capabilities API
  slug: openeo-capabilities-api
- baseURL_template: https://openeo.example/api/{version}
  baseurl_source: spec_template
  description: Organizes and manages data processing on the back-end, either as synchronous on-demand computation or batch jobs.
  name: openEO Data Processing API
  slug: openeo-data-processing-api
- baseURL_template: https://openeo.example/api/{version}
  baseurl_source: spec_template
  description: 'These endpoints allow to list the collections that are available at the back-end and can be used as data cubes for data processing. ## STAC For data discovery of Earth Observation Collections at the b'
  name: openEO EO Data Discovery API
  slug: openeo-eo-data-discovery-api
- baseURL_template: https://openeo.example/api/{version}
  baseurl_source: spec_template
  description: Management of user-uploaded assets and processed data.
  name: openEO File Storage API
  slug: openeo-file-storage-api
- baseURL_template: https://openeo.example/api/{version}
  baseurl_source: spec_template
  description: Management of commercial data orders
  name: openEO Orders API
  slug: openeo-orders-api
- baseURL_template: https://openeo.example/api/{version}
  baseurl_source: spec_template
  description: The process discovery endpoints provide details about the predefined processes that are available at the back-end. To list user-defined processes see '[User-Defined Processes](#tag/User-Defined-Proces
  name: openEO Process Discovery API
  slug: openeo-process-discovery-api
- baseURL_template: https://openeo.example/api/{version}
  baseurl_source: spec_template
  description: On-demand access to data using other web service protocols.
  name: openEO Secondary Services API
  slug: openeo-secondary-services-api
- baseURL_template: https://openeo.example/api/{version}
  baseurl_source: spec_template
  description: These endpoints allow to store and manage user-defined processes with their process graphs at the back-end.
  name: openEO User-Defined Processes API
  slug: openeo-user-defined-processes-api
- baseURL_template: https://openeo.example/api/{version}
  baseurl_source: spec_template
  description: Management of User Workspaces
  name: openEO Workspaces API
  slug: openeo-workspaces-api
artifact_total: 35
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/agentic-access/openeo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/openeo-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/rules/openeo-rules.yml
  title: ''
  type: Spectral
  url: rules/openeo-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/rules/openeo-openeo-api-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/openeo-openeo-api-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/json-ld/openeo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openeo-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/vocabulary/openeo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openeo-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/data-model/openeo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openeo-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/cli/openeo-cli.yml
  title: ''
  type: CLI
  url: cli/openeo-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/changelog/openeo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/openeo-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/conventions/openeo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/openeo-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/lifecycle/openeo-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/openeo-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/lifecycle/openeo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/openeo-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/errors/openeo-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/openeo-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/errors/openeo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/openeo-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/conformance/openeo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openeo-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/overlays/openeo-commercial-data-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/openeo-commercial-data-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/well-known/openeo-bsky-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/openeo-bsky-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/well-known/openeo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/openeo-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/hosts/openeo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openeo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/vendors/openeo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openeo-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/packages/openeo-packages.yml
  title: ''
  type: SDKs
  url: packages/openeo-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/packages/openeo-packages.yml
  title: ''
  type: Packages
  url: packages/openeo-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/radiantearth/stac-spec/releases
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/authentication/openeo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openeo-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/security/openeo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openeo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openeo.org/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/Open-EO/openeo-api/blob/1881dae18b3c2c417f1305774cf295c81d60d400/.spectral.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.openeo.org/
- group: docs
  title: ''
  type: Documentation
  url: https://openeo.org/documentation/1.0/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openeo.org/documentation/1.0/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://openeo.org/documentation/1.0/developers/clients/getting-started.html
- group: auth
  title: ''
  type: Authentication
  url: https://openeo.org/documentation/1.0/authentication.html
- group: docs
  title: ''
  type: ProcessesReference
  url: https://processes.openeo.org/
- group: other
  title: ''
  type: Hub
  url: https://hub.openeo.org/
- group: other
  title: ''
  type: WebEditor
  url: https://editor.openeo.org/
- group: other
  title: ''
  type: Software
  url: https://openeo.org/software.html
- group: company
  title: ''
  type: About
  url: https://openeo.org/about.html
- group: operate
  title: ''
  type: Support
  url: https://openeo.org/contact.html
- group: company
  title: ''
  type: Blog
  url: https://openeo.org/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Open-EO
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openeospec/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCMJQil8j9sHBQkcSlSaEsvQ
- group: company
  title: ''
  type: Bluesky
  url: https://bsky.app/profile/openeo.org
created: '2026-10-09'
description: openEO develops an open application programming interface (API) that connects clients like R, Python and JavaScript to big Earth observation (EO) cloud back-ends in a simple and unified way, so each client can work with every back-end and back-ends can be compared on capacity, cost and results. The openEO API specification, process definitions, client libraries (Python, R, JavaScript, Julia, QGIS plugin) and web editor are open source under Apache 2.0, governed by a Project Steering Committee, and openEO is recognised as an OGC Community Standard.
image: https://openeo.org/images/openeo_logo.png
json_schemas:
- name: Batch Job Results Response as STAC Item
  property_count: 9
  slug: openeo-batch-job-result
- name: Batch Job
  property_count: 17
  slug: openeo-batch-job
- name: Collection
  property_count: 16
  slug: openeo-collection
- name: Create workspace
  property_count: 3
  slug: openeo-create-workspace
- name: JSON Schema
  property_count: 10
  slug: openeo-json-schema
- name: order_id
  property_count: 0
  slug: openeo-order-id
- name: order_parameters
  property_count: 0
  slug: openeo-order-parameters
- name: Order
  property_count: 11
  slug: openeo-order
- name: Process
  property_count: 11
  slug: openeo-process
- name: Creation Parameters
  property_count: 0
  slug: openeo-processing-create-parameters
- name: register_workspace
  property_count: 4
  slug: openeo-register-workspace
- name: Resource Parameter
  property_count: 4
  slug: openeo-resource-parameter
- name: workspace_description
  property_count: 0
  slug: openeo-workspace-description
- name: workspace_id
  property_count: 0
  slug: openeo-workspace-id
- name: Workspace
  property_count: 7
  slug: openeo-workspace
- name: workspace_title
  property_count: 0
  slug: openeo-workspace-title
jsonld:
- class_count: 38
  name: Openeo Context
  property_count: 76
  slug: openeo-context
layout: provider
modified: '2026-10-09'
name: openEO
nav: Providers
network: true
overview: 'openEO publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Management API, Batch Jobs API, Capabilities API, and 8 more. Tagged areas include Company, Earth Observation, Geospatial, Remote Sensing, and Cloud Processing.


  The openEO catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  openEO''s developer surface includes CLI, changelog, authentication, API reference, documentation, getting-started guide, support, and 36 more developer resources.'
plans:
- name: Openeo Plans Pricing
  plan_count: 0
  slug: openeo-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Openeo Rate Limits
  slug: openeo-rate-limits
rules:
- authorship: provider
  effective_rule_count: 43
  extends:
  - spectral:oas
  name: openEO — openeo api rules
  rule_count: 2
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 2
  slug: openeo-openeo-api-spectral-rules
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: openEO API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 2
  slug: openeo-rules
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 0.0
    contract_governance: 35.6
    contract_quality: 70.1
    developer_ergonomics: 73.2
    discoverability: 62.5
    operational_transparency: 28.9
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/openeo/refs/heads/main/screenshots/openeo-2026-10-11T112048.png
security:
- kind: authentication
  name: Openeo Authentication
  slug: openeo-authentication
  summary_line: http/unknown · 3 schemes
- kind: domain-security
  name: Openeo Domain Security
  slug: openeo-domain-security
  summary_line: TLSv1.3 · HSTS
slug: openeo
tags:
- Company
- Earth Observation
- Geospatial
- Remote Sensing
- Cloud Processing
- Open Source
- API Specification
- Data Cubes
website: https://openeo.org/
---
