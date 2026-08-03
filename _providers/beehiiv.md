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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Beehiiv Agentic Access
  operation_count: 77
  slug: beehiiv-agentic-access
  summary_line: 77 operations · 32 acting
api_count: 24
apis:
- description: The subpackage_advertisement_opportunities API from beehiiv — 1 operation(s) for subpackage_advertisement_opportunities.
  name: beehiiv subpackage_advertisement_opportunities API
  slug: beehiiv-subpackage-advertisement-opportunities-api
- description: The subpackage_authors API from beehiiv — 2 operation(s) for subpackage_authors.
  name: beehiiv subpackage_authors API
  slug: beehiiv-subpackage-authors-api
- description: The subpackage_automationJourneys API from beehiiv — 2 operation(s) for subpackage_automationjourneys.
  name: beehiiv subpackage_automationJourneys API
  slug: beehiiv-subpackage-automationjourneys-api
- description: The subpackage_automations API from beehiiv — 3 operation(s) for subpackage_automations.
  name: beehiiv subpackage_automations API
  slug: beehiiv-subpackage-automations-api
- description: The subpackage_bulk_subscriptions API from beehiiv — 1 operation(s) for subpackage_bulk_subscriptions.
  name: beehiiv subpackage_bulk_subscriptions API
  slug: beehiiv-subpackage-bulk-subscriptions-api
- description: The subpackage_bulkSubscriptionUpdates API from beehiiv — 4 operation(s) for subpackage_bulksubscriptionupdates.
  name: beehiiv subpackage_bulkSubscriptionUpdates API
  slug: beehiiv-subpackage-bulksubscriptionupdates-api
- description: The subpackage_conditionSets API from beehiiv — 2 operation(s) for subpackage_conditionsets.
  name: beehiiv subpackage_conditionSets API
  slug: beehiiv-subpackage-conditionsets-api
- description: The subpackage_customFields API from beehiiv — 2 operation(s) for subpackage_customfields.
  name: beehiiv subpackage_customFields API
  slug: beehiiv-subpackage-customfields-api
- description: The subpackage_dataDeletion API from beehiiv — 2 operation(s) for subpackage_datadeletion.
  name: beehiiv subpackage_dataDeletion API
  slug: beehiiv-subpackage-datadeletion-api
- description: The subpackage_engagements API from beehiiv — 1 operation(s) for subpackage_engagements.
  name: beehiiv subpackage_engagements API
  slug: beehiiv-subpackage-engagements-api
- description: The subpackage_newsletterLists API from beehiiv — 2 operation(s) for subpackage_newsletterlists.
  name: beehiiv subpackage_newsletterLists API
  slug: beehiiv-subpackage-newsletterlists-api
- description: The subpackage_newsletterListSubscriptions API from beehiiv — 3 operation(s) for subpackage_newsletterlistsubscriptions.
  name: beehiiv subpackage_newsletterListSubscriptions API
  slug: beehiiv-subpackage-newsletterlistsubscriptions-api
- description: The subpackage_oauth_users API from beehiiv — 1 operation(s) for subpackage_oauth_users.
  name: beehiiv subpackage_oauth_users API
  slug: beehiiv-subpackage-oauth-users-api
- description: The subpackage_polls API from beehiiv — 3 operation(s) for subpackage_polls.
  name: beehiiv subpackage_polls API
  slug: beehiiv-subpackage-polls-api
- description: The subpackage_posts API from beehiiv — 3 operation(s) for subpackage_posts.
  name: beehiiv subpackage_posts API
  slug: beehiiv-subpackage-posts-api
- description: The subpackage_postTemplates API from beehiiv — 1 operation(s) for subpackage_posttemplates.
  name: beehiiv subpackage_postTemplates API
  slug: beehiiv-subpackage-posttemplates-api
- description: The subpackage_publications API from beehiiv — 2 operation(s) for subpackage_publications.
  name: beehiiv subpackage_publications API
  slug: beehiiv-subpackage-publications-api
- description: The subpackage_referralProgram API from beehiiv — 1 operation(s) for subpackage_referralprogram.
  name: beehiiv subpackage_referralProgram API
  slug: beehiiv-subpackage-referralprogram-api
- description: The subpackage_segments API from beehiiv — 5 operation(s) for subpackage_segments.
  name: beehiiv subpackage_segments API
  slug: beehiiv-subpackage-segments-api
- description: The subpackage_subscriptions API from beehiiv — 3 operation(s) for subpackage_subscriptions.
  name: beehiiv subpackage_subscriptions API
  slug: beehiiv-subpackage-subscriptions-api
- description: The subpackage_subscriptionTags API from beehiiv — 1 operation(s) for subpackage_subscriptiontags.
  name: beehiiv subpackage_subscriptionTags API
  slug: beehiiv-subpackage-subscriptiontags-api
- description: The subpackage_tiers API from beehiiv — 2 operation(s) for subpackage_tiers.
  name: beehiiv subpackage_tiers API
  slug: beehiiv-subpackage-tiers-api
- description: The subpackage_webhooks API from beehiiv — 2 operation(s) for subpackage_webhooks.
  name: beehiiv subpackage_webhooks API
  slug: beehiiv-subpackage-webhooks-api
- description: The subpackage_workspaces API from beehiiv — 2 operation(s) for subpackage_workspaces.
  name: beehiiv subpackage_workspaces API
  slug: beehiiv-subpackage-workspaces-api
