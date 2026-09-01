---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The core open-source Tuva dbt package that transforms healthcare data from the Tuva Input Layer into the Tuva Core Data Model and Data Marts, including data-quality tests, normalization, claims prepro
  name: The Tuva Project (dbt package)
  slug: the-tuva-project
- description: An open-source Python utility that flattens nested HL7 FHIR JSON (bundles / resources) into tabular CSV files so FHIR-sourced data can be loaded and mapped into the Tuva Input Layer. A command-line da
  name: FHIR Inferno
  slug: fhir-inferno
- description: 'A family of open-source dbt connector projects (Medicare CCLF, BCDA, CMS synthetic, Aetna, BCBS, and a connector template, plus a FHIR preprocessing connector) that map raw claims, EHR, ADT, and FHIR '
  name: Tuva Connectors
  slug: tuva-connectors
- description: The config API from Tuva Health — 1 operation(s) for config.
  name: Tuva Health Config API
  slug: tuva-health-config-api
- description: The data-sources API from Tuva Health — 1 operation(s) for data-sources.
  name: Tuva Health Data Sources API
  slug: tuva-health-data-sources-api
- description: The health-check API from Tuva Health — 1 operation(s) for health-check.
  name: Tuva Health Health Check API
  slug: tuva-health-health-check-api
- description: The matches API from Tuva Health — 1 operation(s) for matches.
  name: Tuva Health Matches API
  slug: tuva-health-matches-api
- description: The person-records API from Tuva Health — 2 operation(s) for person-records.
  name: Tuva Health Person Records API
  slug: tuva-health-person-records-api
- description: The persons API from Tuva Health — 2 operation(s) for persons.
  name: Tuva Health Persons API
  slug: tuva-health-persons-api
- description: The potential-matches API from Tuva Health — 2 operation(s) for potential-matches.
  name: Tuva Health Potential Matches API
  slug: tuva-health-potential-matches-api
- description: The users API from Tuva Health — 2 operation(s) for users.
  name: Tuva Health Users API
  slug: tuva-health-users-api
artifact_total: 15
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/tuva-health/tuva/blob/main/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tuva-health-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/tuva-health/tuva/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/tuva-health/tuva/releases
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tuva-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tuvahealth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://thetuvaproject.com
- group: docs
  title: ''
  type: Documentation
  url: https://thetuvaproject.com/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://thetuvaproject.com/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tuva-health
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tuva-health
- group: build
  title: ''
  type: Package
  url: https://hub.getdbt.com/tuva-health/the_tuva_project/latest/
- group: build
  title: ''
  type: Packages
  url: packages/tuva-health-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tuva-health-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tuva-health-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tuva-health-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tuva-health-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tuva-health-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://thetuvaproject.substack.com
- group: operate
  title: ''
  type: Support
  url: https://www.tuvahealth.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tuvahealth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tuvahealth.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://tuva-health.github.io/tuva_empi/api-docs/
- group: auth
  title: ''
  type: Authentication
  url: authentication/tuva-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tuva-health-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tuva-health-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://tuva-health.github.io/tuva_empi/docs/releases
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tuva-health-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/tuva-health-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tuva-health-plans-pricing.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tuva-health-empi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Community
  url: https://thetuvaproject.com/community/community-overview
created: '2026-07-24'
description: 'Tuva Health, Inc. is a United States healthcare data company behind The Tuva Project, an open-source, warehouse-native data-transformation platform that harmonizes, validates, normalizes, and enriches raw healthcare data - medical and pharmacy claims, EHR clinical data, ADT feeds, and HL7 FHIR sources - into an analytics-ready Core Data Model and a library of Data Marts (AHRQ measures, readmissions, quality measures, chronic conditions, CCSR, pharmacy). It is delivered primarily as a dbt package plus Python utilities (FHIR Inferno) and a family of source connectors that run inside the customer''s own cloud data warehouse - Snowflake, Databricks, Google BigQuery, Amazon Redshift, or Microsoft Fabric - rather than as a hosted service. Tuva is not a FHIR API vendor: FHIR R4 is a supported input format that Tuva flattens and maps into its Input Layer, not a live FHIR server it operates. It does ship one HTTP API - Tuva EMPI, an Apache-2.0 enterprise master patient index with a
  documented OpenAPI 3.0.3 contract - but that too is customer-deployed from OCI images, so there is no Tuva-operated API host. The company pairs the open-source project with a commercial Core Platform and named services. Home market is the United States.'
image: https://www.tuvahealth.com/img/TuvaHealthLogo-White@4x.png
layout: provider
modified: '2026-08-15'
name: Tuva Health
nav: Providers
network: true
overview: 'Tuva Health publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Config API, Data Sources API, Health Check API, and 5 more. Tagged areas include Healthcare, United States, Health Data, FHIR, and Interoperability.


  Tuva Health''s developer surface includes documentation, getting-started guide, changelog, engineering blog, support, API reference, authentication, and 26 more developer resources.'
plans:
- name: Tuva Health Plans Pricing
  plan_count: 0
  slug: tuva-health-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Tuva Health Rate Limits
  slug: tuva-health-rate-limits
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 41.2
    developer_ergonomics: 80.4
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 43.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tuva-health/refs/heads/main/screenshots/tuva-health-2026-08-17T082502.png
security:
- kind: authentication
  name: Tuva Health Authentication
  slug: tuva-health-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Tuva Health Domain Security
  slug: tuva-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tuva-health
tags:
- Healthcare
- United States
- Health Data
- FHIR
- Interoperability
- Data Analytics
- Data Transformation
- Claims
- Open-Source
- dbt
- EMPI
- Patient Matching
website: https://www.tuvahealth.com
---
