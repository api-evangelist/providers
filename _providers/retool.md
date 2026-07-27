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
- acting_count: 10
  human_in_the_loop: 0
  name: Retool Agentic Access
  operation_count: 17
  slug: retool-agentic-access
  summary_line: 17 operations · 10 acting
api_count: 7
apis:
- description: Retool implements a subset of the SCIM 2.0 API for automated user provisioning and group mapping through identity providers like Okta and Azure Active Directory (Entra ID). Available on Enterprise pla
  name: Retool SCIM 2.0 API
  slug: retool-scim-api
- description: Retool's low-code platform provides a visual development environment with 100+ pre-built components, native connectors to 70+ data sources, AI-powered app generation (AppGen), workflow automation, bui
  name: Retool Platform
  slug: retool-platform
- description: Create and manage Retool applications. Apps are the core visual building blocks created in the Retool editor.
  name: Retool Apps API
  slug: retool-apps-api
- description: Organize apps, resources, and workflows into folders for better team organization.
  name: Retool Folders API
  slug: retool-folders-api
- description: Manage groups and group membership. Groups control access to apps, resources, and workflows within the organization.
  name: Retool Groups API
  slug: retool-groups-api
- description: Manage data source connections (databases, APIs, services) that power Retool queries.
  name: Retool Resources API
  slug: retool-resources-api
- description: Create, read, update, and delete users within a Retool organization. Manage user roles (admin, standard, end-user) and activation status.
  name: Retool Users API
  slug: retool-users-api
artifact_total: 26
collections:
- collection_type: open
  name: Retool Management API
  slug: open-retool-management-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/retool-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/retool-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/retool-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/retool-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://retool.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.retool.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.retool.com/reference/api/v2
- group: company
  title: ''
  type: Blog
  url: https://retool.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://retool.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.retool.com
- group: operate
  title: ''
  type: Support
  url: https://support.retool.com
- group: operate
  title: ''
  type: Community
  url: https://community.retool.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tryretool
- group: commercial
  title: ''
  type: Pricing
  url: https://retool.com/pricing
- group: start
  title: ''
  type: Login
  url: https://login.retool.com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/retool
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tryretool
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/retool/refs/heads/main/openapi/retool-management-api-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/retool/refs/heads/main/vocabulary/retool-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.retool.com/llms.txt
created: '2025-01-08'
description: Retool is a low-code platform for building internal tools, dashboards, and admin panels quickly using pre-built UI components that connect to any database or API. Retool provides a management REST API for programmatically administering users, groups, apps, resources, permissions, and source control integrations. It supports enterprise features including SSO, SCIM 2.0 provisioning, self-hosting, and AI-powered app generation.
examples:
- key_count: 2
  name: Retool Create User Example
  slug: retool-create-user-example
- key_count: 2
  name: Retool List Groups Example
  slug: retool-list-groups-example
- key_count: 2
  name: Retool List Users Example
  slug: retool-list-users-example
finops:
- name: Retool Finops
  service_category: Internal Tools
  slug: retool-finops
graphqls:
- description: Retool is a low-code platform for building internal tools, dashboards, and admin panels. While Retool does not expose a native public GraphQL endpoint, this schema is a conceptual representation of th
  name: Retool GraphQL API
  slug: retool-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/retool.png
json_schemas:
- name: Retool App
  property_count: 8
  slug: retool-app
- name: Retool Group
  property_count: 5
  slug: retool-group
- name: Retool User
  property_count: 10
  slug: retool-user
json_structures:
- name: Retool Management Api Structure
  property_count: 0
  slug: retool-management-api-structure
jsonld:
- class_count: 13
  name: Retool Context
  property_count: 13
  slug: retool-context
layout: provider
modified: '2026-05-19'
name: Retool
nav: Providers
network: true
overview: 'Retool publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Folders API, Groups API, and 2 more. Tagged areas include Admin Panel, Dashboard, Internal Tools, Low Code, and No Code.


  The Retool catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Retool''s developer surface includes authentication, documentation, API reference, engineering blog, changelog, support, GitHub presence, and 13 more developer resources.'
plans:
- name: Retool Plans Pricing
  plan_count: 4
  slug: retool-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 3
  name: Retool Rate Limits
  slug: retool-rate-limits
rules:
- name: Retool API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: retool-jsonschema-spectral-rules
- name: Retool API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 2
    info: 0
    warn: 4
  slug: retool-management-api-rules
score:
  band: strong
  composite: 66.3
  delta: 2.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 69.9
    developer_ergonomics: 32.6
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 68.4
  previous_composite: 64.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/retool/refs/heads/main/screenshots/retool-2026-06-20T193043.png
security:
- kind: authentication
  name: Retool Authentication
  slug: retool-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Retool Domain Security
  slug: retool-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Retool Trust Center
  slug: retool-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: retool
tags:
- Admin Panel
- Dashboard
- Internal Tools
- Low Code
- No Code
website: https://retool.com/
---
