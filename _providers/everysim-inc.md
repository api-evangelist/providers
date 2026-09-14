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
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everysim-inc-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/everysim-inc-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/everysim-inc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/everysim-inc-scopes.yml
- group: start
  title: ''
  type: Login
  url: https://auth.everysim.io/realms/everysim/protocol/openid-connect/auth
- group: company
  title: ''
  type: Website
  url: https://everysim.io
created: '2026-07-17'
description: EverySim Inc. (everysim.io) is a 500 Global-backed company that operates a private, authentication-gated web application. Every public path on everysim.io redirects unauthenticated visitors into a Keycloak-based OpenID Connect / OAuth 2.0 single-sign-on flow (realm "everysim", client "everysim-web", authorization-code with PKCE). As of this profile no public developer API, documentation, SDK, CLI, or developer portal surface was found; the only publicly reachable machine-readable endpoint is the realm's OpenID Connect discovery document on auth.everysim.io. This entry captures the provider's verifiable identity, authentication model, and domain-security posture pending a public API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/everysim-inc.png
layout: provider
modified: '2026-07-19'
name: EverySim Inc.
nav: Providers
network: true
overview: 'EverySim Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Authentication, OpenID Connect, Single Sign-On, and Identity.


  EverySim Inc.''s developer surface includes authentication and 5 more developer resources.'
random_paper: 4
scopes:
- name: Everysim Inc Scopes
  scope_count: 13
  slug: everysim-inc-scopes
  summary_line: 13 scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/everysim-inc/refs/heads/main/screenshots/everysim-inc-2026-07-25T213843.png
security:
- kind: authentication
  name: Everysim Inc Authentication
  slug: everysim-inc-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Everysim Inc Domain Security
  slug: everysim-inc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: everysim-inc
tags:
- Company
- Authentication
- OpenID Connect
- Single Sign-On
- Identity
website: https://everysim.io
---
