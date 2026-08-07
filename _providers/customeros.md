---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Customeros Agentic Access
  operation_count: 2
  slug: customeros-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 3
apis:
- description: Documented synchronous REST API on the customeros.ai cloud (api.customeros.ai/customerbase/v1), authenticated with the X-CUSTOMER-OS-API-KEY header. Includes organization endpoints such as POST /organ
  name: CustomerOS Customerbase REST API
  slug: customeros-customerbase-rest-api
- description: Client-side JavaScript tracker, installed via a script tag behind a customer-hosted reverse-proxy CNAME, that captures page views and custom events and matches visitor IPs to companies. It is a script
  name: CustomerOS Website Tracker
  slug: customeros-website-tracker
- description: Single GraphQL endpoint for all CustomerOS operations.
  name: CustomerOS GraphQL API
  slug: customeros-graphql-api
artifact_total: 11
collections:
- collection_type: open
  name: CustomerOS GraphQL API
  slug: open-customeros
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/customeros-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/customeros-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/customeros-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openline-ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/customeros
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/customeros
- group: company
  title: ''
  type: Website
  url: https://customeros.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.customeros.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/customeros-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/customeros-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/customeros-finops.yml
created: '2026-06-20'
description: CustomerOS (formerly Openline) is an open-source go-to-market / revenue platform for B2B SaaS. Its core open-source application server, customer-os-api, exposes a single GraphQL endpoint (POST /query) covering organizations, contacts, opportunities, contracts, invoices, interactions, and timeline events. The commercial cloud (customeros.ai) adds a documented REST "Customerbase" API and a JavaScript website visitor tracker, with broader access granted on a per-request basis.
finops:
- name: Customeros Finops
  service_category: Customer Relationship Management
  slug: customeros-finops
graphqls:
- description: Representative GraphQL schema for the [CustomerOS](https://customeros.ai/) (formerly Openline)
  name: CustomerOS GraphQL Schema
  slug: customeros-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/customeros.png
layout: provider
modified: '2026-06-20'
name: CustomerOS
nav: Providers
network: true
overview: 'CustomerOS publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include CRM, Revenue, Go-To-Market, GraphQL, and Open Source.


  CustomerOS''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Customeros Plans Pricing
  plan_count: 2
  slug: customeros-plans-pricing
random_paper: 91
rate_limits:
- limit_count: 2
  name: Customeros Rate Limits
  slug: customeros-rate-limits
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/customeros/refs/heads/main/screenshots/customeros-2026-06-20T175351.png
security:
- kind: authentication
  name: Customeros Authentication
  slug: customeros-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Customeros Domain Security
  slug: customeros-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: customeros
tags:
- CRM
- Revenue
- Go-To-Market
- GraphQL
- Open Source
website: https://customeros.ai
---
