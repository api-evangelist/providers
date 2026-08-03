---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Meta Agentic Access
  operation_count: 8
  slug: meta-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 19
apis:
- description: Access Instagram user profiles, media, and account information for Business and Creator accounts via the Instagram Graph API.
  name: Instagram Graph API - User
  slug: instagram-graph-api-user
- description: Access and manage Facebook Page settings, content, posts, and metrics using the Graph API Page node.
  name: Facebook Graph API - Page
  slug: facebook-graph-api-page
- description: Create, read, update, and delete posts on Facebook using the Graph API Post node.
  name: Facebook Graph API - Post
  slug: facebook-graph-api-post
- description: Manage Facebook Groups including members, posts, and settings using the Graph API Group node.
  name: Facebook Graph API - Group
  slug: facebook-graph-api-group
- description: Access and manage Facebook Events including details, attendees, and RSVPs using the Graph API Event node.
  name: Facebook Graph API - Event
  slug: facebook-graph-api-event
- description: Create, manage, and optimize advertising campaigns across Facebook, Instagram, and Audience Network programmatically.
  name: Facebook Marketing API
  slug: facebook-marketing-api
- description: Send web, app, and offline conversion events directly from your server to Meta for improved ad measurement and optimization.
  name: Meta Conversions API
  slug: conversions-api
- description: Search and retrieve publicly visible ads across Meta platforms for transparency and research purposes via the ads_archive Graph API endpoint.
  name: Meta Ad Library API
  slug: ad-library-api
- description: Send and receive messages, manage phone numbers, and build messaging experiences on WhatsApp using Meta's cloud-hosted API.
  name: WhatsApp Cloud API
  slug: whatsapp-cloud-api
- description: Manage WhatsApp Business accounts, phone numbers, message templates, and business profiles programmatically.
  name: WhatsApp Business Management API
  slug: whatsapp-business-management-api
- description: Build messaging experiences on Facebook Messenger including chatbots, rich media messages, and customer service integrations.
  name: Messenger Platform API
  slug: messenger-platform-api
- description: Create and manage content, retrieve profiles, and access insights on Meta's Threads social media platform.
  name: Threads API
  slug: threads-api
- description: Publish photos, videos, carousels, reels, and stories to Instagram Business and Creator accounts programmatically.
  name: Instagram Graph API - Content Publishing
  slug: instagram-graph-api-content-publishing
- description: Send and receive messages on Instagram using the Messenger Platform, enabling customer service and automated messaging for Business accounts.
  name: Instagram Messaging API
  slug: instagram-messaging-api
- description: Programmatic access to the full public content archive from Facebook, Instagram, and Threads for qualified academic and non-profit researchers.
  name: Meta Content Library API
  slug: meta-content-library-api
- description: Access Meta's Llama large language models including Llama 4 and Llama 3 family for building AI-powered applications via a hosted API.
  name: Meta Llama API
  slug: llama-api
- description: Manage user membership in custom audiences
  name: Meta Custom Audiences API
  slug: meta-custom-audiences-api
- description: Page-related user operations
  name: Meta Pages API
  slug: meta-pages-api
- description: Operations on the User node
  name: Meta Users API
  slug: meta-users-api
arazzos:
- description: Resolve the authenticated user and add them to a custom audience.
  name: Meta Add Current User To Audience
  slug: meta-add-current-user-to-audience-workflow
- description: Resolve the current user, read their full profile node, then pull their feed.
  name: Meta Audit Current User
  slug: meta-audit-current-user-workflow
- description: Snapshot a user, remove them from a custom audience, then delete the test user.
  name: Meta Decommission User Account
  slug: meta-decommission-user-account-workflow
- description: Resolve the current user from the access token and read their timeline feed.
  name: Meta Get Current User Feed
  slug: meta-get-current-user-feed-workflow
- description: Confirm a user exists, then add a hashed payload to a custom audience.
  name: Meta Onboard User To Audience
  slug: meta-onboard-user-to-audience-workflow
- description: Configure a test user with an update, then delete the test user to clean up.
  name: Meta Provision Then Cleanup Test User
  slug: meta-provision-then-cleanup-test-user-workflow
- description: Read a target user's feed and resolve the caller's own identity for context.
  name: Meta Read User Feed And Identity
  slug: meta-read-user-feed-and-identity-workflow
