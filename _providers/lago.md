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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 54
  human_in_the_loop: 2
  name: Lago Agentic Access
  operation_count: 93
  slug: lago-agentic-access
  summary_line: 93 operations · 54 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Add-on collection
  name: Lago Add_ons API
  slug: lago-add-ons-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Analytics
  name: Lago Analytics API
  slug: lago-analytics-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Billable metric collection
  name: Lago Billable_metrics API
  slug: lago-billable-metrics-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Coupon collection
  name: Lago Coupons API
  slug: lago-coupons-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Credit notes collection
  name: Lago Credit_notes API
  slug: lago-credit-notes-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Customer collection
  name: Lago Customers API
  slug: lago-customers-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Event collection
  name: Lago Events API
  slug: lago-events-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Fees
  name: Lago Fees API
  slug: lago-fees-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Invoice collection
  name: Lago Invoices API
  slug: lago-invoices-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Organization collection
  name: Lago Organizations API
  slug: lago-organizations-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about PaymentRequests
  name: Lago Payment_requests API
  slug: lago-payment-requests-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Plan collection
  name: Lago Plans API
  slug: lago-plans-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Subscription collection
  name: Lago Subscriptions API
  slug: lago-subscriptions-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Tax collection
  name: Lago Taxes API
  slug: lago-taxes-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Wallet collection
  name: Lago Wallets API
  slug: lago-wallets-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Webhook Endpoints
  name: Lago Webhook_endpoints API
  slug: lago-webhook-endpoints-api
- baseURL: https://api.getlago.com/api/v1
  baseurl_source: spec
  description: Everything about Webhooks
  name: Lago Webhooks API
  slug: lago-webhooks-api
artifact_total: 44
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lago API documentation Add_ons API
  slug: open-lago-add-ons-api
- collection_type: open
  name: Lago API documentation Add_ons Analytics API
  slug: open-lago-analytics-api
- collection_type: open
  name: Lago API documentation Add_ons Billable_metrics API
  slug: open-lago-billable-metrics-api
- collection_type: open
  name: Lago API documentation Add_ons Coupons API
  slug: open-lago-coupons-api
- collection_type: open
  name: Lago API documentation Add_ons Credit_notes API
  slug: open-lago-credit-notes-api
- collection_type: open
  name: Lago API documentation Add_ons Customers API
  slug: open-lago-customers-api
- collection_type: open
  name: Lago API documentation Add_ons Events API
  slug: open-lago-events-api
- collection_type: open
  name: Lago API documentation Add_ons Fees API
  slug: open-lago-fees-api
- collection_type: open
  name: Lago API documentation Add_ons Invoices API
  slug: open-lago-invoices-api
- collection_type: open
  name: Lago API documentation Add_ons Organizations API
  slug: open-lago-organizations-api
- collection_type: open
  name: Lago API documentation Add_ons Payment_requests API
  slug: open-lago-payment-requests-api
- collection_type: open
  name: Lago API documentation Add_ons Plans API
  slug: open-lago-plans-api
- collection_type: open
  name: Lago API documentation Add_ons Subscriptions API
  slug: open-lago-subscriptions-api
- collection_type: open
  name: Lago API documentation Add_ons Taxes API
  slug: open-lago-taxes-api
- collection_type: open
  name: Lago API documentation Add_ons Wallets API
  slug: open-lago-wallets-api
- collection_type: open
  name: Lago API documentation Add_ons Webhook_endpoints API
  slug: open-lago-webhook-endpoints-api
- collection_type: open
  name: Lago API documentation Add_ons Webhooks API
  slug: open-lago-webhooks-api
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
overview: 'Lago publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Add_ons API, Analytics API, Billable_metrics API, and 14 more. Tagged areas include Billing, Metering, Open-Source, and Usage-Based.


  Lago''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Lago Plans Pricing
  plan_count: 3
  slug: lago-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Lago Rate Limits
  slug: lago-rate-limits
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 84.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 62.8
    developer_ergonomics: 31.0
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Open-Source
- Usage-Based
website: https://getlago.com/
---
