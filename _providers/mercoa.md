---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Mercoa Agentic Access
  operation_count: 48
  slug: mercoa-agentic-access
  summary_line: 48 operations · 31 acting
api_count: 1
apis:
- description: 'REST API and SDK suite for embedding accounts payable and accounts receivable into vertical SaaS platforms. Exposes resources for entities, users, invoices, bills, vendors, approval policies, payment '
  name: Mercoa API
  slug: mercoa-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Entities API from Mercoa — 7 operation(s) for entities.
  name: Mercoa Entities API
  slug: mercoa-entities-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Entity Groups API from Mercoa — 5 operation(s) for entity groups.
  name: Mercoa Entity Groups API
  slug: mercoa-entity-groups-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Invoice Templates API from Mercoa — 3 operation(s) for invoice templates.
  name: Mercoa Invoice Templates API
  slug: mercoa-invoice-templates-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Invoices API from Mercoa — 8 operation(s) for invoices.
  name: Mercoa Invoices API
  slug: mercoa-invoices-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The OCR API from Mercoa — 3 operation(s) for ocr.
  name: Mercoa OCR API
  slug: mercoa-ocr-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Organization API from Mercoa — 1 operation(s) for organization.
  name: Mercoa Organization API
  slug: mercoa-organization-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Payment Gateway API from Mercoa — 2 operation(s) for payment gateway.
  name: Mercoa Payment Gateway API
  slug: mercoa-payment-gateway-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Payment Methods API from Mercoa — 3 operation(s) for payment methods.
  name: Mercoa Payment Methods API
  slug: mercoa-payment-methods-api
- baseURL: https://api.mercoa.com
  baseurl_source: declared
  description: The Transactions API from Mercoa — 2 operation(s) for transactions.
  name: Mercoa Transactions API
  slug: mercoa-transactions-api
artifact_total: 28
collections:
- collection_type: open
  name: Mercoa Entities API
  slug: open-mercoa-entities-api
- collection_type: open
  name: Mercoa Entities Entity Groups API
  slug: open-mercoa-entity-groups-api
- collection_type: open
  name: Mercoa Entities Invoice Templates API
  slug: open-mercoa-invoice-templates-api
- collection_type: open
  name: Mercoa Entities Invoices API
  slug: open-mercoa-invoices-api
- collection_type: open
  name: Mercoa Entities OCR API
  slug: open-mercoa-ocr-api
- collection_type: open
  name: Mercoa Entities Organization API
  slug: open-mercoa-organization-api
- collection_type: open
  name: Mercoa Entities Payment Gateway API
  slug: open-mercoa-payment-gateway-api
- collection_type: open
  name: Mercoa Entities Payment Methods API
  slug: open-mercoa-payment-methods-api
- collection_type: open
  name: Mercoa Entities Transactions API
  slug: open-mercoa-transactions-api
- collection_type: open
  name: Mercoa API
  slug: open-mercoa
common:
- group: commercial
  href: https://artifacts.apis.io/mercoa/plans/mercoa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mercoa-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mercoa/rate-limits/mercoa-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mercoa-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mercoa/finops/mercoa-finops.yml
  title: ''
  type: FinOps
  url: finops/mercoa-finops.yml
- group: other
  href: https://artifacts.apis.io/mercoa/capabilities/mercoa-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mercoa-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/mercoa/agentic-access/mercoa-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mercoa-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mercoa/security/mercoa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mercoa-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mercoa/authentication/mercoa-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mercoa-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mercoa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mercoa.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/mercoa-finance
- group: start
  title: ''
  type: Signup
  url: https://mercoa.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.mercoa.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://mercoa.com/blog
created: '2026-05-23'
description: Mercoa is an embedded AP and AR platform that vertical SaaS companies use to launch AI-powered BillPay and invoicing inside their own products. The platform handles bill ingestion via intelligent email inboxes, vendor onboarding, approval workflows, payment scheduling, branded invoicing, AI-driven collection reminders, and disbursement across ACH, check, virtual card, and BNPL. Builders can choose React components, a hosted iFrame, or pure REST APIs and SDKs depending on how much UI control they need. Mercoa publishes official SDKs for TypeScript, Python, and Java and is backed by Y Combinator. Customers monetize Mercoa through per-user pricing, transaction fees, and premium payment option margins.
finops:
- has_sources: false
  method: generated
  name: Mercoa Finops
  primary_unit: ''
  service_category: API
  slug: mercoa-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mercoa.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.mercoa.com over HTTP.
  name: Mercoa MCP Server
  slug: mercoa
modified: '2026-05-23'
name: Mercoa
nav: Providers
network: true
overview: 'Mercoa publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Entities API, Entity Groups API, Invoice Templates API, and 7 more. Tagged areas include Mercoa, Embedded Finance, Accounts Payable, Accounts Receivable, and Bill Pay.


  The Mercoa catalog on APIs.io includes 1 Spectral governance ruleset.


  Mercoa''s developer surface includes authentication, documentation, signup flow, engineering blog, and 9 more developer resources.'
plans:
- name: Mercoa Plans Pricing
  plan_count: 1
  slug: mercoa-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Mercoa Rate Limits
  slug: mercoa-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Mercoa API Rules
  rule_count: 51
  severity_counts:
    error: 42
    hint: 0
    info: 2
    warn: 7
  slug: mercoa-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 18.4
    contract_governance: 13.6
    contract_quality: 49.6
    developer_ergonomics: 42.9
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 18.2
      total: 66
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 10.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/mercoa/mercoa-2026-06-20T185210.png
security:
- kind: authentication
  name: Mercoa Authentication
  slug: mercoa-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mercoa Domain Security
  slug: mercoa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mercoa
tags:
- Mercoa
- Embedded Finance
- Accounts Payable
- Accounts Receivable
- Bill Pay
- Invoicing
- Payments
- Vertical SaaS
- Vendors
- Approvals
- Disbursements
- Virtual Cards
website: https://mercoa.com/
---
