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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Scalekit Agentic Access
  operation_count: 26
  slug: scalekit-agentic-access
  summary_line: 26 operations · 15 acting
api_count: 1
apis:
- baseURL: https://{environment}.scalekit.com
  baseurl_source: declared
  description: Generate self-service admin portal links.
  name: Scalekit Admin Portal API
  slug: scalekit-admin-portal-api
- baseURL: https://{environment}.scalekit.com
  baseurl_source: declared
  description: OAuth 2.0 client credentials token issuance.
  name: Scalekit Authentication API
  slug: scalekit-authentication-api
- baseURL: https://{environment}.scalekit.com
  baseurl_source: declared
  description: Agent / MCP connected accounts and tool execution.
  name: Scalekit Connected Accounts API
  slug: scalekit-connected-accounts-api
- baseURL: https://{environment}.scalekit.com
  baseurl_source: declared
  description: Enterprise SSO connections (SAML / OIDC).
  name: Scalekit Connections API
  slug: scalekit-connections-api
- baseURL: https://{environment}.scalekit.com
  baseurl_source: declared
  description: SCIM directories and synced directory users and groups.
  name: Scalekit Directories API
  slug: scalekit-directories-api
- baseURL: https://{environment}.scalekit.com
  baseurl_source: declared
  description: Toggle feature settings on an organization.
  name: Scalekit Organization Settings API
  slug: scalekit-organization-settings-api
- baseURL: https://{environment}.scalekit.com
  baseurl_source: declared
  description: Create and manage tenant organizations.
  name: Scalekit Organizations API
  slug: scalekit-organizations-api
- baseURL: https://{environment}.scalekit.com
  baseurl_source: declared
  description: Organization roles and permissions.
  name: Scalekit Roles API
  slug: scalekit-roles-api
- baseURL: https://{environment}.scalekit.com
  baseurl_source: declared
  description: Organization user membership lifecycle and invitations.
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
  href: https://raw.githubusercontent.com/api-evangelist/scalekit/refs/heads/main/agentic-access/scalekit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scalekit-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scalekit/refs/heads/main/security/scalekit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scalekit-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scalekit/refs/heads/main/authentication/scalekit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scalekit-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scalekit/refs/heads/main/scopes/scalekit-scopes.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/scalekit/refs/heads/main/plans/scalekit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scalekit-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/scalekit/refs/heads/main/rate-limits/scalekit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scalekit-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/scalekit/refs/heads/main/finops/scalekit-finops.yml
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
modified: '2026-09-16'
name: Scalekit
nav: Providers
network: true
overview: 'Scalekit publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Admin Portal API, Authentication API, Connected Accounts API, and 6 more. Tagged areas include Authentication, SSO, SCIM, Identity, and B2B SaaS.


  Scalekit''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Scalekit Plans Pricing
  plan_count: 5
  slug: scalekit-plans-pricing
random_paper: 12
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
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 61.6
    catalog_earned_first_party: 0.0
    catalog_gap: 53.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 36.3
    contract_governance: 0.0
    contract_quality: 48.0
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 31.1
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 27.8
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
- Identity Federation
website: https://www.scalekit.com
---
