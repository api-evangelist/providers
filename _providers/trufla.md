---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/trufla-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trufla-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trufla-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/trufla-packages.yml
- group: design
  title: ''
  type: Components
  url: components/trufla-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trufla-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trufla-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trufla-conformance.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trufla-technology
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/trufla-technology
- group: company
  title: ''
  type: Website
  url: https://www.trufla.com/
- group: company
  title: ''
  type: About
  url: https://www.trufla.com/about-us/
- group: other
  title: ''
  type: Products
  url: https://www.trufla.com/products/trumarket/
- group: company
  title: ''
  type: Partners
  url: https://www.trufla.com/resources/partners/
- group: other
  title: ''
  type: Marketplace
  url: https://www.trufla.com/products/trumobile/marketplace/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.trufla.com/resources/release-notes/
- group: company
  title: ''
  type: Blog
  url: https://www.trufla.com/blogs/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.trufla.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.trufla.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.trufla.com/request-a-demo/
- group: company
  title: ''
  type: Careers
  url: https://www.trufla.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trufla.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trufla.com/legal/privacy-policy/
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.trufla.com/legal/acceptable-use-policy/
- group: other
  title: ''
  type: Resources
  url: https://www.trufla.com/resources/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.trufla.com/resources/case-studies/
- group: learn
  title: ''
  type: Webinars
  url: https://www.trufla.com/resources/webinars/
created: '2026-07-25'
description: 'Trufla Technology is a Calgary, Alberta insurtech that builds digital distribution software for independent property and casualty insurance brokerages, serving 300+ brokerages primarily across Canada with some UK clients. Founded in 2018 by Sherif Gemayel out of Sharp Insurance''s in-house tooling (SharpMobile plus the E-Method digital agency), Trufla sells a broker-channel suite rather than underwriting risk itself: truWeb for broker websites, SEO and digital marketing; truMarket, an insurance CRM with a "Quote Bind Issue" rating workflow, lead management, an app store and a marketplace; truMobile, a customer self-service app and broker portal with policy access, document delivery, claim reporting and a marketplace for auxiliary products such as travel, roadside and pet; DataHub with the Policy KPI Dashboard and AI Retention X-Ray; Trudi, an AI insurance assistant; and PolicyPro, a contracted back-office outsourcing service. Its API posture is entirely partner-gated and inbound.
  Trufla publishes no public developer portal and no self-serve API — developer.trufla.com, developers.trufla.com, docs.trufla.com and api.trufla.com do not resolve (NXDOMAIN), and every OpenAPI, Swagger, GraphQL and API-docs path probed on www.trufla.com returns 404. Integration happens the way it does across the Canadian broker channel: through broker management system connectors (Acturis, Power Broker, Vertafore, Applied Epic/TAM), Salesforce, SEH Systems, telephony, e-signature and payment apps subscribed from the truMarket app store, and through a CSIO implementation step during onboarding. Trufla makes no reference to ACORD, AL3 or IVANS anywhere on its public site; CSIO — Canada''s insurance data-standards body — is the standards seam here, and Trufla''s own terms of service require the brokerage client to supply its own CSIO account and mailbox plus its own insurer contracts and APIs. What Trufla does publish machine-readably sits outside the developer surface entirely: an llms.txt
  at www.trufla.com/llms.txt that licenses AI summarization while forbidding training and pricing extraction, a SafeBase trust center at trust.trufla.com that names AWS as its sole subprocessor and no completed certification, dated per-product release notes, a GitHub organization at trufla-technology holding only forks, and one first-party npm package, the Angular JSON-Schema form library @trufla/ngx-tru-forms.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Trufla
nav: Providers
network: true
overview: 'Trufla is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Property and Casualty, Insurtech, and Broker.


  Trufla''s developer surface includes changelog, engineering blog, support, signup flow, and 23 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 22.2
  delta: -2.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 24.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Trufla Authentication
  slug: trufla-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Trufla Domain Security
  slug: trufla-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Trufla Trust Center
  slug: trufla-trust-center
  summary_line: trust center published
slug: trufla
tags:
- Insurance
- Canada
- Property and Casualty
- Insurtech
- Broker
- Agency Management
- CSIO
- Policy Administration
- Quote Bind Issue
- Digital Distribution
website: https://www.trufla.com/
---
