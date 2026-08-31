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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Authentik Agentic Access
  operation_count: 27
  slug: authentik-agentic-access
  summary_line: 27 operations · 8 acting
api_count: 1
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
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: authentik Core API
  slug: open-authentik-core-api
- collection_type: open
  name: authentik Core Crypto API
  slug: open-authentik-crypto-api
- collection_type: open
  name: authentik Core Events API
  slug: open-authentik-events-api
- collection_type: open
  name: authentik Core Flows API
  slug: open-authentik-flows-api
- collection_type: open
  name: authentik Core Policies API
  slug: open-authentik-policies-api
- collection_type: open
  name: authentik Core Providers API
  slug: open-authentik-providers-api
- collection_type: open
  name: authentik Core RBAC API
  slug: open-authentik-rbac-api
- collection_type: open
  name: authentik Core Schema API
  slug: open-authentik-schema-api
- collection_type: open
  name: authentik Core Sources API
  slug: open-authentik-sources-api
- collection_type: open
  name: authentik Core Stages API
  slug: open-authentik-stages-api
- collection_type: open
  name: authentik API
  slug: open-authentik
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/goauthentik/authentik/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/goauthentik/authentik/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/goauthentik/authentik/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/goauthentik/authentik/blob/main/CONTRIBUTING.md
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
overview: 'Authentik publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Core API, Crypto API, Events API, and 7 more. Tagged areas include Authentication, Authorization, Identity Provider, LDAP, and Open-Source.


  Authentik''s developer surface includes authentication, documentation, changelog, support, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Authentik Plans Pricing
  plan_count: 3
  slug: authentik-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Authentik Rate Limits
  slug: authentik-rate-limits
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 5.7
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 48.7
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
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
- Open-Source
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
