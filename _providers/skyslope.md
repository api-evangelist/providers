---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Skyslope Agentic Access
  operation_count: 38
  slug: skyslope-agentic-access
  summary_line: 38 operations · 19 acting
api_count: 15
apis:
- description: SkySlope's broader enterprise Transaction Management API, positioned for brokerages to query, extract, and build on top of their SkySlope transaction data for reporting tools, dashboards, and enterpri
  name: SkySlope Transaction Management API (BETA)
  slug: skyslope-transaction-management-api
- description: The Agents, Listings API from SkySlope — 1 operation(s) for agents, listings.
  name: SkySlope Agents, Listings API
  slug: skyslope-agents-listings-api
- description: The Auth API from SkySlope — 1 operation(s) for auth.
  name: SkySlope Auth API
  slug: skyslope-auth-api
- description: The Buyer Agreements API from SkySlope — 1 operation(s) for buyer agreements.
  name: SkySlope Buyer Agreements API
  slug: skyslope-buyer-agreements-api
- description: The Contacts API from SkySlope — 4 operation(s) for contacts.
  name: SkySlope Contacts API
  slug: skyslope-contacts-api
- description: The Documents API from SkySlope — 5 operation(s) for documents.
  name: SkySlope Documents API
  slug: skyslope-documents-api
- description: The Envelopes API from SkySlope — 1 operation(s) for envelopes.
  name: SkySlope Envelopes API
  slug: skyslope-envelopes-api
- description: The Files API from SkySlope — 14 operation(s) for files.
  name: SkySlope Files API
  slug: skyslope-files-api
- description: The Forms API from SkySlope — 1 operation(s) for forms.
  name: SkySlope Forms API
  slug: skyslope-forms-api
- description: The Libraries API from SkySlope — 3 operation(s) for libraries.
  name: SkySlope Libraries API
  slug: skyslope-libraries-api
- description: The Offers API from SkySlope — 2 operation(s) for offers.
  name: SkySlope Offers API
  slug: skyslope-offers-api
- description: The Report API from SkySlope — 1 operation(s) for report.
  name: SkySlope Report API
  slug: skyslope-report-api
- description: The Templates API from SkySlope — 1 operation(s) for templates.
  name: SkySlope Templates API
  slug: skyslope-templates-api
- description: The Users API from SkySlope — 4 operation(s) for users.
  name: SkySlope Users API
  slug: skyslope-users-api
- description: The Webhooks API from SkySlope — 1 operation(s) for webhooks.
  name: SkySlope Webhooks API
  slug: skyslope-webhooks-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/skyslope-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skyslope-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skyslope.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skyslope
- group: docs
  title: ''
  type: Documentation
  url: https://forms.skyslope.com/partner/api/docs
- group: docs
  title: ''
  type: Documentation
  url: https://skyslope.com/general/unlocking-the-power-of-your-data/
- group: commercial
  title: ''
  type: Plans
  url: plans/skyslope-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skyslope-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/skyslope-finops.yml
created: '2026-07-04'
description: SkySlope is a real estate transaction management and digital forms platform used by brokerages, teams, and agents across the U.S. and Canada to store, manage, and audit transaction documents for compliance, prepare and e-sign forms, and manage offers. SkySlope exposes a partner-oriented public API program - a Partnership / Forms API (OAuth 2.0 authorization-code flow with PKCE) for creating and managing listing and transaction files, documents, contacts, envelopes, forms libraries, and templates; an Offers API (OAuth 2.0 client-credentials flow) for retrieving listings, offers, and offer/listing analytics from SkySlope Offers; and a broader Transaction Management API (BETA) positioned for brokerages to query and extract their SkySlope data for reporting and enterprise integration. API access is partner/brokerage-gated - reference documentation is public but obtaining OAuth client credentials requires working with SkySlope.
finops:
- name: Skyslope Finops
  service_category: Real Estate Transaction Management
  slug: skyslope-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skyslope.png
layout: provider
modified: '2026-07-04'
name: SkySlope
nav: Providers
network: true
overview: 'SkySlope publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Agents, Listings API, Auth API, Buyer Agreements API, and 11 more. Tagged areas include Real Estate, Transaction Management, Digital Forms, E-Signature, and Compliance.


  SkySlope''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Skyslope Plans Pricing
  plan_count: 3
  slug: skyslope-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 4
  name: Skyslope Rate Limits
  slug: skyslope-rate-limits
score:
  band: thin
  composite: 36.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.6
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Skyslope Domain Security
  slug: skyslope-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: skyslope
tags:
- Real Estate
- Transaction Management
- Digital Forms
- E-Signature
- Compliance
- PropTech
- Documents
website: https://skyslope.com
---
