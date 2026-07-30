---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: 'Tracks bottles, ingredients, and SKUs with counts, par levels, and variance across the venue''s item catalog. Exposed in the WISK product and apps; not published as a public, self-serve developer API. '
  name: WISK Inventory & Items API
  slug: wisk-ai-inventory-items-api
- description: Organizes inventory, users, and reporting per venue (location) for single sites and multi-location groups. Surfaced in the WISK platform; not published as a public, self-serve developer API.
  name: WISK Venues API
  slug: wisk-ai-venues-api
- description: Captures, AI-processes, and reconciles supplier invoices against purchases and pricing to track cost of goods. Available in the WISK product; not published as a public, self-serve developer API.
  name: WISK Invoices API
  slug: wisk-ai-invoices-api
- description: Partner-gated integration for POS providers to push sales data (POS code or item name, quantity sold, net sales) into WISK customer accounts via a documented Public Sales upload flow. WISK can alterna
  name: WISK POS Integration (Public Sales Upload) API
  slug: wisk-ai-pos-integration-api
- description: No public, documented webhook or event-subscription surface is published by WISK as of this catalog date. Event-driven exchange with POS partners is arranged through WISK's partner integration process
  name: WISK Webhooks
  slug: wisk-ai-webhooks
artifact_total: 10
collections:
- collection_type: open
  name: WISK API
  slug: open-wisk-ai
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wisk-ai-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wisk
- group: company
  title: ''
  type: Website
  url: https://www.wisk.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://help.wisk.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/wisk-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wisk-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wisk-ai-finops.yml
created: '2026-06-21'
description: WISK is a bar, restaurant, and hospitality inventory and cost-management platform that tracks items, counts inventory across venues, scans and reconciles supplier invoices, and integrates with 60+ POS systems to compare theoretical vs. actual usage. WISK's programmatic surface is partner-gated - a documented Public Sales upload API lets POS providers and partners push sales data into WISK, and customer API access is offered on the top (Premium) plan. There is no public, self-serve developer portal or published OpenAPI as of this catalog date.
finops:
- name: Wisk Ai Finops
  service_category: Management and Governance
  slug: wisk-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wisk-ai.png
layout: provider
modified: '2026-06-21'
name: WISK
nav: Providers
network: true
overview: 'WISK publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Inventory & Items API, Venues API, Invoices API, and 1 more. Tagged areas include Inventory, Restaurant, Bar, Hospitality, and Cost Management.


  WISK''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Wisk Ai Plans Pricing
  plan_count: 5
  slug: wisk-ai-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 2
  name: Wisk Ai Rate Limits
  slug: wisk-ai-rate-limits
score:
  band: emerging
  composite: 26.9
  delta: -3.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Wisk Ai Domain Security
  slug: wisk-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wisk-ai
tags:
- Inventory
- Restaurant
- Bar
- Hospitality
- Cost Management
- POS Integration
website: https://www.wisk.ai/
---
