---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 3
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
artifact_total: 4
common:
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
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tuvahealth.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.tuvahealth.com/contact
created: '2026-07-24'
description: 'Tuva Health, Inc. is a United States healthcare data company behind The Tuva Project, an open-source, warehouse-native data-transformation platform that harmonizes, validates, normalizes, and enriches raw healthcare data - medical and pharmacy claims, EHR clinical data, ADT feeds, and HL7 FHIR sources - into an analytics-ready Core Data Model and a library of Data Marts (AHRQ measures, readmissions, quality measures, chronic conditions, CCSR, pharmacy). It is delivered primarily as a dbt package plus Python utilities (FHIR Inferno) and a family of source connectors that run inside the customer''s own cloud data warehouse - Snowflake, Databricks, Google BigQuery, Amazon Redshift, or Microsoft Fabric - rather than as a hosted service. Tuva is not an HTTP or FHIR API vendor: FHIR R4 is a supported input format that Tuva flattens and maps into its Input Layer, not a live FHIR server it operates. The company pairs the open-source project with a commercial Core Platform. Home market
  is the United States.'
image: https://www.tuvahealth.com/img/TuvaHealthLogo-White@4x.png
layout: provider
modified: '2026-07-24'
name: Tuva Health
nav: Providers
network: true
overview: 'Tuva Health publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Health Data, FHIR, and Interoperability.


  Tuva Health''s developer surface includes documentation, getting-started guide, changelog, engineering blog, pricing, support, and 11 more developer resources.'
random_paper: 106
score:
  band: emerging
  composite: 20.6
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 72.2
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 20.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
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
- Open Source
- dbt
website: https://www.tuvahealth.com
---
