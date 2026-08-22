---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Sisense Agentic Access
  operation_count: 17
  slug: sisense-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 8
apis:
- description: The Sisense REST API v2 provides access to Datamodels (the v2 replacement for Elasticubes), builds, and advanced data model management capabilities including schema management, field configuration, an
  name: Sisense REST API v2
  slug: rest-api-v2
- description: The Sisense User and Role Management API (RBAC) enables administrators to manage users, roles, and permissions programmatically. Available on select plans through contact with Customer Success Manager
  name: Sisense User and Role Management API
  slug: user-role-management-api
- description: Login and token management
  name: Sisense Authentication API
  slug: sisense-authentication-api
- description: Create, read, update, and manage dashboards
  name: Sisense Dashboards API
  slug: sisense-dashboards-api
- description: Configure row-level data security rules
  name: Sisense Data Security API
  slug: sisense-data-security-api
- description: Manage Elasticube data models and builds
  name: Sisense Elasticubes API
  slug: sisense-elasticubes-api
- description: Manage user groups for access control
  name: Sisense Groups API
  slug: sisense-groups-api
- description: Manage Sisense users and user settings
  name: Sisense Users API
  slug: sisense-users-api
artifact_total: 37
collections:
- collection_type: postman
  name: Sisense REST Authentication API
  slug: postman-sisense-authentication-api
- collection_type: postman
  name: Sisense REST Authentication Dashboards API
  slug: postman-sisense-dashboards-api
- collection_type: postman
  name: Sisense REST Authentication Data Security API
  slug: postman-sisense-data-security-api
- collection_type: postman
  name: Sisense REST Authentication Elasticubes API
  slug: postman-sisense-elasticubes-api
- collection_type: postman
  name: Sisense REST Authentication Groups API
  slug: postman-sisense-groups-api
- collection_type: postman
  name: Sisense REST Authentication Users API
  slug: postman-sisense-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sisense REST Authentication API
  slug: open-sisense-authentication-api
- collection_type: open
  name: Sisense REST Authentication Dashboards API
  slug: open-sisense-dashboards-api
- collection_type: open
  name: Sisense REST Authentication Data Security API
  slug: open-sisense-data-security-api
- collection_type: open
  name: Sisense REST Authentication Elasticubes API
  slug: open-sisense-elasticubes-api
- collection_type: open
  name: Sisense REST Authentication Groups API
  slug: open-sisense-groups-api
- collection_type: open
  name: Sisense REST API
  slug: open-sisense-rest-api
- collection_type: open
  name: Sisense REST Authentication Users API
  slug: open-sisense-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sisense/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sisense-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sisense-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sisense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sisense-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sisense
- group: company
  title: ''
  type: Website
  url: https://www.sisense.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sisense.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sisense.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sisense.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.sisense.com/blog/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sisense
- group: operate
  title: ''
  type: Community
  url: https://community.sisense.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sisense.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sisense.com/legal/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://support.sisense.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.sisense.com/llms.txt
created: '2025-01-08'
description: Sisense is a business intelligence and analytics platform that enables organizations to build and embed analytics into applications and workflows. It provides REST APIs for managing dashboards, data models (Elasticubes and live models), users, groups, data security rules, and builds. The platform supports both extract-based and live data model architectures with comprehensive programmatic administration capabilities.
examples:
- key_count: 4
  name: Sisense Create User Example
  slug: sisense-create-user-example
- key_count: 4
  name: Sisense List Dashboards Example
  slug: sisense-list-dashboards-example
finops:
- name: Sisense Finops
  service_category: Analytics / Business Intelligence
  slug: sisense-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sisense.png
json_schemas:
- name: Sisense Dashboard
  property_count: 9
  slug: sisense-dashboard
- name: Sisense User
  property_count: 10
  slug: sisense-user
json_structures:
- name: Sisense Dashboard Structure
  property_count: 0
  slug: sisense-dashboard-structure
jsonld:
- class_count: 19
  name: Sisense Context
  property_count: 6
  slug: sisense-context
layout: provider
modified: '2026-05-19'
name: Sisense
nav: Providers
network: true
overview: 'Sisense publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Dashboards API, Data Security API, and 3 more. Tagged areas include Analytics, Business Intelligence, Dashboards, Data Models, and Embedded Analytics.


  The Sisense catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sisense''s developer surface includes authentication, documentation, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Sisense Plans Pricing
  plan_count: 3
  slug: sisense-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Sisense Rate Limits
  slug: sisense-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sisense API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sisense-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: Sisense API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 4
  slug: sisense-rules
score:
  band: developing
  composite: 43.6
  delta: -8.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 9.8
    contract_quality: 63.5
    developer_ergonomics: 40.5
    discoverability: 81.5
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sisense/refs/heads/main/screenshots/sisense-2026-06-20T193954.png
security:
- kind: authentication
  name: Sisense Authentication
  slug: sisense-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sisense Domain Security
  slug: sisense-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sisense Trust Center
  slug: sisense-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: sisense
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Models
- Embedded Analytics
website: https://www.sisense.com/
---
