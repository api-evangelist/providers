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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 65
  human_in_the_loop: 1
  name: Optimizely Agentic Access
  operation_count: 135
  slug: optimizely-agentic-access
  summary_line: 135 operations · 65 acting · 1 human-in-the-loop
api_count: 34
apis:
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
artifact_total: 185
asyncapis:
- description: The Optimizely Content Marketing Platform (CMP) provides webhook notifications when content events occur, such as when assets are published, tasks are completed or modified, and content items are upda
  name: Optimizely CMP Webhooks
  slug: optimizely-cmp-asyncapi
- description: Optimizely Feature Experimentation provides webhook notifications when configuration changes occur, such as datafile updates. Webhooks notify external servers of changes, eliminating the need to const
  name: Optimizely Feature Experimentation Webhooks
  slug: optimizely-feature-experimentation-asyncapi
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
  name: Optimizely Campaign REST API
  slug: open-optimizely-campaign
- collection_type: open
  name: Optimizely CMP Open REST API
  slug: open-optimizely-cmp
- collection_type: open
  name: Optimizely Commerce Service API
  slug: open-optimizely-commerce-service
- collection_type: open
  name: Optimizely Content Delivery API
  slug: open-optimizely-content-delivery
- collection_type: open
  name: Optimizely Content Management API
  slug: open-optimizely-content-management
- collection_type: open
  name: Optimizely Data Platform REST API
  slug: open-optimizely-data-platform
- collection_type: open
  name: Optimizely Feature Experimentation REST API
  slug: open-optimizely-feature-experimentation
- collection_type: open
  name: Optimizely Graph API
  slug: open-optimizely-graph
- collection_type: open
  name: Optimizely Web Experimentation REST API
  slug: open-optimizely-web-experimentation
common:
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
  url: https://www.optimizely.com/legal/terms-of-service/
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
modified: '2026-05-19'
name: Optimizely
nav: Providers
network: true
overview: 'Optimizely publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Attributes API, Audiences API, and 31 more. Tagged areas include A/B Testing, Content Management, Customer Data, E-Commerce, and Experimentation.


  The Optimizely catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Optimizely''s developer surface includes authentication, engineering blog, support, and 13 more developer resources.'
plans:
- name: Optimizely Plans Pricing
  plan_count: 3
  slug: optimizely-plans-pricing
random_paper: 93
rate_limits:
- limit_count: 3
  name: Optimizely Rate Limits
  slug: optimizely-rate-limits
rules:
- name: Optimizely API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: optimizely-asyncapi-spectral-rules
- name: Optimizely API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: optimizely-jsonschema-spectral-rules
scopes:
- name: Optimizely Scopes
  scope_count: 4
  slug: optimizely-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: strong
  composite: 58.2
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 80.4
    developer_ergonomics: 30.4
    discoverability: 59.3
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 58.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Optimizely Authentication
  slug: optimizely-authentication
  summary_line: apiKey/http/oauth2 · 6 schemes
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
