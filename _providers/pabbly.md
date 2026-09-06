---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - plans
  - https://buy.pabbly.com/content/pabbly-plus-pricing.md
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-09-05'
api_count: 7
apis:
- description: REST API for Pabbly Subscription Billing — 95 documented operations across customers, subscriptions, products, plans, multiplans, coupons, invoices, payment methods, transactions and refunds, add-ons,
  name: Pabbly Subscription Billing API
  slug: pabbly-subscriptions
- description: REST API for Pabbly Hook, an inbound webhook gateway that receives, logs, filters, transforms and forwards webhook requests. 21 documented operations across folders, connections, transformations, requ
  name: Pabbly Hook API
  slug: pabbly-hook
- description: REST API for Pabbly Chatflow, a WhatsApp Business messaging platform. 33 documented operations covering 18 message shapes on a single POST /messages endpoint, plus templates, broadcasts, contacts, tag
  name: Pabbly Chatflow API
  slug: pabbly-chatflow
- description: 'REST API for Pabbly Email Marketing — 23 documented operations across subscribers (upsert semantics on create), subscriber lists and segments, campaigns with asynchronous batch sending, custom fields '
  name: Pabbly Email Marketing API
  slug: pabbly-email-marketing
- description: REST API for Pabbly Email Verification. A single operation, POST /email-lists/verify-single, returning a deliverability verdict plus accept_all, disposable, spamtrap, role and free_email risk flags. H
  name: Pabbly Email Verification API
  slug: pabbly-email-verification
- description: Backend-to-backend API that lets a product use Pabbly Connect as its connection manager — search a catalog of 1,000+ apps, mint hosted OAuth or credential request links for an end customer, and vend f
  name: Pabbly Connect Platform API
  slug: pabbly-connect-platform
- description: Beta hosted MCP server that exposes a Pabbly Connect user's own workflow action steps as agent tools. Tools are authored inside Pabbly Connect ("Add to MCP Server"), and the server URL is minted per a
  name: Pabbly Connect MCP Server
  slug: pabbly-connect-mcp
artifact_total: 16
asyncapis:
- description: ''
  name: Pabbly Subscription Billing Webhooks
  slug: pabbly-subscription-billing-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.pabbly.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.pabbly.com/
- group: start
  title: ''
  type: Portal
  url: https://apidocs.pabbly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.pabbly.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.pabbly.com/subscription-billing/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.pabbly.com/subscription-billing/reference/guides/overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/pabbly-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pabbly-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pabbly-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/pabbly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pabbly-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pabbly-subscription-billing-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pabbly-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pabbly-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pabbly-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/pabbly-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pabbly-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pabbly-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pabbly-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pabbly-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pabbly-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pabbly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.pabbly.com/security-vulnerability-disclosure/
- group: auth
  title: ''
  type: TrustCenter
  url: security/pabbly-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.pabbly.com/security/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/pabbly/workspace/pabbly-team-s-public-workspace/overview
- group: operate
  title: ''
  type: Roadmap
  url: https://pabbly.featureos.app/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pabbly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pabbly
- group: operate
  title: ''
  type: Support
  url: https://www.pabbly.com/contact-us/
- group: operate
  title: ''
  type: Community
  url: https://forum.pabbly.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pabbly.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.pabbly.com/blog/feed/
- group: start
  title: ''
  type: SignUp
  url: https://accounts.pabbly.com/signup
- group: start
  title: ''
  type: Login
  url: https://accounts.pabbly.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://buy.pabbly.com/pabbly-plus/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pabbly.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pabbly.com/privacy-policy/
- group: other
  title: ''
  type: BrandAssets
  url: https://www.pabbly.com/brand-assets/
- group: company
  title: ''
  type: About
  url: https://www.pabbly.com/about-us/
created: '2026-03-16'
description: 'Pabbly is an Indian SaaS company selling a suite of marketing and sales software as one-time lifetime deals as well as monthly plans: Pabbly Connect (workflow automation), Pabbly Subscription Billing (recurring billing and invoicing), Pabbly Email Marketing, Pabbly Chatflow (WhatsApp Business messaging), Pabbly Form Builder, Pabbly Hook (an inbound webhook gateway) and Pabbly Email Verification. Its developer platform at apidocs.pabbly.com documents five REST APIs and 173 endpoints, all keyed on HTTP Basic or Bearer credentials generated from the account dashboard, plus a sixth Connect Platform API distributed only through a first-party npm SDK. Pabbly Subscription Billing emits 23 webhook event types, and Pabbly Connect ships a beta hosted MCP server that exposes a customer''s own workflow actions as agent tools.'
finops:
- name: Pabbly Finops
  service_category: API
  slug: pabbly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pabbly.png
layout: provider
mcp_servers:
- description: Pabbly Connect exposes the action steps of a user's own automation workflows as MCP tools. Inside Pabbly Connect the user marks an action step "Add to MCP Server", names the tool (camelCase, no spaces
  name: Pabbly Connect MCP Server
  slug: pabbly-connect-mcp-server
modified: '2026-08-13'
name: Pabbly
nav: Providers
network: true
overview: 'Pabbly publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Email Marketing, Subscription Billing, Billing, and Payments.


  The Pabbly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pabbly''s developer surface includes developer portal, documentation, API reference, getting-started guide, authentication, support, engineering blog, and 34 more developer resources.'
plans:
- name: Pabbly Plans Pricing
  plan_count: 13
  slug: pabbly-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Pabbly Rate Limits
  slug: pabbly-rate-limits
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 50.0
    catalog_earned_first_party: 12.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 68.5
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 57.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pabbly/refs/heads/main/screenshots/pabbly-2026-06-20T191303.png
security:
- kind: authentication
  name: Pabbly Authentication
  slug: pabbly-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Pabbly Domain Security
  slug: pabbly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pabbly Vulnerability Disclosure
  slug: pabbly-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Pabbly Trust Center
  slug: pabbly-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 2 Type 2
slug: pabbly
tags:
- Automation
- Email Marketing
- Subscription Billing
- Billing
- Payments
- Webhook
- Messaging
- WhatsApp
- Email Verification
- Forms
- No-Code
- Software-as-a-Service
website: https://www.pabbly.com/
---
