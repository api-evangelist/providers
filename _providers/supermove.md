---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Supermove Agentic Access
  operation_count: 1
  slug: supermove-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Supermove Developer API New Lead Endpoint API from Supermove — 1 operation(s) for supermove developer api new lead endpoint.
  name: Supermove Supermove Developer API New Lead Endpoint API
  slug: supermove-supermove-developer-api-new-lead-endpoint-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Supermove Developer API - New Lead Endpoint Supermove Developer API New Lead Endpoint API
  slug: open-supermove-supermove-developer-api-new-lead-endpoint-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/supermove-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supermove-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.supermove.com/blog
created: '2026-07-04'
description: Supermove is a cloud-based moving company operating system that manages the full job lifecycle for residential and commercial movers - sales and booking, estimating, dispatch and operations, a field crew app, storage, payments, and accounting. Supermove's public developer surface is intentionally narrow. Rather than a general REST platform API for jobs, customers, estimates, or invoices, the documented public integration is a single inbound "Developer API" - a per-account New Lead Endpoint. Each Supermove account exposes its own unique webhook URL, and upstream lead providers or a company's own website POST lead data as JSON (Content-Type application/json) to that URL to create leads/projects. The endpoint URL itself scopes the payload to the account, so no separate API keys or organization identifiers are used. Broader platform data and product integrations (QuickBooks Online, HubSpot, Stripe, Google Calendar, Zapier, Thumbtack, and other lead providers) are handled through
  Supermove's own connectors rather than a general outbound public API. Access is not self-serve; Supermove is sold via demo and custom quote.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/supermove.png
layout: provider
modified: '2026-07-04'
name: Supermove
nav: Providers
network: true
overview: 'Supermove publishes 1 API on the [APIs.io](https://apis.io/) network: Supermove Developer API New Lead Endpoint API. Tagged areas include Moving, Moving Company Software, Logistics, Field Service, and Lead Management.


  Supermove''s developer surface includes engineering blog and 2 more developer resources.'
plans:
- name: Supermove Plans Pricing
  plan_count: 1
  slug: supermove-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 12.4
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Supermove Domain Security
  slug: supermove-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: supermove
tags:
- Moving
- Moving Company Software
- Logistics
- Field Service
- Lead Management
- Dispatch
- Webhook
---
