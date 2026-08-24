---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Salesforce Experience Cloud Agentic Access
  operation_count: 89
  slug: salesforce-experience-cloud-agentic-access
  summary_line: 89 operations · 28 acting
api_count: 37
apis:
- description: Deploy and retrieve Experience Cloud site configurations, navigation menus, and digital experience bundles. Enables programmatic management of ExperienceBundle and Network metadata types for CI/CD wor
  name: Metadata API (Experience Cloud)
  slug: metadata-api-experience-cloud
- description: Build and customize Lightning Web Runtime sites for Experience Cloud. Provides documentation for creating LWR-based digital experiences with custom components, page layouts, and theme configurations.
  name: LWR Sites API
  slug: lwr-sites-api
- description: Available actions for records and objects
  name: Salesforce Experience Cloud Actions API
  slug: salesforce-experience-cloud-actions-api
- description: Branding set management
  name: Salesforce Experience Cloud Branding Sets API
  slug: salesforce-experience-cloud-branding-sets-api
- description: CMS channel management
  name: Salesforce Experience Cloud Channels API
  slug: salesforce-experience-cloud-channels-api
- description: Content collection delivery operations
  name: Salesforce Experience Cloud Collections API
  slug: salesforce-experience-cloud-collections-api
- description: CMS content management operations
  name: Salesforce Experience Cloud Content API
  slug: salesforce-experience-cloud-content-api
- description: Content delivery operations for headless consumption
  name: Salesforce Experience Cloud Content Delivery API
  slug: salesforce-experience-cloud-content-delivery-api
- description: CMS content type operations
  name: Salesforce Experience Cloud Content Types API
  slug: salesforce-experience-cloud-content-types-api
- description: Managed content delivery channel operations
  name: Salesforce Experience Cloud Delivery Channels API
  slug: salesforce-experience-cloud-delivery-channels-api
- description: Object and field metadata
  name: Salesforce Experience Cloud Describe API
  slug: salesforce-experience-cloud-describe-api
- description: User favorites management
  name: Salesforce Experience Cloud Favorites API
  slug: salesforce-experience-cloud-favorites-api
- description: Feed and feed item operations
  name: Salesforce Experience Cloud Feeds API
  slug: salesforce-experience-cloud-feeds-api
- description: CMS folder management
  name: Salesforce Experience Cloud Folders API
  slug: salesforce-experience-cloud-folders-api
- description: GraphQL query and mutation operations
  name: Salesforce Experience Cloud GraphQL API
  slug: salesforce-experience-cloud-graphql-api
- description: Knowledge article operations within communities
  name: Salesforce Experience Cloud Knowledge API
  slug: salesforce-experience-cloud-knowledge-api
- description: Page layout metadata
  name: Salesforce Experience Cloud Layouts API
  slug: salesforce-experience-cloud-layouts-api
- description: API usage limits and quotas
  name: Salesforce Experience Cloud Limits API
  slug: salesforce-experience-cloud-limits-api
- description: List view data and metadata
  name: Salesforce Experience Cloud List Views API
  slug: salesforce-experience-cloud-list-views-api
- description: Managed content retrieval and search
  name: Salesforce Experience Cloud Managed Content API
  slug: salesforce-experience-cloud-managed-content-api
- description: CMS media file operations
  name: Salesforce Experience Cloud Media API
  slug: salesforce-experience-cloud-media-api
- description: Media content delivery operations
  name: Salesforce Experience Cloud Media Delivery API
  slug: salesforce-experience-cloud-media-delivery-api
- description: Community member operations
  name: Salesforce Experience Cloud Members API
  slug: salesforce-experience-cloud-members-api
- description: Content moderation operations
  name: Salesforce Experience Cloud Moderation API
  slug: salesforce-experience-cloud-moderation-api
- description: Site navigation menu operations
  name: Salesforce Experience Cloud Navigation API
  slug: salesforce-experience-cloud-navigation-api
- description: Object metadata for UI rendering
  name: Salesforce Experience Cloud Object Info API
  slug: salesforce-experience-cloud-object-info-api
- description: Site publishing operations
  name: Salesforce Experience Cloud Publish API
  slug: salesforce-experience-cloud-publish-api
- description: SOQL query execution
  name: Salesforce Experience Cloud Query API
  slug: salesforce-experience-cloud-query-api
- description: Record data and UI operations
  name: Salesforce Experience Cloud Records API
  slug: salesforce-experience-cloud-records-api
