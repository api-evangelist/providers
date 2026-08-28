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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meow-wolf-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meow-wolf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meowwolf.com/
- group: company
  title: ''
  type: Blog
  url: https://meowwolf.com/blog
- group: operate
  title: ''
  type: Support
  url: https://meowwolf.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://meowwolf.com/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MeowWolf
- group: commercial
  title: ''
  type: Pricing
  url: https://tickets.meowwolf.com/
- group: start
  title: ''
  type: SignUp
  url: https://meowwolf.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://meowwolf.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://meowwolf.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meow-wolf-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meow-wolf-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/meow-wolf-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/meow-wolf-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/meow-wolf-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/meow-wolf-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/meow-wolf-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: security/meow-wolf-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meow-wolf-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/meow-wolf-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/meow-wolf-scopes.yml
coverage:
  checked: '2026-08-25'
  detail: Meow Wolf is a location-based immersive-art attraction operator whose software ships only as end-user products (ticketing, a customer portal, a mobile app, a WooCommerce shop); api.meowwolf.com is a Postman Hosted Site custom domain that serves Postman's own "Not found" page with nothing published on it, and the only machine-readable contract anywhere on the estate is an undocumented Auth0 OpenID Connect discovery document at auth.meowwolf.com used for consumer sign-in.
  evidence:
  - status: 404
    url: https://api.meowwolf.com/
  - status: 200
    url: https://auth.meowwolf.com/.well-known/openid-configuration
  - status: 200
    url: https://meowwolf.com/llms.txt
  - status: 404
    url: https://meowwolf.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'Meow Wolf is an arts-production and entertainment company founded in Santa Fe, New Mexico that designs and operates large-scale immersive, interactive art exhibitions — House of Eternal Return (Santa Fe), Omega Mart (Las Vegas), Convergence Station (Denver), The Real Unreal (Grapevine, TX) and Radio Tave (Houston) — with further locations announced for Los Angeles and New York City. Around the exhibitions it runs a consumer ticketing platform, an online merchandise shop, a mobile companion app for iOS and Android, an arts foundation and an education program. It is a visitor-experience business rather than a software vendor: it operates no public developer program and publishes no API reference, OpenAPI, AsyncAPI, GraphQL SDL or Postman collection. Its public engineering output is an open-source GitHub organization of show-control, beacon and AMQP messaging tooling built for its own installations. The one genuine machine-readable contract on the estate is undocumented: auth.meowwolf.com,
  an Auth0 custom-domain tenant, serves a complete anonymous OpenID Connect / RFC 8414 discovery document and a live JWKS for consumer sign-in to the ticketing and portal apps.'
image: https://webassets.meowwolf.com/cdn.prod/5dad7a19f43e6f31a9e92718/5f80a2cc5d23e71099517470_MeowWolfTreehouse.jpg
layout: provider
modified: '2026-08-25'
name: Meow Wolf
nav: Providers
network: true
overview: 'Meow Wolf is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Art, Entertainment, Immersive Experiences, and Events.


  Meow Wolf''s developer surface includes engineering blog, support, pricing, signup flow, authentication, and 17 more developer resources.'
plans:
- name: Meow Wolf Plans Pricing
  plan_count: 0
  slug: meow-wolf-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Meow Wolf Rate Limits
  slug: meow-wolf-rate-limits
scopes:
- name: Meow Wolf Scopes
  scope_count: 0
  slug: meow-wolf-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.5
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 13.2
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Meow Wolf Authentication
  slug: meow-wolf-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Meow Wolf Domain Security
  slug: meow-wolf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Meow Wolf Vulnerability Disclosure
  slug: meow-wolf-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: meow-wolf
tags:
- Company
- Art
- Entertainment
- Immersive Experiences
- Events
- Ticketing
- Museums
- Tourism
- Retail
- Mobile Apps
website: https://meowwolf.com/
---
