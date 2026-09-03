---
agent_readiness:
  band: agent-aware
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-02'
api_count: 3
apis:
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Cases
  name: Debitura Cases API
  slug: debitura-cases-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Clients
  name: Debitura Clients API
  slug: debitura-clients-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Debt-collection contract status and signing URLs for your account.
  name: Debitura Contracts API
  slug: debitura-contracts-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Jurisdiction coverage — query which countries and debt types Debitura can collect in, and check case eligibility.
  name: Debitura Coverage API
  slug: debitura-coverage-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Divisions
  name: Debitura Divisions API
  slug: debitura-divisions-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Referral Partners
  name: Debitura Filter Options API
  slug: debitura-filteroptions-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: IngestionJobs
  name: Debitura Ingestion Jobs API
  slug: debitura-ingestionjobs-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Managed Cases
  name: Debitura Managed Cases API
  slug: debitura-managedcases-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Collection Partner Profile
  name: Debitura Me API
  slug: debitura-me-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: The OAuth API from Debitura — 1 operation(s) for oauth.
  name: Debitura O Auth API
  slug: debitura-oauth-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Payments
  name: Debitura Payments API
  slug: debitura-payments-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Cases
  name: Debitura Preview Cases API
  slug: debitura-previewcases-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Referral Partners
  name: Debitura Referral Partners API
  slug: debitura-referralpartners-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Reporting
  name: Debitura Reporting API
  slug: debitura-reporting-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Tasks
  name: Debitura Tasks API
  slug: debitura-tasks-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Test Cases
  name: Debitura Test Cases API
  slug: debitura-testcases-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Test Webhooks
  name: Debitura Test Webhooks API
  slug: debitura-testwebhooks-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Users
  name: Debitura Users API
  slug: debitura-users-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Webhooks
  name: Debitura Webhook Events API
  slug: debitura-webhookevents-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Manage webhook subscriptions and inspect the delivery event log. Create subscriptions to receive real-time notifications for case lifecycle events, payments, and chats. Use GET /webhooks/events to ver
  name: Debitura Webhooks API
  slug: debitura-webhooks-api
artifact_total: 23
collections:
- collection_type: open
  name: Debitura Collection Partner API
  slug: open-debitura-collection-partner-api
- collection_type: open
  name: Debitura Customer API
  slug: open-debitura-customer-api
- collection_type: open
  name: Debitura Referral Partner API
  slug: open-debitura-referral-partner-api
created: '2026-08-01'
description: 'Debitura is an API-first international debt collection platform covering cross-border B2B and B2C receivables. It publishes three separate public REST APIs, one per role in the network rather than one API with role-gated endpoints: the Customer API for creditors uploading invoices to collection and tracking cases, the Referral Partner API for platforms embedding collection as a referral and tracking revenue share, and the Collection Partner API for collection agencies operating cases on the platform. All three are OpenAPI 3.0.4, each on its own host, and each authenticates with an API key in the XApiKey header; the Customer API additionally accepts a bearer token, and the Referral Partner API exposes OAuth operations for minting them. Webhooks appear in all three, each with a paired test surface for exercising events before going live. Debitura publishes its own APIs.json at docs.debitura.com, which is how this profile was built.'
layout: provider
modified: '2026-08-01'
name: Debitura
nav: Providers
network: true
overview: Debitura publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Cases API, Clients API, Contracts API, and 17 more. Tagged areas include Debt Collection, Accounts Receivable, Debt Recovery, Fintech, and Payments.
random_paper: 8
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 77.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 55.9
    developer_ergonomics: 9.5
    discoverability: 70.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 0.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/debitura/refs/heads/main/screenshots/debitura-2026-08-07T164217.png
slug: debitura
tags:
- Debt Collection
- Accounts Receivable
- Debt Recovery
- Fintech
- Payments
- Invoicing
- Webhook
---
