---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-08-17'
api_count: 17
apis:
- description: Records customer interactions from e-commerce, POS, websites, and mobile apps as loyalty events (for example point_add, checkout_accept), driving the rules and workflows of the loyalty program. Suppor
  name: Antavo Events API
  slug: antavo-events-api
- description: Queues events for reliable background processing during high-traffic periods, returning a correlation id that can be polled for status. Uses token-based authentication via the /v1/auth/token endpoint.
  name: Antavo Async Events API
  slug: antavo-async-events-api
- description: Search, retrieve, and manage loyalty member profiles - including login, opt-in registration, password reset, verification, account merging, and active-customer counts - while maintaining member privac
  name: Antavo Customer API
  slug: antavo-customer-api
- description: The primary headless API for building the member-facing loyalty experience - listing earn and spend activities, challenges, rewards, offers, coupons, transactions, wallet passes, quizzes, contests, pr
  name: Antavo Display API
  slug: antavo-display-api
- description: 'Generic CRUD surface for the foundational building blocks of a program - rewards, challenges, stores, products, transactions, and customer lists - addressed as entities under a module namespace, with '
  name: Antavo Entities API
  slug: antavo-entities-api
- description: Manage the reward catalog and redemptions - create, list, retrieve, update, and archive rewards via the entities surface, and claim rewards. Legacy /rewards claim endpoints are superseded by the Displ
  name: Antavo Rewards API
  slug: antavo-rewards-api
- description: Query coupon usage independent of a customer and create or manage coupon pools - configuring value, expiration, and code patterns - with bulk import of codes and status/error reporting on the batch op
  name: Antavo Coupons and Coupon Pools API
  slug: antavo-coupons-api
- description: Submit a cart and retrieve applicable pre-purchase offers used for customer acquisition and engagement, and list a member's available offers through the Display surface.
  name: Antavo Offers API
  slug: antavo-offers-api
- description: Preview the loyalty points a transaction would earn, including bonus points assigned by the Workflows module, before the transaction is committed.
  name: Antavo Points Preview API
  slug: antavo-points-preview-api
- description: Retrieve ranked lists of top customers with their scores for display in mobile apps, websites, and CRMs.
  name: Antavo Leaderboard API
  slug: antavo-leaderboard-api
- description: Batch processing for reward claims across many customers and for adding or removing customers from lists, each returning a batch id with status and error reporting endpoints.
  name: Antavo Bulk Operations API
  slug: antavo-bulk-operations-api
- description: Create and administer member clubs and communities - templates, membership, invitations, applicants, bans, ownership, point adjustments and donations, history, and disbanding.
  name: Antavo Clubs API
  slug: antavo-clubs-api
- description: List and manage promotions and apply them at checkout - submit a cart to retrieve applicable promotions and finalize the checkout with the resulting discounts.
  name: Antavo Promotion Engine API
  slug: antavo-promotion-engine-api
- description: Generate short-lived access tokens for credential clients configured in the Authentication Manager, used for token-based authentication such as the Async Events API.
  name: Antavo Authentication API
  slug: antavo-authentication-api
- description: Read-only access to the questions and answers configured and managed in the Antavo FAQ module. A valid request returns an array of FAQ entries and, by design, includes no personally identifiable custo
  name: Antavo FAQ API
  slug: antavo-faq-api
- description: A dedicated read-optimised API served from its own per-environment host (read-api.<environment>.antavo.com) for pulling loyalty data at volume. Returns paginated, filterable and sortable lists of cust
  name: Antavo Loyalty Read API
  slug: antavo-loyalty-read-api
- description: Registers a customer's intent to share content for an active campaign configured in the Social Share Campaigns module. Called when a member clicks a share button on a content page with the customer ID
  name: Antavo Social Share Campaigns API
  slug: antavo-social-share-campaigns-api
artifact_total: 43
asyncapis:
- description: ''
  name: Antavo Webhooks
  slug: antavo-webhooks
collections:
- collection_type: open
  name: Antavo Async Events API
  slug: open-antavo-async-events
- collection_type: open
  name: Antavo Authentication API
  slug: open-antavo-authentication
- collection_type: open
  name: Antavo Bulk Operations API
  slug: open-antavo-bulk-operations
- collection_type: open
  name: Antavo Clubs API
  slug: open-antavo-clubs
