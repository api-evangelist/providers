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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/honey-insurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.honeyinsurance.com/
- group: company
  title: ''
  type: About
  url: https://www.honeyinsurance.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.honeyinsurance.com/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://www.honeyinsurance.com/media-centre/newsroom/
- group: operate
  title: ''
  type: Support
  url: https://www.honeyinsurance.com/honey-help/
- group: operate
  title: ''
  type: FAQ
  url: https://www.honeyinsurance.com/faq/
- group: design
  title: ''
  type: Vocabulary
  url: https://www.honeyinsurance.com/glossary/
- group: start
  title: ''
  type: Login
  url: https://www.honeyinsurance.com/my-account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.honeyinsurance.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.honeyinsurance.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://www.honeyinsurance.com/get-a-quote/start
- group: company
  title: ''
  type: Careers
  url: https://www.honeyinsurance.com/join-the-team/
- group: other
  title: ''
  type: BrandKit
  url: https://www.honeyinsurance.com/media-centre/brand-assets/
- group: company
  title: ''
  type: Press
  url: https://www.honeyinsurance.com/media-centre/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/honey-insurance-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.honeyinsurance.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: Authentication
  url: authentication/honey-insurance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/honey-insurance-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/honey-insurance-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/honey-insurance-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/honey-insurance-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/honey-insurance-llms.txt
created: '2026-07-25'
description: 'Honey Insurance is an Australian direct-to-consumer insurtech selling smart home, contents, renters and landlord insurance, founded by Richard Joffe and headquartered in Sydney. Honey Insurance Pty Ltd (ABN 52 643 672 628, AFSL 528244) distributes and administers the policies, which are underwritten by RACQ Insurance Limited (ABN 50 009 704 152, AFSL 233082), an APRA-authorised general insurer. Its differentiator is a bundle of free smart-home sensors supplied at policy inception in exchange for a recurring premium discount, a three-minute online quote-and-bind funnel, and a heavy prevention rather than indemnity pitch. It sells personal lines only and distributes through its own website plus embedded partnerships with mortgage aggregators, home builders and real-estate groups (Finsure, Metricon, McGrath, BGC, Specialist Finance Group, Bank of Queensland, AGL, RACQ). Its API posture is closed: Honey publishes no public developer portal, no API reference, no OpenAPI or Swagger
  definition, no Postman collection, no GraphQL surface and no webhook or event catalogue. Probes of developer, developers, docs, /developers, /api, /developer, /partners and /integrations all return NXDOMAIN or HTTP 404, and the sitemap contains no developer, API or partner-portal page at all. A real backend host exists at api.honeyinsurance.com, but it is a private AWS API Gateway that answers every path with HTTP 403 {"message":"Forbidden"}; it serves Honey''s own quote funnel and account app and is not documented for third parties. The only publicly reachable standards-based surface is an Auth0 custom-domain tenant at auth.honeyinsurance.com serving anonymous OpenID Connect discovery for consumer account sign-in — not developer API credentials. Quote, bind, issue and FNOL all exist only as consumer web and telephone journeys. No ACORD, AL3, ACORD XML or NGDS reference appears anywhere on the site, which is consistent with an Australian personal-lines carrier operating outside the ACORD
  agency-download world and with a home market where the Consumer Data Right was designated for general insurance and then deferred, leaving no forcing function for open insurance APIs.'
image: https://www.honeyinsurance.com/images/honey-banner.png
layout: provider
modified: '2026-07-25'
name: Honey Insurance
nav: Providers
network: true
overview: 'Honey Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Insurtech, Home Insurance, and Property and Casualty.


  Honey Insurance''s developer surface includes engineering blog, support, FAQ, signup flow, authentication, and 18 more developer resources.'
random_paper: 70
scopes:
- name: Honey Insurance Scopes
  scope_count: 14
  slug: honey-insurance-scopes
  summary_line: 14 scopes · authorizationCode/implicit/clientCredentials/deviceCode
score:
  band: emerging
  composite: 25.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 13.5
    operational_transparency: 0.0
  previous_composite: 25.5
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/honey-insurance/refs/heads/main/screenshots/honey-insurance-2026-07-25T221358.png
security:
- kind: authentication
  name: Honey Insurance Authentication
  slug: honey-insurance-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Honey Insurance Domain Security
  slug: honey-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: honey-insurance
tags:
- Insurance
- Australia
- Insurtech
- Home Insurance
- Property and Casualty
- Personal Lines
- Direct to Consumer
- Embedded Insurance
- Smart Home
- Claims
- Underwriting
website: https://www.honeyinsurance.com/
---
