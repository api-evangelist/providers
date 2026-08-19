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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 65
  human_in_the_loop: 1
  name: Optimizely Agentic Access
  operation_count: 135
  slug: optimizely-agentic-access
  summary_line: 135 operations · 65 acting · 1 human-in-the-loop
api_count: 50
apis:
- description: The core Optimizely REST API v2 shared by Web Experimentation and Feature Experimentation — projects, experiments, campaigns, audiences, pages, events, attributes, environments, features, groups, exte
  name: Optimizely Experimentation REST API v2
  slug: experimentation-rest-api-v2
- description: Feature Experimentation Flags v1 — flags, variations, variable definitions, rulesets, rules, holdouts, groups, custom fields, environments and reports. 55 operations, RFC 9457 problem+json errors, res
  name: Optimizely Feature Experimentation Flags API v1
  slug: feature-experimentation-flags-api
- description: Schedule future flag ruleset changes and read environment change-approval settings. Five operations. Harvested verbatim from the provider's published OpenAPI 2026-08-13.
  name: Optimizely Flags Scheduling API
  slug: flags-scheduling-api
- description: Granular roles and permissions for Feature Experimentation — per-entity permissions for users and teams, plus team management. Introduced 2025-03-18. Harvested verbatim from the provider's published O
  name: Optimizely Permission Service API
  slug: permission-service-api
- description: Optimizely Agent is a stand-alone open-source microservice that consolidates the Feature Experimentation SDK surface behind a REST API — config, datafile, decide, track, activate, override, lookup, sa
  name: Optimizely Agent API
  slug: agent-api
- description: The Experimentation data-ingest endpoint. Accepts decision and conversion event payloads from SDKs and server-side integrations. Regional hosts for US and EU. Harvested verbatim from the provider's pu
  name: Optimizely Event API
  slug: event-api
- description: Performance Edge decisioning endpoint used by Optimizely's edge delivery clients. Harvested verbatim from the provider's published OpenAPI 2026-08-13.
  name: Optimizely Edge Decider API
  slug: edge-decider-api
- description: The Optimizely customer data platform, formerly Zaius. Eleven separately published OpenAPI documents covering customer profiles, events, objects, products, orders, lists and subscriptions, consent, re
  name: Optimizely Data Platform (ODP) API v3
  slug: data-platform-api
- description: Optimizely Graph — the GraphQL content query layer over CMS, Commerce and connected sources, with a REST management surface for content ingestion, types, synonyms and best bets. Two published document
  name: Optimizely Graph API
  slug: graph-api
- description: The CMP Open REST API — campaigns, tasks, work requests, templates, content, library assets (images, videos, raw files), users and settings. 115 paths, OAuth 2.0 with both authorization code and clien
  name: Optimizely Content Marketing Platform (CMP) API v3
  slug: content-marketing-platform-api
- description: Email and omnichannel campaign management, formerly Episerver Campaign and optivo broadmail — mailings, smart campaigns and their nodes, recipient lists, transactional mail, unsubscribes and webhooks.
  name: Optimizely Campaign REST API
  slug: campaign-rest-api
