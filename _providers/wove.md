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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 49
  human_in_the_loop: 1
  name: Wove Agentic Access
  operation_count: 85
  slug: wove-agentic-access
  summary_line: 85 operations · 49 acting · 1 human-in-the-loop
api_count: 1
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
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wove External Authentication API
  slug: open-wove-authentication-api
- collection_type: open
  name: Wove External Authentication Documents API
  slug: open-wove-documents-api
- collection_type: open
  name: Wove External Authentication Query Bank API
  slug: open-wove-query-bank-api
- collection_type: open
  name: Wove External Authentication Rates API
  slug: open-wove-rates-api
- collection_type: open
  name: Wove External Authentication Shipments API
  slug: open-wove-shipments-api
- collection_type: open
  name: Wove External Authentication Sources API
  slug: open-wove-sources-api
- collection_type: open
  name: Wove External Authentication Tariffs API
  slug: open-wove-tariffs-api
- collection_type: open
  name: Wove External Authentication Testing API
  slug: open-wove-testing-api
- collection_type: open
  name: Wove External Authentication TMS Organizations API
  slug: open-wove-tms-organizations-api
- collection_type: open
  name: Wove External Authentication Webhooks API
  slug: open-wove-webhooks-api
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
random_paper: 8
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
  composite: 25.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 57.7
    developer_ergonomics: 11.9
    discoverability: 38.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
