---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-03'
api_count: 17
apis:
- description: ''
  name: Power2SME Bank Master API
  slug: power2sme-bank-master-api
- description: ''
  name: Power2SME Customer Contact API
  slug: power2sme-customer-contact-api
- description: ''
  name: Power2SME Email Verification API
  slug: power2sme-email-verification-api
- description: ''
  name: Power2SME Employee Login API
  slug: power2sme-employee-login-api
- description: ''
  name: Power2SME General Mobile OTP Service API
  slug: power2sme-general-mobile-otp-service-api
- description: ''
  name: Power2SME General Mobile OTP Service By Template API
  slug: power2sme-general-mobile-otp-service-by-template-api
- description: ''
  name: Power2SME Holiday Calendar API
  slug: power2sme-holiday-calendar-api
- description: ''
  name: Power2SME Location Master API
  slug: power2sme-location-master-api
- description: ''
  name: Power2SME Mobile Application API
  slug: power2sme-mobile-application-api
- description: ''
  name: Power2SME Mobile OTP Service By Template for Customer only API
  slug: power2sme-mobile-otp-service-by-template-for-customer-only-api
- description: ''
  name: Power2SME Mobile OTP Service for Customer only API
  slug: power2sme-mobile-otp-service-for-customer-only-api
- description: ''
  name: Power2SME Notification Service API
  slug: power2sme-notification-service-api
- description: ''
  name: Power2SME P2S RPT API
  slug: power2sme-p2s-rpt-api
- description: ''
  name: Power2SME SKU Navision API
  slug: power2sme-sku-navision-api
- description: ''
  name: Power2SME SKU's information API
  slug: power2sme-sku-s-information-api
- description: ''
  name: Power2SME Static information API
  slug: power2sme-static-information-api
- description: True Caller Controller
  name: Power2SME true-caller-controller API
  slug: power2sme-true-caller-controller-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: http://www.power2sme.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.power2sme.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.power2sme.com/api/ws/v4/swagger-ui.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.power2sme.com/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.power2sme.com/privacypolicy
- group: auth
  title: ''
  type: Authentication
  url: authentication/power2sme-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/power2sme-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/power2sme-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/power2sme-llms.txt
created: '2026-07-17'
description: Power2SME operates "India's First Buying Club for SMEs" — a B2B raw-materials procurement and SME-financing platform that aggregates demand from small and medium enterprises to secure better pricing and access to working capital. The company exposes a public version 4 platform API (POWER2SME API) covering SME onboarding (Sign Up, Sign In, OTP verification, TrueCaller), password lifecycle, SKU and catalog master data, bank/location/entity reference masters, credit and holiday-calendar utilities, and email/SMS notification services. Surfaced as a portfolio company of Accel and enriched into the API Evangelist network from its live Swagger 2.0 documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/power2sme.png
layout: provider
mcp_servers:
- description: ''
  name: power2sme-mcp.yml
  slug: power2sme-mcpyml
modified: '2026-07-20'
name: Power2SME
nav: Providers
network: true
overview: 'Power2SME publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Bank Master API, Customer Contact API, Email Verification API, and 14 more. Tagged areas include Company, Marketplaces, SME, Procurement, and India.


  Power2SME''s developer surface includes documentation, API reference, authentication, and 7 more developer resources.'
random_paper: 77
score:
  band: thin
  composite: 28.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 32.3
    developer_ergonomics: 29.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Power2Sme Authentication
  slug: power2sme-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Power2Sme Domain Security
  slug: power2sme-domain-security
  summary_line: TLSv1.3 · DMARC
slug: power2sme
tags:
- Company
- Marketplaces
- SME
- Procurement
- India
- Onboarding
- OTP
- API
website: http://www.power2sme.com
---
