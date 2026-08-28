---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The External API (ExtAPI) is named in the company's own llms.txt as the integration surface used to synchronize employee and organizational data from HRIS and identity systems that lack a native conne
  name: Lanes & Planes External API (ExtAPI)
  slug: ext-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.lanes-planes.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.lanes-planes.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://support.lanes-planes.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.lanes-planes.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.lanes-planes.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lanes-planes.com/en/packages/
- group: start
  title: ''
  type: SignUp
  url: https://www.lanes-planes.com/en/demo/
- group: start
  title: ''
  type: Login
  url: https://app.lanes-planes.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lanes-planes.com/en/agb/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lanes-planes.com/en/data-protection/
- group: other
  title: ''
  type: Imprint
  url: https://www.lanes-planes.com/en/imprint/
- group: company
  title: ''
  type: Careers
  url: https://www.lanes-planes.com/en/career/
- group: company
  title: ''
  type: Press
  url: https://www.lanes-planes.com/en/press/
- group: company
  title: ''
  type: Partners
  url: https://www.lanes-planes.com/en/partner/
- group: other
  title: ''
  type: CustomerStories
  url: https://www.lanes-planes.com/en/customer-stories/
- group: company
  title: ''
  type: LinkedIn
  url: https://de.linkedin.com/company/lanes-planes-gmbh
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.lanes-planes.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.lanes-planes.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lanes-and-planes-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/lanes-and-planes-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lanes-and-planes-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lanes-and-planes-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lanes-and-planes-trust-center.yml
created: '2026-07-17'
description: 'Lanes & Planes is a Munich-based travel and expense (T&E) management platform that positions itself as the financial infrastructure for European corporate travel. The platform covers the full T&E lifecycle in one system: travel request, digital approval flows, booking, and final accounting. Its inventory spans European rail (Deutsche Bahn, ÖBB, SBB, SNCF), flights from the major global carriers and alliances including NDC content, over seven million hotels via direct interfaces plus HRS, Expedia and Booking.com, Airbnb for Work, global rental cars, and ground mobility including the Deutschland-Ticket and Flixbus. The product is built for finance departments, emphasizing VAT-compliant automated invoicing, German per-diem (VMA) tax logic, centralized billing on a single creditor, real-time budget tracking, and automated travel-policy enforcement. It integrates with ERP and accounting systems (DATEV, SAP, Microsoft Dynamics, Sage, Addison) and with HRIS platforms, offering native
  Personio synchronization and an External API (ExtAPI) for other HRIS and identity systems such as Workday, BambooHR and HiBob. Enterprise authentication is via SAML 2.0 single sign-on. The company is certified to ISO 27001 and ISO 9001, is GDPR compliant, and hosts on European servers. Lanes & Planes is backed by Battery Ventures.'
image: https://assets.wp.lanes-planes.com/app/uploads/2024/11/Display_image_Lanes-Planes.jpg
layout: provider
modified: '2026-07-19'
name: Lanes & Planes
nav: Providers
network: true
overview: 'Lanes & Planes publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Business Travel, Travel Management, and Expense Management.


  Lanes & Planes'' developer surface includes documentation, support, engineering blog, pricing, signup flow, authentication, and 17 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 27.6
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 27.6
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lanes-and-planes/refs/heads/main/screenshots/lanes-and-planes-2026-07-25T224513.png
security:
- kind: authentication
  name: Lanes And Planes Authentication
  slug: lanes-and-planes-authentication
  summary_line: saml · 1 scheme
- kind: domain-security
  name: Lanes And Planes Domain Security
  slug: lanes-and-planes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lanes And Planes Trust Center
  slug: lanes-and-planes-trust-center
  summary_line: ISO 27001, ISO 9001
slug: lanes-and-planes
tags:
- Company
- Travel
- Business Travel
- Travel Management
- Expense Management
- Spend Management
- Finance
- Accounting
- ERP Integration
- HRIS
- Software-as-a-Service
- Germany
- Europe
website: https://www.lanes-planes.com/
---
