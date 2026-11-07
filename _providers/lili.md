---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Lili Agentic Access
  operation_count: 11
  slug: lili-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 3
apis:
- description: Remote, OAuth 2.0 protected Model Context Protocol server (Streamable HTTP, MCP spec 2025-03-26) exposing 44 tools that let an AI assistant read a Lili business customer's account summary, transaction
  name: Lili MCP Server
  slug: lili-mcp-server
- baseURL: https://prod.lili.co
  baseurl_source: declared
  description: The Lili API from Lili — 8 operation(s) for lili.
  name: Lili API
  slug: lili-lili-api
artifact_total: 24
asyncapis:
- description: ''
  name: Lili Webhooks
  slug: lili-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/lili/agentic-access/lili-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lili-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/lili/rules/lili-rules.yml
  title: ''
  type: Spectral
  url: rules/lili-rules.yml
- group: design
  href: https://artifacts.apis.io/lili/json-ld/lili-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lili-context.jsonld
- group: design
  href: https://artifacts.apis.io/lili/vocabulary/lili-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lili-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/lili/lifecycle/lili-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/lili-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/lili/llms/lili-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lili-site-llms.txt
- group: other
  href: https://artifacts.apis.io/lili/hosts/lili-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lili-hosts.yml
- group: build
  href: https://artifacts.apis.io/lili/integrations/lili-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/lili-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/lili/vendors/lili-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lili-vendors.yml
- group: build
  href: https://artifacts.apis.io/lili/packages/lili-packages.yml
  title: ''
  type: SDKs
  url: packages/lili-packages.yml
- group: other
  href: https://artifacts.apis.io/lili/overlays/lili-application-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lili-application-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/lili/overlays/lili-customer-management-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lili-customer-management-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/lili/overlays/lili-webhooks-api-overlay.yaml
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
  href: https://artifacts.apis.io/lili/changelog/lili-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lili-changelog.yml
- group: agent
  href: https://artifacts.apis.io/lili/llms/lili-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lili-llms.txt
- group: agent
  href: https://artifacts.apis.io/lili/mcp/lili-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lili-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lili/well-known/lili-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lili-well-known.yml
- group: auth
  href: https://artifacts.apis.io/lili/authentication/lili-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lili-authentication.yml
- group: design
  href: https://artifacts.apis.io/lili/conventions/lili-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lili-conventions.yml
- group: design
  href: https://artifacts.apis.io/lili/lifecycle/lili-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lili-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/lili/conformance/lili-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lili-conformance.yml
- group: auth
  href: https://artifacts.apis.io/lili/conformance/lili-conformance.yml
  title: ''
  type: Compliance
  url: conformance/lili-conformance.yml
- group: design
  href: https://artifacts.apis.io/lili/errors/lili-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lili-problem-types.yml
- group: build
  href: https://artifacts.apis.io/lili/errors/lili-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/lili-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/lili/data-model/lili-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lili-data-model.yml
- group: start
  href: https://artifacts.apis.io/lili/sandbox/lili-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/lili-sandbox.yml
- group: design
  href: https://artifacts.apis.io/lili/components/lili-components.yml
  title: ''
  type: Components
  url: components/lili-components.yml
- group: build
  href: https://artifacts.apis.io/lili/packages/lili-packages.yml
  title: ''
  type: Packages
  url: packages/lili-packages.yml
- group: commercial
  href: https://artifacts.apis.io/lili/plans/lili-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lili-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lili/rate-limits/lili-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lili-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/lili/asyncapi/lili-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lili-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/lili/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/lili/security/lili-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lili-domain-security.yml
created: '2026-08-25'
description: 'Lili is a U.S. small-business banking and financial-management platform (banking services provided by Sunrise Banks, N.A., Member FDIC) that combines a business checking account, high-yield savings, a Visa debit card, invoicing, bill pay, expense categorization, tax buckets and business-credit products for LLCs, corporations, partnerships, sole proprietors and non-profits. For developers Lili publishes the Lili Connect platform at dev.lili.co: an Application API that creates a pre-filled business bank account application and returns a hosted or embeddable onboarding URL, a Customer Management API for payment notification and bank-letter retrieval, a Webhooks API for onboarding lifecycle events, and a remote, OAuth 2.0 protected MCP server at mcp.lili.co that exposes 44 read-oriented tools over balances, transactions, invoices, bills, suppliers, cards, tax estimates, statements and business profile for AI assistants and accountants.'
finops:
- has_sources: true
  method: derived
  name: Lili Finops
  primary_unit: account
  service_category: ''
  slug: lili-finops
  template: false
image: https://lili.co/wp-content/uploads/2025/05/meta-preview.png
json_schemas:
- name: LeadRequest
  property_count: 33
  slug: lili-lead-request
- name: LeadResponse
  property_count: 7
  slug: lili-lead-response
- name: PaymentRequest
  property_count: 8
  slug: lili-payment-request
- name: WebhookCreateResponse
  property_count: 4
  slug: lili-webhook-create-response
- name: WebhookRequest
  property_count: 4
  slug: lili-webhook-request
- name: WebhookResponse
  property_count: 5
  slug: lili-webhook-response
jsonld:
- class_count: 19
  name: Lili Context
  property_count: 73
  slug: lili-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.lili.co over streamable HTTP requiring OAuth; 44 tools listed.
  name: Lili MCP Server
  slug: lili
modified: '2026-09-16'
name: Lili
nav: Providers
network: true
overview: 'Lili publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Business Banking, Financial Services, Fintech, and Embedded Finance.


  The Lili catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Lili''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 39 more developer resources.'
plans:
- name: Lili Plans Pricing
  plan_count: 8
  slug: lili-plans-pricing
- name: Lili Price Estimates
  plan_count: 0
  slug: lili-price-estimates
random_paper: 18
rate_limits:
- limit_count: 0
  name: Lili Rate Limits
  slug: lili-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Lili API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: lili-rules
scopes:
- name: Lili Scopes
  scope_count: 0
  slug: lili-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 70.3
  coverage:
    artifact_dirs: 35
    catalog_earned: 80.8
    catalog_earned_first_party: 12.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 69.8
    developer_ergonomics: 73.2
    discoverability: 80.0
    operational_transparency: 31.6
  previous_composite: 70.3
  provenance:
    agentic_access: derived
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
    score: 48.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lili/lili-2026-09-02T150252.png
security:
- kind: authentication
  name: Lili Authentication
  slug: lili-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Lili Domain Security
  slug: lili-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: lili-agent-reads-business-finances
  slug: lili-agent-reads-business-finances
- name: lili-open-business-account
  slug: lili-open-business-account
- name: lili-simulate-sandbox-onboarding
  slug: lili-simulate-sandbox-onboarding
- name: lili-track-application-webhooks
  slug: lili-track-application-webhooks
slug: lili
tags:
- Banking
- Business Banking
- Financial Services
- Fintech
- Embedded Finance
- Onboarding
- KYC
- Webhook
- MCP
- Agent-Native
- Invoicing
- Bill Pay
- Accounting
- Small Business
website: https://lili.co/
---
