---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-24'
api_count: 17
apis:
- description: Read, create, update and delete creator (publisher) records in the customer's CreatorIQ CRM, plus their linked social accounts, scheduled posts, contacts and campaign relationships.
  name: CreatorIQ CRM Publishers API
  slug: creatoriq-crm-publishers-api
- description: Version 2 of the publishers surface, currently exposing bulk retrieval of linked social accounts for a set of publisher identifiers.
  name: CreatorIQ CRM Publishers API V2
  slug: creatoriq-crm-publishers-api-v2
- description: Create and manage campaigns, campaign publishers and their status, campaign activity, expenses, brands and advertiser information.
  name: CreatorIQ Campaign APIs
  slug: creatoriq-campaign-apis
- description: Version 2 brands surface — list, retrieve and search the brands attached to campaigns.
  name: CreatorIQ CRM Campaigns API V2
  slug: creatoriq-crm-campaigns-api-v2
- description: Asynchronous reporting surface exposing forty report views over campaigns, campaign posts, top influencers, videos, per-network breakdowns, audience data and creator-linked account metrics.
  name: CreatorIQ Reporting APIs
  slug: creatoriq-reporting-apis
- description: Look up social accounts and posts by link or handle across Instagram, TikTok and YouTube, retrieve account history and Instagram stories history.
  name: CreatorIQ Social Account APIs
  slug: creatoriq-social-account-apis
- description: Create, update and delete lists of creators and add or remove publishers from a list.
  name: CreatorIQ CRM Lists API
  slug: creatoriq-crm-lists-api
- description: Create, publish and manage One-Sheets — shareable creator pitch sheets — including adding publishers, comments, approvals and rejections.
  name: CreatorIQ CRM Onesheets API
  slug: creatoriq-crm-onesheets-api
- description: Attach and retrieve notes against CRM entities and their dimensions.
  name: CreatorIQ CRM Notes API
  slug: creatoriq-crm-notes-api
- description: List and retrieve the divisions of a partner account — the tenancy boundary that division-level API keys and webhook subscriptions are scoped to.
  name: CreatorIQ Divisions APIs
  slug: creatoriq-divisions-apis
- description: Manage promo codes, promo-code integrations, connected ecommerce accounts and read ecommerce transactions attributed to creators.
  name: CreatorIQ Ecommerce APIs
  slug: creatoriq-ecommerce-apis
- description: Create, list and manage trackable affiliate links used to attribute traffic and conversions to creators.
  name: CreatorIQ CRM LinkTracking API
  slug: creatoriq-crm-linktracking-api
- description: Define and read global and per-campaign conversion metrics, including metrics bound to individual tracking links.
  name: CreatorIQ Conversion Metrics API
  slug: creatoriq-conversion-metrics-api
- description: Submit posts for brand-safety analysis and retrieve the resulting scoring for a post.
  name: CreatorIQ SafeIQ Brand Safety API
  slug: creatoriq-safeiq-brand-safety-api
- description: Draft brand-safety check endpoint published alongside SafeIQ, with separate prod, stage and dev server entries.
  name: CreatorIQ Brand Safety (draft)
  slug: creatoriq-brand-safety-draft
- description: Read creator payouts and payables, and check the payment-information collection status of creators.
  name: CreatorIQ Payments API
  slug: creatoriq-payments-api
- description: 'Subscribe to, unsubscribe from and list CreatorIQ event subscriptions. Events cover campaign create/delete/latest-post/payout-paid, creator account link/unlink/update/delete/campaign-added, One-Sheet '
  name: CreatorIQ Webhooks (pub/sub) API
  slug: creatoriq-webhooks-pubsub-api
artifact_total: 41
asyncapis:
- description: ''
  name: Creatoriq Webhooks
  slug: creatoriq-webhooks
collections:
- collection_type: open
  name: CreatorIQ Brand Safety (draft)
  slug: open-creatoriq-brand-safety-draft
- collection_type: open
  name: CreatorIQ SafeIQ Brand Safety API
  slug: open-creatoriq-brand-safety
- collection_type: open
  name: CreatorIQ Campaign APIs
  slug: open-creatoriq-campaigns
- collection_type: open
  name: Conversion Metrics API
  slug: open-creatoriq-conversion-metrics
- collection_type: open
  name: CreatorIQ Ecommerce APIs
  slug: open-creatoriq-ecommerce
- collection_type: open
  name: CreatorIQ CRM LinkTracking API
  slug: open-creatoriq-link-tracking
- collection_type: open
  name: CreatorIQ CRM Lists API
  slug: open-creatoriq-lists
- collection_type: open
  name: CreatorIQ CRM Publishers API
  slug: open-creatoriq-notes
- collection_type: open
  name: CreatorIQ CRM Onesheets API
  slug: open-creatoriq-onesheets
