---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Full REST API for managing accounts, subscriptions, plans, add-ons, coupons, invoices, line items, transactions, shipping, tax, and webhooks across a Recurly site. Authentication is HTTP Basic with a '
  name: Recurly v3 API
  slug: v3-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/recurly-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recurly-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recurly
- group: company
  title: ''
  type: Website
  url: https://recurly.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.recurly.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://recurly.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://recurly.com/developers/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://recurly.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://recurly.com/get-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recurly
- group: build
  title: ''
  type: Client Libraries
  url: https://recurly.com/developers/client-libraries/
- group: operate
  title: ''
  type: Support
  url: https://recurly.zendesk.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.recurly.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.recurly.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://recurly.com/blog/rss.xml
created: '2026-05-11'
description: Recurly is a subscription management and recurring billing platform that handles signups, plans, add-ons, coupons, dunning, invoicing, tax, revenue recognition, and analytics for subscription businesses. The Recurly v3 REST API gives developers full access to accounts, subscriptions, invoices, transactions, plans, and webhooks, with a versioned `Accept` header for API revisions. Authentication uses HTTP Basic with a site-scoped API key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recurly.png
layout: provider
modified: '2026-05-30'
name: Recurly
nav: Providers
network: true
overview: 'Recurly publishes 1 API on the [APIs.io](https://apis.io/) network: v3 API. Tagged areas include Subscriptions, Billing, Payments, Recurring Revenue, and Invoicing.


  Recurly''s developer surface includes documentation, API reference, pricing, signup flow, support, engineering blog, and 9 more developer resources.'
random_paper: 36
score:
  band: emerging
  composite: 25.9
  delta: -4.2
  facets:
    commercial_clarity: 18.4
    contract_quality: 32.3
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recurly/refs/heads/main/screenshots/recurly-2026-06-20T192713.png
security:
- kind: domain-security
  name: Recurly Domain Security
  slug: recurly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Recurly Trust Center
  slug: recurly-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
slug: recurly
tags:
- Subscriptions
- Billing
- Payments
- Recurring Revenue
- Invoicing
- Dunning
- Revenue Recognition
website: https://recurly.com
---