- description: Available REST resources
  name: Salesforce Experience Cloud Resources API
  slug: salesforce-experience-cloud-resources-api
- description: SOSL search execution
  name: Salesforce Experience Cloud Search API
  slug: salesforce-experience-cloud-search-api
- description: Experience Cloud site management operations
  name: Salesforce Experience Cloud Sites API
  slug: salesforce-experience-cloud-sites-api
- description: Salesforce object operations
  name: Salesforce Experience Cloud sObjects API
  slug: salesforce-experience-cloud-sobjects-api
- description: Site template management
  name: Salesforce Experience Cloud Templates API
  slug: salesforce-experience-cloud-templates-api
- description: Site theme and branding operations
  name: Salesforce Experience Cloud Themes API
  slug: salesforce-experience-cloud-themes-api
- description: Topic management and assignments
  name: Salesforce Experience Cloud Topics API
  slug: salesforce-experience-cloud-topics-api
- description: API version discovery
  name: Salesforce Experience Cloud Versions API
  slug: salesforce-experience-cloud-versions-api
arazzos:
- description: Create an Account, add a Contact under it, then open a Case for that Contact.
  name: Salesforce Experience Cloud Account Contact Case Onboarding
  slug: salesforce-experience-cloud-account-contact-case-onboarding-workflow
- description: Read a site branding set, then update its name, description, and properties.
  name: Salesforce Experience Cloud Branding Set Revision
  slug: salesforce-experience-cloud-branding-set-revise-workflow
- description: Find an open Case by number with SOQL, escalate it, and reload it.
  name: Salesforce Experience Cloud Case Escalation
  slug: salesforce-experience-cloud-case-escalation-workflow
- description: Create a CMS content item, read it back, then publish it to channels.
  name: Salesforce Experience Cloud CMS Content Publish
  slug: salesforce-experience-cloud-cms-content-publish-workflow
- description: Update an existing CMS content item, then republish it to channels.
  name: Salesforce Experience Cloud CMS Content Revise and Republish
  slug: salesforce-experience-cloud-cms-content-revise-republish-workflow
- description: Create a Contact, then open a support Case linked to that Contact.
  name: Salesforce Experience Cloud Contact and Case Intake
  slug: salesforce-experience-cloud-contact-case-intake-workflow
- description: Add a favorite, list the user's favorites, then remove the favorite.
  name: Salesforce Experience Cloud Favorite Lifecycle
  slug: salesforce-experience-cloud-favorite-lifecycle-workflow
- description: Fetch a feed element, inspect its comments, then delete it if it exists.
  name: Salesforce Experience Cloud Feed Element Moderation Delete
  slug: salesforce-experience-cloud-feed-element-moderation-delete-workflow
- description: Post a feed element to a community, read it back, and comment on it.
  name: Salesforce Experience Cloud Feed Post and Comment
  slug: salesforce-experience-cloud-feed-post-comment-workflow
- description: Post a feed element to a community and like it on behalf of the user.
  name: Salesforce Experience Cloud Feed Post and Like
  slug: salesforce-experience-cloud-feed-post-like-workflow
- description: Resolve a record ID via a GraphQL query, then update it through the REST API.
  name: Salesforce Experience Cloud GraphQL Query and REST Update
  slug: salesforce-experience-cloud-graphql-query-rest-update-workflow
- description: Resolve a delivery channel, query its published content, then fetch one item.
  name: Salesforce Experience Cloud Headless Content Delivery
  slug: salesforce-experience-cloud-headless-content-delivery-workflow
- description: Identify the current community user, search members, and read a member's reputation.
  name: Salesforce Experience Cloud Member Reputation Lookup
  slug: salesforce-experience-cloud-member-reputation-lookup-workflow
- description: Read object metadata, find its list views, and load the first list view's data.
  name: Salesforce Experience Cloud Object List View Exploration
  slug: salesforce-experience-cloud-object-listview-explore-workflow
- description: Create an Experience Cloud site, read it back, then publish it.
  name: Salesforce Experience Cloud Site Provision and Publish
  slug: salesforce-experience-cloud-site-provision-publish-workflow
- description: List a site's themes, activate one, then publish the site to apply it.
  name: Salesforce Experience Cloud Site Theme Activate and Publish
  slug: salesforce-experience-cloud-site-theme-activate-publish-workflow
