---
access_model:
  confidence: high
  label: Free trial · Self-serve signup
  onboarding: self-serve
  pricing: free-trial
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Datafold Agentic Access
  operation_count: 52
  slug: datafold-agentic-access
  summary_line: 52 operations · 29 acting
api_count: 13
apis:
- description: The Audit Logs API from Datafold — 1 operation(s) for audit logs.
  name: Datafold Audit Logs API
  slug: datafold-audit-logs-api
- description: The bi_added API from Datafold — 6 operation(s) for bi_added.
  name: Datafold bi_added API
  slug: datafold-bi-added-api
- description: The BI API from Datafold — 15 operation(s) for bi.
  name: Datafold BI API
  slug: datafold-bi-api
- description: The bi_deleted API from Datafold — 1 operation(s) for bi_deleted.
  name: Datafold bi_deleted API
  slug: datafold-bi-deleted-api
- description: The bi_modified API from Datafold — 6 operation(s) for bi_modified.
  name: Datafold bi_modified API
  slug: datafold-bi-modified-api
- description: The bolt API from Datafold — 1 operation(s) for bolt.
  name: Datafold bolt API
  slug: datafold-bolt-api
- description: The CI API from Datafold — 3 operation(s) for ci.
  name: Datafold CI API
  slug: datafold-ci-api
- description: The Data diffs API from Datafold — 5 operation(s) for data diffs.
  name: Datafold Data diffs API
  slug: datafold-data-diffs-api
- description: The data_source_added API from Datafold — 1 operation(s) for data_source_added.
  name: Datafold data_source_added API
  slug: datafold-data-source-added-api
- description: The Data sources API from Datafold — 7 operation(s) for data sources.
  name: Datafold Data sources API
  slug: datafold-data-sources-api
- description: The diff_created API from Datafold — 1 operation(s) for diff_created.
  name: Datafold diff_created API
  slug: datafold-diff-created-api
- description: The Explore API from Datafold — 4 operation(s) for explore.
  name: Datafold Explore API
  slug: datafold-explore-api
- description: The Monitors API from Datafold — 11 operation(s) for monitors.
  name: Datafold Monitors API
  slug: datafold-monitors-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/datafold-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/datafold-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datafold-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datafold-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.datafold.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datafold.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/datafold
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datafold/
- group: company
  title: ''
  type: Blog
  url: https://www.datafold.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datafold.com/contact-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datafold.com
- group: other
  title: ''
  type: X
  url: https://x.com/datafoldcom
- group: commercial
  title: ''
  type: Plans
  url: plans/datafold-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datafold-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datafold-finops.yml
created: '2026-06-13'
description: Datafold is a data reliability platform providing a REST API for running data diffs, monitoring column-level lineage, validating data pipelines, and detecting data regressions before deployment. It supports CI/CD integration, automated anomaly detection, schema change alerts, and cross-database comparison across major cloud data warehouses.
examples:
- key_count: 5
  name: Datafold Examples
  slug: datafold-examples
finops:
- name: Datafold Finops
  service_category: ''
  slug: datafold-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datafold.png
json_schemas:
- name: Datafold API Schemas
  property_count: 0
  slug: datafold-schemas
jsonld:
- class_count: 21
  name: Datafold Context
  property_count: 11
  slug: datafold
layout: provider
modified: '2026-06-13'
name: Datafold
nav: Providers
network: true
overview: 'Datafold publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Audit Logs API, bi_added API, BI API, and 10 more. Tagged areas include Data Reliability, Data Diff, Data Quality, Column-Level Lineage, and Data Pipelines.


  The Datafold catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Datafold''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Datafold Plans Pricing
  plan_count: 3
  slug: datafold-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 0
  name: Datafold Rate Limits
  slug: datafold-rate-limits
rules:
- name: Datafold API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: datafold-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.6
  delta: -4.1
  facets:
    commercial_clarity: 57.9
    contract_quality: 66.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datafold/refs/heads/main/screenshots/datafold-2026-06-20T175639.png
security:
- kind: authentication
  name: Datafold Authentication
  slug: datafold-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Datafold Domain Security
  slug: datafold-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Datafold Trust Center
  slug: datafold-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: datafold
tags:
- Data Reliability
- Data Diff
- Data Quality
- Column-Level Lineage
- Data Pipelines
- CI/CD Integration
- Anomaly Detection
- Data Observability
- Data Migrations
website: https://www.datafold.com
---
