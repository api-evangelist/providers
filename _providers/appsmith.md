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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Appsmith Agentic Access
  operation_count: 5
  slug: appsmith-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 3
apis:
- description: Low-code application management
  name: Appsmith Applications API
  slug: appsmith-applications-api
- description: Connected datasource management
  name: Appsmith Datasources API
  slug: appsmith-datasources-api
- description: Workspace organization and management
  name: Appsmith Workspaces API
  slug: appsmith-workspaces-api
artifact_total: 16
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appsmith-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/appsmith-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appsmith-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appsmith-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appsmith
- group: company
  title: ''
  type: Website
  url: https://www.appsmith.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.appsmith.com
created: 2026-03-27
description: Appsmith is an open source low-code platform for building internal tools and workflow applications.
examples:
- key_count: 8
  name: Application Example
  slug: application-example
finops:
- name: Appsmith Finops
  service_category: API
  slug: appsmith-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appsmith.png
json_schemas:
- name: Application
  property_count: 8
  slug: application
json_structures:
- name: Application Structure
  property_count: 0
  slug: application-structure
jsonld:
- class_count: 10
  name: Appsmith Context
  property_count: 0
  slug: appsmith-context
layout: provider
modified: '2026-04-19'
name: Appsmith
nav: Providers
network: true
overview: 'Appsmith publishes 3 APIs on the [APIs.io](https://apis.io/) network: Applications API, Datasources API, and Workspaces API. Tagged areas include Low-Code, Open Source, Internal Tools, Workflow Automation, and Developer Tools.


  The Appsmith catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Appsmith''s developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: Appsmith Plans Pricing
  plan_count: 3
  slug: appsmith-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Appsmith Rate Limits
  slug: appsmith-rate-limits
rules:
- name: Appsmith API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: appsmith-jsonschema-spectral-rules
- name: Appsmith API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 14
  slug: appsmith-spectral-rules
score:
  band: developing
  composite: 48.9
  delta: -3.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 75.4
    developer_ergonomics: 19.6
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 52.4
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
screenshot: https://raw.githubusercontent.com/api-evangelist/appsmith/refs/heads/main/screenshots/appsmith-2026-06-20T172348.png
security:
- kind: authentication
  name: Appsmith Authentication
  slug: appsmith-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Appsmith Domain Security
  slug: appsmith-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Appsmith Trust Center
  slug: appsmith-trust-center
  summary_line: SOC 2
slug: appsmith
tags:
- Low-Code
- Open Source
- Internal Tools
- Workflow Automation
- Developer Tools
website: https://www.appsmith.com
---
