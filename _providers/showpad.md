---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Access analytics and insights for coaching and training programs, including learning paths, skill assessments, roleplay AI analysis, and coach analytics data.
  name: Showpad Coach API
  slug: showpad-coach-api
- description: Create and manage webhook subscriptions and read their delivery logs. Notifications carry a CloudEvents-shaped envelope and are signed with HMAC-SHA256 over the raw body plus a timestamp, with a five-
  name: Showpad Webhooks API
  slug: showpad-webhooks-api
- description: Hosted remote Model Context Protocol server that lets AI assistants such as Claude and Cursor search Showpad assets, fetch their content, run ShowQL filters, ask questions with cited sources, and read
  name: Showpad MCP Server
  slug: showpad-mcp-server
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The assets API from Showpad — 16 operation(s) for assets.
  name: Showpad Assets API
  phrasing_intents:
  - id: get_assets
    intent: List assets (legacy endpoint)
    question: Can I still list assets with the older .json assets endpoint?
  - id: post_assets
    intent: Upload an asset (legacy endpoint)
    question: Is the old .json create-asset endpoint still usable for uploading a file?
  - id: get_assets_count
    intent: Count assets
    question: How many assets are in our library?
  - id: get_assets_description
    intent: Describe the asset data model
    question: What properties does the asset model have in the legacy API?
  - id: get_assets_id1_tags_id2
    intent: Link or unlink an asset and tag via GET
    question: Is there a GET-based override to tag or untag an asset for clients that can't send POST?
  - id: link_assets_id1_tags_id2_link
    intent: Tag an asset (from the asset side)
    question: How do I attach an existing tag to an asset using the asset's tag link endpoint?
  - id: unlink_assets_id1_tags_id2_unlink
    intent: Untag an asset (from the asset side)
    question: How do I remove a tag from an asset through the asset's unlink endpoint?
  - id: get_assets_id
    intent: Get an asset (legacy endpoint)
    question: Can I fetch one asset through the older .json endpoint?
  phrasing_ops: 26
  slug: showpad-assets-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The channels API from Showpad — 22 operation(s) for channels.
  name: Showpad Channels API
  phrasing_intents:
  - id: get_channels
    intent: List channels (experiences)
    question: Which channels exist in our Showpad content library?
  - id: post_channels
    intent: Create a channel
    question: How do I create a new channel for my sales team's content?
  - id: get_channels_count
    intent: Count channels
    question: How many channels do we have in total?
  - id: get_channels_description
    intent: Describe the channel data model
    question: What fields does a channel object have and which calls apply to it?
  - id: get_channels_experience-types
    intent: List installed experience types
    question: Which experience types are installed in our Showpad instance?
  - id: get_channels_experience-types_experiencetypeid_modules_modulename
    intent: Get an experience type module's info
    question: How do I look up the details of a specific module inside an experience type?
  - id: get_channels_overview
    intent: Get a channel overview for a division
    question: Can I get a summary of all experiences in one division?
  - id: get_channels_id1_usergroups_id2
    intent: Link or unlink a channel and group via GET
    question: Is there a GET-based way to link or unlink a channel and a user group for clients that can't send POST?
  phrasing_ops: 29
  slug: showpad-channels-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The comments API from Showpad — 4 operation(s) for comments.
  name: Showpad Comments API
  phrasing_intents:
  - id: get_comments
    intent: List comments
    question: Which comments have been left across our Showpad content?
  - id: post_comments
    intent: Create a comment
    question: How do I create a standalone comment?
  - id: get_comments_count
    intent: Count comments
    question: How many comments exist in total?
  - id: get_comments_description
    intent: Describe the comment data model
    question: What fields does a comment object have?
  - id: get_comments_id
    intent: Get a comment
    question: How do I fetch a single comment by ID?
  - id: put_comments_id
    intent: Edit a comment (PUT)
    question: How do I edit a comment's text with a PUT request?
  - id: post_comments_id
    intent: Edit a comment (POST)
    question: Can I update a comment with POST instead of PUT?
  - id: delete_comments_id
    intent: Delete a comment
    question: How do I delete a comment?
  phrasing_ops: 8
  slug: showpad-comments-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: These are endpoints for managing crm recommendation rules and fetching shares and shared spaces cmr records
  name: Showpad CRM API
  phrasing_intents:
  - id: recommendation-rules-list
    intent: List CRM recommendation rules
    question: Which content recommendation rules are set up for our CRM instance?
  - id: create-recommendation-rule
    intent: Create a CRM recommendation rule
    question: How do I recommend specific content when a CRM field has a certain value?
  - id: get-recommendation-rule
    intent: Get a CRM recommendation rule
    question: How do I inspect the conditions and tags of one recommendation rule?
  - id: recommendation-rules-delete
    intent: Delete a CRM recommendation rule
    question: How do I remove an outdated recommendation rule?
  - id: update-recommendation-rule
    intent: Update a CRM recommendation rule
    question: How do I change the conditions on an existing recommendation rule?
  - id: shared-space-records-list
    intent: Get CRM records for a Shared Space
    question: Which CRM records and activities are tied to a given Shared Space?
  - id: share-records-list
    intent: Get CRM records for a Share
    question: Which CRM records are associated with a Share I sent?
  phrasing_ops: 7
  slug: showpad-crm-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The divisionpermissions API from Showpad — 6 operation(s) for divisionpermissions.
  name: Showpad Divisionpermissions API
  phrasing_intents:
  - id: get_divisionpermissions
    intent: List division permissions
    question: Which division permissions exist across the account?
  - id: post_divisionpermissions
    intent: Create a division permission
    question: How do I grant someone administrative rights over a division?
  - id: get_divisionpermissions_count
    intent: Count division permissions
    question: How many division permissions grant asset management?
  - id: get_divisionpermissions_description
    intent: Describe the DivisionPermission model
    question: What flags does a DivisionPermission record have?
  - id: get_divisionpermissions_id
    intent: Retrieve a division permission
    question: How do I look up one division permission by its ID?
  - id: put_divisionpermissions_id
    intent: Update a division permission with PUT
    question: How do I change what a division permission allows using PUT?
  - id: post_divisionpermissions_id
    intent: Update a division permission with POST
    question: Is there a POST alternative for editing a division permission?
  - id: delete_divisionpermissions_id
    intent: Delete a division permission
    question: How do I revoke a division permission entirely?
  phrasing_ops: 10
  slug: showpad-divisionpermissions-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The divisions API from Showpad — 17 operation(s) for divisions.
  name: Showpad Divisions API
  phrasing_intents:
  - id: get_divisions
    intent: List divisions with filters (v3)
    question: Which divisions have asset sharing enabled, using the older v3 list?
  - id: post_divisions
    intent: Create a division
    question: How do I set up a new division for another business unit?
  - id: get_divisions_count
    intent: Count divisions
    question: How many divisions exist in our account?
  - id: get_divisions_description
    intent: Describe the Division model and its APIs
    question: What fields make up the Division model?
  - id: get_divisions_id1_usergroups_id2
    intent: Link or unlink a division and group via GET
    question: Is there a GET call that links or unlinks a division and a user group depending on a method value?
  - id: link_divisions_id1_usergroups_id2_link
    intent: Add a user group to a division
    question: How do I give an existing user group access to a division?
  - id: unlink_divisions_id1_usergroups_id2_unlink
    intent: Remove a user group from a division
    question: How do I take a user group out of a division?
  - id: get_divisions_id
    intent: Retrieve a division (v3)
    question: How do I fetch one division's record with the older v3 endpoint?
  phrasing_ops: 24
  slug: showpad-divisions-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The exports API from Showpad — 25 operation(s) for exports.
  name: Showpad Exports API
  phrasing_intents:
  - id: get_exports_asset-authors
    intent: Export asset authors
    question: Who authored each asset in our library, as a bulk export?
  - id: get_exports_asset-countries
    intent: Export asset country assignments
    question: Which countries is each piece of content assigned to?
  - id: get_exports_asset-languages
    intent: Export asset language assignments
    question: What language is each asset tagged with across the whole library?
  - id: get_exports_asset-tags
    intent: Export asset-to-tag links
    question: Which tags are applied to which assets, in one export?
  - id: get_exports_assets
    intent: Export all assets
    question: How do I bulk export our entire content library metadata?
  - id: get_exports_channel-usergroups
    intent: Export channel-to-user-group access
    question: Which user groups have access to which channels?
  - id: get_exports_channel-users
    intent: Export channel-to-user access
    question: Which individual users are assigned to each channel?
  - id: get_exports_channels
    intent: Export all channels
    question: How can I get a full extract of every channel we've built?
  phrasing_ops: 25
  slug: showpad-exports-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The generic API from Showpad — 1 operation(s) for generic.
  name: Showpad Generic API
  phrasing_intents:
  - id: get_id
    intent: Look up any resource by its ID
    question: I have a Showpad ID but don't know what kind of object it is — can I look it up?
  phrasing_ops: 1
  slug: showpad-generic-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: These are endpoints for fetching available Languages and Countries information.
  name: Showpad Locale API
  phrasing_intents:
  - id: getLanguages
    intent: List supported languages
    question: Which languages does Showpad support for content and user preferences?
  - id: getCountries
    intent: List supported countries
    question: What country codes are supported for geographic filtering?
  phrasing_ops: 2
  slug: showpad-locale-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: These are endpoints for managing Mutual Action Plans
  name: Showpad Mutual Action Plan API
  phrasing_intents:
  - id: postMap
    intent: Create a mutual action plan
    question: How do I start a mutual action plan for a deal's shared space?
  - id: gesMaps
    intent: List mutual action plans
    question: Which mutual action plans can I access for a shared space?
  - id: deleteMap
    intent: Delete a mutual action plan
    question: How do I permanently delete a mutual action plan?
  - id: getParticipants
    intent: List a plan's participants
    question: Who is collaborating on a given mutual action plan?
  - id: getParticipantSelf
    intent: Get my participant profile in a plan
    question: What is my own participant record inside a mutual action plan?
  - id: getParticipantSettings
    intent: Get my notification settings for a plan
    question: Am I being notified when actions are assigned to me in a MAP?
  - id: updateParticipantSettings
    intent: Change my notification settings for a plan
    question: How do I stop getting notified when actions are completed in a MAP?
  - id: postMilestone
    intent: Add a milestone to a plan
    question: How do I add a new phase or milestone to a mutual action plan?
  phrasing_ops: 15
  slug: showpad-mutual-action-plan-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The recommendations API from Showpad — 6 operation(s) for recommendations.
  name: Showpad Recommendations API
  phrasing_intents:
  - id: get_recommendations_assets_new
    intent: Recommend newly assigned assets
    question: Which assets were recently made available to me that I haven't opened yet?
  - id: get_recommendations_assets_popular
    intent: Recommend popular assets
    question: What content performs best over the long term on views or shares?
  - id: get_recommendations_assets_trending
    intent: Recommend trending assets
    question: Which assets are getting a spike in attention right now?
  - id: get_recommendations_assets_updated
    intent: Recommend recently updated assets
    question: Which assets have been updated lately that I haven't looked at?
  - id: get_recommendations_experiences_new
    intent: Recommend newly assigned experiences
    question: Which experiences were recently assigned to me?
  - id: get_recommendations_experiences_popular
    intent: Recommend popular experiences
    question: Which experiences get the most views or shares?
  phrasing_ops: 6
  slug: showpad-recommendations-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: These are endpoints for managing Shared Space Templates
  name: Showpad Shared Space Templates API
  phrasing_intents:
  - id: shared-space-templates-list
    intent: List shared space templates
    question: Which shared space templates can I start a new space from?
  - id: shared-space-templates-get
    intent: Get a shared space template
    question: How do I see what a specific shared space template contains?
  phrasing_ops: 2
  slug: showpad-shared-space-templates-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: These are endpoints for managing Shared Spaces
  name: Showpad Shared Spaces API
  phrasing_intents:
  - id: shared-spaces-list
    intent: List shared spaces
    question: Which shared spaces have I created or been invited to?
  - id: shared-space-create
    intent: Create a shared space
    question: How do I open a new shared space for a buyer?
  - id: shared-space-get
    intent: Get a shared space's details
    question: How do I view the settings and details of one shared space?
  - id: shared-space-update
    intent: Update a shared space's settings
    question: How do I rename a shared space or change its description?
  - id: shared-space-delete
    intent: Delete a shared space
    question: How do I permanently delete a shared space?
  - id: shared-space-transfer-ownership
    intent: Transfer ownership of a shared space
    question: How do I hand a shared space over to a colleague when a rep leaves?
  - id: shared-spaces-items-add
    intent: Add files and folders to a shared space
    question: How do I put files into a shared space?
  phrasing_ops: 7
  slug: showpad-shared-spaces-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: These are endpoints for managing Shared Spaces Quick Actions
  name: Showpad Shared Spaces Quick Actions API
  phrasing_intents:
  - id: shared-spaces-quick-actions-list
    intent: List a Shared Space's quick actions
    question: Which quick actions are set up in a Shared Space?
  - id: create-shared-space-quick-action
    intent: Add a quick action to a Shared Space
    question: How do I add an external link as a quick action in a Shared Space?
  - id: get-shared-spaces-quick-action
    intent: Get a Shared Space quick action
    question: How do I see the details of one quick action in a Shared Space?
  - id: update-shared-spaces-quick-action
    intent: Update a Shared Space quick action
    question: How do I change the link or title of an existing quick action?
  - id: delete-shared-spaces-quick-action
    intent: Remove a quick action from a Shared Space
    question: How do I remove a quick action from a Shared Space?
  phrasing_ops: 5
  slug: showpad-shared-spaces-quick-actions-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: These are endpoints for managing Shares
  name: Showpad Shares API
  phrasing_intents:
  - id: create-share
    intent: Share assets with external recipients
    question: How do I send a set of assets to a prospect as a view-only link?
  phrasing_ops: 1
  slug: showpad-shares-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: These are endpoints for managing Tag Categories.
  name: Showpad Tag Categories API
  phrasing_intents:
  - id: getTagCategories
    intent: List tag categories
    question: What tag categories are set up in our content library?
  - id: postTagCategories
    intent: Create a tag category
    question: How do I create a new tag category for organizing content?
  - id: getTagCategory
    intent: Retrieve a tag category
    question: How do I look up one tag category by its ID?
  - id: updateTagCategory
    intent: Update a tag category
    question: How do I rename or publish a tag category?
  - id: deleteTagCategory
    intent: Delete a tag category
    question: How do I remove a tag category we no longer use?
  - id: updateTagCategoryTags
    intent: Add or remove tags in a tag category
    question: How do I add tags to or remove tags from an existing category?
  phrasing_ops: 6
  slug: showpad-tag-categories-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The tags API from Showpad — 12 operation(s) for tags.
  name: Showpad Tags API
  phrasing_intents:
  - id: get_tags
    intent: List tags (legacy endpoint)
    question: Can I still list tags through the older tags.json endpoint?
  - id: post_tags
    intent: Create a tag (legacy endpoint)
    question: Is the old .json endpoint still usable for creating a tag?
  - id: get_tags_count
    intent: Count tags
    question: How many tags exist in our Showpad library?
  - id: get_tags_description
    intent: Describe the tag data model
    question: What fields does a tag object have in the legacy API?
  - id: get_tags_id1_assets_id2
    intent: Link or unlink a tag and asset via GET
    question: Is there a GET override for linking or unlinking from the tag's side?
  - id: link_tags_id1_assets_id2_link
    intent: Tag an asset (from the tag side)
    question: How do I attach an asset to a tag using the tag's asset link endpoint?
  - id: unlink_tags_id1_assets_id2_unlink
    intent: Untag an asset (from the tag side)
    question: How do I remove an asset from a tag through the tag's unlink endpoint?
  - id: get_tags_id
    intent: Get a tag (legacy endpoint)
    question: Can I fetch one tag through the older .json endpoint?
  phrasing_ops: 20
  slug: showpad-tags-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: These are endpoints for managing Themes
  name: Showpad Themes API
  phrasing_intents:
  - id: theme-list
    intent: List themes
    question: Which branding themes are available in our Showpad instance?
  - id: theme-get
    intent: Get a theme's full configuration
    question: What colors and visual assets does a particular theme use?
  phrasing_ops: 2
  slug: showpad-themes-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The tickets API from Showpad — 9 operation(s) for tickets.
  name: Showpad Tickets API
  phrasing_intents:
  - id: get_tickets
    intent: List tickets
    question: Which tickets are still unfinished in our Showpad account?
  - id: post_tickets_cancel
    intent: Cancel tickets (no ID in path)
    question: Is there a bulk-style endpoint to cancel tickets without putting an ID in the URL?
  - id: get_tickets_count
    intent: Count tickets
    question: How many tickets are currently open?
  - id: get_tickets_description
    intent: Describe the ticket data model
    question: What fields does a ticket object have?
  - id: post_tickets_force-use
    intent: Force-use failed tickets (no ID in path)
    question: Is there a collection-level call to force using the related element of failed tickets?
  - id: get_tickets_ids_processingtime
    intent: Get processing time for tickets
    question: How long did a set of tickets take to process?
  - id: get_tickets_id
    intent: Get a ticket
    question: How do I look up a single ticket's status?
  - id: delete_tickets_id
    intent: Delete a ticket
    question: How do I delete a ticket entirely?
  phrasing_ops: 10
  slug: showpad-tickets-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The users API from Showpad — 22 operation(s) for users.
  name: Showpad Users API
  phrasing_intents:
  - id: get_users
    intent: List users with filters (v3)
    question: Which users in our Showpad instance are still only invited and haven't activated yet?
  - id: post_users
    intent: Create a new user
    question: How do I add a new salesperson as a user in Showpad?
  - id: get_users_count
    intent: Count users
    question: How many users do we have in total?
  - id: get_users_description
    intent: Describe the User model and its APIs
    question: What fields does the User model have and which user APIs are available?
  - id: get_users_invite
    intent: Resend invites to all pending users
    question: How can I nudge everyone who still has a pending invitation?
  - id: get_users_me
    intent: Get the current API user
    question: Who am I authenticated as when calling the API?
  - id: get_users_me_recommendations
    intent: Get recommendations for the current user
    question: What content recommendations does Showpad have for me?
  - id: get_users_me_tickets
    intent: Get tickets for the current user
    question: Which tickets are assigned to me?
  phrasing_ops: 29
  slug: showpad-users-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The User Groups API from Showpad — 14 operation(s) for user groups.
  name: Showpad User Groups API
  phrasing_intents:
  - id: get_usergroups
    intent: List user groups
    question: Which user groups exist in our Showpad organization?
  - id: post_usergroups
    intent: Create a user group
    question: How do I create a new user group for a team?
  - id: get_usergroups_count
    intent: Count user groups
    question: How many user groups do we have?
  - id: get_usergroups_description
    intent: Describe the user group data model
    question: What fields does a user group object have?
  - id: get_usergroups_id1_divisions_id2
    intent: Link or unlink a group and division via GET
    question: Is there a GET override for adding or removing a user group's division access?
  - id: link_usergroups_id1_divisions_id2_link
    intent: Give a user group access to a division
    question: How do I give a user group access to a division?
  - id: unlink_usergroups_id1_divisions_id2_unlink
    intent: Remove a user group from a division
    question: How do I revoke a user group's access to a division?
  - id: get_usergroups_id1_users_id2
    intent: Link or unlink a group member via GET
    question: Is there a GET override for adding or removing a member of a user group?
  phrasing_ops: 20
  slug: showpad-user-groups-api
