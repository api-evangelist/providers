---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 3
  human_in_the_loop: 0
  name: Synopsys Agentic Access
  operation_count: 12
  slug: synopsys-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 8
apis:
- description: 'The Coverity Platform REST API provides programmatic access to Coverity static analysis results, project and stream management, defect management, and security findings. Coverity performs deep source '
  name: Synopsys Coverity REST API
  slug: coverity
- description: The Seeker REST API provides programmatic access to Seeker IAST (Interactive Application Security Testing) functionality including project management, vulnerability export, compliance reporting, and a
  name: Synopsys Seeker REST API
  slug: seeker
- description: Vendor entitlement queries from Synopsys Cloud.
  name: Synopsys Entitlements API
  slug: synopsys-entitlements-api
- description: Retrieve and manage security issues.
  name: Synopsys Issues API
  slug: synopsys-issues-api
- description: License file generation and delivery.
  name: Synopsys Licenses API
  slug: synopsys-licenses-api
- description: Project and branch management.
  name: Synopsys Projects API
  slug: synopsys-projects-api
- description: Generate and retrieve security reports.
  name: Synopsys Reports API
  slug: synopsys-reports-api
- description: Trigger and manage security scans.
  name: Synopsys Scans API
  slug: synopsys-scans-api
artifact_total: 24
collections:
- collection_type: open
  name: Synopsys Cloud OpenLink API
  slug: open-synopsys-cloud-openlink
- collection_type: open
  name: Synopsys Polaris API
  slug: open-synopsys-polaris
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/synopsys-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synopsys-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/synopsys-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/synopsys-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/synopsys
- group: company
  title: ''
  type: Website
  url: https://www.synopsys.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://polaris.synopsys.com/developer/
- group: operate
  title: ''
  type: Community
  url: https://community.synopsys.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/synopsys-sig
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/synopsys-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/synopsys-vocabulary.yml
created: '2026-05-03'
description: Synopsys is a global leader in semiconductor design EDA tools and software security testing. The company's Software Integrity Group (now rebranded as Black Duck) provides application security testing products including Polaris, Coverity (SAST), Black Duck (SCA), and Seeker (IAST). Synopsys also offers cloud-based EDA and semiconductor design services through the Synopsys Cloud platform with the OpenLink API for license entitlement management.
examples:
- key_count: 2
  name: Synopsys Cloud Openlink Getentitlements Example
  slug: synopsys-cloud-openlink-getEntitlements-example
- key_count: 2
  name: Synopsys Polaris Listissues Example
  slug: synopsys-polaris-listIssues-example
finops:
- name: Synopsys Finops
  service_category: Application Security / EDA
  slug: synopsys-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synopsys.png
json_schemas:
- name: Security Issue
  property_count: 12
  slug: synopsys-security-issue
json_structures:
- name: Synopsys Security Issue Structure
  property_count: 0
  slug: synopsys-security-issue-structure
jsonld:
- class_count: 25
  name: Synopsys Context
  property_count: 3
  slug: synopsys-context
layout: provider
modified: '2026-05-19'
name: Synopsys
nav: Providers
network: true
overview: 'Synopsys publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Coverity REST API, Entitlements API, Issues API, and 4 more. Tagged areas include Software Security, Application Security Testing, Static Analysis, Software Composition Analysis, and EDA Tools.


  The Synopsys catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Synopsys'' developer surface includes authentication and 10 more developer resources.'
plans:
- name: Synopsys Plans Pricing
  plan_count: 1
  slug: synopsys-plans-pricing
press:
- date: '2026-05-25'
  title: Synopsys, Inc. | Investor Relations & Investor Resources
  url: https://investor.synopsys.com/overview/default.aspx
- date: '2026-05-25'
  title: NVIDIA | Synopsys Partnership
  url: https://www.synopsys.com/partners/nvidia.html
- date: '2026-05-25'
  title: Synopsys and Ansys are Now United
  url: https://www.synopsys.com/synopsys-ansys-united.html
- date: '2026-05-25'
  title: Synopsys News Releases - News Releases
  url: https://news.synopsys.com/
- date: '2026-05-25'
  title: Synopsys Outlines Vision for Engineering the Future
  url: https://www.prnewswire.com/news-releases/synopsys-outlines-vision-for-engineering-the-future-302711205.html
random_paper: 73
rate_limits:
- limit_count: 3
  name: Synopsys Rate Limits
  slug: synopsys-rate-limits
rules:
- name: Synopsys API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: synopsys-jsonschema-spectral-rules
- name: Synopsys API Rules
  rule_count: 12
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 7
  slug: synopsys-rules
scopes:
- name: Synopsys Scopes
  scope_count: 1
  slug: synopsys-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 47.2
  delta: -4.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 66.9
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synopsys/refs/heads/main/screenshots/synopsys-2026-06-20T194831.png
security:
- kind: authentication
  name: Synopsys Authentication
  slug: synopsys-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Synopsys Domain Security
  slug: synopsys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: synopsys
tags:
- Software Security
- Application Security Testing
- Static Analysis
- Software Composition Analysis
- EDA Tools
- Semiconductor Design
- Fortune 1000
website: https://www.synopsys.com
---