- description: Read a specific user's profile and then pull their timeline feed.
  name: Meta Read User Then Feed
  slug: meta-read-user-then-feed-workflow
- description: Resolve the caller, add a new cohort to an audience, then remove stale members.
  name: Meta Refresh Audience Cohort
  slug: meta-refresh-audience-cohort-workflow
- description: Add a fresh set of hashed users to a custom audience and remove a stale set.
  name: Meta Sync Custom Audience Membership
  slug: meta-sync-custom-audience-membership-workflow
- description: Unblock a user from a page, then add them to a custom audience.
  name: Meta Unblock And Add To Audience
  slug: meta-unblock-and-add-to-audience-workflow
- description: Resolve the current user, update their profile, then read it back to confirm.
  name: Meta Update Current User Profile
  slug: meta-update-current-user-profile-workflow
- description: Read a user, branch on whether it exists, and apply an update when found.
  name: Meta Verify And Update User
  slug: meta-verify-and-update-user-workflow
artifact_total: 63
collections:
- collection_type: postman
  name: Meta Graph API - User
  slug: postman-meta
- collection_type: open
  name: Meta Graph API - User
  slug: open-meta
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meta-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meta-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meta-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/meta-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/meta-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meta-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/meta-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/meta-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meta-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/meta-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/meta-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/meta-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/meta-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/meta-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/meta-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/meta-cli.yml
- group: design
  title: ''
  type: Components
  url: components/meta-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/meta-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/meta-sandbox.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/meta/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-add-current-user-to-audience-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-audit-current-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-decommission-user-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-get-current-user-feed-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-onboard-user-to-audience-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-provision-then-cleanup-test-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-read-user-feed-and-identity-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-read-user-then-feed-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-refresh-audience-cohort-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-sync-custom-audience-membership-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-unblock-and-add-to-audience-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-update-current-user-profile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/meta-verify-and-update-user-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meta
- group: start
  title: ''
  type: Portal
  url: https://developers.facebook.com/?no_redirect=1
- group: docs
  title: ''
  type: Documentation
  url: https://developers.facebook.com/docs/
- group: other
  title: ''
  type: Overview
  url: https://developers.facebook.com/docs/graph-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.facebook.com/docs/graph-api/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.facebook.com/docs/facebook-login
- group: auth
  title: ''
  type: Authentication
  url: https://developers.facebook.com/docs/access-tokens
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.facebook.com/docs/graph-api/changelog
- group: docs
  title: ''
  type: Reference
  url: https://developers.facebook.com/docs/graph-api/reference
- group: company
  title: ''
  type: Blog
  url: https://developers.facebook.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://metastatus.com/
- group: start
  title: ''
  type: Console
  url: https://developers.facebook.com/apps/
- group: start
  title: ''
  type: Signup
  url: https://developers.facebook.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.facebook.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.facebook.com/privacy/explanation
- group: operate
  title: ''
  type: Support
  url: https://developers.facebook.com/support/
- group: other
  title: ''
  type: Bugs
  url: https://developers.facebook.com/support/bugs/
- group: operate
  title: ''
  type: Forums
  url: https://developers.facebook.com/community/
- group: operate
  title: ''
  type: FAQ
  url: https://developers.facebook.com/support/faq/
- group: other
  title: ''
  type: Explorer
  url: https://developers.facebook.com/tools/explorer/
- group: build
  title: ''
  type: Tools
  url: https://developers.facebook.com/tools/
- group: other
  title: ''
  type: Applications
  url: https://developers.facebook.com/apps/
- group: operate
  title: ''
  type: Incident Report
  url: https://developers.facebook.com/incident/report/
- group: company
  title: ''
  type: Newsletter
  url: https://developers.facebook.com/m/signup/
- group: learn
  title: ''
  type: Videos
  url: https://developers.facebook.com/videos/
- group: design
  title: ''
  type: Webhooks
  url: https://developers.facebook.com/docs/graph-api/webhooks
- group: auth
  title: ''
  type: Security
  url: https://developers.facebook.com/docs/facebook-login/security
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting/
- group: design
  title: ''
  type: Versioning
  url: https://developers.facebook.com/docs/graph-api/guides/versioning
