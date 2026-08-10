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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Hostbill Agentic Access
  operation_count: 8
  slug: hostbill-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 8
apis:
- description: The Accounts API from HostBill — 1 operation(s) for accounts.
  name: HostBill Accounts API
  slug: hostbill-accounts-api
- description: The Admin API from HostBill — 1 operation(s) for admin.
  name: HostBill Admin API
  slug: hostbill-admin-api
- description: The Clients API from HostBill — 1 operation(s) for clients.
  name: HostBill Clients API
  slug: hostbill-clients-api
- description: The Domains API from HostBill — 1 operation(s) for domains.
  name: HostBill Domains API
  slug: hostbill-domains-api
- description: The Invoices API from HostBill — 1 operation(s) for invoices.
  name: HostBill Invoices API
  slug: hostbill-invoices-api
- description: The Orders API from HostBill — 1 operation(s) for orders.
  name: HostBill Orders API
  slug: hostbill-orders-api
- description: The Tickets API from HostBill — 1 operation(s) for tickets.
  name: HostBill Tickets API
  slug: hostbill-tickets-api
- description: The Transactions API from HostBill — 1 operation(s) for transactions.
  name: HostBill Transactions API
  slug: hostbill-transactions-api
artifact_total: 16
collections:
- collection_type: open
  name: HostBill Admin API
  slug: open-hostbill
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hostbill-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hostbill-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hostbill-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hostbill-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hostbill
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hostbill
- group: company
  title: ''
  type: Website
  url: https://hostbillapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hostbillapp.com/features/
- group: operate
  title: ''
  type: Support
  url: https://hostbillapp.com/support/
- group: company
  title: ''
  type: Blog
  url: https://blog.hostbillapp.com/feed/
created: '2025-02-09'
description: HostBill is a comprehensive billing and automation software for web hosting providers, domain registrars, and online service companies. HostBill provides an Admin API that enables custom applications to call HostBill functions remotely via HTTP protocol or from HostBill modules.
finops:
- name: Hostbill Finops
  service_category: API
  slug: hostbill-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hostbill.png
layout: provider
modified: '2026-05-19'
name: HostBill
nav: Providers
network: true
overview: 'HostBill publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Admin API, Clients API, and 5 more. Tagged areas include Automation, Billing, Domain Registration, and Web Hosting.


  HostBill''s developer surface includes authentication, documentation, support, engineering blog, and 6 more developer resources.'
plans:
- name: Hostbill Plans Pricing
  plan_count: 3
  slug: hostbill-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Hostbill Rate Limits
  slug: hostbill-rate-limits
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.6
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hostbill/refs/heads/main/screenshots/hostbill-2026-06-20T182839.png
security:
- kind: authentication
  name: Hostbill Authentication
  slug: hostbill-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Hostbill Domain Security
  slug: hostbill-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hostbill Vulnerability Disclosure
  slug: hostbill-vulnerability-disclosure
  summary_line: disclosure policy published
slug: hostbill
tags:
- Automation
- Billing
- Domain Registration
- Web Hosting
website: https://hostbillapp.com/
---
