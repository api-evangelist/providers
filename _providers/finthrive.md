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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The FinThrive API, published through a Microsoft Azure API Management instance. The developer portal at api-portal.nthrive.com is publicly reachable and describes auto-generated API documentation, mul
  name: FinThrive API
  slug: finthrive-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://finthrive.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-portal.nthrive.com/
- group: start
  title: ''
  type: Login
  url: https://finthrive.com/product-login
- group: operate
  title: ''
  type: Support
  url: https://finthrive.my.site.com/portal/s/
- group: company
  title: ''
  type: Blog
  url: https://finthrive.com/resources?content_type=blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finthrive.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finthrive.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://finthrive.com/security-and-data-trust-center
- group: operate
  title: ''
  type: Contact
  url: https://finthrive.com/contact-us
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finthrive-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/finthrive-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/finthrive-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finthrive-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finthrive-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/finthrive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/finthrive-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: FinThrive's Azure API Management developer portal at api-portal.nthrive.com loads for anyone, but its own catalog endpoint /mapi/apis?api-version=2022-08-01 returns {"value":[],"count":0} to an anonymous caller — the API and product list is only populated after an Azure Active Directory or FinThrive-issued evaluation sign-in, so the contract behind the live gateway at api.finthrive.com is never public.
  evidence:
  - status: 200
    url: https://api-portal.nthrive.com/mapi/apis?api-version=2022-08-01
  - status: 200
    url: https://api-portal.nthrive.com/mapi/products?api-version=2022-08-01
  - status: 404
    url: https://api.finthrive.com/openapi.json
  - status: 404
    url: https://finthrive.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-12'
description: FinThrive is a healthcare revenue cycle management (RCM) technology company serving hospitals, health systems, ambulatory and physician practices, payers, life sciences organizations and channel partners across the United States. Formed from the 2022 rebrand of nThrive and the acquisition of TransUnion Healthcare, FinThrive sells a SaaS platform spanning patient access (Access Coordinator, Virtual Intake, Insurance Discover), revenue integrity (CDM Management, Revenue Capture, Knowledge Source), revenue optimization (Claims Manager, Contract Manager, A/R Optimizer), analytics (FinThrive Analyze), education (FinThrive Learn) and agentic AI automation, all built on FinThrive Fusion, its unified data-intelligence and integration layer. It operates a production Azure API Management gateway at api.finthrive.com (aliased as api.nthrive.com) with a public developer portal at api-portal.nthrive.com, but every API and product listed there is visible only after an Azure Active Directory
  or FinThrive-issued evaluation sign-in, so no machine-readable contract is published to the public.
image: https://finthrive.com/hs-fs/hubfs/social-suggested-images/finthrive.comhubfsFinThrive_primary_logo_TM_darkBG_RGB_400x60%5B82%5D.png
layout: provider
modified: '2026-08-12'
name: FinThrive
nav: Providers
network: true
overview: 'FinThrive publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Revenue Cycle Management, Health IT, and Claims.


  FinThrive''s developer surface includes support, engineering blog, and 14 more developer resources.'
plans:
- name: Finthrive Plans Pricing
  plan_count: 0
  slug: finthrive-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 0
  name: Finthrive Rate Limits
  slug: finthrive-rate-limits
score:
  band: emerging
  composite: 23.2
  delta: -1.1
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Finthrive Authentication
  slug: finthrive-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Finthrive Domain Security
  slug: finthrive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Finthrive Trust Center
  slug: finthrive-trust-center
  summary_line: SOC, HITRUST, NIST CSF, EHNAC
slug: finthrive
tags:
- Company
- Healthcare
- Revenue Cycle Management
- Health IT
- Claims
- Billing
- Payments
- Insurance
- Patient Access
- Analytics
- SaaS
- United States
website: https://finthrive.com/
---
