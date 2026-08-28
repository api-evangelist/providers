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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: JOOR's production identity service, a Keycloak realm exposing standard OpenID Connect / OAuth 2.0 endpoints (authorize, token, userinfo, introspection, JWKS) used to authenticate access to the JOOR pl
  name: JOOR Identity (OpenID Connect)
  slug: joor-identity-openid-connect
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/joor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jooraccess.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/joor
- group: operate
  title: ''
  type: StatusPage
  url: https://status.joor.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/joor-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/joor-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/joor-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/joor-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/joor-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/joor-llms.txt
created: '2026-07-17'
description: JOOR is a New York-based SaaS company (founded 2010) operating a leading B2B wholesale fashion commerce platform and digital marketplace that connects fashion brands with retailers to run their wholesale business end to end. The platform digitizes wholesale buying with online linesheets, lookbooks, virtual showrooms, order management, and the JOOR Marketplace, alongside products such as JOOR Pay (wholesale payments), JOOR Passport (virtual trade shows), and Retail data/analytics. JOOR connects thousands of brands with hundreds of thousands of retail doors globally. Its production platform is fronted by a Kong API gateway and secured with Keycloak-based OpenID Connect authentication; API access is partner/integration-oriented rather than a self-serve public developer program. This profile was enriched from JOOR's live public surface (OIDC discovery, GitHub organization, and status page).
image: https://www.jooraccess.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Joor
nav: Providers
network: true
overview: 'Joor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Wholesale, Retail, and E-Commerce.


  Joor''s developer surface includes authentication and 9 more developer resources.'
random_paper: 1
scopes:
- name: Joor Scopes
  scope_count: 9
  slug: joor-scopes
  summary_line: 9 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 16.4
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 79.6
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 16.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/joor/refs/heads/main/screenshots/joor-2026-07-25T223239.png
security:
- kind: authentication
  name: Joor Authentication
  slug: joor-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Joor Domain Security
  slug: joor-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: joor
tags:
- Company
- Fashion
- Wholesale
- Retail
- E-Commerce
- B2B
- Marketplace
- Payments
website: https://www.jooraccess.com
---
