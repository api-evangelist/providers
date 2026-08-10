---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dagster Agentic Access
  operation_count: 3
  slug: dagster-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 4
apis:
- description: The Dagster GraphQL API allows clients to interact with Dagster programmatically. It can be used to query information about Dagster runs, retrieve metadata about repositories, jobs, and ops, and launc
  name: Dagster GraphQL API
  slug: graphql-api
- description: Report asset check evaluations.
  name: Dagster Checks API
  slug: dagster-checks-api
- description: Report asset materialization events.
  name: Dagster Materializations API
  slug: dagster-materializations-api
- description: Report asset observation events.
  name: Dagster Observations API
  slug: dagster-observations-api
arazzos:
- description: Observe, materialize, and check an external asset in a single correlated event pipeline.
  name: Dagster External Asset Event Pipeline
  slug: dagster-external-asset-event-pipeline-workflow
- description: Report an external asset materialization, then record an asset check evaluation against the same asset.
  name: Dagster Materialize and Check External Asset
  slug: dagster-materialize-and-check-asset-workflow
- description: Report an observation for an external asset, then report its materialization.
  name: Dagster Observe and Materialize External Asset
  slug: dagster-observe-then-materialize-asset-workflow
artifact_total: 22
collections:
- collection_type: postman
  name: Dagster External Assets REST API
  slug: postman-dagster-external-assets-rest-api
- collection_type: open
  name: Dagster External Assets REST API
  slug: open-dagster-external-assets-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dagster-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dagster-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dagster-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dagster/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dagster-external-asset-event-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dagster-materialize-and-check-asset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dagster-observe-then-materialize-asset-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dagsterlabs
- group: start
  title: ''
  type: Portal
  url: https://dagster.cloud/
- group: start
  title: ''
  type: Signup
  url: https://dagster.cloud/signup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dagster.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dagster.io/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dagster.io/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://dagster.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.dagster.io/about/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://dagster.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://dagster.io/support
- group: operate
  title: ''
  type: Community
  url: https://dagster.io/community
- group: operate
  title: ''
  type: Slack
  url: https://dagster.io/slack
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dagster-io
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/dagster-io/dagster
- group: build
  title: ''
  type: Python SDK
  url: https://pypi.org/project/dagster/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dagster.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dagster.io/terms
- group: auth
  title: ''
  type: Security
  url: https://dagster.io/security
- group: company
  title: ''
  type: About
  url: https://dagster.io/company/about-us
- group: operate
  title: ''
  type: Contact
  url: https://dagster.io/contact
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dagster-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dagster-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dagster.io/llms.txt
created: '2026-03-03'
description: Dagster is a data orchestration platform centered on software-defined assets with strong observability and testing support. It exposes a GraphQL API for programmatic interaction with Dagster instances and a REST API for reporting external asset materializations, checks, and observations from outside pipelines.
finops:
- name: Dagster Finops
  service_category: API
  slug: dagster-finops
graphqls:
- description: The Dagster GraphQL API allows clients to interact with Dagster programmatically. It can be used to query information about Dagster runs, retrieve metadata about repositories, jobs, and ops, and launc
  name: Dagster GraphQL API
  slug: dagster-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dagster.png
json_schemas:
- name: AssetCheck
  property_count: 5
  slug: asset-check
- name: AssetMaterialization
  property_count: 5
  slug: asset-materialization
- name: AssetObservation
  property_count: 5
  slug: asset-observation
jsonld:
- class_count: 3
  name: Dagster Context
  property_count: 8
  slug: dagster-context
layout: provider
modified: '2026-05-19'
name: Dagster
nav: Providers
network: true
overview: 'Dagster publishes 3 APIs on the [APIs.io](https://apis.io/) network: Checks API, Materializations API, and Observations API. Tagged areas include Data Engineering, Data Orchestration, Data Pipelines, ETL, and Workflows.


  The Dagster catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Dagster''s developer surface includes authentication, developer portal, signup flow, documentation, API reference, getting-started guide, engineering blog, and 23 more developer resources.'
plans:
- name: Dagster Plans Pricing
  plan_count: 3
  slug: dagster-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Dagster Rate Limits
  slug: dagster-rate-limits
rules:
- name: Dagster API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: dagster-external-assets-rest-api-rules
- name: Dagster API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dagster-jsonschema-spectral-rules
score:
  band: strong
  composite: 63.3
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 72.1
    developer_ergonomics: 63.0
    discoverability: 64.8
    governance: 31.3
    operational_transparency: 63.2
  previous_composite: 63.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dagster/refs/heads/main/screenshots/dagster-2026-06-20T175440.png
security:
- kind: authentication
  name: Dagster Authentication
  slug: dagster-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dagster Domain Security
  slug: dagster-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dagster
tags:
- Data Engineering
- Data Orchestration
- Data Pipelines
- ETL
- Workflows
- Assets
- GraphQL
website: https://dagster.cloud/
---
