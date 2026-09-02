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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Oidc Agentic Access
  operation_count: 7
  slug: oidc-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- description: Endpoints for authenticating end-users and obtaining authorization grants.
  name: OIDC Authentication API
  slug: oidc-authentication-api
- description: OpenID Connect Discovery endpoints for provider metadata.
  name: OIDC Discovery API
  slug: oidc-discovery-api
- description: JSON Web Key Set endpoint for token signature verification.
  name: OIDC JWKS API
  slug: oidc-jwks-api
- description: Session management endpoints including logout.
  name: OIDC Session API
  slug: oidc-session-api
- description: Token endpoint for exchanging authorization codes for tokens.
  name: OIDC Token API
  slug: oidc-token-api
- description: Endpoint for retrieving claims about the authenticated end-user.
  name: OIDC UserInfo API
  slug: oidc-userinfo-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenID Connect Authentication API
  slug: open-oidc-authentication-api
- collection_type: open
  name: OpenID Connect Authentication Discovery API
  slug: open-oidc-discovery-api
- collection_type: open
  name: OpenID Connect Authentication JWKS API
  slug: open-oidc-jwks-api
- collection_type: open
  name: OpenID Connect Authentication Session API
  slug: open-oidc-session-api
- collection_type: open
  name: OpenID Connect Authentication Token API
  slug: open-oidc-token-api
- collection_type: open
  name: OpenID Connect Authentication UserInfo API
  slug: open-oidc-userinfo-api
- collection_type: open
  name: OpenID Connect API
  slug: open-oidc
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oidc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oidc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oidc-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://openid.net/
- group: docs
  title: ''
  type: Documentation
  url: https://openid.net/developers/specs/
- group: docs
  title: ''
  type: Reference
  url: https://openid.net/specs/openid-connect-core-1_0.html
- group: company
  title: ''
  type: Blog
  url: https://openid.net/feed/
created: '2025-01-01'
description: OpenID Connect (OIDC) is an identity layer built on top of OAuth 2.0 that enables clients to verify the identity of end-users based on authentication performed by an authorization server. It provides a standardized way to obtain basic profile information about users through RESTful endpoints including discovery, authorization, token, userinfo, and JWKS.
finops:
- name: Oidc Finops
  service_category: API
  slug: oidc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oidc.png
json_schemas:
- name: OpenID Connect Discovery Document
  property_count: 34
  slug: oidc-discovery
- name: OpenID Connect ID Token Claims
  property_count: 32
  slug: oidc-id-token
- name: OpenID Connect UserInfo Response
  property_count: 20
  slug: oidc-userinfo-response
layout: provider
modified: '2026-05-19'
name: OIDC
nav: Providers
network: true
overview: 'OIDC publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Discovery API, JWKS API, and 3 more. Tagged areas include Authentication, Identity, JWT, OIDC, and OpenID Connect.


  The OIDC catalog on APIs.io includes 1 Spectral governance ruleset.


  OIDC''s developer surface includes authentication, documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Oidc Plans Pricing
  plan_count: 3
  slug: oidc-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Oidc Rate Limits
  slug: oidc-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OIDC API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: oidc-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 70.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 49.5
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oidc/refs/heads/main/screenshots/oidc-2026-06-20T190645.png
security:
- kind: authentication
  name: Oidc Authentication
  slug: oidc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Oidc Domain Security
  slug: oidc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oidc
tags:
- Authentication
- Identity
- JWT
- OIDC
- OpenID Connect
website: https://openid.net/
---