- collection_type: open
  name: Antavo Coupon Pools API
  slug: open-antavo-coupon-pools
- collection_type: open
  name: Antavo Coupons API
  slug: open-antavo-coupons
- collection_type: open
  name: Antavo Customers API
  slug: open-antavo-customer
- collection_type: open
  name: Antavo Display API
  slug: open-antavo-display
- collection_type: open
  name: Antavo Entities API
  slug: open-antavo-entities
- collection_type: open
  name: Antavo Events API
  slug: open-antavo-events
- collection_type: open
  name: Antavo FAQ API
  slug: open-antavo-faq
- collection_type: open
  name: Antavo Leaderboard API
  slug: open-antavo-leaderboard
- collection_type: open
  name: Antavo Loyalty Read API
  slug: open-antavo-loyalty-read
- collection_type: open
  name: Antavo Offers API
  slug: open-antavo-offers
- collection_type: open
  name: Antavo Promotion Engine API
  slug: open-antavo-promotion-engine
- collection_type: open
  name: Antavo Rewards API
  slug: open-antavo-rewards
- collection_type: open
  name: Antavo Socal Share Campaigns API
  slug: open-antavo-social-share-campaigns
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/antavo-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/antavo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/antavo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/antavo
- group: company
  title: ''
  type: Website
  url: https://antavo.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.antavo.com/docs/antavo-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/antavo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/antavo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/antavo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://antavo.com/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.antavo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.antavo.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.antavo.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://antavo.atlassian.net/servicedesk/customer/portals
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.antavo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://antavo.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://antavo.com/legals/privacy/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/31303107/2sAYdmkTFm
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/antavo-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/antavo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/antavo-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/antavo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/antavo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://antavo.com/status/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.antavo.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/antavo-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/antavo-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/antavo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://antavo.com/product/loyalty-engine/technology/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/antavo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/antavo-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/antavo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/antavo-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/antavo-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/antavo-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/antavo-submit-loyalty-event.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/antavo-async-event-ingestion.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/antavo-member-experience-and-reward-claim.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/antavo-cart-promotions-and-points-preview.md
created: '2026-07-10'
description: Antavo is an enterprise loyalty management platform - the Antavo AI Loyalty Cloud - that lets brands build and run omnichannel, multi-brand, multi-country loyalty programs. Its API-first, headless Loyalty Engine exposes a comprehensive REST API covering customer events, customer profiles, the headless Display surface for loyalty experiences, configurable entities (rewards, challenges, stores, products, transactions), coupons, offers, leaderboards, clubs, promotions, and bulk operations. Requests use standard HTTP verbs with JSON, secured by API key/secret with optional request signing, IP filtering, and token-based auth. API access is provisioned per Antavo environment for enterprise customers, while the developer documentation is fully public.
finops:
- name: Antavo Finops
  service_category: Marketing and Customer Loyalty
  slug: antavo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/antavo.png
layout: provider
modified: '2026-08-13'
name: Antavo
nav: Providers
network: true
overview: 'Antavo publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Events API, Async Events API, Customer API, and 14 more. Tagged areas include Loyalty, Customer Loyalty, Rewards, Enterprise, and Headless.


  The Antavo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Antavo''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, pricing, and 33 more developer resources.'
plans:
- name: Antavo Plans Pricing
  plan_count: 2
  slug: antavo-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 4
  name: Antavo Rate Limits
  slug: antavo-rate-limits
scopes:
- name: Antavo Scopes
  scope_count: 1
  slug: antavo-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: exemplar
  composite: 66.4
  delta: 46.2
  facets:
    commercial_clarity: 65.8
    contract_quality: 61.1
    developer_ergonomics: 76.1
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 84.2
  previous_composite: 20.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/screenshots/antavo-2026-07-25T200404.png
security:
- kind: authentication
  name: Antavo Authentication
  slug: antavo-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Antavo Domain Security
  slug: antavo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Antavo Vulnerability Disclosure
  slug: antavo-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Antavo Trust Center
  slug: antavo-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, GDPR / UK GDPR
slug: antavo
tags:
- Loyalty
- Customer Loyalty
- Rewards
- Enterprise
- Headless
- Retail
- Marketing
- Engagement
- Promotions
- Gamification
- Events
- eCommerce
- Coupons
- Points
- Membership
website: https://antavo.com
---
