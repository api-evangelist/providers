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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 54
  human_in_the_loop: 5
  name: Clerk Dev Agentic Access
  operation_count: 80
  slug: clerk-dev-agentic-access
  summary_line: 80 operations · 54 acting · 5 human-in-the-loop
api_count: 15
apis:
- description: Identifiers permitted or denied from signing up.
  name: Clerk Allowlist & Blocklist API
  slug: clerk-dev-allowlist-blocklist-api
- description: Browser / device clients tracking active sessions.
  name: Clerk Clients API
  slug: clerk-dev-clients-api
- description: Email addresses, phone numbers, and message templates.
  name: Clerk Email & SMS API
  slug: clerk-dev-email-sms-api
- description: Application-level sign-up invitations.
  name: Clerk Invitations API
  slug: clerk-dev-invitations-api
- description: Public keys for verifying Clerk-issued JWTs.
  name: Clerk JWKS API
  slug: clerk-dev-jwks-api
- description: Named claim templates for custom session tokens.
  name: Clerk JWT Templates API
  slug: clerk-dev-jwt-templates-api
- description: OAuth applications where Clerk is the identity provider.
  name: Clerk OAuth Applications API
  slug: clerk-dev-oauth-applications-api
- description: Invitations to join an organization.
  name: Clerk Organization Invitations API
  slug: clerk-dev-organization-invitations-api
- description: Members of an organization and their roles.
  name: Clerk Organization Memberships API
  slug: clerk-dev-organization-memberships-api
- description: Multi-tenant organizations.
  name: Clerk Organizations API
  slug: clerk-dev-organizations-api
- description: Enterprise SSO connections.
  name: Clerk SAML & Enterprise Connections API
  slug: clerk-dev-saml-enterprise-connections-api
- description: User sessions and session tokens.
  name: Clerk Sessions API
  slug: clerk-dev-sessions-api
- description: Sign-up attempts, sign-in tokens, and actor tokens.
  name: Clerk Sign-ups & Tokens API
  slug: clerk-dev-sign-ups-tokens-api
- description: Create and manage users and their identities.
  name: Clerk Users API
  slug: clerk-dev-users-api
- description: Svix-powered webhook portal management.
  name: Clerk Webhooks API
  slug: clerk-dev-webhooks-api
artifact_total: 23
collections:
- collection_type: open
  name: Clerk Backend API
  slug: open-clerk-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clerk-dev-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clerk-dev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clerk-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clerk-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clerk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clerkinc
- group: company
  title: ''
  type: Website
  url: https://clerk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://clerk.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/clerk-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clerk-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clerk-dev-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://clerk.com/blog
created: '2026-07-02'
description: Clerk is a complete authentication and user management platform for web and mobile apps, providing embeddable UI components, SDKs, and REST APIs to handle sign-up and sign-in, users, organizations and memberships, sessions, multi-factor authentication, JWTs and JWT templates, JWKS, SAML/enterprise SSO, OAuth applications, and email/SMS verification. The Clerk Backend API (base https://api.clerk.com/v1, secret-key authenticated) manages these resources server-side, the Frontend API drives client auth flows, and change events are delivered as Svix-powered HTTP webhooks.
finops:
- name: Clerk Dev Finops
  service_category: Identity and Access Management
  slug: clerk-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clerk-dev.png
layout: provider
modified: '2026-07-02'
name: Clerk
nav: Providers
network: true
overview: 'Clerk publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Allowlist & Blocklist API, Clients API, Email & SMS API, and 12 more. Tagged areas include Authentication, User Management, Identity, Sessions, and Organizations.


  Clerk''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Clerk Dev Plans Pricing
  plan_count: 4
  slug: clerk-dev-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 10
  name: Clerk Dev Rate Limits
  slug: clerk-dev-rate-limits
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clerk-dev/refs/heads/main/screenshots/clerk-dev-2026-07-25T205602.png
security:
- kind: authentication
  name: Clerk Dev Authentication
  slug: clerk-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clerk Dev Domain Security
  slug: clerk-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clerk Dev Vulnerability Disclosure
  slug: clerk-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clerk-dev
tags:
- Authentication
- User Management
- Identity
- Sessions
- Organizations
- SSO
- JWT
- MFA
website: https://clerk.com/
---
