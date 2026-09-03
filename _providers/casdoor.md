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
- acting_count: 13
  human_in_the_loop: 0
  name: Casdoor Agentic Access
  operation_count: 24
  slug: casdoor-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 1
apis:
- description: The Casdoor REST API provides programmatic access to the IAM platform's core resources including users, organizations, applications, roles, groups, permissions, identity providers, tokens, sessions, c
  name: Casdoor REST API
  slug: casdoor-rest-api
- description: Casdoor implements an OAuth 2.0 authorization server and OpenID Connect identity provider, exposing the standard authorization, token, userinfo, revocation, introspection, JWKS, and OIDC discovery end
  name: Casdoor OAuth 2.0 / OIDC Provider
  slug: casdoor-oauth-oidc
- description: SAML 2.0 identity provider endpoints in Casdoor that issue SAML assertions to enterprise service providers, supporting SSO scenarios for legacy and enterprise SaaS applications via standard SAML metad
  name: Casdoor SAML 2.0 Identity Provider
  slug: casdoor-saml
- description: Casdoor exposes a CAS (Central Authentication Service) server compatible with CAS protocol versions 1.0, 2.0, and 3.0, providing single sign-on to applications that integrate via the CAS ticket-valida
  name: Casdoor CAS Server
  slug: casdoor-cas
- description: Casdoor provides an LDAP server interface so that legacy applications and infrastructure components requiring LDAP authentication can bind against Casdoor users and groups, and a sync engine that impo
  name: Casdoor LDAP Server
  slug: casdoor-ldap
- description: SCIM 2.0 (System for Cross-domain Identity Management) endpoints for automated user and group provisioning between Casdoor and downstream identity-aware systems.
  name: Casdoor SCIM 2.0 API
  slug: casdoor-scim
- description: Casdoor's MCP (Model Context Protocol) gateway and A2A (Agent-to-Agent) protocol surface, designed to broker authentication and authorization for AI agents and MCP-aware tooling using Casdoor as the i
  name: Casdoor MCP Gateway
  slug: casdoor-mcp-gateway
- description: Outbound webhook events that notify external systems of identity events such as user signup, login, logout, profile changes, password resets, and MFA enrollments.
  name: Casdoor Webhooks
  slug: casdoor-webhooks
- baseURL: https://door.casdoor.com
  baseurl_source: declared
  description: OAuth/OIDC client applications
  name: Casdoor Applications API
  slug: casdoor-applications-api
- baseURL: https://door.casdoor.com
  baseurl_source: declared
  description: Login, callback, and device authorization
  name: Casdoor Authentication API
  slug: casdoor-authentication-api
- baseURL: https://door.casdoor.com
  baseurl_source: declared
  description: OpenID Connect discovery and JWKS endpoints
  name: Casdoor OIDC API
  slug: casdoor-oidc-api
- baseURL: https://door.casdoor.com
  baseurl_source: declared
  description: Multi-tenant organization management
  name: Casdoor Organizations API
  slug: casdoor-organizations-api
- baseURL: https://door.casdoor.com
  baseurl_source: declared
  description: Casbin policy enforcement
  name: Casdoor Permissions API
  slug: casdoor-permissions-api
- baseURL: https://door.casdoor.com
  baseurl_source: declared
  description: Role-based access control
  name: Casdoor Roles API
  slug: casdoor-roles-api
- baseURL: https://door.casdoor.com
  baseurl_source: declared
  description: User CRUD and credential operations
  name: Casdoor Users API
  slug: casdoor-users-api
artifact_total: 75
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Casdoor REST Applications API
  slug: open-casdoor-applications-api
- collection_type: open
  name: Casdoor REST Applications Authentication API
  slug: open-casdoor-authentication-api
- collection_type: open
  name: Casdoor REST Applications OIDC API
  slug: open-casdoor-oidc-api
- collection_type: open
  name: Casdoor REST Applications Organizations API
  slug: open-casdoor-organizations-api
- collection_type: open
  name: Casdoor REST Applications Permissions API
  slug: open-casdoor-permissions-api
- collection_type: open
  name: Casdoor REST Applications Roles API
  slug: open-casdoor-roles-api
- collection_type: open
  name: Casdoor REST Applications Users API
  slug: open-casdoor-users-api
