---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 49
  human_in_the_loop: 1
  name: Wove Agentic Access
  operation_count: 85
  slug: wove-agentic-access
  summary_line: 85 operations · 49 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: OAuth 2.0 authentication endpoints
  name: Wove Authentication API
  slug: wove-authentication-api
- description: Document management within shipments
  name: Wove Documents API
  slug: wove-documents-api
- description: Query Bank management - add/remove sources from your rate query pool
  name: Wove Query Bank API
  slug: wove-query-bank-api
- description: Query freight rates from your Query Bank
  name: Wove Rates API
  slug: wove-rates-api
- description: Shipment management operations
  name: Wove Shipments API
  slug: wove-shipments-api
- description: Rate sheet source management - upload, process, and query status
  name: Wove Sources API
  slug: wove-sources-api
- description: Duty and tariff rate lookup by HS code with customer-specific overrides
  name: Wove Tariffs API
  slug: wove-tariffs-api
- description: Test endpoints for API validation
  name: Wove Testing API
  slug: wove-testing-api
- description: TMS organization management - CRUD and bulk JSONL import
  name: Wove TMS Organizations API
  slug: wove-tms-organizations-api
- description: Webhook management for async notifications
  name: Wove Webhooks API
  slug: wove-webhooks-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wove-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wove-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wove-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wove-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wove-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wove.com
created: '2026-07-17'
description: Wove is a company surfaced as a portfolio company of 500-global and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wove.png
layout: provider
modified: '2026-07-17'
name: Wove
nav: Providers
network: true
overview: 'Wove publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Documents API, Query Bank API, and 7 more. Tagged areas include Company.


  Wove''s developer surface includes authentication and 5 more developer resources.'
random_paper: 44
rate_limits:
- limit_count: 2
  name: Wove Rate Limits
  slug: wove-rate-limits
scopes:
- name: Wove Scopes
  scope_count: 9
  slug: wove-scopes
  summary_line: 9 scopes · clientCredentials
score:
  band: emerging
  composite: 26.2
  delta: 0.7
  facets:
    commercial_clarity: 7.9
    contract_quality: 56.7
    developer_ergonomics: 10.9
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Wove Authentication
  slug: wove-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wove Domain Security
  slug: wove-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Wove Vulnerability Disclosure
  slug: wove-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Wove Trust Center
  slug: wove-trust-center
  summary_line: SOC 2
slug: wove
tags:
- Company
website: https://wove.com
---
