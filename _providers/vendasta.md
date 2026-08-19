---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 203
  human_in_the_loop: 2
  name: Vendasta Agentic Access
  operation_count: 347
  slug: vendasta-agentic-access
  summary_line: 347 operations · 203 acting · 2 human-in-the-loop
api_count: 38
apis:
- description: The Account APIs allow you to perform actions against a single account that your application has been added to.
  name: Vendasta account API
  slug: vendasta-account-api
- description: 'The Activity API lets you inform us of new activity from your Marketplace App. It will be displayed in the user''s activity stream and used for notifications. Note: This endpoint has duplicate detectio'
  name: Vendasta activity API
  slug: vendasta-activity-api
- description: The Change Spend APIs allow interact with change spend requests, like resolving them by approving or rejecting
  name: Vendasta change_spend API
  slug: vendasta-change-spend-api
- description: The Customer APIs allow you to perform actions against customers of the account that your application has been added to.
  name: Vendasta customer API
  slug: vendasta-customer-api
- description: The executive report APIs are used to submit data to the executive report for a single app on an account.
  name: Vendasta executive_report API
  slug: vendasta-executive-report-api
- description: The Marketplace App APIs allow you to perform actions against your applications, as well as certain operations against all marketplace apps.
  name: Vendasta marketplace_app API
  slug: vendasta-marketplace-app-api
- description: The OAuth APIs allow applications to retrieve a bearer token that must be supplied with all API calls. See the Authentication documentation for more details.
  name: Vendasta oauth API
  slug: vendasta-oauth-api
- description: The User APIs allow you to perform operations against Vendasta Users. Each user has a unique identifier in the format UID-{}. This ID is guaranteed to stay the same, while the email associated to a us
  name: Vendasta user API
  slug: vendasta-user-api
- description: 'The Platform REST APIs are the core of the Vendasta API Gateway: business locations, sales accounts, users and their location permissions, orders and order custom fields, order fulfillment forms, subs'
  name: Vendasta Platform REST API
  slug: vendasta-platform-api