- baseURL: https://{subdomain}.showpad.biz/api/v3
  baseurl_source: declared
  description: The User Permissions API from Showpad — 6 operation(s) for user permissions.
  name: Showpad User Permissions API
  phrasing_intents:
  - id: get_userpermissions
    intent: List user permission profiles
    question: Which user permission profiles allow web access or kiosk mode?
  - id: post_userpermissions
    intent: Create a user permission profile
    question: How do I define a new set of user permissions for a role?
  - id: get_userpermissions_count
    intent: Count user permission profiles
    question: How many user permission profiles exist?
  - id: get_userpermissions_description
    intent: Describe the UserPermission model
    question: What feature switches make up the UserPermission model?
  - id: get_userpermissions_id
    intent: Retrieve a user permission profile
    question: How do I look up one user permission profile by its ID?
  - id: put_userpermissions_id
    intent: Update a user permission profile with PUT
    question: How do I turn off web access in a permission profile using PUT?
  - id: post_userpermissions_id
    intent: Update a user permission profile with POST
    question: Is there a POST alternative for editing a user permission profile?
  - id: delete_userpermissions_id
    intent: Delete a user permission profile
    question: How do I remove a user permission profile we no longer use?
  phrasing_ops: 10
  slug: showpad-user-permissions-api
artifact_total: 40
asyncapis:
- description: ''
  name: Showpad Webhooks
  slug: showpad-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.showpad.com/
