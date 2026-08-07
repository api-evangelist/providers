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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 36
  human_in_the_loop: 3
  name: Propelauth Agentic Access
  operation_count: 54
  slug: propelauth-agentic-access
  summary_line: 54 operations · 36 acting · 3 human-in-the-loop
api_count: 18
apis:
- description: Backend REST API for issuing, validating, listing, updating, and revoking end-user API keys that PropelAuth manages on behalf of your users and tenant organizations. Includes personal and org-scoped k
  name: PropelAuth End-User API Keys API
  slug: propelauth-api-keys-api
- description: OAuth 2.0 / OpenID Connect identity-provider endpoints exposed by your PropelAuth Auth URL. Use PropelAuth as an OIDC provider for first-party and third-party OAuth clients, including no-code / low-co
  name: PropelAuth OAuth2 API
  slug: propelauth-oauth2-api
- description: Mint short-lived access tokens for impersonation and testing
  name: PropelAuth Access Tokens API
  slug: propelauth-access-tokens-api
- description: OpenID Connect discovery
  name: PropelAuth Discovery API
  slug: propelauth-discovery-api
- description: RFC 7591 dynamic client registration
  name: PropelAuth Dynamic Client Registration API
  slug: propelauth-dynamic-client-registration-api
- description: Inspect PropelAuth dashboard employees (internal team)
  name: PropelAuth Employees API
  slug: propelauth-employees-api
- description: Inspect and revoke pending organization invites
  name: PropelAuth Invites API
  slug: propelauth-invites-api
- description: Issue one-time magic links for login flows
  name: PropelAuth Magic Links API
  slug: propelauth-magic-links-api
- description: OAuth 2.1 flows for MCP clients
  name: PropelAuth MCP OAuth 2.1 API
  slug: propelauth-mcp-oauth-2-1-api
- description: Add, remove, invite, and change roles for users within an organization
  name: PropelAuth Members API
  slug: propelauth-members-api
- description: Authorization server metadata discovery
  name: PropelAuth Metadata API
  slug: propelauth-metadata-api
- description: Migrate users from external authentication providers
  name: PropelAuth Migration API
  slug: propelauth-migration-api
- description: Create, read, update, and delete tenant organizations
  name: PropelAuth Organizations API
  slug: propelauth-organizations-api
- description: Manage custom role mappings per organization
  name: PropelAuth Role Mappings API
  slug: propelauth-role-mappings-api
- description: Manage user sessions and forced logout
  name: PropelAuth Sessions API
  slug: propelauth-sessions-api
- description: Inspect API key usage statistics
  name: PropelAuth Usage API
  slug: propelauth-usage-api
- description: Create, query, update, disable, delete, and inspect users
  name: PropelAuth Users API
  slug: propelauth-users-api
- description: Validate end-user, personal, organization, and imported API keys
  name: PropelAuth Validation API
  slug: propelauth-validation-api
arazzos:
- description: Create a user, fetch it back, then enrich the profile with a follow-up update.
  name: PropelAuth Create And Update User
  slug: propelauth-create-and-update-user-workflow
- description: Resolve an existing user by email, create a new org, and invite that user in by ID.
  name: PropelAuth Invite Existing User By ID
  slug: propelauth-invite-existing-user-by-id-workflow
- description: Create an organization, email an invite to a user, and confirm the invite is pending.
  name: PropelAuth Invite User To Org
  slug: propelauth-invite-user-to-org-workflow
- description: Create a new user, then mint a one-time magic link to sign them in.
  name: PropelAuth Issue Magic Link For New User
  slug: propelauth-issue-magic-link-for-new-user-workflow
- description: Import a user from an external auth system, resolve their ID, then attach a legacy password hash.
  name: PropelAuth Migrate User With Password
  slug: propelauth-migrate-user-with-password-workflow
- description: Resolve a user by email, remove them from an org, and confirm the remaining membership.
  name: PropelAuth Offboard User From Org
  slug: propelauth-offboard-user-from-org-workflow
- description: Create a user, create an organization, and add the user to it with a role.
  name: PropelAuth Onboard User Into Org
  slug: propelauth-onboard-user-into-org-workflow
- description: Find a user by email, change their role within an org, and confirm the new role.
  name: PropelAuth Promote Org Member
  slug: propelauth-promote-org-member-workflow
- description: Create an organization, issue an API key bound to it, then read the key's metadata back.
  name: PropelAuth Provision Org API Key
  slug: propelauth-provision-org-api-key-workflow
- description: Stand up a new organization, create its first admin user, add them, and verify membership.
  name: PropelAuth Provision Org With Admin
  slug: propelauth-provision-org-with-admin-workflow
