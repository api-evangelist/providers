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
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Supermove Agentic Access
  operation_count: 1
  slug: supermove-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://help.supermove.com/hc/en-us/articles/36934839868692-Developer-API-New-Lead-Endpoint
  baseurl_source: declared
  description: The Supermove Developer API New Lead Endpoint API from Supermove — 1 operation(s) for supermove developer api new lead endpoint.
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
screenshot: https://raw.githubusercontent.com/api-evangelist/supermove/refs/heads/main/screenshots/supermove-2026-09-02T161244.png
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
