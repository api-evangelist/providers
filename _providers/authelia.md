---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 71
  human_in_the_loop: 11
  name: Authelia Agentic Access
  operation_count: 111
  slug: authelia-agentic-access
  summary_line: 111 operations · 71 acting · 11 human-in-the-loop
api_count: 1
apis:
- description: Authelia acts as an OpenID Certified OpenID Connect 1.0 Provider supporting Authorization Code, Implicit, and Hybrid flows with PKCE, PAR, and various token endpoint authentication methods.
  name: Authelia OpenID Connect 1.0 Provider
  slug: authelia-oidc-provider
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: Authentication endpoints
  name: Authelia Authentication API
  slug: authelia-authentication-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: Authorization endpoints
  name: Authelia Authorization API
  slug: authelia-authorization-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: First Factor Authentication
  name: Authelia First Factor API
  slug: authelia-first-factor-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: OAuth 2.0 Endpoints
  name: Authelia OAuth 2.0 API
  slug: authelia-oauth-2-0-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: OpenID Connect 1.0 Endpoints
  name: Authelia OpenID Connect 1.0 API
  slug: authelia-openid-connect-1-0-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: Password change endpoint
  name: Authelia Password Change API
  slug: authelia-password-change-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: Password reset endpoints
  name: Authelia Password Reset API
  slug: authelia-password-reset-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: TOTP, WebAuthn and Duo endpoints
  name: Authelia Second Factor API
  slug: authelia-second-factor-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: Configuration, health and state endpoints
  name: Authelia State API
  slug: authelia-state-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: User session elevation endpoints
  name: Authelia User Elevation API
  slug: authelia-user-elevation-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: User configuration endpoints
  name: Authelia User Information API
  slug: authelia-user-information-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: General utilities used in several operations
  name: Authelia Utilities API
  slug: authelia-utilities-api
artifact_total: 51
collections:
- collection_type: open
  name: Authelia OpenID Connect 1.0 Endpoints Discovery API
  slug: open-authelia-discovery-api
- collection_type: open
  name: Authelia OpenID Connect 1.0 Endpoints Discovery OIDC API
  slug: open-authelia-oidc-api
- collection_type: open
  name: Authelia OpenID Connect 1.0 Endpoints
  slug: open-authelia
common:
- group: commercial
  href: https://artifacts.apis.io/authelia/finops/authelia-finops.yml
  title: ''
  type: FinOps
  url: finops/authelia-finops.yml
- group: other
  href: https://artifacts.apis.io/authelia/capabilities/authelia-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/authelia-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/authelia/overlays/authelia-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/authelia-api-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/authelia/authelia/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/authelia/authelia/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/authelia/authelia/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/authelia/authelia/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/authelia/authelia/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/authelia/agentic-access/authelia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/authelia-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/authelia/security/authelia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/authelia-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/authelia/authentication/authelia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/authelia-authentication.yml
- group: auth
  href: https://artifacts.apis.io/authelia/scopes/authelia-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/authelia-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.authelia.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.authelia.com/configuration/prologue/introduction/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/authelia
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/authelia/authelia
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/authelia/authelia/releases
- group: operate
  title: ''
  type: Support
  url: https://github.com/authelia/authelia/discussions
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/authelia
- group: build
  href: https://artifacts.apis.io/authelia/packages/authelia-packages.yml
  title: ''
  type: Packages
  url: packages/authelia-packages.yml
- group: agent
  href: https://artifacts.apis.io/authelia/llms/authelia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/authelia-llms.txt
- group: agent
  href: https://artifacts.apis.io/authelia/mcp/authelia-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/authelia-mcp.yml
- group: design
  href: https://artifacts.apis.io/authelia/conformance/authelia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/authelia-conformance.yml
- group: design
  href: https://artifacts.apis.io/authelia/errors/authelia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/authelia-problem-types.yml
- group: design
  href: https://artifacts.apis.io/authelia/lifecycle/authelia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/authelia-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/authelia/lifecycle/authelia-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/authelia-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/authelia/conventions/authelia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/authelia-conventions.yml
- group: operate
  href: https://artifacts.apis.io/authelia/changelog/authelia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/authelia-changelog.yml
- group: build
  href: https://artifacts.apis.io/authelia/cli/authelia-cli.yml
  title: ''
  type: CLI
  url: cli/authelia-cli.yml
- group: design
  href: https://artifacts.apis.io/authelia/data-model/authelia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/authelia-data-model.yml
- group: agent
  href: https://artifacts.apis.io/authelia/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/authelia/plans/authelia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/authelia-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/authelia/rate-limits/authelia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/authelia-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/authelia/security/authelia-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/authelia-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/authelia/security/authelia-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/authelia-vulnerability-disclosure.yml
- group: docs
  href: https://artifacts.apis.io/authelia/json-schema/authelia-configuration.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/authelia-configuration.schema.json
- group: docs
  href: https://artifacts.apis.io/authelia/json-schema/authelia-user-database.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/authelia-user-database.schema.json
- group: docs
  href: https://artifacts.apis.io/authelia/json-schema/authelia-exports.identifiers.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/authelia-exports.identifiers.schema.json
- group: docs
  href: https://artifacts.apis.io/authelia/json-schema/authelia-exports.totp.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/authelia-exports.totp.schema.json
- group: docs
  href: https://artifacts.apis.io/authelia/json-schema/authelia-exports.webauthn.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/authelia-exports.webauthn.schema.json
- group: docs
  title: ''
  type: APIReference
  url: https://www.authelia.com/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.authelia.com/integration/prologue/get-started/
- group: company
  title: ''
  type: Blog
  url: https://www.authelia.com/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.authelia.com/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.authelia.com/policies/privacy/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.authelia.com/policies/security/