- description: Find a pending invite for an org and revoke it when one is outstanding.
  name: PropelAuth Revoke Pending Invite
  slug: propelauth-revoke-pending-invite-workflow
- description: Find a user's active API key, revoke it, and issue a fresh replacement.
  name: PropelAuth Rotate User API Key
  slug: propelauth-rotate-user-api-key-workflow
- description: Look a user up by email and update them if they exist, otherwise create them.
  name: PropelAuth Upsert User By Email
  slug: propelauth-upsert-user-by-email-workflow
artifact_total: 79
collections:
- collection_type: postman
  name: PropelAuth End-User API Keys API
  slug: postman-propelauth-api-keys-api
- collection_type: postman
  name: PropelAuth MCP Authentication API
  slug: postman-propelauth-mcp-api
- collection_type: postman
  name: PropelAuth OAuth2 API
  slug: postman-propelauth-oauth2-api
- collection_type: postman
  name: PropelAuth Organization API
  slug: postman-propelauth-org-api
- collection_type: postman
  name: PropelAuth User API
  slug: postman-propelauth-user-api
- collection_type: open
  name: PropelAuth End-User API Keys API
  slug: open-propelauth-api-keys-api
- collection_type: open
  name: PropelAuth MCP Authentication API
  slug: open-propelauth-mcp-api
- collection_type: open
  name: PropelAuth OAuth2 API
  slug: open-propelauth-oauth2-api
- collection_type: open
  name: PropelAuth Organization API
  slug: open-propelauth-org-api
- collection_type: open
  name: PropelAuth User API
  slug: open-propelauth-user-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/propelauth-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/propelauth-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/propelauth-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/propelauth-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/propelauth/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-create-and-update-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-invite-existing-user-by-id-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-invite-user-to-org-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-issue-magic-link-for-new-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-migrate-user-with-password-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-offboard-user-from-org-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-onboard-user-into-org-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-promote-org-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-provision-org-api-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-provision-org-with-admin-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-revoke-pending-invite-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-rotate-user-api-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/propelauth-upsert-user-by-email-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.propelauth.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.propelauth.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.propelauth.com/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.propelauth.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.propelauth.com/reference/api/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.propelauth.com/reference/api/user
- group: docs
  title: ''
  type: Documentation
  url: https://docs.propelauth.com/reference/api/org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.propelauth.com/reference/api/apikey
- group: docs
  title: ''
  type: Documentation
  url: https://docs.propelauth.com/reference/api/oauth2
- group: docs
  title: ''
  type: Documentation
  url: https://docs.propelauth.com/mcp-authentication/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.propelauth.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.propelauth.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.propelauth.com/default/history.rss
- group: company
  title: ''
  type: Blog
  url: https://www.propelauth.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.propelauth.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.propelauth.com/legal/privacy-policy
- group: start
  title: ''
  type: Signup
  url: https://auth.propelauth.com/en/signup
- group: docs
  title: ''
  type: Documentation
  url: https://byo.propelauth.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.propelauth.com/files/PropelAuth.postman_collection.json
- group: operate
  title: ''
  type: Support
  url: support@propelauth.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PropelAuth
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/react
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/javascript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/nextjs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/express
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/propelauth-fastapi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/propelauth-flask
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/propelauth-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/propelauth-django-rest-framework
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/propelauth-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/rust
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/propelauth-rb
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/cloudflare-worker
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/frontend-apis
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PropelAuth/node-apis
- group: build
  title: ''
  type: Tools
  url: https://github.com/PropelAuth/cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/PropelAuth/terraform-provider-propelauth
- group: build
  title: ''
  type: Tools
  url: https://github.com/PropelAuth/byo-go
- group: build
  title: ''
  type: Tools
  url: https://github.com/PropelAuth/propelauth-byo-java
- group: build
  title: ''
  type: Tools
  url: https://github.com/PropelAuth/base-elements
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/PropelAuth/documentation
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/react-frontend-starter
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/express-backend-starter
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/flask-backend-starter
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/fastapi-backend-starter
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/python-chalice-backend-starter
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/rust-axum-starter
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/redwood
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/postgraphile-propelauth-starter
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/nextjs-example-app
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/react-express-comment-example
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/demo-genai-api-keys
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/demo-b2b-coupon-generator
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/PropelAuth/windows-login-pages
- group: commercial
  title: ''
  type: Plans
  url: plans/propelauth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/propelauth-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/propelauth-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/propelauth-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/propelauth-rules.yml