- description: B2B commerce, formerly Insite Software. Three published documents — Admin API V1 (1,577 paths), Storefront API V1 (168 paths) and Storefront API V2 (15 paths, running in parallel with V1 rather than s
  name: Optimizely Configured Commerce API
  slug: configured-commerce-api
- description: Read-only content delivery from Optimizely CMS — content by identifier, children, ancestors, and site metadata. Deployed inside the customer's own CMS instance, so the base URL is the customer's CMS h
  name: Optimizely CMS Content Delivery API v3.0
  slug: cms-content-delivery-api
- description: Content recommendation delivery, formerly Idio. Thirteen paths covering content, topics, users and recommendation delivery, authenticated with a key query parameter. The spec declares a templated serv
  name: Optimizely Content Recommendations API
  slug: content-recommendations-api
- description: Deployment and environment management for Optimizely Digital Experience Platform (PaaS), served from the Episerver PaaS portal. Nine paths. Harvested verbatim 2026-08-13.
  name: Optimizely DXP Cloud API
  slug: dxp-cloud-api
- description: Optimizely's hosted remote Model Context Protocol server for Web and Feature Experimentation, on the Opal MCP platform. Tools are prefixed exp_ and cover querying projects/flags/experiments/environmen
  name: Optimizely Remote MCP Server — Experimentation
  slug: mcp-experimentation
- description: Manage campaign assets such as images and media files.
  name: Optimizely Assets API
  slug: optimizely-assets-api
- description: Manage custom attributes used for audience targeting and segmentation.
  name: Optimizely Attributes API
  slug: optimizely-attributes-api
- description: Create and manage audience segments for targeting experiments and rollouts.
  name: Optimizely Audiences API
  slug: optimizely-audiences-api
- description: Manage content campaigns and editorial calendar entries.
  name: Optimizely Campaigns API
  slug: optimizely-campaigns-api
- description: Manage catalog entries including products, variants, packages, and bundles.
  name: Optimizely Catalog Entries API
  slug: optimizely-catalog-entries-api
- description: Manage relationships between catalog entries and nodes.
  name: Optimizely Catalog Entry Relations API
  slug: optimizely-catalog-entry-relations-api
- description: Manage catalog nodes (categories) for organizing entries.
  name: Optimizely Catalog Nodes API
  slug: optimizely-catalog-nodes-api
- description: Manage product catalogs that organize commerce content.
  name: Optimizely Catalogs API
  slug: optimizely-catalogs-api
- description: Manage content items including articles and other content types within the CMP content repository.
  name: Optimizely Content API
  slug: optimizely-content-api
- description: Retrieve available content type definitions.
  name: Optimizely Content Types API
  slug: optimizely-content-types-api
- description: Manage customer accounts and contact information.
  name: Optimizely Customers API
  slug: optimizely-customers-api
- description: Manage environments within a project for developing, staging, and deploying flag configurations.
  name: Optimizely Environments API
  slug: optimizely-environments-api
- description: Send customer events to ODP for tracking actions, behaviors, and interactions across channels.
  name: Optimizely Events API
  slug: optimizely-events-api
- description: Create and manage A/B test experiments on top of feature flags.
  name: Optimizely Experiments API
  slug: optimizely-experiments-api
- description: Manage reusable extensions that encapsulate experiment logic and visual changes.
  name: Optimizely Extensions API
  slug: optimizely-extensions-api
- description: Manage features with variables used in feature flag configurations.
  name: Optimizely Features API
  slug: optimizely-features-api
- description: Create and manage feature flags with variables and variations for controlled rollouts and experimentation.
  name: Optimizely Flags API
  slug: optimizely-flags-api
- description: Execute GraphQL queries against the Optimizely content graph to retrieve and search content.
  name: Optimizely GraphQL API
  slug: optimizely-graphql-api
- description: Manage labels used for categorizing and organizing content.
  name: Optimizely Labels API
  slug: optimizely-labels-api
- description: Manage mailing lists used for campaign distribution.
  name: Optimizely Mailing Lists API
  slug: optimizely-mailing-lists-api
- description: Create, update, and manage objects such as products, orders, and custom entities in ODP.
  name: Optimizely Objects API
  slug: optimizely-objects-api
- description: Manage purchase orders, cart operations, and order workflows.
  name: Optimizely Orders API
  slug: optimizely-orders-api
- description: Manage page definitions that specify which URLs or conditions trigger experiments.
  name: Optimizely Pages API
  slug: optimizely-pages-api
- description: Create, update, and retrieve customer profiles with unified identity resolution.
  name: Optimizely Profiles API
  slug: optimizely-profiles-api
- description: Manage Feature Experimentation projects that serve as containers for flags, experiments, and environments.
  name: Optimizely Projects API
  slug: optimizely-projects-api
- description: Manage recipients and recipient lists for email campaigns.
  name: Optimizely Recipients API
  slug: optimizely-recipients-api
- description: Manage rulesets that define which variation a flag delivers to visitors within a given environment.
  name: Optimizely Rulesets API
  slug: optimizely-rulesets-api
- description: Manage the ODP schema including domain objects and their fields.
  name: Optimizely Schema API
  slug: optimizely-schema-api
- description: Query customer segments and audience definitions.
  name: Optimizely Segments API
  slug: optimizely-segments-api
- description: Retrieve site definitions including language settings and configuration.
  name: Optimizely Sites API
  slug: optimizely-sites-api
- description: Manage smart campaigns that automate multi-step marketing workflows.
  name: Optimizely Smart Campaigns API
  slug: optimizely-smart-campaigns-api
- description: Manage content tasks, assignments, and workflow steps within the content marketing platform.
  name: Optimizely Tasks API
  slug: optimizely-tasks-api
- description: Send transactional emails triggered by recipient actions or events.
  name: Optimizely Transactional Mail API
  slug: optimizely-transactional-mail-api
- description: Manage unsubscribe lists for opt-out recipients.
  name: Optimizely Unsubscribes API
  slug: optimizely-unsubscribes-api
artifact_total: 238
asyncapis:
- description: The Optimizely Content Marketing Platform (CMP) provides webhook notifications when content events occur, such as when assets are published, tasks are completed or modified, and content items are upda
  name: Optimizely CMP Webhooks
  slug: optimizely-cmp-asyncapi
- description: Optimizely Feature Experimentation provides webhook notifications when configuration changes occur, such as datafile updates. Webhooks notify external servers of changes, eliminating the need to const
  name: Optimizely Feature Experimentation Webhooks
  slug: optimizely-feature-experimentation-asyncapi
- description: ''
  name: Optimizely Webhooks
  slug: optimizely-webhooks
collections:
- collection_type: postman
  name: Optimizely Campaign REST Assets API
  slug: postman-optimizely-assets-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Attributes API
  slug: postman-optimizely-attributes-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Audiences API
  slug: postman-optimizely-audiences-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Campaigns API
  slug: postman-optimizely-campaigns-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Catalog Entries API
  slug: postman-optimizely-catalog-entries-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Catalog Entry Relations API
  slug: postman-optimizely-catalog-entry-relations-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Catalog Nodes API
  slug: postman-optimizely-catalog-nodes-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Catalogs API
  slug: postman-optimizely-catalogs-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Content API
  slug: postman-optimizely-content-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Content Types API
  slug: postman-optimizely-content-types-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Customers API
  slug: postman-optimizely-customers-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Environments API
  slug: postman-optimizely-environments-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Events API
  slug: postman-optimizely-events-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Experiments API
  slug: postman-optimizely-experiments-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Extensions API
  slug: postman-optimizely-extensions-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Features API
  slug: postman-optimizely-features-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Flags API
  slug: postman-optimizely-flags-api
- collection_type: postman
  name: Optimizely Campaign REST Assets GraphQL API
  slug: postman-optimizely-graphql-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Labels API
  slug: postman-optimizely-labels-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Mailing Lists API
  slug: postman-optimizely-mailing-lists-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Objects API
  slug: postman-optimizely-objects-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Orders API
  slug: postman-optimizely-orders-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Pages API
  slug: postman-optimizely-pages-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Profiles API
  slug: postman-optimizely-profiles-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Projects API
  slug: postman-optimizely-projects-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Recipients API
  slug: postman-optimizely-recipients-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Rulesets API
  slug: postman-optimizely-rulesets-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Schema API
  slug: postman-optimizely-schema-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Segments API
  slug: postman-optimizely-segments-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Sites API
  slug: postman-optimizely-sites-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Smart Campaigns API
  slug: postman-optimizely-smart-campaigns-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Tasks API
  slug: postman-optimizely-tasks-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Transactional Mail API
  slug: postman-optimizely-transactional-mail-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Unsubscribes API
  slug: postman-optimizely-unsubscribes-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Optimizely Campaign REST Assets API
  slug: open-optimizely-assets-api
- collection_type: open
  name: Optimizely Campaign REST Assets Attributes API
  slug: open-optimizely-attributes-api
- collection_type: open
  name: Optimizely Campaign REST Assets Audiences API
  slug: open-optimizely-audiences-api
- collection_type: open
  name: Optimizely Campaign REST API
  slug: open-optimizely-campaign
- collection_type: open
  name: Optimizely Campaign REST Assets Campaigns API
  slug: open-optimizely-campaigns-api
- collection_type: open
  name: Optimizely Campaign REST Assets Catalog Entries API
  slug: open-optimizely-catalog-entries-api
- collection_type: open
  name: Optimizely Campaign REST Assets Catalog Entry Relations API
  slug: open-optimizely-catalog-entry-relations-api
- collection_type: open
  name: Optimizely Campaign REST Assets Catalog Nodes API
  slug: open-optimizely-catalog-nodes-api
- collection_type: open
  name: Optimizely Campaign REST Assets Catalogs API
  slug: open-optimizely-catalogs-api
- collection_type: open
  name: Optimizely CMP Open REST API
  slug: open-optimizely-cmp
- collection_type: open
  name: Optimizely Commerce Service API
  slug: open-optimizely-commerce-service
- collection_type: open
  name: Optimizely Campaign REST Assets Content API
  slug: open-optimizely-content-api
- collection_type: open
  name: Optimizely Content Delivery API
  slug: open-optimizely-content-delivery
- collection_type: open
  name: Optimizely Content Management API
  slug: open-optimizely-content-management
- collection_type: open
  name: Optimizely Campaign REST Assets Content Types API
  slug: open-optimizely-content-types-api
- collection_type: open
  name: Optimizely Campaign REST Assets Customers API
  slug: open-optimizely-customers-api
- collection_type: open
  name: Optimizely Data Platform REST API
  slug: open-optimizely-data-platform
- collection_type: open
  name: Optimizely Campaign REST Assets Environments API
  slug: open-optimizely-environments-api
- collection_type: open
  name: Optimizely Campaign REST Assets Events API
  slug: open-optimizely-events-api
- collection_type: open
  name: Optimizely Campaign REST Assets Experiments API
  slug: open-optimizely-experiments-api
- collection_type: open
  name: Optimizely Campaign REST Assets Extensions API
  slug: open-optimizely-extensions-api
- collection_type: open
  name: Optimizely Feature Experimentation REST API
  slug: open-optimizely-feature-experimentation
- collection_type: open
  name: Optimizely Campaign REST Assets Features API
  slug: open-optimizely-features-api
- collection_type: open
  name: Optimizely Campaign REST Assets Flags API
  slug: open-optimizely-flags-api
- collection_type: open
  name: Optimizely Graph API
  slug: open-optimizely-graph
- collection_type: open
  name: Optimizely Campaign REST Assets GraphQL API
  slug: open-optimizely-graphql-api
- collection_type: open
  name: Optimizely Campaign REST Assets Labels API
  slug: open-optimizely-labels-api
- collection_type: open
  name: Optimizely Campaign REST Assets Mailing Lists API
  slug: open-optimizely-mailing-lists-api
- collection_type: open
  name: Optimizely Campaign REST Assets Objects API
  slug: open-optimizely-objects-api
- collection_type: open
  name: Optimizely Campaign REST Assets Orders API
  slug: open-optimizely-orders-api
- collection_type: open
  name: Optimizely Campaign REST Assets Pages API
  slug: open-optimizely-pages-api
- collection_type: open
  name: Optimizely Campaign REST Assets Profiles API
  slug: open-optimizely-profiles-api
- collection_type: open
  name: Optimizely Campaign REST Assets Projects API
  slug: open-optimizely-projects-api
- collection_type: open
  name: Optimizely Campaign REST Assets Recipients API
  slug: open-optimizely-recipients-api
- collection_type: open
  name: Optimizely Campaign REST Assets Rulesets API
  slug: open-optimizely-rulesets-api
- collection_type: open
  name: Optimizely Campaign REST Assets Schema API
  slug: open-optimizely-schema-api
- collection_type: open
  name: Optimizely Campaign REST Assets Segments API
  slug: open-optimizely-segments-api
- collection_type: open
  name: Optimizely Campaign REST Assets Sites API
  slug: open-optimizely-sites-api
- collection_type: open
  name: Optimizely Campaign REST Assets Smart Campaigns API
  slug: open-optimizely-smart-campaigns-api
- collection_type: open
  name: Optimizely Campaign REST Assets Tasks API
  slug: open-optimizely-tasks-api
- collection_type: open
  name: Optimizely Campaign REST Assets Transactional Mail API
  slug: open-optimizely-transactional-mail-api
- collection_type: open
  name: Optimizely Campaign REST Assets Unsubscribes API
  slug: open-optimizely-unsubscribes-api
- collection_type: open
  name: Optimizely Web Experimentation REST API
  slug: open-optimizely-web-experimentation
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/optimizely-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.developers.optimizely.com/.well-known/api-catalog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/optimizely-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/optimizely-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/optimizely-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/optimizely-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/optimizely-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/optimizely-cli.yml
- group: design
  title: ''
  type: Components
  url: components/optimizely-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/optimizely-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/optimizely-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/optimizely-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/optimizely-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/optimizely-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.optimizely.com/trust-center/compliance
- group: auth
  title: ''
  type: Security
  url: https://www.optimizely.com/trust-center/security
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/optimizely-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.optimizely.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/optimizely-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/optimizely-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/optimizely-feature-experimentation-asyncapi.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/optimizely-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/optimizely-plans-pricing.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/optimizely-experimentation-v2-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developers.optimizely.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developers.optimizely.com/web-experimentation/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developers.optimizely.com/feature-experimentation/docs/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.optimizely.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.optimizely.com/free-trial/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.optimizely.com/hc/en-us/
- group: operate
  title: ''
  type: Community
  url: https://world.optimizely.com/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/optimizely-vocabulary.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/optimizely/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/optimizely-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/optimizely-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/optimizely-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optimizely-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/optimizely-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/optimizely-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/optimizely
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/optimizely
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.developers.optimizely.com/
- group: company
  title: ''
  type: Website
  url: https://www.optimizely.com/
- group: company
  title: ''
  type: Blog
  url: https://www.optimizely.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.optimizely.com/
- group: start
  title: ''
  type: Login
  url: https://app.optimizely.com/signin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optimizely.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optimizely.com/legal/terms/
created: '2025-03-04'
description: Optimizely is a digital experience platform that provides A/B testing, feature flagging, content management, and commerce solutions for enterprises. Their developer platform offers a comprehensive suite of REST and GraphQL APIs spanning experimentation, content delivery, customer data, campaign management, and e-commerce capabilities.
features:
- 'Entry: ~$36K/year for basic Optimizely use'
- 'Mid: ~$63,700 per 10M impressions for Web Experimentation'
- 'Enterprise: $200K-$400K+/year for full DXP suite'
- 'Modular: pick CMS / Commerce / Experimentation independently'
- Web Experimentation (A/B + multivariate)
- Feature Experimentation (server-side flags)
- Personalization with audiences and Stats Engine
- Content Cloud (CMS)
- Commerce Cloud and Configured Commerce
- Optimizely AI Copilot
- REST API at api.optimizely.com
- Default 100 req/min/project
- OAuth 2.0 + Personal API tokens
- Webhooks for project events
- Datafile-based Feature Experimentation SDKs (10+)
- Stats Engine with Sequential Testing
finops:
- name: Optimizely Finops
  service_category: Digital Experience Platform
  slug: optimizely-finops
graphqls:
- description: Optimizely Graph is a unified content query and delivery service that provides access to content across Optimizely products through a single GraphQL API. It enables flexible data retrieval, high-perfo
  name: Optimizely GraphQL API
  slug: optimizely-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optimizely.png
json_schemas:
- name: Asset
  property_count: 6
  slug: optimizely-asset
- name: AssetInput
  property_count: 3
  slug: optimizely-assetinput
- name: Attribute
  property_count: 6
  slug: optimizely-attribute
- name: Audience
  property_count: 7
  slug: optimizely-audience
- name: AudienceInput
  property_count: 4
  slug: optimizely-audienceinput
- name: Campaign
  property_count: 8
  slug: optimizely-campaign
- name: CampaignInput
  property_count: 3
  slug: optimizely-campaigninput
- name: Catalog
  property_count: 6
  slug: optimizely-catalog
- name: CatalogEntry
  property_count: 8
  slug: optimizely-catalogentry
- name: CatalogEntryInput
  property_count: 5
  slug: optimizely-catalogentryinput
- name: CatalogInput
  property_count: 4
  slug: optimizely-cataloginput
- name: CatalogNode
  property_count: 8
  slug: optimizely-catalognode
- name: CatalogNodeInput
  property_count: 5
  slug: optimizely-catalognodeinput
- name: CmpCampaign
  property_count: 9
  slug: optimizely-cmpcampaign
- name: CmpContent
  property_count: 9
  slug: optimizely-cmpcontent
- name: ContentInput
  property_count: 7
  slug: optimizely-contentinput
- name: ContentItem
  property_count: 13
  slug: optimizely-contentitem
- name: ContentPatch
  property_count: 3
  slug: optimizely-contentpatch
- name: ContentType
  property_count: 5
  slug: optimizely-contenttype
- name: Optimizely Customer Profile
  property_count: 5
  slug: optimizely-customer-profile
- name: Customer
  property_count: 5
  slug: optimizely-customer
- name: Environment
  property_count: 8
  slug: optimizely-environment
- name: EnvironmentInput
  property_count: 3
  slug: optimizely-environmentinput
- name: Event
  property_count: 7
  slug: optimizely-event
- name: EventInput
  property_count: 4
  slug: optimizely-eventinput
- name: Optimizely Experiment
  property_count: 13
  slug: optimizely-experiment
- name: ExperimentInput
  property_count: 4
  slug: optimizely-experimentinput
- name: ExperimentResults
  property_count: 5
  slug: optimizely-experimentresults
- name: Extension
  property_count: 6
  slug: optimizely-extension
- name: Optimizely Feature Flag
  property_count: 9
  slug: optimizely-feature-flag
- name: Feature
  property_count: 6
  slug: optimizely-feature
- name: Flag
  property_count: 9
  slug: optimizely-flag
- name: FlagEnvironment
  property_count: 2
  slug: optimizely-flagenvironment
- name: FlagInput
  property_count: 5
  slug: optimizely-flaginput
- name: FlagVariation
  property_count: 3
  slug: optimizely-flagvariation
- name: FlagVariationInput
  property_count: 3
  slug: optimizely-flagvariationinput
- name: GraphQLRequest
  property_count: 3
  slug: optimizely-graphqlrequest
- name: GraphQLResponse
  property_count: 3
  slug: optimizely-graphqlresponse
- name: Label
  property_count: 3
  slug: optimizely-label
- name: MailingList
  property_count: 4
  slug: optimizely-mailinglist
- name: Metric
  property_count: 5
  slug: optimizely-metric
- name: NodeRelation
  property_count: 3
  slug: optimizely-noderelation
- name: NodeRelationInput
  property_count: 2
  slug: optimizely-noderelationinput
- name: ObjectInput
  property_count: 2
  slug: optimizely-objectinput
- name: OdpObject
  property_count: 5
  slug: optimizely-odpobject
- name: Order
  property_count: 9
  slug: optimizely-order
- name: Page
  property_count: 8
  slug: optimizely-page
- name: PageInput
  property_count: 5
  slug: optimizely-pageinput
- name: Pagination
  property_count: 3
  slug: optimizely-pagination
- name: Profile
  property_count: 11
  slug: optimizely-profile
- name: ProfileInput
  property_count: 2
  slug: optimizely-profileinput
- name: Project
  property_count: 8
  slug: optimizely-project
- name: ProjectInput
  property_count: 2
  slug: optimizely-projectinput
- name: Recipient
  property_count: 8
  slug: optimizely-recipient
- name: RecipientInput
  property_count: 4
  slug: optimizely-recipientinput
- name: Rule
  property_count: 6
  slug: optimizely-rule
- name: RuleInput
  property_count: 5
  slug: optimizely-ruleinput
- name: Ruleset
  property_count: 1
  slug: optimizely-ruleset
- name: RulesetInput
  property_count: 1
  slug: optimizely-rulesetinput
- name: SchemaField
  property_count: 4
  slug: optimizely-schemafield
- name: SchemaFieldInput
  property_count: 4
  slug: optimizely-schemafieldinput
- name: SchemaObject
  property_count: 4
  slug: optimizely-schemaobject
- name: SchemaObjectInput
  property_count: 2
  slug: optimizely-schemaobjectinput
- name: Segment
  property_count: 3
  slug: optimizely-segment
- name: Site
  property_count: 4
  slug: optimizely-site
- name: SmartCampaign
  property_count: 5
  slug: optimizely-smartcampaign
- name: Task
  property_count: 11
  slug: optimizely-task
- name: TaskInput
  property_count: 6
  slug: optimizely-taskinput
- name: TransactionalMailInput
  property_count: 3
  slug: optimizely-transactionalmailinput
- name: TransactionalMailResponse
  property_count: 2
  slug: optimizely-transactionalmailresponse
- name: Unsubscribe
  property_count: 3
  slug: optimizely-unsubscribe
- name: UnsubscribeInput
  property_count: 1
  slug: optimizely-unsubscribeinput
- name: Variable
  property_count: 3
  slug: optimizely-variable
- name: VariableInput
  property_count: 3
  slug: optimizely-variableinput
- name: Variation
  property_count: 4
  slug: optimizely-variation
- name: VariationInput
  property_count: 2
  slug: optimizely-variationinput
json_structures:
- name: Optimizely Structure
  property_count: 0
  slug: optimizely-structure
jsonld:
- class_count: 0
  name: Optimizely Context
  property_count: 12
  slug: optimizely-context
layout: provider
mcp_servers:
- description: ''
  name: optimizely-mcp.yml
  slug: optimizely-mcpyml
modified: '2026-08-13'
name: Optimizely
nav: Providers
network: true
overview: 'Optimizely publishes 49 APIs on the [APIs.io](https://apis.io/) network, including Experimentation REST API v2, Feature Experimentation Flags API v1, Flags Scheduling API, and 46 more. Tagged areas include A/B Testing, Content Management, Customer Data, E-Commerce, and Experimentation.


  The Optimizely catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Optimizely''s developer surface includes CLI, sandbox, changelog, documentation, API reference, getting-started guide, pricing, and 42 more developer resources.'
plans:
- name: Optimizely Plans Pricing
  plan_count: 3
  slug: optimizely-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 8
  name: Optimizely Rate Limits
  slug: optimizely-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Optimizely API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: optimizely-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Optimizely API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: optimizely-jsonschema-spectral-rules
scopes:
- name: Optimizely Scopes
  scope_count: 6
  slug: optimizely-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: exemplar
  composite: 75.4
  delta: -2.8
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 56.8
    contract_quality: 82.2
    developer_ergonomics: 76.2
    discoverability: 75.9
    governance: 56.8
    operational_transparency: 76.3
  previous_composite: 78.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optimizely/refs/heads/main/screenshots/optimizely-2026-08-07T190808.png
security:
- kind: authentication
  name: Optimizely Authentication
  slug: optimizely-authentication
  summary_line: oauth2/http/apiKey · 10 schemes
- kind: domain-security
  name: Optimizely Domain Security
  slug: optimizely-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Optimizely Vulnerability Disclosure
  slug: optimizely-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Optimizely Trust Center
  slug: optimizely-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA
slug: optimizely
tags:
- A/B Testing
- Content Management
- Customer Data
- E-Commerce
- Experimentation
- Feature Flags
- Marketing
website: https://www.optimizely.com/
---
