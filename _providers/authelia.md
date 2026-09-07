---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.6
  scored_at: '2026-09-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Authelia Agentic Access
  operation_count: 12
  slug: authelia-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- description: Authelia acts as an OpenID Certified OpenID Connect 1.0 Provider supporting Authorization Code, Implicit, and Hybrid flows with PKCE, PAR, and various token endpoint authentication methods.
  name: Authelia OpenID Connect 1.0 Provider
  slug: authelia-oidc-provider
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: The full first-party Authelia HTTP API — the portal, authorization, authentication, second factor, user information, session elevation, password reset/change and OpenID Connect 1.0 surfaces. Described
  name: Authelia API
  slug: authelia-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: Well-known discovery endpoints.
  name: Authelia Discovery API
  slug: authelia-discovery-api
- baseURL: https://auth.example.com
  baseurl_source: declared
  description: OpenID Connect 1.0 / OAuth 2.0 provider endpoints.
  name: Authelia OIDC API
  slug: authelia-oidc-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: AgenticAccess
  url: agentic-access/authelia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/authelia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/authelia-authentication.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/authelia-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/authelia-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/authelia-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/authelia-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/authelia-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/authelia-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/authelia-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/authelia-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/authelia-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/authelia-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/authelia-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/authelia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/authelia-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/authelia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/authelia-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/authelia-configuration.schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/authelia-user-database.schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/authelia-exports.identifiers.schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/authelia-exports.totp.schema.json
- group: docs
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
- name: Authelia Finops
  service_category: API
  slug: authelia-finops
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
  property_count: 0
  slug: authelia-configuration.schema
- name: Authelia Exports.Identifiers.Schema
  property_count: 0
  slug: authelia-exports.identifiers.schema
- name: Authelia Exports.Totp.Schema
  property_count: 0
  slug: authelia-exports.totp.schema
- name: Authelia Exports.Webauthn.Schema
  property_count: 0
  slug: authelia-exports.webauthn.schema
- name: Authelia User Database.Schema
  property_count: 0
  slug: authelia-user-database.schema
layout: provider
modified: '2026-09-06'
name: Authelia
nav: Providers
network: true
overview: 'Authelia publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, OIDC API, and 1 more. Tagged areas include Authentication, Authorization, LDAP, MFA, and Open-Source.


  Authelia''s developer surface includes authentication, documentation, changelog, support, CLI, API reference, getting-started guide, and 37 more developer resources.'
plans:
- name: Authelia Plans Pricing
  plan_count: 0
  slug: authelia-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 11
  name: Authelia Rate Limits
  slug: authelia-rate-limits
scopes:
- name: Authelia Scopes
  scope_count: 9
  slug: authelia-scopes
  summary_line: 9 scopes
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.8
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 56.2
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 73.7
  open_source:
    applies: true
    score: 100.0
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/authelia/refs/heads/main/screenshots/authelia-2026-06-20T172602.png
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
  summary_line: disclosure policy published
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
- Open-Source
- OpenID Connect
- Self-Hosted
- SSO
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
