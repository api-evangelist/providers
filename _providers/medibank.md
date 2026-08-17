---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medibank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.medibank.com.au/
- group: company
  title: ''
  type: Blog
  url: https://www.medibank.com.au/livebetter/newsroom/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/medibank
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Medibank
- group: docs
  title: ''
  type: Documentation
  url: https://www.medibank.com.au/providers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.medibank.com.au/providers/claims/
- group: docs
  title: ''
  type: Documentation
  url: https://www.medibank.com.au/providers/medical/mppa/
- group: docs
  title: ''
  type: Documentation
  url: https://www.medibank.com.au/providers/hospital/
- group: docs
  title: ''
  type: Documentation
  url: https://www.medibank.com.au/providers/information-for-simplified-billing-agents/
- group: start
  title: ''
  type: Portal
  url: https://providers.medibank.com.au/
- group: operate
  title: ''
  type: Support
  url: https://www.medibank.com.au/help/
- group: start
  title: ''
  type: Login
  url: https://members.medibank.com.au/
- group: start
  title: ''
  type: SignUp
  url: https://www.medibank.com.au/health-insurance/join/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/medibank-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/medibank-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medibank-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medibank.com.au/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.medibank.com.au/legal-information/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.medibank.com.au/help/security-and-privacy/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.medibank.com.au/about/investor-centre/
created: '2026-07-25'
description: 'Medibank Private Limited (ASX: MPL) is Australia''s largest private health insurer, headquartered in Melbourne and operating two retail brands, Medibank and ahm, alongside the Amplar Health services arm. Founded in 1976 as a government-owned fund and privatised through an ASX listing in 2014, it underwrites hospital, extras and ambulance cover for Australian residents, Overseas Student Health Cover and Overseas Visitors Health Cover, and distributes travel, pet, life, income protection and accident cover (Recover Boost) alongside its core private health insurance book. Its home market is Australia, where private health insurance is a separately regulated market supervised by APRA and the Private Health Insurance Ombudsman, and where the Consumer Data Right that opened banking and energy was designated for general insurance and then deferred — so there is no open insurance obligation and no CDR seam reaching a health fund like Medibank. Medibank''s API posture is fully partner-gated
  and there is no public API. No developer portal exists on any conventional host: developer, developers, docs and apis subdomains of medibank.com.au do not resolve in DNS, api.medibank.com.au resolves but does not accept public TCP connections on port 443, and /developers, /api, /developer, /partners and /integrations all return HTTP 404 on www.medibank.com.au, whose 1,364-URL sitemap contains no developer or API page at all. The only first-party integration surfaces are login walls and email-gated onboarding: providers.medibank.com.au is a React single-page "Medibank - Provider Self Service" application (Provider Central, ESP) that returns its shell for every path, portal.medibank.com.au is a Palo Alto GlobalProtect corporate VPN, and the HCP Portal for Hospital Casemix Protocol submissions is granted only by emailing Medibank''s HCP team. The real machine-to-machine claiming rails are third-party and government-operated rather than Medibank-published: ECLIPSE, the Services Australia in-patient
  online claiming system, carries hospital claims and 25 percent Fund Gap medical claims under claim type "MB" and serves Online Eligibility Check with Presenting Illness codes, with ECFWeb and THELMA as alternative eligibility channels and HICAPS and iSOFT terminals handling ancillary claiming. No ACORD reference of any kind appears on Medibank''s public estate, which is the expected result — Australian private health insurance runs on ECLIPSE, HCP and the MBS rather than on ACORD AL3 or ACORD XML. No OpenAPI or Swagger definition, no Postman collection, no GraphQL or gRPC surface, no webhook or event catalog, and no documented authentication scheme could be confirmed anywhere on Medibank''s public web estate as of 2026-07-25, and none of the four insurance API verbs — quote, bind, issue or FNOL — is exposed to unauthenticated developers.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Medibank
nav: Providers
network: true
overview: 'Medibank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Health Insurance, Private Health Insurance, and Life and Health.


  Medibank''s developer surface includes engineering blog, documentation, developer portal, support, signup flow, and 16 more developer resources.'
random_paper: 82
score:
  band: emerging
  composite: 21.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 57.4
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 21.1
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medibank/refs/heads/main/screenshots/medibank-2026-08-07T172342.png
security:
- kind: domain-security
  name: Medibank Domain Security
  slug: medibank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: medibank
tags:
- Insurance
- Australia
- Health Insurance
- Private Health Insurance
- Life and Health
- Carrier
- Claims
- Policy Administration
- Travel Insurance
- Pet Insurance
- Partner Gated
website: https://www.medibank.com.au/
---