- group: other
  href: https://artifacts.apis.io/showpad/capabilities/showpad-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/showpad-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/showpad/overlays/showpad-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/showpad-v3-overlay.yaml
- group: other
  href: https://artifacts.apis.io/showpad/overlays/showpad-v4-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/showpad-v4-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/showpad/scopes/showpad-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/showpad-scopes.yml
- group: auth
  href: https://artifacts.apis.io/showpad/authentication/showpad-authentication.yml
  title: ''
  type: Authentication
  url: authentication/showpad-authentication.yml
- group: auth
  href: https://artifacts.apis.io/showpad/security/showpad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/showpad-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/showpad/security/showpad-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/showpad-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.showpad.com/responsible-disclosure
- group: auth
  href: https://artifacts.apis.io/showpad/security/showpad-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/showpad-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.bigtincan.com/
- group: design
  href: https://artifacts.apis.io/showpad/conformance/showpad-conformance.yml
  title: ''
  type: Conformance
  url: conformance/showpad-conformance.yml
- group: agent
  href: https://artifacts.apis.io/showpad/well-known/showpad-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/showpad-well-known.yml
- group: agent
  href: https://artifacts.apis.io/showpad/mcp/showpad-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/showpad-mcp.yml
- group: build
  href: https://artifacts.apis.io/showpad/mcp/showpad-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/showpad-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/showpad/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/showpad/llms/showpad-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/showpad-llms.txt
