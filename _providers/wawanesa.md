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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Broker-facing commercial small business API announced by Wawanesa on 2022-03-30, built with HUB International and described by Wawanesa as "fully aligned with CSIO data standards". Per the company ann
  name: Wawanesa Commercial Small Business API
  slug: wawanesa-commercial-small-business-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wawanesa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wawanesa-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wawanesa-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wawanesa-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wawanesa-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://csio.com/news/wawanesa-insurance-achieves-api-security-standards-certification-safeguarding-data-and
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wawanesa-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.wawanesa.com/canada/
- group: company
  title: ''
  type: Blog
  url: https://www.wawanesa.com/canada/blog/
- group: company
  title: ''
  type: News
  url: https://www.wawanesa.com/canada/news/
- group: start
  title: ''
  type: PartnerPortal
  url: https://brokerplatform.wawanesa.com/
- group: start
  title: ''
  type: Login
  url: https://login.brokerplatform.wawanesa.com/
- group: start
  title: ''
  type: CustomerPortal
  url: https://membercentre.wawanesa.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.wawanesa.com/canada/contact-us/inquiries-and-feedback.html
- group: operate
  title: ''
  type: Support
  url: https://www.wawanesa.com/canada/contact-us/inquiries-and-feedback.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wawanesa.com/canada/pip/about-privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wawanesa.com/canada/pip/terms-and-conditions.html
- group: company
  title: ''
  type: Careers
  url: https://www.wawanesa.com/jobs/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wawanesa-insurance
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/wawanesa
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/wawanesainsurance
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/wawanesa
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/wawanesacanada
created: '2026-07-25'
description: 'The Wawanesa Mutual Insurance Company, founded in 1896 in Wawanesa, Manitoba and headquartered in Winnipeg, is one of Canada''s largest property and casualty mutual insurers, writing auto, home, condo, tenant, seasonal residence, farm and commercial lines across every province and territory through a 100% independent broker distribution model, alongside its wholly-owned life and group subsidiary Wawanesa Life. Wawanesa runs its policy, claims and billing on Guidewire InsuranceSuite following a roughly $300 million Strategic Systems Renewal that made it one of the first Canadian insurers to put its entire product suite online, and it has announced a broker-facing API programme — most notably a Commercial Small Business API aligned to CSIO data standards that supports real-time rating, quoting and binding — plus CSIO My Proof of Insurance electronic pink slips. None of that surface is public: Wawanesa publishes no developer portal, no API reference, no OpenAPI, and no self-serve
  signup. Probes of developer./developers./docs. wawanesa.com do not resolve, api.wawanesa.com answers 403 at the root, and the only integration path is the Salesforce-based Broker Platform behind an Okta login with onboarding brokered by a Wawanesa Business Development representative. Canada has no open-insurance mandate — Consumer-Driven Banking excludes insurance outright — so the connectivity layer here is CSIO, not ACORD, and the honest posture is partner-gated with no public API. What Wawanesa does publish is certification: it holds CSIO''s API Security Standards Certification (2024-10-29), was the first CSIO member certified in JSON API Standards for Billing (2025-02-05), was the first insurer to attain Claims eDocs Certification (2022-04-04), and contributed nine reusable API packages — Quote, New Business, Policy Inquiry, Policy Update List, Policy Cancellation, Risk Appetite, Required Fields, Billing Inquiry and eDocs — to CSIO''s Reusable Services Library for other carriers and
  BMS vendors to implement.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Wawanesa Insurance
nav: Providers
network: true
overview: 'Wawanesa Insurance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Property and Casualty, Carrier, and Mutual Insurer.


  Wawanesa Insurance''s developer surface includes authentication, engineering blog, product news, support, YouTube channel, and 18 more developer resources.'
random_paper: 43
scopes:
- name: Wawanesa Scopes
  scope_count: 0
  slug: wawanesa-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.7
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 28.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Wawanesa Authentication
  slug: wawanesa-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Wawanesa Domain Security
  slug: wawanesa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wawanesa
tags:
- Insurance
- Canada
- Property and Casualty
- Carrier
- Mutual Insurer
- Broker
- Commercial Lines
- Personal Lines
- Underwriting
- Claims
- Policy Administration
- CSIO
- Partner Gated
website: https://www.wawanesa.com/canada/
---
