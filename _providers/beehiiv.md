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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Beehiiv Agentic Access
  operation_count: 77
  slug: beehiiv-agentic-access
  summary_line: 77 operations · 32 acting
api_count: 5
apis:
- description: The Authorizations API from beehiiv — 1 operation(s) for authorizations.
  name: beehiiv Authorizations API
  slug: beehiiv-authorizations-api
- description: The Tokens API from beehiiv — 4 operation(s) for tokens.
  name: beehiiv Tokens API
  slug: beehiiv-tokens-api
- description: The Webhooks API from beehiiv — 0 operation(s) for webhooks.
  name: beehiiv Webhooks API
  slug: beehiiv-webhooks-api
- description: The Ad Network Offers API from beehiiv — 2 operation(s) for ad network offers.
  name: beehiiv Ad Network Offers API
  slug: beehiiv-ad-network-offers-api
- description: The Ad Network Reports API from beehiiv — 3 operation(s) for ad network reports.
  name: beehiiv Ad Network Reports API
  slug: beehiiv-ad-network-reports-api
- description: The Advertisement Opportunities API from beehiiv — 1 operation(s) for advertisement opportunities.
  name: beehiiv Advertisement Opportunities API
  slug: beehiiv-advertisement-opportunities-api
- description: The Authors API from beehiiv — 2 operation(s) for authors.
  name: beehiiv Authors API
  slug: beehiiv-authors-api
- description: The Automation Journeys API from beehiiv — 2 operation(s) for automation journeys.
  name: beehiiv Automation Journeys API
  slug: beehiiv-automation-journeys-api
- description: The Automations API from beehiiv — 3 operation(s) for automations.
  name: beehiiv Automations API
  slug: beehiiv-automations-api
- description: The Bulk Subscription Updates API from beehiiv — 4 operation(s) for bulk subscription updates.
  name: beehiiv Bulk Subscription Updates API
  slug: beehiiv-bulk-subscription-updates-api
- description: The Bulk Subscriptions API from beehiiv — 1 operation(s) for bulk subscriptions.
  name: beehiiv Bulk Subscriptions API
  slug: beehiiv-bulk-subscriptions-api
- description: The Complimentary Access API from beehiiv — 2 operation(s) for complimentary access.
  name: beehiiv Complimentary Access API
  slug: beehiiv-complimentary-access-api
- description: The Condition Sets API from beehiiv — 2 operation(s) for condition sets.
  name: beehiiv Condition Sets API
  slug: beehiiv-condition-sets-api
- description: The Custom Fields API from beehiiv — 2 operation(s) for custom fields.
  name: beehiiv Custom Fields API
  slug: beehiiv-custom-fields-api
- description: The Data Deletion API from beehiiv — 2 operation(s) for data deletion.
  name: beehiiv Data Deletion API
  slug: beehiiv-data-deletion-api
- description: The engagements API from beehiiv — 1 operation(s) for engagements.
  name: beehiiv Engagements API
  slug: beehiiv-engagements-api
- description: The Newsletter List Subscriptions API from beehiiv — 3 operation(s) for newsletter list subscriptions.
  name: beehiiv Newsletter List Subscriptions API
  slug: beehiiv-newsletter-list-subscriptions-api
- description: The Newsletter Lists API from beehiiv — 2 operation(s) for newsletter lists.
  name: beehiiv Newsletter Lists API
  slug: beehiiv-newsletter-lists-api
- description: The oauth_users API from beehiiv — 1 operation(s) for oauth_users.
  name: beehiiv OAUTH Users API
  slug: beehiiv-oauth-users-api
- description: The podcasts API from beehiiv — 4 operation(s) for podcasts.
  name: beehiiv Podcasts API
  slug: beehiiv-podcasts-api
- description: The Polls API from beehiiv — 3 operation(s) for polls.
  name: beehiiv Polls API
  slug: beehiiv-polls-api
- description: The Post Templates API from beehiiv — 1 operation(s) for post templates.
  name: beehiiv Post Templates API
  slug: beehiiv-post-templates-api
- description: The Posts API from beehiiv — 5 operation(s) for posts.
  name: beehiiv Posts API
  slug: beehiiv-posts-api
- description: The Publications API from beehiiv — 2 operation(s) for publications.
  name: beehiiv Publications API
  slug: beehiiv-publications-api
- description: The Referral Program API from beehiiv — 1 operation(s) for referral program.
  name: beehiiv Referral Program API
  slug: beehiiv-referral-program-api
- description: The Segments API from beehiiv — 5 operation(s) for segments.
  name: beehiiv Segments API
  slug: beehiiv-segments-api
- description: The Subscription Tags API from beehiiv — 1 operation(s) for subscription tags.
  name: beehiiv Subscription Tags API
  slug: beehiiv-subscription-tags-api