- group: build
  href: https://artifacts.apis.io/showpad/packages/showpad-packages.yml
  title: ''
  type: Packages
  url: packages/showpad-packages.yml
- group: build
  href: https://artifacts.apis.io/showpad/packages/showpad-packages.yml
  title: ''
  type: SDKs
  url: packages/showpad-packages.yml
- group: build
  href: https://artifacts.apis.io/showpad/cli/showpad-cli.yml
  title: ''
  type: CLI
  url: cli/showpad-cli.yml
- group: design
  href: https://artifacts.apis.io/showpad/components/showpad-components.yml
  title: ''
  type: Components
  url: components/showpad-components.yml
- group: design
  href: https://artifacts.apis.io/showpad/conventions/showpad-conventions.yml
  title: ''
  type: Conventions
  url: conventions/showpad-conventions.yml
- group: design
  href: https://artifacts.apis.io/showpad/errors/showpad-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/showpad-problem-types.yml
- group: design
  href: https://artifacts.apis.io/showpad/data-model/showpad-data-model.yml
  title: ''
  type: DataModel
  url: data-model/showpad-data-model.yml
- group: design
  href: https://artifacts.apis.io/showpad/lifecycle/showpad-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/showpad-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.showpad.com
- group: start
  href: https://artifacts.apis.io/showpad/sandbox/showpad-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/showpad-sandbox.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.showpad.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.showpad.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.showpad.com/docs/apis/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.showpad.com/docs/apis/references
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.showpad.com/docs/apis/concepts/fundamentals
- group: other
  title: ''
  type: Fundamentals
  url: https://developer.showpad.com/docs/apis/concepts/fundamentals
