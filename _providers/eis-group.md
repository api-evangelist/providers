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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eis-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eisgroup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.eisgroup.com/
- group: company
  title: ''
  type: Blog
  url: https://www.eisgroup.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.eisgroup.com/feed/
- group: company
  title: ''
  type: Newsroom
  url: https://www.eisgroup.com/company/newsroom/
- group: company
  title: ''
  type: Partners
  url: https://www.eisgroup.com/company/partners/
- group: company
  title: ''
  type: PartnerApplication
  url: https://www.eisgroup.com/company/partner-application/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eisgroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eisgroupltd
- group: operate
  title: ''
  type: Contact
  url: https://www.eisgroup.com/company/contact/
- group: operate
  title: ''
  type: Support
  url: https://www.eisgroup.com/company/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eisgroup.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eisgroup.com/privacy-statement/
- group: auth
  title: ''
  type: Compliance
  url: https://www.eisgroup.com/company#CertificationsRecognitions
- group: design
  title: ''
  type: Conformance
  url: conformance/eis-group-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/eis-group-packages.yml
- group: design
  title: ''
  type: Components
  url: components/eis-group-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eis-group-llms.txt
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/eisgroup/ui-render
- group: auth
  title: ''
  type: Certifications
  url: https://machalliance.org/members/eis
created: '2026-07-25'
description: EIS Group (EIS Ltd) is a United States core-systems vendor for insurance, founded in 2008 out of Exigen Insurance Solutions and headquartered in San Francisco, California. EIS sells the EIS Platform and EIS OneSuite — a cloud-native, microservices core suite covering customer management, policy administration, billing, and claims — across group benefits, property and casualty / general, protection, life and annuities, and pet insurance. EIS markets itself as API-first and claims thousands of open REST APIs (1,100 digital APIs announced in 2019, 9,000+ claimed for OneSuite) fronted by the EIS DXP API middleware, but none of that surface is public. There is no self-serve developer portal on eisgroup.com; the documentation host docs.eisgroup.com answers HTTP 401 behind an HTTP Basic realm named "EIS Group Users", so the entire API reference is a customer/partner login wall. No OpenAPI, Swagger, GraphQL, AsyncAPI, or public Postman collection could be retrieved. The only public
  code EIS ships is two open-source GitHub repositories (kraken-rules, ui-render), which are libraries rather than APIs. ACORD is attested only indirectly — an analyst evaluation hosted on eisgroup.com states the system integrates using "web services, APIs, RESTful APIs, ACORD and certified ACORD" — with no ACORD artifacts, AL3 mappings, or IVANS/agency-download detail published. What EIS does publish is a substantial certification posture — a certified MACH Alliance membership (Microservices, API-first, Cloud-native SaaS, Headless) and a full ISO stack covering 27001, 27701, 22301, 27017, 27018, 27035-1, 12207, 15288, 25000 and ISO/IEC 42001, which EIS announced in June 2025 as the first cloud-native insurance core platform provider to obtain. One first-party package is public, eis-ui-render on npm. This is the canonical United States core-systems posture — the APIs exist and are sold, but they are reachable only through a licensed implementation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: EIS Group
nav: Providers
network: true
overview: 'EIS Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United States, Core Systems, Policy Administration, and Claims.


  EIS Group''s developer surface includes documentation, engineering blog, support, and 18 more developer resources.'
random_paper: 68
score:
  band: emerging
  composite: 20.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 20.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eis-group/refs/heads/main/screenshots/eis-group-2026-07-25T213033.png
security:
- kind: domain-security
  name: Eis Group Domain Security
  slug: eis-group-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eis-group
tags:
- Insurance
- United States
- Core Systems
- Policy Administration
- Claims
- Billing
- Underwriting
- Property and Casualty
- Life Insurance
- Employee Benefits
- Insurtech
- ACORD
website: https://www.eisgroup.com/
---