- description: Update an Experience Cloud site's settings, then publish the changes.
  name: Salesforce Experience Cloud Site Update and Publish
  slug: salesforce-experience-cloud-site-update-publish-workflow
- description: Create an sObject record, read it back, then update it via the REST API.
  name: Salesforce Experience Cloud sObject Record Lifecycle
  slug: salesforce-experience-cloud-sobject-record-lifecycle-workflow
- description: Run a SOQL query to find a record, then update the first match.
  name: Salesforce Experience Cloud SOQL Query and Update
  slug: salesforce-experience-cloud-soql-query-update-workflow
- description: Search community topics by name and create one if it does not exist, else update it.
  name: Salesforce Experience Cloud Topic Upsert
  slug: salesforce-experience-cloud-topic-upsert-workflow
- description: Create, read, and update a record through the User Interface API.
  name: Salesforce Experience Cloud UI API Record Lifecycle
  slug: salesforce-experience-cloud-ui-record-lifecycle-workflow
artifact_total: 228
collections:
- collection_type: postman
  name: Salesforce Experience Cloud Salesforce CMS Connect API
  slug: postman-salesforce-experience-cloud-cms-connect
- collection_type: postman
  name: Salesforce Experience Cloud Salesforce CMS Delivery API
  slug: postman-salesforce-experience-cloud-cms-delivery
- collection_type: postman
  name: Salesforce Experience Cloud Salesforce CMS Managed Content API
  slug: postman-salesforce-experience-cloud-cms-managed-content
- collection_type: postman
  name: Salesforce Experience Cloud Salesforce Connect REST API (Communities)
  slug: postman-salesforce-experience-cloud-connect-communities
- collection_type: postman
  name: Salesforce Experience Cloud Salesforce GraphQL API
  slug: postman-salesforce-experience-cloud-graphql
- collection_type: postman
  name: Salesforce Experience Cloud Salesforce REST API
  slug: postman-salesforce-experience-cloud-rest-api
- collection_type: postman
  name: Salesforce Experience Cloud Sites API
  slug: postman-salesforce-experience-cloud-sites
- collection_type: postman
  name: Salesforce Experience Cloud Templates API
  slug: postman-salesforce-experience-cloud-templates
- collection_type: postman
  name: Salesforce Experience Cloud Salesforce User Interface API
  slug: postman-salesforce-experience-cloud-user-interface
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions API
  slug: open-salesforce-experience-cloud-actions-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Branding Sets API
  slug: open-salesforce-experience-cloud-branding-sets-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Channels API
  slug: open-salesforce-experience-cloud-channels-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect API
  slug: open-salesforce-experience-cloud-cms-connect
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Delivery API
  slug: open-salesforce-experience-cloud-cms-delivery
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Managed Content API
  slug: open-salesforce-experience-cloud-cms-managed-content
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Collections API
  slug: open-salesforce-experience-cloud-collections-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce Connect REST API (Communities)
  slug: open-salesforce-experience-cloud-connect-communities
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Content API
  slug: open-salesforce-experience-cloud-content-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Content Delivery API
  slug: open-salesforce-experience-cloud-content-delivery-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Content Types API
  slug: open-salesforce-experience-cloud-content-types-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Delivery Channels API
  slug: open-salesforce-experience-cloud-delivery-channels-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Describe API
  slug: open-salesforce-experience-cloud-describe-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Favorites API
  slug: open-salesforce-experience-cloud-favorites-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Feeds API
  slug: open-salesforce-experience-cloud-feeds-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Folders API
  slug: open-salesforce-experience-cloud-folders-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions GraphQL API
  slug: open-salesforce-experience-cloud-graphql-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce GraphQL API
  slug: open-salesforce-experience-cloud-graphql
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Knowledge API
  slug: open-salesforce-experience-cloud-knowledge-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Layouts API
  slug: open-salesforce-experience-cloud-layouts-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Limits API
  slug: open-salesforce-experience-cloud-limits-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions List Views API
  slug: open-salesforce-experience-cloud-list-views-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Managed Content API
  slug: open-salesforce-experience-cloud-managed-content-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Media API
  slug: open-salesforce-experience-cloud-media-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Media Delivery API
  slug: open-salesforce-experience-cloud-media-delivery-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Members API
  slug: open-salesforce-experience-cloud-members-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Moderation API
  slug: open-salesforce-experience-cloud-moderation-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Navigation API
  slug: open-salesforce-experience-cloud-navigation-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Object Info API
  slug: open-salesforce-experience-cloud-object-info-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Publish API
  slug: open-salesforce-experience-cloud-publish-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Query API
  slug: open-salesforce-experience-cloud-query-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Records API
  slug: open-salesforce-experience-cloud-records-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Resources API
  slug: open-salesforce-experience-cloud-resources-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce REST API
  slug: open-salesforce-experience-cloud-rest-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Search API
  slug: open-salesforce-experience-cloud-search-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Sites API
  slug: open-salesforce-experience-cloud-sites-api
