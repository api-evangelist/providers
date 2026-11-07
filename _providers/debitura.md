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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.5
  scored_at: '2026-11-06'
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
  description: Manage webhook subscriptions and inspect the delivery event log. Create subscriptions to receive real-time notifications for case lifecycle events, payments, and chats. Use GET /webhooks/events to ver
  name: Debitura Webhooks API
  slug: debitura-webhooks-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: The OAuth API from Debitura — 1 operation(s) for oauth.
  name: Debitura O Auth API
  slug: debitura-oauth-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Test Cases
  name: Debitura Test Cases API
  slug: debitura-test-cases-api
- baseURL: https://customer-api.debitura.com
  baseurl_source: declared
  description: Webhooks
  name: Debitura Webhook Events API
  slug: debitura-webhook-events-api
artifact_total: 25
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
common:
- group: company
  title: ''
  type: Blog
  url: https://www.debitura.com/blog
- group: other
  href: https://artifacts.apis.io/debitura/capabilities/debitura-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/debitura-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://debitura.com
created: '2026-08-01'
description: 'Debitura is an API-first international debt collection platform covering cross-border B2B and B2C receivables. It publishes three separate public REST APIs, one per role in the network rather than one API with role-gated endpoints: the Customer API for creditors uploading invoices to collection and tracking cases, the Referral Partner API for platforms embedding collection as a referral and tracking revenue share, and the Collection Partner API for collection agencies operating cases on the platform. All three are OpenAPI 3.0.4, each on its own host, and each authenticates with an API key in the XApiKey header; the Customer API additionally accepts a bearer token, and the Referral Partner API exposes OAuth operations for minting them. Webhooks appear in all three, each with a paired test surface for exercising events before going live. Debitura publishes its own APIs.json at docs.debitura.com, which is how this profile was built.'
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.debitura.com over HTTP; 16 tools listed.
  name: Debitura MCP Server
  slug: debitura
modified: '2026-10-06'
name: Debitura
nav: Providers
network: true
overview: 'Debitura publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cases API, Clients API, Contracts API, and 17 more. Tagged areas include Debt Collection, Accounts Receivable, Debt Recovery, Fintech, and Payments.


  The Debitura catalog on APIs.io includes 1 Spectral governance ruleset.


  Debitura''s developer surface includes engineering blog and 2 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Debitura API Rules
  rule_count: 65
  severity_counts:
    error: 46
    hint: 0
    info: 2
    warn: 17
  slug: debitura-rules
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 57.2
    developer_ergonomics: 11.9
    discoverability: 70.0
    operational_transparency: 0.0
  previous_composite: 21.7
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 75.0
      total: 20
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 0.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/debitura/debitura-2026-08-07T164217.png
slug: debitura
tags:
- Debt Collection
- Accounts Receivable
- Debt Recovery
- Fintech
- Payments
- Invoicing
- Webhook
website: https://debitura.com
---
