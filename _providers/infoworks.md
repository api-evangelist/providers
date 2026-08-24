---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The Infoworks v3 REST API — 369 paths and 510 operations across 62 tag groupings — for onboarding sources, crawling and ingesting tables, building pipelines and pipeline groups, scheduling and running
  name: Infoworks REST API v3
  slug: infoworks-rest-api-v3
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.uniphore.com/infoworks/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.infoworks.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.infoworks.io/infoworks-rest-api-v3/ref
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.infoworks.io/developer-resources/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.infoworks.io/getting-started/navigating-infoworks
- group: operate
  title: ''
  type: Support
  url: https://support.infoworks.io/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.uniphore.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Infoworks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uniphore.com/legal/msa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uniphore.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.uniphore.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/infoworks-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/infoworks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/infoworks-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/infoworks-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infoworks-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/infoworks-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infoworks-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/infoworks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/infoworks-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infoworks-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/infoworks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/infoworks-vulnerability-disclosure.yml
created: '2026-08-23'
description: Infoworks is an Enterprise Data Operations and Orchestration (EDO2) platform that automates data onboarding, preparation and operationalization onto Databricks, Snowflake, BigQuery, Synapse and Apache Spark. Unlike a multi-tenant SaaS, Infoworks is deployed into the customer's own cloud account (Kubernetes on AKS/EKS/GKE, or VM-based), so every deployment answers on its own host and the published contract carries a templated server. The product exposes the Infoworks REST API v3 — 369 paths and 510 operations across 62 tag groupings (41 of them declared) covering sources, tables, table groups, topic and file mappings, domains, pipelines, pipeline groups, workflows, workflow versions, jobs, environments, clusters, secrets, service authentication, users, admin operations and metrics — plus a first-party Python SDK on PyPI. Infoworks was acquired by Uniphore in 2024 and is sold as InfoWorks inside the Uniphore Business AI platform; the corporate site now redirects to uniphore.com
  while the product documentation, support desk and API reference remain on infoworks.io.
image: https://uploads.developerhub.io/prod/Bqr9/thfuawsbhl64giqmsect3d7t9soygddj2m5jd6spkfpphxzhyiyr28crjxt3yycf.png
layout: provider
modified: '2026-08-23'
name: Infoworks
nav: Providers
network: true
overview: 'Infoworks publishes 1 API on the [APIs.io](https://apis.io/) network: REST API v3. Tagged areas include Data Engineering, Data Integration, Data Ingestion, Data Pipelines, and Workflow Orchestration.


  Infoworks'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, and 18 more developer resources.'
plans:
- name: Infoworks Plans Pricing
  plan_count: 0
  slug: infoworks-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Infoworks Rate Limits
  slug: infoworks-rate-limits
score:
  band: developing
  composite: 39.4
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 30.3
    contract_quality: 51.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 28.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Infoworks Authentication
  slug: infoworks-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Infoworks Domain Security
  slug: infoworks-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Infoworks Vulnerability Disclosure
  slug: infoworks-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Infoworks Trust Center
  slug: infoworks-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO/IEC 27701:2019, SOC 2 Type 2, PCI DSS v4.0.1, NIST CSF, CASA Tier 2, FIPS 140-2, FIPS 140-3
slug: infoworks
tags:
- Data Engineering
- Data Integration
- Data Ingestion
- Data Pipelines
- Workflow Orchestration
- Data Warehouse Modernization
- Databricks
- Snowflake
- Big Data
- ETL
- Enterprise Data Operations
- Self-Hosted
website: https://www.uniphore.com/infoworks/
---