- collection_type: open
  name: Salesforce Experience Cloud Sites API
  slug: open-salesforce-experience-cloud-sites
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions sObjects API
  slug: open-salesforce-experience-cloud-sobjects-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Templates API
  slug: open-salesforce-experience-cloud-templates-api
- collection_type: open
  name: Salesforce Experience Cloud Templates API
  slug: open-salesforce-experience-cloud-templates
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Themes API
  slug: open-salesforce-experience-cloud-themes-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Topics API
  slug: open-salesforce-experience-cloud-topics-api
- collection_type: open
  name: Salesforce Experience Cloud Salesforce User Interface API
  slug: open-salesforce-experience-cloud-user-interface
- collection_type: open
  name: Salesforce Experience Cloud Salesforce CMS Connect Actions Versions API
  slug: open-salesforce-experience-cloud-versions-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforce-experience-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesforce-experience-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salesforce-experience-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salesforce-experience-cloud-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/salesforce-experience-cloud/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-account-contact-case-onboarding-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-branding-set-revise-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-case-escalation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-cms-content-publish-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-cms-content-revise-republish-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-contact-case-intake-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-favorite-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-feed-element-moderation-delete-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-feed-post-comment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-feed-post-like-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-graphql-query-rest-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-headless-content-delivery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-member-reputation-lookup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-object-listview-explore-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-site-provision-publish-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-site-theme-activate-publish-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-site-update-publish-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-sobject-record-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-soql-query-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-topic-upsert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-experience-cloud-ui-record-lifecycle-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/salesforce-experience-cloud
- group: start
  title: ''
  type: Portal
  url: https://developer.salesforce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.salesforce.com/docs/atlas.en-us.communities_dev.meta/communities_dev/communities_dev_intro_before.htm
- group: auth
  title: ''
  type: Authentication
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.salesforce.com/blogs/2026/01/developers-guide-to-the-spring-26-release
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/sfdc-website-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/full_privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salesforce
- group: operate
  title: ''
  type: Community
  url: https://trailhead.salesforce.com/trailblazer-community/topics/salesforcedeveloper
- group: company
  title: ''
  type: Website
  url: https://www.salesforce.com/products/experience-cloud/overview/
- group: start
  title: ''
  type: Login
  url: https://login.salesforce.com/
- group: start
  title: ''
  type: Signup
  url: https://developer.salesforce.com/signup
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/
- group: build
  title: ''
  type: SDKs
  url: https://developer.salesforce.com/developer-centers/lightning-web-components
- group: learn
  title: ''
  type: Trailhead Learning
  url: https://trailhead.salesforce.com/
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/salesforce-developers/workspace/salesforce-developers
- group: build
  title: ''
  type: API Library
  url: https://developer.salesforce.com/docs/apis
- group: other
  title: ''
  type: Developer Center
  url: https://developer.salesforce.com/developer-centers/experience-cloud
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/salesforce-experience-cloud-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/salesforce-experience-cloud-site-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/salesforce-experience-cloud-managed-content-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/salesforce-experience-cloud-feed-element-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/salesforce-experience-cloud-community-user-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/salesforce-experience-cloud-cms-channel-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/salesforce-experience-cloud-sobject-record-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/salesforce-experience-cloud-rules.yml
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/salesforce-experience-cloud-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/salesforce-experience-cloud-vocabulary.yml
created: '2024'
description: APIs for building and managing Salesforce Experience Cloud sites, communities, and digital experiences including content management, theming, navigation, and Lightning Web Runtime powered portals.
examples:
- key_count: 6
  name: Salesforce Experience Cloud Cms Content Example
  slug: salesforce-experience-cloud-cms-content-example
- key_count: 6
  name: Salesforce Experience Cloud Create Site Example
  slug: salesforce-experience-cloud-create-site-example
