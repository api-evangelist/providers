---
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aifi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aifi.com/
- group: company
  title: ''
  type: About
  url: https://www.aifi.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.aifi.com/blog
- group: company
  title: ''
  type: Press
  url: https://www.aifi.com/press-coverage
- group: company
  title: ''
  type: Partners
  url: https://www.aifi.com/partners
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aifi.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://www.aifi.com/lets-talk
- group: other
  title: ''
  type: OpenSourcePolicy
  url: https://www.aifi.com/open-source
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aifi-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aifi-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aifi-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.aifi.com/realms/aifi/.well-known/openid-configuration
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aifi-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aifi-conformance.yml
coverage:
  checked: '2026-08-06'
  detail: AiFi markets a suite of OASIS retailer APIs, but docs.aifi.com sits behind an oauth2-proxy that 302s every single path — including /openapi.json and every /.well-known/ path — to an AiFi Keycloak login (realm `aifi`, client_id `docs-oidc-client`), and www.aifi.com carries no developer, docs or API page at all, so not one line of the API reference or contract is publicly readable.
  evidence:
  - status: 302
    url: https://docs.aifi.com/openapi.json
  - status: 302
    url: https://docs.aifi.com/
  - status: 404
    url: https://www.aifi.com/developers
  - status: 404
    url: https://www.aifi.com/openapi.json
  - status: 200
    url: https://auth.aifi.com/realms/aifi/.well-known/openid-configuration
  reason: partner-login
  state: gated
created: '2026-08-06'
description: AiFi is a spatial-intelligence platform that uses camera-only computer vision to understand human behavior in physical spaces. Founded in 2016 and headquartered in San Francisco, it powers autonomous checkout, frictionless identity and entry, real-time fraud prevention, historical journey analytics and an operational co-pilot across retail, stadiums and arenas, quick-service restaurants, travel hubs, healthcare, campuses and government border control. The platform needs no shelf sensors or RFID and tracks shoppers with anonymous skeletal keypoint detection rather than facial recognition by default. AiFi publishes a suite of retailer-facing OASIS APIs that bridge its platform to POS (NCR, Oracle, Square) and payment (Stripe, Adyen) systems, but the developer documentation is served only to authenticated accounts through an AiFi Keycloak single sign-on.
image: https://framerusercontent.com/assets/5f5E5VdygR6bvI2EpHrCRo6Euo.png
layout: provider
modified: '2026-08-06'
name: AiFi
nav: Providers
network: true
overview: 'AiFi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Computer-Vision, Retail, Autonomous Checkout, and Spatial Intelligence.


  AiFi''s developer surface includes engineering blog, authentication, and 13 more developer resources.'
random_paper: 10
scopes:
- name: Aifi Scopes
  scope_count: 10
  slug: aifi-scopes
  summary_line: 10 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: emerging
  composite: 16.4
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 16.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aifi/refs/heads/main/screenshots/aifi-2026-08-07T161053.png
security:
- kind: authentication
  name: Aifi Authentication
  slug: aifi-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Aifi Domain Security
  slug: aifi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aifi
tags:
- Company
- Computer-Vision
- Retail
- Autonomous Checkout
- Spatial Intelligence
- Artificial Intelligence
- Analytics
- Identity
- Fraud Prevention
- Point-of-Sale
website: https://www.aifi.com/
---
