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
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The OpenID Connect / OAuth 2.0 authorization server Gymshark operates on its own domain at auth.gymshark.com (an Auth0 tenant) for Gymshark customer accounts across the web storefronts and the Gymshar
  name: Gymshark Identity (OpenID Connect)
  slug: gymshark-identity-openid-connect
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.gymshark.com/
- group: company
  title: ''
  type: Blog
  url: https://www.gymshark.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.gymshark.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.gymshark.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gymshark.com/pages/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gymshark.com/pages/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.gymshark.com/pages/cookie-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.gymshark.com/account/register
- group: start
  title: ''
  type: Login
  url: https://www.gymshark.com/account/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gymshark
- group: company
  title: ''
  type: Careers
  url: https://careers.gymshark.com/
- group: company
  title: ''
  type: About
  url: https://www.gymshark.com/pages/about-us
- group: other
  title: ''
  type: Sustainability
  url: https://www.gymshark.com/pages/sustainability
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/gymshark_stock/
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.gymshark.com/.well-known/openid-configuration
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gymshark-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gymshark-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gymshark-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gymshark-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gymshark-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/gymshark-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gymshark-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gymshark-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/gymshark
created: '2026-08-04'
description: Gymshark is a British fitness apparel and accessories brand founded in 2012 in Birmingham, England, selling gym and workout clothing direct to consumers worldwide through gymshark.com, a set of regional storefronts (uk., eu., row., de., fr., ca., au. and others) and its Gymshark Shop and Gymshark Training mobile apps. The storefront runs on Shopify behind a headless Next.js/OpenNext front end deployed on AWS, and customer identity is handled by an Auth0 tenant Gymshark operates on its own domain at auth.gymshark.com. Gymshark publishes no public developer portal, no developer documentation and no public product API; the only publicly discoverable machine-readable contract on its own hosts is the OpenID Connect / OAuth 2.0 authorization-server metadata served from auth.gymshark.com. Its engineering team does publish open-source Go, JavaScript and Swift libraries under the github.com/gymshark organization, and it runs a public vulnerability disclosure program on HackerOne.
image: https://cdn.shopify.com/s/files/1/0098/8822/files/gymshark_social_banner_1200x1200.jpg?v=1549554764
layout: provider
modified: '2026-08-04'
name: Gymshark
nav: Providers
network: true
overview: 'Gymshark publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Apparel, and Fitness.


  Gymshark''s developer surface includes engineering blog, support, signup flow, authentication, and 20 more developer resources.'
random_paper: 9
scopes:
- name: Gymshark Scopes
  scope_count: 14
  slug: gymshark-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/implicit/deviceCode
score:
  band: emerging
  composite: 20.3
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 20.3
  provenance:
    conformance: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gymshark/refs/heads/main/screenshots/gymshark-2026-08-07T165908.png
security:
- kind: authentication
  name: Gymshark Authentication
  slug: gymshark-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Gymshark Domain Security
  slug: gymshark-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gymshark Vulnerability Disclosure
  slug: gymshark-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: gymshark
tags:
- Company
- Retail
- E-Commerce
- Apparel
- Fitness
- Consumer
- Direct to Consumer
- Identity
- OpenID Connect
website: https://www.gymshark.com/
---
