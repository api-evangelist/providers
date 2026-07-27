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
- acting_count: 17
  human_in_the_loop: 1
  name: Intralinks Agentic Access
  operation_count: 30
  slug: intralinks-agentic-access
  summary_line: 30 operations · 17 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The Authentication API from Intralinks — 2 operation(s) for authentication.
  name: Intralinks Authentication API
  slug: intralinks-authentication-api
- description: The Custom Fields API from Intralinks — 1 operation(s) for custom fields.
  name: Intralinks Custom Fields API
  slug: intralinks-custom-fields-api
- description: The Documents API from Intralinks — 3 operation(s) for documents.
  name: Intralinks Documents API
  slug: intralinks-documents-api
- description: The Folders API from Intralinks — 2 operation(s) for folders.
  name: Intralinks Folders API
  slug: intralinks-folders-api
- description: The Groups API from Intralinks — 3 operation(s) for groups.
  name: Intralinks Groups API
  slug: intralinks-groups-api
- description: The Permissions API from Intralinks — 1 operation(s) for permissions.
  name: Intralinks Permissions API
  slug: intralinks-permissions-api
- description: The Splash API from Intralinks — 1 operation(s) for splash.
  name: Intralinks Splash API
  slug: intralinks-splash-api
- description: The Workspaces API from Intralinks — 2 operation(s) for workspaces.
  name: Intralinks Workspaces API
  slug: intralinks-workspaces-api
artifact_total: 25
collections:
- collection_type: open
  name: Intralinks API
  slug: open-intralinks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/intralinks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intralinks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/intralinks-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ssc-intralinks
- group: start
  title: ''
  type: Portal
  url: https://developers.intralinks.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.intralinks.com/swagger/
- group: operate
  title: ''
  type: Support
  url: https://support.intralinks.com/hc/en-us/sections/17037626903707-Intralinks-APIs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.intralinks.com/why-intralinks/apis-deployment
created: '2025-01-01'
description: Intralinks is a cloud-based virtual data room and secure file sharing platform used for M&A transactions, due diligence, and confidential business collaboration. The platform provides APIs for programmatic access to workspaces, documents, folders, groups, users, and permissions, enabling integration with enterprise document management and deal workflow systems.
finops:
- name: Intralinks Finops
  service_category: API
  slug: intralinks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intralinks.png
json_schemas:
- name: Intralinks Custom Field
  property_count: 5
  slug: custom-field
- name: Intralinks Document
  property_count: 11
  slug: document
- name: Intralinks Folder
  property_count: 8
  slug: folder
- name: Intralinks Group
  property_count: 8
  slug: group
- name: Intralinks Permission
  property_count: 4
  slug: permission
- name: Intralinks Splash Screen
  property_count: 4
  slug: splash
- name: Intralinks User
  property_count: 8
  slug: user
- name: Intralinks Workspace
  property_count: 9
  slug: workspace
jsonld:
- class_count: 0
  name: Intralinks Context
  property_count: 8
  slug: intralinks-context
layout: provider
modified: '2026-05-19'
name: Intralinks
nav: Providers
network: true
overview: 'Intralinks publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Custom Fields API, Documents API, and 5 more. Tagged areas include Document Management, Secure File Sharing, and Virtual Data Room.


  The Intralinks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Intralinks'' developer surface includes authentication, developer portal, documentation, support, getting-started guide, and 3 more developer resources.'
plans:
- name: Intralinks Plans Pricing
  plan_count: 3
  slug: intralinks-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 5
  name: Intralinks Rate Limits
  slug: intralinks-rate-limits
rules:
- name: Intralinks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: intralinks-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.2
  delta: 4.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 68.7
    developer_ergonomics: 43.5
    discoverability: 75.0
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 50.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intralinks/refs/heads/main/screenshots/intralinks-2026-06-20T183611.png
security:
- kind: authentication
  name: Intralinks Authentication
  slug: intralinks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Intralinks Domain Security
  slug: intralinks-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: intralinks
tags:
- Document Management
- Secure File Sharing
- Virtual Data Room
website: https://developers.intralinks.com
---