- description: The Subscriptions API from beehiiv — 3 operation(s) for subscriptions.
  name: beehiiv Subscriptions API
  slug: beehiiv-subscriptions-api
- description: The Tiers API from beehiiv — 2 operation(s) for tiers.
  name: beehiiv Tiers API
  slug: beehiiv-tiers-api
- description: The workspaces API from beehiiv — 3 operation(s) for workspaces.
  name: beehiiv Workspaces API
  slug: beehiiv-workspaces-api
artifact_total: 97
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
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities API
  slug: open-beehiiv-subpackage-advertisement-opportunities-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_authors API
  slug: open-beehiiv-subpackage-authors-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_automationJourneys API
  slug: open-beehiiv-subpackage-automationjourneys-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_automations API
  slug: open-beehiiv-subpackage-automations-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_bulk_subscriptions API
  slug: open-beehiiv-subpackage-bulk-subscriptions-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_bulkSubscriptionUpdates API
  slug: open-beehiiv-subpackage-bulksubscriptionupdates-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_conditionSets API
  slug: open-beehiiv-subpackage-conditionsets-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_customFields API
  slug: open-beehiiv-subpackage-customfields-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_dataDeletion API
  slug: open-beehiiv-subpackage-datadeletion-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_engagements API
  slug: open-beehiiv-subpackage-engagements-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_newsletterLists API
  slug: open-beehiiv-subpackage-newsletterlists-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_newsletterListSubscriptions API
  slug: open-beehiiv-subpackage-newsletterlistsubscriptions-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_oauth_users API
  slug: open-beehiiv-subpackage-oauth-users-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_polls API
  slug: open-beehiiv-subpackage-polls-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_posts API
  slug: open-beehiiv-subpackage-posts-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_postTemplates API
  slug: open-beehiiv-subpackage-posttemplates-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_publications API
  slug: open-beehiiv-subpackage-publications-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_referralProgram API
  slug: open-beehiiv-subpackage-referralprogram-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_segments API
  slug: open-beehiiv-subpackage-segments-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_subscriptions API
  slug: open-beehiiv-subpackage-subscriptions-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_subscriptionTags API
  slug: open-beehiiv-subpackage-subscriptiontags-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_tiers API
  slug: open-beehiiv-subpackage-tiers-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_webhooks API
  slug: open-beehiiv-subpackage-webhooks-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_workspaces API
  slug: open-beehiiv-subpackage-workspaces-api
- collection_type: open
  name: API Reference
  slug: open-beehiiv
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/beehiiv-capability-edges.yml
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
  url: mcp/beehiiv-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.beehiiv.com/mcp
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
- group: build
  title: ''
  type: Packages
  url: packages/beehiiv-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beehiiv-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/beehiiv-api-catalog.json
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/beehiiv-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beehiiv-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/beehiiv-api-reference-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/beehiiv-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/beehiiv-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/beehiiv-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beehiiv-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.beehiiv.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/beehiiv-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/beehiiv-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/beehiiv-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/beehiiv-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/beehiiv-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/beehiiv-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: openapi/beehiiv-webhook-events-openapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.beehiiv.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kinlaneapi/beehiiv/overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beehiiv.com/tou
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beehiiv.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.beehiiv.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.beehiiv.com/login
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
  name: beehiiv MCP Server
  slug: beehiiv-mcp-server
- description: ''
  name: beehiiv MCP Server
  slug: beehiiv-mcp-server-2
- description: ''
  name: beehiiv MCP Server
  slug: beehiiv-mcp-server-3
modified: '2026-08-13'
name: beehiiv
nav: Providers
network: true
overview: 'beehiiv publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Authorizations API, Tokens API, Webhooks API, and 27 more. Tagged areas include Newsletter, Creator, Email, Subscription, and Publishing.


  The beehiiv catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  beehiiv''s developer surface includes authentication, pricing, documentation, API reference, getting-started guide, support, engineering blog, and 44 more developer resources.'
plans:
- name: Beehiiv Plans Pricing
  plan_count: 4
  slug: beehiiv-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Beehiiv Rate Limits
  slug: beehiiv-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: beehiiv API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: beehiiv-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: beehiiv API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: beehiiv-jsonschema-spectral-rules
scopes:
- name: Beehiiv Scopes
  scope_count: 0
  slug: beehiiv-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 70.7
  coverage:
    artifact_dirs: 29
    catalog_gap: 35.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 71.4
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 31.8
    operational_transparency: 55.3
  previous_composite: 71.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 54
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/screenshots/beehiiv-2026-06-20T173135.png
security:
- kind: authentication
  name: Beehiiv Authentication
  slug: beehiiv-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Beehiiv Domain Security
  slug: beehiiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Beehiiv Trust Center
  slug: beehiiv-trust-center
  summary_line: SOC 2 Type I
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
