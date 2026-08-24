---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: Provides access to the Litify legal operating system via the Salesforce REST API. Supports managing matters, intakes, documents, tasks, time tracking, billing, and client communications for law firms.
  name: Litify Salesforce REST API
  slug: litify-salesforce-rest-api
- description: Provides access to Litify's Docrio document management layer, enabling integrators to create, retrieve, and manage documents and folders associated with legal matters. Documents uploaded via integrati
  name: Litify Docrio API
  slug: litify-docrio-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/litify-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/litify/refs/heads/main/plans/litify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/litify/refs/heads/main/rate-limits/litify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/litify/refs/heads/main/finops/litify-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.litify.com/
- group: company
  title: ''
  type: Blog
  url: https://www.litify.com/blog
- group: commercial
  title: ''
  type: LegalTermsOfService
  url: https://www.litify.com/legal/litify-api-integration-agreement
- group: commercial
  title: ''
  type: Pricing
  url: https://www.litify.com/pricing
created: '2026-06-13'
description: Litify is a legal operating system built on Salesforce that provides REST APIs for managing matters, intakes, documents, tasks, time tracking, billing, and client communications for law firms and legal departments. Integrators access Litify functionality via the Salesforce REST API and the Litify Docrio API under the terms of the Litify API Integration Agreement.
finops:
- name: Litify Finops
  service_category: ''
  slug: litify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/litify.png
jsonld:
- class_count: 10
  name: Litify Context
  property_count: 9
  slug: litify-context
layout: provider
modified: '2026-06-13'
name: Litify
nav: Providers
network: true
overview: 'Litify publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Law Firms, Matter Management, Intake Management, and Document-Management.


  The Litify catalog on APIs.io includes 1 JSON-LD context.


  Litify''s developer surface includes engineering blog, pricing, and 6 more developer resources.'
plans:
- name: Litify Plans Pricing
  plan_count: 2
  slug: litify-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Litify Rate Limits
  slug: litify-rate-limits
score:
  band: emerging
  composite: 18.1
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/litify/refs/heads/main/screenshots/litify-2026-06-20T184607.png
security:
- kind: domain-security
  name: Litify Domain Security
  slug: litify-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: litify
tags:
- Legal
- Law Firms
- Matter Management
- Intake Management
- Document-Management
- Time Tracking
- Billing
- Client Communications
- Legal Technology
- Salesforce
website: https://www.litify.com/
---
