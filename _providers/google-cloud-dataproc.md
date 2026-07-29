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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Google Cloud Dataproc Agentic Access
  operation_count: 12
  slug: google-cloud-dataproc-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 3
apis:
- description: Operations on Dataproc clusters
  name: Google Cloud Dataproc Clusters API
  slug: google-cloud-dataproc-clusters-api
- description: Operations on Dataproc jobs
  name: Google Cloud Dataproc Jobs API
  slug: google-cloud-dataproc-jobs-api
- description: Operations on workflow templates
  name: Google Cloud Dataproc WorkflowTemplates API
  slug: google-cloud-dataproc-workflowtemplates-api
artifact_total: 18
collections:
- collection_type: postman
  name: Google Cloud Dataproc Clusters API
  slug: postman-google-cloud-dataproc-clusters-api
- collection_type: postman
  name: Google Cloud Dataproc Clusters Jobs API
  slug: postman-google-cloud-dataproc-jobs-api
- collection_type: postman
  name: Google Cloud Dataproc Clusters WorkflowTemplates API
  slug: postman-google-cloud-dataproc-workflowtemplates-api
- collection_type: open
  name: Google Cloud Dataproc API
  slug: open-cloud-dataproc
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-dataproc/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-dataproc-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-dataproc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-dataproc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-dataproc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-dataproc-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudDataproc
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/dataproc
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/dataproc/docs/quickstarts
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/dataproc/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/dataproc/docs/concepts/iam
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/dataproc/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/dataproc/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-dataproc-context.jsonld
created: '2026-03-13'
description: Google Cloud Dataproc is a fully managed and highly scalable service for running Apache Spark, Apache Hadoop, Apache Flink, Presto, and other open-source data processing frameworks. It enables batch processing, querying, streaming, and machine learning use cases with cluster management that takes seconds instead of minutes, along with per-second billing and autoscaling capabilities.
finops:
- name: Google Cloud Dataproc Finops
  service_category: API
  slug: google-cloud-dataproc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-dataproc.png
json_schemas:
- name: Google Cloud Dataproc Cluster
  property_count: 6
  slug: cluster
jsonld:
- class_count: 21
  name: Google Cloud Dataproc Context
  property_count: 0
  slug: google-cloud-dataproc-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Dataproc
nav: Providers
network: true
overview: 'Google Cloud Dataproc publishes 3 APIs on the [APIs.io](https://apis.io/) network: Clusters API, Jobs API, and WorkflowTemplates API. Tagged areas include Big Data, Data Processing, Google Cloud, Hadoop, and Spark.


  The Google Cloud Dataproc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Dataproc''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Dataproc Plans Pricing
  plan_count: 3
  slug: google-cloud-dataproc-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Google Cloud Dataproc Rate Limits
  slug: google-cloud-dataproc-rate-limits
rules:
- name: Google Cloud Dataproc API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-dataproc-jsonschema-spectral-rules
scopes:
- name: Google Cloud Dataproc Scopes
  scope_count: 1
  slug: google-cloud-dataproc-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 62.6
  delta: -3.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 70.3
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 65.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-dataproc/refs/heads/main/screenshots/google-cloud-dataproc-2026-06-20T182106.png
security:
- kind: authentication
  name: Google Cloud Dataproc Authentication
  slug: google-cloud-dataproc-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Dataproc Domain Security
  slug: google-cloud-dataproc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Dataproc Vulnerability Disclosure
  slug: google-cloud-dataproc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-dataproc
tags:
- Big Data
- Data Processing
- Google Cloud
- Hadoop
- Spark
website: https://cloud.google.com/dataproc
---
