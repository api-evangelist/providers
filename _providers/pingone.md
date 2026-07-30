---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Pingone Agentic Access
  operation_count: 17
  slug: pingone-agentic-access
  summary_line: 17 operations · 11 acting
api_count: 7
apis:
- description: REST API for managing PingOne environments, users, populations, applications, identity providers, MFA, risk policies, and authentication flows. Authentication uses OAuth 2.0 access tokens obtained fro
  name: PingOne Platform API
  slug: platform-api
- description: 'REST API for the PingOne Advanced Identity Cloud tenant providing identity management, access management, and tenant operations. Supports two authentication methods - API key and secret for read-only '
  name: PingOne Advanced Identity Cloud API
  slug: advanced-identity-cloud-api
- description: Manage OIDC/SAML applications.
  name: PingOne Applications API
  slug: pingone-applications-api
- description: OAuth 2.0 token endpoints.
  name: PingOne Authentication API
  slug: pingone-authentication-api
- description: Manage PingOne environments.
  name: PingOne Environments API
  slug: pingone-environments-api
- description: Manage user populations inside an environment.
  name: PingOne Populations API
  slug: pingone-populations-api
- description: Manage end-user identities.
  name: PingOne Users API
  slug: pingone-users-api
artifact_total: 13
collections:
- collection_type: open
  name: PingOne Platform API
  slug: open-pingone
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pingone-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pingone-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pingone-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pingone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pingone-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pingidentity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ping-identity
- group: company
  title: ''
  type: Website
  url: https://www.pingidentity.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pingidentity.com/pingone/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.pingidentity.com/pingone/main/v1/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pingidentity.com/en/platform/pricing.html
- group: start
  title: ''
  type: Signup
  url: https://www.pingidentity.com/en/try-ping.html
- group: company
  title: ''
  type: Blog
  url: https://www.pingidentity.com/en/resources/blog.html
created: '2026-05-11'
description: PingOne is Ping Identity's cloud-based identity and access management platform providing authentication, authorization, single sign-on, MFA, identity verification, risk evaluation, and user lifecycle management for workforce and customer identities. The platform unifies Ping Identity capabilities into a multi-region cloud service across the US, EU, Canada, and Asia-Pacific. PingOne exposes a comprehensive REST Platform API secured with OAuth 2.0 access tokens issued by its authentication service.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pingone.png
layout: provider
modified: '2026-05-11'
name: PingOne
nav: Providers
network: true
overview: 'PingOne publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Platform API, Applications API, Authentication API, and 3 more. Tagged areas include Identity, Authentication, Authorization, Single Sign-On, and Multi-Factor Authentication.


  PingOne''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 30.6
  delta: -2.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 51.0
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pingone/refs/heads/main/screenshots/pingone-2026-06-20T191715.png
security:
- kind: authentication
  name: Pingone Authentication
  slug: pingone-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pingone Domain Security
  slug: pingone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pingone Vulnerability Disclosure
  slug: pingone-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Pingone Trust Center
  slug: pingone-trust-center
  summary_line: SOC 2, ISO 27001
slug: pingone
tags:
- Identity
- Authentication
- Authorization
- Single Sign-On
- Multi-Factor Authentication
- IAM
- CIAM
website: https://www.pingidentity.com
---
