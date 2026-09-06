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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: Remote, OAuth 2.0 protected Model Context Protocol server (Streamable HTTP, MCP spec 2025-03-26) exposing 44 tools that let an AI assistant read a Lili business customer's account summary, transaction
  name: Lili MCP Server
  slug: lili-mcp-server
- baseURL: https://prod.lili.co
  baseurl_source: declared
  description: The Lili API from Lili — 8 operation(s) for lili.
  name: Lili Lili API
  slug: lili-lili-api
artifact_total: 10
asyncapis:
- description: ''
  name: Lili Webhooks
  slug: lili-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/lili-application-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lili-customer-management-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lili-webhooks-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://lili.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.lili.co/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.lili.co/lili-apis
- group: docs
  title: ''
  type: APIReference
  url: https://dev.lili.co/lili-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.lili.co/guides/lili-quick-start
- group: operate
  title: ''
  type: Support
  url: https://lili.co/customer-support
- group: company
  title: ''
  type: Blog
  url: https://lili.co/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://lili.co/feed
- group: commercial
  title: ''
  type: Pricing
  url: https://lili.co/plans
- group: start
  title: ''
  type: SignUp
  url: https://lili.co/business-banking
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lili.co/legal-documents/lili-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lili.co/legal-documents/lili-privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://dev.lili.co/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lili-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lili-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lili-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lili-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lili-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lili-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lili-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lili-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lili-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/lili-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lili-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/lili-decline-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lili-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lili-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/lili-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/lili-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lili-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lili-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lili-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lili-domain-security.yml
created: '2026-08-25'
description: 'Lili is a U.S. small-business banking and financial-management platform (banking services provided by Sunrise Banks, N.A., Member FDIC) that combines a business checking account, high-yield savings, a Visa debit card, invoicing, bill pay, expense categorization, tax buckets and business-credit products for LLCs, corporations, partnerships, sole proprietors and non-profits. For developers Lili publishes the Lili Connect platform at dev.lili.co: an Application API that creates a pre-filled business bank account application and returns a hosted or embeddable onboarding URL, a Customer Management API for payment notification and bank-letter retrieval, a Webhooks API for onboarding lifecycle events, and a remote, OAuth 2.0 protected MCP server at mcp.lili.co that exposes 44 read-oriented tools over balances, transactions, invoices, bills, suppliers, cards, tax estimates, statements and business profile for AI assistants and accountants.'
image: https://lili.co/wp-content/uploads/2025/05/meta-preview.png
layout: provider
mcp_servers:
- description: ''
  name: Lili MCP Server
  slug: lili-mcp-server
- description: ''
  name: Lili MCP Server
  slug: lili-mcp-server-2
modified: '2026-08-25'
name: Lili
nav: Providers
network: true
overview: 'Lili publishes 1 API on the [APIs.io](https://apis.io/) network: Lili API. Tagged areas include Banking, Business Banking, Financial-Services, Fintech, and Embedded Finance.


  The Lili catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lili''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Lili Plans Pricing
  plan_count: 4
  slug: lili-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Lili Rate Limits
  slug: lili-rate-limits
scopes:
- name: Lili Scopes
  scope_count: 0
  slug: lili-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 59.1
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 65.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 77.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lili/refs/heads/main/screenshots/lili-2026-09-02T150252.png
security:
- kind: authentication
  name: Lili Authentication
  slug: lili-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Lili Domain Security
  slug: lili-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lili
tags:
- Banking
- Business Banking
- Financial-Services
- Fintech
- Embedded Finance
- Onboarding
- KYC
- Webhook
- MCP
- agent-native
- Invoicing
- Bill Pay
- Accounting
- Small Business
website: https://lili.co/
---
