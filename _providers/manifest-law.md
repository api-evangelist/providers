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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Programmatic surface behind ManifestOS, gated by the Manifest Law OAuth 2.0 / OpenID Connect authorization server (issuer https://app.manifestlaw.com/api/auth, `api` scope).
  name: ManifestOS API
  slug: manifestos-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/manifest-law-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/manifest-law-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/manifest-law-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/manifest-law-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manifest-law-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/manifest-law-llms.txt
- group: start
  title: ''
  type: Login
  url: https://app.manifestlaw.com
- group: company
  title: ''
  type: Website
  url: https://manifestlaw.com
created: '2026-07-17'
description: Manifest Law operates ManifestOS, a communication and case management platform for the legal industry, and is backed by Menlo Ventures. The platform exposes a standards-based OAuth 2.0 / OpenID Connect authorization server at app.manifestlaw.com, with an `api` scope for programmatic access and dynamic OAuth client management (`oauth_clients:manage`). This profile was enriched by the API Evangelist pipeline from Manifest Law's public discovery documents; no OpenAPI specification was published at the time of enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/manifest-law.png
layout: provider
modified: '2026-07-20'
name: Manifest Law
nav: Providers
network: true
overview: 'Manifest Law publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal, Legal Tech, Case Management, and Communication.


  Manifest Law''s developer surface includes authentication and 7 more developer resources.'
random_paper: 24
scopes:
- name: Manifest Law Scopes
  scope_count: 7
  slug: manifest-law-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: emerging
  composite: 13.9
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 13.9
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/manifest-law/refs/heads/main/screenshots/manifest-law-2026-07-25T230049.png
security:
- kind: authentication
  name: Manifest Law Authentication
  slug: manifest-law-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Manifest Law Domain Security
  slug: manifest-law-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: manifest-law
tags:
- Company
- Legal
- Legal Tech
- Case Management
- Communication
- OAuth
- OpenID Connect
website: https://manifestlaw.com
---
