---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 54
  human_in_the_loop: 2
  name: Lago Agentic Access
  operation_count: 93
  slug: lago-agentic-access
  summary_line: 93 operations · 54 acting · 2 human-in-the-loop
api_count: 17
apis:
- description: Everything about Add-on collection
  name: Lago Add_ons API
  slug: lago-add-ons-api
- description: Everything about Analytics
  name: Lago Analytics API
  slug: lago-analytics-api
- description: Everything about Billable metric collection
  name: Lago Billable_metrics API
  slug: lago-billable-metrics-api
- description: Everything about Coupon collection
  name: Lago Coupons API
  slug: lago-coupons-api
- description: Everything about Credit notes collection
  name: Lago Credit_notes API
  slug: lago-credit-notes-api
- description: Everything about Customer collection
  name: Lago Customers API
  slug: lago-customers-api
- description: Everything about Event collection
  name: Lago Events API
  slug: lago-events-api
- description: Everything about Fees
  name: Lago Fees API
  slug: lago-fees-api
- description: Everything about Invoice collection
  name: Lago Invoices API
  slug: lago-invoices-api
- description: Everything about Organization collection
  name: Lago Organizations API
  slug: lago-organizations-api
- description: Everything about PaymentRequests
  name: Lago Payment_requests API
  slug: lago-payment-requests-api
- description: Everything about Plan collection
  name: Lago Plans API
  slug: lago-plans-api
- description: Everything about Subscription collection
  name: Lago Subscriptions API
  slug: lago-subscriptions-api
- description: Everything about Tax collection
  name: Lago Taxes API
  slug: lago-taxes-api
- description: Everything about Wallet collection
  name: Lago Wallets API
  slug: lago-wallets-api
- description: Everything about Webhook Endpoints
  name: Lago Webhook_endpoints API
  slug: lago-webhook-endpoints-api
- description: Everything about Webhooks
  name: Lago Webhooks API
  slug: lago-webhooks-api
artifact_total: 26
collections:
- collection_type: open
  name: Lago API documentation
  slug: open-lago
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lago-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lago-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lago-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lago-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lago-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getlago
- group: company
  title: ''
  type: Website
  url: https://getlago.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.getlago.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getlago/lago
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/getlago/inside-lago-voice-skill
- group: agent
  title: ''
  type: LlmsText
  url: https://getlago.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://getlago.com/blog
created: '2024-07-02'
description: Lago offers a self-hosted and cloud, scalable and modular architecture for metering and usage-based billing, at every stage of your company.
finops:
- name: Lago Finops
  service_category: API
  slug: lago-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lago.png
layout: provider
modified: '2026-05-19'
name: Lago
nav: Providers
network: true
overview: 'Lago publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Add_ons API, Analytics API, Billable_metrics API, and 14 more. Tagged areas include Billing, Metering, Open Source, and Usage-Based.


  Lago''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Lago Plans Pricing
  plan_count: 3
  slug: lago-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Lago Rate Limits
  slug: lago-rate-limits
score:
  band: thin
  composite: 38.3
  delta: -2.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.4
    developer_ergonomics: 21.7
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lago/refs/heads/main/screenshots/lago-2026-06-20T184248.png
security:
- kind: authentication
  name: Lago Authentication
  slug: lago-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lago Domain Security
  slug: lago-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Lago Vulnerability Disclosure
  slug: lago-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Lago Trust Center
  slug: lago-trust-center
  summary_line: SOC 2, GDPR
slug: lago
tags:
- Billing
- Metering
- Open Source
- Usage-Based
website: https://getlago.com/
---