artifact_total: 63
asyncapis:
- description: 'AsyncAPI 2.6 description of the beehiiv outbound webhook surface. beehiiv posts JSON event payloads to a customer-configured endpoint URL when selected events occur on a publication. The set of event '
  name: beehiiv Webhooks
  slug: beehiiv-asyncapi
collections:
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities API
  slug: postman-beehiiv-subpackage-advertisement-opportunities-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_authors API
  slug: postman-beehiiv-subpackage-authors-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_automationJourneys API
  slug: postman-beehiiv-subpackage-automationjourneys-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_automations API
  slug: postman-beehiiv-subpackage-automations-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_bulk_subscriptions API
  slug: postman-beehiiv-subpackage-bulk-subscriptions-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_bulkSubscriptionUpdates API
  slug: postman-beehiiv-subpackage-bulksubscriptionupdates-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_conditionSets API
  slug: postman-beehiiv-subpackage-conditionsets-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_customFields API
  slug: postman-beehiiv-subpackage-customfields-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_dataDeletion API
  slug: postman-beehiiv-subpackage-datadeletion-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_engagements API
  slug: postman-beehiiv-subpackage-engagements-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_newsletterLists API
  slug: postman-beehiiv-subpackage-newsletterlists-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_newsletterListSubscriptions API
  slug: postman-beehiiv-subpackage-newsletterlistsubscriptions-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_oauth_users API
  slug: postman-beehiiv-subpackage-oauth-users-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_polls API
  slug: postman-beehiiv-subpackage-polls-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_posts API
  slug: postman-beehiiv-subpackage-posts-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_postTemplates API
  slug: postman-beehiiv-subpackage-posttemplates-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_publications API
  slug: postman-beehiiv-subpackage-publications-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_referralProgram API
  slug: postman-beehiiv-subpackage-referralprogram-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_segments API
  slug: postman-beehiiv-subpackage-segments-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_subscriptions API
  slug: postman-beehiiv-subpackage-subscriptions-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_subscriptionTags API
  slug: postman-beehiiv-subpackage-subscriptiontags-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_tiers API
  slug: postman-beehiiv-subpackage-tiers-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_webhooks API
  slug: postman-beehiiv-subpackage-webhooks-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_workspaces API
  slug: postman-beehiiv-subpackage-workspaces-api
- collection_type: open
  name: API Reference
  slug: open-beehiiv
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/beehiiv/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/beehiiv-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/beehiiv-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beehiiv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beehiiv-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beehiiv
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beehiiv
- group: company
  title: ''
  type: Website
  url: https://www.beehiiv.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.beehiiv.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://developers.beehiiv.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.beehiiv.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.beehiiv.com/welcome/getting-started
- group: operate
  title: ''
  type: RateLimiting
  url: https://developers.beehiiv.com/welcome/rate-limiting
- group: commercial
  title: ''
  type: Plans
  url: plans/beehiiv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/beehiiv-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/beehiiv-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/beehiiv-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.beehiiv.com/llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.beehiiv.com/llms-full.txt
- group: agent
  title: ''
  type: MCPServer
  url: https://developers.beehiiv.com/_mcp/server
- group: build
  title: ''
  type: SDKs
  url: https://github.com/beehiiv/typescript-sdk
- group: operate
  title: ''
  type: Support
  url: https://support.beehiiv.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.beehiiv.com/blog
created: '2026-05-08'
description: beehiiv is a newsletter publishing platform offering email publishing, subscriber management, paid subscriptions, an ad network, referrals, polls, automations, segments, webhooks, and analytics for creators and media companies. Founded in 2021 by former Morning Brew operators and headquartered in New York City.
finops:
- name: Beehiiv Finops
  service_category: Newsletter Publishing
  slug: beehiiv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beehiiv.png
json_schemas:
- name: beehiiv Post
  property_count: 19
  slug: beehiiv-post
- name: beehiiv Subscription
  property_count: 16
  slug: beehiiv-subscription
jsonld:
- class_count: 0
  name: Beehiiv Context
  property_count: 6
  slug: beehiiv-context
layout: provider
mcp_servers:
- description: ''
  name: server
  slug: server
modified: '2026-05-30'
name: beehiiv
nav: Providers
network: true
overview: 'beehiiv publishes 24 APIs on the [APIs.io](https://apis.io/) network, including subpackage_advertisement_opportunities API, subpackage_authors API, subpackage_automationJourneys API, and 21 more. Tagged areas include Newsletter, Creator, Email, Subscription, and Publishing.


  The beehiiv catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  beehiiv''s developer surface includes authentication, pricing, documentation, API reference, getting-started guide, support, engineering blog, and 16 more developer resources.'
plans:
- name: Beehiiv Plans Pricing
  plan_count: 4
  slug: beehiiv-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 1
  name: Beehiiv Rate Limits
  slug: beehiiv-rate-limits
rules:
- name: beehiiv API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: beehiiv-asyncapi-spectral-rules
- name: beehiiv API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: beehiiv-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.6
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 80.6
    developer_ergonomics: 63.0
    discoverability: 68.5
    governance: 41.7
    operational_transparency: 26.3
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/screenshots/beehiiv-2026-06-20T173135.png
security:
- kind: authentication
  name: Beehiiv Authentication
  slug: beehiiv-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Beehiiv Domain Security
  slug: beehiiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Beehiiv Trust Center
  slug: beehiiv-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: beehiiv
tags:
- Newsletter
- Creator
- Email
- Subscription
- Publishing
- Media
- Advertising
website: https://www.beehiiv.com/
---