- group: design
  title: ''
  type: Versioning
  url: https://www.authelia.com/policies/versioning/
created: '2026-03-25'
description: Authelia is an open source authentication and authorization server providing multi-factor authentication and single sign-on for applications behind a reverse proxy. It supports OpenID Connect 1.0, OAuth 2.0, TOTP, WebAuthn, and Duo Push as authentication methods. Authelia exposes a REST API documented with an OpenAPI specification and integrates with nginx, Traefik, Caddy, and other reverse proxies.
features:
- description: Supports TOTP, WebAuthn/FIDO2, Duo Push, and mobile authenticator apps as second factors.
  name: Multi-Factor Authentication
- description: OpenID Certified identity provider supporting Authorization Code, Implicit, and Hybrid flows.
  name: OpenID Connect 1.0 Provider
- description: Session-based SSO across all applications behind the reverse proxy with configurable session lifetime.
  name: Single Sign-On
- description: User authentication against LDAP, Active Directory, and OpenLDAP directories with group-based access control.
  name: LDAP/Active Directory Integration
- description: Fine-grained access control policies based on domain, path, user, group, and network for precise authorization.
  name: Access Control Rules
- description: Native integration with nginx, Traefik, Caddy, HAProxy, Envoy, and Skipper via forward-auth and ExtAuthz endpoints.
  name: Reverse Proxy Integration
- description: Support for WebAuthn/FIDO2 passwordless login using hardware security keys and platform authenticators.
  name: Passwordless Authentication
finops:
- has_sources: true
  method: derived
  name: Authelia Finops
  primary_unit: ''
  service_category: ''
  slug: authelia-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/authelia.png
integrations:
- description: Integration with nginx-based proxies including nginx, nginx-proxy-manager, and Swag via auth_request module.
  name: Nginx
- description: Native Traefik middleware integration via ForwardAuth for seamless authentication in Docker and Kubernetes environments.
  name: Traefik
- description: Caddy forward-auth integration for protecting applications behind the Caddy web server.
  name: Caddy
- description: User directory integration with LDAP, Active Directory, and FreeIPA for enterprise user management.
  name: LDAP/Active Directory
- description: Official Helm chart available at the authelia/chartrepo GitHub repository for Kubernetes deployment.
  name: Helm
json_schemas:
- name: Authelia Configuration.Schema
  property_count: 22
  slug: authelia-configuration.schema
- name: Authelia Exports.Identifiers.Schema
  property_count: 1
  slug: authelia-exports.identifiers.schema
- name: Authelia Exports.Totp.Schema
  property_count: 1
  slug: authelia-exports.totp.schema
- name: Authelia Exports.Webauthn.Schema
  property_count: 1
  slug: authelia-exports.webauthn.schema
- name: Authelia User Database.Schema
  property_count: 1
  slug: authelia-user-database.schema
layout: provider
modified: '2026-09-06'
name: Authelia
nav: Providers
network: true
overview: 'Authelia publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Authorization API, First Factor API, and 10 more. Tagged areas include Authentication, Authorization, LDAP, MFA, and Open Source.


  The Authelia catalog on APIs.io includes 1 Spectral governance ruleset.


  Authelia''s developer surface includes authentication, documentation, changelog, support, CLI, API reference, getting-started guide, and 40 more developer resources.'
plans:
- name: Authelia Plans Pricing
  plan_count: 0
  slug: authelia-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 11
  name: Authelia Rate Limits
  slug: authelia-rate-limits
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: Authelia API Rules
  rule_count: 70
  severity_counts:
    error: 55
    hint: 0
    info: 5
    warn: 10
  slug: authelia-rules
scopes:
- name: Authelia Scopes
  scope_count: 9
  slug: authelia-scopes
  summary_line: 9 scopes
score:
  band: strong
  composite: 54.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 31.8
    contract_quality: 50.8
    developer_ergonomics: 56.5
    discoverability: 73.2
    operational_transparency: 73.7
  open_source:
    applies: true
    score: 100.0
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/authelia/authelia-2026-06-20T172602.png
security:
- kind: authentication
  name: Authelia Authentication
  slug: authelia-authentication
  summary_line: apiKey/openIdConnect · 2 schemes
- kind: domain-security
  name: Authelia Domain Security
  slug: authelia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Authelia Vulnerability Disclosure
  slug: authelia-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 3
skills:
- name: authelia-manage-second-factor-credentials
  slug: authelia-manage-second-factor-credentials
- name: authelia-oauth2-token-lifecycle
  slug: authelia-oauth2-token-lifecycle
- name: authelia-verify-deployment-state
  slug: authelia-verify-deployment-state
slug: authelia
solutions:
- description: Complete self-hosted identity and access management solution for privacy-conscious deployments.
  name: Self-Hosted Identity
- description: Enforce zero trust network access policies for internal applications with per-request authentication verification.
  name: Zero Trust Security
tags:
- Authentication
- Authorization
- LDAP
- MFA
- Open Source
- OpenID Connect
- Self-Hosted
- SSO
- Identity Federation
use_cases:
- description: Deploy a self-hosted SSO solution for internal web applications and services without relying on cloud identity providers.
  name: Self-Hosted SSO
- description: Protect self-hosted homelab applications with MFA and access control without exposing them to the internet unprotected.
  name: Homelab Security
- description: Provide centralized authentication for small business web applications using LDAP and access control policies.
  name: Small Business Identity
- description: Act as an OpenID Connect provider for applications requiring OAuth 2.0 and OIDC-based authentication flows.
  name: OIDC Provider
website: https://www.authelia.com
---