- key_count: 6
  name: Salesforce Experience Cloud Executegraphqlquery Example
  slug: salesforce-experience-cloud-executegraphqlquery-example
finops:
- name: Salesforce Experience Cloud Finops
  service_category: CRM / Digital Experience Platform
  slug: salesforce-experience-cloud-finops
graphqls:
- description: Query Salesforce data using GraphQL for Experience Cloud. Offers a flexible query language for retrieving exactly the data needed, reducing over-fetching and improving performance for digital experien
  name: Salesforce Experience Cloud GraphQL API
  slug: salesforce-experience-cloud-graphql
image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/salesforce-logo.svg
json_schemas:
- name: ActorReference
  property_count: 4
  slug: salesforce-experience-cloud-actorreference
- name: ApiVersion
  property_count: 3
  slug: salesforce-experience-cloud-apiversion
- name: BrandingProperty
  property_count: 3
  slug: salesforce-experience-cloud-brandingproperty
- name: BrandingSet
  property_count: 4
  slug: salesforce-experience-cloud-brandingset
- name: BrandingSetCollection
  property_count: 2
  slug: salesforce-experience-cloud-brandingsetcollection
- name: BrandingSetInput
  property_count: 3
  slug: salesforce-experience-cloud-brandingsetinput
- name: Channel
  property_count: 7
  slug: salesforce-experience-cloud-channel
- name: ChannelCollection
  property_count: 4
  slug: salesforce-experience-cloud-channelcollection
- name: ChildRelationship
  property_count: 8
  slug: salesforce-experience-cloud-childrelationship
- name: CMS Channel
  property_count: 7
  slug: salesforce-experience-cloud-cms-channel
- name: CollectionList
  property_count: 4
  slug: salesforce-experience-cloud-collectionlist
- name: CollectionSummary
  property_count: 4
  slug: salesforce-experience-cloud-collectionsummary
- name: Comment
  property_count: 7
  slug: salesforce-experience-cloud-comment
- name: CommentInput
  property_count: 1
  slug: salesforce-experience-cloud-commentinput
- name: CommentPage
  property_count: 6
  slug: salesforce-experience-cloud-commentpage
- name: Community
  property_count: 19
  slug: salesforce-experience-cloud-community
- name: Community User
  property_count: 14
  slug: salesforce-experience-cloud-community-user
- name: CommunityListResponse
  property_count: 2
  slug: salesforce-experience-cloud-communitylistresponse
- name: CommunityUser
  property_count: 14
  slug: salesforce-experience-cloud-communityuser
- name: Content
  property_count: 11
  slug: salesforce-experience-cloud-content
- name: ContentCollection
  property_count: 4
  slug: salesforce-experience-cloud-contentcollection
- name: ContentInput
  property_count: 5
  slug: salesforce-experience-cloud-contentinput
- name: ContentNode
  property_count: 5
  slug: salesforce-experience-cloud-contentnode
- name: ContentType
  property_count: 3
  slug: salesforce-experience-cloud-contenttype
- name: ContentTypeCollection
  property_count: 2
  slug: salesforce-experience-cloud-contenttypecollection
- name: CreateCommunityInput
  property_count: 4
  slug: salesforce-experience-cloud-createcommunityinput
- name: CreateResult
  property_count: 3
  slug: salesforce-experience-cloud-createresult
- name: DeliveryChannel
  property_count: 6
  slug: salesforce-experience-cloud-deliverychannel
- name: DeliveryChannelCollection
  property_count: 4
  slug: salesforce-experience-cloud-deliverychannelcollection
- name: DeliveryCollection
  property_count: 6
  slug: salesforce-experience-cloud-deliverycollection
- name: DeliveryContentCollection
  property_count: 6
  slug: salesforce-experience-cloud-deliverycontentcollection
- name: DeliveryContentItem
  property_count: 10
  slug: salesforce-experience-cloud-deliverycontentitem
- name: DescribeGlobalResult
  property_count: 3
  slug: salesforce-experience-cloud-describeglobalresult
- name: DescribeSObjectResult
  property_count: 35
  slug: salesforce-experience-cloud-describesobjectresult
- name: ErrorResponse
  property_count: 2
  slug: salesforce-experience-cloud-errorresponse
- name: Favorite
  property_count: 7
  slug: salesforce-experience-cloud-favorite