- group: design
  title: ''
  type: Pagination
  url: https://developers.facebook.com/docs/graph-api/results
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/facebook
- group: other
  title: ''
  type: Open Source
  url: https://opensource.fb.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/facebook-graph-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/facebook/facebook-python-business-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/facebook/facebook-nodejs-business-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/facebook/facebook-php-business-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/facebook/facebook-java-business-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/facebook/facebook-ruby-business-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/facebook/facebook-ios-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/facebook/facebook-android-sdk
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/user.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/page.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/post.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ad-campaign.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/message.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/media.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/meta-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: ''
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.facebook.com/docs/graph-api/overview/rate-limiting/
- group: design
  title: ''
  type: Versioning
  url: https://developers.facebook.com/docs/graph-api/guides/versioning
- group: design
  title: ''
  type: Pagination
  url: ''
- group: design
  title: ''
  type: Pagination
  url: ''
- group: design
  title: ''
  type: Pagination
  url: ''
created: '2024-04-14T00:00:00.000Z'
description: Collection of Meta (Facebook) platform APIs for social networking, messaging, advertising, content publishing, AI, and developer tools across Facebook, Instagram, WhatsApp, Threads, and Messenger.
features:
- 'Meta (Facebook + Instagram + WhatsApp + Threads): hundreds of services across Social + Messaging + Ads'
- 'Detailed pricing: see https://developers.facebook.com/docs/marketing-api'
- 'Service: Facebook Graph API'
- 'Service: Marketing API'
- 'Service: Instagram Graph API'
- 'Service: Instagram Basic Display API'
- 'Service: WhatsApp Business Platform / Cloud API'
- 'Service: Threads API'
- 'Service: Messenger Platform'
- 'Service: Workplace by Meta API (sunset)'
- 'Service: Meta Conversion API (server-side events)'
finops:
- name: Meta Finops
  service_category: Social + Messaging + Ads
  slug: meta-finops
graphqls:
- description: Meta's Graph API is a graph-traversal API modeled around nodes (objects), edges (connections between objects), and fields (properties of objects). While it does not expose a strict GraphQL SDL endpoin
  name: Meta Graph API — GraphQL Conceptual Schema
  slug: meta-graphql
image: https://about.meta.com/brand/resources/meta/our-logo/
json_schemas:
- name: Meta Marketing API Ad Campaign
  property_count: 24
  slug: ad-campaign
- name: Meta Graph API Media
  property_count: 26
  slug: media
- name: Meta Messaging API Message
  property_count: 17
  slug: message
- name: Meta Graph API Page
  property_count: 32
  slug: page
- name: Meta Graph API Post
  property_count: 28
  slug: post
- name: Meta Graph API User
  property_count: 26
  slug: user
jsonld:
- class_count: 0
  name: Meta Context
  property_count: 6
  slug: meta-context
layout: provider
mcp_servers:
- description: ''
  name: meta-mcp.yml
  slug: meta-mcpyml
modified: '2026-06-20'
name: Meta
nav: Providers
network: true
overview: 'Meta publishes 3 APIs on the [APIs.io](https://apis.io/) network: Custom Audiences API, Pages API, and Users API. Tagged areas include Advertising, Analytics, Artificial Intelligence, Messaging, and Social.


  The Meta catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Meta''s developer surface includes authentication, changelog, CLI, sandbox, developer portal, documentation, getting-started guide, and 76 more developer resources.'
plans:
- name: Meta Plans Pricing
  plan_count: 3
  slug: meta-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 2
  name: Meta Rate Limits
  slug: meta-rate-limits
rules:
- name: Meta API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: meta-jsonschema-spectral-rules
scopes:
- name: Meta Scopes
  scope_count: 15
  slug: meta-scopes
  summary_line: 15 scopes · implicit
score:
  band: exemplar
  composite: 71.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.2
    developer_ergonomics: 93.5
    discoverability: 74.1
    governance: 69.8
    operational_transparency: 76.3
  previous_composite: 71.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 66.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meta/refs/heads/main/screenshots/meta-2026-06-20T185238.png
security:
- kind: authentication
  name: Meta Authentication
  slug: meta-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Meta Domain Security
  slug: meta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Meta Vulnerability Disclosure
  slug: meta-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: meta
tags:
- Advertising
- Analytics
- Artificial Intelligence
- Messaging
- Social
- Social Media
- Virtual Reality
website: https://developers.facebook.com/?no_redirect=1
---