- description: A SCIM 2.0 implementation for provisioning and de-provisioning Vendasta users and groups from an external identity provider. Covers Users, Groups and System Operations (ServiceProviderConfig, Resource
  name: Vendasta SCIM 2.0 User Management API
  slug: vendasta-scim-api
- description: The CRM REST API for contacts, companies, opportunities, associations and custom objects, exposed as generic JSON:API resource operations under /org. Vendasta names the CRM API as the one Platform sur
  name: Vendasta CRM REST API
  slug: vendasta-crm-rest-api
- description: 'The CRM surface exposed through the gRPC reverse-proxy gateway: CRMService, CRMAssociationService, CRMCompanyService, CRMOpportunityService, CRMFieldSchemaService and CRMFieldSchemaCustomizationServic'
  name: Vendasta CRM API (gRPC gateway)
  slug: vendasta-crm-grpc-api
- description: 'Local SEO (formerly Listing Builder) product API: listing sync listings, listing scores, listing profiles and citations for a business location. Scope-gated with the `listing` OAuth2 scope.'
  name: Vendasta Local SEO REST API
  slug: vendasta-local-seo-api
- description: 'Advertising Intelligence product API: connected advertising accounts, account-level stats, campaign info and campaign stats across the ad channels a business runs. Scope-gated with the `advertising` O'
  name: Vendasta Advertising Intelligence REST API
  slug: vendasta-advertising-api
- description: Reputation AI product API for reading business location reviews collected across review sources. Scope-gated with the `reputation` OAuth2 scope.
  name: Vendasta Reputation REST API
  slug: vendasta-reputation-api
- description: 'The fuller Reputation surface through the gRPC gateway: ListingService, ReviewService and NetPromoterScoreService — 17 operations covering listings, reviews and NPS data for the business locations an '
  name: Vendasta Reputation API (gRPC gateway)
  slug: vendasta-reputation-grpc-api
- description: Customer Voice product API for sending review requests to a business location customers and managing the email/SMS templates those requests use. Scope-gated with the `reviews` OAuth2 scope.
  name: Vendasta Customer Voice REST API
  slug: vendasta-customer-voice-api
- description: Social AI product API for connected social profiles and messages on a business location. Published as OpenAPI 3.1.0. Scope-gated with the `social` OAuth2 scope.
  name: Vendasta Social REST API
  slug: vendasta-social-api
- description: The Business context API covering the Customer List for a business location — list, get, update and delete customers. Vendasta has deprecated the Customer List in favour of the CRM; this surface is ma
  name: Vendasta Business REST API
  slug: vendasta-business-api
- description: 'The Data Glossary context: glossary contexts and glossary terms, the vocabulary layer that explains what similarly named fields mean in each part of the Vendasta platform (a sales view of a business i'
  name: Vendasta Data Glossary API
  slug: vendasta-glossary-api
- description: API for the AI Employees (AI assistants) that Vendasta runs on a partner platform — receptionist, reputation specialist, sales assistant, social media manager and custom AI employees. Scope-gated with
  name: Vendasta AI Employees API
  slug: vendasta-ai-employees-api
- description: 'The knowledge (embeddings) API that grounds Vendasta AI Employees: upsert a knowledge source into an account or partner knowledge base, request a signed URL for direct file upload, remove a source, an'
  name: Vendasta AI Knowledge API
  slug: vendasta-ai-knowledge-api
- description: Conversations AI service API for the unified inbox that centralises SMS, web chat, voice and other channels. Scope-gated with `conversation`, `conversation:read` and `conversation.widget`.
  name: Vendasta Conversation API
  slug: vendasta-conversation-api
- description: The Composer service on the Vendasta gRPC gateway, used for composing content within the platform.
  name: Vendasta Composer API
  slug: vendasta-composer-api
- description: Forms service API for creating and managing the forms a business publishes and the submissions they collect.
  name: Vendasta Forms API
  slug: vendasta-forms-api
- description: Meetings (CalendarHero) API for creating meetings, adding contacts, messaging and searching. Scope-gated with the `meeting` OAuth2 scope.
  name: Vendasta Meetings API
  slug: vendasta-meetings-api
- description: Sales Orders service and its auxiliary field schema, exposed through the gRPC gateway — the order surface behind the platform marketplace.
  name: Vendasta Sales Orders API
  slug: vendasta-sales-orders-api
- description: 'Social Posts services: SocialPosts, SocialPostsV2, the WordPress plugin service and the blog posts service — publishing and scheduling social and blog content for a business.'
  name: Vendasta Social Posts API
  slug: vendasta-social-posts-api
- description: Social Drafts service for creating, listing and managing draft social content before it is scheduled or published.
  name: Vendasta Social Drafts API
  slug: vendasta-social-drafts-api
- description: 'Listing Products services through the gRPC gateway: ListingProductsService, ListingSourceService, ListingProfileService, SEOService and Citations — the fuller local-listings surface behind Local SEO.'
  name: Vendasta Listing Products API
  slug: vendasta-listing-products-api
- description: Analytics service for multi-location brands and franchises, rolling product performance up across the locations under one partner.
  name: Vendasta Multi-Location Analytics API
  slug: vendasta-multi-location-analytics-api
- description: The VAnalytics service on the gRPC gateway, exposing Vendasta platform analytics data.
  name: Vendasta Vanalytics API
  slug: vendasta-vanalytics-api
- description: Site detail service for Vendasta managed WordPress hosting (Website Pro), which runs client WordPress sites on Google Cloud.
  name: Vendasta WordPress Hosting API
  slug: vendasta-wordpress-hosting-api
- description: Website Pro admin center services — search and WordPress administration across the sites a partner manages.
  name: Vendasta Website Pro Admin Center API
  slug: vendasta-wsp-admin-center-api
- description: Website Pro monitoring service for uptime and health signals on managed WordPress sites.
  name: Vendasta Website Pro Monitor API
  slug: vendasta-wsp-monitor-api
- description: Website Pro site information and cache services for managed WordPress sites.
  name: Vendasta Website Pro Site Info API
  slug: vendasta-wsp-site-info-api
- description: Website Pro SiteManager support tooling used to diagnose and operate managed WordPress sites.
  name: Vendasta Website Pro Support Tools API
  slug: vendasta-wsp-support-tools-api
- description: Website Pro site options and PageSpeed services for managed WordPress sites.
  name: Vendasta Website Pro WP Manager API
  slug: vendasta-wsp-wp-manager-api
artifact_total: 57
asyncapis:
- description: ''
  name: Vendasta Webhooks
  slug: vendasta-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account API
  slug: open-vendasta-account-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account activity API
  slug: open-vendasta-activity-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account change_spend API
  slug: open-vendasta-change-spend-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account customer API
  slug: open-vendasta-customer-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account executive_report API
  slug: open-vendasta-executive-report-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account marketplace_app API
  slug: open-vendasta-marketplace-app-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account oauth API
  slug: open-vendasta-oauth-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account user API
  slug: open-vendasta-user-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/vendasta-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vendasta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vendasta-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vendasta-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vendasta-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/vendasta-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vendasta-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vendasta-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vendasta-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/vendasta-marketplace-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/vendasta-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vendasta-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vendasta-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vendasta-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vendasta-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vendasta-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.vendasta.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.vendasta.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.vendasta.com/vendor
- group: docs
  title: ''
  type: APIReference
  url: https://developers.vendasta.com/api/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.vendasta.com/vendor
- group: auth
  title: ''
  type: Security
  url: https://www.vendasta.com/developers/vulnerability-disclosure-program/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.vendasta.com/
- group: operate
  title: ''
  type: Support
  url: https://support.vendasta.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vendasta.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vendasta.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trust.vendasta.com/resources?name=terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trust.vendasta.com/resources?name=customer-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vendasta.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/vendasta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vendasta-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vendasta-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vendasta-scopes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vendasta-webhooks.yml
- group: build
  title: ''
  type: CLI
  url: cli/vendasta-cli.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/vendasta-error-codes.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vendasta-platform-overlay.yaml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/vendasta/api-gateway-docs/blob/master/docs/Overview/Versioning.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vendasta
- group: start
  title: ''
  type: SignUp
  url: https://signup.vendasta.com/
- group: start
  title: ''
  type: Login
  url: https://login-prod.apigateway.co/account-selector/login?serviceProviderId=AA
- group: other
  title: ''
  type: SCIM
  url: openapi/vendasta-scim-openapi.yml
created: '2026-07-17'
description: 'Vendasta is an end-to-end commerce and operating platform that lets agencies, media companies, banks, telcos and other channel partners sell digital products and services to small and medium-sized businesses under their own brand. The platform bundles a white-label Marketplace of resellable products, a Business App client dashboard, CRM and sales pipeline, marketing automation, billing, managed WordPress hosting and a family of AI Employees. Vendasta exposes two distinct API surfaces. The API Gateway at prod.apigateway.co is the current one: 30 first-party OpenAPI documents covering Platform (business locations, users, orders, subscriptions, automations), CRM, SCIM 2.0 user provisioning, Local SEO, Reputation, Social, Customer Voice, Advertising Intelligence, AI Employees, AI Knowledge, Meetings, Forms and Website Pro — JSON:API over application/vnd.api+json, secured by OAuth2 with 73 published scopes, deliberately unversioned with per-operation x-lifecycle maturity. The legacy
  Marketplace API V1 at developers.vendasta.com/api/v1 remains for vendor apps: accounts, users, customers, add-ons, activities, executive reports and file groups, plus eight JWT-signed Marketplace webhooks. Headquartered in Saskatoon, Canada, Vendasta was founded in 2008.'
image: https://www.vendasta.com/wp-content/uploads/2021/03/vendasta-logo.png
layout: provider
mcp_servers:
- description: ''
  name: vendasta-mcp.yml
  slug: vendasta-mcpyml
modified: '2026-08-13'
name: Vendasta
nav: Providers
network: true
overview: 'Vendasta publishes 38 APIs on the [APIs.io](https://apis.io/) network, including account API, activity API, change_spend API, and 35 more. Tagged areas include Company, SaaS, Marketplace, SMB, and White Label.


  The Vendasta catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vendasta''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 36 more developer resources.'
plans:
- name: Vendasta Plans Pricing
  plan_count: 4
  slug: vendasta-plans-pricing
random_paper: 109
rate_limits:
- limit_count: 2
  name: Vendasta Rate Limits
  slug: vendasta-rate-limits
scopes:
- name: Vendasta Scopes
  scope_count: 73
  slug: vendasta-scopes
  summary_line: 73 scopes
score:
  band: strong
  composite: 64.8
  delta: -5.6
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 30.3
    contract_quality: 61.2
    developer_ergonomics: 44.6
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 81.6
  previous_composite: 70.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 96.6
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/vendasta/refs/heads/main/screenshots/vendasta-2026-08-17T080435.png
security:
- kind: authentication
  name: Vendasta Authentication
  slug: vendasta-authentication
  summary_line: oauth2/http/openIdConnect · 6 schemes
- kind: domain-security
  name: Vendasta Domain Security
  slug: vendasta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vendasta Vulnerability Disclosure
  slug: vendasta-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Vendasta Trust Center
  slug: vendasta-trust-center
  summary_line: SOC 2
slug: vendasta
tags:
- Company
- SaaS
- Marketplace
- SMB
- White Label
- Reseller
- Marketing
- CRM
- Digital Agency
- Platform
website: https://www.vendasta.com
---
