---
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/budget-direct-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/budget-direct-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.budgetdirect.com.au/
- group: company
  title: ''
  type: About
  url: https://www.budgetdirect.com.au/about-us.html
- group: operate
  title: ''
  type: Contact
  url: https://www.budgetdirect.com.au/contact-us.html
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/budget-direct
- group: operate
  title: ''
  type: PressReleases
  url: https://www.budgetdirect.com.au/about-us/media-releases.html
- group: build
  title: ''
  type: CodeOfConduct
  url: https://www.budgetdirect.com.au/about-us/code-of-practice.html
- group: other
  title: ''
  type: ParentOrganization
  url: https://www.autogeneral.com.au/
- group: company
  title: ''
  type: Partners
  url: https://www.autogeneral.com.au/partners/
- group: operate
  title: ''
  type: Support
  url: https://www.budgetdirect.com.au/contact-us.html
- group: start
  title: ''
  type: Login
  url: https://www.budgetdirect.com.au/existing-customers/policy-manager.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.budgetdirect.com.au/start/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.budgetdirect.com.au/start/privacy-policy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AutoGeneral
- group: auth
  title: ''
  type: Compliance
  url: https://www.budgetdirect.com.au/about-us/code-of-practice.html
- group: auth
  title: ''
  type: Security
  url: https://www.autogeneral.com.au/docs/ag-external-vulnerability-disclosure-policy.pdf
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/budget-direct-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/budget-direct-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/budget-direct-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/budget-direct-llms.txt
created: '2026-07-25'
description: 'Budget Direct is one of Australia''s largest direct-to-consumer general insurance brands, operated from Toowong, Queensland by Auto & General Services Pty Ltd (ABN 61 003 617 909) with general insurance products issued by Auto & General Insurance Company Limited (ABN 42 111 586 353), an APRA-authorised insurer. The brand sells car, home and contents, motorcycle, travel, pet and life insurance plus roadside assistance direct to Australian consumers online and by phone, with life cover underwritten by NobleOak Life Limited and travel cover by Zurich Australian Insurance Limited. Its parent, Auto & General, also white-labels personal lines through distribution partners including Qantas, Coles Insurance, ING and Oceania Insurance. Budget Direct publishes NO public self-serve developer portal and NO public API. Every candidate developer host was probed on 2026-07-25 — developer., developers., docs., api., partners., portal., broker., sandbox. and apis.budgetdirect.com.au all fail
  DNS resolution, and /developers, /developer, /api, /partners and /integrations all return HTTP 404 — while the full 738-URL sitemap contains no developer, API or integration page. Quote, bind, issue and claim (FNOL) exist only as consumer web journeys and a logged-in existing-customer self-service area; there is no documented machine surface for any of them. The parent domain does carry an Apigee gateway hostname (api.autogeneral.com.au, CNAME to autogeneral-prod.apigee.net, preconnect-hinted by the consumer site) but it is first-party and undocumented, with no developer portal, no OpenAPI, no ACORD/AL3 reference anywhere on either site, and partner integration handled as private commercial arrangements through Auto & General. This record is an honest stub: an APRA-regulated Australian carrier with no public API surface. The only machine-readable documents it serves are an RFC 9116 /.well-known/security.txt pointing at Auto & General''s published external vulnerability disclosure policy,
  and the Apple and Android app-association files for its Fuel Discounts mobile app.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Budget Direct
nav: Providers
network: true
overview: 'Budget Direct is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Property and Casualty, Direct to Consumer Insurance, and Motor Insurance.


  Budget Direct''s developer surface includes support and 20 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 25.2
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 25.2
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/budget-direct/refs/heads/main/screenshots/budget-direct-2026-07-25T204030.png
security:
- kind: domain-security
  name: Budget Direct Domain Security
  slug: budget-direct-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Budget Direct Vulnerability Disclosure
  slug: budget-direct-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: budget-direct
tags:
- Insurance
- Australia
- Property and Casualty
- Direct to Consumer Insurance
- Motor Insurance
- Home Insurance
- Travel Insurance
- Life Insurance
- Underwriting
- Claims
- Carrier
- No Public API
website: https://www.budgetdirect.com.au/
---
