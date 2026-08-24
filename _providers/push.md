---
access_model:
  confidence: high
  label: Sales-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans/push-plans-pricing.yml
  - authentication/push-authentication.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 41
  human_in_the_loop: 0
  name: Push Agentic Access
  operation_count: 67
  slug: push-agentic-access
  summary_line: 67 operations · 41 acting
api_count: 1
apis:
- description: 'Token-authenticated REST API for the Cendyn CRM (formerly PUSHTech) hospitality CRM / CDP platform. 67 operations across 15 resources: read the account credit balance, manage contacts and their custom'
  name: Cendyn CRM (PUSHTech) REST API
  slug: cendyn-crm-pushtech-rest-api
arazzos:
- description: Discover account-specific product custom fields, create a product, record a purchase against an existing guest contact, and read the purchase back to confirm it landed — the flow that turns the Cendyn
  name: Load a product catalog and attach guest purchase history
  slug: push-load-catalog-and-purchase-history
- description: Check the account has credit, create a guest contact in Cendyn CRM (PUSHTech) with GDPR consent recorded, subscribe them to an audience list, send a welcome email, and confirm the delivery reached a t
  name: Onboard a guest and send a welcome message
  slug: push-onboard-and-welcome-guest
artifact_total: 10
asyncapis:
- description: 'Event surface of the Cendyn CRM (formerly PUSHTech) hospitality CRM / CDP platform. The platform makes an HTTP POST to subscriber-configured callback URLs when activities, message deliveries, contact '
  name: Cendyn CRM (PUSHTech) Webhooks
  slug: push-webhooks-asyncapi
- description: ''
  name: Push Webhooks
  slug: push-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://pushtech.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cendyncrm.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cendyncrm.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cendyncrm.com/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cendyncrm.com/api/authentication
- group: operate
  title: ''
  type: Support
  url: https://pushtech.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.cendyn.com/resources/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pushtech
- group: start
  title: ''
  type: Login
  url: https://www.pushtech.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pushtech.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pushtech.com/privacy_policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/push-cendyn-crm-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/push-cendyn-crm-overlay.yaml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/push-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/push-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/push-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/push-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/push-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/push-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/push-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/push-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/push-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/push-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/push-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/push-rate-limits.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/push-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/push-llms.txt
- group: design
  title: ''
  type: Arazzo
  url: arazzo/push-onboard-and-welcome-guest.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/push-load-catalog-and-purchase-history.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/push-domain-security.yml
created: '2026-07-17'
description: Push (PUSHTech, now operating as Cendyn CRM after its acquisition by Cendyn) is a CRM and customer data platform specialised in hospitality — the guest journey for hotels — with additional use in retail, ecommerce and marketplace. The platform unifies the guest database and orchestrates pre-stay, during-stay and post-stay communication across email, SMS and web/app push. Its token-authenticated REST API exposes 67 operations across 15 resources (contacts and contact custom fields, companies, products, purchases, coupon lists, hotel data, audience lists, campaigns, deliveries, account balance and a bulk sync-data ingest) from two independent data centers, api.eu.cendyncrm.com and api.us.cendyncrm.com. An HMAC-signed webhook surface publishes five event groups — activities, deliveries, contacts, bulk contacts and incoming SMS — and a first-party JavaScript Web SDK handles browser tracking and web push. The developer portal moved from developers.pushtech.com to developers.cendyncrm.com
  without a redirect; the old hostnames no longer resolve. Cendyn CRM publishes no OpenAPI, no AsyncAPI, no MCP server, no agent card and no /.well-known/ documents; the machine-readable artifacts in this repo are derived by API Evangelist from the provider's own published HTML reference.
image: https://pushtech.com/favicon.ico
layout: provider
modified: '2026-08-13'
name: Push
nav: Providers
network: true
overview: 'Push publishes 1 API on the [APIs.io](https://apis.io/) network: Cendyn CRM (PUSHTech) REST API. Tagged areas include Company, CRM, Customer Data Platform, Marketing Automation, and Hospitality.


  The Push catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Push''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 25 more developer resources.'
plans:
- name: Push Plans Pricing
  plan_count: 0
  slug: push-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Push Rate Limits
  slug: push-rate-limits
score:
  band: thin
  composite: 37.3
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 16.7
    contract_quality: 22.7
    developer_ergonomics: 66.1
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/push/refs/heads/main/screenshots/push-2026-08-17T081405.png
security:
- kind: authentication
  name: Push Authentication
  slug: push-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Push Domain Security
  slug: push-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: push
tags:
- Company
- CRM
- Customer Data Platform
- Marketing Automation
- Hospitality
- Hotels
- Guest Experience
- Email
- SMS
- Push Notifications
- Webhook
- Segmentation
website: https://pushtech.com
---
