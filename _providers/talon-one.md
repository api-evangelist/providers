---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 68.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 142
  human_in_the_loop: 3
  name: Talon One Agentic Access
  operation_count: 271
  slug: talon-one-agentic-access
  summary_line: 271 operations · 142 acting · 3 human-in-the-loop
api_count: 5
apis:
- description: Real-time, high-traffic Integration API. Send customer sessions, customer profiles, events, cart item catalogs and loyalty activity into the Talon.One Rule Engine and receive back the effects (discoun
  name: Talon.One Integration API
  slug: talon-one-integration-api
- description: 'Back-office Management API that programmatically does what the Campaign Manager UI does: applications, campaigns, rulesets, campaign templates, coupons, referrals, giveaways, loyalty programs and card'
  name: Talon.One Management API
  slug: talon-one-management-api
- description: Third-party API used by customer data platforms (CDPs) and customer engagement platforms (CEPs) to exchange data with Talon.One. Ships platform-specific endpoint families for Braze, Emarsys, Iterable,
  name: Talon.One Third-party API
  slug: talon-one-third-party-api
- description: Shopify Integration API used by the Talon.One Shopify app to update customer sessions and customer profiles from a Shopify storefront, authenticated with a Shopify Customer Account API token or a Shop
  name: Talon.One Shopify Integration API
  slug: talon-one-shopify-integration-api
- description: Outbound notification (webhook) catalog published by Talon.One as an OpenAPI 3.1 document whose webhooks{} block carries the payload schema of every notification Talon.One POSTs to a customer endpoint
  name: Talon.One Outbound Notifications
  slug: talon-one-outbound-notifications
artifact_total: 20
asyncapis:
- description: ''
  name: Talon One Webhooks
  slug: talon-one-webhooks
collections:
- collection_type: open
  name: Integration API
  slug: open-talon-one-integration-api
- collection_type: open
  name: Management API
  slug: open-talon-one-management-api
- collection_type: open
  name: Notification schemas
  slug: open-talon-one-outbound-notifications
- collection_type: open
  name: Shopify Integration API
  slug: open-talon-one-shopify-integration-api
- collection_type: open
  name: Third-party API
  slug: open-talon-one-third-party-api
- collection_type: open
  name: Talon.One API
  slug: open-talon-one
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/talon-one-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/talon-one-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/talon-one-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/talon-one
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/talon-one
- group: company
  title: ''
  type: Website
  url: https://www.talon.one
- group: docs
  title: ''
  type: Documentation
  url: https://docs.talon.one
- group: start
  title: ''
  type: SignUp
  url: https://www.talon.one/book-a-demo
- group: commercial
  title: ''
  type: Plans
  url: plans/talon-one-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/talon-one-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/talon-one-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.talon.one/blog
- group: build
  title: ''
  type: Packages
  url: packages/talon-one-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/talon-one-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/talon-one-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/talon-one-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/talon-one-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/talon-one-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/talon-one-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/talon-one-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/talon-one-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/talon-one-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.talon.one/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/talon-one-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/talon-one-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/talon-one-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/talon-one-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.talon.one/whats-new
- group: start
  title: ''
  type: Sandbox
  url: sandbox/talon-one-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/talon-one-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/talon-one-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/talon-one-integration-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.talon.one/docs/dev/get-started/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.talon.one/integration-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.talon.one/docs/dev/quickstart
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/talonone-rnd/workspace/talon-one/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.talon.one/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.talon.one/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.talon.one/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.talon.one/contact-us
created: '2026-07-10'
description: Talon.One is an enterprise promotion, loyalty, and incentives engine that lets teams build and run coupons, discounts, referrals, bundles, giveaways, and multi-tier loyalty programs from a single rules-based platform. It exposes two primary REST APIs. The Integration API pushes real-time customer sessions, profiles, and events into the rules engine and returns the effects (discounts, awarded loyalty points, accepted coupons) to apply in the calling application. The Management API programmatically administers applications, campaigns, rulesets, coupons, loyalty programs, audiences, custom attributes, collections, and analytics exports that back the Campaign Manager. Talon.One is delivered as a managed, per-customer deployment; each account calls its own base URL (https://yourbaseurl.talon.one) and authenticates with an API key whose prefix distinguishes the Integration key (ApiKey-v1) from the Management key (ManagementKey-v1).
finops:
- name: Talon One Finops
  service_category: Marketing and Promotions
  slug: talon-one-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/talon-one.png
layout: provider
mcp_servers:
- description: ''
  name: talon-one-mcp.yml
  slug: talon-one-mcpyml
modified: '2026-08-13'
name: Talon.One
nav: Providers
network: true
overview: 'Talon.One publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Integration API, Management API, Third-party API, and 2 more. Tagged areas include Promotions, Loyalty, Coupons, Incentives, and Campaigns.


  The Talon.One catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Talon.One''s developer surface includes authentication, documentation, signup flow, engineering blog, changelog, sandbox, API reference, and 34 more developer resources.'
plans:
- name: Talon One Plans Pricing
  plan_count: 3
  slug: talon-one-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Talon One Rate Limits
  slug: talon-one-rate-limits
score:
  band: exemplar
  composite: 74.6
  delta: 32.9
  facets:
    commercial_clarity: 100.0
    contract_quality: 64.3
    developer_ergonomics: 84.8
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 84.2
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: authentication
  name: Talon One Authentication
  slug: talon-one-authentication
  summary_line: apiKey/http · 8 schemes
- kind: domain-security
  name: Talon One Domain Security
  slug: talon-one-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Talon One Trust Center
  slug: talon-one-trust-center
  summary_line: ISO 27001, SOC 2, GDPR
slug: talon-one
tags:
- Promotions
- Loyalty
- Coupons
- Incentives
- Campaigns
- Personalization
- MarTech
- Rules Engine
- Referrals
- Discounts
- Ecommerce
- Retail
website: https://www.talon.one
---