- group: design
  title: ''
  type: Versioning
  url: https://developer.showpad.com/docs/apis/concepts/versions
- group: design
  href: https://artifacts.apis.io/showpad/asyncapi/showpad-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/showpad-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/showpad/changelog/showpad-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/showpad-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.showpad.com/news
- group: operate
  title: ''
  type: Status
  url: https://status.showpad.com
- group: company
  title: ''
  type: Blog
  url: https://www.showpad.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.showpad.com/hc/en-us/requests/new
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.showpad.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/showpad
- group: commercial
  title: ''
  type: Pricing
  url: https://www.showpad.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.showpad.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.showpad.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.showpad.com/privacy-policy
- group: commercial
  href: https://artifacts.apis.io/showpad/plans/showpad-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/showpad-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/showpad/rate-limits/showpad-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/showpad-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/showpad/finops/showpad-finops.yml
  title: ''
  type: FinOps
  url: finops/showpad-finops.yml
created: '2026-06-13'
description: Showpad is a sales enablement and coaching platform offering a REST API for managing sales content, training programs, meeting analytics, and buyer engagement. The API supports content management with ShowQL query language, buyer engagement through shares and digital sales rooms, seller effectiveness via CRM recommendation rules, user management with SCIM 2.0, and analytics covering content reporting and coaching insights across the sales cycle. Showpad publishes machine-readable OpenAPI 3.0.3 definitions for both API v3 (200 operations) and API v4 (65 operations), a signed webhook surface, and a hosted OAuth-protected MCP server for AI assistants.
finops:
- has_sources: true
  method: derived
  name: Showpad Finops
  primary_unit: ''
  service_category: ''
  slug: showpad-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/showpad.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.showpad.com over HTTP requiring OAuth; 9 tools listed.
  name: Showpad MCP Server
  slug: showpad-mcp-server
