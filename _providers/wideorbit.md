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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Certified-partner API gateway for WideOrbit.io providing real-time, object-level interaction with WideOrbit Traffic, Network, and Omni systems. Access is restricted to authorized, WideOrbit-certified '
  name: WideOrbit.io API Gateway
  slug: wideorbitio-api-gateway
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wideorbit-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wideorbit-conformance.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wideorbit-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.wideorbit.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.wideorbit.com/io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wideorbit.com/io/
- group: start
  title: ''
  type: SignUp
  url: https://www.wocentral.com/
- group: start
  title: ''
  type: Login
  url: https://www.wocentral.com/
- group: operate
  title: ''
  type: Support
  url: https://www.wideorbit.com/product-support/
- group: company
  title: ''
  type: Blog
  url: https://www.wideorbit.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wideorbit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wideorbit.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wideorbit.com/privacy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wideorbit-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wideorbit-authentication.yml
created: '2026-07-17'
description: WideOrbit is a premium ad management platform for the media industry, giving broadcast television, cable and broadcast networks, radio, and digital publishers a single system to sell, traffic, bill, and reconcile advertising across linear, digital, and cross-media campaigns. Its products span WO Traffic, WO Network, WO Omni, WO Media Sales, WO Programmatic, and the WO Aurora radio automation suite, all reached through the WO Central workspace. For integration partners, WideOrbit.io exposes a certified developer program and an OIDC-secured API gateway that offers real-time, object-level access to Traffic, Network, and Omni data, complemented by the WO Data Bridge cloud data warehouse. WideOrbit manages roughly $33 billion in annual ad revenue for 6,450+ stations and networks. It was surfaced as a portfolio company of Mayfield and enriched in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wideorbit.png
layout: provider
modified: '2026-07-21'
name: WideOrbit
nav: Providers
network: true
overview: 'WideOrbit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Media, and Broadcasting.


  WideOrbit''s developer surface includes documentation, signup flow, support, engineering blog, authentication, and 10 more developer resources.'
random_paper: 21
scopes:
- name: Wideorbit Scopes
  scope_count: 0
  slug: wideorbit-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.9
  delta: 0.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 79.6
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 23.7
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Wideorbit Authentication
  slug: wideorbit-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Wideorbit Domain Security
  slug: wideorbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wideorbit
tags:
- Company
- Advertising
- AdTech
- Media
- Broadcasting
- Radio
- Television
- Ad Management
- Programmatic
- Media Sales
website: https://www.wideorbit.com
---
