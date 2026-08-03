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
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.definityfinancial.com/
- group: company
  title: ''
  type: Website
  url: https://www.economical.com/
- group: company
  title: ''
  type: Website
  url: https://www.sonnet.ca/
- group: company
  title: ''
  type: Website
  url: https://www.petsecure.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/definity-insurance
- group: company
  title: ''
  type: Blog
  url: https://www.economical.com/en/blog
- group: company
  title: ''
  type: Blog
  url: https://www.sonnet.ca/blog
- group: operate
  title: ''
  type: Support
  url: https://www.economical.com/en/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.sonnet.ca/faqs
- group: start
  title: ''
  type: SignUp
  url: https://www.sonnet.ca/get-a-quote
- group: start
  title: ''
  type: Login
  url: https://www.sonnet.ca/account-log-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.economical.com/en/terms-of-use
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sonnet.ca/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.economical.com/en/privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sonnet.ca/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://csio.com/csio-certification/certified-members
- group: other
  title: ''
  type: Standard
  url: https://csio.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/definity-financial-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/definity-financial-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/definity-financial-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/definity-financial-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/definity-financial-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/definity-financial-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/definity-financial-sonnet-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/definity-financial-economical-llms.txt
created: '2026-07-25'
description: 'Definity Financial Corporation is a Canadian property and casualty insurance group headquartered in Waterloo, Ontario and listed on the Toronto Stock Exchange (DFY). It is the demutualized successor to Economical Mutual Insurance Company, founded in 1871 in Berlin (now Kitchener), Ontario; policyholders approved demutualization in May 2021 and the company completed its IPO in November 2021, renaming the operating carrier Definity Insurance Company. Definity underwrites personal and commercial property, automobile, farm, and pet lines across Canada through four brands: Economical (broker-distributed home, auto, farm and business insurance), Sonnet (described by the company as the largest fully digital direct-to-consumer insurance business in Canada), Family Insurance Solutions, and Petline/Petsecure (pet insurance). It is one of the Big Few Canadian P&C carriers and reported roughly $6.3B in gross written premiums on a trailing-twelve-month pro-forma basis including its Travelers
  Canada acquisition. Its API posture is partner-gated and honest to state plainly: Definity publishes no public, self-serve developer portal and no downloadable OpenAPI, Swagger, GraphQL, or AsyncAPI definition on any first-party host. Every developer-shaped subdomain of definityfinancial.com fails to resolve, an api.definity.com host exists behind Imperva but answers HTTP 404 with an empty body to every anonymous path including OAuth and OpenID discovery, and the only reachable broker surface, broker.economical.com, is a Docebo learning management system for broker training rather than an API reference. The gated API is nonetheless real and independently attested: CSIO, Canada''s property-and-casualty data-standards body and the domestic counterpart to ACORD, certified Definity against its API Security Standards on 27 November 2024 — the industry''s standard authentication and authorization API model for insurer-to-broker-management-system connectivity, requiring confirmed mitigation of
  16 OAuth security concerns and 18 API endpoint concerns — and Definity is additionally CSIO eDocs Certified and Compliance Certified (all non-standard Z-Codes eliminated from broker data exchange). Its Vyne broker digital platform runs on Guidewire Cloud, which Definity was the first Canadian P&C insurer to adopt for its core insurance platform. Two brands, Sonnet and Economical, publish real hand-authored llms.txt documents with explicit AI-training, generation, summarization and crawling directives, including named directives for OpenAI, Google-DeepMind and Anthropic. All of this sits in a Canadian market where OSFI supervises prudentially, the provinces regulate conduct, and Consumer-Driven Banking excludes insurance entirely, so no open-insurance mandate forces a public API surface and standardization is industry-led through CSIO instead.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Definity Financial
nav: Providers
network: true
overview: 'Definity Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Property and Casualty, Carrier, and Underwriting.


  Definity Financial''s developer surface includes engineering blog, support, signup flow, authentication, and 21 more developer resources.'
random_paper: 33
score:
  band: emerging
  composite: 24.8
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 24.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/definity-financial/refs/heads/main/screenshots/definity-financial-2026-07-25T211640.png
security:
- kind: authentication
  name: Definity Financial Authentication
  slug: definity-financial-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Definity Financial Domain Security
  slug: definity-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: definity-financial
tags:
- Insurance
- Canada
- Property and Casualty
- Carrier
- Underwriting
- Claims
- Broker
- Pet Insurance
- Direct to Consumer
- Partner Gated
- CSIO
- Insurtech
website: https://www.definityfinancial.com/
---
