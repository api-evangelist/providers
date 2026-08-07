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
- acting_count: 8
  human_in_the_loop: 0
  name: Authentik Agentic Access
  operation_count: 27
  slug: authentik-agentic-access
  summary_line: 27 operations · 8 acting
api_count: 10
apis:
- description: Users, applications, groups and tokens.
  name: Authentik Core API
  slug: authentik-core-api
- description: Certificate-key pairs.
  name: Authentik Crypto API
  slug: authentik-crypto-api
- description: Audit and notification events.
  name: Authentik Events API
  slug: authentik-events-api
- description: Authentication and enrollment flows.
  name: Authentik Flows API
  slug: authentik-flows-api
- description: Policies and policy bindings.
  name: Authentik Policies API
  slug: authentik-policies-api
- description: OAuth2/OIDC, SAML, LDAP, Proxy and other providers.
  name: Authentik Providers API
  slug: authentik-providers-api
- description: Role-based access control.
  name: Authentik RBAC API
  slug: authentik-rbac-api
- description: Self-describing OpenAPI schema.
  name: Authentik Schema API
  slug: authentik-schema-api
- description: External identity sources.
  name: Authentik Sources API
  slug: authentik-sources-api
- description: Flow stages (identification, password, etc.).
  name: Authentik Stages API
  slug: authentik-stages-api
artifact_total: 36
collections:
- collection_type: open
  name: authentik API
  slug: open-authentik
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/authentik-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/authentik-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/authentik-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/authentik-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/authentik-security
- group: company
  title: ''
  type: Website
  url: https://goauthentik.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.goauthentik.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goauthentik
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/goauthentik/authentik
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/goauthentik/authentik/releases
- group: operate
  title: ''
  type: Support
  url: https://github.com/goauthentik/authentik/discussions
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/jg33eMhnj6
- group: commercial
  title: ''
  type: Pricing
  url: https://goauthentik.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://goauthentik.io/blog/rss.xml
created: '2026-03-25'
description: Authentik is an open source identity provider with a comprehensive REST API for managing users, groups, flows, providers, sources, policies, and outposts. It supports OAuth2, OIDC, SAML, LDAP, SCIM, and RADIUS protocols with official client SDKs in TypeScript, Python, Go, Rust, Kotlin, and Swift.
features:
- description: Full REST API covering all authentik features with built-in Swagger UI at /api/v3/ on every instance.
  name: Comprehensive REST API
- description: Native support for OAuth2, OIDC, SAML, LDAP, SCIM, RADIUS, and SSTP protocols for broad integration coverage.
  name: Multi-Protocol Support
- description: Customizable authentication and enrollment flows with visual flow designer for configuring multi-step authentication processes.
  name: Flow Engine
- description: Official API client SDKs in TypeScript, Python, Go, Rust, Kotlin, and Swift auto-generated from the OpenAPI schema.
  name: Multi-Language SDKs
- description: Official Terraform provider for infrastructure-as-code management of authentik resources.
  name: Terraform Provider
- description: Official Helm chart for Kubernetes deployment with configurable replicas, persistence, and external database support.
  name: Helm Deployment
- description: Role-based access control for granular permission management across authentik resources and administrative functions.
  name: RBAC
finops:
- name: Authentik Finops
  service_category: API
  slug: authentik-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/authentik.png
integrations:
- description: Forward auth integration with major reverse proxies for transparent application authentication.
  name: Nginx/Traefik/Caddy
- description: Native Kubernetes deployment via Helm chart with optional operator and RBAC integration.
  name: Kubernetes
- description: LDAP outpost that exposes authentik users to LDAP-compatible applications without a directory server.
  name: LDAP Directory
- description: Native OAuth2 integration with Grafana for unified authentication in monitoring stacks.
  name: Grafana
- description: OIDC or SAML integration with Nextcloud for unified login in self-hosted file storage.
  name: Nextcloud
layout: provider
modified: '2026-04-19'
name: Authentik
nav: Providers
network: true
overview: 'Authentik publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Core API, Crypto API, Events API, and 7 more. Tagged areas include Authentication, Authorization, Identity Provider, LDAP, and OAuth.


  Authentik''s developer surface includes authentication, documentation, changelog, support, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Authentik Plans Pricing
  plan_count: 3
  slug: authentik-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Authentik Rate Limits
  slug: authentik-rate-limits
score:
  band: developing
  composite: 42.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 53.5
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/screenshots/authentik-2026-06-20T172603.png
security:
- kind: authentication
  name: Authentik Authentication
  slug: authentik-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Authentik Domain Security
  slug: authentik-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Authentik Vulnerability Disclosure
  slug: authentik-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: authentik
solutions:
- description: Complete identity and access management platform deployable on any infrastructure with no vendor lock-in.
  name: Self-Hosted IAM
- description: Secure and authenticate any application using forward auth with optional MFA and per-user access policies.
  name: Application Gateway
tags:
- Authentication
- Authorization
- Identity Provider
- LDAP
- OAuth
- Open Source
- OpenID Connect
- SAML
- SCIM
- Self-Hosted
use_cases:
- description: Deploy a complete identity provider on-premises or in private cloud with full data sovereignty.
  name: Self-Hosted Identity Provider
- description: Provide single sign-on for all internal applications using OIDC, SAML, or LDAP protocol support.
  name: SSO Gateway
- description: Build customer-facing registration and authentication flows with customizable enrollment and recovery processes.
  name: B2C Identity
- description: Implement zero trust application access with forward auth proxy integration and per-application policies.
  name: Zero Trust Access
website: https://goauthentik.io
---
