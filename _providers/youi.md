---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
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
  score: 2.6
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/youi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/youi-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.youi.com.au/about-us/security-vulnerability-disclosure-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/youi-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/youi-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/youi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.youi.com.au/documents/code-of-practice
- group: build
  title: ''
  type: Packages
  url: packages/youi-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/youi-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.youi.com.au/
- group: company
  title: ''
  type: About
  url: https://www.youi.com.au/about-us
- group: start
  title: ''
  type: CustomerPortal
  url: https://portal.youi.com.au/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.youi.com.au/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.youi.com.au/about-us/security-vulnerability-disclosure-policy
- group: operate
  title: ''
  type: Support
  url: https://www.youi.com.au/contact
- group: company
  title: ''
  type: Blog
  url: https://www.youi.com.au/you-connect
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.youi.com.au/documents/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.youi.com.au/documents/terms-of-use
- group: start
  title: ''
  type: Login
  url: https://secure.youi.com.au/Authentication/PolicyLogin.aspx
- group: company
  title: ''
  type: Careers
  url: https://www.youi.com.au/about-us/careers
created: '2026-07-25'
description: Youi is an Australian general insurance carrier headquartered at Sippy Downs on the Queensland Sunshine Coast, authorised by APRA and operating under AFSL 316511 (ABN 79 123 074 733). It is a wholly owned subsidiary of Youi Holdings Pty Ltd, part of OUTsurance International Holdings, with the South African-listed OUTsurance Group as ultimate holding company. Youi writes personal and small-business property and casualty lines direct to consumers - car, NSW CTP Green Slip, SA CTP, motorcycle, caravan and trailer, watercraft, home building and contents, and small business cover including public liability - and is a member of the Insurance Council of Australia and a signatory to the General Insurance Code of Practice. Its positioning is direct-to-consumer telephone and online underwriting rather than broker distribution. On API posture the honest finding is that Youi publishes no public API surface at all. Probing on 2026-07-25 found no developer portal (the developer., developers.,
  docs. and api. subdomains do not resolve, and /developers, /api, /developer, /partners and /integrations all return HTTP 404), no downloadable OpenAPI or Swagger, no public Postman collection, no GraphQL, and no webhook or event catalog. The only integration-adjacent hosts are the customer self-service policy portal at portal.youi.com.au (HTTP 200, robots noindex, an Angular single-page app behind a login) and its private first-party backend portalapi.youi.com.au (HTTP 404 at root, serving no swagger or openapi document). No ACORD, AL3, ACORD XML, NGDS or IVANS reference was found anywhere on the public site. Australia's Consumer Data Right, which opened banking and energy, was designated for general insurance and then deferred, so no regulatory forcing function exists, and Youi's direct-to-consumer model gives it no broker or agency-management integration seam either. Recorded as partner-gated and customer-login-gated only, with no public self-serve API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Youi
nav: Providers
network: true
overview: 'Youi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Property and Casualty, General Insurance, and Motor Insurance.


  Youi''s developer surface includes support, engineering blog, and 18 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 23.0
  delta: -0.3
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 23.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Youi Domain Security
  slug: youi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Youi Vulnerability Disclosure
  slug: youi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: youi
tags:
- Insurance
- Australia
- Property and Casualty
- General Insurance
- Motor Insurance
- Home Insurance
- Business Insurance
- Compulsory Third Party
- Carrier
- Direct to Consumer
- No Public API
website: https://www.youi.com.au/
---
