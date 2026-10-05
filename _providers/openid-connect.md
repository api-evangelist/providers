---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-04'
api_count: 6
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
  name: OIDC User Info API
  slug: oidc-user-info-api
artifact_total: 7
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openid-connect/refs/heads/main/capabilities/openid-connect-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/openid-connect-capability-edges.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openid-connect/refs/heads/main/security/openid-connect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openid-connect-domain-security.yml
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
- group: agent
  title: ''
  type: LlmsText
  url: https://openid.net/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://openid.net/feed/
created: '2025-01-01'
description: OpenID Connect (OIDC) is an identity authentication protocol that is an extension of OAuth 2.0. It enables clients to verify the identity of end-users and obtain basic profile information in a secure, standardized way using JSON Web Tokens (JWT).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openid-connect.png
layout: provider
modified: '2026-04-28'
name: OpenID Connect
nav: Providers
network: true
overview: 'OpenID Connect publishes 6 APIs on the [APIs.io](https://apis.io/) network, including OIDC Authentication API, OIDC Discovery API, OIDC JWKS API, and 3 more. Tagged areas include Authentication, Identity, JWT, and OpenID Connect.


  OpenID Connect''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.8
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 19.0
    discoverability: 60.7
    operational_transparency: 0.0
  previous_composite: 8.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/openid-connect/refs/heads/main/screenshots/openid-connect-2026-06-20T191005.png
security:
- kind: domain-security
  name: Openid Connect Domain Security
  slug: openid-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openid-connect
tags:
- Authentication
- Identity
- JWT
- OpenID Connect
website: https://openid.net/
---
