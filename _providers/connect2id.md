---
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
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-17'
api_count: 14
apis:
- description: OAuth 2.0 / OpenID Connect authorization endpoint.
  name: Connect2id Server Authorization API
  slug: authorization
- description: OAuth 2.0 token endpoint.
  name: Connect2id Server Token API
  slug: token
- description: OpenID Connect UserInfo endpoint.
  name: Connect2id Server UserInfo API
  slug: userinfo
- description: OAuth 2.0 dynamic client registration and management.
  name: Connect2id Server Client Registration API
  slug: client-registration
- description: OAuth 2.0 token introspection (RFC 7662).
  name: Connect2id Server Token Introspection API
  slug: token-introspection
- description: OAuth 2.0 token revocation (RFC 7009).
  name: Connect2id Server Token Revocation API
  slug: token-revocation
- description: PAR endpoint (RFC 9126).
  name: Connect2id Server Pushed Authorization Requests API
  slug: par
- description: Client-Initiated Backchannel Authentication.
  name: Connect2id Server CIBA API
  slug: ciba
- description: OpenID Provider metadata.
  name: Connect2id Server Discovery API
  slug: discovery
- description: Public JSON Web Key set.
  name: Connect2id Server JWK Set API
  slug: jwk-set
- description: OpenID Connect logout / end session.
  name: Connect2id Server Logout API
  slug: logout
- description: OpenID Connect session management iframe.
  name: Connect2id Server Check Session API
  slug: check-session
- description: OpenID Federation client registration.
  name: Connect2id Server Federation Client Registration API
  slug: federation-client-registration
- description: OpenID Federation entity configuration.
  name: Connect2id Server Federation Entity Configuration API
  slug: federation-entity-configuration
artifact_total: 16
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connect2id/refs/heads/main/well-known/connect2id-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/connect2id-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connect2id/refs/heads/main/hosts/connect2id-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connect2id-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connect2id/refs/heads/main/security/connect2id-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connect2id-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://connect2id.com
- group: docs
  title: ''
  type: Documentation
  url: https://connect2id.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://connect2id.com/products/server/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://connect2id.com/products/server/docs/quick-start
- group: operate
  title: ''
  type: ChangeLog
  url: https://connect2id.com/products/server/docs/release-notes
- group: company
  title: ''
  type: Blog
  url: https://connect2id.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://connect2id.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://connect2id.com/privacy-statement
- group: operate
  title: ''
  type: Support
  url: https://connect2id.com/products/server/license-and-support
- group: operate
  title: ''
  type: Contact
  url: https://connect2id.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/connect2id
- group: other
  title: ''
  type: OpenIDConnect
  url: https://demo.c2id.com/.well-known/openid-configuration
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connect2id/refs/heads/main/authentication/connect2id-authentication.yml
  title: ''
  type: Authentication
  url: authentication/connect2id-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: https://demo.c2id.com
- group: build
  title: ''
  type: SDKs
  url: https://connect2id.com/products/nimbus-oauth-openid-connect-sdk
coverage:
  detail: Connect2id documents the Connect2id server's web APIs at connect2id.com/products/server/docs/api and serves OpenID discovery metadata on its demo issuer, but publishes no OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://connect2id.com/products/server/docs/api
  - status: 200
    url: https://demo.c2id.com/.well-known/openid-configuration
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Connect2id is the maker of the Connect2id server, an OpenID Connect and OAuth 2.0 authorization server, and the open-source Nimbus OAuth 2.0 / OpenID Connect SDK and Nimbus JOSE+JWT libraries for Java.
image: https://connect2id.com/img/asset/c29jaWFsX2ltYWdlcy9ob21lLW9nLTE3MjAxOTIwNzgucG5n/home-og-1720192078.png?w=1200&h=630&fit=crop&s=1978b01022b2e3b6d51085899425cfce
layout: provider
modified: '2026-10-13'
name: Connect2id
nav: Providers
network: true
overview: 'Connect2id is listed with 14 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpenID Connect, Authentication, and Identity.


  Connect2id''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, authentication, and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 53.6
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Connect2Id Authentication
  slug: connect2id-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Connect2Id Domain Security
  slug: connect2id-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: connect2id
tags:
- Company
- OpenID Connect
- Authentication
- Identity
website: https://connect2id.com
---
