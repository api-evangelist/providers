---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.llm-discovery-api.com/functions/v1/llm-discovery/public
  baseurl_source: declared
  description: The AI Discovery API from Payem — 1 operation(s) for ai discovery.
  name: Payem AI Discovery API
  slug: payem-ai-discovery-api
- baseURL: https://api.llm-discovery-api.com/functions/v1/llm-discovery/public
  baseurl_source: declared
  description: The Business API from Payem — 1 operation(s) for business.
  name: Payem Business API
  slug: payem-business-api
- baseURL: https://api.llm-discovery-api.com/functions/v1/llm-discovery/public
  baseurl_source: declared
  description: The Categories API from Payem — 1 operation(s) for categories.
  name: Payem Categories API
  slug: payem-categories-api
- baseURL: https://api.llm-discovery-api.com/functions/v1/llm-discovery/public
  baseurl_source: declared
  description: The Faq API from Payem — 1 operation(s) for faq.
  name: Payem Faq API
  slug: payem-faq-api
- baseURL: https://api.llm-discovery-api.com/functions/v1/llm-discovery/public
  baseurl_source: declared
  description: The Qa API from Payem — 5 operation(s) for qa.
  name: Payem Qa API
  slug: payem-qa-api
- baseURL: https://api.llm-discovery-api.com/functions/v1/llm-discovery/public
  baseurl_source: declared
  description: The Search API from Payem — 1 operation(s) for search.
  name: Payem Search API
  slug: payem-search-api
- baseURL: https://api.llm-discovery-api.com/functions/v1/llm-discovery/public
  baseurl_source: declared
  description: The Testimonials API from Payem — 1 operation(s) for testimonials.
  name: Payem Testimonials API
  slug: payem-testimonials-api
artifact_total: 13
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/payem-ai-discovery-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/payem-mcp.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/payem-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.payem.co/
- group: company
  title: ''
  type: Blog
  url: https://www.payem.co/blog
- group: operate
  title: ''
  type: Support
  url: https://www.payem.co/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.payem.co/faq
- group: start
  title: ''
  type: Login
  url: https://app.payemcard.com/login
- group: start
  title: ''
  type: SignUp
  url: https://www.payem.co/lp/personalized-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.payem.co/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.payem.co/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.payem.co/legal/security-and-compliance
- group: agent
  title: ''
  type: WellKnown
  url: well-known/payem-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/payem-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/payem-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/payem-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payem-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/payem-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/payem-plans-pricing.yml
created: '2026-08-26'
description: PayEm is a global spend management and procurement platform that automates the request-to-reconciliation process for finance, procurement, HR and operations teams. The product covers intake requests and agile approval workflows, virtual and physical corporate cards (including an American Express program), AP automation with AI/OCR invoice processing, purchase-order creation and matching, vendor onboarding, budget control, expense tracking, multi-subsidiary management, cross-border payments, real-time reconciliation and an audit trail, with native connectors into NetSuite, QuickBooks Online, Priority ERP, Xero, HRIS systems, TravelPerk and Slack. Founded in 2019 and operating from San Francisco and Tel Aviv, PayEm holds SOC 1 and SOC 2 Type II attestations audited by EY. PayEm publishes no public developer program - no developer portal, API reference, SDK, webhook catalog or machine-readable product contract is reachable without a sales conversation. The only machine-readable
  contract served from payem.co is an AI-discovery content API operated on PayEm's behalf by LightSite.ai, linked from PayEm's own robots.txt and reachable via a 308 from https://www.payem.co/.well-known/openapi.json.
image: https://www.payem.co/icon.svg
jsonld:
- class_count: 0
  name: Payem Organization Context
  property_count: 0
  slug: payem-organization
layout: provider
modified: '2026-08-26'
name: Payem
nav: Providers
network: true
overview: 'Payem publishes 7 APIs on the [APIs.io](https://apis.io/) network, including AI Discovery API, Business API, Categories API, and 4 more. Tagged areas include Company, Spend Management, Procurement, Accounts Payable, and Corporate Cards.


  The Payem catalog on APIs.io includes 1 JSON-LD context.


  Payem''s developer surface includes engineering blog, support, signup flow, and 16 more developer resources.'
plans:
- name: Payem Plans Pricing
  plan_count: 0
  slug: payem-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Payem Rate Limits
  slug: payem-rate-limits
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 65.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 52.7
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 41.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payem/refs/heads/main/screenshots/payem-2026-09-02T150919.png
security:
- kind: authentication
  name: Payem Authentication
  slug: payem-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Payem Domain Security
  slug: payem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Payem Trust Center
  slug: payem-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, GDPR, CCPA
slug: payem
tags:
- Company
- Spend Management
- Procurement
- Accounts Payable
- Corporate Cards
- Expense Management
- Financial Operations
- Invoice Processing
- Fintech
- ERP Integration
website: https://www.payem.co/
---
