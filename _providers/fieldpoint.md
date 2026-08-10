---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The Fieldpoint Data Transfer Service (FPDTS) is Fieldpoint's open REST API that enables data exchange between the Fieldpoint FSM platform and external enterprise systems. The API supports creating and
  name: Fieldpoint REST API (FPDTS)
  slug: fieldpoint-rest-api-fpdts
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fieldpoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fieldpoint.net
- group: docs
  title: ''
  type: Documentation
  url: https://fieldpoint.net/integrations/
- group: company
  title: ''
  type: Blog
  url: https://fieldpoint.net/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fieldpoint-service-applications
- group: other
  title: ''
  type: X
  url: https://twitter.com/fieldpointtalks
- group: operate
  title: ''
  type: Support
  url: https://fieldpointsupport.net/
- group: other
  title: ''
  type: CaseStudies
  url: https://fieldpoint.net/case-studies/
- group: commercial
  title: ''
  type: Plans
  url: plans/fieldpoint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fieldpoint-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fieldpoint-finops.yml
created: '2026-06-13'
description: Fieldpoint is an enterprise field service management (FSM) platform built for commercial contractors and service organizations across HVAC, electrical, fire inspection, security, medical equipment, and technology verticals. The platform covers the full service lifecycle including quoting, work order management, scheduling and dispatching, mobile technician apps, inventory tracking, service contracts, project costing, and customer management. Fieldpoint exposes an open REST API known as the Fieldpoint Data Transfer Service (FPDTS) that enables custom integrations with ERP, CRM, accounting, payroll, and workforce management systems. The platform ships pre-built connectors for Microsoft Dynamics GP/365, NetSuite, QuickBooks, Salesforce, WorkMarket, AvaTax, and more, while the FPDTS API allows enterprises to build bespoke integrations with any additional back-office system.
finops:
- name: Fieldpoint Finops
  service_category: ''
  slug: fieldpoint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fieldpoint.png
jsonld:
- class_count: 7
  name: Fieldpoint Context
  property_count: 14
  slug: fieldpoint-context
layout: provider
modified: '2026-06-13'
name: Fieldpoint
nav: Providers
network: true
overview: 'Fieldpoint publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Field Service Management, Work Orders, Scheduling, Dispatching, and Technician Management.


  The Fieldpoint catalog on APIs.io includes 1 JSON-LD context.


  Fieldpoint''s developer surface includes documentation, engineering blog, support, and 8 more developer resources.'
plans:
- name: Fieldpoint Plans Pricing
  plan_count: 2
  slug: fieldpoint-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 0
  name: Fieldpoint Rate Limits
  slug: fieldpoint-rate-limits
score:
  band: emerging
  composite: 20.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 17.7
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fieldpoint/refs/heads/main/screenshots/fieldpoint-2026-06-20T181152.png
security:
- kind: domain-security
  name: Fieldpoint Domain Security
  slug: fieldpoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fieldpoint
tags:
- Field Service Management
- Work Orders
- Scheduling
- Dispatching
- Technician Management
- Asset Tracking
- Service Contracts
- Mobile Workforce
- Inventory Management
- Enterprise Software
website: https://fieldpoint.net
---
