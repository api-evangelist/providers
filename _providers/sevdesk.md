---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Sevdesk Agentic Access
  operation_count: 30
  slug: sevdesk-agentic-access
  summary_line: 30 operations · 13 acting
api_count: 1
apis:
- baseURL: https://my.sevdesk.de/api/v1
  baseurl_source: declared
  description: Bank and clearing check accounts.
  name: sevdesk CheckAccount API
  slug: sevdesk-checkaccount-api
- baseURL: https://my.sevdesk.de/api/v1
  baseurl_source: declared
  description: Transactions booked against a check account.
  name: sevdesk CheckAccountTransaction API
  slug: sevdesk-checkaccounttransaction-api
- baseURL: https://my.sevdesk.de/api/v1
  baseurl_source: declared
  description: Contacts - customers, suppliers, and other business partners.
  name: sevdesk Contact API
  slug: sevdesk-contact-api
- baseURL: https://my.sevdesk.de/api/v1
  baseurl_source: declared
  description: Outgoing invoices and their lifecycle.
  name: sevdesk Invoice API
  slug: sevdesk-invoice-api
- baseURL: https://my.sevdesk.de/api/v1
  baseurl_source: declared
  description: Orders, quotations, and packing lists.
  name: sevdesk Order API
  slug: sevdesk-order-api
- baseURL: https://my.sevdesk.de/api/v1
  baseurl_source: declared
  description: Parts / articles with stock (inventory).
  name: sevdesk Part API
  slug: sevdesk-part-api
- baseURL: https://my.sevdesk.de/api/v1
  baseurl_source: declared
  description: Tags and tag relations used to label resources.
  name: sevdesk Tag API
  slug: sevdesk-tag-api
- baseURL: https://my.sevdesk.de/api/v1
  baseurl_source: declared
  description: Vouchers (receipts) used for expense and revenue bookkeeping.
  name: sevdesk Voucher API
  slug: sevdesk-voucher-api
- baseURL: https://my.sevdesk.de/api/v1
  baseurl_source: declared
  description: Credit notes issued to contacts.
  name: sevdesk Credit Note API
  slug: sevdesk-credit-note-api
artifact_total: 26
collections:
- collection_type: open
  name: sevdesk CheckAccount API
  slug: open-sevdesk-checkaccount-api
- collection_type: open
  name: sevdesk CheckAccount CheckAccountTransaction API
  slug: open-sevdesk-checkaccounttransaction-api
- collection_type: open
  name: sevdesk CheckAccount Contact API
  slug: open-sevdesk-contact-api
- collection_type: open
  name: sevdesk CheckAccount CreditNote API
  slug: open-sevdesk-creditnote-api
- collection_type: open
  name: sevdesk CheckAccount Invoice API
  slug: open-sevdesk-invoice-api
- collection_type: open
  name: sevdesk CheckAccount Order API
  slug: open-sevdesk-order-api
- collection_type: open
  name: sevdesk CheckAccount Part API
  slug: open-sevdesk-part-api
- collection_type: open
  name: sevdesk CheckAccount Tag API
  slug: open-sevdesk-tag-api
- collection_type: open
  name: sevdesk CheckAccount Voucher API
  slug: open-sevdesk-voucher-api
- collection_type: open
  name: sevdesk API
  slug: open-sevdesk
common:
- group: other
  href: https://artifacts.apis.io/sevdesk/capabilities/sevdesk-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sevdesk-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/sevdesk/agentic-access/sevdesk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sevdesk-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sevdesk/security/sevdesk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sevdesk-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sevdesk/authentication/sevdesk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sevdesk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sevdesk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sevdesk
- group: company
  title: ''
  type: Website
  url: https://sevdesk.de
- group: docs
  title: ''
  type: Documentation
  url: https://api.sevdesk.de/
- group: commercial
  href: https://artifacts.apis.io/sevdesk/plans/sevdesk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sevdesk-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sevdesk/rate-limits/sevdesk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sevdesk-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sevdesk/finops/sevdesk-finops.yml
  title: ''
  type: FinOps
  url: finops/sevdesk-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://tech.sevdesk.com/
created: '2026-07-12'
description: sevdesk is a German cloud accounting, invoicing, and bookkeeping platform for freelancers and small businesses. Its RESTful API (base https://my.sevdesk.de/api/v1) exposes everything the web application does - contacts, invoices, orders, credit notes, vouchers (receipts), bank check accounts and transactions, parts (inventory), tags, plus DATEV and CSV exports - authenticated with a per-administrator API token passed in the Authorization header. Nested resources can be pulled in with the embed query parameter.
finops:
- has_sources: true
  method: generated
  name: Sevdesk Finops
  primary_unit: ''
  service_category: Business Software - Accounting and Invoicing
  slug: sevdesk-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sevdesk.png
layout: provider
modified: '2026-07-12'
name: sevdesk
nav: Providers
network: true
overview: 'sevdesk publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including CheckAccount API, CheckAccountTransaction API, Contact API, and 6 more. Tagged areas include Accounting, Invoicing, Bookkeeping, Finance, and Germany.


  The sevdesk catalog on APIs.io includes 1 Spectral governance ruleset.


  sevdesk''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Sevdesk Plans Pricing
  plan_count: 5
  slug: sevdesk-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Sevdesk Rate Limits
  slug: sevdesk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: sevdesk API Rules
  rule_count: 61
  severity_counts:
    error: 55
    hint: 0
    info: 2
    warn: 4
  slug: sevdesk-rules
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 51.5
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 29.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sevdesk/sevdesk-2026-09-02T155034.png
security:
- kind: authentication
  name: Sevdesk Authentication
  slug: sevdesk-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sevdesk Domain Security
  slug: sevdesk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sevdesk
tags:
- Accounting
- Invoicing
- Bookkeeping
- Finance
- Germany
- Vouchers
- Contacts
- Software-as-a-Service
- ERP
- Financial Software
website: https://sevdesk.de
---
