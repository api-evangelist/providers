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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Datafold Agentic Access
  operation_count: 52
  slug: datafold-agentic-access
  summary_line: 52 operations · 29 acting
api_count: 1
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
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Datafold Audit Logs API
  slug: open-datafold-audit-logs-api
- collection_type: open
  name: Datafold Audit Logs bi_added API
  slug: open-datafold-bi-added-api
- collection_type: open
  name: Datafold Audit Logs BI API
  slug: open-datafold-bi-api
- collection_type: open
  name: Datafold Audit Logs bi_deleted API
  slug: open-datafold-bi-deleted-api
- collection_type: open
  name: Datafold Audit Logs bi_modified API
  slug: open-datafold-bi-modified-api
- collection_type: open
  name: Datafold Audit Logs bolt API
  slug: open-datafold-bolt-api
- collection_type: open
  name: Datafold Audit Logs CI API
  slug: open-datafold-ci-api
- collection_type: open
  name: Datafold Audit Logs Data diffs API
  slug: open-datafold-data-diffs-api
- collection_type: open
  name: Datafold Audit Logs data_source_added API
  slug: open-datafold-data-source-added-api
- collection_type: open
  name: Datafold Audit Logs Data sources API
  slug: open-datafold-data-sources-api
- collection_type: open
  name: Datafold Audit Logs diff_created API
  slug: open-datafold-diff-created-api
- collection_type: open
  name: Datafold Audit Logs Explore API
  slug: open-datafold-explore-api
- collection_type: open
  name: Datafold Audit Logs Monitors API
  slug: open-datafold-monitors-api
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
overview: 'Datafold publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Audit Logs API, bi_added API, BI API, and 10 more. Tagged areas include Data Reliability, Data Diff, Data Quality, Column-Level Lineage, and Data Pipeline.


  The Datafold catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Datafold''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Datafold Plans Pricing
  plan_count: 3
  slug: datafold-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Datafold Rate Limits
  slug: datafold-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Datafold API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: datafold-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 63.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Data Pipeline
- CI/CD Integration
- Anomaly Detection
- Data Observability
- Data Migrations
website: https://www.datafold.com
---
