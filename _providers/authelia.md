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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Authelia Agentic Access
  operation_count: 12
  slug: authelia-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 3
apis:
- description: Authelia acts as an OpenID Certified OpenID Connect 1.0 Provider supporting Authorization Code, Implicit, and Hybrid flows with PKCE, PAR, and various token endpoint authentication methods.
  name: Authelia OpenID Connect 1.0 Provider
  slug: authelia-oidc-provider
- description: Well-known discovery endpoints.
  name: Authelia Discovery API
  slug: authelia-discovery-api
- description: OpenID Connect 1.0 / OAuth 2.0 provider endpoints.
  name: Authelia OIDC API
  slug: authelia-oidc-api
artifact_total: 29
collections:
- collection_type: open
  name: Authelia OpenID Connect 1.0 Endpoints
  slug: open-authelia
common:
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
layout: provider
modified: '2026-04-19'
name: Authelia
nav: Providers
network: true
overview: 'Authelia publishes 2 APIs on the [APIs.io](https://apis.io/) network: Discovery API and OIDC API. Tagged areas include Authentication, Authorization, LDAP, MFA, and Open Source.


  Authelia''s developer surface includes authentication, documentation, changelog, support, and 7 more developer resources.'
plans:
- name: Authelia Plans Pricing
  plan_count: 3
  slug: authelia-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Authelia Rate Limits
  slug: authelia-rate-limits
scopes:
- name: Authelia Scopes
  scope_count: 5
  slug: authelia-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 40.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.9
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/authelia/refs/heads/main/screenshots/authelia-2026-06-20T172602.png
security:
- kind: authentication
  name: Authelia Authentication
  slug: authelia-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Authelia Domain Security
  slug: authelia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
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
