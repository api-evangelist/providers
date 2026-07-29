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
- acting_count: 47
  human_in_the_loop: 2
  name: Zesty Agentic Access
  operation_count: 86
  slug: zesty-agentic-access
  summary_line: 86 operations · 47 acting · 2 human-in-the-loop
api_count: 25
apis:
- description: The Zesty.io Instances API is a REST API that allows CRUD operations on Zesty.io instances. It provides access to content models, content items, fields, views, stylesheets, scripts, settings, head tag
  name: Zesty Instances API
  slug: instances-api
- description: Manage registered applications.
  name: Zesty Apps API
  slug: zesty-apps-api
- description: View audit trail entries.
  name: Zesty Audits API
  slug: zesty-audits-api
- description: User authentication and session management.
  name: Zesty Authentication API
  slug: zesty-authentication-api
- description: Manage media bins (top-level containers).
  name: Zesty Bins API
  slug: zesty-bins-api
- description: Manage content item data.
  name: Zesty Content Items API
  slug: zesty-content-items-api
- description: Manage content model schemas.
  name: Zesty Content Models API
  slug: zesty-content-models-api
- description: Manage fields on content models.
  name: Zesty Fields API
  slug: zesty-fields-api
- description: Manage and upload media files.
  name: Zesty Files API
  slug: zesty-files-api
- description: Manage media groups (folders within bins).
  name: Zesty Groups API
  slug: zesty-groups-api
- description: Manage HTML head tag entries.
  name: Zesty Head Tags API
  slug: zesty-head-tags-api
- description: Manage the instance navigation tree.
  name: Zesty Navigation API
  slug: zesty-navigation-api
- description: Password management operations.
  name: Zesty Password API
  slug: zesty-password-api
- description: Publish content items to the live site.
  name: Zesty Publishing API
  slug: zesty-publishing-api
- description: Resolve file ZUIDs to CDN URLs.
  name: Zesty Resolver API
  slug: zesty-resolver-api
- description: Manage roles and permissions.
  name: Zesty Roles API
  slug: zesty-roles-api
- description: Manage JavaScript files.
  name: Zesty Scripts API
  slug: zesty-scripts-api
- description: Search across content items.
  name: Zesty Search API
  slug: zesty-search-api
- description: Manage instance settings.
  name: Zesty Settings API
  slug: zesty-settings-api
- description: Manage CSS stylesheet files.
  name: Zesty Stylesheets API
  slug: zesty-stylesheets-api
- description: Manage teams.
  name: Zesty Teams API
  slug: zesty-teams-api
- description: Manage API access tokens.
  name: Zesty Tokens API
  slug: zesty-tokens-api
- description: Manage user accounts.
  name: Zesty Users API
  slug: zesty-users-api
- description: Manage view template files.
  name: Zesty Views API
  slug: zesty-views-api
- description: Manage webhook subscriptions.
  name: Zesty Webhooks API
  slug: zesty-webhooks-api
artifact_total: 49
collections:
- collection_type: open
  name: Zesty Accounts API
  slug: open-zesty-accounts-api
- collection_type: open
  name: Zesty Auth API
  slug: open-zesty-auth-api
- collection_type: open
  name: Zesty Instances API
  slug: open-zesty-instances-api
- collection_type: open
  name: Zesty Media API
  slug: open-zesty-media-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zesty-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zesty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zesty-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zesty-io
- group: docs
  title: ''
  type: Documentation
  url: https://www.zesty.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zesty.io/
- group: company
  title: ''
  type: Blog
  url: https://www.zesty.io/mindshare/
- group: operate
  title: ''
  type: Support
  url: https://www.zesty.io/contact/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/zesty-io
- group: build
  title: ''
  type: SDKs
  url: https://github.com/zesty-io/node-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/zesty-io/fetch-wrapper
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.zesty.io/llms.txt
created: '2025-02-17'
description: Zesty.io is a composable, data-driven, headless CMS platform that provides REST APIs for authentication, account management, instance content management, and media file management. All resources are identified by ZUIDs (Zesty Universal Identifiers). The platform supports WebEngine for traditional CMS, headless API architecture, GraphQL, and JamStack implementations. Built on Google Cloud Platform with Fastly edge caching.
finops:
- name: Zesty Finops
  service_category: Headless CMS
  slug: zesty-finops
graphqls:
- description: ''
  name: Zesty GraphQL API
  slug: zesty-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zesty.png
json_schemas:
- name: Zesty Content Item
  property_count: 6
  slug: content-item
- name: Zesty Content Model
  property_count: 9
  slug: content-model
- name: Zesty Field
  property_count: 11
  slug: field
- name: Zesty Instance
  property_count: 7
  slug: instance
- name: Zesty Media Bin
  property_count: 4
  slug: media-bin
- name: Zesty Media File
  property_count: 9
  slug: media-file
- name: Zesty Media Group
  property_count: 6
  slug: media-group
- name: Zesty Role
  property_count: 6
  slug: role
- name: Zesty Team
  property_count: 5
  slug: team
- name: Zesty Token
  property_count: 5
  slug: token
- name: Zesty User
  property_count: 6
  slug: user
jsonld:
- class_count: 0
  name: Zesty Context
  property_count: 11
  slug: zesty-context
layout: provider
modified: '2026-05-19'
name: Zesty
nav: Providers
network: true
overview: 'Zesty publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Instances API, Apps API, Audits API, and 22 more. Tagged areas include CMS, Composable, Content Management, GraphQL, and Headless CMS.


  The Zesty catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zesty''s developer surface includes authentication, documentation, engineering blog, support, GitHub presence, and 7 more developer resources.'
plans:
- name: Zesty Plans Pricing
  plan_count: 4
  slug: zesty-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Zesty Rate Limits
  slug: zesty-rate-limits
rules:
- name: Zesty API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: zesty-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.9
  delta: -3.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 76.9
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zesty/refs/heads/main/screenshots/zesty-2026-06-20T201845.png
security:
- kind: authentication
  name: Zesty Authentication
  slug: zesty-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zesty Domain Security
  slug: zesty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zesty
tags:
- CMS
- Composable
- Content Management
- GraphQL
- Headless CMS
- Media
---