- name: FavoriteInput
  property_count: 4
  slug: salesforce-experience-cloud-favoriteinput
- name: FavoritesRepresentation
  property_count: 1
  slug: salesforce-experience-cloud-favoritesrepresentation
- name: Feed Element
  property_count: 10
  slug: salesforce-experience-cloud-feed-element
- name: FeedElement
  property_count: 10
  slug: salesforce-experience-cloud-feedelement
- name: FeedElementCapabilities
  property_count: 2
  slug: salesforce-experience-cloud-feedelementcapabilities
- name: FeedElementInput
  property_count: 3
  slug: salesforce-experience-cloud-feedelementinput
- name: FeedElementPage
  property_count: 9
  slug: salesforce-experience-cloud-feedelementpage
- name: FieldDescribe
  property_count: 57
  slug: salesforce-experience-cloud-fielddescribe
- name: FieldValueRepresentation
  property_count: 2
  slug: salesforce-experience-cloud-fieldvaluerepresentation
- name: Folder
  property_count: 3
  slug: salesforce-experience-cloud-folder
- name: FolderCollection
  property_count: 2
  slug: salesforce-experience-cloud-foldercollection
- name: GraphQLConnection
  property_count: 3
  slug: salesforce-experience-cloud-graphqlconnection
- name: GraphQLEdge
  property_count: 2
  slug: salesforce-experience-cloud-graphqledge
- name: GraphQLError
  property_count: 4
  slug: salesforce-experience-cloud-graphqlerror
- name: GraphQLFieldValue
  property_count: 2
  slug: salesforce-experience-cloud-graphqlfieldvalue
- name: GraphQLRequest
  property_count: 3
  slug: salesforce-experience-cloud-graphqlrequest
- name: GraphQLResponse
  property_count: 3
  slug: salesforce-experience-cloud-graphqlresponse
- name: LayoutItem
  property_count: 7
  slug: salesforce-experience-cloud-layoutitem
- name: LayoutSection
  property_count: 7
  slug: salesforce-experience-cloud-layoutsection
- name: Like
  property_count: 4
  slug: salesforce-experience-cloud-like
- name: LikePage
  property_count: 6
  slug: salesforce-experience-cloud-likepage
- name: ListViewInfo
  property_count: 13
  slug: salesforce-experience-cloud-listviewinfo
- name: ListViewRepresentation
  property_count: 9
  slug: salesforce-experience-cloud-listviewrepresentation
- name: ListViewSummaryCollection
  property_count: 7
  slug: salesforce-experience-cloud-listviewsummarycollection
- name: Managed Content Version
  property_count: 11
  slug: salesforce-experience-cloud-managed-content
- name: ManagedContentDeliveryPage
  property_count: 4
  slug: salesforce-experience-cloud-managedcontentdeliverypage
- name: ManagedContentVersion
  property_count: 10
  slug: salesforce-experience-cloud-managedcontentversion
- name: ManagedContentVersionCollection
  property_count: 6
  slug: salesforce-experience-cloud-managedcontentversioncollection
- name: MediaCollection
  property_count: 4
  slug: salesforce-experience-cloud-mediacollection
- name: MediaFile
  property_count: 8
  slug: salesforce-experience-cloud-mediafile
- name: MessageBody
  property_count: 3
  slug: salesforce-experience-cloud-messagebody
- name: MessageBodyInput
  property_count: 1
  slug: salesforce-experience-cloud-messagebodyinput
- name: MessageSegment
  property_count: 2
  slug: salesforce-experience-cloud-messagesegment
- name: MessageSegmentInput
  property_count: 2
  slug: salesforce-experience-cloud-messagesegmentinput
- name: ModerationFlagCollection
  property_count: 5
  slug: salesforce-experience-cloud-moderationflagcollection
- name: NavigationMenuItem
  property_count: 7
  slug: salesforce-experience-cloud-navigationmenuitem
- name: NavigationMenuItemCollection
  property_count: 2
  slug: salesforce-experience-cloud-navigationmenuitemcollection
- name: ObjectInfoRepresentation
  property_count: 21
  slug: salesforce-experience-cloud-objectinforepresentation
- name: OrgLimits
  property_count: 0
  slug: salesforce-experience-cloud-orglimits
- name: PublishResult
  property_count: 2
  slug: salesforce-experience-cloud-publishresult
- name: PublishStatus
  property_count: 2
  slug: salesforce-experience-cloud-publishstatus