modified: '2026-08-14'
name: Showpad
nav: Providers
network: true
overview: 'Showpad publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assets API, Channels API, Comments API, and 22 more. Tagged areas include Sales Enablement, Sales Coaching, Content Management, Buyer Engagement, and Sales Analytics.


  The Showpad catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Showpad''s developer surface includes authentication, CLI, sandbox, developer portal, documentation, API reference, getting-started guide, and 42 more developer resources.'
plans:
- name: Showpad Plans Pricing
  plan_count: 3
  slug: showpad-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Showpad Rate Limits
  slug: showpad-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Showpad API Rules
  rule_count: 57
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 10
  slug: showpad-rules
scopes:
- name: Showpad Scopes
  scope_count: 8
  slug: showpad-scopes
  summary_line: 8 scopes · password/authorizationCode
score:
  band: exemplar
  composite: 68.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 31.8
    contract_quality: 56.6
    developer_ergonomics: 70.8
    discoverability: 75.0
    operational_transparency: 52.6
  previous_composite: 68.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/showpad/showpad-2026-06-20T193845.png
security:
- kind: authentication
  name: Showpad Authentication
  slug: showpad-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Showpad Domain Security
  slug: showpad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Showpad Vulnerability Disclosure
  slug: showpad-vulnerability-disclosure
  summary_line: Intigriti · contact published
- kind: trust-center
  name: Showpad Trust Center
  slug: showpad-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27701
skill_count: 4
skills:
- name: Create a Showpad Shared Space and add content
  slug: showpad-create-shared-space
- name: Provision Showpad users, groups and divisions
  slug: showpad-manage-users-and-groups
- name: Search and fetch Showpad sales content
  slug: showpad-search-and-fetch-content
- name: Subscribe to Showpad webhooks and verify signatures
  slug: showpad-subscribe-to-webhooks
slug: showpad
tags:
- Sales Enablement
- Sales Coaching
- Content Management
- Buyer Engagement
- Sales Analytics
- Training
- CRM Integration
- Digital Sales Rooms
- MCP
- SCIM
website: https://www.showpad.com/
---
