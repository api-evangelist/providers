---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Hostbill Agentic Access
  operation_count: 8
  slug: hostbill-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 8
apis:
- baseURL: https://yourinstance.hostbillapp.com/api2.php
  baseurl_source: declared
  description: The Accounts API from HostBill — 1 operation(s) for accounts.
  name: HostBill Accounts API
  slug: hostbill-accounts-api
- baseURL: https://yourinstance.hostbillapp.com/api2.php
  baseurl_source: declared
  description: The Admin API from HostBill — 1 operation(s) for admin.
  name: HostBill Admin API
  slug: hostbill-admin-api
- baseURL: https://yourinstance.hostbillapp.com/api2.php
  baseurl_source: declared
  description: The Clients API from HostBill — 1 operation(s) for clients.
  name: HostBill Clients API
  slug: hostbill-clients-api
- baseURL: https://yourinstance.hostbillapp.com/api2.php
  baseurl_source: declared
  description: The Domains API from HostBill — 1 operation(s) for domains.
  name: HostBill Domains API
  slug: hostbill-domains-api
- baseURL: https://yourinstance.hostbillapp.com/api2.php
  baseurl_source: declared
  description: The Invoices API from HostBill — 1 operation(s) for invoices.
  name: HostBill Invoices API
  slug: hostbill-invoices-api
- baseURL: https://yourinstance.hostbillapp.com/api2.php
  baseurl_source: declared
  description: The Orders API from HostBill — 1 operation(s) for orders.
  name: HostBill Orders API
  slug: hostbill-orders-api
- baseURL: https://yourinstance.hostbillapp.com/api2.php
  baseurl_source: declared
  description: The Tickets API from HostBill — 1 operation(s) for tickets.
  name: HostBill Tickets API
  slug: hostbill-tickets-api
- baseURL: https://yourinstance.hostbillapp.com/api2.php
  baseurl_source: declared
  description: The Transactions API from HostBill — 1 operation(s) for transactions.
  name: HostBill Transactions API
  slug: hostbill-transactions-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HostBill Admin Accounts API
  slug: open-hostbill-accounts-api
- collection_type: open
  name: HostBill Accounts Admin API
  slug: open-hostbill-admin-api
- collection_type: open
  name: HostBill Admin Accounts Clients API
  slug: open-hostbill-clients-api
- collection_type: open
  name: HostBill Admin Accounts Domains API
  slug: open-hostbill-domains-api
- collection_type: open
  name: HostBill Admin Accounts Invoices API
  slug: open-hostbill-invoices-api
- collection_type: open
  name: HostBill Admin Accounts Orders API
  slug: open-hostbill-orders-api
- collection_type: open
  name: HostBill Admin Accounts Tickets API
  slug: open-hostbill-tickets-api
- collection_type: open
  name: HostBill Admin Accounts Transactions API
  slug: open-hostbill-transactions-api
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
random_paper: 4
rate_limits:
- limit_count: 5
  name: Hostbill Rate Limits
  slug: hostbill-rate-limits
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 45.4
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
