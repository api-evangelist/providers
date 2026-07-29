---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Fonoa Agentic Access
  operation_count: 10
  slug: fonoa-agentic-access
  summary_line: 10 operations · 8 acting
api_count: 5
apis:
- description: Webhooks management API for configuring real-time event notifications from Fonoa's platform. Recommended over polling for transaction status updates and e-invoicing compliance events.
  name: Fonoa Webhooks API
  slug: webhooks-api
- description: The Lookup V2 API from Fonoa — 5 operation(s) for lookup v2.
  name: Fonoa Lookup V2 API
  slug: fonoa-lookup-v2-api
- description: The Onboarding API from Fonoa — 1 operation(s) for onboarding.
  name: Fonoa Onboarding API
  slug: fonoa-onboarding-api
- description: The Tax API from Fonoa — 1 operation(s) for tax.
  name: Fonoa Tax API
  slug: fonoa-tax-api
- description: The Transactions API from Fonoa — 1 operation(s) for transactions.
  name: Fonoa Transactions API
  slug: fonoa-transactions-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fonoa-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fonoa-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fonoa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fonoa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fonoa-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.fonoa.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fonoa.com/reference/welcome-to-fonoa
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fonoa.com/reference/getting-started-with-fonoa-api
- group: auth
  title: ''
  type: Authentication
  url: https://docs.fonoa.com/reference/api-authentication-overview
- group: other
  title: ''
  type: Environments
  url: https://docs.fonoa.com/reference/environments
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.fonoa.com/reference/change-log
- group: company
  title: ''
  type: Blog
  url: https://www.fonoa.com/resources/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fonoa
- group: other
  title: ''
  type: X
  url: https://twitter.com/Fonoa_HQ
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fonoa-Tech
- group: auth
  title: ''
  type: Security
  url: https://www.fonoa.com/resources/security
- group: commercial
  title: ''
  type: Plans
  url: plans/fonoa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fonoa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fonoa-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/fonoa-context.jsonld
created: '2026-06-12'
description: Fonoa is a global indirect tax automation platform that connects the full indirect tax lifecycle on one platform, serving enterprises across 100+ countries and jurisdictions. The platform provides APIs for real-time tax ID validation across 120+ countries, VAT/GST and sales tax calculation, e-invoicing compliance with local mandates, transaction reporting, and automated multi-country tax return filing. Companies such as Zoom, Uber, Booking.com, and Remote.com rely on Fonoa to automate and manage their global indirect tax obligations through a single API integration.
finops:
- name: Fonoa Finops
  service_category: ''
  slug: fonoa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fonoa.png
jsonld:
- class_count: 46
  name: Fonoa Context
  property_count: 2
  slug: fonoa-context
layout: provider
modified: '2026-06-12'
name: Fonoa
nav: Providers
network: true
overview: 'Fonoa publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Lookup V2 API, Onboarding API, Tax API, and 1 more. Tagged areas include Tax, VAT, GST, E-Invoicing, and Tax Automation.


  The Fonoa catalog on APIs.io includes 1 JSON-LD context.


  Fonoa''s developer surface includes authentication, documentation, getting-started guide, changelog, engineering blog, and 15 more developer resources.'
plans:
- name: Fonoa Plans Pricing
  plan_count: 1
  slug: fonoa-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 3
  name: Fonoa Rate Limits
  slug: fonoa-rate-limits
score:
  band: developing
  composite: 45.3
  delta: -2.7
  facets:
    commercial_clarity: 36.8
    contract_quality: 63.0
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fonoa/refs/heads/main/screenshots/fonoa-2026-06-20T181458.png
security:
- kind: authentication
  name: Fonoa Authentication
  slug: fonoa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fonoa Domain Security
  slug: fonoa-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fonoa Vulnerability Disclosure
  slug: fonoa-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Fonoa Trust Center
  slug: fonoa-trust-center
  summary_line: GDPR
slug: fonoa
tags:
- Tax
- VAT
- GST
- E-Invoicing
- Tax Automation
- Tax Compliance
- Tax Calculation
- Tax ID Validation
- Invoice Generation
- Global Tax
- Indirect Tax
- FinTech
website: https://www.fonoa.com
---
