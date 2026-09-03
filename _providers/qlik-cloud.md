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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Qlik Cloud Agentic Access
  operation_count: 32
  slug: qlik-cloud-agentic-access
  summary_line: 32 operations · 18 acting
api_count: 13
apis:
- description: WebSocket-based JSON-RPC API for direct interaction with the Qlik Associative Engine.
  name: Qlik Engine JSON API
  slug: qlik-engine-json-api
- description: APIs for data integration, ETL processes, and data pipeline management.
  name: Qlik Data Integration
  slug: qlik-data-integration
- description: API for managing app reloads and data refresh operations.
  name: Qlik Reload
  slug: qlik-reload
- description: Manage users, groups, and access control in Qlik Cloud.
  name: Qlik Users and Groups
  slug: qlik-users-and-groups
- description: Manage shared and personal spaces for organizing Qlik content.
  name: Qlik Spaces
  slug: qlik-spaces
- description: Create, manage, and interact with Qlik Sense applications.
  name: Qlik Apps
  slug: qlik-apps
- description: Create and manage automated workflows in Qlik Cloud.
  name: Qlik Automations
  slug: qlik-automations
- baseURL: https://your-tenant.region.qlikcloud.com
  baseurl_source: spec
  description: The Api Keys API from Qlik Cloud — 1 operation(s) for api keys.
  name: Qlik Cloud Api Keys API
  slug: qlik-cloud-api-keys-api
- baseURL: https://your-tenant.region.qlikcloud.com
  baseurl_source: spec
  description: The Apps API from Qlik Cloud — 6 operation(s) for apps.
  name: Qlik Cloud Apps API
  slug: qlik-cloud-apps-api
- baseURL: https://your-tenant.region.qlikcloud.com
  baseurl_source: spec
  description: The Csrf Token API from Qlik Cloud — 1 operation(s) for csrf token.
  name: Qlik Cloud Csrf Token API
  slug: qlik-cloud-csrf-token-api
- baseURL: https://your-tenant.region.qlikcloud.com
  baseurl_source: spec
  description: The Spaces API from Qlik Cloud — 4 operation(s) for spaces.
  name: Qlik Cloud Spaces API
  slug: qlik-cloud-spaces-api
- baseURL: https://your-tenant.region.qlikcloud.com
  baseurl_source: spec
  description: The Users API from Qlik Cloud — 6 operation(s) for users.
  name: Qlik Cloud Users API
  slug: qlik-cloud-users-api
- baseURL: https://your-tenant.region.qlikcloud.com
  baseurl_source: spec
  description: The Webhooks API from Qlik Cloud — 1 operation(s) for webhooks.
  name: Qlik Cloud Webhooks API
  slug: qlik-cloud-webhooks-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qlik Cloud REST Api Keys API
  slug: open-qlik-cloud-api-keys-api
- collection_type: open
  name: Qlik Cloud REST Api Keys Apps API
  slug: open-qlik-cloud-apps-api
- collection_type: open
  name: Qlik Cloud REST Api Keys Csrf Token API
  slug: open-qlik-cloud-csrf-token-api
- collection_type: open
  name: Qlik Cloud REST Api Keys Spaces API
  slug: open-qlik-cloud-spaces-api
- collection_type: open
  name: Qlik Cloud REST Api Keys Users API
  slug: open-qlik-cloud-users-api
- collection_type: open
  name: Qlik Cloud REST Api Keys Webhooks API
  slug: open-qlik-cloud-webhooks-api
- collection_type: open
  name: Qlik Cloud REST API
  slug: open-qlik-cloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qlik-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qlik-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qlik-cloud-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qlik
- group: start
  title: ''
  type: GettingStarted
  url: https://qlik.dev/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://qlik.dev/authenticate
- group: start
  title: ''
  type: Portal
  url: https://qlik.dev
- group: operate
  title: ''
  type: Community
  url: https://community.qlik.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qlik-oss
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qlik.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qlik.com/us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qlik.com/us/legal/privacy
- group: company
  title: ''
  type: Website
  url: https://www.qlik.com
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/qlik-oss/qlik-mcp-registry
created: '2024-01-01'
description: Collection of APIs for Qlik Cloud platform, providing data integration, analytics, and visualization capabilities.
finops:
- name: Qlik Cloud Finops
  service_category: API
  slug: qlik-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qlik-cloud.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Qlik Cloud
nav: Providers
network: true
overview: 'Qlik Cloud publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Api Keys API, Apps API, Csrf Token API, and 3 more. Tagged areas include Analytics, Business Intelligence, Cloud, Data Integration, and Software-as-a-Service.


  Qlik Cloud''s developer surface includes authentication, getting-started guide, developer portal, and 11 more developer resources.'
plans:
- name: Qlik Cloud Plans Pricing
  plan_count: 3
  slug: qlik-cloud-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Qlik Cloud Rate Limits
  slug: qlik-cloud-rate-limits
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 42.9
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qlik-cloud/refs/heads/main/screenshots/qlik-cloud-2026-06-20T192341.png
security:
- kind: authentication
  name: Qlik Cloud Authentication
  slug: qlik-cloud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qlik Cloud Domain Security
  slug: qlik-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: qlik-cloud
tags:
- Analytics
- Business Intelligence
- Cloud
- Data Integration
- Software-as-a-Service
- Visualization
website: https://www.qlik.com
---