- collection_type: open
  name: CreatorIQ Payments API
  slug: open-creatoriq-payments
- collection_type: open
  name: CreatorIQ CRM Publishers API
  slug: open-creatoriq-publishers
- collection_type: open
  name: CreatorIQ Reporting APIs
  slug: open-creatoriq-reports
- collection_type: open
  name: CreatorIQ Social Account APIs
  slug: open-creatoriq-socials
- collection_type: open
  name: CreatorIQ Divisions APIs
  slug: open-creatoriq-v1-divisions
- collection_type: open
  name: CreatorIQ CRM Campaigns API V2
  slug: open-creatoriq-v2-campaigns
- collection_type: open
  name: CreatorIQ CRM Publishers API V2
  slug: open-creatoriq-v2-publishers
- collection_type: open
  name: CreatorIQ Public APIs
  slug: open-creatoriq-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.creatoriq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.creatoriq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.creatoriq.com/docs/ciq-api-documentation/o5yqwvpp1lbnb-overview
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.creatoriq.com/docs/ciq-api-documentation/6e239b2598043-creator-iq-crm-publishers-api
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.creatoriq.com/docs/ciq-api-documentation/05lf89tv60rvy-introduction-to-api-keys
- group: auth
  title: ''
  type: Authentication
  url: authentication/creatoriq-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://www.creatoriq.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.creatoriq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.creatoriq.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/creatoriq-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.creatoriq.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.creatoriq.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.creatoriq.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.creatoriq.com/legal/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/creatoriq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/creatoriq-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.creatoriq.com/trust
- group: auth
  title: ''
  type: DomainSecurity
  url: security/creatoriq-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.creatoriq.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://apidocs.creatoriq.com/docs/ciq-api-documentation/o5yqwvpp1lbnb-overview
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/creatoriq-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.creatoriq.com/docs/ciq-api-documentation/6b7999d265a29-changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/creatoriq-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/creatoriq-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/creatoriq-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/creatoriq-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/creatoriq-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/creatoriq-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/creatoriq-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/creatoriq-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/creatoriq-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/_index.yml
created: '2026-08-11'
description: 'CreatorIQ is an enterprise creator- and influencer-marketing platform used by brands and agencies to discover creators, build and manage a private creator network, run and measure campaigns, handle creator payouts, and report on performance across Instagram, TikTok, YouTube and other social networks. Its public REST API — documented on a Stoplight portal at apidocs.creatoriq.com and served from https://apis.creatoriq.com — exposes the customer''s own CRM: publishers (creators), campaigns, lists, one-sheets, notes, divisions, social accounts and post/account metrics, an asynchronous reporting surface of forty report views, ecommerce promo codes and transactions, affiliate link tracking, conversion metrics, SafeIQ brand-safety scoring, and a Payments API for payouts and payables. A pub/sub webhook API lets integrators subscribe to campaign, creator, one-sheet and list events with MD5 and SHA-256 signed callbacks. Authentication is a single `x-api-key` header issued per partner
  or per division by a CreatorIQ account manager; there is no self-serve signup.'
image: https://www.creatoriq.com/hubfs/2025%20Rebrading%20Assets%20%3E%20DO%20NOT%20DELETE/Logos/creatorIQ-logo-new.svg
layout: provider
modified: '2026-08-11'
name: CreatorIQ
nav: Providers
network: true
overview: 'CreatorIQ publishes 17 APIs on the [APIs.io](https://apis.io/) network, including CRM Publishers API, CRM Publishers API V2, Campaign APIs, and 14 more. Tagged areas include Influencer Marketing, Creator Economy, Social-Media, Marketing, and Campaign Management.


  The CreatorIQ catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CreatorIQ''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Creatoriq Plans Pricing
  plan_count: 0
  slug: creatoriq-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Creatoriq Rate Limits
  slug: creatoriq-rate-limits
score:
  band: exemplar
  composite: 67.3
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 72.1
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 78.9
  previous_composite: 67.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/creatoriq/refs/heads/main/screenshots/creatoriq-2026-08-17T080838.png
security:
- kind: authentication
  name: Creatoriq Authentication
  slug: creatoriq-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Creatoriq Domain Security
  slug: creatoriq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Creatoriq Vulnerability Disclosure
  slug: creatoriq-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Creatoriq Trust Center
  slug: creatoriq-trust-center
  summary_line: ISO/IEC 27001:2022
slug: creatoriq
tags:
- Influencer Marketing
- Creator Economy
- Social-Media
- Marketing
- Campaign Management
- creator-crm
- Social Analytics
- Brand Safety
- Affiliate Marketing
- Creator Payments
- E-Commerce
- Reporting
- Webhook
website: https://www.creatoriq.com/
---