- name: QueryResult
  property_count: 4
  slug: salesforce-experience-cloud-queryresult
- name: RecordActionsRepresentation
  property_count: 1
  slug: salesforce-experience-cloud-recordactionsrepresentation
- name: RecordInput
  property_count: 2
  slug: salesforce-experience-cloud-recordinput
- name: RecordLayoutRepresentation
  property_count: 4
  slug: salesforce-experience-cloud-recordlayoutrepresentation
- name: RecordRepresentation
  property_count: 11
  slug: salesforce-experience-cloud-recordrepresentation
- name: RecordTypeInfo
  property_count: 8
  slug: salesforce-experience-cloud-recordtypeinfo
- name: RecordUiRepresentation
  property_count: 4
  slug: salesforce-experience-cloud-recorduirepresentation
- name: Reputation
  property_count: 2
  slug: salesforce-experience-cloud-reputation
- name: SearchResult
  property_count: 1
  slug: salesforce-experience-cloud-searchresult
- name: Experience Cloud Site
  property_count: 19
  slug: salesforce-experience-cloud-site
- name: sObject Record
  property_count: 11
  slug: salesforce-experience-cloud-sobject-record
- name: SObjectBasicInfo
  property_count: 2
  slug: salesforce-experience-cloud-sobjectbasicinfo
- name: SObjectDescribeBrief
  property_count: 26
  slug: salesforce-experience-cloud-sobjectdescribebrief
- name: SObjectRecord
  property_count: 2
  slug: salesforce-experience-cloud-sobjectrecord
- name: Template
  property_count: 9
  slug: salesforce-experience-cloud-template
- name: TemplateCollection
  property_count: 2
  slug: salesforce-experience-cloud-templatecollection
- name: Theme
  property_count: 4
  slug: salesforce-experience-cloud-theme
- name: ThemeCollection
  property_count: 1
  slug: salesforce-experience-cloud-themecollection
- name: ThemeProperty
  property_count: 4
  slug: salesforce-experience-cloud-themeproperty
- name: Topic
  property_count: 7
  slug: salesforce-experience-cloud-topic
- name: TopicCollection
  property_count: 3
  slug: salesforce-experience-cloud-topiccollection
- name: TopicInput
  property_count: 2
  slug: salesforce-experience-cloud-topicinput
- name: UpdateCommunityInput
  property_count: 3
  slug: salesforce-experience-cloud-updatecommunityinput
- name: UserPage
  property_count: 5
  slug: salesforce-experience-cloud-userpage
json_structures:
- name: Salesforce Experience Cloud Structure
  property_count: 0
  slug: salesforce-experience-cloud-structure
jsonld:
- class_count: 0
  name: Salesforce Experience Cloud Context
  property_count: 14
  slug: salesforce-experience-cloud-context
layout: provider
modified: '2026-08-21'
name: Salesforce Experience Cloud
nav: Providers
network: true
overview: 'Salesforce Experience Cloud publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Branding Sets API, Channels API, and 32 more. Tagged areas include CMS, Communities, CRM, Customer Portal, and Digital Experience.


  The Salesforce Experience Cloud catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Salesforce Experience Cloud''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, support, and 52 more developer resources.'
plans:
- name: Salesforce Experience Cloud Plans Pricing
  plan_count: 1
  slug: salesforce-experience-cloud-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Salesforce Experience Cloud Rate Limits
  slug: salesforce-experience-cloud-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Salesforce Experience Cloud API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: salesforce-experience-cloud-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Salesforce Experience Cloud API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 2
    info: 0
    warn: 3
  slug: salesforce-experience-cloud-rules
scopes:
- name: Salesforce Experience Cloud Scopes
  scope_count: 5
  slug: salesforce-experience-cloud-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 28.8
    contract_quality: 68.7
    developer_ergonomics: 61.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 23.7
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesforce-experience-cloud/refs/heads/main/screenshots/salesforce-experience-cloud-2026-06-20T193345.png
security:
- kind: authentication
  name: Salesforce Experience Cloud Authentication
  slug: salesforce-experience-cloud-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Salesforce Experience Cloud Domain Security
  slug: salesforce-experience-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: salesforce-experience-cloud
tags:
- CMS
- Communities
- CRM
- Customer Portal
- Digital Experience
- Experience Cloud
- Partner Portal
website: https://www.salesforce.com/products/experience-cloud/overview/
---
