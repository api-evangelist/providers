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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 16
  human_in_the_loop: 2
  name: Singlestore Agentic Access
  operation_count: 29
  slug: singlestore-agentic-access
  summary_line: 29 operations · 16 acting · 2 human-in-the-loop
api_count: 9
apis:
- description: Upload, download, list, and delete files in the personal, shared, or models space within SingleStore Helios Spaces (stage storage).
  name: SingleStore Files API
  slug: singlestore-files-api
- description: Health check operations for verifying connectivity to the Data API endpoint without requiring authentication credentials.
  name: SingleStore Health API
  slug: singlestore-health-api
- description: Create, retrieve, list, and delete scheduled notebook jobs within SingleStore Helios. Jobs enable automated execution of notebooks on configurable schedules.
  name: SingleStore Jobs API
  slug: singlestore-jobs-api
- description: Retrieve information about the current user's organization within SingleStore Helios.
  name: SingleStore Organizations API
  slug: singlestore-organizations-api
- description: Execute SQL statements against a SingleStore Helios workspace over HTTP. Supports DDL, DML, and SELECT statements returning results as JSON.
  name: SingleStore Queries API
  slug: singlestore-queries-api
- description: List available cloud provider regions that support workspace group creation, including shared tier regions.
  name: SingleStore Regions API
  slug: singlestore-regions-api
- description: Manage organization-level secrets that can be referenced securely in notebooks and jobs without exposing plaintext credentials.
  name: SingleStore Secrets API
  slug: singlestore-secrets-api
- description: Create, list, retrieve, update, and delete workspace groups within a SingleStore Helios organization. Workspace groups are logical containers that group workspaces by region and network configuration.
  name: SingleStore WorkspaceGroups API
  slug: singlestore-workspacegroups-api
- description: Create, list, retrieve, update, suspend, resume, and delete workspaces within a workspace group. Workspaces are the compute resources that connect to a SingleStore database.
  name: SingleStore Workspaces API
  slug: singlestore-workspaces-api
artifact_total: 26
collections:
- collection_type: open
  name: SingleStore Data API
  slug: open-singlestore-data-api
- collection_type: open
  name: SingleStore Management API
  slug: open-singlestore-management-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/singlestore-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/singlestore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/singlestore-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/singlestore-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/singlestore
- group: company
  title: ''
  type: Website
  url: https://www.singlestore.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.singlestore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.singlestore.com/cloud/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.singlestore.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.singlestore.com/blog/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/singlestore-labs
- group: start
  title: ''
  type: Signup
  url: https://www.singlestore.com/cloud-trial/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.singlestore.com/cloud-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.singlestore.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://support.singlestore.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.singlestore.com/llms.txt
created: '2025-01-01'
description: SingleStore is a cloud-native distributed SQL database designed for real-time analytics and mixed workloads. It offers a management API for provisioning and managing cloud workspaces, and a data API for executing SQL statements over HTTP without requiring native database drivers. SingleStore Helios is the fully managed cloud service providing serverless database capabilities with elastic scaling.
examples:
- key_count: 4
  name: Singlestore Execute Sql Example
  slug: singlestore-execute-sql-example
- key_count: 4
  name: Singlestore Query Rows Example
  slug: singlestore-query-rows-example
finops:
- name: Singlestore Finops
  service_category: API
  slug: singlestore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/singlestore.png
json_schemas:
- name: SingleStore Data API Query
  property_count: 3
  slug: singlestore-query
- name: SingleStore Workspace
  property_count: 10
  slug: singlestore-workspace
json_structures:
- name: Singlestore Workspace Structure
  property_count: 0
  slug: singlestore-workspace-structure
jsonld:
- class_count: 0
  name: Singlestore Context
  property_count: 9
  slug: singlestore-context
layout: provider
modified: '2026-05-19'
name: SingleStore
nav: Providers
network: true
overview: 'SingleStore publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Files API, Health API, Jobs API, and 6 more. Tagged areas include Database, SQL, Analytics, Cloud, and Distributed SQL.


  The SingleStore catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SingleStore''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, support, and 10 more developer resources.'
plans:
- name: Singlestore Plans Pricing
  plan_count: 3
  slug: singlestore-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Singlestore Rate Limits
  slug: singlestore-rate-limits
rules:
- name: SingleStore API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: singlestore-jsonschema-spectral-rules
- name: SingleStore API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: singlestore-rules
score:
  band: strong
  composite: 60.9
  delta: 3.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 64.2
    developer_ergonomics: 34.8
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 57.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/singlestore/refs/heads/main/screenshots/singlestore-2026-06-20T193949.png
security:
- kind: authentication
  name: Singlestore Authentication
  slug: singlestore-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Singlestore Domain Security
  slug: singlestore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Singlestore Vulnerability Disclosure
  slug: singlestore-vulnerability-disclosure
  summary_line: disclosure policy published
slug: singlestore
tags:
- Database
- SQL
- Analytics
- Cloud
- Distributed SQL
website: https://www.singlestore.com/
---