created: '2026-05-25T00:00:00.000Z'
description: PropelAuth is a B2B SaaS authentication and multi-tenant user management platform purpose-built for organizations that sell to other organizations. It provides hosted login UIs, first-class organizations / tenants with custom roles and permissions, enterprise SSO via SAML and OIDC, SCIM directory sync, end-user API keys with validation and usage reporting, OAuth 2.0 / OpenID Connect identity-provider endpoints, and OAuth 2.1 MCP server authentication with dynamic client registration for AI agents. Backend SDKs span Node, Express, FastAPI, Flask, Django REST Framework, Python, Go, Rust, .NET, Ruby, and Cloudflare Workers; frontend SDKs cover React, JavaScript, and Next.js (App + Pages Router). A Terraform provider and official CLI back infrastructure-as-code workflows. Pricing starts free with 10,000 MAU and scales through Growth ($150/mo) and Growth Plus ($500/mo) to custom Enterprise contracts.
examples:
- key_count: 2
  name: Propelauth Create Magic Link Example
  slug: propelauth-create-magic-link-example
- key_count: 2
  name: Propelauth Create Org Example
  slug: propelauth-create-org-example
- key_count: 2
  name: Propelauth Create User Example
  slug: propelauth-create-user-example
- key_count: 2
  name: Propelauth Validate Api Key Example
  slug: propelauth-validate-api-key-example
features:
- Hosted, customizable login UIs for B2B SaaS
- First-class organizations / tenants with custom roles and granular permissions (RBAC)
- End-user API keys (personal and org-scoped) with validation, usage stats, and import of legacy keys
- Enterprise SSO via SAML and OIDC with self-service per-organization setup (Okta, Entra ID, etc.)
- SCIM directory sync for enterprise customers (Growth Plus and Enterprise tiers)
- MCP server authentication via OAuth 2.1, PKCE, dynamic client registration, and token introspection
- User impersonation with audit trail and alerting
- Multi-factor authentication (TOTP) enforceable per organization
- Magic links and password authentication with configurable password policies
- Per-organization 2FA enforcement and session controls
- OAuth 2.0 / OpenID Connect identity-provider endpoints including discovery
- User migration from external auth providers (bcrypt, argon2, scrypt, pbkdf2, firebase scrypt)
- Separate staging environment included on Growth tier and above
- Custom domain on the free tier
- Backend SDKs for Node, Express, FastAPI, Flask, Django REST Framework, Python, Go, Rust, .NET, Ruby, and Cloudflare Workers
- Frontend SDKs for React, JavaScript, and Next.js (App + Pages Router)
- Official PropelAuth CLI and Terraform provider for infrastructure-as-code
- Postman collection for the entire backend API
- 10,000 MAU included on every tier; overage $0.05/MAU on Growth and Growth Plus
- Advanced API Keys add-on for 5,000,000 monthly validations
- Bring-Your-Own-Auth deployment mode (`byo.propelauth.com`)
finops:
- name: Propelauth Finops
  service_category: Identity
  slug: propelauth-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/propelauth.png
json_schemas:
- name: PropelAuth End-User API Key
  property_count: 7
  slug: propelauth-api-key
- name: PropelAuth Organization
  property_count: 14
  slug: propelauth-org
- name: PropelAuth User
  property_count: 19
  slug: propelauth-user
jsonld:
- class_count: 0
  name: Propelauth Context
  property_count: 4
  slug: propelauth-context
layout: provider
modified: '2026-05-25'
name: PropelAuth
nav: Providers
network: true
overview: 'PropelAuth publishes 18 APIs on the [APIs.io](https://apis.io/) network, including End-User API Keys API, OAuth2 API, Access Tokens API, and 15 more. Tagged areas include Authentication, Identity, B2B, Multi-Tenancy, and Authorization.


  The PropelAuth catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  PropelAuth''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, signup flow, and 72 more developer resources.'
plans:
- name: Propelauth Plans Pricing
  plan_count: 4
  slug: propelauth-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 4
  name: Propelauth Rate Limits
  slug: propelauth-rate-limits
rules:
- name: PropelAuth API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: propelauth-jsonschema-spectral-rules
- name: PropelAuth API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: propelauth-rules
score:
  band: exemplar
  composite: 68.7
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 73.4
    developer_ergonomics: 65.2
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 68.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/propelauth/refs/heads/main/screenshots/propelauth-2026-06-20T192214.png
security:
- kind: authentication
  name: Propelauth Authentication
  slug: propelauth-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Propelauth Domain Security
  slug: propelauth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Propelauth Trust Center
  slug: propelauth-trust-center
  summary_line: SOC 2, GDPR
slug: propelauth
tags:
- Authentication
- Identity
- B2B
- Multi-Tenancy
- Authorization
- RBAC
- SSO
- SCIM
- MCP
- API Keys
website: https://www.propelauth.com
---
