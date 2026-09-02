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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Appsmith Agentic Access
  operation_count: 5
  slug: appsmith-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Appsmith Applications API
  slug: open-appsmith-applications-api
- collection_type: open
  name: Appsmith Applications Datasources API
  slug: open-appsmith-datasources-api
- collection_type: open
  name: Appsmith Applications Workspaces API
  slug: open-appsmith-workspaces-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/appsmithorg/appsmith/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/appsmithorg/appsmith/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/appsmithorg/appsmith/blob/release/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/appsmithorg/appsmith/blob/release/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/appsmithorg/appsmith/blob/release/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/appsmithorg/appsmith/blob/release/LICENSE
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
overview: 'Appsmith publishes 3 APIs on the [APIs.io](https://apis.io/) network: Applications API, Datasources API, and Workspaces API. Tagged areas include Low-Code, Open-Source, Internal Tools, Workflow-Automation, and Developer Tools.


  The Appsmith catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Appsmith''s developer surface includes authentication, documentation, and 11 more developer resources.'
plans:
- name: Appsmith Plans Pricing
  plan_count: 3
  slug: appsmith-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Appsmith Rate Limits
  slug: appsmith-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Appsmith API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: appsmith-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Appsmith API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 14
  slug: appsmith-spectral-rules
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 55.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 28.8
    contract_quality: 70.7
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Open-Source
- Internal Tools
- Workflow-Automation
- Developer Tools
website: https://www.appsmith.com
---