- collection_type: open
  name: Casdoor REST API
  slug: open-casdoor
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/casdoor/casdoor/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/casdoor/casdoor/blob/master/SECURITY.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/casdoor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/casdoor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/casdoor-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://casdoor.org
- group: docs
  title: ''
  type: Documentation
  url: https://casdoor.ai/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://casdoor.ai/docs/basic/server-installation
- group: auth
  title: ''
  type: Authentication
  url: https://casdoor.ai/docs/basic/core-concepts
- group: docs
  title: ''
  type: Swagger
  url: https://door.casdoor.com/swagger/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/casdoor/casdoor
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/casdoor
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/casdoor/casdoor
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/casdoor/casdoor/issues
- group: company
  title: ''
  type: Blog
  url: https://casdoor.org/blog
- group: operate
  title: ''
  type: Community
  url: https://casdoor.ai/docs/community/forum
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/5rPsrAzK7S
- group: commercial
  title: ''
  type: License
  url: https://github.com/casdoor/casdoor/blob/master/LICENSE
- group: other
  title: ''
  type: DockerHub
  url: https://hub.docker.com/r/casbin/casdoor
- group: start
  title: ''
  type: Demo
  url: https://door.casdoor.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://casdoor.org/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://casdoor.com/pricing
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/casdoor/public-mcp-server-registry
created: '2026-03-25'
description: Casdoor is an open-source, AI-first identity and access management (IAM) and MCP gateway authentication server with a web UI. Built in Go (Beego) with a React frontend, Casdoor supports OAuth 2.0, OIDC, SAML 2.0, CAS, LDAP, Kerberos/SPNEGO, WebAuthn / Passkeys, TOTP / MFA, SCIM 2.0 provisioning, social login, multi-tenant organizations, role-based access control, and an MCP Gateway plus A2A Protocol for agent-to-agent communication. The platform exposes a RESTful API documented via Swagger and ships SDKs for Go, Java, Python, Node.js, C#, C++, PHP, Ruby, JavaScript, Lua, and Haskell. Released under the Apache License 2.0.
features:
- name: OAuth 2.0 Server
- name: OIDC Provider
- name: SAML 2.0 IdP
- name: CAS Server
- name: LDAP Server
- name: SCIM 2.0 Provisioning
- name: WebAuthn / Passkeys
- name: TOTP MFA
- name: Face ID Biometrics
- name: Social Login
- name: RBAC
- name: ABAC
- name: ACL
- name: Multi-Tenancy
- name: Organizations
- name: Audit Logs
- name: Webhooks
- name: Identity Provider Federation
- name: MCP Gateway
- name: A2A Protocol
- name: Self-Hosted
- name: Apache 2.0 License
finops:
- name: Casdoor Finops
  service_category: API
  slug: casdoor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/casdoor.png
integrations:
- name: GitHub
- name: Google
- name: Azure AD
- name: WeChat
- name: QQ
- name: MySQL
- name: PostgreSQL
- name: SQL Server
- name: Redis
- name: Beego
- name: React
- name: Casbin
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Casdoor
nav: Providers
network: true
overview: 'Casdoor publishes 8 APIs on the [APIs.io](https://apis.io/) network, including REST API, Applications API, Authentication API, and 5 more. Tagged areas include Authentication, Authorization, IAM, Identity, and LDAP.


  Casdoor''s developer surface includes authentication, documentation, getting-started guide, GitHub presence, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Casdoor Plans Pricing
  plan_count: 3
  slug: casdoor-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Casdoor Rate Limits
  slug: casdoor-rate-limits
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 12.6
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 60.0
  previous_composite: 28.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/casdoor/refs/heads/main/screenshots/casdoor-2026-06-20T174037.png
security:
- kind: authentication
  name: Casdoor Authentication
  slug: casdoor-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Casdoor Domain Security
  slug: casdoor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: casdoor
tags:
- Authentication
- Authorization
- IAM
- Identity
- LDAP
- MCP
- MFA
- OIDC
- Open-Source
- Passkeys
- SAML
- SCIM
- Single Sign-On
- SSO
- WebAuthn
use_cases:
- name: Single Sign-On
- name: Customer Identity (CIAM)
- name: Workforce Identity
- name: Passwordless Login
- name: Multi-Factor Authentication
- name: Enterprise SSO via SAML
- name: API Authorization
- name: Identity Provider for AI Agents
- name: User Provisioning Automation
- name: Self-Hosted Auth Server
website: https://casdoor.org
---
