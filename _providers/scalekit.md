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
- acting_count: 15
  human_in_the_loop: 0
  name: Scalekit Agentic Access
  operation_count: 26
  slug: scalekit-agentic-access
  summary_line: 26 operations · 15 acting
api_count: 9
apis:
- description: Generate self-service admin portal links.
  name: Scalekit Admin Portal API
  slug: scalekit-admin-portal-api
- description: OAuth 2.0 client credentials token issuance.
  name: Scalekit Authentication API
  slug: scalekit-authentication-api
- description: Agent / MCP connected accounts and tool execution.
  name: Scalekit Connected Accounts API
  slug: scalekit-connected-accounts-api
- description: Enterprise SSO connections (SAML / OIDC).
  name: Scalekit Connections API
  slug: scalekit-connections-api
- description: SCIM directories and synced directory users and groups.
  name: Scalekit Directories API
  slug: scalekit-directories-api
- description: Toggle feature settings on an organization.
  name: Scalekit Organization Settings API
  slug: scalekit-organization-settings-api
- description: Create and manage tenant organizations.
  name: Scalekit Organizations API
  slug: scalekit-organizations-api
- description: Organization roles and permissions.
  name: Scalekit Roles API
  slug: scalekit-roles-api
- description: Organization user membership lifecycle and invitations.
  name: Scalekit Users & Memberships API
  slug: scalekit-users-memberships-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scalekit Admin Portal API
  slug: open-scalekit-admin-portal-api
- collection_type: open
  name: Scalekit Admin Portal Authentication API
  slug: open-scalekit-authentication-api
- collection_type: open
  name: Scalekit Admin Portal Connected Accounts API
  slug: open-scalekit-connected-accounts-api
- collection_type: open
  name: Scalekit Admin Portal Connections API
  slug: open-scalekit-connections-api
- collection_type: open
  name: Scalekit Admin Portal Directories API
  slug: open-scalekit-directories-api
- collection_type: open
  name: Scalekit Admin Portal Organization Settings API
  slug: open-scalekit-organization-settings-api
- collection_type: open
  name: Scalekit Admin Portal Organizations API
  slug: open-scalekit-organizations-api
- collection_type: open
  name: Scalekit Admin Portal Roles API
  slug: open-scalekit-roles-api
- collection_type: open
  name: Scalekit Admin Portal Users & Memberships API
  slug: open-scalekit-users-memberships-api
- collection_type: open
  name: Scalekit API
  slug: open-scalekit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scalekit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scalekit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scalekit-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/scalekit-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scalekit-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scalekit
- group: company
  title: ''
  type: Website
  url: https://www.scalekit.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scalekit.com
- group: commercial
  title: ''
  type: Plans
  url: plans/scalekit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scalekit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/scalekit-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.scalekit.com/blog
created: '2026-06-20'
description: Scalekit is the authentication platform for B2B SaaS and AI agents. It provides drop-in enterprise Single Sign-On (SAML/OIDC), SCIM directory provisioning, social login, full-stack user management, machine-to-machine (M2M) auth, and agent / MCP authentication with connected accounts and tool execution - all exposed through a per-environment REST API secured with OAuth 2.0 client credentials.
finops:
- name: Scalekit Finops
  service_category: Identity and Access Management
  slug: scalekit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scalekit.png
layout: provider
modified: '2026-06-20'
name: Scalekit
nav: Providers
network: true
overview: 'Scalekit publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Admin Portal API, Authentication API, Connected Accounts API, and 6 more. Tagged areas include Authentication, SSO, SCIM, Identity, and B2B SaaS.


  Scalekit''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Scalekit Plans Pricing
  plan_count: 5
  slug: scalekit-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 6
  name: Scalekit Rate Limits
  slug: scalekit-rate-limits
scopes:
- name: Scalekit Scopes
  scope_count: 0
  slug: scalekit-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.6
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scalekit/refs/heads/main/screenshots/scalekit-2026-06-20T193503.png
security:
- kind: authentication
  name: Scalekit Authentication
  slug: scalekit-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Scalekit Domain Security
  slug: scalekit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: scalekit
tags:
- Authentication
- SSO
- SCIM
- Identity
- B2B SaaS
- Agent Auth
website: https://www.scalekit.com
---
