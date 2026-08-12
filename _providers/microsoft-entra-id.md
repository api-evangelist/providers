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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Microsoft Entra Id Agentic Access
  operation_count: 23
  slug: microsoft-entra-id-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 6
apis:
- description: Microsoft Entra ID (formerly Azure AD) is a cloud-based identity and access management service for authenticating and authorizing users and applications with OAuth2, OIDC, and SAML support.
  name: Microsoft Entra ID
  slug: microsoft-entra-id
- description: Application registration management
  name: Microsoft Entra ID Applications API
  slug: microsoft-entra-id-applications-api
- description: Directory role management
  name: Microsoft Entra ID DirectoryRoles API
  slug: microsoft-entra-id-directoryroles-api
- description: Group management
  name: Microsoft Entra ID Groups API
  slug: microsoft-entra-id-groups-api
- description: Service principal management
  name: Microsoft Entra ID ServicePrincipals API
  slug: microsoft-entra-id-serviceprincipals-api
- description: User identity management
  name: Microsoft Entra ID Users API
  slug: microsoft-entra-id-users-api
artifact_total: 16
collections:
- collection_type: open
  name: Microsoft Entra ID (Microsoft Graph) REST API
  slug: open-microsoft-entra-id
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-entra-id-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-entra-id-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-entra-id-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-entra-id-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-entra-id-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-entra-id-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/entra/identity/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AzureAD
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/security/blog/product/microsoft-entra/feed/
created: '2026-03-25'
description: Microsoft Entra ID (formerly Azure AD) is a cloud-based identity and access management service for authenticating and authorizing users and applications with OAuth2, OIDC, and SAML support.
finops:
- name: Microsoft Entra Id Finops
  service_category: API
  slug: microsoft-entra-id-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-entra-id.png
layout: provider
modified: '2026-04-28'
name: Microsoft Entra ID
nav: Providers
network: true
overview: 'Microsoft Entra ID publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Applications API, DirectoryRoles API, Groups API, and 2 more. Tagged areas include Authentication and Identity Provider.


  Microsoft Entra ID''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Entra Id Plans Pricing
  plan_count: 3
  slug: microsoft-entra-id-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 5
  name: Microsoft Entra Id Rate Limits
  slug: microsoft-entra-id-rate-limits
scopes:
- name: Microsoft Entra Id Scopes
  scope_count: 6
  slug: microsoft-entra-id-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 29.3
  delta: -8.3
  facets:
    commercial_clarity: 23.7
    contract_quality: 55.3
    developer_ergonomics: 21.7
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-entra-id/refs/heads/main/screenshots/microsoft-entra-id-2026-06-20T185459.png
security:
- kind: authentication
  name: Microsoft Entra Id Authentication
  slug: microsoft-entra-id-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Entra Id Domain Security
  slug: microsoft-entra-id-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Entra Id Vulnerability Disclosure
  slug: microsoft-entra-id-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Entra Id Trust Center
  slug: microsoft-entra-id-trust-center
  summary_line: GDPR
slug: microsoft-entra-id
tags:
- Authentication
- Identity Provider
website: https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id
---
