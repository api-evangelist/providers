---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Egnyte Agentic Access
  operation_count: 14
  slug: egnyte-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- description: The File System API from Egnyte — 2 operation(s) for file system.
  name: Egnyte File System API
  slug: egnyte-file-system-api
- description: The Groups API from Egnyte — 1 operation(s) for groups.
  name: Egnyte Groups API
  slug: egnyte-groups-api
- description: The Links API from Egnyte — 1 operation(s) for links.
  name: Egnyte Links API
  slug: egnyte-links-api
- description: The Permissions API from Egnyte — 1 operation(s) for permissions.
  name: Egnyte Permissions API
  slug: egnyte-permissions-api
- description: The Users API from Egnyte — 2 operation(s) for users.
  name: Egnyte Users API
  slug: egnyte-users-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Egnyte Public File System API
  slug: open-egnyte-file-system-api
- collection_type: open
  name: Egnyte Public File System Groups API
  slug: open-egnyte-groups-api
- collection_type: open
  name: Egnyte Public File System Links API
  slug: open-egnyte-links-api
- collection_type: open
  name: Egnyte Public File System Permissions API
  slug: open-egnyte-permissions-api
- collection_type: open
  name: Egnyte Public File System Users API
  slug: open-egnyte-users-api
- collection_type: open
  name: Egnyte Public API
  slug: open-egnyte
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/egnyte-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/egnyte-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/egnyte-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/egnyte-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.egnyte.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.egnyte.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.egnyte.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.egnyte.com/docs/read/Public_API_Authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.egnyte.com/docs/read/getting_started
- group: other
  title: ''
  type: API Explorer
  url: https://developers.egnyte.com/io-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.egnyte.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://developers.egnyte.com/member/register
- group: start
  title: ''
  type: Login
  url: https://developers.egnyte.com/member/login
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.egnyte.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.egnyte.com/
- group: company
  title: ''
  type: Blog
  url: https://www.egnyte.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.egnyte.com/corp/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.egnyte.com/corp/legal/end-user-license-agreement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/egnyte
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/egnyte/python-egnyte
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/egnyte
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/egnyte
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/egnyte/egnyte-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.egnyte.com/llms.txt
created: '2026-05-11'
description: Egnyte is an enterprise content collaboration and file sharing platform that provides secure cloud and hybrid file storage, document collaboration, governance, and data security controls for regulated industries. Egnyte's Public API exposes the file system, users, groups, permissions, audit reporting, links, and workflow capabilities so partners and customers can build custom integrations. Authentication is handled via OAuth 2.0 (Authorization Code, Implicit, Resource Owner, and Refresh Token flows) scoped per API surface.
graphqls:
- description: Egnyte is a cloud content platform for business. The API covers file and folder management, sharing permissions, link creation, search, version history, audit logs, user provisioning, and project work
  name: Egnyte GraphQL API
  slug: egnyte-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/egnyte.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Egnyte
nav: Providers
network: true
overview: 'Egnyte publishes 5 APIs on the [APIs.io](https://apis.io/) network, including File System API, Groups API, Links API, and 2 more. Tagged areas include File Sharing, Content Collaboration, Enterprise Storage, Document-Management, and Governance.


  Egnyte''s developer surface includes authentication, documentation, getting-started guide, pricing, signup flow, support, engineering blog, and 17 more developer resources.'
random_paper: 1
scopes:
- name: Egnyte Scopes
  scope_count: 6
  slug: egnyte-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 56.6
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/egnyte/refs/heads/main/screenshots/egnyte-2026-06-20T180523.png
security:
- kind: authentication
  name: Egnyte Authentication
  slug: egnyte-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Egnyte Domain Security
  slug: egnyte-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: egnyte
tags:
- File Sharing
- Content Collaboration
- Enterprise Storage
- Document-Management
- Governance
- Data Security
website: https://www.egnyte.com
---
