---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 62.3
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 1543
  human_in_the_loop: 25
  name: Adobe Suite Agentic Access
  operation_count: 2823
  slug: adobe-suite-agentic-access
  summary_line: 2823 operations · 1543 acting · 25 human-in-the-loop
api_count: 70
apis:
- description: Integrate e-signature workflows and document signing.
  name: Adobe Sign API
  slug: adobe-sign-api
- description: Content management and digital asset management APIs.
  name: Adobe Experience Manager API
  slug: adobe-experience-manager-api
- description: Search and license stock photos, videos, and assets.
  name: Adobe Stock API
  slug: adobe-stock-api
- description: Extend Premiere Pro with plugins, panels, and automation for video editing workflows including support for new file formats, effects, and transitions.
  name: Adobe Premiere Pro API
  slug: adobe-premiere-pro-api
- description: Create visual effects, manipulate project elements, and automate complex tasks in After Effects through plugins, scripts, and panels.
  name: Adobe After Effects API
  slug: adobe-after-effects-api
- description: Manage personalization activities, audiences, offers, and deliver experiences across web, mobile, and IoT channels.
  name: Adobe Target API
  slug: adobe-target-api
- description: Manage marketing campaigns, deliveries, workflows, subscriptions, and profiles through REST APIs for cross-channel campaign orchestration.
  name: Adobe Campaign API
  slug: adobe-campaign-api
- description: Programmatically manage users, groups, and product entitlements for Adobe enterprise organizations.
  name: Adobe User Management API
  slug: adobe-user-management-api
- description: Register event providers, define event metadata, subscribe webhook or journaling registrations, and ingest custom events across the Adobe estate. Adobe I/O Events is the event backbone behind Photosho
  name: Adobe I/O Events API
  slug: adobe-io-events-api
- description: 'Adobe ships Model Context Protocol servers on three surfaces: a remote Marketo Engage server exposing 100+ marketing operations, a remote Adobe Experience Manager as a Cloud Service server, and a loca'
  name: Adobe MCP Servers
  slug: adobe-mcp-servers
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Query the accelerated store in a stateless manner to quickly return results based on aggregated data.
  name: Adobe Suite Accelerated Queries API
  phrasing_intents:
  - id: runAcceleratedQuery
    intent: Query the accelerated store
    question: How do I run a fast query against accelerated store datasets?
  phrasing_ops: 1
  slug: adobe-suite-accelerated-queries-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Access control policies provide information about resources and permissions for the current user. More information about using this set of endpoints can be found in the [access control endpoint guide]
  name: Adobe Suite Access Control Policies API
  phrasing_intents:
  - id: listPolicyNames
    intent: List permission names and resource types
    question: What permission names and resource types can access control policies reference?
  - id: listEffectiveAclPolicies
    intent: Check a user's effective policies
    question: Which access policies actually apply to me on these resources?
  phrasing_ops: 2
  slug: adobe-suite-access-control-policies-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Accesslevel API from Adobe Suite — 6 operation(s) for accesslevel.
  name: Adobe Suite Accesslevel API
  phrasing_intents:
  - id: getAccessLevel
    intent: Get one access level
    question: How do I see the settings of a single Workfront access level?
  - id: editAccessLevel
    intent: Edit an access level
    question: How do I change the permissions in one access level?
  - id: deleteAccessLevel
    intent: Delete an access level
    question: How do I delete an access level we no longer use?
  - id: getAccessLevels
    intent: Get several access levels by ID
    question: Can I fetch multiple access levels at once by their IDs?
  - id: editAccessLevels
    intent: Edit many access levels at once
    question: Can I update several access levels in one request?
  - id: addAccessLevels
    intent: Create or copy an access level
    question: How do I create a new custom access level?
  - id: deleteAccessLevels
    intent: Delete several access levels
    question: Can I delete a batch of access levels in one call?
  - id: replaceAccessLevels
    intent: Replace access levels with another one
    question: How do I retire access levels and move their users to a replacement level?
  phrasing_ops: 11
  slug: adobe-suite-accesslevel-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Account information for the authenticated user.
  name: Adobe Suite Accounts API
  phrasing_intents:
  - id: getAccount
    intent: Get the Lightroom user's account details
    question: What subscription status does the signed-in Lightroom user have?
  phrasing_ops: 1
  slug: adobe-suite-accounts-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Acknowledgement API from Adobe Suite — 8 operation(s) for acknowledgement.
  name: Adobe Suite Acknowledgement API
  phrasing_intents:
  - id: getAcknowledgement
    intent: Look up one acknowledgement record
    question: How do I fetch a single acknowledgement record in Workfront by ID?
  - id: editAcknowledgement
    intent: Update one acknowledgement record
    question: Can I edit an existing acknowledgement record directly?
  - id: deleteAcknowledgement
    intent: Delete one acknowledgement record
    question: How do I delete a single acknowledgement record?
  - id: getAcknowledgements
    intent: Fetch several acknowledgements by ID
    question: Can I pull a batch of acknowledgement records if I have their IDs?
  - id: editAcknowledgements
    intent: Update many acknowledgement records at once
    question: Is there a bulk edit for acknowledgement records?
  - id: addAcknowledgements
    intent: Create an acknowledgement record
    question: How do I create a new acknowledgement record directly?
  - id: deleteAcknowledgements
    intent: Delete many acknowledgement records
    question: Can I bulk delete acknowledgement records by ID?
  - id: countAcknowledgements
    intent: Count acknowledgement records
    question: How many acknowledgement records match a filter?
  phrasing_ops: 13
  slug: adobe-suite-acknowledgement-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Ad API from Adobe Suite — 3 operation(s) for ad.
  name: Adobe Suite Ad API
  phrasing_intents:
  - id: adStart
    intent: Track the start of an ad
    question: How do I tell Media Analytics that an ad began playing?
  - id: adComplete
    intent: Track an ad finishing
    question: How do I signal that an ad played to the end?
  - id: adSkip
    intent: Track a skipped ad
    question: How do I report that a viewer skipped an ad?
  phrasing_ops: 3
  slug: adobe-suite-ad-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Ad Break API from Adobe Suite — 2 operation(s) for ad break.
  name: Adobe Suite Ad Break API
  phrasing_intents:
  - id: adBreakStart
    intent: Signal the start of an ad break
    question: How do I tell media tracking that an ad break has started?
  - id: adBreakComplete
    intent: Signal the end of an ad break
    question: How do I report that an ad break has finished?
  phrasing_ops: 2
  slug: adobe-suite-ad-break-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Adhocrun API from Adobe Suite — 1 operation(s) for adhocrun.
  name: Adobe Suite Adhocrun API
  phrasing_intents:
  - id: runAdhocActivation
    intent: Export audiences to batch destinations on demand
    question: Can I push audiences to a file-based destination right now instead of waiting for the next scheduled export?
  phrasing_ops: 1
  slug: adobe-suite-adhocrun-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Sandbox operations available only to admins. Sandbox admin privileges are managed through the [Adobe Admin Console](https://adminconsole.adobe.com).
  name: Adobe Suite Admin operations API
  phrasing_intents:
  - id: listSandboxTypes
    intent: List supported sandbox types
    question: What types of sandboxes can our organization create?
  - id: listSandboxes
    intent: List the organization's sandboxes
    question: How do I see every sandbox that belongs to our organization?
  - id: createSandbox
    intent: Create a sandbox
    question: How do I create a new development sandbox?
  - id: retrieveSandbox
    intent: Get a sandbox by name
    question: What state is a particular sandbox in right now?
  - id: resetSandbox
    intent: Reset a sandbox
    question: How do I reset a sandbox back to a clean state?
  - id: deleteSandbox
    intent: Delete a sandbox
    question: Is it possible to delete a sandbox we no longer need?
  - id: patchSandbox
    intent: Rename a sandbox's display title
    question: What's the way to change a sandbox's display title?
  phrasing_ops: 7
  slug: adobe-suite-admin-operations-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Agilework API from Adobe Suite — 6 operation(s) for agilework.
  name: Adobe Suite Agilework API
  phrasing_intents:
  - id: getAgileWork
    intent: Get one agile work item
    question: How do I look up a single agile work item in Workfront by its ID?
  - id: editAgileWork
    intent: Edit an agile work item
    question: Can I change the details of one existing agile work item?
  - id: deleteAgileWork
    intent: Delete an agile work item
    question: How do I remove one agile work item?
  - id: getAgileWorks
    intent: Get several agile work items by ID
    question: Can I fetch a batch of agile work items when I have their IDs?
  - id: editAgileWorks
    intent: Edit many agile work items at once
    question: Can I update a whole set of agile work items in one request?
  - id: deleteAgileWorks
    intent: Delete several agile work items
    question: Can I delete a batch of agile work items in one go?
  - id: countAgileWorks
    intent: Count agile work items
    question: How many agile work items are there?
  - id: searchAgileWorks
    intent: Search agile work items
    question: How can I find agile work items that meet certain conditions?
  phrasing_ops: 10
  slug: adobe-suite-agilework-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Information for albums, which contain references to zero or more assets.
  name: Adobe Suite Albums API
  phrasing_intents:
  - id: createAlbum
    intent: Create an album in a catalog
    question: How can I create a new album or project set in a Lightroom catalog?
  - id: readAlbum
    intent: Get a Lightroom album
    question: How do I read the details of one album in my Lightroom catalog?
  - id: updateAlbum
    intent: Update an existing album
    question: Can I rename or change an album my app created earlier?
  - id: deleteAlbum
    intent: Delete an album
    question: How do I delete an album from my catalog?
  - id: getAlbums
    intent: List albums in a catalog
    question: What albums exist in my Lightroom catalog?
  - id: addAssetsToAlbum
    intent: Add assets to an album
    question: How can I put a batch of photos into an album?
  - id: listAssetsOfAlbum
    intent: List the photos and videos in an album
    question: How do I get all the photos inside a specific album?
  phrasing_ops: 7
  slug: adobe-suite-albums-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Alert subscriptions allow you to receive notifications on the different statuses of both ad hoc and scheduled queries. Alerts can be received by email, within the Platform UI, or both.
  name: Adobe Suite Alert Subscriptions API
  phrasing_intents:
  - id: listAlertsPerImsOrgAndSandbox
    intent: List query alerts in a sandbox
    question: What query service alerts are set up in my sandbox?
  - id: createAndSubscribeToAnAlert
    intent: Create a query alert and subscribe users
    question: How do I get emailed when a scheduled query fails?
  - id: listSubscribersForAnAlertByAssetsId
    intent: List alert subscriptions for a query or schedule
    question: Who is subscribed to alerts on a particular query?
  - id: listSubscribersForAnAlertByAssetIdAndAlertType
    intent: List subscribers for one alert type on a query
    question: Who gets notified when this query fails, specifically?
  - id: deleteAlert
    intent: Delete a query alert
    question: How do I remove an alert from a query entirely?
  - id: patchAlert
    intent: Enable or disable a query alert
    question: Can I pause an alert temporarily without deleting it?
  - id: listAllAlertsSubscribedToByEmailId
    intent: List the alerts a user is subscribed to
    question: Which alerts is a particular colleague subscribed to?
  phrasing_ops: 7
  slug: adobe-suite-alert-subscriptions-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Annotations API from Adobe Suite — 2 operation(s) for annotations.
  name: Adobe Suite Annotations API
  phrasing_intents:
  - id: getAnnotations_1
    intent: List Analytics annotations
    question: How do I list all the annotations in my Adobe Analytics company?
  - id: createAnnotation_1
    intent: Create an Analytics annotation
    question: How do I add an annotation to mark an event on my reports?
  - id: getAnnotation_1
    intent: Get one Analytics annotation
    question: What are the details of a specific annotation?
  - id: updateAnnotation_1
    intent: Update an existing Analytics annotation
    question: How do I change the name or dates on an annotation I already made?
  - id: deleteAnnotation_1
    intent: Delete an Analytics annotation
    question: How do I delete an annotation that is no longer relevant?
  phrasing_ops: 5
  slug: adobe-suite-annotations-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Announcement API from Adobe Suite — 7 operation(s) for announcement.
  name: Adobe Suite Announcement API
  phrasing_intents:
  - id: getAnnouncement
    intent: Get an announcement by ID
    question: What does a particular Workfront announcement say and who was it sent to?
  - id: editAnnouncement
    intent: Update an announcement
    question: How do I fix a typo in an announcement I already wrote?
  - id: deleteAnnouncement
    intent: Delete an announcement
    question: How do I remove an announcement that shouldn't have gone out?
  - id: getAnnouncements
    intent: Get several announcements by their IDs
    question: Can I fetch a handful of announcements in one request?
  - id: editAnnouncements
    intent: Bulk-update several announcements
    question: Can I edit a number of announcements in one call?
  - id: addAnnouncements
    intent: Create an announcement
    question: How do I post a new system announcement to Workfront users?
  - id: deleteAnnouncements
    intent: Delete several announcements at once
    question: Can I clean up old announcements in bulk?
  - id: countAnnouncements
    intent: Count announcements
    question: How many announcements have been created so far?
  phrasing_ops: 12
  slug: adobe-suite-announcement-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Announcementattachment API from Adobe Suite — 5 operation(s) for announcementattachment.
  name: Adobe Suite Announcementattachment API
  phrasing_intents:
  - id: getAnnouncementAttachment
    intent: Look up one announcement attachment
    question: What details are available for a single Workfront announcement attachment?
  - id: getAnnouncementAttachments
    intent: Fetch several announcement attachments
    question: Can I pull multiple announcement attachments at once by ID?
  - id: countAnnouncementAttachments
    intent: Count announcement attachments
    question: How many files are attached to announcements?
  - id: searchAnnouncementAttachments
    intent: Search announcement attachments
    question: Which attachments belong to a particular announcement?
  - id: reportAnnouncementAttachments
    intent: Run a report on announcement attachments
    question: Can I get summary report data about announcement attachments?
  phrasing_ops: 5
  slug: adobe-suite-announcementattachment-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Apiversionmetadata API from Adobe Suite — 5 operation(s) for apiversionmetadata.
  name: Adobe Suite Apiversionmetadata API
  phrasing_intents:
  - id: getAPIVersionMetadata
    intent: Get one API version metadata record
    question: How do I read the metadata for a single API version?
  - id: getAPIVersionMetadatas
    intent: Fetch several API version metadata records
    question: Can I load metadata for multiple API versions in one request?
  - id: countAPIVersionMetadatas
    intent: Count API version metadata records
    question: How many API version metadata records exist?
  - id: searchAPIVersionMetadatas
    intent: Search API version metadata
    question: Which API versions are available, and how do I search their metadata?
  - id: reportAPIVersionMetadatas
    intent: Run an aggregated report on API version metadata
    question: Can I get grouped report data about API version metadata?
  phrasing_ops: 5
  slug: adobe-suite-apiversionmetadata-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: App configurations allow credentials to be stored and retrieved for later use.
  name: Adobe Suite App configurations API
  phrasing_intents:
  - id: listAppConfigurations
    intent: List a company's app configurations
    question: Which mobile app configurations exist for my company in Tags?
  - id: createAppConfiguration
    intent: Create an app configuration
    question: How do I add push messaging credentials for a mobile app in Tags?
  - id: retrieveAppConfiguration
    intent: Retrieve an app configuration
    question: What settings are stored on a specific app configuration?
  - id: deleteAppConfiguration
    intent: Delete an app configuration
    question: Can I remove an app configuration we no longer use?
  - id: updateAppConfiguration
    intent: Update an app configuration
    question: How do I change the credentials or name of an app configuration?
  - id: retrieveAppConfigurationCompany
    intent: Find the company owning an app configuration
    question: Which company owns a given app configuration?
  phrasing_ops: 6
  slug: adobe-suite-app-configurations-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The applepay/auth API from Adobe Suite — 1 operation(s) for applepay/auth.
  name: Adobe Suite Applepay/auth API
  phrasing_intents:
  - id: GetV1ApplepayAuth
    intent: Get the details needed to pay with Apple Pay
    question: What details does my storefront need before submitting an Apple Pay payment?
  phrasing_ops: 1
  slug: adobe-suite-applepay-auth-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Approval API from Adobe Suite — 4 operation(s) for approval.
  name: Adobe Suite Approval API
  phrasing_intents:
  - id: approvalIsInMyApprovals
    intent: Check if an object awaits my approval
    question: Is a particular item waiting for my approval?
  - id: approvalIsInMySubmittedApprovals
    intent: Check if I submitted an object for approval
    question: Did I submit a particular item for approval?
  - id: getApprovalMyApprovals
    intent: List items awaiting my approval
    question: What is waiting for me to approve?
  - id: getApprovalMySubmittedApprovals
    intent: List items I submitted for approval
    question: Which of my submissions are still out for approval?
  phrasing_ops: 4
  slug: adobe-suite-approval-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Approvalpath API from Adobe Suite — 5 operation(s) for approvalpath.
  name: Adobe Suite Approvalpath API
  phrasing_intents:
  - id: getApprovalPath
    intent: Get one approval path
    question: Who are the approvers on a specific approval path?
  - id: getApprovalPaths
    intent: Get several approval paths by ID
    question: Can I fetch multiple approval paths in one call?
  - id: countApprovalPaths
    intent: Count approval paths
    question: How many approval paths are configured?
  - id: searchApprovalPaths
    intent: Search approval paths
    question: How do I find approval paths tied to a particular approval process?
  - id: reportApprovalPaths
    intent: Run a report on approval paths
    question: Can I get a grouped report of approval paths?
  phrasing_ops: 5
  slug: adobe-suite-approvalpath-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Information for assets, typically images or videos.
  name: Adobe Suite Assets API
  phrasing_intents:
  - id: createAsset
    intent: Create a Lightroom asset with initial metadata
    question: What's the first step to add a new photo to a Lightroom catalog through the API?
  - id: getAsset
    intent: Get a Lightroom catalog asset
    question: How do I read the details of one photo in my Lightroom catalog?
  - id: getAssets
    intent: List assets in a Lightroom catalog
    question: Which photos in my Lightroom catalog were captured within a certain date range?
  - id: createAssetOriginal
    intent: Upload an asset's original file
    question: How do I upload the original image file for a Lightroom asset?
  - id: generateRenditions
    intent: Generate renditions for a Lightroom asset
    question: How can I get Lightroom to regenerate a fullsize or 2560 rendition after an edit?
  - id: getAssetRendition
    intent: Download an asset rendition
    question: Can I download a thumbnail or fullsize rendition of a Lightroom photo?
  - id: putAssetExternalXmpDevelopSetting
    intent: Upload or copy XMP develop settings for an asset
    question: How do I attach an XMP develop settings file to a Lightroom asset?
  - id: getAssetExternalXmpDevelopSetting
    intent: Download an asset's XMP develop settings
    question: Where can I read the external XMP develop settings file for a Lightroom asset?
  phrasing_ops: 12
  slug: adobe-suite-assets-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Assignment API from Adobe Suite — 13 operation(s) for assignment.
  name: Adobe Suite Assignment API
  phrasing_intents:
  - id: getAssignment
    intent: Look up one work assignment
    question: How do I see who a specific assignment in Workfront is given to?
  - id: editAssignment
    intent: Update one assignment
    question: Can I change an existing assignment record by its ID?
  - id: deleteAssignment
    intent: Delete one assignment
    question: How do I remove a single assignment record?
  - id: getAssignments
    intent: Fetch several assignments by ID
    question: Can I load multiple assignments at once when I know their IDs?
  - id: editAssignments
    intent: Update many assignments at once
    question: Is there a bulk edit for assignment records?
  - id: addAssignments
    intent: Create an assignment
    question: How do I create a new assignment record?
  - id: deleteAssignments
    intent: Delete many assignments at once
    question: Can I bulk delete a list of assignments?
  - id: countAssignments
    intent: Count assignments matching filters
    question: How many assignments exist in Workfront right now?
  phrasing_ops: 18
  slug: adobe-suite-assignment-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Attribute based access control policies are statements that bring attributes together to establish permissible and impermissible actions. More information about using this set of endpoints can be foun
  name: Adobe Suite Attribute Based Access Control Policies API
  phrasing_intents:
  - id: listExistingPolicies
    intent: List access control policies
    question: Which attribute-based access control policies exist in my organization?
  - id: createPolicy
    intent: Create an access control policy
    question: How do I create a new attribute-based access policy with rules?
  - id: retrievePolicy
    intent: Get one access control policy
    question: How do I view the rules of one specific access policy?
  - id: updatePolicyByPolicyId
    intent: Replace an access control policy
    question: How do I overwrite an access policy with a complete new definition?
  - id: updatePolicy
    intent: Patch individual policy properties
    question: Can I change just one property of an access policy without resending the whole thing?
  - id: deletePolicy
    intent: Delete an access control policy
    question: How do I delete an access policy we no longer use?
  phrasing_ops: 6
  slug: adobe-suite-attribute-based-access-control-policies-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Attribute based access control products endpoints allow you to manage products as well as permission categories and permission sets associated with products in your organization. More information abou
  name: Adobe Suite Attribute Based Access Control Products API
  phrasing_intents:
  - id: listEntitledProducts
    intent: List entitled products
    question: Which Adobe Experience Platform products is my org entitled to?
  - id: listPermissionCategories
    intent: List a product's permission categories
    question: What permission categories does a given product have?
  - id: listPermissionSets
    intent: List a product's permission sets
    question: Which permission sets can I assign for a product?
  phrasing_ops: 3
  slug: adobe-suite-attribute-based-access-control-products-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Attribute based access control roles define the access that an administrator, a specialist, or an end-user has to resources in your organization. More information about using this set of endpoints can
  name: Adobe Suite Attribute Based Access Control Roles API
  phrasing_intents:
  - id: listExistingRoles
    intent: List access control roles
    question: What roles exist in our Experience Platform access control setup?
  - id: createRole
    intent: Create a role
    question: How do I create a new access control role?
  - id: retrieveRole
    intent: Get a role
    question: What are the details of one access control role, looked up by ID?
  - id: updateRole
    intent: Patch a single role property
    question: Can I change just one property of a role with a patch operation?
  - id: updateRoleByRoleId
    intent: Replace a role's name, description and type
    question: How do I fully update a role's name, description and type together?
  - id: deleteRole
    intent: Delete a role
    question: Can I delete an access control role we no longer use?
  - id: retrieveSubjects
    intent: List the users assigned to a role
    question: Which users are assigned to a given role?
  - id: updateSubjects
    intent: Add or remove users on a role
    question: How do I add a user to an access control role?
  phrasing_ops: 8
  slug: adobe-suite-attribute-based-access-control-roles-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Audience metadata templates allow you to programmatically manage audiences in your destination. <br><br> For a description of when to use this endpoint, see the overview on [audience metadata manageme
  name: Adobe Suite Audience metadata templates API
  phrasing_intents:
  - id: listAudienceTemplate
    intent: List audience metadata templates
    question: What audience metadata templates exist for my Destination SDK destinations?
  - id: createAudienceTemplate
    intent: Create an audience metadata template
    question: How do I create audience metadata config for a destination built with Destination SDK?
  - id: retrieveAudienceTemplate
    intent: Get an audience metadata template
    question: How do I read one audience template's configuration?
  - id: updateAudienceTemplate
    intent: Update an audience metadata template
    question: How do I replace the config of an existing audience template?
  - id: deleteAudienceTemplate
    intent: Delete an audience metadata template
    question: How do I delete an audience template I no longer need?
  phrasing_ops: 5
  slug: adobe-suite-audience-metadata-templates-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Audiences are a set of people, accounts, households, or other entities that share common characteristics and behaviors. This set can be generated either by using Platform or from external sources. Mor
  name: Adobe Suite Audiences API
  phrasing_intents:
  - id: listAudiences
    intent: List audiences
    question: Which audiences exist in my Experience Platform sandbox?
  - id: createAudience
    intent: Create an audience
    question: How do I create a new audience definition in Experience Platform?
  - id: getAudience
    intent: Get an audience's details
    question: What is the definition behind a specific audience?
  - id: deleteAudience
    intent: Delete an audience
    question: Can I permanently delete an audience I no longer need?
  - id: patchAudience
    intent: Change specific attributes of an audience
    question: Can I change just the name or description of an audience without resending it all?
  - id: updateAudience
    intent: Replace an audience definition
    question: How do I overwrite an entire audience with a new definition?
  - id: bulkGetAudiences
    intent: Fetch several audiences by ID
    question: Can I retrieve many audiences in a single request?
  phrasing_ops: 7
  slug: adobe-suite-audiences-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Audit events are timestamped records of observed activities in Experience Platform. The API allows you to query events over the last 90 days and create export requests from the last 365 days in 90 day
  name: Adobe Suite Audit events API
  phrasing_intents:
  - id: listAuditEvents
    intent: Query Platform audit events
    question: Who changed what in my Experience Platform sandbox, according to the audit log?
  - id: exportAuditEvents
    intent: Export Platform audit events
    question: Can I export the Experience Platform audit log to a file?
  - id: getAuditEvents
    intent: List tags audit events
    question: What changes have been made to my tags properties recently?
  - id: retrieveAuditEvent
    intent: Get a tags audit event
    question: How do I look up a single tags audit event by ID?
  phrasing_ops: 4
  slug: adobe-suite-audit-events-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Schema Registry maintains a log of all the changes that have occurred to a resource (class, field group, data type, or schema) between different updates.
  name: Adobe Suite Audit log API
  phrasing_intents:
  - id: retrieveAuditLog
    intent: See the change history of a schema resource
    question: How do I see every change made to an XDM schema or field group?
  phrasing_ops: 1
  slug: adobe-suite-audit-log-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Auditloginassession API from Adobe Suite — 9 operation(s) for auditloginassession.
  name: Adobe Suite Auditloginassession API
  phrasing_intents:
  - id: getAuditLoginAsSession
    intent: Get one log-in-as audit session
    question: How do I look up one record of an admin logging in as another user?
  - id: getAuditLoginAsSessions
    intent: Get several log-in-as sessions by ID
    question: Can I load multiple log-in-as audit sessions from a list of IDs?
  - id: countAuditLoginAsSessions
    intent: Count log-in-as audit sessions
    question: How many times have admins logged in as other users?
  - id: searchAuditLoginAsSessions
    intent: Search log-in-as audit sessions
    question: How do I find impersonation sessions within a date range?
  - id: reportAuditLoginAsSessions
    intent: Aggregate report of log-in-as sessions
    question: Can I get totals of impersonation sessions grouped by admin?
  - id: auditLoginAsSessionAllAccessedUsers
    intent: List every user who was logged in as
    question: Which users have ever had an admin log in as them?
  - id: auditLoginAsSessionAllAdmins
    intent: List every admin who used log-in-as
    question: Which administrators have used the log-in-as feature?
  - id: auditLoginAsSessionGetAccessedUsers
    intent: List users one admin has logged in as
    question: Whose accounts has a particular admin logged in as?
  phrasing_ops: 9
  slug: adobe-suite-auditloginassession-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Avatar API from Adobe Suite — 2 operation(s) for avatar.
  name: Adobe Suite Avatar API
  phrasing_intents:
  - id: getAvatar
    intent: Get one avatar
    question: How do I fetch a single avatar record in Workfront?
  - id: editAvatar
    intent: Update an avatar
    question: Can I change an existing avatar?
  - id: deleteAvatar
    intent: Delete an avatar
    question: How do I delete an avatar?
  - id: getAvatars
    intent: Fetch several avatars by ID
    question: Can I load multiple avatars at once by their IDs?
  - id: editAvatars
    intent: Bulk update avatars
    question: How do I edit many avatars in one request?
  - id: addAvatars
    intent: Create an avatar
    question: How do I create a new avatar?
  - id: deleteAvatars
    intent: Bulk delete avatars
    question: Can I delete several avatars at once?
  phrasing_ops: 7
  slug: adobe-suite-avatar-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Awaitingapproval API from Adobe Suite — 7 operation(s) for awaitingapproval.
  name: Adobe Suite Awaitingapproval API
  phrasing_intents:
  - id: getAwaitingApproval
    intent: Look up one pending approval
    question: How do I see the details of one item waiting for approval in Workfront?
  - id: deleteAwaitingApproval
    intent: Delete one pending approval record
    question: Can I remove a single awaiting-approval record?
  - id: getAwaitingApprovals
    intent: Fetch several pending approvals by ID
    question: Can I load a batch of awaiting approvals when I have their IDs?
  - id: addAwaitingApprovals
    intent: Create an awaiting-approval record
    question: What do I send to create a new awaiting-approval record?
  - id: deleteAwaitingApprovals
    intent: Delete many pending approval records
    question: Can I bulk delete awaiting approvals by listing their IDs?
  - id: countAwaitingApprovals
    intent: Count pending approvals
    question: How many items are awaiting approval across the system for a filter?
  - id: searchAwaitingApprovals
    intent: Search pending approvals
    question: How do I find approvals waiting on a particular approver or object?
  - id: reportAwaitingApprovals
    intent: Run an aggregate report on pending approvals
    question: Can I get grouped totals of pending approvals as a report?
  phrasing_ops: 10
  slug: adobe-suite-awaitingapproval-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Base connections retain information regarding how to connect to a source or target. For destinations, the source that you are connecting to is Experience Platform data and the target is the desired de
  name: Adobe Suite Base connections API
  phrasing_intents:
  - id: getConnections
    intent: List destination base connections
    question: How do I see all the destination base connections in my organization?
  - id: postTargetBaseConnection
    intent: Create a target base connection
    question: How do I authorize a new connection to a destination?
  - id: getConnectionById
    intent: Get a base connection's details
    question: What configuration does one base connection have?
  - id: patchConnectionById
    intent: Update a base connection
    question: How do I update the credentials on an existing base connection?
  - id: deleteConnectionById
    intent: Delete a base connection
    question: What's the way to delete a destination base connection?
  phrasing_ops: 5
  slug: adobe-suite-base-connections-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Baseline API from Adobe Suite — 5 operation(s) for baseline.
  name: Adobe Suite Baseline API
  phrasing_intents:
  - id: getBaseline
    intent: Get a Workfront baseline
    question: How do I fetch one Workfront project baseline by ID?
  - id: editBaseline
    intent: Edit a Workfront baseline
    question: How do I update one project baseline?
  - id: deleteBaseline
    intent: Delete a Workfront baseline
    question: How do I delete one project baseline?
  - id: getBaselines
    intent: Get several baselines by ID
    question: How do I fetch multiple baselines in one request?
  - id: editBaselines
    intent: Bulk edit baselines
    question: How do I update many baselines at once?
  - id: addBaselines
    intent: Create a project baseline
    question: How do I create a new baseline to snapshot a project's plan?
  - id: deleteBaselines
    intent: Bulk delete baselines
    question: How do I delete several baselines in one call?
  - id: countBaselines
    intent: Count baselines
    question: How many baselines exist in Workfront?
  phrasing_ops: 10
  slug: adobe-suite-baseline-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Baselinetask API from Adobe Suite — 5 operation(s) for baselinetask.
  name: Adobe Suite Baselinetask API
  phrasing_intents:
  - id: getBaselineTask
    intent: Get a baseline task
    question: How do I look up a task as it was captured in a project baseline?
  - id: getBaselineTasks
    intent: Fetch several baseline tasks by ID
    question: Can I retrieve multiple baseline tasks in one request by their IDs?
  - id: countBaselineTasks
    intent: Count baseline tasks
    question: How many baseline tasks are recorded?
  - id: searchBaselineTasks
    intent: Search baseline tasks
    question: What's the way to search baseline tasks, for example by their baseline dates?
  - id: reportBaselineTasks
    intent: Report on baseline tasks
    question: Can I produce an aggregated report of baseline tasks?
  phrasing_ops: 5
  slug: adobe-suite-baselinetask-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'Batch ingestion is used to ingest data into Experience Platform as batch files. For example, data being ingested can be the profile data from a flat file in a CRM system (for example: Parquet or JSON)'
  name: Adobe Suite Batch Ingestion API
  phrasing_intents:
  - id: createBatch
    intent: Start a new ingestion batch for a dataset
    question: How do I open a batch before uploading files to a dataset?
  - id: uploadSmallFile
    intent: Upload a small file into a batch
    question: How do I upload a file under 256MB to a dataset in my batch?
  - id: uploadLargeFilePart
    intent: Upload one part of a large file
    question: How do I send a chunk of a big file after initializing the upload?
  - id: completeLargeFileUpload
    intent: Initialize or finish a large file upload
    question: How do I begin uploading a file larger than 256MB to a batch?
  - id: getLargeFileStatus
    intent: Check how much of a large file has arrived
    question: How can I see which byte ranges of my large upload the server has received?
  - id: retrievePreview
    intent: Preview the data uploaded to a batch
    question: Can I preview the rows I have uploaded before completing a batch?
  - id: completeBatch
    intent: Complete a batch to trigger promotion
    question: How do I signal that all files for a batch are uploaded?
  phrasing_ops: 7
  slug: adobe-suite-batch-ingestion-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Batched requests allow users to supply an array of objects in the request payload, representing what would normally be individual requests.
  name: Adobe Suite Batched requests API
  phrasing_intents:
  - id: listBatchedRequest
    intent: List Catalog batched requests
    question: Can I see the batched requests previously sent to Catalog Service?
  - id: createBatchedRequest
    intent: Send several Catalog requests in one batch
    question: Can I bundle multiple Catalog Service calls into a single request?
  phrasing_ops: 2
  slug: adobe-suite-batched-requests-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Batches allow users to understand which operations and applications have been performed on objects tracked by the system.
  name: Adobe Suite Batches API
  phrasing_intents:
  - id: listBatches
    intent: List ingestion batches in the catalog
    question: How do I list the data batches tracked by the Experience Platform catalog?
  - id: createBatch
    intent: Create a new catalog batch
    question: How do I register a new batch in the catalog to track an ingestion?
  - id: retrieveUniqueBatchValues
    intent: Look up distinct values of a batch field
    question: How can I see every distinct value stored in one field across my batches?
  - id: retrieveBatch
    intent: Look up a catalog batch
    question: How do I get the details of one catalog batch by its ID?
  - id: updateBatch
    intent: Replace a catalog batch's details
    question: How do I overwrite a batch record with a full new version?
  - id: createBatchWithId
    intent: Create a catalog batch under a chosen ID
    question: Can I create a batch using a specific ID instead of letting the catalog assign one?
  - id: deleteBatch
    intent: Delete a catalog batch (deprecated)
    question: How do I delete a batch record from the catalog?
  - id: patchBatch
    intent: Update selected fields on a catalog batch
    question: Can I change just a few attributes of a batch without resending all of it?
  phrasing_ops: 12
  slug: adobe-suite-batches-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Behaviors define the nature of data that a schema describes. Each XDM class must reference a specific behavior, which all schemas that employ that class will inherit. Schemas that inherit the "record"
  name: Adobe Suite Behaviors API
  phrasing_intents:
  - id: listBehaviors
    intent: List schema behaviors
    question: Which schema behaviors, like record or time-series, are available?
  - id: retrieveBehavior
    intent: Get a schema behavior
    question: What fields does a specific behavior like time-series add?
  phrasing_ops: 2
  slug: adobe-suite-behaviors-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Beta API from Adobe Suite — 4 operation(s) for beta.
  name: Adobe Suite Beta API
  phrasing_intents:
  - id: taggedDocuments
    intent: List tagged Adobe Express documents
    question: Which tagged Adobe Express documents can I access, including ones shared with me?
  - id: taggedDocumentDetails
    intent: Get pages and tagged elements of a document
    question: How do I see the pages and tagged elements inside one Express document?
  - id: generateVariation
    intent: Generate a variation of a tagged document
    question: How do I create a new version of an Express template with different text or images?
  - id: exportRendition
    intent: Export Express pages as images, video or PDF
    question: How do I export pages of an Adobe Express document as PNG or PDF?
  phrasing_ops: 4
  slug: adobe-suite-beta-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Billingrecord API from Adobe Suite — 6 operation(s) for billingrecord.
  name: Adobe Suite Billingrecord API
  phrasing_intents:
  - id: getBillingRecord
    intent: Get a billing record by ID
    question: What amounts and status does a specific billing record in Workfront show?
  - id: editBillingRecord
    intent: Update a billing record
    question: How do I change the description or status of an existing billing record?
  - id: deleteBillingRecord
    intent: Delete a billing record
    question: How do I remove a billing record created by mistake?
  - id: getBillingRecords
    intent: Get several billing records by their IDs
    question: Can I fetch multiple billing records at once?
  - id: editBillingRecords
    intent: Bulk-update several billing records
    question: Can I update many billing records in a single request?
  - id: addBillingRecords
    intent: Create a billing record
    question: How do I create a billing record for a project?
  - id: deleteBillingRecords
    intent: Delete several billing records at once
    question: Can I delete a batch of billing records together?
  - id: countBillingRecords
    intent: Count billing records
    question: How many billing records do we have?
  phrasing_ops: 11
  slug: adobe-suite-billingrecord-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Bitrate API from Adobe Suite — 1 operation(s) for bitrate.
  name: Adobe Suite Bitrate API
  phrasing_intents:
  - id: bitrateChange
    intent: Report a bitrate change in a media session
    question: How do I tell Adobe media tracking that a stream's bitrate changed?
  phrasing_ops: 1
  slug: adobe-suite-bitrate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Branches API from Adobe Suite — 1 operation(s) for branches.
  name: Adobe Suite Branches API
  phrasing_intents:
  - id: getBranches
    intent: List branches in a program repository
    question: Which git branches exist in my Cloud Manager repository?
  phrasing_ops: 1
  slug: adobe-suite-branches-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Budgetedhour API from Adobe Suite — 3 operation(s) for budgetedhour.
  name: Adobe Suite Budgetedhour API
  phrasing_intents:
  - id: getBudgetedHour
    intent: Get one budgeted hour entry
    question: How many hours were budgeted in a specific budgeted hour record?
  - id: deleteBudgetedHour
    intent: Delete a budgeted hour entry
    question: How do I remove one budgeted hour entry?
  - id: getBudgetedHours
    intent: Get several budgeted hour entries by ID
    question: Can I fetch several budgeted hour records at once?
  - id: addBudgetedHours
    intent: Create a budgeted hour entry
    question: How do I budget hours for resource planning?
  - id: deleteBudgetedHours
    intent: Delete several budgeted hour entries
    question: Can I bulk delete budgeted hour records?
  - id: searchBudgetedHours
    intent: Search budgeted hour entries
    question: How do I find budgeted hours for a project or resource pool?
  phrasing_ops: 6
  slug: adobe-suite-budgetedhour-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Buffer API from Adobe Suite — 1 operation(s) for buffer.
  name: Adobe Suite Buffer API
  phrasing_intents:
  - id: bufferStart
    intent: Report that video buffering started
    question: How do I tell media analytics that playback is buffering?
  phrasing_ops: 1
  slug: adobe-suite-buffer-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: A tag library is compiled into a build in order for it to be assigned to an environment for testing and deployment. The contents of a build varies depending on the resources included in the library, t
  name: Adobe Suite Builds API
  phrasing_intents:
  - id: listLibraryBuilds
    intent: List a tags library's builds
    question: How do I see all the builds that were made from a tags library?
  - id: createBuild
    intent: Build a tags library
    question: How can I create a new build of a library so its changes can be published?
  - id: getBuild
    intent: Look up a build
    question: How do I check the status of one build by its ID?
  - id: republishBuild
    intent: Republish an existing build
    question: Can I republish a build without creating a new one?
  phrasing_ops: 4
  slug: adobe-suite-builds-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Burndownevent API from Adobe Suite — 5 operation(s) for burndownevent.
  name: Adobe Suite Burndownevent API
  phrasing_intents:
  - id: getBurndownEvent
    intent: Get a single burndown event
    question: How do I look up one agile burndown event by ID?
  - id: getBurndownEvents
    intent: Get several burndown events by ID
    question: Can I fetch multiple burndown events in one call?
  - id: countBurndownEvents
    intent: Count burndown events
    question: How many burndown events have been recorded?
  - id: searchBurndownEvents
    intent: Search burndown events with filters
    question: How do I find burndown events for a particular iteration?
  - id: reportBurndownEvents
    intent: Run a report on burndown events
    question: Can I get aggregated report data about burndown events?
  phrasing_ops: 5
  slug: adobe-suite-burndownevent-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Calculated Metrics API from Adobe Suite — 5 operation(s) for calculated metrics.
  name: Adobe Suite Calculated Metrics API
  phrasing_intents:
  - id: findCalculatedMetrics
    intent: List calculated metrics
    question: Which calculated metrics exist in our Adobe Analytics company?
  - id: calculatedmetrics_createCalculatedMetric
    intent: Create a calculated metric
    question: How do I create a new calculated metric such as visits per visitor?
  - id: calculatedmetrics_getCalculatedMetricFunctions
    intent: List functions available to calculated metrics
    question: What functions can I use inside a calculated metric formula?
  - id: calculatedmetrics_getCalculatedMetricFunction
    intent: Get one calculated metric function
    question: What arguments does a specific calculated metric function take?
  - id: calculatedmetrics_validateCalculatedMetric
    intent: Validate a calculated metric definition
    question: Can I check a calculated metric definition is valid before saving it?
  - id: findOneCalculatedMetric
    intent: Get one calculated metric
    question: How do I retrieve a single calculated metric and its definition?
  - id: calculatedmetrics_updateCalculatedMetric
    intent: Update a calculated metric
    question: Can I change the formula of an existing calculated metric?
  - id: calculatedmetrics_deleteCalculatedMetric
    intent: Delete a calculated metric
    question: How do I remove a calculated metric we no longer use?
  phrasing_ops: 8
  slug: adobe-suite-calculated-metrics-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Calendarentry API from Adobe Suite — 5 operation(s) for calendarentry.
  name: Adobe Suite Calendarentry API
  phrasing_intents:
  - id: getCalendarEntry
    intent: Look up one calendar entry
    question: What details are stored on a single Workfront calendar entry?
  - id: editCalendarEntry
    intent: Edit a calendar entry
    question: How do I change the date or title of one calendar entry?
  - id: deleteCalendarEntry
    intent: Delete a calendar entry
    question: Can I remove one entry from a calendar?
  - id: getCalendarEntrys
    intent: Fetch several calendar entries by ID
    question: Can I pull multiple calendar entries at once by their IDs?
  - id: editCalendarEntrys
    intent: Bulk edit calendar entries
    question: Can I update several calendar entries in one request?
  - id: addCalendarEntrys
    intent: Create a calendar entry
    question: How do I add a new entry to a Workfront calendar?
  - id: deleteCalendarEntrys
    intent: Delete several calendar entries
    question: Can I bulk delete old calendar entries?
  - id: countCalendarEntrys
    intent: Count calendar entries
    question: How many calendar entries are there?
  phrasing_ops: 10
  slug: adobe-suite-calendarentry-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Calendarentryexternalreference API from Adobe Suite — 5 operation(s) for calendarentryexternalreference.
  name: Adobe Suite Calendarentryexternalreference API
  phrasing_intents:
  - id: getCalendarEntryExternalReference
    intent: Get one calendar entry external reference
    question: How do I look up a single external reference attached to a calendar entry?
  - id: getCalendarEntryExternalReferences
    intent: Get several calendar external references
    question: Can I load multiple calendar entry external references from their IDs?
  - id: countCalendarEntryExternalReferences
    intent: Count calendar entry external references
    question: How many external references are linked to calendar entries?
  - id: searchCalendarEntryExternalReferences
    intent: Search calendar entry external references
    question: How do I find calendar external references for a given entry?
  - id: reportCalendarEntryExternalReferences
    intent: Aggregate report of calendar external references
    question: Can I get grouped totals of calendar entry external references?
  phrasing_ops: 5
  slug: adobe-suite-calendarentryexternalreference-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Calendarportalsection API from Adobe Suite — 5 operation(s) for calendarportalsection.
  name: Adobe Suite Calendarportalsection API
  phrasing_intents:
  - id: getCalendarPortalSection
    intent: Get one calendar portal section
    question: How do I look up a single calendar portal section in Workfront?
  - id: getCalendarPortalSections
    intent: Get several calendar portal sections by ID
    question: Can I fetch multiple calendar portal sections at once by ID?
  - id: addCalendarPortalSections
    intent: Create or copy a calendar portal section
    question: How do I add a new calendar to the portal?
  - id: countCalendarPortalSections
    intent: Count calendar portal sections
    question: How many calendar portal sections do we have?
  - id: searchCalendarPortalSections
    intent: Search calendar portal sections
    question: Which calendar portal sections match a name or owner?
  - id: reportCalendarPortalSections
    intent: Run an aggregate report on calendar sections
    question: Can I get a grouped summary report of calendar portal sections?
  phrasing_ops: 6
  slug: adobe-suite-calendarportalsection-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Calendarsection API from Adobe Suite — 7 operation(s) for calendarsection.
  name: Adobe Suite Calendarsection API
  phrasing_intents:
  - id: getCalendarSection
    intent: Get a single calendar section
    question: How do I look up one Workfront calendar section by ID?
  - id: editCalendarSection
    intent: Edit one calendar section
    question: Can I change the color or filter of one calendar section?
  - id: deleteCalendarSection
    intent: Delete one calendar section
    question: How do I remove a single section from a calendar?
  - id: getCalendarSections
    intent: Get several calendar sections by ID
    question: Can I fetch several calendar sections at once by their IDs?
  - id: editCalendarSections
    intent: Edit many calendar sections at once
    question: Can I update a batch of calendar sections in one request?
  - id: addCalendarSections
    intent: Create a calendar section
    question: How do I add a new section to a Workfront calendar?
  - id: deleteCalendarSections
    intent: Delete many calendar sections at once
    question: Can I delete a list of calendar sections in one call?
  - id: countCalendarSections
    intent: Count calendar sections
    question: How many calendar sections exist across our calendars?
  phrasing_ops: 12
  slug: adobe-suite-calendarsection-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: A callback is a message that Platform sends to a URL host whenever a new audit event is generated.
  name: Adobe Suite Callbacks API
  phrasing_intents:
  - id: listCallbacks
    intent: List a property's callbacks
    question: Which callbacks are registered on my tag property?
  - id: createCallback
    intent: Register a callback on a property
    question: How do I get a webhook when events happen on a tag property?
  - id: retrieveCallback
    intent: Get a callback
    question: What URL and subscriptions does a specific callback have?
  - id: deleteCallback
    intent: Delete a callback
    question: Can I stop a callback from receiving notifications by deleting it?
  - id: updateCallback
    intent: Update a callback
    question: How do I change the URL or subscriptions on an existing callback?
  phrasing_ops: 5
  slug: adobe-suite-callbacks-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Campaign Preview API API from Adobe Suite — 1 operation(s) for campaign preview api.
  name: Adobe Suite Campaign Preview API
  phrasing_intents:
  - id: createCampaignPreview
    intent: Preview a campaign for sample profiles
    question: How will my campaign render for a particular customer profile?
  phrasing_ops: 1
  slug: adobe-suite-campaign-preview-api-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Campaign Proof API API from Adobe Suite — 2 operation(s) for campaign proof api.
  name: Adobe Suite Campaign Proof API
  phrasing_intents:
  - id: triggerCampaignProof
    intent: Send a proof of a campaign
    question: How do I send a test proof of a Journey Optimizer campaign before launch?
  - id: getCampaignProofStatus
    intent: Check a campaign proof job's status
    question: Has my campaign proof finished sending?
  phrasing_ops: 2
  slug: adobe-suite-campaign-proof-api-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Campaign management resource
  name: Adobe Suite Campaign Resource API
  phrasing_intents:
  - id: getCampaignMessageOrVariant
    intent: Get a channel variant of a campaign message
    question: How do I fetch one channel-specific variant of a campaign message?
  - id: getCampaigns
    intent: List campaigns
    question: Which campaigns exist in my sandbox?
  - id: getCampaignVersions
    intent: List a campaign's versions
    question: What versions has a campaign gone through?
  - id: getCampaign
    intent: Get a campaign's details
    question: What are the settings and status of one campaign?
  - id: getCampaignPublishingNotifications
    intent: Check a campaign's publishing validation
    question: Why won't my campaign publish, and which validation issues are blocking it?
  - id: getCampaignPackage
    intent: Get a campaign package's details
    question: What's inside a package attached to a campaign?
  - id: getCampaignMessageOrVariant_1
    intent: Get a campaign message
    question: How do I read a campaign message as a whole, not a single channel variant?
  phrasing_ops: 7
  slug: adobe-suite-campaign-resource-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Capping configuration API from Adobe Suite — 6 operation(s) for capping configuration.
  name: Adobe Suite Capping configuration API
  phrasing_intents:
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/post/endpointconfigs.jsonPublic
    intent: Cap calls journeys make to an endpoint
    question: How do I limit how many calls my journeys send to an external endpoint URL?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/get/endpointconfigs_uid.jsonPublic
    intent: Get an endpoint capping configuration
    question: What rate limit is currently defined for a given capping configuration?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/put/endpointconfigs_uid.jsonPublic
    intent: Overwrite an endpoint capping configuration
    question: Can I change the call limit on an existing capping configuration?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/delete/endpointconfigs_uid.jsonPublic
    intent: Delete an endpoint capping configuration
    question: Can I delete a capping configuration that is still deployed?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/get/endpointconfigs_uid_candeploy.jsonPublic
    intent: Check if a capping configuration can deploy
    question: Is my endpoint capping configuration valid enough to deploy?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/post/endpointconfigs_uid_deploy.jsonPublic
    intent: Deploy an endpoint capping configuration
    question: How do I make a capping configuration take effect on live journeys?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/post/endpointconfigs_uid_undeploy.jsonPublic
    intent: Undeploy an endpoint capping configuration
    question: Can I temporarily stop enforcing a capping configuration without deleting it?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/post/list_endpointconfigs.jsonPublic
    intent: List all endpoint capping configurations
    question: Which endpoint capping configurations exist in my organization and sandbox?
  phrasing_ops: 8
  slug: adobe-suite-capping-configuration-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The carts/guest-carts/{cartId}/checkGiftCard/{giftCardCode} API from Adobe Suite — 1 operation(s) for carts/guest-carts/{cartid}/checkgiftcard/{giftcardcode}.
  name: Adobe Suite Carts/guest Carts/{cart Id}/check Gift Card/{gift Card Code} API
  phrasing_intents:
  - id: GetV1CartsGuestcartsCartIdCheckGiftCardGiftCardCode
    intent: Check a gift card balance on a guest cart
    question: How much balance is left on a gift card a guest added to their cart?
  phrasing_ops: 1
  slug: adobe-suite-carts-guest-carts-cartid-checkgiftcard-giftcardcode-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The carts/guest-carts/{cartId}/giftCards API from Adobe Suite — 1 operation(s) for carts/guest-carts/{cartid}/giftcards.
  name: Adobe Suite Carts/guest Carts/{cart Id}/gift Cards API
  phrasing_intents:
  - id: PostV1CartsGuestcartsCartIdGiftCards
    intent: Apply a gift card to a guest cart
    question: How does a guest shopper redeem a gift card at checkout?
  phrasing_ops: 1
  slug: adobe-suite-carts-guest-carts-cartid-giftcards-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The carts/guest-carts/{cartId}/giftCards/{giftCardCode} API from Adobe Suite — 1 operation(s) for carts/guest-carts/{cartid}/giftcards/{giftcardcode}.
  name: Adobe Suite Carts/guest Carts/{cart Id}/gift Cards/{gift Card Code} API
  phrasing_intents:
  - id: DeleteV1CartsGuestcartsCartIdGiftCardsGiftCardCode
    intent: Remove a gift card from a guest cart
    question: How do I take a gift card off a guest shopper's cart?
  phrasing_ops: 1
  slug: adobe-suite-carts-guest-carts-cartid-giftcards-giftcardcode-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The carts/mine API from Adobe Suite — 1 operation(s) for carts/mine.
  name: Adobe Suite Carts/mine API
  phrasing_intents:
  - id: PutV1CartsMine
    intent: Save the signed-in customer's cart
    question: How do I save changes to my own cart as a logged-in customer?
  - id: GetV1CartsMine
    intent: Get the signed-in customer's cart
    question: How do I get the current shopping cart for the logged-in customer?
  phrasing_ops: 2
  slug: adobe-suite-carts-mine-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The carts/mine/balance/apply API from Adobe Suite — 1 operation(s) for carts/mine/balance/apply.
  name: Adobe Suite Carts/mine/balance/apply API
  phrasing_intents:
  - id: PostV1CartsMineBalanceApply
    intent: Apply store credit to my cart
    question: How do I use my store credit balance at checkout?
  phrasing_ops: 1
  slug: adobe-suite-carts-mine-balance-apply-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The carts/mine/checkGiftCard/{giftCardCode} API from Adobe Suite — 1 operation(s) for carts/mine/checkgiftcard/{giftcardcode}.
  name: Adobe Suite Carts/mine/check Gift Card/{gift Card Code} API
  phrasing_intents:
  - id: GetV1CartsMineCheckGiftCardGiftCardCode
    intent: Check a gift card balance on my cart
    question: What's the remaining balance on a gift card applied to my shopping cart?
  phrasing_ops: 1
  slug: adobe-suite-carts-mine-checkgiftcard-giftcardcode-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The carts/mine/collect-totals API from Adobe Suite — 1 operation(s) for carts/mine/collect-totals.
  name: Adobe Suite Carts/mine/collect Totals API
  phrasing_intents:
  - id: PutV1CartsMineCollecttotals
    intent: Set my cart's payment and shipping and get totals
    question: Can I choose payment and shipping methods on my cart and see the updated total?
  phrasing_ops: 1
  slug: adobe-suite-carts-mine-collect-totals-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The carts/mine/payment-information API from Adobe Suite — 1 operation(s) for carts/mine/payment-information.
  name: Adobe Suite Carts/mine/payment Information API
  phrasing_intents:
  - id: PostV1CartsMinePaymentinformation
    intent: Set payment and place order for my cart
    question: How do I set a payment method and place the order on my cart in one step?
  - id: GetV1CartsMinePaymentinformation
    intent: Get payment info for my cart
    question: Which payment methods and totals apply to my current cart?
  phrasing_ops: 2
  slug: adobe-suite-carts-mine-payment-information-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The carts/mine/po-payment-information API from Adobe Suite — 1 operation(s) for carts/mine/po-payment-information.
  name: Adobe Suite Carts/mine/po Payment Information API
  phrasing_intents:
  - id: PostV1CartsMinePopaymentinformation
    intent: Pay and place a purchase order for my cart
    question: How does a logged-in B2B customer check out their cart as a purchase order?
  phrasing_ops: 1
  slug: adobe-suite-carts-mine-po-payment-information-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The carts/mine/set-payment-information API from Adobe Suite — 1 operation(s) for carts/mine/set-payment-information.
  name: Adobe Suite Carts/mine/set Payment Information API
  phrasing_intents:
  - id: PostV1CartsMineSetpaymentinformation
    intent: Set payment method on my cart
    question: How does a logged-in customer set a payment method on their cart without placing the order?
  phrasing_ops: 1
  slug: adobe-suite-carts-mine-set-payment-information-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Catalog information for the authenticated user.
  name: Adobe Suite Catalogs API
  phrasing_intents:
  - id: getCatalog
    intent: Get the user's Lightroom catalog metadata
    question: How do I get the ID of my Lightroom catalog before listing assets or albums?
  phrasing_ops: 1
  slug: adobe-suite-catalogs-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Manage categories in a hierarchical structure with localization support. Categories organize products into logical groups and support nested hierarchies using slug-based paths. Category management inc
  name: Adobe Suite Categories API
  phrasing_intents:
  - id: createCategories
    intent: Create product catalog categories
    question: How do I create nested product categories like men/clothing/pants?
  - id: updateCategories
    intent: Update product catalog categories
    question: Can I change the display name of existing catalog categories?
  - id: deleteCategories
    intent: Delete catalog categories and children
    question: Does deleting a category also remove its child categories?
  phrasing_ops: 3
  slug: adobe-suite-categories-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Category API from Adobe Suite — 20 operation(s) for category.
  name: Adobe Suite Category API
  phrasing_intents:
  - id: getCategory
    intent: Get a single custom form category
    question: What does one custom form category in Workfront look like when I fetch it by ID?
  - id: editCategory
    intent: Edit a single category
    question: How can I change the settings of one existing category?
  - id: deleteCategory
    intent: Delete a single category
    question: How do I remove one category I no longer use?
  - id: getCategorys
    intent: Get several categories by ID at once
    question: Can I fetch a handful of categories in one call by passing their IDs?
  - id: editCategorys
    intent: Edit many categories in one request
    question: Is there a way to update several categories in a single bulk request?
  - id: addCategorys
    intent: Create or copy a category
    question: How do I create a new custom form category?
  - id: deleteCategorys
    intent: Delete several categories at once
    question: Can I delete a batch of categories in one go by listing their IDs?
  - id: countCategorys
    intent: Count categories matching a filter
    question: How many categories exist in our Workfront instance?
  phrasing_ops: 25
  slug: adobe-suite-category-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Categoryaccessrule API from Adobe Suite — 6 operation(s) for categoryaccessrule.
  name: Adobe Suite Categoryaccessrule API
  phrasing_intents:
  - id: getCategoryAccessRule
    intent: Get one custom form access rule
    question: Who has access to a custom form according to a specific category access rule?
  - id: deleteCategoryAccessRule
    intent: Delete a single category access rule
    question: Can I revoke one sharing rule on a custom form?
  - id: getCategoryAccessRules
    intent: Fetch several category access rules by ID
    question: Can I pull multiple category access rules in one request by ID?
  - id: addCategoryAccessRules
    intent: Share a custom form via an access rule
    question: How do I share a custom form with another user or team?
  - id: deleteCategoryAccessRules
    intent: Delete several category access rules by ID
    question: Can I remove many custom form sharing rules at once?
  - id: countCategoryAccessRules
    intent: Count category access rules
    question: How many custom form access rules exist?
  - id: searchCategoryAccessRules
    intent: Search category access rules
    question: Which access rules grant a particular team access to custom forms?
  - id: reportCategoryAccessRules
    intent: Run an aggregate report on access rules
    question: Can I get grouped totals of category access rules by access level?
  phrasing_ops: 9
  slug: adobe-suite-categoryaccessrule-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Manage category attribute definitions. These settings control how category attributes appear and function throughout the storefront. Category attribute metadata specifies how category attributes are d
  name: Adobe Suite Category Metadata API
  phrasing_intents:
  - id: createCategoryMetadata
    intent: Create category attribute metadata
    question: How do I define a new category attribute with its data type in the Commerce catalog?
  - id: updateCategoryMetadata
    intent: Update category attribute metadata
    question: Can I change category attribute metadata that already exists?
  - id: deleteCategoryMetadata
    intent: Delete category attribute metadata
    question: What's the way to remove category attribute metadata from the catalog?
  phrasing_ops: 3
  slug: adobe-suite-categorymetadata-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The challenge-controller API from Adobe Suite — 3 operation(s) for challenge-controller.
  name: Adobe Suite Challenge Controller API
  phrasing_intents:
  - id: bulkWithdraw
    intent: Withdraw a profile from loyalty challenges
    question: How do I pull a loyalty member out of several challenges at once?
  - id: activeChallengeStateByProfileWithPayload
    intent: Get a profile's active challenge state
    question: Which loyalty challenges is a member currently active in, and how far along are they?
  - id: bulkSignup
    intent: Sign a profile up for loyalty challenges
    question: How do I enroll a loyalty member in multiple challenges in one call?
  phrasing_ops: 3
  slug: adobe-suite-challenge-controller-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Profile interaction with a Challenge affecting its state
  name: Adobe Suite Challenge State API
  phrasing_intents:
  - id: withdraw
    intent: Withdraw a profile from a loyalty challenge
    question: How do I pull a customer out of a loyalty challenge they joined?
  - id: activeChallengeStateByProfile
    intent: Get a profile's challenge state
    question: What is a customer's current progress state across loyalty challenges?
  - id: signup
    intent: Sign a profile up for a loyalty challenge
    question: How do I enroll a customer in a loyalty challenge?
  - id: events
    intent: Send a loyalty event to challenges
    question: How do I feed a customer event into loyalty challenges so progress updates?
  - id: activeChallengesByProfile
    intent: List active challenges for a profile
    question: Which loyalty challenges is this customer currently in?
  - id: activeChallenges
    intent: List all active challenges in the org
    question: What loyalty challenges are running across my organization right now?
  - id: healthCheck
    intent: Check the loyalty challenge service health
    question: Is the loyalty challenge service up?
  - id: challengeDetail
    intent: Get challenge details for a profile
    question: How do I see the full details of a challenge for a particular customer?
  phrasing_ops: 8
  slug: adobe-suite-challenge-state-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Manage the creation, updating, deleting, and retrieval of Challenges
  name: Adobe Suite Challenges API
  phrasing_intents:
  - id: readOne_1
    intent: Get a loyalty challenge
    question: What tasks and rewards are set up on one particular loyalty challenge?
  - id: update_1
    intent: Replace a loyalty challenge entirely
    question: How do I overwrite a whole loyalty challenge definition with a new one?
  - id: delete_1
    intent: Delete a loyalty challenge and its journey
    question: What happens to the linked journey when I delete a loyalty challenge?
  - id: patch_1
    intent: Partially update a loyalty challenge
    question: Can I change only a few top-level fields of a challenge without resending the whole thing?
  - id: readMany_1
    intent: List loyalty challenges
    question: Which loyalty challenges have we set up in this sandbox?
  - id: create_1
    intent: Create a loyalty challenge
    question: How do I set up a new loyalty challenge for customers to complete?
  - id: unPublish
    intent: Unpublish a loyalty challenge
    question: How can I take a live loyalty challenge away from customers?
  - id: publish
    intent: Publish a loyalty challenge to customers
    question: What makes a loyalty challenge go live for customers?
  phrasing_ops: 11
  slug: adobe-suite-challenges-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Chapter API from Adobe Suite — 3 operation(s) for chapter.
  name: Adobe Suite Chapter API
  phrasing_intents:
  - id: chapterStart
    intent: Track the start of a chapter
    question: How do I signal that a video chapter has begun?
  - id: chapterComplete
    intent: Track a chapter finishing
    question: How do I report that a viewer finished a chapter?
  - id: chapterSkip
    intent: Track a skipped chapter
    question: How do I record that a viewer skipped a chapter?
  phrasing_ops: 3
  slug: adobe-suite-chapter-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Classes define behavioral aspects of the data within the schema and describe the smallest number of common properties contained in all schemas that implement the same class.
  name: Adobe Suite Classes API
  phrasing_intents:
  - id: listClasses
    intent: List XDM classes
    question: How do I see all the XDM classes available in the Schema Registry?
  - id: retrieveClass
    intent: Get an XDM class
    question: How can I look up one XDM class definition by its ID?
  - id: createClass
    intent: Create a custom XDM class
    question: How do I define my own XDM class in the Schema Registry?
  - id: replaceClass
    intent: Replace a custom class definition
    question: Can I rewrite a custom class entirely with a new definition?
  - id: updateClass
    intent: Patch attributes of a custom class
    question: Can I change just the title or description of a custom class without rewriting it?
  - id: removeClass
    intent: Delete a custom XDM class
    question: How do I delete a custom class I created?
  phrasing_ops: 6
  slug: adobe-suite-classes-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Classification Dataset API from Adobe Suite — 3 operation(s) for classification dataset.
  name: Adobe Suite Classification Dataset API
  phrasing_intents:
  - id: getOneDataset
    intent: Get a classification dataset
    question: How do I look up one Analytics classification dataset and its columns?
  - id: updateOneDataset
    intent: Update a classification dataset
    question: Can I rename a classification dataset or change its columns?
  - id: deleteDataset
    intent: Delete a classification dataset and its data
    question: How do I delete a classification dataset?
  - id: getCompatibilityMetrics
    intent: Get classification-compatible metrics for a report suite
    question: Which metrics in a report suite can be classified?
  - id: getDatasetTemplate
    intent: Download a classification dataset template
    question: How do I get an import template for a classification dataset?
  phrasing_ops: 5
  slug: adobe-suite-classification-dataset-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Classification Job API from Adobe Suite — 10 operation(s) for classification job.
  name: Adobe Suite Classification Job API
  phrasing_intents:
  - id: commitApiImportJob
    intent: Commit an import job for processing
    question: After uploading my classification file, how do I tell the import job to start processing?
  - id: createApiJobEntity
    intent: Create a file-based classification import job
    question: How do I set up an import job on a classification dataset before uploading a file?
  - id: createExportJob
    intent: Export a classification dataset
    question: How do I export the rows of a classification dataset to a file?
  - id: createJsonImportJob
    intent: Import classification data as inline JSON
    question: Can I send classification rows directly as JSON instead of uploading a file?
  - id: findJobsByDataset
    intent: List classification jobs for a dataset
    question: Which import and export jobs have run against a classification dataset?
  - id: getJobById
    intent: Check a classification job's status
    question: How do I check whether my classification import or export job finished?
  - id: retrieveArtifact
    intent: Download a classification export file
    question: How do I download the output of a finished classification export?
  - id: retrieveArtifactById
    intent: Download a named file from a classification export
    question: When an export produced several files, how do I download one of them by name?
  phrasing_ops: 10
  slug: adobe-suite-classification-job-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Classifier API from Adobe Suite — 7 operation(s) for classifier.
  name: Adobe Suite Classifier API
  phrasing_intents:
  - id: getClassifier
    intent: Get one classifier by ID
    question: How do I look up a single Workfront classifier by its ID?
  - id: editClassifier
    intent: Edit a single classifier
    question: What call updates one classifier's settings?
  - id: deleteClassifier
    intent: Delete a single classifier
    question: How do I delete one classifier?
  - id: getClassifiers
    intent: Get several classifiers by ID
    question: Can I fetch a list of classifiers by their IDs in one call?
  - id: editClassifiers
    intent: Bulk edit classifiers
    question: How do I update many classifiers in one request?
  - id: addClassifiers
    intent: Create a classifier
    question: How do I add a new classifier?
  - id: deleteClassifiers
    intent: Bulk delete classifiers
    question: Can I delete several classifiers in one call?
  - id: countClassifiers
    intent: Count classifiers
    question: How many classifiers match a filter?
  phrasing_ops: 12
  slug: adobe-suite-classifier-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Real-time events originating client-side, such as browsers or mobile devices
  name: Adobe Suite Client-to-server collection API
  phrasing_intents:
  - id: postV1Interact
    intent: Send one browser event and get a personalized response
    question: How do I send a single unauthenticated event to the Edge Network and get personalization back?
  - id: postV1Collect
    intent: Send a batch of client events without a response
    question: How can I push several events from different visitors in one unauthenticated call?
  - id: postV1IdentityAcquire
    intent: Acquire visitor identities for given namespaces
    question: How do I fetch an ECID or other identity for a visitor from the Edge Network?
  phrasing_ops: 3
  slug: adobe-suite-client-to-server-collection-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Cluster services provide access to groupings of identities as linked in the identity graph. These endpoints have been deprecated. Use Graph API to access groupings of identities as linked in the ident
  name: Adobe Suite Cluster API
  phrasing_intents:
  - id: listClusterMembers
    intent: List identities linked to one identity (deprecated)
    question: Which identities in other namespaces are linked to this one in the identity graph?
  - id: getListOfClusterMembers
    intent: List linked identities for many identities (deprecated)
    question: Can I fetch the linked identity clusters for a whole list of identities at once?
  phrasing_ops: 2
  slug: adobe-suite-cluster-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Combine multiple PDF Files into a single PDF File
  name: Adobe Suite Combine PDF API
  phrasing_intents:
  - id: pdfoperations.combinepdf
    intent: Combine several PDFs into one
    question: How do I merge several PDF files into a single document?
  - id: pdfoperations.combinepdf.jobstatus
    intent: Check the status of a combine PDF job
    question: Has my PDF merge job finished yet?
  phrasing_ops: 2
  slug: adobe-suite-combine-pdf-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Core Firefly API operations for generating and manipulating images and videos.
  name: Adobe Suite Common Operations API
  phrasing_intents:
  - id: generateImagesV3Async
    intent: Generate images from a text prompt
    question: How do I generate images from a text prompt with Firefly?
  - id: firefly_image_v5_generate_async_v4
    intent: Generate images with the Image5 model
    question: Can I generate images with the newer Firefly Image5 model?
  - id: generateSimilarImagesV3Async
    intent: Generate images similar to a reference
    question: Can I get variations that look like an image I already have?
  - id: expandImagesV3Async
    intent: Expand an image to a new size or ratio
    question: How do I extend an image beyond its borders to change its aspect ratio?
  - id: fillImagesV3Async
    intent: Fill a masked area of an image
    question: How do I replace part of an image using a mask and a prompt?
  - id: generateVideoV3
    intent: Generate a short video from a prompt
    question: Can Firefly make a five second video from a text prompt?
  - id: getCustomModels
    intent: List a user's custom models
    question: Which custom models do I have available for generation?
  - id: storageImageV2
    intent: Upload a source image or mask
    question: How do I upload an image to use in fill, expand or upscale?
  phrasing_ops: 8
  slug: adobe-suite-common-operations-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: A company represents the organization of a tags user, typically a business. These companies match 1:1 with IMS Organization IDs. API users will only have visibility into the companies to which they ha
  name: Adobe Suite Companies API
  phrasing_intents:
  - id: listCompanies
    intent: List tag companies
    question: Which companies can I access in Experience Platform Tags?
  - id: retrieveCompany
    intent: Get one tag company
    question: How do I look up the details of a single Tags company?
  - id: listProperties
    intent: List a company's tag properties
    question: What tag properties does my company have?
  - id: createProperty
    intent: Create a tag property
    question: How do I create a new web or mobile property in Tags?
  - id: listAppConfigurations
    intent: List a company's app configurations
    question: Which push messaging app configurations exist for my company?
  - id: createAppConfiguration
    intent: Create an app configuration
    question: How do I register a mobile app configuration for push messaging?
  phrasing_ops: 6
  slug: adobe-suite-companies-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Company API from Adobe Suite — 7 operation(s) for company.
  name: Adobe Suite Company API
  phrasing_intents:
  - id: getCompany
    intent: Get a single company record
    question: How do I look up one client or vendor company by its ID?
  - id: editCompany
    intent: Edit a single company
    question: How can I update the details of one company in Workfront?
  - id: deleteCompany
    intent: Delete a single company
    question: How do I delete a company we no longer work with?
  - id: getCompanys
    intent: Get several companies by ID at once
    question: Can I load multiple companies in one request using their IDs?
  - id: editCompanys
    intent: Edit many companies in one request
    question: Is there a way to bulk update several companies?
  - id: addCompanys
    intent: Create a company
    question: How do I add a new client company?
  - id: deleteCompanys
    intent: Delete several companies at once
    question: Can I bulk delete companies by listing their IDs?
  - id: replaceCompanys
    intent: Replace a company with another everywhere
    question: How do I merge a duplicate company into the one we want to keep?
  phrasing_ops: 12
  slug: adobe-suite-company-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Component Meta Data API from Adobe Suite — 10 operation(s) for component meta data.
  name: Adobe Suite Component Meta Data API
  phrasing_intents:
  - id: getByGlobalCompanyIdComponentmetadataShares
    intent: List components a user has shared out
    question: Which segments and projects have I shared with other people?
  - id: postByGlobalCompanyIdComponentmetadataShares
    intent: Share a segment or project with someone
    question: How do I share one segment with a single colleague without touching its other shares?
  - id: modifyShares
    intent: Overwrite who analytics components are shared with
    question: Can I set the full share list for segments or other components in one call?
  - id: searchComponentTags
    intent: Search shares for specific components
    question: Who has a given segment or calculated metric been shared with?
  - id: getShare
    intent: Retrieve a component share by ID
    question: What does one component share record contain?
  - id: deleteShare_1
    intent: Delete a component share
    question: Can I delete a share so it is removed from every component it was on?
  - id: findAllSharesToCurrentUser
    intent: List components shared with me
    question: Which segments have other people shared with me in Adobe Analytics?
  - id: searchComponentTags_2
    intent: Search tags applied to components
    question: Which tags are attached to a list of analytics components?
  phrasing_ops: 16
  slug: adobe-suite-component-meta-data-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'Object composite image generation: prompt-based composite, precise composite, and adaptive composite endpoints.'
  name: Adobe Suite Composite Operations API
  phrasing_intents:
  - id: generateObjectCompositeV3Async
    intent: Generate a scene around a product image
    question: Can Firefly place my product photo into a generated scene from a text prompt?
  - id: preciseComposite
    intent: Blend an object onto a background precisely
    question: How do I paste an object onto a background image while keeping its original look?
  - id: adaptiveComposite
    intent: Adaptively composite an object into a scene
    question: Can the object's lighting and colors be adjusted to match the background?
  phrasing_ops: 3
  slug: adobe-suite-composite-operations-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Composites API from Adobe Suite — 1 operation(s) for composites.
  name: Adobe Suite Composites API
  phrasing_intents:
  - id: v1/composites/compose
    intent: Generate a 3D product composite with a Firefly background
    question: How do I place a 3D product model in front of an AI-generated background?
  phrasing_ops: 1
  slug: adobe-suite-composites-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Compress a PDF File
  name: Adobe Suite Compress PDF API
  phrasing_intents:
  - id: pdfoperations.compresspdf
    intent: Compress a PDF to reduce its file size
    question: Can I shrink a large PDF before emailing it or sending it through a workflow?
  - id: pdfoperations.compresspdf.jobstatus
    intent: Check a compress PDF job's status
    question: Is my PDF compression job finished yet?
  phrasing_ops: 2
  slug: adobe-suite-compress-pdf-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Computed attributes enable a field value to be automatically computed based on other values, calculations, and expressions. Computed attributes functionality is in **beta** and is **not** available to
  name: Adobe Suite Computed attributes API
  phrasing_intents:
  - id: listComputedAttributes
    intent: List computed attributes
    question: Which computed profile attributes are defined in my sandbox?
  - id: createComputedAttribute
    intent: Create a computed attribute
    question: How do I define a new computed attribute on customer profiles?
  - id: retrieveComputedAttribute
    intent: Get one computed attribute
    question: How do I see the definition of a specific computed attribute?
  - id: deleteComputedAttribute
    intent: Delete a computed attribute
    question: How do I remove a computed attribute I no longer need?
  - id: updateComputedAttribute
    intent: Change a computed attribute's status
    question: How do I switch a computed attribute from draft to active?
  phrasing_ops: 5
  slug: adobe-suite-computed-attributes-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Configurations provide additional information that is necessary when setting up a dataset export.
  name: Adobe Suite Configurations API
  phrasing_intents:
  - id: getDatasets
    intent: List datasets eligible for export to a destination
    question: Which datasets can I export to a destination?
  phrasing_ops: 1
  slug: adobe-suite-configurations-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Connection specifications retain the connector properties of a given source. A connection spec can be divided into three distinct sections, authentication specifications (authSpec), source specificati
  name: Adobe Suite Connection specs API
  phrasing_intents:
  - id: listConnectionSpecs
    intent: List source connection specs
    question: Which source connectors are available in my Experience Platform organization?
  - id: createConnectionSpec
    intent: Create a connection spec for a source
    question: How do I define a new connection spec for a self-serve source connector?
  - id: retrieveConnectionSpec
    intent: Get a connection spec
    question: What auth and source settings does a specific connection spec define?
  - id: updateConnectionSpec
    intent: Update a connection spec
    question: How do I change an existing connection spec for my source?
  - id: exploreByConnectionSpecId
    intent: Explore objects of a connection spec
    question: What tables or files can I browse through a given connection spec?
  - id: configByConnectionSpecId
    intent: Get config options for a connection spec
    question: Which configuration options are available for a connection spec?
  phrasing_ops: 6
  slug: adobe-suite-connection-specs-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Base connections retain information between your source and Adobe Experience Platform. They include metadata, a partial view of the credentials used to authenticate a given source, and the unique base
  name: Adobe Suite Connections API
  phrasing_intents:
  - id: listConnections
    intent: List base connections in the organization
    question: How do I list all the source base connections in my Experience Platform org?
  - id: createConnection
    intent: Create a base connection to a source
    question: How do I create a new base connection for a data source?
  - id: retrieveConnection
    intent: Get a single base connection
    question: How do I look up the details of one base connection?
  - id: testConnection
    intent: Test a base connection's connectivity
    question: How do I check whether an existing source connection can still reach its source?
  - id: getByConnectionId
    intent: Explore the contents of a source connection
    question: How do I browse the tables or files available through a source connection?
  - id: performAction
    intent: Change the state of a base connection
    question: How do I trigger a state transition action on an existing connection?
  - id: deleteConnection
    intent: Delete a base connection
    question: How do I remove a source connection I no longer use?
  - id: patchConnection
    intent: Update a base connection's details
    question: How do I rename a connection or rotate its credentials?
  phrasing_ops: 11
  slug: adobe-suite-connections-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Certain privacy regulations require businesses to honor customer opt-out-of-sale requests. The Privacy Service API allows you to process these opt-out requests for Experience Cloud applications.
  name: Adobe Suite Consent API
  phrasing_intents:
  - id: processCCPASalesConsent
    intent: Process a customer opt-out of data sale
    question: How do I record a customer's CCPA request to opt out of the sale of their data?
  phrasing_ops: 1
  slug: adobe-suite-consent-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Content fragment API API from Adobe Suite — 5 operation(s) for content fragment api.
  name: Adobe Suite Content fragment API
  phrasing_intents:
  - id: createFragment
    intent: Create a content fragment
    question: How do I create a new reusable content fragment of a given type?
  - id: getFragments
    intent: List content fragments
    question: Which content fragments exist in my sandbox?
  - id: getFragment
    intent: Get a content fragment's details
    question: What's in a content fragment, including its current draft content?
  - id: putFragment
    intent: Replace a content fragment
    question: How do I overwrite a fragment's name, type and content in full?
  - id: patchFragment
    intent: Patch a fragment's name, description or folder
    question: Can I change just a fragment's name without resending its content?
  - id: publishFragment
    intent: Publish a content fragment
    question: How do I publish a fragment so campaigns and journeys can use it?
  - id: getLiveFragment
    intent: Get a fragment's last published content
    question: What content is live for a fragment from its last successful publication?
  - id: getLastPublicationStatus
    intent: Check a fragment's last publication status
    question: Did my last fragment publication succeed, fail or is it still in progress?
  phrasing_ops: 8
  slug: adobe-suite-content-fragment-api-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Content template API API from Adobe Suite — 2 operation(s) for content template api.
  name: Adobe Suite Content template API
  phrasing_intents:
  - id: createTemplate
    intent: Create a content template
    question: How do I create a reusable content template for email or code channels?
  - id: getTemplates
    intent: List content templates
    question: How do I list the content templates in my Journey Optimizer sandbox?
  - id: getTemplate
    intent: Get a content template by ID
    question: How do I fetch one content template's full details?
  - id: putTemplate
    intent: Replace a content template
    question: How do I fully overwrite an existing content template with new content?
  - id: deleteTemplate
    intent: Delete a content template
    question: How do I delete a content template I no longer use?
  - id: patchTemplate
    intent: Rename or move a content template
    question: Can I just rename a template or change its description without resending the content?
  phrasing_ops: 6
  slug: adobe-suite-content-template-api-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The ContentSets API from Adobe Suite — 8 operation(s) for contentsets.
  name: Adobe Suite Content Sets API
  phrasing_intents:
  - id: getContentSets
    intent: List a program's content sets
    question: Which content sets are defined for my Cloud Manager program?
  - id: createContentSet
    intent: Create a content set
    question: How do I define a new content set of asset paths to move between environments?
  - id: getContentSet
    intent: Get one content set
    question: Can I see which paths a specific content set includes?
  - id: updateContentSet
    intent: Update a content set
    question: Can I change the paths included in an existing content set?
  - id: deleteContentSet
    intent: Delete a content set
    question: How do I remove a content set I no longer need?
  - id: listContentFlows
    intent: List a program's content flows
    question: What content copy runs have happened in my program?
  - id: createContentFlow
    intent: Copy content between environments with a content set
    question: How do I copy content from production down to a stage or dev environment?
  - id: checkBackflowCompatibility
    intent: Check two environments are compatible for content copy
    question: Can I check whether content can flow back from one environment to another before running it?
  phrasing_ops: 12
  slug: adobe-suite-contentsets-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Contextsensitivehelp API from Adobe Suite — 5 operation(s) for contextsensitivehelp.
  name: Adobe Suite Contextsensitivehelp API
  phrasing_intents:
  - id: getContextSensitiveHelp
    intent: Get one context-sensitive help entry
    question: How do I look up a single Workfront context-sensitive help entry by ID?
  - id: getContextSensitiveHelps
    intent: Get several help entries by ID
    question: Can I fetch a batch of context-sensitive help entries by their IDs?
  - id: countContextSensitiveHelps
    intent: Count context-sensitive help entries
    question: How many context-sensitive help entries are there?
  - id: searchContextSensitiveHelps
    intent: Search context-sensitive help entries
    question: Which help entries match certain conditions?
  - id: reportContextSensitiveHelps
    intent: Run a report on context-sensitive help
    question: Can I produce an aggregated report of context-sensitive help entries?
  phrasing_ops: 5
  slug: adobe-suite-contextsensitivehelp-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Convert PDF documents to InDesign (INDD or IDML) format. The output is a ZIP file containing the converted documents and all associated assets.
  name: Adobe Suite Convert PDF to InDesign API
  phrasing_intents:
  - id: convertPDFToInDesign
    intent: Convert a PDF into an InDesign document
    question: How do I turn a PDF into an editable InDesign file?
  - id: getConvertPDFToInDesignJobStatus
    intent: Check a PDF to InDesign conversion job
    question: Is my PDF to InDesign conversion finished, and where do I download the ZIP?
  phrasing_ops: 2
  slug: adobe-suite-convert-pdf-to-indesign-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Create PDF document from Microsoft Office documents (Word, Excel and PowerPoint), Markdown and Image file formats.
  name: Adobe Suite Create PDF API
  phrasing_intents:
  - id: pdfoperations.createpdf
    intent: Convert a document or image to PDF
    question: How do I convert a Word, Excel or PowerPoint file into a PDF?
  - id: pdfoperations.jobstatus
    intent: Check the status of a create-PDF job
    question: How do I know when my PDF conversion job is finished?
  phrasing_ops: 2
  slug: adobe-suite-create-pdf-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: If a Platform customer does not need to provide any authentication credentials to connect to your destination, a credentials configuration can provide the required credentials instead. Note that you m
  name: Adobe Suite Credentials API
  phrasing_intents:
  - id: listCredential
    intent: List destination credential configurations
    question: Which credential configurations exist for my destinations?
  - id: createCredential
    intent: Create a destination credential configuration
    question: How do I store credentials a destination uses to deliver data?
  - id: retrieveCredential
    intent: Retrieve a destination credential configuration
    question: How do I look up one credential configuration?
  - id: updateCredential
    intent: Update a destination credential configuration
    question: Can I rotate the credentials stored in an existing configuration?
  - id: deleteCredential
    intent: Delete a destination credential configuration
    question: How do I remove a credential configuration a destination no longer needs?
  phrasing_ops: 5
  slug: adobe-suite-credentials-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Submit and execute custom scripts for InDesign automation. Supports comprehensive scripting capabilities for document manipulation and processing.
  name: Adobe Suite Custom Scripts API
  phrasing_intents:
  - id: submitCustomScript
    intent: Register a custom script bundle
    question: How do I register my own InDesign script to run in the cloud?
  - id: listCustomScripts
    intent: List registered InDesign custom scripts
    question: Which custom InDesign scripts have we registered?
  - id: executeCustomScript
    intent: Run a registered custom script
    question: How do I run a registered custom script against my InDesign files?
  - id: getCustomScriptDetails
    intent: Get details of one custom script
    question: What version and registration date does a particular custom script have?
  - id: deleteCustomScript
    intent: Delete a custom script and all its versions
    question: How do I unregister a custom script?
  - id: updateScriptAppVersion
    intent: Pin the InDesign version a script runs on
    question: Can I fix a custom script to a specific InDesign major or minor version?
  - id: listAppVersions
    intent: List available InDesign app versions
    question: Which InDesign versions can custom scripts run on?
  phrasing_ops: 7
  slug: adobe-suite-custom-scripts-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Customenum API from Adobe Suite — 31 operation(s) for customenum.
  name: Adobe Suite Customenum API
  phrasing_intents:
  - id: getCustomEnum
    intent: Get one custom enum value by ID
    question: How can I look up a single custom status or priority value by its ID?
  - id: editCustomEnum
    intent: Edit a single custom enum value
    question: How do I rename or recolor one existing custom status value in Workfront?
  - id: deleteCustomEnum
    intent: Delete one custom enum value
    question: Can I remove a single custom priority or status value I no longer use?
  - id: getCustomEnums
    intent: Fetch several custom enum values by ID
    question: Can I retrieve a batch of custom enum entries in one call by listing their IDs?
  - id: editCustomEnums
    intent: Bulk edit many custom enum values
    question: How do I update a whole batch of custom enum values in a single request?
  - id: addCustomEnums
    intent: Create a new custom enum value
    question: How do I add a new custom status, priority or condition value?
  - id: deleteCustomEnums
    intent: Bulk delete custom enum values
    question: Is there a way to delete many custom enum entries in one call?
  - id: countCustomEnums
    intent: Count custom enum values
    question: How many custom enum values are defined in my Workfront instance?
  phrasing_ops: 36
  slug: adobe-suite-customenum-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Customer Account Controller V 2
  name: Adobe Suite Customer Accounts API
  phrasing_intents:
  - id: createCustomerAccountUsingPOST
    intent: Create a reseller customer account (v2)
    question: How does a reseller create a customer account before placing an order, on the v2 API?
  - id: findAccountByCustomerIdUsingGET
    intent: Get customer account details (v2)
    question: How do I look up a customer account by ID on the v2 endpoint?
  - id: updateAccountUsingPATCH
    intent: Update a customer's address and contacts (v2)
    question: How do I change a customer's address or contact info with the v2 API?
  - id: createCustomerAccountUsingPOST_1
    intent: Create a reseller customer account (v3)
    question: How does a reseller create a customer account on the current v3 API?
  - id: findAccountByCustomerIdUsingGET_1
    intent: Get customer account details (v3)
    question: Where do I fetch a customer's account record through the current v3 customers endpoint?
  - id: updateAccountUsingPATCH_1
    intent: Update a customer's address and contacts (v3)
    question: Can the newer v3 API edit an end customer's mailing address and contacts?
  phrasing_ops: 6
  slug: adobe-suite-customer-accounts-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Customer API from Adobe Suite — 5 operation(s) for customer.
  name: Adobe Suite Customer API
  phrasing_intents:
  - id: customerGetPackagingOptionValue
    intent: Get the value of a packaging option
    question: What value is set for a given packaging option on our Workfront customer?
  - id: customerGoalsEnabled
    intent: Check whether Goals is enabled
    question: Is the Goals feature turned on for our customer?
  - id: customerIsPackagingOptionEnabled
    intent: Check whether a packaging option is enabled
    question: Is a particular packaging option switched on for us?
  - id: customerProductEnabled
    intent: Check whether a product is enabled
    question: Is a specific product enabled for our customer account?
  - id: customerUpdateLoginAsSettings
    intent: Update Log In As settings
    question: How do I change who can use Log In As for our customer?
  phrasing_ops: 5
  slug: adobe-suite-customer-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Customerpreferences API from Adobe Suite — 6 operation(s) for customerpreferences.
  name: Adobe Suite Customerpreferences API
  phrasing_intents:
  - id: getCustomerPreferences
    intent: Get a customer preference record by ID
    question: What value is stored in a specific Workfront customer preference?
  - id: getCustomerPreferencess
    intent: Get several customer preferences by ID
    question: Can I load multiple customer preference records at once?
  - id: addCustomerPreferencess
    intent: Create a customer preference
    question: How do I add a new customer-level preference setting?
  - id: searchCustomerPreferencess
    intent: Search customer preferences
    question: How do I find customer preferences by name?
  - id: customerPreferencesGetIsAutoUpgradeDisabled
    intent: Check whether auto-upgrade is disabled
    question: Is automatic upgrading turned off for our Workfront customer?
  - id: customerPreferencesGetTimesheetPreferences
    intent: Get timesheet preferences
    question: What timesheet preferences are configured for our organization?
  - id: customerPreferencesSetTimesheetPreferences
    intent: Set timesheet preferences
    question: How do I change our organization's timesheet settings?
  phrasing_ops: 7
  slug: adobe-suite-customerpreferences-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The customers API from Adobe Suite — 1 operation(s) for customers.
  name: Adobe Suite Customers API
  phrasing_intents:
  - id: PostV1Customers
    intent: Create a customer account
    question: How do I register a new customer account in Adobe Commerce?
  phrasing_ops: 1
  slug: adobe-suite-customers-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The customers/{customerId}/password/resetLinkToken/{resetPasswordLinkToken} API from Adobe Suite — 1 operation(s) for customers/{customerid}/password/resetlinktoken/{resetpasswordlinktoken}.
  name: Adobe Suite Customers/{customer Id}/password/reset Link Token/{reset Password Link Token} API
  phrasing_intents:
  - id: GetV1CustomersCustomerIdPasswordResetLinkTokenResetPasswordLinkToken
    intent: Validate a customer's password reset token
    question: How do I check whether a customer's password reset link is still valid?
  phrasing_ops: 1
  slug: adobe-suite-customers-customerid-password-resetlinktoken-resetpasswordlinktoken-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The customers/isEmailAvailable API from Adobe Suite — 1 operation(s) for customers/isemailavailable.
  name: Adobe Suite Customers/is Email Available API
  phrasing_intents:
  - id: PostV1CustomersIsEmailAvailable
    intent: Check if an email is free for signup
    question: Is an email address already tied to a customer account?
  phrasing_ops: 1
  slug: adobe-suite-customers-isemailavailable-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The customers/me/activate API from Adobe Suite — 1 operation(s) for customers/me/activate.
  name: Adobe Suite Customers/me/activate API
  phrasing_intents:
  - id: PutV1CustomersMeActivate
    intent: Activate my customer account
    question: How do I activate a store account using the key from my confirmation email?
  phrasing_ops: 1
  slug: adobe-suite-customers-me-activate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The customers/me/password API from Adobe Suite — 1 operation(s) for customers/me/password.
  name: Adobe Suite Customers/me/password API
  phrasing_intents:
  - id: PutV1CustomersMePassword
    intent: Change the signed-in customer's password
    question: How can a logged-in shopper change their own password?
  phrasing_ops: 1
  slug: adobe-suite-customers-me-password-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The customers/password API from Adobe Suite — 1 operation(s) for customers/password.
  name: Adobe Suite Customers/password API
  phrasing_intents:
  - id: PutV1CustomersPassword
    intent: Email a customer a password reset link
    question: How do I send a store customer a password reset email?
  phrasing_ops: 1
  slug: adobe-suite-customers-password-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The customers/resetPassword API from Adobe Suite — 1 operation(s) for customers/resetpassword.
  name: Adobe Suite Customers/reset Password API
  phrasing_intents:
  - id: PostV1CustomersResetPassword
    intent: Reset a customer's password with a token
    question: Can a shopper set a new password using the reset token from their email?
  phrasing_ops: 1
  slug: adobe-suite-customers-resetpassword-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Customlabel API from Adobe Suite — 10 operation(s) for customlabel.
  name: Adobe Suite Customlabel API
  phrasing_intents:
  - id: getCustomLabel
    intent: Get one custom label
    question: How do I look up a single custom label in Workfront?
  - id: deleteCustomLabel
    intent: Delete a custom label
    question: How do I delete a custom label record by ID?
  - id: getCustomLabels
    intent: Fetch several custom labels by ID
    question: Can I load a batch of custom labels by their IDs?
  - id: addCustomLabels
    intent: Create a custom label
    question: How do I create a new custom label?
  - id: deleteCustomLabels
    intent: Bulk delete custom labels
    question: Can I delete several custom labels at once?
  - id: countCustomLabels
    intent: Count custom labels
    question: How many custom labels exist that match a filter?
  - id: searchCustomLabels
    intent: Search custom labels
    question: What's the way to search custom label records by field?
  - id: reportCustomLabels
    intent: Run a report on custom labels
    question: Can I produce an aggregate report over custom labels?
  phrasing_ops: 13
  slug: adobe-suite-customlabel-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Customquarter API from Adobe Suite — 5 operation(s) for customquarter.
  name: Adobe Suite Customquarter API
  phrasing_intents:
  - id: getCustomQuarter
    intent: Get one custom fiscal quarter
    question: What are the start and end dates of a specific custom quarter?
  - id: editCustomQuarter
    intent: Update a custom quarter
    question: How do I change the dates of one custom quarter?
  - id: deleteCustomQuarter
    intent: Delete a custom quarter
    question: How do I remove one custom quarter definition?
  - id: getCustomQuarters
    intent: Get several custom quarters by ID
    question: Can I fetch multiple custom quarters in one call?
  - id: editCustomQuarters
    intent: Update many custom quarters at once
    question: Can I bulk edit several custom quarters together?
  - id: addCustomQuarters
    intent: Create a custom quarter
    question: How do I define a custom fiscal quarter for reporting?
  - id: deleteCustomQuarters
    intent: Delete several custom quarters
    question: Can I delete multiple custom quarters in one call?
  - id: countCustomQuarters
    intent: Count custom quarters
    question: How many custom quarters are defined?
  phrasing_ops: 10
  slug: adobe-suite-customquarter-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Configure data access and egress for Experience Platform.
  name: Adobe Suite Data Access API
  phrasing_intents:
  - id: listDatasetFiles
    intent: List a batch's dataset files
    question: Which dataset files were written by a specific ingestion batch?
  - id: retrieveFailedBatch
    intent: List a failed batch's files
    question: How do I see the files from a batch that failed ingestion?
  - id: retrieveBatchMeta
    intent: Get a batch's meta and row error files
    question: Where can I find the row errors for an ingestion batch?
  phrasing_ops: 3
  slug: adobe-suite-data-access-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'A data element functions as a variable which points to an important piece of data within your application. Data elements are used within rules and extension configurations. When the rule is triggered '
  name: Adobe Suite Data elements API
  phrasing_intents:
  - id: listPropertyDataElements
    intent: List a tag property's data elements
    question: Which data elements are defined on my tags property?
  - id: createDataElement
    intent: Create a data element
    question: How do I add a new data element to a tags property?
  - id: retrieveDataElement
    intent: Look up a data element
    question: What are the settings of one data element?
  - id: updateDataElement
    intent: Update or revise a data element
    question: Can I change a data element's settings or name?
  - id: listDataElementNotes
    intent: List notes on a data element
    question: What notes have been left on a data element?
  - id: createNote
    intent: Add a note to a data element
    question: How do I leave a note on a data element for my team?
  phrasing_ops: 6
  slug: adobe-suite-data-elements-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Create document variations from CSV data and InDesign templates. Supports UTF-16BE encoding for CSV files, which is necessary for languages or characters requiring multi-byte representation. For plain
  name: Adobe Suite Data Merge API
  phrasing_intents:
  - id: dataMerge
    intent: Merge CSV data into an InDesign template
    question: How do I generate personalized PDFs by merging a CSV into an InDesign template?
  - id: dataMergeTags
    intent: Get the data merge tags in a document
    question: Which data merge fields does my InDesign template expect?
  phrasing_ops: 2
  slug: adobe-suite-data-merge-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Data merge, create rendition, and shared job status for asynchronous Illustrator API jobs.
  name: Adobe Suite Data Merge & Create Rendition API
  phrasing_intents:
  - id: dataMerge
    intent: Merge CSV data into an Illustrator template
    question: How do I generate one Illustrator file per row of a CSV spreadsheet?
  - id: createRendition
    intent: Convert an Illustrator file to another format
    question: Can I convert an .ai document into a web- or print-ready format like PDF or PNG?
  - id: facadeJobStatus
    intent: Check an Illustrator job's status
    question: Has my Illustrator data merge or rendition job finished?
  phrasing_ops: 3
  slug: adobe-suite-data-merge-create-rendition-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Data types are used as reference field types in classes or schemas to define complex types. Data types may define multiple sub-fields providing a consistent multi-field structure.
  name: Adobe Suite Data types API
  phrasing_intents:
  - id: listDataTypes
    intent: List XDM data types
    question: Which XDM data types are available in the Schema Registry?
  - id: retrieveDataType
    intent: Retrieve an XDM data type
    question: How do I look up the fields of one XDM data type?
  - id: createDataType
    intent: Create a custom XDM data type
    question: How do I define a new reusable data type for my schemas?
  - id: replaceDatatype
    intent: Replace a custom data type entirely
    question: Can I rewrite a whole custom data type in one request?
  - id: updateDataType
    intent: Patch attributes of a custom data type
    question: Can I change just one field of a custom data type with JSON Patch?
  - id: deleteDatatype
    intent: Delete a custom data type
    question: How do I remove a custom data type I no longer need?
  phrasing_ops: 6
  slug: adobe-suite-data-types-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Dataflow runs represent an instance of a dataflow execution, which exports data to your destination. A dataflow run is specific to a dataflow and a segment for which the data export occurred. Furtherm
  name: Adobe Suite Dataflow runs API
  phrasing_intents:
  - id: getFlowRuns
    intent: List destination dataflow runs
    question: How do I see the runs of my destination dataflows?
  phrasing_ops: 1
  slug: adobe-suite-dataflow-runs-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Destination dataflows represent the data transfer between a source connection (Experience Platform) and a target connection (the destination you set up). This also includes information regarding the d
  name: Adobe Suite Dataflows API
  phrasing_intents:
  - id: getFlows
    intent: List destination dataflows
    question: Which destination dataflows are set up for my organization?
  - id: postFlow
    intent: Create a destination dataflow
    question: How do I set up a dataflow to activate data to a destination?
  - id: getFlowById
    intent: Get a destination dataflow
    question: What's the configuration of a specific destination dataflow?
  - id: patchFlowById
    intent: Update a destination dataflow
    question: Can I change the configuration of an existing destination dataflow?
  - id: deleteFlowById
    intent: Delete a destination dataflow
    question: How do I stop and remove a destination dataflow?
  phrasing_ops: 5
  slug: adobe-suite-dataflows-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The datarepair API from Adobe Suite — 4 operation(s) for datarepair.
  name: Adobe Suite Datarepair API
  phrasing_intents:
  - id: get_auth_v1__reportSuiteId__auth_get
    intent: Check data repair authorization for a report suite
    question: Am I authorized to run a data repair on a given report suite?
  - id: get_jobs_v1__reportSuiteId__job_get
    intent: List data repair jobs for a report suite
    question: What data repair jobs have been run on my report suite?
  - id: create_job_v1__reportSuiteId__job_post
    intent: Start a data repair job
    question: How do I repair or delete variable data in Analytics for a date range?
  - id: get_job_v1__reportSuiteId__job__jobId__get
    intent: Check the status of one data repair job
    question: Has my data repair job finished yet?
  - id: get_server_call_estimate_v1__reportSuiteId__serverCallEstimate_get
    intent: Estimate server calls for a data repair
    question: How many server calls would a data repair over a date range cost?
  phrasing_ops: 5
  slug: adobe-suite-datarepair-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Use the `/ttl` endpoint to schedule expiration dates for datasets in Adobe Experience Platform.
  name: Adobe Suite Dataset Expiration (TTL) API
  phrasing_intents:
  - id: listTtl
    intent: List dataset expiration schedules
    question: Which datasets in my org are scheduled to expire?
  - id: createTtl
    intent: Schedule a dataset to expire
    question: How do I set a dataset to be deleted automatically on a certain date?
  - id: getTtl
    intent: Get a dataset expiration's details
    question: How do I check the expiration configured for one dataset?
  - id: updateTtl
    intent: Change a pending dataset expiration
    question: How do I push back the date a dataset is set to expire?
  - id: deleteTtl
    intent: Cancel a pending dataset expiration
    question: How do I stop a dataset from being deleted on its scheduled expiry?
  phrasing_ops: 5
  slug: adobe-suite-dataset-expiration-ttl-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The DatasetEnablement API from Adobe Suite — 3 operation(s) for datasetenablement.
  name: Adobe Suite Dataset Enablement API
  phrasing_intents:
  - id: validateOrchestratedCampaignExtensionOnDataset
    intent: Check a dataset for orchestrated campaigns
    question: Can a dataset be used with Orchestrated Campaigns?
  - id: enableOrchestratedCampaignExtensionOnDataset
    intent: Enable orchestrated campaigns on a dataset
    question: How do I turn on the Orchestrated Campaign extension for a dataset?
  - id: getDatasetExtensionEnablementJobStatus
    intent: Check a dataset enablement job
    question: Has my orchestrated campaign dataset enablement finished?
  phrasing_ops: 3
  slug: adobe-suite-datasetenablement-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Datasets are the building blocks for data transformation and tracking in Catalog Service.
  name: Adobe Suite Datasets API
  phrasing_intents:
  - id: listDatasets
    intent: List datasets in a sandbox
    question: How do I see all the datasets in my Experience Platform sandbox?
  - id: createDataset
    intent: Create a dataset
    question: How do I create a new dataset tied to an XDM schema?
  - id: retrieveDataset
    intent: Look up a dataset
    question: How do I get the details of one dataset by its ID?
  - id: putDataset
    intent: Replace a dataset's definition
    question: Can I overwrite a dataset's full definition with a new one?
  - id: deleteDataset
    intent: Delete a dataset
    question: What's the way to delete a dataset I no longer need?
  - id: patchDataset
    intent: Change specific fields of a dataset
    question: Can I change just a dataset's tags without resending the whole thing?
  - id: retrieveDatasetCredentials
    intent: Get a dataset's access credentials
    question: How do I get the storage credentials for reading or writing a dataset's files?
  - id: retrieveDatasetLabels
    intent: Get a dataset's data usage labels
    question: Which data usage labels are applied to a dataset?
  phrasing_ops: 10
  slug: adobe-suite-datasets-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Date Ranges API from Adobe Suite — 2 operation(s) for date ranges.
  name: Adobe Suite Date Ranges API
  phrasing_intents:
  - id: getDateRange_1
    intent: Get one saved date range
    question: How do I read the definition of one saved Adobe Analytics date range?
  - id: putByGlobalCompanyIdDaterangesById
    intent: Update a saved date range
    question: Can I rename or redefine a date range I already saved in Analytics?
  - id: deleteByGlobalCompanyIdDaterangesById
    intent: Delete a saved date range
    question: How do I remove a reusable date range I no longer need?
  - id: getDateRanges_1
    intent: List a user's saved date ranges
    question: Which reusable date ranges have I saved in Analytics?
  - id: postByGlobalCompanyIdDateranges
    intent: Create a reusable date range
    question: How do I save a new custom date range to reuse across Analytics projects?
  phrasing_ops: 5
  slug: adobe-suite-date-ranges-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Schema descriptors are tenant-level metadata used to provide interpretive details on how data based on certain schemas may relate or interact with one another.
  name: Adobe Suite Descriptors API
  phrasing_intents:
  - id: listDescriptors
    intent: List schema descriptors
    question: Which descriptors describe relationships and identities across our XDM schemas?
  - id: retrieveDescriptor
    intent: Get one schema descriptor
    question: How do I view a single descriptor by its @id?
  - id: createDescriptor
    intent: Create a schema descriptor
    question: How do I mark a schema field as a primary identity with a descriptor?
  - id: updateDescriptor
    intent: Rewrite an existing schema descriptor
    question: Can I change the field an existing descriptor points to?
  - id: deleteDescriptor
    intent: Delete a schema descriptor
    question: How do I remove a descriptor I added to a schema?
  phrasing_ops: 5
  slug: adobe-suite-descriptors-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Destination configurations contain essential metadata for individual destinations, including their name, category, description, and more. The settings in this configuration also determine how Experien
  name: Adobe Suite Destination configurations API
  phrasing_intents:
  - id: listDestinations
    intent: List destination configurations
    question: How do I see every destination configuration in my IMS organization?
  - id: createDestination
    intent: Create a destination configuration
    question: How do I set up a new destination with Adobe Destination SDK?
  - id: retrieveDestination
    intent: Get a destination configuration
    question: How do I view the full settings of one destination configuration?
  - id: updateDestination
    intent: Update a destination configuration
    question: How do I change an existing destination's configuration?
  - id: deleteDestination
    intent: Delete a destination configuration
    question: How do I remove a destination configuration I no longer use?
  phrasing_ops: 5
  slug: adobe-suite-destination-configurations-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: After you have configured and tested your destination, you can use the destination publishing endpoint to submit it to Adobe for review and publishing. Read more in the [destination publishing API tut
  name: Adobe Suite Destination publishing API
  phrasing_intents:
  - id: listPublishDestinationRequest
    intent: List destination publish requests
    question: Which destinations has my organization submitted for publishing?
  - id: createPublishDestinationRequest
    intent: Submit a destination for publishing
    question: How do I submit a destination configuration I authored for publishing?
  - id: retrievePublishDestinationRequest
    intent: Check a destination's publishing status
    question: What's the publishing status of a destination I submitted?
  phrasing_ops: 3
  slug: adobe-suite-destination-publishing-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Destination server configurations contain information about the server receiving the messages (the server on your side). Template configurations allow you to configure how to format the exported messa
  name: Adobe Suite Destination servers and templates API
  phrasing_intents:
  - id: listDestinationServer
    intent: List destination server configurations
    question: Which destination server configurations exist for my organization?
  - id: createDestinationServer
    intent: Create a destination server configuration
    question: How do I set up a new server and template for a custom destination?
  - id: retrieveDestinationServer
    intent: Get one destination server configuration
    question: How do I view the details of a specific destination server config?
  - id: updateDestinationServer
    intent: Update a destination server configuration
    question: Can I change the endpoint or template of an existing destination server?
  - id: deleteDestinationServer
    intent: Delete a destination server configuration
    question: How do I remove a destination server configuration I no longer use?
  phrasing_ops: 5
  slug: adobe-suite-destination-servers-and-templates-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Destination Authoring API provides several tools to test file-based and streaming destinations. Read the overview documents for testing [file-based](https://experienceleague.adobe.com/en/docs/expe
  name: Adobe Suite Destination testing API
  slug: adobe-suite-destination-testing-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Dimensions API from Adobe Suite — 2 operation(s) for dimensions.
  name: Adobe Suite Dimensions API
  phrasing_intents:
  - id: dimensions_getDimensions
    intent: List dimensions for a report suite
    question: Which dimensions are available in my Adobe Analytics report suite?
  - id: dimensions_getDimension
    intent: Get one Analytics dimension by ID
    question: How do I look up details of a single dimension like variables/evar1?
  phrasing_ops: 2
  slug: adobe-suite-dimensions-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The directory/countries API from Adobe Suite — 1 operation(s) for directory/countries.
  name: Adobe Suite Directory/countries API
  phrasing_intents:
  - id: GetV1DirectoryCountries
    intent: List the store's countries and regions
    question: Which countries and regions does my Commerce store support?
  phrasing_ops: 1
  slug: adobe-suite-directory-countries-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The directory/countries/{countryId} API from Adobe Suite — 1 operation(s) for directory/countries/{countryid}.
  name: Adobe Suite Directory/countries/{country Id} API
  phrasing_intents:
  - id: GetV1DirectoryCountriesCountryId
    intent: Get a country and its regions for the store
    question: Which regions or states does the store list for a given country?
  phrasing_ops: 1
  slug: adobe-suite-directory-countries-countryid-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The directory/currency API from Adobe Suite — 1 operation(s) for directory/currency.
  name: Adobe Suite Directory/currency API
  phrasing_intents:
  - id: GetV1DirectoryCurrency
    intent: Get the store's currency settings
    question: What base and display currencies does the store use?
  phrasing_ops: 1
  slug: adobe-suite-directory-currency-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Docmetadatalink API from Adobe Suite — 5 operation(s) for docmetadatalink.
  name: Adobe Suite Docmetadatalink API
  phrasing_intents:
  - id: getDocMetadataLink
    intent: Look up one document metadata link
    question: How do I view a single document metadata link record?
  - id: deleteDocMetadataLink
    intent: Delete a document metadata link
    question: How do I remove a metadata link from a document?
  - id: getDocMetadataLinks
    intent: Fetch several document metadata links
    question: Can I load multiple doc metadata links by their IDs?
  - id: addDocMetadataLinks
    intent: Create a document metadata link
    question: How do I link metadata to a document?
  - id: deleteDocMetadataLinks
    intent: Delete many document metadata links
    question: Can I bulk delete doc metadata links?
  - id: countDocMetadataLinks
    intent: Count document metadata links
    question: How many document metadata links exist?
  - id: searchDocMetadataLinks
    intent: Search document metadata links
    question: Which doc metadata links match certain criteria?
  - id: reportDocMetadataLinks
    intent: Run a document metadata link report
    question: Can I get an aggregated report of doc metadata links?
  phrasing_ops: 8
  slug: adobe-suite-docmetadatalink-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Docmetadatalinkgroup API from Adobe Suite — 7 operation(s) for docmetadatalinkgroup.
  name: Adobe Suite Docmetadatalinkgroup API
  phrasing_intents:
  - id: getDocMetadataLinkGroup
    intent: Get a document metadata link group
    question: How can I look up one document metadata link group by its ID?
  - id: deleteDocMetadataLinkGroup
    intent: Delete a document metadata link group
    question: Can I remove one document metadata link group I no longer need?
  - id: getDocMetadataLinkGroups
    intent: Fetch several metadata link groups by ID
    question: Can I retrieve multiple document metadata link groups in one request by their IDs?
  - id: addDocMetadataLinkGroups
    intent: Create a document metadata link group
    question: How do I create a new group that links metadata to a document?
  - id: deleteDocMetadataLinkGroups
    intent: Bulk delete document metadata link groups
    question: Is there a way to delete many document metadata link groups at once?
  - id: countDocMetadataLinkGroups
    intent: Count document metadata link groups
    question: How many document metadata link groups exist?
  - id: searchDocMetadataLinkGroups
    intent: Search document metadata link groups
    question: What's the way to search document metadata link groups by attributes?
  - id: reportDocMetadataLinkGroups
    intent: Report on document metadata link groups
    question: Can I get an aggregated report over document metadata link groups?
  phrasing_ops: 10
  slug: adobe-suite-docmetadatalinkgroup-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Document API from Adobe Suite — 32 operation(s) for document.
  name: Adobe Suite Document API
  phrasing_intents:
  - id: getDocument
    intent: Get one Workfront document
    question: How do I look up a single document by its ID in Workfront?
  - id: editDocument
    intent: Edit a document's details
    question: How do I change the name or description of one existing document?
  - id: deleteDocument
    intent: Delete a document
    question: What's the call to permanently delete one document from Workfront?
  - id: getDocuments
    intent: Get several documents by ID at once
    question: Can I fetch a batch of documents in one call if I have their IDs?
  - id: editDocuments
    intent: Edit many documents in one request
    question: Can I update a whole batch of documents in a single request?
  - id: addDocuments
    intent: Create a document
    question: How do I add a new document record in Workfront?
  - id: deleteDocuments
    intent: Delete several documents at once
    question: Can I delete a batch of documents in one call?
  - id: countDocuments
    intent: Count documents matching a filter
    question: How many documents do we have in Workfront?
  phrasing_ops: 37
  slug: adobe-suite-document-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Merge Word based templates with input JSON data to create Word and PDF documents
  name: Adobe Suite Document Generation API
  phrasing_intents:
  - id: pdfoperations.documentgeneration
    intent: Generate documents from a Word template
    question: How do I merge JSON data into a Word template to produce a PDF?
  - id: pdfoperations.documentgeneration.jobstatus
    intent: Check a document generation job
    question: Is my document generation job finished yet?
  phrasing_ops: 2
  slug: adobe-suite-document-generation-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Retrieve information from INDD / IDML documents including layers, links and fonts.
  name: Adobe Suite Document Info API
  phrasing_intents:
  - id: getDocumentInfo
    intent: Extract information from an InDesign document
    question: How do I find out which fonts, links and pages an InDesign file uses?
  - id: getDocumentInfoJobStatus
    intent: Check a document info job and get results
    question: How do I know when my InDesign document analysis is done?
  phrasing_ops: 2
  slug: adobe-suite-document-info-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Documentapproval API from Adobe Suite — 5 operation(s) for documentapproval.
  name: Adobe Suite Documentapproval API
  phrasing_intents:
  - id: getDocumentApproval
    intent: Get one document approval
    question: How do I look up a single document approval in Workfront by its ID?
  - id: editDocumentApproval
    intent: Edit a document approval
    question: Can I change the status or details of one document approval?
  - id: deleteDocumentApproval
    intent: Delete a document approval
    question: How do I remove one approval request from a document?
  - id: getDocumentApprovals
    intent: Get several document approvals by ID
    question: Can I fetch a batch of document approvals if I have their IDs?
  - id: editDocumentApprovals
    intent: Edit many document approvals at once
    question: Can I update a whole set of document approvals in one request?
  - id: addDocumentApprovals
    intent: Request approval on a document
    question: How do I send a document to someone for approval?
  - id: deleteDocumentApprovals
    intent: Delete several document approvals
    question: Can I delete a batch of document approvals in one call?
  - id: countDocumentApprovals
    intent: Count document approvals
    question: How many document approvals are there?
  phrasing_ops: 10
  slug: adobe-suite-documentapproval-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Documentfolder API from Adobe Suite — 18 operation(s) for documentfolder.
  name: Adobe Suite Documentfolder API
  phrasing_intents:
  - id: getDocumentFolder
    intent: Get one document folder
    question: How do I look up a single document folder by its ID in Workfront?
  - id: editDocumentFolder
    intent: Edit a document folder
    question: Can I rename or change the details of one existing document folder?
  - id: deleteDocumentFolder
    intent: Delete a document folder
    question: How do I remove one document folder?
  - id: getDocumentFolders
    intent: Get several document folders by ID
    question: Can I fetch a batch of document folders at once when I already have their IDs?
  - id: editDocumentFolders
    intent: Edit many document folders in one request
    question: Can I update a whole set of document folders in a single request?
  - id: addDocumentFolders
    intent: Create a document folder
    question: How do I create a new document folder in Workfront?
  - id: deleteDocumentFolders
    intent: Delete several document folders at once
    question: Can I delete a batch of document folders in one call?
  - id: countDocumentFolders
    intent: Count document folders
    question: How many document folders do we have?
  phrasing_ops: 23
  slug: adobe-suite-documentfolder-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Documentversion API from Adobe Suite — 8 operation(s) for documentversion.
  name: Adobe Suite Documentversion API
  phrasing_intents:
  - id: getDocumentVersion
    intent: Get one document version
    question: How do I look up a single document version in Workfront?
  - id: getDocumentVersions
    intent: Fetch several document versions by ID
    question: Can I load multiple document versions at once by ID?
  - id: addDocumentVersions
    intent: Create a document version
    question: How do I add a new version to a document?
  - id: countDocumentVersions
    intent: Count document versions
    question: How many document versions match a filter?
  - id: searchDocumentVersions
    intent: Search document versions
    question: What's the way to search document versions by field?
  - id: reportDocumentVersions
    intent: Run a report on document versions
    question: Can I produce an aggregate report over document versions?
  - id: documentVersionGetDocumentReviewerDecision
    intent: Get the reviewer decision on a document version
    question: What did the reviewer decide on this document version?
  - id: documentVersionGetProofingTokens
    intent: Get proofing tokens for a document version
    question: How do I obtain proofing tokens to open a document version in proofing?
  phrasing_ops: 9
  slug: adobe-suite-documentversion-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Domain API from Adobe Suite — 4 operation(s) for domain.
  name: Adobe Suite Domain API
  phrasing_intents:
  - id: getDomain
    intent: List custom domains in a Cloud Manager program
    question: Which custom domains are registered in my Cloud Manager program?
  - id: createDomain
    intent: Add a custom domain to a program
    question: How do I add a custom domain name to a Cloud Manager program?
  - id: getApiProgramByProgramIdDomainByDomainId
    intent: Get one domain by ID
    question: What's the verification status of a specific domain by its ID?
  - id: modifyDomain
    intent: Update a domain's label
    question: Can I change the label on a domain I already added?
  - id: deleteDomain
    intent: Remove a domain from a program
    question: How do I remove a custom domain from my Cloud Manager program?
  - id: domainValidationToken
    intent: Run a domain ownership validation check
    question: After adding my TXT record, how do I tell Cloud Manager to verify the domain?
  - id: postApiProgramByProgramIdDomainByDomainIdValidation
    intent: Create a domain ownership validation token
    question: Where do I get the token to prove I own a custom domain?
  phrasing_ops: 7
  slug: adobe-suite-domain-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Domain Mappings - CDN Configurations API from Adobe Suite — 5 operation(s) for domain mappings - cdn configurations.
  name: Adobe Suite Domain Mappings - CDN Configurations API
  phrasing_intents:
  - id: getDomainMappingById
    intent: Get a domain mapping
    question: How is a particular custom domain mapped to its CDN origin in my Cloud Manager program?
  - id: updateDomainMapping
    intent: Update a domain mapping's certificate or tier
    question: How do I swap the SSL certificate on an existing domain mapping?
  - id: deleteDomainMapping
    intent: Delete a domain mapping
    question: How do I remove a custom domain's CDN configuration from a program?
  - id: validateHelixDomain
    intent: Verify DNS changes for a domain mapping
    question: How can I check whether the DNS records for my custom domain are set up correctly?
  - id: getAllDomainMappingsByProgramId
    intent: List domain mappings in a program
    question: Which custom domains are mapped to CDN origins across my whole program?
  - id: createDomainMapping
    intent: Create a domain mapping (CDN configuration)
    question: How do I point a custom domain at an environment or site through the CDN?
  - id: getAllDomainMappingsByProgramIdAndEnvironmentId
    intent: List domain mappings for an environment
    question: Which custom domains route to a specific environment?
  - id: getAllDomainMappingsByProgramIdAndSiteId
    intent: List domain mappings for an EDS site
    question: Which custom domains are mapped to a particular Edge Delivery Services site?
  phrasing_ops: 8
  slug: adobe-suite-domain-mappings-cdn-configurations-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Download API from Adobe Suite — 1 operation(s) for download.
  name: Adobe Suite Download API
  phrasing_intents:
  - id: downloaded
    intent: Report offline media consumption
    question: How do I track what a user watched while they were offline?
  phrasing_ops: 1
  slug: adobe-suite-download-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'Endpoints for Dynamic Graphics Render (DGR): template describe, presets, render, job status, cancel a render job, and list render jobs. The Cancel (`PUT /v1/cancel/{jobId}`) and List Render Jobs (`GET'
  name: Adobe Suite Dynamic Graphics Render API
  phrasing_intents:
  - id: template-describe
    intent: List the editable controls in a video template
    question: Which text, fonts, images and audio can I change in a Motion Graphics template?
  - id: get-presets
    intent: List video rendering presets
    question: What social-first encoding presets can I render video outputs with?
  - id: template-render
    intent: Render video variations from a template
    question: How do I render personalized video versions from a MOGRT with different text or images?
  - id: cancel-render-job
    intent: Cancel a video render job
    question: Can I stop a template render that is still in progress?
  - id: list-render-jobs
    intent: List my template render jobs
    question: Which of my video render jobs are still running?
  phrasing_ops: 5
  slug: adobe-suite-dynamic-graphics-render-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The EDS Sites API from Adobe Suite — 3 operation(s) for eds sites.
  name: Adobe Suite EDS Sites API
  phrasing_intents:
  - id: retrieveSite
    intent: Get an Edge Delivery Services site
    question: What configuration does a specific Edge Delivery Services site in my program have?
  - id: updateSite
    intent: Update an Edge Delivery Services site
    question: How do I change the settings of an existing EDS site?
  - id: deleteSite
    intent: Delete an Edge Delivery Services site
    question: How do I remove an EDS site from my program?
  - id: validateSite
    intent: Validate an Edge Delivery Services site
    question: How can I check that an EDS site is set up correctly?
  - id: getProgramSites
    intent: List Edge Delivery Services sites in a program
    question: Which EDS sites belong to my Cloud Manager program?
  - id: createSite
    intent: Create an Edge Delivery Services site
    question: How do I register a new Edge Delivery Services site in a program?
  phrasing_ops: 6
  slug: adobe-suite-eds-sites-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Unless explicitly indicated otherwise, only enabled policies participate in evaluation. The Policy Service API maintains a list of enabled core policies for your organization that you can manage using
  name: Adobe Suite Enabled core policies API
  phrasing_intents:
  - id: listEnabledCorePolicies
    intent: List enabled core data governance policies
    question: Which core data usage policies are currently enabled for our org?
  - id: createOrUpdateEnabledCorePolicies
    intent: Set which core policies are enabled
    question: What's the way to turn on a specific set of core data usage policies?
  phrasing_ops: 2
  slug: adobe-suite-enabled-core-policies-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Endorsement API from Adobe Suite — 7 operation(s) for endorsement.
  name: Adobe Suite Endorsement API
  phrasing_intents:
  - id: getEndorsement
    intent: Get an endorsement by ID
    question: Who gave a particular endorsement in Workfront and what did it say?
  - id: deleteEndorsement
    intent: Delete an endorsement
    question: How do I remove an endorsement I gave by mistake?
  - id: getEndorsements
    intent: Get several endorsements by their IDs
    question: Can I load several endorsements in one request?
  - id: addEndorsements
    intent: Endorse a colleague
    question: How do I give a teammate an endorsement for their work?
  - id: deleteEndorsements
    intent: Delete several endorsements at once
    question: Can I remove a batch of endorsements together?
  - id: countEndorsements
    intent: Count endorsements
    question: How many endorsements have been given in total?
  - id: searchEndorsements
    intent: Search endorsements
    question: How do I find endorsements given to a particular user?
  - id: reportEndorsements
    intent: Run a report over endorsements
    question: Can I get endorsement counts grouped by recipient?
  phrasing_ops: 10
  slug: adobe-suite-endorsement-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Endorsementshare API from Adobe Suite — 5 operation(s) for endorsementshare.
  name: Adobe Suite Endorsementshare API
  phrasing_intents:
  - id: getEndorsementShare
    intent: Get an endorsement share
    question: Who was an endorsement shared with in Workfront?
  - id: deleteEndorsementShare
    intent: Delete an endorsement share
    question: How do I remove a single endorsement share?
  - id: getEndorsementShares
    intent: Get several endorsement shares by ID
    question: Can I load multiple endorsement shares at once by ID?
  - id: addEndorsementShares
    intent: Share an endorsement
    question: How do I share an endorsement with someone in Workfront?
  - id: deleteEndorsementShares
    intent: Bulk delete endorsement shares
    question: Can I remove many endorsement shares in one call?
  - id: countEndorsementShares
    intent: Count endorsement shares
    question: How many endorsement shares exist?
  - id: searchEndorsementShares
    intent: Search endorsement shares
    question: Which endorsement shares match certain conditions?
  - id: reportEndorsementShares
    intent: Run a report on endorsement shares
    question: Can I get a grouped report of endorsement shares?
  phrasing_ops: 8
  slug: adobe-suite-endorsementshare-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Engines act as an umbrella entity holding all machine learning instances. This is tied to a Docker image, Java archive, or EGG file which contains machine learning logic to train and score a Model.
  name: Adobe Suite Engines API
  phrasing_intents:
  - id: retrieveEngines
    intent: List Sensei ML engines
    question: Which machine learning engines have been onboarded in my organization?
  - id: createEngine
    intent: Create a Sensei ML engine
    question: How do I onboard a new ML engine with a JAR or EGG artifact?
  - id: retrieveDockerRegistryInfo
    intent: Get Docker registry details for engines
    question: What Docker registry should I push my engine images to?
  - id: retrieveEngine
    intent: Get a Sensei ML engine
    question: What algorithm and language does a particular engine use?
  - id: updateEngine
    intent: Update a Sensei ML engine
    question: How do I rename an existing engine or change its description?
  - id: deleteEngine
    intent: Delete a Sensei ML engine
    question: How do I remove an engine I no longer need?
  phrasing_ops: 6
  slug: adobe-suite-engines-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: An entity is an Experience Data Model (XDM) object whose attributes and related time-series events have been merged from various sources to form an individual profile. For more information on using th
  name: Adobe Suite Entities API
  phrasing_intents:
  - id: retrieveEntity
    intent: Look up a profile or entity by identity
    question: How do I pull a customer's real-time profile using an identity like an email?
  - id: retrieveMultipleEntities
    intent: Look up many profiles by identity at once
    question: Can I retrieve profiles for a whole list of identities in one request?
  - id: deleteEntity
    intent: Delete an entity from the profile store
    question: How do I delete a single profile entity by its identity?
  phrasing_ops: 3
  slug: adobe-suite-entities-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Environment Advanced Networking Configuration API from Adobe Suite — 1 operation(s) for environment advanced networking configuration.
  name: Adobe Suite Environment Advanced Networking Configuration API
  phrasing_intents:
  - id: getEnvironmentAdvancedNetworkingConfigurationList
    intent: Get an environment's advanced networking setup
    question: Is advanced networking enabled on my AEM Cloud Manager environment, and how is it configured?
  - id: enableEnvironmentAdvancedNetworkingConfiguration
    intent: Enable advanced networking on an environment
    question: How do I turn on advanced networking for one environment?
  - id: disableEnvironmentAdvancedNetworkingConfiguration
    intent: Disable advanced networking on an environment
    question: How do I switch off advanced networking for an environment?
  phrasing_ops: 3
  slug: adobe-suite-environment-advanced-networking-configuration-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Environment Restore From Backup API from Adobe Suite — 5 operation(s) for environment restore from backup.
  name: Adobe Suite Environment Restore From Backup API
  phrasing_intents:
  - id: getRestorePoints
    intent: List available backup restore points
    question: Which backups can I restore my Cloud Service environment from?
  - id: getRestoreExecution
    intent: Get one restore execution
    question: How do I check the progress of a specific environment restore?
  - id: getRestoreExecutionLogs
    intent: Get the logs of a restore execution
    question: Where can I read the logs from an environment restore?
  - id: getRestoreExecutions
    intent: List restore executions for an environment
    question: What restores have been run on this environment so far?
  - id: restoreExecution
    intent: Restore an environment from backup
    question: How do I roll my Cloud Service environment back to an earlier backup?
  phrasing_ops: 5
  slug: adobe-suite-environment-restore-from-backup-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: An environment indicates the specific host where a build can be deployed, and whether the build should be deployed as a set of files or compressed in an archive format. In the Reactor API, environment
  name: Adobe Suite Environments API
  phrasing_intents:
  - id: listEnvironments
    intent: List a tag property's environments
    question: Which environments are set up on my Adobe tags property?
  - id: createEnvironment
    intent: Create an environment on a tag property
    question: How do I add a development, staging or production environment to a tags property?
  - id: retrieveEnvironment
    intent: Look up a tag environment
    question: What are the settings of one tags environment?
  - id: deleteEnvironment
    intent: Delete a tag environment
    question: How do I remove an environment from a tags property?
  - id: updateEnvironment
    intent: Update a tag environment
    question: Can I rename a tags environment or change its host?
  - id: listBuilds
    intent: List an environment's builds
    question: Which library builds have been published to a tag environment?
  - id: listEnvironmentSecrets
    intent: List an environment's secrets
    question: What secrets are stored on a tag environment?
  - id: retrieveEnvironmentHost
    intent: Get the host an environment deploys to
    question: Which host does a tag environment deliver its builds to?
  phrasing_ops: 17
  slug: adobe-suite-environments-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Error API from Adobe Suite — 1 operation(s) for error.
  name: Adobe Suite Error API
  phrasing_intents:
  - id: error
    intent: Report a media playback error event
    question: What should a video player send to Media Edge when playback hits an error?
  phrasing_ops: 1
  slug: adobe-suite-error-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Estimates provide statistical information on a segment definition, such as the projected audience size and confidence interval. More information about using this set of endpoints can be found in the [
  name: Adobe Suite Estimates API
  phrasing_intents:
  - id: retrieveEstimate
    intent: Get the results of an audience estimate job
    question: How big is the audience my estimate job predicted?
  phrasing_ops: 1
  slug: adobe-suite-estimates-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Events API from Adobe Suite — 6 operation(s) for events.
  name: Adobe Suite Events API
  phrasing_intents:
  - id: filePost
    intent: Upload a bulk data insertion file to Analytics
    question: How do I send a gzipped CSV of hits to Adobe Analytics for processing?
  - id: fileValidatePut
    intent: Validate a bulk data insertion file
    question: Can I check my bulk insertion CSV format without it being processed?
  - id: eventsUsingGET
    intent: List all current issues and maintenances
    question: What issues and maintenance windows are affecting Adobe services right now?
  - id: incidentsUsingGET
    intent: List ongoing service issues
    question: Are there any ongoing incidents impacting a product I use?
  - id: maintenanceUsingGET
    intent: List ongoing maintenances
    question: What maintenance is in progress right now for a given service?
  - id: scheduledUsingGET
    intent: List upcoming scheduled maintenances
    question: When is the next planned maintenance for a product I depend on?
  phrasing_ops: 6
  slug: adobe-suite-events-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Ewsfilehandle API from Adobe Suite — 1 operation(s) for ewsfilehandle.
  name: Adobe Suite Ewsfilehandle API
  phrasing_intents:
  - id: getEwsFileHandleUpload
    intent: Get a file handle for an upload
    question: How do I get a file handle for a file I'm uploading to Workfront?
  phrasing_ops: 1
  slug: adobe-suite-ewsfilehandle-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The execution API from Adobe Suite — 5 operation(s) for execution.
  name: Adobe Suite Execution API
  phrasing_intents:
  - id: postIMUnitaryMessageExecution
    intent: Send an API-triggered message to specific recipients
    question: How do I trigger an API campaign message to a handful of named recipients in Journey Optimizer?
  - id: postIMAudienceMessageExecution
    intent: Trigger or schedule a message to an audience
    question: How do I send a campaign message to a whole Experience Platform audience?
  - id: getBatchExecutionStatusByExecutionId
    intent: Check an audience message execution by execution ID
    question: How do I check whether my audience campaign send finished, using its execution ID?
  - id: getBatchExecutionStatusByScheduleId
    intent: Check an audience message execution by schedule ID
    question: How do I see the status of a scheduled audience campaign using its schedule ID?
  - id: deleteScheduledExecution
    intent: Cancel a scheduled campaign execution
    question: How do I cancel a scheduled campaign send before it goes out?
  - id: postIMUnitaryHAMessageExecution
    intent: Send a high-throughput API-triggered message
    question: Is there a high-throughput option for triggering unitary campaign messages at volume?
  phrasing_ops: 6
  slug: adobe-suite-execution-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Execution Artifacts API from Adobe Suite — 2 operation(s) for execution artifacts.
  name: Adobe Suite Execution Artifacts API
  phrasing_intents:
  - id: listStepArtifacts
    intent: List artifacts produced by a pipeline step
    question: How do I see the artifacts a Cloud Manager pipeline step produced?
  - id: getStepArtifact
    intent: Get one artifact from a pipeline step
    question: Can I fetch a single artifact from a pipeline execution step?
  phrasing_ops: 2
  slug: adobe-suite-execution-artifacts-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Expense API from Adobe Suite — 7 operation(s) for expense.
  name: Adobe Suite Expense API
  phrasing_intents:
  - id: getExpense
    intent: Look up one expense
    question: How do I view a single Workfront expense by its ID?
  - id: editExpense
    intent: Update one expense
    question: Can I change the amount or type recorded on an existing expense?
  - id: deleteExpense
    intent: Delete one expense
    question: How do I remove an expense that was logged by mistake?
  - id: getExpenses
    intent: Fetch several expenses by ID
    question: Can I retrieve a batch of expenses when I know their IDs?
  - id: editExpenses
    intent: Update many expenses at once
    question: How do I bulk edit several expenses in one request?
  - id: addExpenses
    intent: Log a new expense
    question: How do I record a new expense against a project or task?
  - id: deleteExpenses
    intent: Delete many expenses at once
    question: Can I bulk delete a list of expenses by ID?
  - id: countExpenses
    intent: Count expenses
    question: How many expenses match a given filter?
  phrasing_ops: 12
  slug: adobe-suite-expense-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Expensetype API from Adobe Suite — 6 operation(s) for expensetype.
  name: Adobe Suite Expensetype API
  phrasing_intents:
  - id: getExpenseType
    intent: Get a single expense type
    question: How do I look up one Workfront expense type by ID?
  - id: editExpenseType
    intent: Edit one expense type
    question: Can I change the name or rate of a single expense type?
  - id: deleteExpenseType
    intent: Delete one expense type
    question: How do I delete a single expense type?
  - id: getExpenseTypes
    intent: Get several expense types by ID
    question: Can I fetch several expense types at once by ID?
  - id: editExpenseTypes
    intent: Edit many expense types at once
    question: Can I update a batch of expense types in one request?
  - id: addExpenseTypes
    intent: Create an expense type
    question: How do I add a new expense type like travel or hardware?
  - id: deleteExpenseTypes
    intent: Delete many expense types at once
    question: Can I delete a list of expense types in one call?
  - id: replaceExpenseTypes
    intent: Replace expense types with another one
    question: Can I retire an expense type and move its expenses to a different type?
  phrasing_ops: 11
  slug: adobe-suite-expensetype-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: A data scientist conducts multiple experiments to arrive at a high-performing Model while training. This can include changing datasets, features, learning parameters, and hardware.
  name: Adobe Suite Experiments API
  phrasing_intents:
  - id: retrieveExperiments
    intent: List machine learning experiments
    question: Which Sensei ML experiments exist for my MLInstances?
  - id: createExperiment
    intent: Create a machine learning experiment
    question: How do I create a new experiment for an MLInstance?
  - id: deleteExperiments
    intent: Delete all experiments for an MLInstance
    question: Can I wipe out every experiment belonging to one MLInstance in one call?
  - id: retrieveExperiment
    intent: Get a machine learning experiment
    question: What MLInstance and workflow is a particular experiment tied to?
  - id: updateExperiment
    intent: Update a machine learning experiment
    question: How do I rename an existing experiment?
  - id: deleteExperiment
    intent: Delete a machine learning experiment
    question: How do I delete just one experiment?
  - id: listExperimentRuns
    intent: List runs of an experiment
    question: Which training or scoring runs have been executed for an experiment?
  - id: createExperimentRun
    intent: Start an experiment run
    question: How do I kick off a training run for an experiment?
  phrasing_ops: 10
  slug: adobe-suite-experiments-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Schema Registry API allows you to transfer and share XDM resources between sandboxes and IMS Organizations. For any schema, field group, or data type, you can generate an export payload containing
  name: Adobe Suite Export/Import API
  phrasing_intents:
  - id: retrieveExportPayload
    intent: Export a schema resource for transfer
    question: How do I copy a schema or field group to a different sandbox?
  - id: importResource
    intent: Import a resource from an export payload
    question: How do I bring an exported schema into another sandbox?
  phrasing_ops: 2
  slug: adobe-suite-export-import-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'Export jobs are asynchronous processes that are used to persist audience members to datasets. More information about using this set of endpoints can be found in the [export jobs endpoint guide](https:'
  name: Adobe Suite Export jobs API
  phrasing_intents:
  - id: listExportJobs
    intent: List profile export jobs
    question: What audience export jobs have run in my sandbox?
  - id: createExportJob
    intent: Export profiles to a dataset
    question: How do I export the profiles in a segment to a dataset?
  - id: retrieveExportJob
    intent: Get one export job's status
    question: Is my profile export job finished yet?
  - id: cancelExportJob
    intent: Cancel or delete an export job
    question: Can I stop a profile export that is still running?
  phrasing_ops: 4
  slug: adobe-suite-export-jobs-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Convert a PDF File to a non-PDF File
  name: Adobe Suite Export PDF API
  phrasing_intents:
  - id: pdfoperations.exportpdf
    intent: Convert a PDF to Word, Excel, PowerPoint or RTF
    question: How do I convert a PDF into an editable Word document?
  - id: pdfoperations.exportpdf.jobstatus
    intent: Check an export PDF job's status
    question: Is my PDF export job finished yet?
  phrasing_ops: 2
  slug: adobe-suite-export-pdf-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Export PDF Form Data API will retrieve the data from a PDF form and return it as a JSON file.
  name: Adobe Suite Export PDF Form Data API
  phrasing_intents:
  - id: pdfoperations.getformdata
    intent: Extract filled-in form data from a PDF
    question: How do I pull the values someone typed into a PDF form as JSON?
  - id: pdfoperations.getformdata.jobstatus
    intent: Check a PDF form data export job
    question: Is my PDF form data export done yet?
  phrasing_ops: 2
  slug: adobe-suite-export-pdf-form-data-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: An extension package usage authorization is an authorization granted by the package owner to other companies for the private use of the extension package versions.
  name: Adobe Suite Extension package usage authorization API
  phrasing_intents:
  - id: retrieveExtensionPackageUsageAuthorizationForPackage
    intent: List usage authorizations for an extension package
    question: Which organizations are authorized to use one of my private tag extension packages?
  - id: createExtensionPackageUsageAuthorization
    intent: Authorize an organization to use an extension package
    question: How do I share a private extension package with another organization?
  - id: retrieveExtensionPackageUsageAuthorization
    intent: List all extension package usage authorizations
    question: Which extension package usage authorizations involve my organization?
  - id: deletePackageUsageAuthorization
    intent: Revoke an extension package usage authorization
    question: How do I revoke another org's access to my extension package?
  - id: updateExtensionPackageUsageAuthorization
    intent: Approve or change a usage authorization
    question: Can I accept or reject an extension package authorization that was offered to my org?
  - id: retrieveDataExtensionPackageUsageAuthorization
    intent: Get the package behind a usage authorization
    question: Which extension package does a given usage authorization refer to?
  phrasing_ops: 6
  slug: adobe-suite-extension-package-usage-authorization-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: An extension package represents a grouping of individual capabilities that can be made available to a tags user. Most commonly, these capabilities come in the form of rule components (events, conditio
  name: Adobe Suite Extension packages API
  phrasing_intents:
  - id: listExtensionPackages
    intent: List tag extension packages
    question: How do I browse the extension packages available for Adobe Experience Platform tags?
  - id: createExtensionPackage
    intent: Upload a new extension package
    question: How do I publish a new tag extension by uploading its package file?
  - id: retrieveExtensionPackage
    intent: Get one extension package
    question: How do I look up the details of a single extension package?
  - id: updateExtensionPackage
    intent: Replace a development extension package's archive
    question: Can I upload a new archive to an extension package that is still in development?
  - id: privateReleaseExtensionPackage
    intent: Privately release or discontinue an extension package
    question: How do I release my extension package privately to every property in my company?
  - id: retrieveExtensionPackageVersion
    intent: List versions of an extension package
    question: What versions exist for a given extension package?
  phrasing_ops: 6
  slug: adobe-suite-extension-packages-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: An extension represents the installed instance of an extension package. An extension makes the features defined by an extension package available to a property. These features are leveraged when creat
  name: Adobe Suite Extensions API
  phrasing_intents:
  - id: listExtensions
    intent: List the extensions installed on a property
    question: Which extensions are installed on my Adobe tags property?
  - id: createExtension
    intent: Install an extension on a property
    question: How do I install an extension package onto a tags property?
  - id: retrieveExtension
    intent: Get an extension's details
    question: How do I look up one installed extension by ID?
  - id: deleteExtension
    intent: Uninstall an extension
    question: How do I remove an extension from a tags property for good?
  - id: reviseExtension
    intent: Create a new revision of an extension
    question: How do I save a new revision of an extension with updated settings?
  - id: retrievePackageForExtension
    intent: Get the package behind an extension
    question: Which extension package version is this installed extension based on?
  - id: listExtensionLibraries
    intent: List libraries that use an extension
    question: Which libraries include this extension?
  - id: retrieveExtensionProperty
    intent: Find which property an extension is on
    question: What property is this extension installed on?
  phrasing_ops: 12
  slug: adobe-suite-extensions-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Externalauthtoken API from Adobe Suite — 5 operation(s) for externalauthtoken.
  name: Adobe Suite Externalauthtoken API
  phrasing_intents:
  - id: getExternalAuthToken
    intent: Look up one external auth token
    question: How do I inspect a single stored external authentication token in Workfront?
  - id: editExternalAuthToken
    intent: Update one external auth token
    question: Can I update the details stored on an existing external auth token?
  - id: deleteExternalAuthToken
    intent: Delete one external auth token
    question: How do I remove a stored external authentication token?
  - id: getExternalAuthTokens
    intent: Fetch several external auth tokens by ID
    question: Can I retrieve multiple external auth tokens in one call by ID?
  - id: editExternalAuthTokens
    intent: Update many external auth tokens at once
    question: Can I bulk edit several external auth tokens in one request?
  - id: addExternalAuthTokens
    intent: Store a new external auth token
    question: How do I save a new external authentication token for an integration?
  - id: deleteExternalAuthTokens
    intent: Delete many external auth tokens at once
    question: Can I bulk delete external auth tokens by listing their IDs?
  - id: countExternalAuthTokens
    intent: Count external auth tokens
    question: How many external auth tokens match a given filter?
  phrasing_ops: 10
  slug: adobe-suite-externalauthtoken-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Externaldocument API from Adobe Suite — 10 operation(s) for externaldocument.
  name: Adobe Suite Externaldocument API
  phrasing_intents:
  - id: searchExternalDocuments
    intent: Search external document records with filters
    question: How do I query Workfront's external document records using filter conditions?
  - id: externalDocumentBrowseListWithLinkAction
    intent: Browse a document provider with a link action
    question: Can I browse a connected document provider's files while preparing a link action?
  - id: externalDocumentGetDocumentDownloadUrl
    intent: Get a download URL for an external document
    question: How do I get a download link for a file stored in a connected document provider?
  - id: externalDocumentGetRootFolderID
    intent: Get the root folder ID from a document provider
    question: How do I find the root folder of a connected external document provider?
  - id: externalDocumentGetRootFolderIDFromDB
    intent: Get a provider's stored root folder ID
    question: Can I read the root folder ID Workfront already has saved for a document provider?
  - id: externalDocumentLinkExternalDocumentObjects
    intent: Link external documents to a Workfront object
    question: How do I attach files from a connected storage provider to a project or task?
  - id: externalDocumentSetLinkedFolderMetadata
    intent: Set metadata for a linked external folder
    question: How do I tie an external storage folder to a project as its linked folder?
  - id: getExternalDocumentBrowseList
    intent: Browse files in an external document provider
    question: How do I list the files and folders in a connected storage provider?
  phrasing_ops: 10
  slug: adobe-suite-externaldocument-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Externalproviderconfig API from Adobe Suite — 5 operation(s) for externalproviderconfig.
  name: Adobe Suite Externalproviderconfig API
  phrasing_intents:
  - id: getExternalProviderConfig
    intent: Get a single external provider config
    question: How do I look up one Workfront external provider configuration by ID?
  - id: editExternalProviderConfig
    intent: Edit one external provider config
    question: Can I change the settings of a single external provider configuration?
  - id: deleteExternalProviderConfig
    intent: Delete one external provider config
    question: How do I remove a single external provider configuration?
  - id: getExternalProviderConfigs
    intent: Get several external provider configs by ID
    question: Can I fetch several external provider configurations at once?
  - id: editExternalProviderConfigs
    intent: Edit many external provider configs at once
    question: Can I update a batch of external provider configurations together?
  - id: addExternalProviderConfigs
    intent: Create an external provider config
    question: How do I add a new external provider configuration?
  - id: deleteExternalProviderConfigs
    intent: Delete many external provider configs at once
    question: Can I delete a list of external provider configurations in one call?
  - id: countExternalProviderConfigs
    intent: Count external provider configs
    question: How many external provider configurations are set up?
  phrasing_ops: 10
  slug: adobe-suite-externalproviderconfig-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Externalsection API from Adobe Suite — 9 operation(s) for externalsection.
  name: Adobe Suite Externalsection API
  phrasing_intents:
  - id: getExternalSection
    intent: Get one external section by ID
    question: How do I look up a single external page section in Workfront?
  - id: editExternalSection
    intent: Edit an external section
    question: How do I change the settings of an existing external page section?
  - id: deleteExternalSection
    intent: Delete an external section
    question: How do I remove one embedded external page section?
  - id: getExternalSections
    intent: Fetch several external sections by ID
    question: Can I retrieve a batch of external sections using a list of IDs?
  - id: editExternalSections
    intent: Bulk edit external sections
    question: Can I update many external page sections in a single bulk call?
  - id: addExternalSections
    intent: Create or copy an external section
    question: How do I add a new external page section that embeds another site?
  - id: deleteExternalSections
    intent: Bulk delete external sections
    question: Can I delete several external page sections at once?
  - id: countExternalSections
    intent: Count external sections
    question: How many external page sections are configured?
  phrasing_ops: 14
  slug: adobe-suite-externalsection-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Extract content from PDF documents and output it in a structured JSON format, along with tables and figures
  name: Adobe Suite Extract PDF API
  phrasing_intents:
  - id: pdfoperations.extractpdf
    intent: Extract text, tables and figures from a PDF
    question: Can I pull the structured text and headings out of a PDF as JSON?
  - id: pdfoperations.extractpdf.jobstatus
    intent: Check a PDF extraction job
    question: Has my PDF extract job finished?
  phrasing_ops: 2
  slug: adobe-suite-extract-pdf-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Favorite API from Adobe Suite — 5 operation(s) for favorite.
  name: Adobe Suite Favorite API
  phrasing_intents:
  - id: getFavorite
    intent: Look up one favorite
    question: How do I see a single item I marked as a favorite in Workfront?
  - id: deleteFavorite
    intent: Remove one favorite
    question: Can I unfavorite a single item?
  - id: getFavorites
    intent: Fetch several favorites by ID
    question: Can I retrieve multiple favorites in one call by their IDs?
  - id: addFavorites
    intent: Add an item to favorites
    question: How do I mark a project or task as a favorite?
  - id: deleteFavorites
    intent: Remove many favorites at once
    question: Can I bulk remove favorites by listing their IDs?
  - id: countFavorites
    intent: Count favorites
    question: How many favorites match a given filter?
  - id: searchFavorites
    intent: Search favorites
    question: What's the way to find favorites by object type or owner?
  - id: reportFavorites
    intent: Run an aggregate report on favorites
    question: Can I get grouped totals of favorites as a report?
  phrasing_ops: 8
  slug: adobe-suite-favorite-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: A field group is a reusable component that defines one or more fields to implement certain functions within a schema based on a compatible class.
  name: Adobe Suite Field groups API
  phrasing_intents:
  - id: listFieldGroups
    intent: List XDM field groups in a container
    question: Which schema field groups are available in the global or tenant container?
  - id: retrieveFieldGroup
    intent: Get one XDM field group
    question: How do I look at the fields defined in a specific field group?
  - id: createFieldGroup
    intent: Create a custom field group
    question: How do I add my own custom field group to extend an XDM schema class?
  - id: updateFieldGroup
    intent: Replace a custom field group entirely
    question: Can I rewrite a whole custom field group in one request?
  - id: patchFieldGroup
    intent: Patch attributes of a custom field group
    question: Can I add or replace just one attribute of a field group with JSON Patch?
  - id: removeFieldGroup
    intent: Delete a custom field group
    question: How do I delete a custom field group I created?
  phrasing_ops: 6
  slug: adobe-suite-field-groups-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Retrieve headers containing metadata for a file specified by ID.
  name: Adobe Suite Files API
  phrasing_intents:
  - id: retrieveDatasetFile
    intent: Download a dataset file or list its chunks
    question: How do I download a dataset file from Experience Platform?
  - id: retrieveDatasetFileHeaders
    intent: Get a dataset file's headers only
    question: Can I check a dataset file's size and type without downloading it?
  phrasing_ops: 2
  slug: adobe-suite-files-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'Flow specs retain information that define a flow. They include information on how a flow can be scheduled, whether a flow supports options like partial ingestion and error diagnostics, as well as the '
  name: Adobe Suite Flow specs API
  phrasing_intents:
  - id: listFlowSpecs
    intent: List flow specifications
    question: What flow specs are available for building dataflows?
  - id: createFlowSpec
    intent: Create a flow spec
    question: How do I register a new flow spec for a connector?
  - id: retrieveFlowSpec
    intent: Get a flow spec
    question: How do I read the definition of one flow spec?
  - id: updateFlowSpec
    intent: Update a flow spec
    question: How do I change an existing flow spec's schedule or run settings?
  - id: searchFlowSpecs
    intent: Search flow specs by criteria
    question: Can I query flow specs with a filter string and group the results?
  phrasing_ops: 5
  slug: adobe-suite-flow-specs-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Flows (or dataflows) represent the transfer of data between source and target. They include details on the transformations applied to your data, the current status of your flow, and details on the mos
  name: Adobe Suite Flows API
  phrasing_intents:
  - id: listFlows
    intent: List dataflows in the organization
    question: How do I see all the dataflows set up in my Experience Platform organization?
  - id: createFlow
    intent: Create a dataflow
    question: What do I need to create a dataflow connecting a source to a target?
  - id: retrieveFlow
    intent: Get a dataflow's details
    question: How can I check the configuration of one specific dataflow?
  - id: deleteByFlow
    intent: Delete a dataflow
    question: Can I delete a dataflow I no longer need?
  - id: patchFlow
    intent: Update a dataflow
    question: How do I change settings on an existing dataflow?
  - id: getFlowsByFilters
    intent: Search dataflows by filter criteria
    question: Can I search flows with a query string instead of listing them all?
  - id: postStateTransition
    intent: Change a dataflow's state
    question: How do I enable, disable or otherwise change the state of a dataflow?
  phrasing_ops: 7
  slug: adobe-suite-flows-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Folders are a capability that let you better organize your business objects for easier navigability and categorization.
  name: Adobe Suite Folders API
  phrasing_intents:
  - id: createFolder
    intent: Create a folder
    question: How do I create a folder to organize my datasets or segments?
  - id: retrieveFolder
    intent: Get a folder's details
    question: What are the details of a specific folder?
  - id: updateFolder
    intent: Update a folder
    question: How can I rename or move an existing folder?
  - id: deleteFolder
    intent: Delete a folder
    question: How do I delete a folder I no longer need?
  - id: getSubfolders
    intent: List a folder's subfolders
    question: Which subfolders sit inside a given folder?
  - id: validateFolder
    intent: Check if a folder can hold objects
    question: Is this folder eligible to have objects placed in it?
  phrasing_ops: 6
  slug: adobe-suite-folders-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'Mapping-set functions allow you to transform your data between source and destination schemas. You can use these functions to validate your expressions and get a list of all the available mapping-set '
  name: Adobe Suite Functions API
  phrasing_intents:
  - id: validateExpression
    intent: Validate a Data Prep mapping expression
    question: Will my Data Prep mapping expression compile before I use it in a mapping set?
  - id: listMappingSetFunctions
    intent: List Data Prep mapping functions
    question: Which functions can I use in Data Prep mapping expressions?
  - id: listMappingSetOperators
    intent: List Data Prep mapping operators
    question: Which operators are allowed in Data Prep mapping expressions?
  phrasing_ops: 3
  slug: adobe-suite-functions-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'Creates an access token using client id and client secret. Click <a href="https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/IMS/">here</a> to refer '
  name: Adobe Suite Generate Token API
  phrasing_intents:
  - id: authentication.generatetoken
    intent: Get an access token for PDF Services
    question: How do I get an access token to call Adobe PDF Services?
  phrasing_ops: 1
  slug: adobe-suite-generate-token-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The giftregistry/mine/estimate-shipping-methods API from Adobe Suite — 1 operation(s) for giftregistry/mine/estimate-shipping-methods.
  name: Adobe Suite Giftregistry/mine/estimate Shipping Methods API
  phrasing_intents:
  - id: PostV1GiftregistryMineEstimateshippingmethods
    intent: Estimate shipping for my gift registry
    question: What shipping methods and costs apply to items in my gift registry?
  phrasing_ops: 1
  slug: adobe-suite-giftregistry-mine-estimate-shipping-methods-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Graph API provides access to groupings of identities as linked in the identity graph.
  name: Adobe Suite Graph API
  phrasing_intents:
  - id: getGraphs
    intent: List identities linked in the identity graph
    question: Given an email or ECID, which other identities are linked to it in the identity graph?
  phrasing_ops: 1
  slug: adobe-suite-graph-api-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Group API from Adobe Suite — 27 operation(s) for group.
  name: Adobe Suite Group API
  phrasing_intents:
  - id: getGroup
    intent: Look up one Workfront group
    question: What details can I see for a single Workfront group?
  - id: editGroup
    intent: Edit a single group
    question: How do I change the name or settings of one group?
  - id: deleteGroup
    intent: Delete a single group
    question: Can I delete one group that is no longer used?
  - id: getGroups
    intent: Fetch several groups by ID at once
    question: Can I retrieve a batch of groups in one call when I already know their IDs?
  - id: editGroups
    intent: Edit many groups in one request
    question: Can I bulk update multiple groups in a single request?
  - id: addGroups
    intent: Create or copy a group
    question: How do I create a new group in Workfront?
  - id: deleteGroups
    intent: Delete several groups at once
    question: Can I remove a batch of groups in one call?
  - id: replaceGroups
    intent: Replace groups with another group
    question: Can I swap out old groups so their references point to a different group?
  phrasing_ops: 32
  slug: adobe-suite-group-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts API from Adobe Suite — 1 operation(s) for guest-carts.
  name: Adobe Suite Guest Carts API
  phrasing_intents:
  - id: PostV1Guestcarts
    intent: Create an empty guest cart
    question: What's the way to start a shopping cart for a shopper who isn't logged in?
  phrasing_ops: 1
  slug: adobe-suite-guest-carts-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId} API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}.
  name: Adobe Suite Guest Carts/{cart Id} API
  phrasing_intents:
  - id: GetV1GuestcartsCartId
    intent: Get a guest shopper's cart
    question: How can a guest user see what's in their cart?
  - id: PutV1GuestcartsCartId
    intent: Assign a guest cart to a customer
    question: How do I attach a guest's cart to a customer account after they sign in?
  phrasing_ops: 2
  slug: adobe-suite-guest-carts-cartid-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/billing-address API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/billing-address.
  name: Adobe Suite Guest Carts/{cart Id}/billing Address API
  phrasing_intents:
  - id: GetV1GuestcartsCartIdBillingaddress
    intent: Get a guest cart's billing address
    question: What billing address is on a guest shopper's cart?
  - id: PostV1GuestcartsCartIdBillingaddress
    intent: Set a guest cart's billing address
    question: How do I assign a billing address to a guest checkout cart?
  phrasing_ops: 2
  slug: adobe-suite-guest-carts-cartid-billing-address-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/collect-totals API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/collect-totals.
  name: Adobe Suite Guest Carts/{cart Id}/collect Totals API
  phrasing_intents:
  - id: PutV1GuestcartsCartIdCollecttotals
    intent: Set guest cart methods and collect totals
    question: How do I set the payment and shipping method on a guest cart and get its totals?
  phrasing_ops: 1
  slug: adobe-suite-guest-carts-cartid-collect-totals-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/coupons API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/coupons.
  name: Adobe Suite Guest Carts/{cart Id}/coupons API
  phrasing_intents:
  - id: GetV1GuestcartsCartIdCoupons
    intent: See the coupon applied to a guest cart
    question: Which coupon code is applied to a guest shopper's cart?
  - id: DeleteV1GuestcartsCartIdCoupons
    intent: Remove the coupon from a guest cart
    question: How do I take a coupon off a guest shopper's cart?
  phrasing_ops: 2
  slug: adobe-suite-guest-carts-cartid-coupons-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/coupons/{couponCode} API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/coupons/{couponcode}.
  name: Adobe Suite Guest Carts/{cart Id}/coupons/{coupon Code} API
  phrasing_intents:
  - id: PutV1GuestcartsCartIdCouponsCouponCode
    intent: Apply a coupon to a guest cart
    question: How do I apply a coupon code to a guest shopper's cart?
  phrasing_ops: 1
  slug: adobe-suite-guest-carts-cartid-coupons-couponcode-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/estimate-shipping-methods API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/estimate-shipping-methods.
  name: Adobe Suite Guest Carts/{cart Id}/estimate Shipping Methods API
  phrasing_intents:
  - id: PostV1GuestcartsCartIdEstimateshippingmethods
    intent: Estimate shipping options for a guest cart
    question: Which shipping methods are available for a guest cart going to a given address?
  phrasing_ops: 1
  slug: adobe-suite-guest-carts-cartid-estimate-shipping-methods-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/gift-message API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/gift-message.
  name: Adobe Suite Guest Carts/{cart Id}/gift Message API
  phrasing_intents:
  - id: GetV1GuestcartsCartIdGiftmessage
    intent: Get the gift message on a guest cart
    question: What gift message has a guest shopper added to their order?
  - id: PostV1GuestcartsCartIdGiftmessage
    intent: Set the gift message on a guest cart
    question: How do I add a gift message to a guest checkout order?
  phrasing_ops: 2
  slug: adobe-suite-guest-carts-cartid-gift-message-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/gift-message/{itemId} API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/gift-message/{itemid}.
  name: Adobe Suite Guest Carts/{cart Id}/gift Message/{item Id} API
  phrasing_intents:
  - id: GetV1GuestcartsCartIdGiftmessageItemId
    intent: Get the gift message on a guest cart item
    question: What gift message is attached to an item in a guest shopper's cart?
  - id: PostV1GuestcartsCartIdGiftmessageItemId
    intent: Set a gift message on a guest cart item
    question: Can a guest shopper add a gift message to one item in their cart?
  phrasing_ops: 2
  slug: adobe-suite-guest-carts-cartid-gift-message-itemid-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/items API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/items.
  name: Adobe Suite Guest Carts/{cart Id}/items API
  phrasing_intents:
  - id: GetV1GuestcartsCartIdItems
    intent: List items in a guest cart
    question: What products are currently in a guest shopper's cart?
  - id: PostV1GuestcartsCartIdItems
    intent: Add or update an item in a guest cart
    question: How do I add a product to a guest checkout cart?
  phrasing_ops: 2
  slug: adobe-suite-guest-carts-cartid-items-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/items/{itemId} API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/items/{itemid}.
  name: Adobe Suite Guest Carts/{cart Id}/items/{item Id} API
  phrasing_intents:
  - id: PutV1GuestcartsCartIdItemsItemId
    intent: Update an item in a guest cart
    question: How do I change the quantity of an item in a guest shopper's cart?
  - id: DeleteV1GuestcartsCartIdItemsItemId
    intent: Remove an item from a guest cart
    question: How do I remove a product from a guest checkout cart?
  phrasing_ops: 2
  slug: adobe-suite-guest-carts-cartid-items-itemid-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/order API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/order.
  name: Adobe Suite Guest Carts/{cart Id}/order API
  phrasing_intents:
  - id: PutV1GuestcartsCartIdOrder
    intent: Place an order for a guest cart
    question: How do I turn a guest shopper's cart into an order?
  phrasing_ops: 1
  slug: adobe-suite-guest-carts-cartid-order-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/payment-information API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/payment-information.
  name: Adobe Suite Guest Carts/{cart Id}/payment Information API
  phrasing_intents:
  - id: PostV1GuestcartsCartIdPaymentinformation
    intent: Pay for a guest cart and place the order
    question: How does a guest shopper pay and place an order in Adobe Commerce?
  - id: GetV1GuestcartsCartIdPaymentinformation
    intent: Get payment details for a guest cart
    question: Which payment methods are available for a guest shopper's cart?
  phrasing_ops: 2
  slug: adobe-suite-guest-carts-cartid-payment-information-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/payment-methods API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/payment-methods.
  name: Adobe Suite Guest Carts/{cart Id}/payment Methods API
  phrasing_intents:
  - id: GetV1GuestcartsCartIdPaymentmethods
    intent: List payment methods for a guest cart
    question: Which payment methods can a guest use to check out this cart?
  phrasing_ops: 1
  slug: adobe-suite-guest-carts-cartid-payment-methods-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/selected-payment-method API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/selected-payment-method.
  name: Adobe Suite Guest Carts/{cart Id}/selected Payment Method API
  phrasing_intents:
  - id: GetV1GuestcartsCartIdSelectedpaymentmethod
    intent: Get a guest cart's selected payment method
    question: Which payment method has a guest shopper chosen for their cart?
  - id: PutV1GuestcartsCartIdSelectedpaymentmethod
    intent: Set the payment method on a guest cart
    question: How do I set a payment method on a guest shopper's cart?
  phrasing_ops: 2
  slug: adobe-suite-guest-carts-cartid-selected-payment-method-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/set-payment-information API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/set-payment-information.
  name: Adobe Suite Guest Carts/{cart Id}/set Payment Information API
  phrasing_intents:
  - id: PostV1GuestcartsCartIdSetpaymentinformation
    intent: Set payment details on a guest cart
    question: How does a guest shopper add payment information at checkout?
  phrasing_ops: 1
  slug: adobe-suite-guest-carts-cartid-set-payment-information-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/shipping-information API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/shipping-information.
  name: Adobe Suite Guest Carts/{cart Id}/shipping Information API
  phrasing_intents:
  - id: PostV1GuestcartsCartIdShippinginformation
    intent: Set shipping details on a guest cart
    question: How do I add a shipping address and method to a guest checkout cart?
  phrasing_ops: 1
  slug: adobe-suite-guest-carts-cartid-shipping-information-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/shipping-methods API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/shipping-methods.
  name: Adobe Suite Guest Carts/{cart Id}/shipping Methods API
  phrasing_intents:
  - id: GetV1GuestcartsCartIdShippingmethods
    intent: List shipping options for a guest cart
    question: Which shipping methods can a guest shopper choose for their cart?
  phrasing_ops: 1
  slug: adobe-suite-guest-carts-cartid-shipping-methods-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/totals API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/totals.
  name: Adobe Suite Guest Carts/{cart Id}/totals API
  phrasing_intents:
  - id: GetV1GuestcartsCartIdTotals
    intent: Get a guest cart's totals
    question: How do I get the subtotal, tax and grand total for a guest shopper's cart?
  phrasing_ops: 1
  slug: adobe-suite-guest-carts-cartid-totals-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-carts/{cartId}/totals-information API from Adobe Suite — 1 operation(s) for guest-carts/{cartid}/totals-information.
  name: Adobe Suite Guest Carts/{cart Id}/totals Information API
  phrasing_intents:
  - id: PostV1GuestcartsCartIdTotalsinformation
    intent: Estimate a guest cart's totals for an address
    question: How do I calculate a guest cart's totals for a shipping address and method?
  phrasing_ops: 1
  slug: adobe-suite-guest-carts-cartid-totals-information-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The guest-giftregistry/{cartId}/estimate-shipping-methods API from Adobe Suite — 1 operation(s) for guest-giftregistry/{cartid}/estimate-shipping-methods.
  name: Adobe Suite Guest Giftregistry/{cart Id}/estimate Shipping Methods API
  phrasing_intents:
  - id: PostV1GuestgiftregistryCartIdEstimateshippingmethods
    intent: Estimate shipping to a gift registry
    question: What shipping methods and costs apply when a guest ships a gift to a registry?
  phrasing_ops: 1
  slug: adobe-suite-guest-giftregistry-cartid-estimate-shipping-methods-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The health API from Adobe Suite — 2 operation(s) for health.
  name: Adobe Suite Health API
  phrasing_intents:
  - id: getImHealth
    intent: Check Unitary API service health
    question: Is the Unitary API service healthy for my IMS organization?
  - id: getHealth
    intent: Check Lightroom services health
    question: Are the Lightroom services up right now?
  phrasing_ops: 2
  slug: adobe-suite-health-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: A host represents a hosted destination where a library build can be delivered and ultimately deployed. Hosts can be either Akamai or SFTP servers.
  name: Adobe Suite Hosts API
  phrasing_intents:
  - id: listHosts
    intent: List a property's hosts
    question: Which hosts deliver my Tags library for a property?
  - id: createHost
    intent: Create a host for a property
    question: How do I add an SFTP or Adobe-managed host to a Tags property?
  - id: retrieveHost
    intent: Retrieve a host
    question: What are the settings of a particular Tags host?
  - id: deleteHost
    intent: Delete a host
    question: Can I delete a host that a property no longer uses?
  - id: updateHost
    intent: Update an SFTP host
    question: Can I edit a host, and which host types allow updates?
  - id: retrieveHostProperty
    intent: Find the property a host belongs to
    question: Which property does a host belong to?
  phrasing_ops: 6
  slug: adobe-suite-hosts-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Hour API from Adobe Suite — 8 operation(s) for hour.
  name: Adobe Suite Hour API
  phrasing_intents:
  - id: getHour
    intent: Get one logged hour entry
    question: How can I look up a single time entry logged in Workfront?
  - id: editHour
    intent: Edit a single hour entry
    question: How do I correct the time on one logged hour entry?
  - id: deleteHour
    intent: Delete one hour entry
    question: How do I remove a time entry that was logged by mistake?
  - id: getHours
    intent: Fetch several hour entries by ID
    question: Can I retrieve several logged hour entries at once by their IDs?
  - id: editHours
    intent: Edit many hour entries in one request
    question: Is there a way to update a batch of time entries together?
  - id: addHours
    intent: Log a new hour entry
    question: How do I log time worked through the API?
  - id: deleteHours
    intent: Delete several hour entries at once
    question: Can I delete multiple time entries in one call?
  - id: countHours
    intent: Count logged hour entries
    question: How many hour entries have been logged?
  phrasing_ops: 13
  slug: adobe-suite-hour-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Convert HTML Resources to a PDF File
  name: Adobe Suite Html to PDF API
  phrasing_intents:
  - id: pdfoperations.htmltopdf
    intent: Convert HTML or a web page into a PDF
    question: How do I turn an HTML page with inline CSS into a PDF with Adobe PDF Services?
  - id: pdfoperations.htmltopdf.jobstatus
    intent: Check whether an HTML-to-PDF job is done
    question: How do I know when my HTML to PDF conversion has finished?
  phrasing_ops: 2
  slug: adobe-suite-html-to-pdf-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Identity services provide access to a profile identity in XID form.
  name: Adobe Suite Identity API
  phrasing_intents:
  - id: retrieveIdentity
    intent: Look up an identity's XID
    question: How do I get the XID for an identity when I know its namespace and value?
  - id: identityUsingGET
    intent: Get a Marketo access token with GET
    question: How do I get a Marketo Engage access token with a GET request?
  - id: identityUsingPOST
    intent: Get a Marketo access token with POST
    question: Can I request a Marketo access token with a POST instead of a GET?
  phrasing_ops: 3
  slug: adobe-suite-identity-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Identity namespaces provide context to identity data. Experience Platform provides standard namespaces as well as allowing organizations to create and manage custom namespaces.
  name: Adobe Suite Identity Namespace API
  phrasing_intents:
  - id: getIdNamespaces
    intent: List identity namespaces
    question: Which identity namespaces are available to my organization?
  - id: createNamespace
    intent: Create a custom identity namespace
    question: How do I add a custom identity namespace for a loyalty ID?
  - id: retrieveIdentityNamespace
    intent: Get an identity namespace
    question: What code and type does a specific identity namespace have?
  - id: updateIdentityNamespace
    intent: Update an identity namespace
    question: Can I rename or re-describe an existing custom namespace?
  phrasing_ops: 4
  slug: adobe-suite-identity-namespace-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Convert raster artwork to vector format using Illustrator Image Trace. These jobs run asynchronously.
  name: Adobe Suite Image Trace API
  phrasing_intents:
  - id: traceImage
    intent: Convert a raster image into an SVG vector
    question: Can I turn a JPEG or PNG into a scalable SVG?
  - id: imageTraceJobStatus
    intent: Check an image trace job's status
    question: Has my image-to-vector job finished?
  phrasing_ops: 2
  slug: adobe-suite-image-trace-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Import PDF Form Data API will take the form data provided as a JSON, insert it into the PDF form, and generate the resulting PDF.
  name: Adobe Suite Import PDF Form Data API
  phrasing_intents:
  - id: pdfoperations.setformdata
    intent: Fill a PDF form with JSON data
    question: How do I fill in the fields of a PDF form from JSON?
  - id: pdfoperations.setformdata.jobstatus
    intent: Check a PDF form fill job
    question: How do I know when my PDF form fill has completed?
  phrasing_ops: 2
  slug: adobe-suite-import-pdf-form-data-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Info API from Adobe Suite — 1 operation(s) for info.
  name: Adobe Suite Info API
  phrasing_intents:
  - id: info
    intent: Get customer SSO and API version info
    question: Which API version is my instance running?
  phrasing_ops: 1
  slug: adobe-suite-info-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Initiative API from Adobe Suite — 5 operation(s) for initiative.
  name: Adobe Suite Initiative API
  phrasing_intents:
  - id: getInitiative
    intent: Get one initiative
    question: How do I look up a single Workfront initiative by ID?
  - id: getInitiatives
    intent: Get several initiatives by ID
    question: Can I fetch multiple initiatives at once using their IDs?
  - id: countInitiatives
    intent: Count initiatives
    question: How many initiatives are there in our planning?
  - id: searchInitiatives
    intent: Search initiatives
    question: Which initiatives match a name or status I'm looking for?
  - id: reportInitiatives
    intent: Run an aggregate report on initiatives
    question: Can I get a grouped summary report of initiatives?
  phrasing_ops: 5
  slug: adobe-suite-initiative-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Insights contain metrics which are used to empower a data scientist to evaluate and choose optimal ML Models by displaying relevant evaluation metrics.
  name: Adobe Suite Insights API
  phrasing_intents:
  - id: retrieveInsights
    intent: List model insights from experiment runs
    question: How do I list insights for all my Sensei experiment runs?
  - id: createInsights
    intent: Create a model insight
    question: How do I record a new insight with metrics for a trained model?
  - id: retrieveInsight
    intent: Get a single model insight
    question: How do I read one specific insight by ID?
  - id: retrieveMetrics
    intent: List default evaluation metrics per algorithm
    question: What default metrics are available for evaluating a given algorithm?
  phrasing_ops: 4
  slug: adobe-suite-insights-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The integration/admin/token API from Adobe Suite — 1 operation(s) for integration/admin/token.
  name: Adobe Suite Integration/admin/token API
  phrasing_intents:
  - id: PostV1IntegrationAdminToken
    intent: Get an admin access token
    question: What do I call to get an admin bearer token for the Commerce REST API?
  phrasing_ops: 1
  slug: adobe-suite-integration-admin-token-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The integration/customer/revoke-customer-token API from Adobe Suite — 1 operation(s) for integration/customer/revoke-customer-token.
  name: Adobe Suite Integration/customer/revoke Customer Token API
  phrasing_intents:
  - id: PostV1IntegrationCustomerRevokecustomertoken
    intent: Revoke a customer's access token
    question: What call invalidates a storefront customer's API token?
  phrasing_ops: 1
  slug: adobe-suite-integration-customer-revoke-customer-token-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The integration/customer/token API from Adobe Suite — 1 operation(s) for integration/customer/token.
  name: Adobe Suite Integration/customer/token API
  phrasing_intents:
  - id: PostV1IntegrationCustomerToken
    intent: Get an access token from customer credentials
    question: How do I get a customer access token for the Commerce REST API?
  phrasing_ops: 1
  slug: adobe-suite-integration-customer-token-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The inventory/in-store-pickup/pickup-locations/ API from Adobe Suite — 1 operation(s) for inventory/in-store-pickup/pickup-locations/.
  name: Adobe Suite Inventory/in Store Pickup/pickup Locations/ API
  phrasing_intents:
  - id: GetV1InventoryInstorepickupPickuplocations
    intent: Find in-store pickup locations
    question: Which stores near a customer offer in-store pickup?
  phrasing_ops: 1
  slug: adobe-suite-inventory-in-store-pickup-pickup-locations-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Use the IP Access endpoints to manage allowed IP ranges, enabling secure data access for Query Service in Adobe Experience Platform.
  name: Adobe Suite IP Access API
  phrasing_intents:
  - id: retrieveIPRanges
    intent: Get allowed IP ranges for a sandbox
    question: Which IP addresses are allowed to query data in my sandbox through Query Service?
  - id: setIPRanges
    intent: Set allowed IP ranges for a sandbox
    question: How do I restrict Query Service access to our office IP ranges?
  - id: deleteIPRanges
    intent: Remove all IP range restrictions for a sandbox
    question: How do I clear every IP restriction on a sandbox?
  phrasing_ops: 3
  slug: adobe-suite-ip-access-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The IP Allowlist API from Adobe Suite — 2 operation(s) for ip allowlist.
  name: Adobe Suite IP Allowlist API
  phrasing_intents:
  - id: getIPAllowlist
    intent: Get an IP allowlist
    question: How do I see the IP ranges in one of my Cloud Manager allowlists?
  - id: updateIPAllowlist
    intent: Update an IP allowlist
    question: Can I change the IP ranges or name of an existing allowlist?
  - id: deleteIPAllowlist
    intent: Delete an IP allowlist
    question: How do I remove an IP allowlist from a program?
  - id: getProgramIPAllowlists
    intent: List a program's IP allowlists
    question: Which IP allowlists are defined for my program?
  - id: createIPAllowlist
    intent: Create an IP allowlist
    question: How do I restrict access to a program to certain IP addresses?
  phrasing_ops: 5
  slug: adobe-suite-ip-allowlist-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The IP Allowlist Binding API from Adobe Suite — 2 operation(s) for ip allowlist binding.
  name: Adobe Suite IP Allowlist Binding API
  phrasing_intents:
  - id: getIPAllowlistBinding
    intent: Get one IP allowlist binding
    question: How do I check which environment and tier a specific IP allowlist binding applies to?
  - id: deleteIPAllowlistBinding
    intent: Remove an IP allowlist binding
    question: How do I unbind an IP allowlist from an environment?
  - id: getIPAllowlistBindings
    intent: List an IP allowlist's bindings
    question: Which environments is an IP allowlist currently bound to?
  - id: createIPAllowlistBinding
    intent: Bind an IP allowlist to an environment
    question: How do I apply an IP allowlist to an environment in Cloud Manager?
  phrasing_ops: 4
  slug: adobe-suite-ip-allowlist-binding-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Use the IP Validation endpoint to verify if a specified IP address is permitted to access data within a designated sandbox in Query Service.
  name: Adobe Suite IP Validation API
  phrasing_intents:
  - id: validateIPAddress
    intent: Check whether an IP can access a sandbox
    question: Is a given IP address allowed to access my Experience Platform sandbox?
  phrasing_ops: 1
  slug: adobe-suite-ip-validation-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Iprange API from Adobe Suite — 5 operation(s) for iprange.
  name: Adobe Suite Iprange API
  phrasing_intents:
  - id: getIPRange
    intent: Get one IP range by ID
    question: How do I read a single allowed IP range in Adobe Workfront?
  - id: editIPRange
    intent: Edit a single IP range
    question: What call changes the start or end address of one IP range?
  - id: deleteIPRange
    intent: Delete a single IP range
    question: How do I remove one IP range from the allow list?
  - id: getIPRanges
    intent: Get several IP ranges by ID
    question: Can I load several IP ranges by their IDs in one request?
  - id: editIPRanges
    intent: Bulk edit IP ranges
    question: How do I update many IP ranges at once?
  - id: addIPRanges
    intent: Create an IP range
    question: How do I add a new IP range to the allow list?
  - id: deleteIPRanges
    intent: Bulk delete IP ranges
    question: Can I delete several IP ranges in one call?
  - id: countIPRanges
    intent: Count IP ranges
    question: How many IP ranges match a filter?
  phrasing_ops: 10
  slug: adobe-suite-iprange-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Iteration API from Adobe Suite — 7 operation(s) for iteration.
  name: Adobe Suite Iteration API
  phrasing_intents:
  - id: getIteration
    intent: Look up one agile iteration
    question: What are the details of a single Workfront iteration?
  - id: editIteration
    intent: Edit an iteration
    question: How do I change the dates or goal of one iteration?
  - id: deleteIteration
    intent: Delete an iteration
    question: Can I delete a sprint I created by mistake?
  - id: getIterations
    intent: Fetch several iterations by ID
    question: Can I pull multiple iterations at once using their IDs?
  - id: editIterations
    intent: Bulk edit iterations
    question: Can I update several iterations in one request?
  - id: addIterations
    intent: Create an iteration
    question: How do I create a new sprint for an agile team?
  - id: deleteIterations
    intent: Delete several iterations
    question: Can I bulk delete old sprints?
  - id: countIterations
    intent: Count iterations
    question: How many iterations do we have?
  phrasing_ops: 12
  slug: adobe-suite-iteration-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'Track job execution status and lifecycle events. Retrieves the most recent status event for jobs across different execution stages: `not_started` (job creation), `running` (execution begins), `succeed'
  name: Adobe Suite Job Status API
  phrasing_intents:
  - id: getJobStatus
    intent: Check a custom script job's status
    question: How do I check the status of a custom script job I ran?
  - id: getV2StatusByJobId
    intent: Check a Photoshop v2 job's status
    question: How do I poll a Photoshop v2 or auto-crop job?
  phrasing_ops: 2
  slug: adobe-suite-job-status-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Operations related to journey management
  name: Adobe Suite Journeys API
  phrasing_intents:
  - id: getJourneys
    intent: List Journey Optimizer journeys
    question: How do I list the journeys in a Journey Optimizer sandbox?
  - id: getJourneyById
    intent: Get a journey by ID
    question: What does one journey's full definition look like when fetched by ID?
  phrasing_ops: 2
  slug: adobe-suite-journeys-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Kanbanboard API from Adobe Suite — 5 operation(s) for kanbanboard.
  name: Adobe Suite Kanbanboard API
  phrasing_intents:
  - id: getKanbanBoard
    intent: Look up one Kanban board
    question: How do I get the details of one Workfront Kanban board?
  - id: editKanbanBoard
    intent: Update one Kanban board
    question: Can I rename or reconfigure an existing Kanban board?
  - id: deleteKanbanBoard
    intent: Delete one Kanban board
    question: How do I delete a Kanban board I no longer use?
  - id: getKanbanBoards
    intent: Fetch several Kanban boards by ID
    question: Can I retrieve several Kanban boards at once by their IDs?
  - id: editKanbanBoards
    intent: Update many Kanban boards at once
    question: Is there a bulk edit for Kanban boards?
  - id: addKanbanBoards
    intent: Create a Kanban board
    question: How do I set up a new Kanban board for my team?
  - id: deleteKanbanBoards
    intent: Delete many Kanban boards
    question: Can I bulk delete Kanban boards by ID?
  - id: countKanbanBoards
    intent: Count Kanban boards
    question: How many Kanban boards match a filter?
  phrasing_ops: 10
  slug: adobe-suite-kanbanboard-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Data usage labels allow you to categorize datasets and fields according to usage policies that apply to that data.
  name: Adobe Suite Labels API
  phrasing_intents:
  - id: listCoreLabels
    intent: List core data usage labels
    question: What core data usage labels does Adobe provide for data governance?
  - id: retrieveCoreLabel
    intent: Get one core data usage label
    question: What does a specific core label like C1 mean?
  - id: listCustomLabels
    intent: List custom data usage labels
    question: Which custom labels has my organization defined?
  - id: retrieveCustomLabel
    intent: Get one custom data usage label
    question: What are the details of a custom label we created?
  - id: createUpdateCustomLabel
    intent: Create or update a custom label
    question: How do I define a new custom data usage label?
  phrasing_ops: 5
  slug: adobe-suite-labels-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The LastBatches API from Adobe Suite — 1 operation(s) for lastbatches.
  name: Adobe Suite Last Batches API
  phrasing_intents:
  - id: listLastBatches
    intent: Check the latest ingestion batch per dataset
    question: What was the last batch loaded into each of my datasets, and did it succeed?
  phrasing_ops: 1
  slug: adobe-suite-lastbatches-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Layouttemplate API from Adobe Suite — 5 operation(s) for layouttemplate.
  name: Adobe Suite Layouttemplate API
  phrasing_intents:
  - id: getLayoutTemplate
    intent: Get a single layout template
    question: How do I look up one layout template by ID?
  - id: editLayoutTemplate
    intent: Edit a single layout template
    question: How can I change the navigation or views in one layout template?
  - id: deleteLayoutTemplate
    intent: Delete a single layout template
    question: How do I delete a layout template nobody uses?
  - id: getLayoutTemplates
    intent: Get several layout templates by ID
    question: Can I fetch multiple layout templates in one call?
  - id: editLayoutTemplates
    intent: Edit many layout templates at once
    question: Is there a bulk edit for layout templates?
  - id: addLayoutTemplates
    intent: Create a layout template
    question: How do I create a new layout template for a group of users?
  - id: deleteLayoutTemplates
    intent: Delete several layout templates at once
    question: Can I bulk delete layout templates by ID?
  - id: countLayoutTemplates
    intent: Count layout templates
    question: How many layout templates exist?
  phrasing_ops: 10
  slug: adobe-suite-layouttemplate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: A library is a collection of resources (extensions, rules, and data elements) that represent the desired behavior of a property. Libraries are compiled into builds, and those builds are assigned to di
  name: Adobe Suite Libraries API
  phrasing_intents:
  - id: listLibraries
    intent: List the libraries in a tags property
    question: What libraries exist in my Adobe tags property?
  - id: createLibrary
    intent: Create a library in a tags property
    question: How do I start a new library to bundle tag changes for publishing?
  - id: retrieveLibrary
    intent: Get a library's details
    question: How do I look up one tags library by its ID?
  - id: deleteLibrary
    intent: Delete a library
    question: How do I permanently remove a tags library I no longer need?
  - id: updateLibrary
    intent: Rename a library or move it through publishing
    question: How do I rename a tags library?
  - id: retrieveLibraryProperty
    intent: Find which property a library belongs to
    question: Which tags property owns this library?
  - id: listLibraryBuilds
    intent: List a library's builds
    question: How do I see all the builds that were made from a library?
  - id: createBuild
    intent: Build a library
    question: How do I kick off a build for a tags library?
  phrasing_ops: 30
  slug: adobe-suite-libraries-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: App-facing APIs for Adobe CC Libraries.
  name: Adobe Suite Library Service API
  phrasing_intents:
  - id: getLibraries
    intent: List a user's Creative Cloud Libraries
    question: How do I list all the Creative Cloud Libraries I have access to?
  - id: createLibraries
    intent: Create, copy or move a library
    question: How do I create a new Creative Cloud Library?
  - id: getLibrary
    intent: Get a specific library's details
    question: How do I fetch the details of one library by its ID?
  - id: headLibrary
    intent: Check a library's headers without the body
    question: Can I check whether a library exists without downloading its full details?
  - id: deleteLibrary
    intent: Delete a library
    question: How do I delete a whole Creative Cloud Library?
  - id: patchLibrary
    intent: Run several library operations in sequence
    question: Can I send an array of requests that run one after another against a library?
  - id: unArchiveLibraryElements
    intent: Restore archived elements in a library
    question: How do I bring back elements I archived in a library?
  - id: deleteLibraryElements
    intent: Permanently delete archived elements
    question: How do I permanently purge several archived elements from a library?
  phrasing_ops: 19
  slug: adobe-suite-library-service-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: App-facing APIs specifically for Adobe CC Library Bookmarks.
  name: Adobe Suite Library Service - Bookmarks API
  phrasing_intents:
  - id: getBookmarks
    intent: List my library bookmarks
    question: Which Creative Cloud Libraries have I bookmarked?
  - id: addLibraryBookmarks
    intent: Bookmark one or more libraries
    question: How do I bookmark a library so it shows in my list?
  - id: putLibraryBookmark
    intent: Update an existing library bookmark
    question: Can I change a bookmark I already created?
  - id: removeLibraryBookmark
    intent: Remove a library bookmark
    question: How do I un-bookmark a library?
  phrasing_ops: 4
  slug: adobe-suite-library-service-bookmarks-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: App-facing APIs specifically for Adobe CC Public Libraries.
  name: Adobe Suite Library Service - Public API
  phrasing_intents:
  - id: getPublicLibrary
    intent: Retrieve a public Creative Cloud library
    question: How do I read the details of a publicly shared Creative Cloud library?
  - id: headPublicLibrary
    intent: Check that a public library exists
    question: Can I check whether a public library is still available without downloading it?
  - id: getPublicLibraryElements
    intent: List the elements in a public library
    question: What colors, graphics and other assets are in a public library?
  - id: getPublicLibraryElement
    intent: Retrieve one element from a public library
    question: How do I pull a single asset out of a public Creative Cloud library?
  phrasing_ops: 4
  slug: adobe-suite-library-service-public-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Lightroom API from Adobe Suite — 6 operation(s) for lightroom.
  name: Adobe Suite Lightroom API
  phrasing_intents:
  - id: autoStraighten
    intent: Auto straighten a photo
    question: How do I automatically level a crooked photo with Lightroom?
  - id: autoTone
    intent: Auto tone a photo
    question: How do I automatically fix exposure and contrast in a photo?
  - id: edit
    intent: Apply specific edit settings to a photo
    question: How do I apply my own exposure, contrast or saturation values to an image?
  - id: presets
    intent: Apply a Lightroom preset to a photo
    question: How do I apply a saved preset to an image?
  - id: xmp
    intent: Apply XMP settings to a photo
    question: Can I apply the settings from an XMP sidecar to an image?
  - id: acrstatus
    intent: Check a Lightroom editing job's status
    question: How do I know when my photo edit job has finished?
  phrasing_ops: 6
  slug: adobe-suite-lightroom-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Like API from Adobe Suite — 5 operation(s) for like.
  name: Adobe Suite Like API
  phrasing_intents:
  - id: getLike
    intent: Get one like on an update
    question: How do I look up a single like by its ID?
  - id: getLikes
    intent: Get several likes by ID
    question: Can I load multiple likes at once from a list of IDs?
  - id: countLikes
    intent: Count likes
    question: How many likes have updates and notes received?
  - id: searchLikes
    intent: Search likes
    question: How do I find the likes on a particular note?
  - id: reportLikes
    intent: Aggregate report of likes
    question: Can I get like totals grouped by person or note?
  phrasing_ops: 5
  slug: adobe-suite-like-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Convert a PDF File to a Linearized or Web Optimized PDF File
  name: Adobe Suite Linearize PDF API
  phrasing_intents:
  - id: pdfoperations.linearizepdf
    intent: Linearize a PDF for fast web viewing
    question: How do I make a PDF web-optimized so it loads page by page over the network?
  - id: pdfoperations.linearizepdf.jobstatus
    intent: Check a PDF linearization job's status
    question: Is my linearize PDF job finished yet?
  phrasing_ops: 2
  slug: adobe-suite-linearize-pdf-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Login API from Adobe Suite — 1 operation(s) for login.
  name: Adobe Suite Login API
  phrasing_intents:
  - id: login
    intent: Log in and start a session
    question: What's the way to log in and get a session with username and password?
  phrasing_ops: 1
  slug: adobe-suite-login-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Logout API from Adobe Suite — 1 operation(s) for logout.
  name: Adobe Suite Logout API
  phrasing_intents:
  - id: logout
    intent: Log out of the current session
    question: How do I end my current API session?
  phrasing_ops: 1
  slug: adobe-suite-logout-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Endpoints for managing asynchronous jobs.
  name: Adobe Suite Manage jobs API
  phrasing_intents:
  - id: status
    intent: Check a v1 async job status
    question: How do I check whether a Dynamic Graphics Render or Describe job finished?
  - id: cancel-render-job
    intent: Cancel a template render job
    question: Can I abort a template render job that is still running?
  - id: list-render-jobs
    intent: List my template render jobs
    question: Which template render jobs have I submitted?
  - id: job-result-v2
    intent: Get a reframed video job result
    question: How do I get the output of a video reframe job?
  - id: jobResultV3
    intent: Check a v3 generation or upscale job
    question: How do I check an upscale or composite job's status?
  - id: cancelJobV4
    intent: Cancel a v3 asynchronous job
    question: Can I cancel a generation or upscale job I started?
  phrasing_ops: 6
  slug: adobe-suite-manage-jobs-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Mapping sets can be used to define how data in a source schema maps to that of a destination schema.
  name: Adobe Suite Mapping sets API
  phrasing_intents:
  - id: listMappingSets
    intent: List data prep mapping sets
    question: How do I list the mapping sets defined in my Experience Platform sandbox?
  - id: createMappingSet
    intent: Create a mapping set
    question: How do I create a new mapping set that maps source fields to an XDM schema?
  - id: validateMappingSet
    intent: Validate a mapping set before saving
    question: Can I check that my field mappings are valid without creating the mapping set?
  - id: previewMappingSet
    intent: Preview mapping output on sample data
    question: How can I see what my mappings produce on sample data before using them?
  - id: retrieveMappingSet
    intent: Get a mapping set
    question: How do I look up one mapping set by ID?
  - id: putMappingSet
    intent: Update a mapping set
    question: How do I change the mappings in an existing mapping set?
  - id: listMappings
    intent: List the mappings in a mapping set
    question: How do I see every individual field mapping inside a mapping set?
  - id: retrieveMapping
    intent: Get one mapping from a mapping set
    question: How do I look up a single field mapping within a mapping set?
  phrasing_ops: 8
  slug: adobe-suite-mapping-sets-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Marketing actions, in the context of Data Governance, are actions that an Experience Platform data consumer takes, for which there is a need to check for violations of data usage policies.
  name: Adobe Suite Marketing actions API
  phrasing_intents:
  - id: listCoreMarketingActions
    intent: List Adobe-defined core marketing actions
    question: What core marketing actions does Adobe define for data governance?
  - id: retrieveCoreMarketingAction
    intent: Get a core marketing action
    question: How do I look up one of Adobe's core marketing actions by name?
  - id: listCustomMarketingActions
    intent: List my organization's custom marketing actions
    question: Which custom marketing actions has my organization defined?
  - id: retrieveCustomMarketingAction
    intent: Get a custom marketing action
    question: How do I look up a custom marketing action my team created?
  - id: createOrUpdateCustomMarketingAction
    intent: Create or update a custom marketing action
    question: How do I define a new custom marketing action for data usage policies?
  - id: deleteCustomMarketingAction
    intent: Delete a custom marketing action
    question: How do I remove a custom marketing action we no longer use?
  phrasing_ops: 6
  slug: adobe-suite-marketing-actions-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Merge policies are the rules that Platform uses to determine how data will be prioritized and what data will be combined to create an individual customer profile. For more information on using this se
  name: Adobe Suite Merge policies API
  phrasing_intents:
  - id: getMany
    intent: List merge policies
    question: Which merge policies exist for our Real-Time Customer Profile data?
  - id: createMergePolicy
    intent: Create a merge policy
    question: How do I create a merge policy that decides how profile fragments are combined?
  - id: retrieveMergePolicy
    intent: Get one merge policy
    question: What identity graph and attribute merge rules does a specific merge policy use?
  - id: updateMergePolicy
    intent: Replace a merge policy
    question: Can I overwrite an entire merge policy with a new definition?
  - id: deleteMergePolicy
    intent: Delete a merge policy
    question: How do I delete a merge policy we no longer use?
  - id: patchMergePolicy
    intent: Change individual fields on a merge policy
    question: Can I change just one attribute of a merge policy without replacing it?
  - id: bulkGetMergePolicies
    intent: Get several merge policies by ID
    question: Can I fetch several merge policies at once by passing their IDs?
  phrasing_ops: 7
  slug: adobe-suite-merge-policies-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Metadata collection
  name: Adobe Suite Metadata Resource API
  phrasing_intents:
  - id: getSurfaces
    intent: List channel surfaces
    question: What surfaces are configured for my messaging channels?
  - id: getSurface
    intent: Get a surface's details
    question: How do I look up the configuration of one channel surface?
  phrasing_ops: 2
  slug: adobe-suite-metadata-resource-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Observability metrics are parameters used to gain statistical insights into actions being performed in Adobe Experience Platform. These insights include counts of available Platform resources and stat
  name: Adobe Suite Metrics API
  phrasing_intents:
  - id: retrieveMetricsV1
    intent: Retrieve observability metrics (deprecated V1)
    question: Can I still pull Experience Platform observability metrics with the older GET version?
  - id: retrieveMetricsV2
    intent: Retrieve observability metrics (V2)
    question: How do I query Experience Platform observability metrics over a time window?
  - id: getMetrics
    intent: List metrics available for a report suite
    question: Which Analytics metrics can I use in a given report suite?
  - id: getMetric
    intent: Get one Analytics metric by ID
    question: What does a single Analytics metric mean and how is it defined?
  phrasing_ops: 4
  slug: adobe-suite-metrics-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Milestone API from Adobe Suite — 5 operation(s) for milestone.
  name: Adobe Suite Milestone API
  phrasing_intents:
  - id: getMilestone
    intent: Get one Workfront milestone
    question: How do I look up a single milestone by its ID?
  - id: editMilestone
    intent: Update one milestone
    question: Can I rename or recolor an existing milestone?
  - id: deleteMilestone
    intent: Delete one milestone
    question: How do I remove a single milestone?
  - id: getMilestones
    intent: Get several milestones by ID
    question: Can I load multiple milestones at once from their IDs?
  - id: editMilestones
    intent: Update many milestones at once
    question: Can I change several milestones in one request?
  - id: addMilestones
    intent: Create a milestone
    question: How do I add a new milestone to use in milestone paths?
  - id: deleteMilestones
    intent: Delete several milestones
    question: Can I remove multiple milestones in one call?
  - id: countMilestones
    intent: Count milestones
    question: How many milestones are defined in Workfront?
  phrasing_ops: 10
  slug: adobe-suite-milestone-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Milestonepath API from Adobe Suite — 5 operation(s) for milestonepath.
  name: Adobe Suite Milestonepath API
  phrasing_intents:
  - id: getMilestonePath
    intent: Get one milestone path
    question: Which milestones make up a specific milestone path?
  - id: editMilestonePath
    intent: Edit a single milestone path
    question: How do I rename or change the milestones on one milestone path?
  - id: deleteMilestonePath
    intent: Delete a single milestone path
    question: Can I remove a milestone path that no project uses anymore?
  - id: getMilestonePaths
    intent: Fetch several milestone paths by ID
    question: Can I retrieve a batch of milestone paths when I know their IDs?
  - id: editMilestonePaths
    intent: Edit many milestone paths at once
    question: Is it possible to bulk update several milestone paths?
  - id: addMilestonePaths
    intent: Create a milestone path
    question: How do I create a milestone path for our project templates?
  - id: deleteMilestonePaths
    intent: Delete several milestone paths by ID
    question: Can I remove a batch of milestone paths at once?
  - id: countMilestonePaths
    intent: Count milestone paths matching filters
    question: How many milestone paths exist in Workfront?
  phrasing_ops: 10
  slug: adobe-suite-milestonepath-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: '"Mixin" is the former term for a field group. The /mixins endpoints are deprecated and only maintained as legacy endpoints. For new implementations, please use the /fieldgroups endpoint instead.'
  name: Adobe Suite Mixins (deprecated) API
  phrasing_intents:
  - id: listMixins
    intent: List mixins in a container (deprecated)
    question: How do I list the mixins in the schema registry's tenant or global container?
  - id: lookupMixin
    intent: Get one mixin (deprecated)
    question: How do I look up a single mixin by its ID in the schema registry?
  - id: createMixin
    intent: Create a custom mixin (deprecated)
    question: How do I create a custom mixin that extends an XDM class?
  - id: replaceMixin
    intent: Replace a custom mixin (deprecated)
    question: Can I overwrite a custom mixin with a whole new definition?
  - id: updateMixin
    intent: Patch a custom mixin (deprecated)
    question: Can I change part of a custom mixin with a JSON Patch?
  - id: removeMixin
    intent: Delete a custom mixin (deprecated)
    question: What's the way to delete a custom mixin from my tenant?
  phrasing_ops: 6
  slug: adobe-suite-mixins-deprecated-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: MLInstances represent the combination of a specific Engine with particular set of configurations. An instance is often use-case specific for a customer or client.
  name: Adobe Suite ML Instances API
  phrasing_intents:
  - id: listMLInstances
    intent: List ML instances
    question: How do I see all the ML instances I've set up?
  - id: createMLInstance
    intent: Create an ML instance of an engine
    question: How can I create a new MLInstance from an existing engine?
  - id: deleteMLInstances
    intent: Delete all ML instances for an engine
    question: Can I remove every ML instance built on one engine at once?
  - id: retrieveMLInstance
    intent: Get an ML instance
    question: How do I look up one ML instance's details?
  - id: updateMLInstance
    intent: Update an ML instance
    question: Can I rename or retag an existing ML instance?
  - id: deleteMLInstance
    intent: Delete one ML instance
    question: How do I delete a single ML instance?
  phrasing_ops: 6
  slug: adobe-suite-mlinstances-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: An MLService is a published trained model that provides your organization with the ability to access and reuse previously developed models. A key feature of MLServices is the ability to automate train
  name: Adobe Suite ML Services API
  phrasing_intents:
  - id: retrieveMLServices
    intent: List MLServices
    question: Which machine learning services are deployed in my sandbox?
  - id: createMLService
    intent: Create an MLService
    question: How do I publish a trained ML instance as a service that scores on a schedule?
  - id: deleteMLServices
    intent: Delete all MLServices for an ML instance
    question: Can I remove every MLService built from one ML instance at once?
  - id: retrieveMLService
    intent: Get one MLService
    question: How do I see the schedules and datasets of a single MLService?
  - id: updateMLService
    intent: Update an MLService
    question: Can I change the scoring schedule of an existing MLService?
  - id: deleteMLService
    intent: Delete one MLService
    question: How do I remove a single ML service I no longer need?
  phrasing_ops: 6
  slug: adobe-suite-mlservices-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Allows machine learning Model management and registration (Model artifact that is created by the training process).
  name: Adobe Suite Models API
  phrasing_intents:
  - id: listModels
    intent: List machine learning models
    question: What trained models exist in my Adobe Experience Platform sandbox?
  - id: createModel
    intent: Create a model for an engine and ML instance
    question: How do I register a new model for an engine and ML instance?
  - id: retrieveModel
    intent: Get one model's details
    question: How do I look up the metadata for a specific model?
  - id: updateModel
    intent: Update an existing model
    question: How do I rename a model or change its description?
  - id: deleteModel
    intent: Delete a model
    question: How do I permanently remove a model I no longer need?
  - id: retrieveModelArtifact
    intent: Download a model's binary artifact
    question: How do I download the binary file behind a trained model?
  - id: retrieveModelTranscodings
    intent: List a model's transcodings
    question: Which format conversions have been made for a model?
  - id: createModelTranscoding
    intent: Transcode a model into another format
    question: How do I convert a model into a different target format?
  phrasing_ops: 9
  slug: adobe-suite-models-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The negotiable-carts/{cartId}/billing-address API from Adobe Suite — 1 operation(s) for negotiable-carts/{cartid}/billing-address.
  name: Adobe Suite Negotiable Carts/{cart Id}/billing Address API
  phrasing_intents:
  - id: GetV1NegotiablecartsCartIdBillingaddress
    intent: Get a negotiable quote's billing address
    question: What billing address is set on a B2B negotiable quote?
  - id: PostV1NegotiablecartsCartIdBillingaddress
    intent: Set a negotiable quote's billing address
    question: How do I assign a billing address to a negotiable quote?
  phrasing_ops: 2
  slug: adobe-suite-negotiable-carts-cartid-billing-address-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The negotiable-carts/{cartId}/coupons API from Adobe Suite — 1 operation(s) for negotiable-carts/{cartid}/coupons.
  name: Adobe Suite Negotiable Carts/{cart Id}/coupons API
  phrasing_intents:
  - id: DeleteV1NegotiablecartsCartIdCoupons
    intent: Remove a coupon from a negotiable cart
    question: How do I take a coupon off a B2B negotiable quote cart?
  phrasing_ops: 1
  slug: adobe-suite-negotiable-carts-cartid-coupons-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The negotiable-carts/{cartId}/coupons/{couponCode} API from Adobe Suite — 1 operation(s) for negotiable-carts/{cartid}/coupons/{couponcode}.
  name: Adobe Suite Negotiable Carts/{cart Id}/coupons/{coupon Code} API
  phrasing_intents:
  - id: PutV1NegotiablecartsCartIdCouponsCouponCode
    intent: Apply a coupon to a negotiable quote cart
    question: How do I add a coupon code to a B2B negotiable quote cart?
  phrasing_ops: 1
  slug: adobe-suite-negotiable-carts-cartid-coupons-couponcode-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The negotiable-carts/{cartId}/estimate-shipping-methods API from Adobe Suite — 1 operation(s) for negotiable-carts/{cartid}/estimate-shipping-methods.
  name: Adobe Suite Negotiable Carts/{cart Id}/estimate Shipping Methods API
  phrasing_intents:
  - id: PostV1NegotiablecartsCartIdEstimateshippingmethods
    intent: Estimate shipping for a negotiable quote cart
    question: What shipping methods are available for a B2B negotiable quote?
  phrasing_ops: 1
  slug: adobe-suite-negotiable-carts-cartid-estimate-shipping-methods-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The negotiable-carts/{cartId}/estimate-shipping-methods-by-address-id API from Adobe Suite — 1 operation(s) for negotiable-carts/{cartid}/estimate-shipping-methods-by-address-id.
  name: Adobe Suite Negotiable Carts/{cart Id}/estimate Shipping Methods By Address ID API
  phrasing_intents:
  - id: PostV1NegotiablecartsCartIdEstimateshippingmethodsbyaddressid
    intent: Estimate shipping for a negotiable quote cart
    question: How do I estimate shipping costs for a B2B negotiable quote using a saved address?
  phrasing_ops: 1
  slug: adobe-suite-negotiable-carts-cartid-estimate-shipping-methods-by-address-id-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The negotiable-carts/{cartId}/giftCards API from Adobe Suite — 1 operation(s) for negotiable-carts/{cartid}/giftcards.
  name: Adobe Suite Negotiable Carts/{cart Id}/gift Cards API
  phrasing_intents:
  - id: PostV1NegotiablecartsCartIdGiftCards
    intent: Apply a gift card to a negotiable quote
    question: How do I apply a gift card to a B2B negotiable quote?
  phrasing_ops: 1
  slug: adobe-suite-negotiable-carts-cartid-giftcards-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The negotiable-carts/{cartId}/giftCards/{giftCardCode} API from Adobe Suite — 1 operation(s) for negotiable-carts/{cartid}/giftcards/{giftcardcode}.
  name: Adobe Suite Negotiable Carts/{cart Id}/gift Cards/{gift Card Code} API
  phrasing_intents:
  - id: DeleteV1NegotiablecartsCartIdGiftCardsGiftCardCode
    intent: Remove a gift card from a negotiable quote cart
    question: How do I take a gift card off a B2B negotiable quote cart?
  phrasing_ops: 1
  slug: adobe-suite-negotiable-carts-cartid-giftcards-giftcardcode-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The negotiable-carts/{cartId}/payment-information API from Adobe Suite — 1 operation(s) for negotiable-carts/{cartid}/payment-information.
  name: Adobe Suite Negotiable Carts/{cart Id}/payment Information API
  phrasing_intents:
  - id: PostV1NegotiablecartsCartIdPaymentinformation
    intent: Set payment and place an order for a quote cart
    question: How do I place the order for a negotiated B2B quote?
  - id: GetV1NegotiablecartsCartIdPaymentinformation
    intent: Get payment information for a negotiable quote cart
    question: What payment methods are available for a B2B negotiable quote cart?
  phrasing_ops: 2
  slug: adobe-suite-negotiable-carts-cartid-payment-information-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The negotiable-carts/{cartId}/set-payment-information API from Adobe Suite — 1 operation(s) for negotiable-carts/{cartid}/set-payment-information.
  name: Adobe Suite Negotiable Carts/{cart Id}/set Payment Information API
  phrasing_intents:
  - id: PostV1NegotiablecartsCartIdSetpaymentinformation
    intent: Set payment for a negotiable quote cart
    question: Can a B2B buyer set the payment method on a negotiable quote cart?
  phrasing_ops: 1
  slug: adobe-suite-negotiable-carts-cartid-set-payment-information-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The negotiable-carts/{cartId}/shipping-information API from Adobe Suite — 1 operation(s) for negotiable-carts/{cartid}/shipping-information.
  name: Adobe Suite Negotiable Carts/{cart Id}/shipping Information API
  phrasing_intents:
  - id: PostV1NegotiablecartsCartIdShippinginformation
    intent: Set shipping info on a negotiable quote cart
    question: How do I set the shipping address and method on a B2B negotiable quote cart?
  phrasing_ops: 1
  slug: adobe-suite-negotiable-carts-cartid-shipping-information-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The negotiable-carts/{cartId}/totals API from Adobe Suite — 1 operation(s) for negotiable-carts/{cartid}/totals.
  name: Adobe Suite Negotiable Carts/{cart Id}/totals API
  phrasing_intents:
  - id: GetV1NegotiablecartsCartIdTotals
    intent: Get totals for a negotiable quote cart
    question: How do I see the totals of a B2B negotiable quote cart?
  phrasing_ops: 1
  slug: adobe-suite-negotiable-carts-cartid-totals-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Network infrastructure API from Adobe Suite — 2 operation(s) for network infrastructure.
  name: Adobe Suite Network infrastructure API
  phrasing_intents:
  - id: getNetworkInfrastructures
    intent: List a program's network infrastructures
    question: Which advanced networking configurations exist in my Cloud Manager program?
  - id: createNetworkInfrastructure
    intent: Create a network infrastructure
    question: How do I set up a dedicated egress IP or VPN for my AEM program?
  - id: getNetworkInfrastructure
    intent: Get a network infrastructure
    question: What is the status of a specific network infrastructure?
  - id: updateNetworkInfrastructure
    intent: Update a network infrastructure
    question: How do I change the connections or DNS of an existing network infrastructure?
  - id: deleteNetworkInfrastructure
    intent: Delete a network infrastructure
    question: Can I remove an advanced networking setup from a program?
  phrasing_ops: 5
  slug: adobe-suite-network-infrastructure-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Note API from Adobe Suite — 7 operation(s) for note.
  name: Adobe Suite Note API
  phrasing_intents:
  - id: getNote
    intent: Get one note or comment by ID
    question: How do I read a single Workfront comment when I have its ID?
  - id: editNote
    intent: Edit a note
    question: How do I change the text of a comment I already posted?
  - id: deleteNote
    intent: Delete a note
    question: How do I delete a comment I posted by mistake?
  - id: getNotes
    intent: Fetch several notes by ID
    question: Can I load a batch of comments in one request by their IDs?
  - id: editNotes
    intent: Bulk edit notes
    question: Can I update many comments in one bulk request?
  - id: addNotes
    intent: Post a new note or comment
    question: How do I add a comment to a task, issue or project?
  - id: deleteNotes
    intent: Bulk delete notes
    question: Can I delete several comments at once?
  - id: countNotes
    intent: Count notes
    question: How many comments exist in total?
  phrasing_ops: 12
  slug: adobe-suite-note-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Notes are textual annotations that you can add to certain tag resources, such as data elements, extensions, libraries, properties, rules, and rule components.
  name: Adobe Suite Notes API
  phrasing_intents:
  - id: retrieveNote
    intent: Get a single note
    question: How do I read one tags note if I have its ID?
  - id: listPropertyNotes
    intent: List the notes on a tags property
    question: What notes has my team left on this tags property?
  - id: createPropertyNote
    intent: Add a note to a tags property
    question: How do I leave a note on a whole tags property?
  - id: listDataElementNotes
    intent: List the notes on a data element
    question: Are there any notes explaining what this data element captures?
  - id: createNote
    intent: Add a note to a data element
    question: How do I annotate a data element with a note?
  - id: listSecretNotes
    intent: List the notes on a secret
    question: What notes are attached to this event forwarding secret?
  - id: createSecretNote
    intent: Add a note to a secret
    question: How do I record a note against a secret, like who owns it?
  - id: listExtensionNotes
    intent: List the notes on an extension
    question: What notes exist for this installed extension?
  phrasing_ops: 15
  slug: adobe-suite-notes-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Notetag API from Adobe Suite — 5 operation(s) for notetag.
  name: Adobe Suite Notetag API
  phrasing_intents:
  - id: getNoteTag
    intent: Get one note tag
    question: How do I look up a single note tag in Workfront?
  - id: getNoteTags
    intent: Fetch several note tags by ID
    question: Can I load multiple note tags at once by ID?
  - id: countNoteTags
    intent: Count note tags
    question: How many note tags match a filter?
  - id: searchNoteTags
    intent: Search note tags
    question: What's the way to search note tags by field value?
  - id: reportNoteTags
    intent: Run a report on note tags
    question: Can I get a grouped report of note tags?
  phrasing_ops: 5
  slug: adobe-suite-notetag-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Objectcategory API from Adobe Suite — 6 operation(s) for objectcategory.
  name: Adobe Suite Objectcategory API
  phrasing_intents:
  - id: getObjectCategory
    intent: Get one object-to-form attachment
    question: Which custom form is attached to an object according to a specific object category record?
  - id: getObjectCategorys
    intent: Fetch several object categories by ID
    question: Can I retrieve multiple object category records at once by ID?
  - id: countObjectCategorys
    intent: Count object categories
    question: How many custom form attachments exist across objects?
  - id: searchObjectCategorys
    intent: Search object categories
    question: Which objects have a particular custom form attached?
  - id: reportObjectCategorys
    intent: Run an aggregate report on object categories
    question: Can I get grouped counts of form attachments by object type?
  - id: getObjectCategoryGetForObject
    intent: List forms attached to a specific object
    question: Which custom forms are attached to a given project or task?
  phrasing_ops: 6
  slug: adobe-suite-objectcategory-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Perform OCR on a PDF File
  name: Adobe Suite OCR API
  phrasing_intents:
  - id: pdfoperations.ocr
    intent: Make a scanned PDF searchable with OCR
    question: Can I run OCR on a scanned PDF so the text becomes searchable?
  - id: pdfoperations.ocr.jobstatus
    intent: Check an OCR job
    question: Is my OCR job done?
  phrasing_ops: 2
  slug: adobe-suite-ocr-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Optask API from Adobe Suite — 36 operation(s) for optask.
  name: Adobe Suite Optask API
  phrasing_intents:
  - id: getOpTask
    intent: Get one Workfront issue by ID
    question: How do I fetch a single Workfront issue when I already know its ID?
  - id: editOpTask
    intent: Edit a single issue
    question: What call changes the fields on one specific issue?
  - id: deleteOpTask
    intent: Delete a single issue
    question: How do I delete one issue by its ID?
  - id: getOpTasks
    intent: Get several issues by their IDs
    question: Can I load a batch of issues in one request if I have a list of IDs?
  - id: editOpTasks
    intent: Bulk edit many issues at once
    question: How do I apply the same change to lots of issues in one request?
  - id: addOpTasks
    intent: Create or copy an issue
    question: How do I log a new issue in Adobe Workfront through the API?
  - id: deleteOpTasks
    intent: Bulk delete several issues
    question: Can I delete a whole list of issues in a single call?
  - id: countOpTasks
    intent: Count issues matching a filter
    question: How many issues match a given filter?
  phrasing_ops: 41
  slug: adobe-suite-optask-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Orchestrated campaigns API from Adobe Suite — 1 operation(s) for orchestrated campaigns.
  name: Adobe Suite Orchestrated campaigns API
  phrasing_intents:
  - id: triggerOrchestratedCampaign
    intent: Trigger an orchestrated campaign
    question: How do I fire an orchestrated campaign that's set to be triggered by a signal?
  phrasing_ops: 1
  slug: adobe-suite-orchestrated-campaigns-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Customer Order Controller V 3
  name: Adobe Suite Orders API
  phrasing_intents:
  - id: createOrderPreviewUsingPOST
    intent: Preview an order before placing it
    question: Can I preview pricing for an order before actually placing it?
  - id: findOrdersUsingGET
    intent: Get a customer's order history (v2)
    question: How do I pull a customer's order history using the v2 API?
  - id: createOrderUsingPOST
    intent: Place an order for a customer (v2)
    question: How do I place an order for a customer with the v2 orders API?
  - id: findOrderUsingGET
    intent: Get an order's details (v2)
    question: How do I read one order's details using the v2 API?
  - id: cancelOrderUsingPATCH
    intent: Cancel a customer's order
    question: How do I cancel an order that was placed for a customer?
  - id: findOrdersUsingGET_1
    intent: Search a customer's order history (v3)
    question: Can I filter a customer's orders by date range or status?
  - id: createOrderUsingPOST_1
    intent: Place an order for a customer (v3)
    question: How do I create a new order or renewal with the v3 orders API?
  - id: findOrderUsingGET_1
    intent: Get an order's details (v3)
    question: How do I check the status of a single order on v3?
  phrasing_ops: 9
  slug: adobe-suite-orders-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Rotate and delete pages of a PDF File
  name: Adobe Suite Page Manipulation API
  phrasing_intents:
  - id: pdfoperations.pagemanipulation
    intent: Rotate or delete pages in a PDF
    question: How do I rotate certain pages of a PDF from portrait to landscape?
  - id: pdfoperations.pagemanipulation.jobstatus
    intent: Check a PDF page manipulation job
    question: Has my PDF rotate or delete-pages job finished?
  phrasing_ops: 2
  slug: adobe-suite-page-manipulation-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Parameter API from Adobe Suite — 13 operation(s) for parameter.
  name: Adobe Suite Parameter API
  phrasing_intents:
  - id: getParameter
    intent: Get a custom field parameter by ID
    question: What type, label and options does a particular custom field parameter have?
  - id: editParameter
    intent: Update a custom field parameter
    question: How do I change the label or settings of an existing custom field?
  - id: deleteParameter
    intent: Delete a custom field parameter
    question: How do I remove a custom field parameter we no longer use?
  - id: getParameters
    intent: Get several parameters by their IDs
    question: Can I pull the definitions of several custom fields in one request?
  - id: editParameters
    intent: Bulk-update several parameters
    question: Can I update many custom field parameters in one go?
  - id: addParameters
    intent: Create or copy a custom field parameter
    question: How do I create a new custom field in Workfront?
  - id: deleteParameters
    intent: Delete several parameters at once
    question: Can I delete a group of custom fields in one request?
  - id: countParameters
    intent: Count custom field parameters
    question: How many custom fields have been defined in our instance?
  phrasing_ops: 18
  slug: adobe-suite-parameter-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Parametergroup API from Adobe Suite — 5 operation(s) for parametergroup.
  name: Adobe Suite Parametergroup API
  phrasing_intents:
  - id: getParameterGroup
    intent: Get one parameter group
    question: How do I read a single custom field parameter group in Workfront?
  - id: editParameterGroup
    intent: Update a parameter group
    question: Can I rename or change an existing parameter group?
  - id: deleteParameterGroup
    intent: Delete a parameter group
    question: How do I delete a parameter group?
  - id: getParameterGroups
    intent: Fetch several parameter groups by ID
    question: Can I load a batch of parameter groups by their IDs?
  - id: editParameterGroups
    intent: Bulk update parameter groups
    question: How do I edit many parameter groups in one request?
  - id: addParameterGroups
    intent: Create a parameter group
    question: How do I create a new parameter group for custom fields?
  - id: deleteParameterGroups
    intent: Bulk delete parameter groups
    question: Can I delete several parameter groups at once?
  - id: countParameterGroups
    intent: Count parameter groups
    question: How many parameter groups match a filter?
  phrasing_ops: 10
  slug: adobe-suite-parametergroup-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Parameteroption API from Adobe Suite — 5 operation(s) for parameteroption.
  name: Adobe Suite Parameteroption API
  phrasing_intents:
  - id: getParameterOption
    intent: Get one custom field option
    question: How can I view a single choice defined for a Workfront custom field?
  - id: editParameterOption
    intent: Edit a single custom field option
    question: How do I rename or change one dropdown choice on a custom field?
  - id: deleteParameterOption
    intent: Delete one custom field option
    question: How do I remove a choice from a custom field?
  - id: getParameterOptions
    intent: Fetch several custom field options by ID
    question: Can I retrieve several parameter options in one call by ID?
  - id: editParameterOptions
    intent: Edit many custom field options at once
    question: Is there a way to update several custom field choices in one request?
  - id: addParameterOptions
    intent: Create a custom field option
    question: How do I add a new choice to a dropdown custom field?
  - id: deleteParameterOptions
    intent: Delete several custom field options at once
    question: Can I delete multiple custom field choices in one call?
  - id: countParameterOptions
    intent: Count custom field options
    question: How many parameter options are defined?
  phrasing_ops: 10
  slug: adobe-suite-parameteroption-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Pause API from Adobe Suite — 1 operation(s) for pause.
  name: Adobe Suite Pause API
  phrasing_intents:
  - id: pauseStart
    intent: Report that playback was paused
    question: How do I tell Media Edge that a viewer paused playback?
  phrasing_ops: 1
  slug: adobe-suite-pause-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Operation to create the tagged pdf and excel report for accessibility auto-tag use case.
  name: Adobe Suite PDF Accessibility Auto-Tag API
  phrasing_intents:
  - id: pdfoperations.autotag
    intent: Auto-tag a PDF for accessibility
    question: How do I automatically add accessibility tags to an untagged PDF?
  - id: pdfoperations.autotag.jobstatus
    intent: Check an accessibility auto-tag job
    question: How do I know when my PDF auto-tag job has finished?
  phrasing_ops: 2
  slug: adobe-suite-pdf-accessibility-auto-tag-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Accessibility Checker API will check PDF files to see if they meet the machine-verifiable requirements of PDF/UA and WCAG.
  name: Adobe Suite PDF Accessibility Checker API
  phrasing_intents:
  - id: pdfoperations.accessibilitychecker
    intent: Check a PDF for accessibility
    question: Does my PDF meet the machine-verifiable PDF/UA and WCAG requirements?
  - id: pdfoperations.accessibilitychecker.jobstatus
    intent: Poll a PDF accessibility check job
    question: Is my PDF accessibility check finished yet?
  phrasing_ops: 2
  slug: adobe-suite-pdf-accessibility-checker-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Create electronic seal on PDF documents like invoices, agreements etc using the digital certificate issued to the user by Trust Service Provider.
  name: Adobe Suite PDF Electronic Seal API
  phrasing_intents:
  - id: pdfoperations.electronicseal
    intent: Apply an electronic seal to a PDF
    question: How do I stamp an organization's electronic seal on a PDF?
  - id: pdfoperations.electronicseal.jobstatus
    intent: Check an electronic seal job's status
    question: Has my PDF electronic seal job finished yet?
  phrasing_ops: 2
  slug: adobe-suite-pdf-electronic-seal-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Extract basic information about a PDF document.
  name: Adobe Suite PDF Properties API
  phrasing_intents:
  - id: pdfoperations.pdfproperties
    intent: Extract basic properties of a PDF
    question: How can I find out a PDF's page count and PDF version?
  - id: pdfoperations.pdfproperties.jobstatus
    intent: Check the status of a PDF properties job
    question: Is my PDF properties extraction job done yet?
  phrasing_ops: 2
  slug: adobe-suite-pdf-properties-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Convert a PDF File to image files
  name: Adobe Suite PDF To Images API
  phrasing_intents:
  - id: pdfoperations.pdftoimages
    intent: Convert a PDF into page images
    question: Can I turn each page of a PDF into a separate image file?
  - id: pdfoperations.pdftoimages.jobstatus
    intent: Check a PDF to images job's status
    question: Has my PDF to image conversion finished?
  phrasing_ops: 2
  slug: adobe-suite-pdf-to-images-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Extract content from PDF documents and output it in a well-formatted LLM-friendly Markdown text, along with tables and figures
  name: Adobe Suite PDF To Markdown API
  phrasing_intents:
  - id: pdfoperations.pdftomarkdown
    intent: Convert a PDF into Markdown
    question: How do I extract a PDF's text and tables into Markdown?
  - id: pdfoperations.pdftomarkdown.jobstatus
    intent: Check a PDF to Markdown job
    question: Is my PDF to Markdown conversion done yet?
  phrasing_ops: 2
  slug: adobe-suite-pdf-to-markdown-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: PDF Watermark API will add a watermark in PDF document.
  name: Adobe Suite PDF Watermark API
  phrasing_intents:
  - id: pdfoperations.addwatermark
    intent: Add a watermark to a PDF
    question: How do I stamp a watermark onto pages of a PDF using Adobe PDF Services?
  - id: pdfoperations.addwatermark.jobstatus
    intent: Check the status of a watermark job
    question: How do I know when my PDF watermark job has finished?
  phrasing_ops: 2
  slug: adobe-suite-pdf-watermark-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Photoshop API from Adobe Suite — 17 operation(s) for photoshop.
  name: Adobe Suite Photoshop API
  phrasing_intents:
  - id: cutout
    intent: Remove the background from an image
    question: How do I remove the background from a product photo automatically?
  - id: mask
    intent: Generate a subject mask for an image
    question: Can I get a black and white mask of the main subject instead of a cutout?
  - id: icstatus
    intent: Check a background removal or mask job
    question: Is my remove-background job finished yet?
  - id: renditionCreate
    intent: Render a PSD to other image formats
    question: Can I convert a PSD into JPEG or PNG renditions?
  - id: actionJSON
    intent: Play back Photoshop actions in actionJSON
    question: Can I run Photoshop actions described as actionJSON instead of an .atn file?
  - id: actionJsonCreate
    intent: Convert an .atn action file to actionJSON
    question: How can I turn my recorded .atn action file into actionJSON?
  - id: smartObject
    intent: Replace a smart object in a PSD
    question: Can I swap the embedded smart object in a PSD mockup with a new image?
  - id: photoshopActions
    intent: Run Photoshop .atn actions on an image
    question: Can I apply my recorded Photoshop actions file to images in the cloud?
  phrasing_ops: 17
  slug: adobe-suite-photoshop-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Photoshop APIs for image processing operations
  name: Adobe Suite Photoshop APIs API
  phrasing_intents:
  - id: autoCrop
    intent: Smart-crop an image and detect subjects
    question: How do I automatically crop an image around its subject?
  - id: createArtboard
    intent: Combine images into an artboard document
    question: How do I lay several images out as artboards in one Photoshop document?
  - id: createComposite
    intent: Create or edit a layered composite
    question: How do I build a composite PSD by adding or editing layers?
  - id: edit
    intent: Apply adjustments to an image
    question: How do I apply image adjustments like exposure or color changes via the Photoshop API?
  - id: executeActions
    intent: Run Photoshop actions or scripts on an image
    question: Can I run a recorded Photoshop action or script against an image in the cloud?
  - id: generateManifest
    intent: Get a PSD's layer manifest
    question: How do I read the layer structure of a PSD file?
  phrasing_ops: 6
  slug: adobe-suite-photoshop-apis-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Ping API from Adobe Suite — 1 operation(s) for ping.
  name: Adobe Suite Ping API
  phrasing_intents:
  - id: ping
    intent: Send a playback ping event
    question: How often do I need to send ping events during main content playback?
  phrasing_ops: 1
  slug: adobe-suite-ping-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Pipeline Execution API from Adobe Suite — 8 operation(s) for pipeline execution.
  name: Adobe Suite Pipeline Execution API
  phrasing_intents:
  - id: getCurrentExecution
    intent: Get a pipeline's current execution
    question: Is my Cloud Manager pipeline running right now?
  - id: startPipeline
    intent: Start a pipeline execution
    question: How do I kick off a Cloud Manager pipeline run?
  - id: getExecution
    intent: Get a specific pipeline execution
    question: What was the outcome of a past pipeline run?
  - id: stepState
    intent: Get the state of a pipeline step
    question: What state is a particular step of a pipeline run in?
  - id: advancePipelineExecution
    intent: Advance a paused pipeline step
    question: My pipeline is paused waiting for approval, how do I let it continue?
  - id: cancelPipelineExecutionStep
    intent: Cancel a running pipeline execution
    question: How do I stop a Cloud Manager pipeline run that is in progress?
  - id: getStepLogs
    intent: Get logs for a pipeline step
    question: Where can I read the build logs for a failed pipeline step?
  - id: stepMetric
    intent: Get quality metrics for a pipeline step
    question: What code quality or test metrics did a pipeline step report?
  phrasing_ops: 9
  slug: adobe-suite-pipeline-execution-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Pipelines API from Adobe Suite — 3 operation(s) for pipelines.
  name: Adobe Suite Pipelines API
  phrasing_intents:
  - id: getPipelines
    intent: List a program's pipelines
    question: Which Cloud Manager pipelines can I access in a program?
  - id: getPipeline
    intent: Get one pipeline
    question: How do I look up the configuration of a single pipeline?
  - id: deletePipeline
    intent: Delete a pipeline and its data
    question: How do I delete a pipeline I no longer use?
  - id: patchPipeline
    intent: Update a pipeline's phases
    question: How do I change the phases of an existing pipeline?
  - id: invalidateCache
    intent: Clear a pipeline's build cache
    question: How do I reset a pipeline's cached artifacts?
  phrasing_ops: 5
  slug: adobe-suite-pipelines-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Play API from Adobe Suite — 1 operation(s) for play.
  name: Adobe Suite Play API
  phrasing_intents:
  - id: play
    intent: Report a media play event
    question: What event does Media Edge expect when the video starts or resumes playing?
  phrasing_ops: 1
  slug: adobe-suite-play-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Data usage policies are rules that describe the kinds of marketing actions that are allowed or not allowed to be performed on data within Adobe Experience Platform.
  name: Adobe Suite Policies API
  phrasing_intents:
  - id: listCorePolicies
    intent: List Adobe-defined core data usage policies
    question: Which built-in data governance policies does Adobe Experience Platform ship with?
  - id: retrieveCorePolicy
    intent: Get one core data usage policy
    question: What exactly does a particular Adobe core policy deny?
  - id: listCustomPolicies
    intent: List our custom data usage policies
    question: Which custom governance policies has our organization defined?
  - id: createCustomPolicy
    intent: Create a custom data usage policy
    question: How do I create my own data usage policy that denies a marketing action on labeled data?
  - id: retrieveCustomPolicy
    intent: Get one custom data usage policy
    question: How do I view the rules of one of our custom policies?
  - id: updateCustomPolicy
    intent: Replace a custom data usage policy
    question: Can I overwrite a custom policy with a completely new definition?
  - id: deleteCustomPolicy
    intent: Delete a custom data usage policy
    question: How do I delete a custom governance policy we no longer need?
  - id: patchCustomPolicy
    intent: Change individual fields on a custom policy
    question: Can I just flip a custom policy's status to enabled without resending the whole thing?
  phrasing_ops: 8
  slug: adobe-suite-policies-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The policy evaluation endpoints allow you to test a marketing action against specific labels or against datasets and fields to check for policy violations.
  name: Adobe Suite Policy evaluation API
  phrasing_intents:
  - id: evaluateCoreMarketingActionUsingLabels
    intent: Test a core marketing action against labels
    question: Would a core marketing action violate policy on data carrying certain usage labels?
  - id: evaluateCoreMarketingActionUsingDatasets
    intent: Test a core marketing action against datasets
    question: Can I use a core marketing action on these actual datasets or fields without breaking a policy?
  - id: evaluateCustomMarketingActionUsingLabels
    intent: Test a custom marketing action against labels
    question: Does a marketing action my org defined itself conflict with data usage labels?
  - id: evaluateCustomMarketingActionUsingDatasets
    intent: Test a custom marketing action against datasets
    question: Can our own custom marketing action run on a specific dataset without a policy violation?
  - id: bulkEval
    intent: Run many policy evaluations in one call
    question: Can I evaluate several marketing actions against data usage policies in a single request?
  phrasing_ops: 5
  slug: adobe-suite-policy-evaluation-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Portalsection API from Adobe Suite — 20 operation(s) for portalsection.
  name: Adobe Suite Portalsection API
  phrasing_intents:
  - id: getPortalSection
    intent: Get one Workfront report (portal section)
    question: How do I pull up a single Workfront report by its ID?
  - id: editPortalSection
    intent: Update one Workfront report
    question: Can I change the settings of one existing portal section report?
  - id: deletePortalSection
    intent: Delete one Workfront report
    question: How do I remove a single portal section report from Workfront?
  - id: getPortalSections
    intent: Get several Workfront reports by ID
    question: Can I load several portal section reports at once when I already know their IDs?
  - id: editPortalSections
    intent: Update many Workfront reports at once
    question: Can I apply edits to a batch of portal section reports in one request?
  - id: addPortalSections
    intent: Create or copy a Workfront report
    question: How do I create a new portal section report in Workfront?
  - id: deletePortalSections
    intent: Delete several Workfront reports
    question: Can I remove multiple portal section reports in a single call?
  - id: countPortalSections
    intent: Count Workfront reports
    question: How many portal section reports exist in our Workfront instance?
  phrasing_ops: 25
  slug: adobe-suite-portalsection-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Portalsectionlastviewer API from Adobe Suite — 5 operation(s) for portalsectionlastviewer.
  name: Adobe Suite Portalsectionlastviewer API
  phrasing_intents:
  - id: getPortalSectionLastViewer
    intent: Look up one report last-viewer record
    question: How do I see who last viewed a particular portal section or report?
  - id: getPortalSectionLastViewers
    intent: Fetch several last-viewer records by ID
    question: Can I load multiple portal section last-viewer records at once?
  - id: countPortalSectionLastViewers
    intent: Count portal section last-viewer records
    question: How many last-viewed records are there for portal sections?
  - id: searchPortalSectionLastViewers
    intent: Search portal section last-viewer records
    question: Which reports or dashboards has a given user viewed most recently?
  - id: reportPortalSectionLastViewers
    intent: Run a report on portal section views
    question: Can I get grouped totals of who viewed which portal sections?
  phrasing_ops: 5
  slug: adobe-suite-portalsectionlastviewer-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Portalsectionstatisticinfo API from Adobe Suite — 5 operation(s) for portalsectionstatisticinfo.
  name: Adobe Suite Portalsectionstatisticinfo API
  phrasing_intents:
  - id: getPortalSectionStatisticInfo
    intent: Get portal section statistics by ID
    question: What usage statistics are recorded for a particular Workfront report or dashboard section?
  - id: getPortalSectionStatisticInfos
    intent: Get several portal section statistics by ID
    question: Can I load statistics for several portal sections in one request?
  - id: countPortalSectionStatisticInfos
    intent: Count portal section statistic records
    question: How many portal section statistic records exist?
  - id: searchPortalSectionStatisticInfos
    intent: Search portal section statistics
    question: How do I find usage statistics for reports run in a certain period?
  - id: reportPortalSectionStatisticInfos
    intent: Run a report over portal section statistics
    question: Can I get aggregated usage figures grouped by report or dashboard section?
  phrasing_ops: 5
  slug: adobe-suite-portalsectionstatisticinfo-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Portaltab API from Adobe Suite — 15 operation(s) for portaltab.
  name: Adobe Suite Portaltab API
  phrasing_intents:
  - id: getPortalTab
    intent: Get a single portal tab
    question: How do I look up one Workfront portal tab by its ID?
  - id: editPortalTab
    intent: Edit one portal tab
    question: Can I change the settings of one specific portal tab?
  - id: deletePortalTab
    intent: Delete one portal tab
    question: How do I remove a single portal tab?
  - id: getPortalTabs
    intent: Get several portal tabs by ID
    question: Can I fetch several portal tabs at once by passing a list of IDs?
  - id: editPortalTabs
    intent: Edit many portal tabs at once
    question: Can I apply edits to a batch of portal tabs in a single request?
  - id: addPortalTabs
    intent: Create or copy a portal tab
    question: How do I create a new portal tab?
  - id: deletePortalTabs
    intent: Delete many portal tabs at once
    question: Can I delete a whole list of portal tabs in one call?
  - id: countPortalTabs
    intent: Count portal tabs
    question: How many portal tabs exist in our Workfront instance?
  phrasing_ops: 20
  slug: adobe-suite-portaltab-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Portfolio API from Adobe Suite — 16 operation(s) for portfolio.
  name: Adobe Suite Portfolio API
  phrasing_intents:
  - id: getPortfolio
    intent: Look up one portfolio
    question: What's the call to pull up a single Workfront portfolio by its ID?
  - id: editPortfolio
    intent: Update one portfolio
    question: How do I change the details of an existing portfolio?
  - id: deletePortfolio
    intent: Delete one portfolio
    question: Can I remove a single portfolio I no longer need?
  - id: getPortfolios
    intent: Fetch several portfolios by ID
    question: Can I retrieve a batch of portfolios in one call when I know their IDs?
  - id: editPortfolios
    intent: Update many portfolios at once
    question: How do I bulk edit several portfolios in a single request?
  - id: addPortfolios
    intent: Create a portfolio
    question: How do I set up a new portfolio to group my programs and projects?
  - id: deletePortfolios
    intent: Delete many portfolios at once
    question: Can I bulk delete several portfolios by listing their IDs?
  - id: countPortfolios
    intent: Count portfolios
    question: How many portfolios match a given filter?
  phrasing_ops: 21
  slug: adobe-suite-portfolio-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Retrieve the first 100 rows of CSV or Parquet files.
  name: Adobe Suite Preview API
  phrasing_intents:
  - id: retrieveDatasetPreview
    intent: Preview the first rows of a dataset
    question: Can I peek at the first 100 rows of a dataset's files?
  phrasing_ops: 1
  slug: adobe-suite-preview-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Previews provide paginated lists of qualifying profiles for a segment definition. More information about using this set of endpoints can be found in the [previews and estimates endpoint guide](https:/
  name: Adobe Suite Previews API
  phrasing_intents:
  - id: createPreview
    intent: Start a segment preview job
    question: How do I preview which profiles a PQL expression would qualify?
  - id: retrievePreview
    intent: Get the results of a preview job
    question: Where can I see the sample profiles returned by my preview job?
  - id: deletePreview
    intent: Cancel or delete a preview job
    question: Can I cancel a preview job that is still running?
  phrasing_ops: 3
  slug: adobe-suite-previews-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Define pricing scopes to manage product prices across different customer tiers and markets. Price books support a hierarchical model, allowing up to three levels of nested child price books under each
  name: Adobe Suite Price Books API
  phrasing_intents:
  - id: createPriceBooks
    intent: Create or replace price books
    question: How do I set up a base price book with its currency for my Commerce catalog?
  - id: updatePriceBooks
    intent: Update existing price books
    question: How do I rename a price book that already exists?
  - id: deletePriceBooks
    intent: Delete price books and their pricing
    question: What happens to child price books when I delete their parent?
  phrasing_ops: 3
  slug: adobe-suite-price-books-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Manage product SKU prices across different price books and customer tiers. Define regular prices, discounts, and tiered pricing for specific customer segments or markets by specifying a price book id.
  name: Adobe Suite Prices API
  phrasing_intents:
  - id: createPrices
    intent: Create or replace product prices
    question: How do I load regular prices for my catalog SKUs into Adobe Commerce?
  - id: updatePrices
    intent: Update existing product prices
    question: Can I change just the discount on a price without resending everything?
  - id: deletePrices
    intent: Delete product prices
    question: How do I remove prices for SKUs I no longer sell?
  phrasing_ops: 3
  slug: adobe-suite-prices-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Privacy jobs process customer privacy requests, including access/delete and opt-out requests. Each privacy job is tracked under a specific regulation.
  name: Adobe Suite Privacy jobs API
  phrasing_intents:
  - id: listPrivacyJobs
    intent: List privacy jobs for a regulation
    question: Which GDPR or CCPA privacy requests have we submitted?
  - id: createPrivacyJob
    intent: Submit a privacy access or delete request
    question: How do I submit a customer's data access or deletion request?
  - id: retrievePrivacyJob
    intent: Get a privacy job's status
    question: Has a specific privacy request finished processing?
  - id: retrievePrivacyJobContent
    intent: Download a customer's access request data
    question: Where do I download the data gathered for a customer's access request?
  phrasing_ops: 4
  slug: adobe-suite-privacy-jobs-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Product Layers API from Adobe Suite — 2 operation(s) for product layers.
  name: Adobe Suite Product Layers API
  phrasing_intents:
  - id: createProductLayers
    intent: Create or replace product layers
    question: How do I override product attributes for a specific locale or market?
  - id: deleteProductLayers
    intent: Delete product layers
    question: How do I remove an expired promotional layer while keeping the base product?
  phrasing_ops: 2
  slug: adobe-suite-product-layers-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Manage product attribute definitions including display settings, search behavior, and filtering capabilities. These settings control how product attributes appear and function throughout the storefron
  name: Adobe Suite Product Metadata API
  phrasing_intents:
  - id: createProductMetadata
    intent: Create product attribute metadata
    question: What product attribute metadata do I have to define before loading products into the Commerce catalog?
  - id: updateProductMetadata
    intent: Update existing product attribute metadata
    question: How do I change metadata for a product attribute that already exists?
  - id: deleteProductMetadata
    intent: Delete product attribute metadata
    question: How do I remove product attribute metadata from the catalog?
  phrasing_ops: 3
  slug: adobe-suite-productmetadata-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Create and manage product data including simple products, configurable products, and their variants. Control product visibility, attributes, images, and pricing
  name: Adobe Suite Products API
  phrasing_intents:
  - id: createProducts
    intent: Create or replace catalog products
    question: How do I load new products, including configurable ones, into the Commerce catalog service?
  - id: updateProducts
    intent: Update fields on existing catalog products
    question: Can I change just some attributes of products that are already in the catalog?
  - id: deleteProducts
    intent: Delete catalog products by SKU
    question: How do I remove discontinued products from the catalog service?
  phrasing_ops: 3
  slug: adobe-suite-products-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The products-render-info API from Adobe Suite — 1 operation(s) for products-render-info.
  name: Adobe Suite Products Render Info API
  phrasing_intents:
  - id: GetV1Productsrenderinfo
    intent: Get display-ready product info for a store
    question: How do I get formatted prices, names and stock status for products in a store?
  phrasing_ops: 1
  slug: adobe-suite-products-render-info-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Preview the latest sample job showing how many profile fragments and merged profiles are in the Profile store, as well as listing profile distribution by dataset and by identity namespace. For more in
  name: Adobe Suite Profile preview API
  phrasing_intents:
  - id: previewSampleStatus
    intent: Check the last profile sample job
    question: When did the last successful profile sample job run?
  - id: profileDatasetReport
    intent: Report profile counts by dataset
    question: Which datasets contribute the most profiles?
  - id: profileNamespaceReport
    intent: Report profile counts by identity namespace
    question: How are profiles distributed across identity namespaces like email or ECID?
  phrasing_ops: 3
  slug: adobe-suite-profile-preview-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'Profile System Jobs allow you to delete profile fragments for a given dataset or batch. For more information on using this set of endpoints, please read the [profile system jobs endpoint guide](https:'
  name: Adobe Suite Profile System Jobs API
  phrasing_intents:
  - id: listDeleteRequests
    intent: List profile data delete requests
    question: What profile delete requests have been submitted in my sandbox?
  - id: createDeleteRequest
    intent: Delete all profile data for a dataset
    question: How do I wipe a dataset's data out of Real-Time Customer Profile?
  - id: retrieveDeleteRequest
    intent: Check one profile delete request
    question: Has my profile delete request completed?
  - id: deleteDeleteRequest
    intent: Remove a profile delete request record
    question: Can I remove a delete request from the profile system jobs list?
  phrasing_ops: 4
  slug: adobe-suite-profile-system-jobs-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Collect specific data for Platform profile(s)
  name: Adobe Suite Profile updates API
  phrasing_intents:
  - id: postV1PrivacySetConsent
    intent: Set a visitor's marketing consent
    question: How do I record a visitor's opt-in or opt-out for marketing?
  phrasing_ops: 1
  slug: adobe-suite-profile-updates-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: A profile represents a tags user. Platform does not maintain its own database of users and permissions, and instead relies on Adobe IDs managed by Adobe’s company-wide Identity Management System (IMS)
  name: Adobe Suite Profiles API
  phrasing_intents:
  - id: retrieveUserDetails
    intent: Get the logged-in user's profile
    question: Who am I logged in as in the Reactor tags API?
  phrasing_ops: 1
  slug: adobe-suite-profiles-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Program API from Adobe Suite — 17 operation(s) for program.
  name: Adobe Suite Program API
  phrasing_intents:
  - id: getProgram
    intent: Look up one Workfront program
    question: How do I pull up a single program in Workfront by its ID?
  - id: editProgram
    intent: Update one program
    question: Can I change the details of an existing program by its ID?
  - id: deleteProgram
    intent: Delete one program
    question: How do I delete a single program?
  - id: getPrograms
    intent: Fetch several programs by their IDs
    question: Can I load a batch of programs at once if I already know their IDs?
  - id: editPrograms
    intent: Update many programs in one request
    question: Is there a bulk edit for programs?
  - id: addPrograms
    intent: Create a program
    question: How do I set up a new program to group projects?
  - id: deletePrograms
    intent: Delete many programs at once
    question: Can I delete a list of programs in one request?
  - id: countPrograms
    intent: Count programs matching filters
    question: How many programs do we have in Workfront?
  phrasing_ops: 22
  slug: adobe-suite-program-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Programs API from Adobe Suite — 5 operation(s) for programs.
  name: Adobe Suite Programs API
  phrasing_intents:
  - id: getPrograms
    intent: List programs (deprecated endpoint)
    question: Is there still an older endpoint that lists all my Cloud Manager programs?
  - id: getProgram
    intent: Get a program by ID
    question: How do I look up the details of one Adobe Cloud Manager program?
  - id: deleteProgram
    intent: Delete a program
    question: How do I delete a program I no longer need?
  - id: postFeedback
    intent: Submit feedback on a program
    question: How do I leave a rating and comment on a program?
  - id: getNewRelicSubAccountUserList
    intent: List a program's New Relic sub-account users
    question: Who has access to the New Relic sub-account for my program?
  - id: createDeleteNewRelicSubAccountUsers
    intent: Add or remove New Relic sub-account users
    question: How do I add someone to my program's New Relic sub-account?
  - id: getProgramsForTenant
    intent: List programs for a tenant
    question: How do I list every program defined for my tenant?
  - id: addProgram
    intent: Create a program for a tenant
    question: How do I create a new program for my tenant?
  phrasing_ops: 8
  slug: adobe-suite-programs-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Project API from Adobe Suite — 27 operation(s) for project.
  name: Adobe Suite Project API
  phrasing_intents:
  - id: getProject
    intent: Get one project by ID
    question: How do I look up a single Workfront project when I already know its ID?
  - id: editProject
    intent: Edit a single project
    question: How do I change the details of one existing project?
  - id: deleteProject
    intent: Delete one project
    question: How do I permanently remove a single project?
  - id: getProjects
    intent: Fetch several projects by their IDs
    question: Is there a way to pull several projects at once by a list of IDs?
  - id: editProjects
    intent: Bulk edit many projects at once
    question: Can I apply changes to many projects in a single bulk update?
  - id: addProjects
    intent: Create a new project or copy an existing one
    question: How do I create a brand new project?
  - id: deleteProjects
    intent: Bulk delete several projects
    question: Can I delete a whole batch of projects in one go?
  - id: countProjects
    intent: Count projects matching filters
    question: How many projects do we have right now?
  phrasing_ops: 32
  slug: adobe-suite-project-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Projects API from Adobe Suite — 3 operation(s) for projects.
  name: Adobe Suite Projects API
  phrasing_intents:
  - id: projects_getProject
    intent: Get an Analytics project's configuration
    question: How do I retrieve the configuration of one Analytics Workspace project?
  - id: projects_updateProject
    intent: Update an Analytics project
    question: How do I rename or change the definition of an existing Analytics project?
  - id: projects_deleteProject
    intent: Delete an Analytics project
    question: How do I delete an Analytics Workspace project?
  - id: projects_validateProject
    intent: Validate a project definition
    question: Can I check that a project definition is valid before saving it?
  - id: projects_getProjects
    intent: List a user's Analytics projects
    question: Which Analytics Workspace projects do I have access to?
  - id: projects_createProject
    intent: Create an Analytics project
    question: How do I create a new Analytics Workspace project through the API?
  phrasing_ops: 6
  slug: adobe-suite-projects-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Proof API from Adobe Suite — 1 operation(s) for proof.
  name: Adobe Suite Proof API
  phrasing_intents:
  - id: searchProofs
    intent: Search Workfront proofs
    question: How do I find proofs that match certain criteria?
  phrasing_ops: 1
  slug: adobe-suite-proof-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Proofaction API from Adobe Suite — 5 operation(s) for proofaction.
  name: Adobe Suite Proofaction API
  phrasing_intents:
  - id: getProofAction
    intent: Get one proof action
    question: How do I look up a single Workfront proof action by its ID?
  - id: getProofActions
    intent: Get several proof actions by ID
    question: Can I fetch a batch of proof actions when I have their IDs?
  - id: addProofActions
    intent: Create a proof action
    question: How do I record a new action taken on a proof?
  - id: countProofActions
    intent: Count proof actions
    question: How many proof actions have been recorded?
  - id: searchProofActions
    intent: Search proof actions
    question: What proof actions meet certain conditions?
  - id: reportProofActions
    intent: Run a report on proof actions
    question: Can I produce an aggregated report of proof actions?
  phrasing_ops: 6
  slug: adobe-suite-proofaction-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Proofapproval API from Adobe Suite — 5 operation(s) for proofapproval.
  name: Adobe Suite Proofapproval API
  phrasing_intents:
  - id: getProofApproval
    intent: Get a proof approval
    question: What's the decision recorded on a specific proof approval in Workfront?
  - id: getProofApprovals
    intent: Get several proof approvals by ID
    question: Can I load a batch of proof approvals by their IDs?
  - id: countProofApprovals
    intent: Count proof approvals
    question: How many proof approvals are there?
  - id: searchProofApprovals
    intent: Search proof approvals
    question: Which proof approvals match a set of filters?
  - id: reportProofApprovals
    intent: Run a report on proof approvals
    question: Can I get a grouped report of proof approvals?
  phrasing_ops: 5
  slug: adobe-suite-proofapproval-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'A property is a container that holds most of the other resources available within the Reactor API. The only resources that are not owned by a property are audit events, companies, extension packages, '
  name: Adobe Suite Properties API
  phrasing_intents:
  - id: listProperties
    intent: List a company's tag properties
    question: Which tag properties does my company have in Adobe Experience Platform Tags?
  - id: createProperty
    intent: Create a tag property for a company
    question: How do I set up a new tag property for a website under my company?
  - id: retrieveProperty
    intent: Get a tag property's details
    question: What settings does a specific tag property have?
  - id: deleteProperty
    intent: Delete a tag property
    question: Can I permanently remove a tag property I no longer use?
  - id: updateProperty
    intent: Update a tag property's settings
    question: How can I change the name or domains of an existing tag property?
  - id: retrievePropertyCompany
    intent: Find the company that owns a property
    question: Which company does a particular tag property belong to?
  - id: listCallbacks
    intent: List a property's callbacks
    question: What webhook callbacks are registered on my tag property?
  - id: createCallback
    intent: Register a callback on a property
    question: How do I get notified at my own URL when something changes in a tag property?
  phrasing_ops: 24
  slug: adobe-suite-properties-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Add encryption and/or restrict permissions on a PDF File
  name: Adobe Suite Protect PDF API
  phrasing_intents:
  - id: pdfoperations.protectpdf
    intent: Password-protect and restrict a PDF
    question: How do I put a password on a PDF with Adobe PDF Services?
  - id: pdfoperations.protectpdf.jobstatus
    intent: Check a protect-PDF job's status
    question: Is my PDF protection job finished yet?
  phrasing_ops: 2
  slug: adobe-suite-protect-pdf-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Public API from Adobe Suite — 6 operation(s) for public.
  name: Adobe Suite Public API
  phrasing_intents:
  - id: getPublicApiV1ApprovalsByAssetTypeByAssetId
    intent: Get the approval for an asset
    question: What approval is required on a given Workfront asset?
  - id: putPublicApiV1ApprovalsByAssetTypeByAssetIdStages
    intent: Create or update an asset approval
    question: How do I start an approval on an asset with a single stage?
  - id: putPublicApiV1ApprovalsByAssetTypeByAssetIdDecisions
    intent: Approve or reject an asset
    question: How do I record my approve or reject decision on an asset's approval stage?
  - id: putPublicApiV1ApprovalsByAssetTypeByAssetIdParticipants
    intent: Add approvers to an asset approval
    question: How do I add reviewers to an existing approval?
  - id: deletePublicApiV1ApprovalsByAssetTypeByAssetIdParticipants
    intent: Remove approvers from an asset approval
    question: How do I take someone off an approval as a reviewer?
  - id: putPublicApiV1ApprovalsByAssetTypeByAssetIdStagesByStageIdLock
    intent: Lock an approval stage
    question: How do I freeze an approval stage so nobody can make further decisions?
  - id: putPublicApiV1ApprovalsByAssetTypeByAssetIdStagesByStageIdUnlock
    intent: Unlock an approval stage
    question: How do I reopen a locked approval stage for decisions?
  phrasing_ops: 7
  slug: adobe-suite-public-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Externally verify the authenticity of the certificates to enhance trust in safeguarding sensitive information.
  name: Adobe Suite Public certificates API
  phrasing_intents:
  - id: retrieveCertificates
    intent: List public mTLS certificates for Adobe apps
    question: Where can I get Adobe's public certificates to verify mutual TLS connections?
  phrasing_ops: 1
  slug: adobe-suite-public-certificates-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The purchase-order-carts/{cartId}/payment-information API from Adobe Suite — 1 operation(s) for purchase-order-carts/{cartid}/payment-information.
  name: Adobe Suite Purchase Order Carts/{cart Id}/payment Information API
  phrasing_intents:
  - id: PostV1PurchaseordercartsCartIdPaymentinformation
    intent: Set payment and place a purchase order
    question: How do I set the payment method and place the order for a purchase order cart?
  - id: GetV1PurchaseordercartsCartIdPaymentinformation
    intent: Get payment details for a purchase order cart
    question: What payment methods and totals apply to my B2B purchase order cart?
  phrasing_ops: 2
  slug: adobe-suite-purchase-order-carts-cartid-payment-information-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The purchase-order-carts/{cartId}/set-payment-information API from Adobe Suite — 1 operation(s) for purchase-order-carts/{cartid}/set-payment-information.
  name: Adobe Suite Purchase Order Carts/{cart Id}/set Payment Information API
  phrasing_intents:
  - id: PostV1PurchaseordercartsCartIdSetpaymentinformation
    intent: Set payment information on a purchase order cart
    question: Which call sets the payment method on a purchase order cart?
  phrasing_ops: 1
  slug: adobe-suite-purchase-order-carts-cartid-set-payment-information-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The queries endpoint uses standard SQL to query data held in Adobe Experience Platform. For example, you can join any number of datasets in the data lake and capture the results as a new dataset.
  name: Adobe Suite Queries API
  phrasing_intents:
  - id: listQueries
    intent: List Query Service queries
    question: How do I list the SQL queries run in my Experience Platform org?
  - id: createQuery
    intent: Run a new SQL query
    question: How do I run a SQL query against my data lake through Query Service?
  - id: retrieveQuery
    intent: Get a query's details and state
    question: How do I check the status of a query I submitted?
  - id: cancelQuery
    intent: Cancel or soft-delete a query
    question: How do I stop a long-running SQL query?
  phrasing_ops: 4
  slug: adobe-suite-queries-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Query templates let you create, store, and execute any query as an ad hoc or scheduled service.
  name: Adobe Suite Query Templates API
  phrasing_intents:
  - id: listQueryTemplates
    intent: List saved query templates
    question: Which query templates have we saved in Query Service?
  - id: createQueryTemplate
    intent: Save a SQL query as a template
    question: How do I save a SQL statement as a reusable query template?
  - id: retrieveQueryTemplateCount
    intent: Count query templates
    question: How many query templates exist in this sandbox?
  - id: retrieveQueryTemplate
    intent: Retrieve a query template
    question: How do I see the SQL stored in a query template?
  - id: updateQueryTemplate
    intent: Update a query template
    question: Can I change the SQL in an existing query template?
  - id: deleteQueryTemplate
    intent: Delete a query template
    question: How do I remove a saved query template?
  phrasing_ops: 6
  slug: adobe-suite-query-templates-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Queuedef API from Adobe Suite — 8 operation(s) for queuedef.
  name: Adobe Suite Queuedef API
  phrasing_intents:
  - id: getQueueDef
    intent: Look up one request queue definition
    question: How do I read the setup of one Workfront request queue?
  - id: getQueueDefs
    intent: Fetch several queue definitions by ID
    question: Can I retrieve multiple request queue definitions by their IDs?
  - id: countQueueDefs
    intent: Count request queue definitions
    question: How many request queues match a filter?
  - id: searchQueueDefs
    intent: Search request queue definitions
    question: How do I find request queues by project or visibility?
  - id: reportQueueDefs
    intent: Run an aggregate report on request queues
    question: Can I get grouped totals of request queue definitions?
  - id: queueDefGetQueueDefTree
    intent: Get the topic tree of a request queue
    question: Can I see the full hierarchy of topics and groups in a request queue?
  - id: queueDefSearchByPath
    intent: Find request queues by path name
    question: Can I look up a queue by typing part of its path name?
  - id: getQueueDefQueueTopics
    intent: List topics defined in request queues
    question: Which topics are available in my request queues?
  phrasing_ops: 8
  slug: adobe-suite-queuedef-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Queuetopic API from Adobe Suite — 6 operation(s) for queuetopic.
  name: Adobe Suite Queuetopic API
  phrasing_intents:
  - id: getQueueTopic
    intent: Get one request queue topic
    question: How do I read a Workfront request queue topic by ID?
  - id: editQueueTopic
    intent: Edit a single queue topic
    question: What call changes one request queue topic?
  - id: deleteQueueTopic
    intent: Delete a single queue topic
    question: How do I remove one topic from a request queue?
  - id: getQueueTopics
    intent: Get several queue topics by ID
    question: Can I load a list of queue topics by their IDs in one request?
  - id: editQueueTopics
    intent: Bulk edit queue topics
    question: How do I update several queue topics together?
  - id: addQueueTopics
    intent: Create a request queue topic
    question: How do I add a new topic to a request queue?
  - id: deleteQueueTopics
    intent: Bulk delete queue topics
    question: Can I delete several queue topics in one request?
  - id: countQueueTopics
    intent: Count queue topics
    question: How many queue topics match a filter?
  phrasing_ops: 11
  slug: adobe-suite-queuetopic-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Queuetopicgroup API from Adobe Suite — 6 operation(s) for queuetopicgroup.
  name: Adobe Suite Queuetopicgroup API
  phrasing_intents:
  - id: getQueueTopicGroup
    intent: Look up one request queue topic group
    question: How do I get the details of one queue topic group in Workfront?
  - id: editQueueTopicGroup
    intent: Update one queue topic group
    question: Can I rename or change a single queue topic group?
  - id: deleteQueueTopicGroup
    intent: Delete one queue topic group
    question: How do I remove a topic group from a request queue?
  - id: getQueueTopicGroups
    intent: Fetch several queue topic groups by ID
    question: Can I retrieve multiple topic groups in one call when I know their IDs?
  - id: editQueueTopicGroups
    intent: Update many queue topic groups at once
    question: Is there a bulk edit for request queue topic groups?
  - id: addQueueTopicGroups
    intent: Create a queue topic group
    question: How do I add a new topic group to organize a request queue?
  - id: deleteQueueTopicGroups
    intent: Delete many queue topic groups
    question: Can I bulk delete topic groups from request queues?
  - id: countQueueTopicGroups
    intent: Count queue topic groups
    question: How many queue topic groups match my filter?
  phrasing_ops: 11
  slug: adobe-suite-queuetopicgroup-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The quick-checkout/account-details API from Adobe Suite — 1 operation(s) for quick-checkout/account-details.
  name: Adobe Suite Quick Checkout/account Details API
  phrasing_intents:
  - id: PostV1QuickcheckoutAccountdetails
    intent: Retrieve quick checkout account details
    question: How can I get a shopper's saved account information for quick checkout?
  phrasing_ops: 1
  slug: adobe-suite-quick-checkout-account-details-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The quick-checkout/has-account API from Adobe Suite — 1 operation(s) for quick-checkout/has-account.
  name: Adobe Suite Quick Checkout/has Account API
  phrasing_intents:
  - id: PostV1QuickcheckoutHasaccount
    intent: Check if a shopper has a Bolt account
    question: Does this shopper's email already have a Bolt account?
  phrasing_ops: 1
  slug: adobe-suite-quick-checkout-has-account-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The quick-checkout/storefront/has-account API from Adobe Suite — 1 operation(s) for quick-checkout/storefront/has-account.
  name: Adobe Suite Quick Checkout/storefront/has Account API
  phrasing_intents:
  - id: PostV1QuickcheckoutStorefrontHasaccount
    intent: Check if an email has a storefront account
    question: How do I tell whether a shopper's email already has an account in the store?
  phrasing_ops: 1
  slug: adobe-suite-quick-checkout-storefront-has-account-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Use the `/quota` endpoint in the Data Hygiene API to monitor your Advanced Data Lifecycle Management usage against your organization’s quota limits for each job type.
  name: Adobe Suite Quota API
  phrasing_intents:
  - id: listQuotas
    intent: Check data hygiene quota usage
    question: How much of my data hygiene quota have I used this month?
  phrasing_ops: 1
  slug: adobe-suite-quota-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Rapid Development Environments API from Adobe Suite — 1 operation(s) for rapid development environments.
  name: Adobe Suite Rapid Development Environments API
  phrasing_intents:
  - id: resetRde
    intent: Reset a Rapid Development Environment
    question: How do I reset my AEM Rapid Development Environment to a clean state?
  phrasing_ops: 1
  slug: adobe-suite-rapid-development-environments-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Rate API from Adobe Suite — 11 operation(s) for rate.
  name: Adobe Suite Rate API
  phrasing_intents:
  - id: getRate
    intent: Get a single billing rate
    question: How do I look up one billing rate by its ID?
  - id: editRate
    intent: Edit a single billing rate
    question: How can I change the value of one existing rate?
  - id: deleteRate
    intent: Delete a single billing rate
    question: How do I delete one rate that is no longer valid?
  - id: getRates
    intent: Get several rates by ID at once
    question: Can I fetch multiple rates in one call by listing their IDs?
  - id: editRates
    intent: Edit many rates in one request
    question: Is there a bulk edit for rates?
  - id: addRates
    intent: Create a billing rate
    question: How do I add a new billing rate record?
  - id: deleteRates
    intent: Delete several rates at once
    question: Can I bulk delete rates by passing a list of IDs?
  - id: countRates
    intent: Count rates matching a filter
    question: How many rate records do we have?
  phrasing_ops: 16
  slug: adobe-suite-rate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Recent API from Adobe Suite — 6 operation(s) for recent.
  name: Adobe Suite Recent API
  phrasing_intents:
  - id: getRecent
    intent: Get one recent-items entry by ID
    question: How do I look up a single entry in my recently viewed items?
  - id: deleteRecent
    intent: Remove an entry from recent items
    question: How do I clear one item out of my recents list?
  - id: getRecents
    intent: Fetch several recent-items entries by ID
    question: Can I load several recently viewed entries at once by ID?
  - id: addRecents
    intent: Add an entry to recent items
    question: How do I record an object in the recently viewed list?
  - id: deleteRecents
    intent: Bulk remove recent-items entries
    question: Can I clear several entries from my recents at once?
  - id: countRecents
    intent: Count recent-items entries
    question: How many items are in my recently viewed list?
  - id: searchRecents
    intent: Search recently viewed items
    question: How do I find recently viewed items of a certain type?
  - id: reportRecents
    intent: Run an aggregated report on recent items
    question: Can I get grouped report data about recently viewed items?
  phrasing_ops: 9
  slug: adobe-suite-recent-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Use the `/workorder` endpoint in the Data Hygiene API to programmatically manage record delete requests in Adobe Experience Platform. Specify primary identities to target and remove the relevant recor
  name: Adobe Suite Record Delete (Work order) API
  phrasing_intents:
  - id: getWorkOrders
    intent: List data hygiene work orders
    question: Which record delete requests has our organization submitted?
  - id: createWorkOrder
    intent: Submit a record delete work order
    question: How do I request deletion of specific customer identities from our data?
  - id: getWorkOrderById
    intent: Get the status of one work order
    question: Has my record delete request finished processing yet?
  - id: updateWorkOrderById
    intent: Rename or re-describe a work order
    question: Can I change the name or description on a work order I already submitted?
  phrasing_ops: 4
  slug: adobe-suite-record-delete-work-order-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Record Type Controller
  name: Adobe Suite Record Types API
  phrasing_intents:
  - id: getRecordTypes
    intent: List record types in a workspace
    question: Which record types are defined in a Workfront Planning workspace?
  - id: getRecordType
    intent: Get a record type by ID
    question: What fields and settings does a single record type have?
  phrasing_ops: 2
  slug: adobe-suite-record-types-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Record Controller
  name: Adobe Suite Records API
  phrasing_intents:
  - id: getRecord
    intent: Get a record by ID
    question: What data does a specific Workfront Planning record hold?
  - id: updateRecord
    intent: Update a record
    question: How do I change the field values on an existing record?
  - id: deleteRecord
    intent: Delete a record
    question: How do I permanently remove a record?
  - id: createRecord
    intent: Create a record
    question: How do I add a new record of a given record type?
  - id: searchRecordsGet
    intent: Search records with query-string filters
    question: How do I find records of one type whose fields match certain values using a simple GET?
  - id: searchRecordsPost
    intent: Search records with a filter and sort body
    question: Can I search records with sorting rules sent in a request body?
  phrasing_ops: 6
  slug: adobe-suite-records-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Endpoints for video reframing.
  name: Adobe Suite Reframe API
  phrasing_intents:
  - id: generate-reframed-video
    intent: Reframe a video with the older v1 endpoint
    question: Is there still a v1 way to reframe a video for a new aspect ratio?
  - id: generate-reframed-video-v2
    intent: Reframe a video for a new aspect ratio
    question: How do I use AI to reframe a landscape video into vertical or square formats?
  - id: job-result-v2
    intent: Get the result of a reframe job
    question: How do I check whether my reframed video is ready?
  phrasing_ops: 3
  slug: adobe-suite-reframe-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Region Deployments API from Adobe Suite — 2 operation(s) for region deployments.
  name: Adobe Suite Region Deployments API
  phrasing_intents:
  - id: getRegionDeployment
    intent: Get one region deployment
    question: How do I look up a single region deployment of a Cloud Manager environment?
  - id: getRegionDeployments
    intent: List an environment's region deployments
    question: Which regions is my environment deployed to?
  - id: createRegionDeployment
    intent: Add region deployments to an environment
    question: How do I add another region to an environment?
  - id: patchRegionDeployment
    intent: Remove region deployments from an environment
    question: How do I remove a region from an environment?
  phrasing_ops: 4
  slug: adobe-suite-region-deployments-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Regions API from Adobe Suite — 1 operation(s) for regions.
  name: Adobe Suite Regions API
  phrasing_intents:
  - id: getProgramRegions
    intent: List regions available to a program
    question: Which regions can I create Cloud Manager environments in for my program?
  phrasing_ops: 1
  slug: adobe-suite-regions-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Query and view the product taxonomy of Adobe Products and Services.
  name: Adobe Suite Registry API
  phrasing_intents:
  - id: cloudsUsingGET
    intent: List Adobe product clouds
    question: What top-level Adobe product families does the status registry know about?
  - id: productsUsingGET
    intent: List Adobe products and services
    question: Which products and services are tracked across the clouds?
  - id: eventTypesUsingGET
    intent: List status event types
    question: What kinds of events can affect Adobe products, like outages or maintenance?
  - id: regionsUsingGET
    intent: List regions that status events can affect
    question: Which geographic regions can a status event be reported for?
  - id: localesUsingGET
    intent: List supported status message locales
    question: What languages are status event messages available in?
  - id: messagesUsingGET
    intent: List status event messages in all locales
    question: How do I get the message text for events impacting Adobe products?
  - id: messagesUsingGET_1
    intent: List status event messages for one locale
    question: Can I get status event messages translated into a single language?
  phrasing_ops: 7
  slug: adobe-suite-registry-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Replace file-based links in InDesign documents with AEM URLs. Particularly useful for customers working with Adobe Experience Manager (AEM) using Adobe Asset Link, enabling designers to work with outp
  name: Adobe Suite Remap Links API
  phrasing_intents:
  - id: remapLinks
    intent: Replace InDesign file links with AEM URLs
    question: Can I convert the file-based links in an InDesign document into Experience Manager asset URLs?
  phrasing_ops: 1
  slug: adobe-suite-remap-links-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Remove password protection from a PDF File
  name: Adobe Suite Remove Protection API
  phrasing_intents:
  - id: pdfoperations.removeprotection
    intent: Remove password protection from a PDF
    question: How do I unlock a password-protected PDF when I know the password?
  - id: pdfoperations.removeprotection.jobstatus
    intent: Check a PDF unlock job
    question: How do I know when a PDF has been unlocked?
  phrasing_ops: 2
  slug: adobe-suite-remove-protection-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Create file renditions in specified formats (e.g., PNG, JPEG, or PDF).
  name: Adobe Suite Rendition API
  phrasing_intents:
  - id: renditionJob
    intent: Render InDesign documents as JPEG, PNG or PDF
    question: Can I export an InDesign document to PDF in the cloud?
  phrasing_ops: 1
  slug: adobe-suite-rendition-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Reportablebudgetedhour API from Adobe Suite — 5 operation(s) for reportablebudgetedhour.
  name: Adobe Suite Reportablebudgetedhour API
  phrasing_intents:
  - id: getReportableBudgetedHour
    intent: Look up one reportable budgeted hour record
    question: How do I view a single reportable budgeted hour entry in Workfront?
  - id: getReportableBudgetedHours
    intent: Fetch several budgeted hour records by ID
    question: Can I retrieve multiple reportable budgeted hours at once by ID?
  - id: countReportableBudgetedHours
    intent: Count reportable budgeted hour records
    question: How many budgeted hour records match a given filter?
  - id: searchReportableBudgetedHours
    intent: Search reportable budgeted hours
    question: What's the way to find budgeted hours for a role or project?
  - id: reportReportableBudgetedHours
    intent: Run an aggregate report on budgeted hours
    question: Can I get grouped totals of budgeted hours as a report?
  phrasing_ops: 5
  slug: adobe-suite-reportablebudgetedhour-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Reports API from Adobe Suite — 3 operation(s) for reports.
  name: Adobe Suite Reports API
  phrasing_intents:
  - id: runReport
    intent: Run an Adobe Analytics report
    question: How do I pull a ranked report of a dimension and metrics from Adobe Analytics?
  - id: runRealtimeReport
    intent: Run a real-time Analytics report
    question: How do I see live, real-time data for a report suite?
  - id: runTopItemReport
    intent: Get the top items for a dimension
    question: What are the top pages in a report suite over the last 90 days?
  phrasing_ops: 3
  slug: adobe-suite-reports-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Repositories API from Adobe Suite — 2 operation(s) for repositories.
  name: Adobe Suite Repositories API
  phrasing_intents:
  - id: getRepositories
    intent: List a program's repositories
    question: Which Git repositories belong to my Cloud Manager program?
  - id: getRepository
    intent: Get one repository in a program
    question: What are the details of a specific repository in a program?
  phrasing_ops: 2
  slug: adobe-suite-repositories-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The requisition_lists API from Adobe Suite — 1 operation(s) for requisition_lists.
  name: Adobe Suite Requisition Lists API
  phrasing_intents:
  - id: PostV1Requisition_lists
    intent: Save a requisition list
    question: How do I create a requisition list for repeat B2B orders?
  phrasing_ops: 1
  slug: adobe-suite-requisition-lists-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Reseller Account Controller V 2
  name: Adobe Suite Resellers API
  phrasing_intents:
  - id: createResellerUsingPOST
    intent: Create a reseller account (v2)
    question: How do I create a reseller account with the v2 endpoint?
  - id: checkResellerChangeUsingGET
    intent: Preview a reseller change (v2)
    question: How do I check an approval code before switching a customer's reseller on v2?
  - id: executeResellerChangeUsingPOST
    intent: Apply a reseller change (v2)
    question: How do I complete a reseller transfer with the v2 API?
  - id: findAccountByResellerIdUsingGET
    intent: Get a reseller account (v2)
    question: How do I read a reseller's account details with the v2 API?
  - id: updateResellerUsingPATCH
    intent: Update a reseller account (v2)
    question: How do I change a reseller's address or phone number on v2?
  - id: createResellerUsingPOST_1
    intent: Create a reseller account (v3)
    question: How do I onboard a reseller on the v3 reseller API after they accept terms?
  - id: checkResellerChangeUsingGET_1
    intent: Preview a reseller change (v3)
    question: What subscriptions would transfer in a v3 reseller change?
  - id: executeResellerChangeUsingPOST_1
    intent: Apply a reseller change (v3)
    question: How do I execute a reseller change using the v3 endpoint?
  phrasing_ops: 10
  slug: adobe-suite-resellers-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Reservedtime API from Adobe Suite — 5 operation(s) for reservedtime.
  name: Adobe Suite Reservedtime API
  phrasing_intents:
  - id: getReservedTime
    intent: Look up one reserved time block
    question: What does a single reserved time record show about a user's blocked-off time?
  - id: editReservedTime
    intent: Edit a reserved time block
    question: How do I change the dates of someone's reserved time?
  - id: deleteReservedTime
    intent: Delete a reserved time block
    question: Can I cancel a user's reserved time off?
  - id: getReservedTimes
    intent: Fetch several reserved time blocks
    question: Can I pull multiple reserved time records at once by ID?
  - id: editReservedTimes
    intent: Bulk edit reserved time
    question: Can I update several reserved time entries in one request?
  - id: addReservedTimes
    intent: Reserve time for a user
    question: How do I block out time for a user so they are not scheduled?
  - id: deleteReservedTimes
    intent: Delete several reserved time blocks
    question: Can I bulk delete reserved time entries?
  - id: countReservedTimes
    intent: Count reserved time entries
    question: How many reserved time entries exist?
  phrasing_ops: 10
  slug: adobe-suite-reservedtime-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Resourcecontour API from Adobe Suite — 5 operation(s) for resourcecontour.
  name: Adobe Suite Resourcecontour API
  phrasing_intents:
  - id: getResourceContour
    intent: Get one resource contour by ID
    question: How do I look up a single resource contour in Workfront?
  - id: editResourceContour
    intent: Edit a resource contour
    question: How do I change the shape of an existing resource contour?
  - id: deleteResourceContour
    intent: Delete a resource contour
    question: How do I remove one resource contour?
  - id: getResourceContours
    intent: Fetch several resource contours by ID
    question: Can I load a batch of resource contours by a list of IDs?
  - id: editResourceContours
    intent: Bulk edit resource contours
    question: Can I update many resource contours in one bulk request?
  - id: addResourceContours
    intent: Create a resource contour
    question: How do I create a new resource contour?
  - id: deleteResourceContours
    intent: Bulk delete resource contours
    question: Can I delete several resource contours at once?
  - id: countResourceContours
    intent: Count resource contours
    question: How many resource contours are defined?
  phrasing_ops: 10
  slug: adobe-suite-resourcecontour-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Resourceplannerfilter API from Adobe Suite — 13 operation(s) for resourceplannerfilter.
  name: Adobe Suite Resourceplannerfilter API
  phrasing_intents:
  - id: getResourcePlannerFilter
    intent: Get a resource planner filter
    question: What conditions does a particular saved resource planner filter apply in Workfront?
  - id: editResourcePlannerFilter
    intent: Edit a resource planner filter
    question: How do I change a single saved resource planner filter?
  - id: deleteResourcePlannerFilter
    intent: Delete a resource planner filter
    question: How do I remove one saved resource planner filter?
  - id: getResourcePlannerFilters
    intent: Get several resource planner filters by ID
    question: Can I load multiple resource planner filters in one call by their IDs?
  - id: editResourcePlannerFilters
    intent: Bulk edit resource planner filters
    question: How do I update many resource planner filters in a single request?
  - id: addResourcePlannerFilters
    intent: Create a resource planner filter
    question: How do I save a new resource planner filter in Workfront?
  - id: deleteResourcePlannerFilters
    intent: Bulk delete resource planner filters
    question: Can I delete a whole set of resource planner filters at once?
  - id: countResourcePlannerFilters
    intent: Count resource planner filters
    question: How many resource planner filters exist in our Workfront instance?
  phrasing_ops: 18
  slug: adobe-suite-resourceplannerfilter-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Resourcepool API from Adobe Suite — 5 operation(s) for resourcepool.
  name: Adobe Suite Resourcepool API
  phrasing_intents:
  - id: getResourcePool
    intent: Get one resource pool
    question: Who belongs to a specific resource pool in Workfront?
  - id: editResourcePool
    intent: Update a resource pool
    question: How do I rename or change one resource pool?
  - id: deleteResourcePool
    intent: Delete a resource pool
    question: How do I remove a resource pool I no longer use?
  - id: getResourcePools
    intent: Get several resource pools by ID
    question: Can I fetch a set of resource pools by their IDs in one call?
  - id: editResourcePools
    intent: Update many resource pools at once
    question: Can I bulk edit several resource pools together?
  - id: addResourcePools
    intent: Create a resource pool
    question: How do I set up a new resource pool for capacity planning?
  - id: deleteResourcePools
    intent: Delete several resource pools
    question: Can I delete multiple resource pools at once?
  - id: countResourcePools
    intent: Count resource pools
    question: How many resource pools exist?
  phrasing_ops: 10
  slug: adobe-suite-resourcepool-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The reward/mine/use-reward API from Adobe Suite — 1 operation(s) for reward/mine/use-reward.
  name: Adobe Suite Reward/mine/use Reward API
  phrasing_intents:
  - id: PostV1RewardMineUsereward
    intent: Apply my reward points to my cart
    question: How do I use my reward points on my current order?
  phrasing_ops: 1
  slug: adobe-suite-reward-mine-use-reward-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Richtextnote API from Adobe Suite — 5 operation(s) for richtextnote.
  name: Adobe Suite Richtextnote API
  phrasing_intents:
  - id: getRichTextNote
    intent: Get a single rich text note
    question: How do I read one rich text note in Workfront by ID?
  - id: getRichTextNotes
    intent: Get several rich text notes by ID
    question: Can I fetch multiple rich text notes in one call?
  - id: countRichTextNotes
    intent: Count rich text notes
    question: How many rich text notes are there?
  - id: searchRichTextNotes
    intent: Search rich text notes
    question: How do I find rich text notes that match certain conditions?
  - id: reportRichTextNotes
    intent: Run a report over rich text notes
    question: Can I get an aggregated report of rich text notes?
  phrasing_ops: 5
  slug: adobe-suite-richtextnote-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Risk API from Adobe Suite — 5 operation(s) for risk.
  name: Adobe Suite Risk API
  phrasing_intents:
  - id: getRisk
    intent: Get one project risk
    question: How do I look up a single risk logged on a Workfront project?
  - id: editRisk
    intent: Edit a risk
    question: How do I update the probability or mitigation of one risk?
  - id: deleteRisk
    intent: Delete a risk
    question: How do I remove a risk from a project?
  - id: getRisks
    intent: Get several risks by ID
    question: Can I fetch multiple risks together if I know their IDs?
  - id: editRisks
    intent: Edit many risks at once
    question: Can I update several risks in one request?
  - id: addRisks
    intent: Create a risk
    question: How do I log a new risk on a project?
  - id: deleteRisks
    intent: Delete several risks
    question: Can I delete a batch of risks at once?
  - id: countRisks
    intent: Count risks
    question: How many risks are logged across our projects?
  phrasing_ops: 10
  slug: adobe-suite-risk-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Risktype API from Adobe Suite — 6 operation(s) for risktype.
  name: Adobe Suite Risktype API
  phrasing_intents:
  - id: getRiskType
    intent: Get a single risk type
    question: How do I look up one risk type by ID?
  - id: editRiskType
    intent: Edit a single risk type
    question: How can I rename or change one risk type?
  - id: deleteRiskType
    intent: Delete a single risk type
    question: How do I remove a risk type we don't use?
  - id: getRiskTypes
    intent: Get several risk types by ID at once
    question: Can I fetch multiple risk types in one call?
  - id: editRiskTypes
    intent: Edit many risk types in one request
    question: Is there a bulk edit for risk types?
  - id: addRiskTypes
    intent: Create a risk type
    question: How do I add a new risk type for project risk tracking?
  - id: deleteRiskTypes
    intent: Delete several risk types at once
    question: Can I bulk delete risk types by ID?
  - id: replaceRiskTypes
    intent: Replace a risk type with another
    question: How do I retire a risk type and move its usages to a different one?
  phrasing_ops: 11
  slug: adobe-suite-risktype-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Role API from Adobe Suite — 6 operation(s) for role.
  name: Adobe Suite Role API
  phrasing_intents:
  - id: getRole
    intent: Get one Workfront job role
    question: How do I look up a single job role by its ID?
  - id: editRole
    intent: Update one job role
    question: Can I rename or change the rates on an existing job role?
  - id: deleteRole
    intent: Delete one job role
    question: How do I remove a single job role?
  - id: getRoles
    intent: Get several job roles by ID
    question: Can I load multiple job roles at once from their IDs?
  - id: editRoles
    intent: Update many job roles at once
    question: Can I change several job roles in one request?
  - id: addRoles
    intent: Create a job role
    question: How do I add a new job role such as Designer or Developer?
  - id: deleteRoles
    intent: Delete several job roles
    question: Can I remove multiple job roles in one call?
  - id: replaceRoles
    intent: Replace job roles with another role
    question: How do I merge old job roles into one replacement role?
  phrasing_ops: 11
  slug: adobe-suite-role-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Routingrule API from Adobe Suite — 5 operation(s) for routingrule.
  name: Adobe Suite Routingrule API
  phrasing_intents:
  - id: getRoutingRule
    intent: Get a routing rule
    question: How do I look up a single routing rule that assigns incoming requests?
  - id: editRoutingRule
    intent: Edit a routing rule
    question: Can I change who a request queue routing rule sends work to?
  - id: deleteRoutingRule
    intent: Delete a routing rule
    question: How do I remove a routing rule from a request queue?
  - id: getRoutingRules
    intent: Fetch several routing rules by ID
    question: Can I retrieve a set of routing rules at once by listing their IDs?
  - id: editRoutingRules
    intent: Bulk edit routing rules
    question: How can I update many routing rules in one call?
  - id: addRoutingRules
    intent: Create a routing rule
    question: How do I set up a new routing rule for a request queue?
  - id: deleteRoutingRules
    intent: Bulk delete routing rules
    question: Can I delete a batch of routing rules together?
  - id: countRoutingRules
    intent: Count routing rules
    question: How many routing rules are configured?
  phrasing_ops: 10
  slug: adobe-suite-routingrule-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Rsrcpool API from Adobe Suite — 5 operation(s) for rsrcpool.
  name: Adobe Suite Rsrcpool API
  phrasing_intents:
  - id: getRsrcPool
    intent: Get one resource pool
    question: How do I look up a single Workfront resource pool by its ID?
  - id: editRsrcPool
    intent: Edit a resource pool
    question: Can I rename or change the details of one resource pool?
  - id: deleteRsrcPool
    intent: Delete a resource pool
    question: How do I remove one resource pool?
  - id: getRsrcPools
    intent: Get several resource pools by ID
    question: Can I fetch a batch of resource pools when I have their IDs?
  - id: editRsrcPools
    intent: Edit many resource pools at once
    question: Can I update a whole set of resource pools in one request?
  - id: addRsrcPools
    intent: Create a resource pool
    question: How do I create a new resource pool for grouping people?
  - id: deleteRsrcPools
    intent: Delete several resource pools
    question: Can I delete a batch of resource pools in one call?
  - id: countRsrcPools
    intent: Count resource pools
    question: How many resource pools are defined?
  phrasing_ops: 10
  slug: adobe-suite-rsrcpool-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'Rule components are the individual items that make up a rule. Rule components have three basic types: events (what triggers a rule), conditions (what the rule checks to determine an action), and actio'
  name: Adobe Suite Rule components API
  phrasing_intents:
  - id: listRuleComponents
    intent: List the components of a tag rule
    question: What events, conditions and actions make up a given tag rule?
  - id: createRuleComponent
    intent: Add a component to a tag rule
    question: How do I add a new event, condition or action to a rule?
  - id: retrieveRuleComponent
    intent: Retrieve a rule component
    question: How do I look up one rule component's settings?
  - id: deleteRuleComponent
    intent: Delete a rule component
    question: How do I remove a condition or action from a rule?
  - id: updateRuleComponent
    intent: Update a rule component
    question: Can I change the settings of an existing rule component?
  - id: getRuleComponentExtension
    intent: Find the extension behind a rule component
    question: Which extension provides a particular rule component?
  - id: retrieveRuleComponentOrigin
    intent: Retrieve a rule component's origin
    question: What is the original revision a rule component was copied from?
  - id: listRuleComponentsRelatedRules
    intent: List rules that use a rule component
    question: Which rules use a particular rule component?
  phrasing_ops: 10
  slug: adobe-suite-rule-components-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Rules control the behavior of the resources contained in a deployed library. A rule is a group of one or more rule components, and exists to tie the rule components together in a logical way.
  name: Adobe Suite Rules API
  phrasing_intents:
  - id: listRules
    intent: List a tag property's rules
    question: Which rules are set up in my Adobe tags property?
  - id: createRule
    intent: Create a rule in a tag property
    question: How do I add a new rule to a tags property?
  - id: retrieveRule
    intent: Get a tag rule's details
    question: What are the settings of a specific tag rule?
  - id: deleteRule
    intent: Delete a tag rule
    question: How do I delete a rule from my tags property?
  - id: updateRule
    intent: Update or revise a tag rule
    question: How do I change a rule's name or enabled state?
  - id: listRuleComponents
    intent: List a rule's components
    question: Which events, conditions and actions make up a rule?
  - id: createRuleComponent
    intent: Add a component to a rule
    question: How do I add an event, condition or action to a rule?
  - id: listRuleLibraries
    intent: List libraries that include a rule
    question: Which libraries contain a particular rule?
  phrasing_ops: 14
  slug: adobe-suite-rules-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Runs (or flow runs) represent the instance of a flow execution. For example, if a flow is scheduled to run hourly at 9 AM, 10 AM, and 11 AM, then you would have three instances of a run. Runs retain m
  name: Adobe Suite Runs API
  phrasing_intents:
  - id: listFlowRuns
    intent: List dataflow runs
    question: Which dataflow runs have happened in our organization?
  - id: createFlowRun
    intent: Start a new run for a flow
    question: How do I trigger an on-demand run of an existing dataflow?
  - id: retrieveFlowRun
    intent: Get one dataflow run
    question: What is the status and metrics of one specific flow run?
  - id: updateRun
    intent: Update a dataflow run
    question: Can I update the metrics or activities recorded on a flow run?
  - id: postAction
    intent: Perform an action on a flow run
    question: Can I cancel or otherwise act on a running dataflow run?
  phrasing_ops: 5
  slug: adobe-suite-runs-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: You can generate sample data for any specified schema within the Schema Library. The response object returned can then be used as the source of dataset ingestion.
  name: Adobe Suite Sample data API
  phrasing_intents:
  - id: retrieveSampleData
    intent: Generate sample data for a schema
    question: Can I see an example record that matches my XDM schema?
  phrasing_ops: 1
  slug: adobe-suite-sample-data-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Scenes API from Adobe Suite — 5 operation(s) for scenes.
  name: Adobe Suite Scenes API
  phrasing_intents:
  - id: v1/scenes/assemble
    intent: Assemble a 3D scene
    question: How do I combine several 3D models into one scene with the Substance 3D API?
  - id: v1/scenes/convert
    intent: Convert a 3D file to another format
    question: Can I convert an FBX model to GLB or USDZ?
  - id: v1/scenes/describe
    intent: Describe the contents of a 3D scene
    question: What cameras, meshes and materials are inside my 3D file?
  - id: v1/scenes/render
    intent: Render a 3D object with full options
    question: How do I render a product image from a 3D model with a ground plane and custom background?
  - id: v1/scenes/render-basic
    intent: Render a 3D object (basic version)
    question: Is there a simpler basic render endpoint for a quick 3D preview?
  phrasing_ops: 5
  slug: adobe-suite-scenes-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Schedule API from Adobe Suite — 11 operation(s) for schedule.
  name: Adobe Suite Schedule API
  phrasing_intents:
  - id: getSchedule
    intent: Get one Workfront work schedule
    question: How do I look up a single work schedule by ID?
  - id: editSchedule
    intent: Update one work schedule
    question: Can I change the working days or hours on one existing schedule?
  - id: deleteSchedule
    intent: Delete one work schedule
    question: How do I remove a single work schedule?
  - id: getSchedules
    intent: Get several schedules by ID
    question: Can I load multiple work schedules at once from a list of IDs?
  - id: editSchedules
    intent: Update many work schedules at once
    question: Can I edit a batch of work schedules in one request?
  - id: addSchedules
    intent: Create or copy a work schedule
    question: How do I create a new work schedule for a team or region?
  - id: deleteSchedules
    intent: Delete several work schedules
    question: Can I remove multiple work schedules in one call?
  - id: replaceSchedules
    intent: Replace schedules with another schedule
    question: How do I swap old work schedules out for a single replacement schedule?
  phrasing_ops: 16
  slug: adobe-suite-schedule-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Scheduledreport API from Adobe Suite — 6 operation(s) for scheduledreport.
  name: Adobe Suite Scheduledreport API
  phrasing_intents:
  - id: getScheduledReport
    intent: Get one scheduled report
    question: What schedule and recipients are set on a specific scheduled report?
  - id: editScheduledReport
    intent: Edit a single scheduled report
    question: How do I change when a scheduled report is delivered?
  - id: deleteScheduledReport
    intent: Delete a single scheduled report
    question: Can I stop and remove one scheduled report delivery?
  - id: getScheduledReports
    intent: Fetch several scheduled reports by ID
    question: Can I pull a batch of scheduled reports when I have their IDs?
  - id: editScheduledReports
    intent: Edit many scheduled reports at once
    question: Is there a way to bulk update several scheduled reports?
  - id: addScheduledReports
    intent: Create or copy a scheduled report
    question: How do I schedule a Workfront report to be emailed regularly?
  - id: deleteScheduledReports
    intent: Delete several scheduled reports by ID
    question: Can I remove many scheduled reports in one request?
  - id: countScheduledReports
    intent: Count scheduled reports matching filters
    question: How many scheduled reports are set up in our instance?
  phrasing_ops: 11
  slug: adobe-suite-scheduledreport-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Schedules let you perform SQL functions on a regular cadence from a start date to an end date or set a maximum number of runs.
  name: Adobe Suite Schedules API
  phrasing_intents:
  - id: listSchedules
    intent: List scheduled queries
    question: How do I see every scheduled SQL query my organization has set up?
  - id: createSchedule
    intent: Schedule a query to run on a recurrence
    question: How can I make a Query Service SQL query run automatically on a schedule?
  - id: retrieveSchedule
    intent: Get details of a scheduled query
    question: When was my scheduled query created and what state is it in?
  - id: deleteSchedule
    intent: Delete a scheduled query
    question: How do I stop and remove a query schedule entirely?
  - id: updateSchedule
    intent: Update a scheduled query
    question: Can I change the details of an existing query schedule, like disabling it?
  - id: listScheduleRuns
    intent: List the runs of a scheduled query
    question: How can I see the run history of a scheduled query?
  - id: triggerScheduleRun
    intent: Run a scheduled query immediately
    question: Can I kick off a scheduled query right now instead of waiting for its next slot?
  - id: retrieveScheduledQueryRun
    intent: Get details of one scheduled query run
    question: How do I check whether a particular run of my scheduled query succeeded?
  phrasing_ops: 14
  slug: adobe-suite-schedules-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Schemas provide an abstract definition of a real-world object along with constraints and expectations that can be applied and used to validate data.
  name: Adobe Suite Schemas API
  phrasing_intents:
  - id: listSchemas
    intent: List XDM schemas in a container
    question: Which XDM schemas exist in my tenant container?
  - id: retrieveSchema
    intent: Get an XDM schema
    question: What fields and class does a particular XDM schema have?
  - id: createSchema
    intent: Create a custom XDM schema
    question: How do I create my own XDM schema based on a class like XDM Individual Profile?
  - id: updateSchema
    intent: Replace a custom XDM schema
    question: Can I rewrite an entire custom schema in one request?
  - id: patchSchema
    intent: Patch attributes of a custom XDM schema
    question: Can I add a field group or change one attribute of a schema without rewriting it?
  - id: deleteSchema
    intent: Delete a custom XDM schema
    question: How do I delete a custom schema I created?
  phrasing_ops: 6
  slug: adobe-suite-schemas-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Scorecard API from Adobe Suite — 5 operation(s) for scorecard.
  name: Adobe Suite Scorecard API
  phrasing_intents:
  - id: getScoreCard
    intent: Get a scorecard by ID
    question: What questions and weights are on a particular Workfront scorecard?
  - id: editScoreCard
    intent: Update a scorecard
    question: How do I change the questions on an existing scorecard?
  - id: deleteScoreCard
    intent: Delete a scorecard
    question: How do I remove a scorecard we no longer use?
  - id: getScoreCards
    intent: Get several scorecards by their IDs
    question: Can I load multiple scorecards in one request?
  - id: editScoreCards
    intent: Bulk-update several scorecards
    question: Can I edit many scorecards at once?
  - id: addScoreCards
    intent: Create or copy a scorecard
    question: How do I create a new scorecard for scoring project requests?
  - id: deleteScoreCards
    intent: Delete several scorecards at once
    question: Can I delete a batch of scorecards together?
  - id: countScoreCards
    intent: Count scorecards
    question: How many scorecards exist in our instance?
  phrasing_ops: 10
  slug: adobe-suite-scorecard-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The search endpoint provides a way to find resources matching a desired criteria, expressed as a query. All queries are scoped to your current company and accessible properties.
  name: Adobe Suite Search API
  phrasing_intents:
  - id: createSearch
    intent: Search tags resources like rules and data elements
    question: What's the way to search across my tag properties' rules, data elements and extensions?
  - id: GetV1Search
    intent: Full-text search the Commerce store
    question: Can I run a full-text search for products in the Commerce storefront?
  phrasing_ops: 2
  slug: adobe-suite-search-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: A secret is a resource that represents an authentication credential. Secrets are used in event forwarding to authenticate to another system for secure data exchange. Secrets can only be created within
  name: Adobe Suite Secrets API
  phrasing_intents:
  - id: listPropertySecrets
    intent: List a tag property's secrets
    question: How do I see all the secrets stored on a tags property?
  - id: createSecret
    intent: Create a secret on a tag property
    question: How do I add a new secret, like OAuth or token credentials, to a tags property?
  - id: retrieveSecret
    intent: Get a secret's details
    question: How do I look up one secret by its ID?
  - id: deleteSecret
    intent: Delete a secret
    question: How do I delete a secret I no longer need?
  - id: testOrRetrySecret
    intent: Test or retry a secret's credential exchange
    question: How do I manually retry the credential exchange for a secret?
  - id: listEnvironmentSecrets
    intent: List an environment's secrets
    question: Which secrets are bound to a particular environment?
  - id: listSecretNotes
    intent: List notes on a secret
    question: How do I read the notes left on a secret?
  - id: createSecretNote
    intent: Add a note to a secret
    question: Can I leave a note on a secret for my team?
  phrasing_ops: 11
  slug: adobe-suite-secrets-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Segment definitions include a Profile Query Language (PQL) statement that defines which profiles will be part of an audience. More information about using this set of endpoints can be found in the [se
  name: Adobe Suite Segment definitions API
  phrasing_intents:
  - id: listSegmentDefinitions
    intent: List segment definitions
    question: What audience segment definitions exist in my Experience Platform sandbox?
  - id: createSegmentDefinition
    intent: Create a segment definition
    question: How do I define a new audience with a PQL expression?
  - id: retrieveSegmentDefinitionById
    intent: Get one segment definition
    question: How do I see the expression and settings of a specific segment definition?
  - id: deleteSegmentDefinition
    intent: Delete a segment definition
    question: How do I remove an audience segment definition I no longer need?
  - id: patchSegmentDefinition
    intent: Overwrite an existing segment definition
    question: Can I change the expression of a segment definition that already exists?
  - id: bulkGetSegmentDefinitions
    intent: Fetch several segment definitions by ID
    question: Can I retrieve multiple segment definitions in one request?
  - id: convertSegmentDefinition
    intent: Convert a segment expression between PQL formats
    question: How do I turn a PQL text expression into its JSON form?
  phrasing_ops: 7
  slug: adobe-suite-segment-definitions-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Segment jobs process previously established segment definitions to generate an audience. More information about using this set of endpoints can be found in the [segment jobs endpoint guide](https://ex
  name: Adobe Suite Segment jobs API
  phrasing_intents:
  - id: listSegmentJobs
    intent: List segment evaluation jobs
    question: Which segment jobs have run recently in my sandbox?
  - id: createSegmentJob
    intent: Start a segment evaluation job
    question: How do I kick off a job that evaluates my segment definitions?
  - id: retrieveSegmentJob
    intent: Check the status of a segment job
    question: How do I tell whether my segment job has finished?
  - id: deleteSegmentJob
    intent: Cancel a segment job
    question: Can I stop a segment job that is still running?
  - id: bulkGetSegmentJobs
    intent: Fetch several segment jobs by ID
    question: Can I check the status of many segment jobs in one request?
  phrasing_ops: 5
  slug: adobe-suite-segment-jobs-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: 'Segment search allows users to search across multiple namespaces or get specific structural information about specified objects. More information about using this set of endpoints can be found in the '
  name: Adobe Suite Segment search API
  phrasing_intents:
  - id: listSearchCounts
    intent: Count search hits across namespaces
    question: How many matches does a search term get in each namespace?
  - id: listFullTextIndexedObjects
    intent: List full-text indexed objects in a namespace
    question: How do I list the segment objects indexed for full-text search in one namespace?
  - id: retrieveSearchObjectStructure
    intent: Get a search object's taxonomy
    question: Where does a given search object sit in the folder taxonomy?
  phrasing_ops: 3
  slug: adobe-suite-segment-search-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Segments API from Adobe Suite — 3 operation(s) for segments.
  name: Adobe Suite Segments API
  phrasing_intents:
  - id: segments_getSegments
    intent: List Analytics segments
    question: How do I list the segments available in my Adobe Analytics company?
  - id: segments_createSegment
    intent: Create an Analytics segment
    question: What do I send to build a new segment in Analytics?
  - id: segments_validateSegment
    intent: Validate a segment definition
    question: Can I check that a segment definition is valid before saving it?
  - id: segments_getSegment
    intent: Get one Analytics segment
    question: How can I view the definition of one specific segment?
  - id: segments_updateSegment
    intent: Update an Analytics segment
    question: Can I change the definition or name of an existing segment?
  - id: segments_deleteSegment
    intent: Delete an Analytics segment
    question: How do I delete a segment nobody uses anymore?
  phrasing_ops: 6
  slug: adobe-suite-segments-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Real-time events forwarded by a private server
  name: Adobe Suite Server-to-server collection API
  phrasing_intents:
  - id: postV2Interact
    intent: Send one server-side event and get a response
    question: How do I send an authenticated event from my server and get personalization back?
  - id: postV2Collect
    intent: Batch-send server-side events without a response
    question: How can my server push many events from different users in one authenticated call?
  phrasing_ops: 2
  slug: adobe-suite-server-to-server-collection-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Session API from Adobe Suite — 4 operation(s) for session.
  name: Adobe Suite Session API
  phrasing_intents:
  - id: sessionStart
    intent: Start a media tracking session
    question: How do I begin tracking a video playback session with the Adobe Media Edge API?
  - id: sessionComplete
    intent: Mark a media session as watched to the end
    question: How do I signal that a viewer reached the end of the main content?
  - id: sessionEnd
    intent: Close an abandoned media session immediately
    question: The viewer left mid-video — how do I close the session right away instead of waiting for the timeout?
  - id: session
    intent: Get media session information
    question: Can I read back information about the current media tracking session?
  phrasing_ops: 4
  slug: adobe-suite-session-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Source connections create and manage a connection to the internal source from where data is exported. For destination connections, the source connection can be either the Experience Platform Profile S
  name: Adobe Suite Source connections API
  phrasing_intents:
  - id: getSourceConnections
    intent: List source connections for destinations
    question: What source connections for destinations exist in my Experience Platform org?
  - id: postSourceConnection
    intent: Create a source connection for a destination
    question: How do I connect the Profile Store or Data Lake as a source for a destination dataflow?
  - id: getSourceConnectionById
    intent: Get a destination source connection by ID
    question: How do I view details of one source connection used for destinations?
  - id: deleteSourceConnectionById
    intent: Delete a destination source connection
    question: How do I delete a source connection that fed a destination?
  - id: retrieveSourceConnection
    intent: Get an ingestion source connection
    question: How do I look up a source connection used to ingest data by its ID?
  - id: deleteSourceConnection
    intent: Delete an ingestion source connection
    question: How do I delete a source connection that ingests data into Platform?
  - id: patchSourceConnection
    intent: Update a source connection
    question: How do I update a source connection's name or details?
  - id: performAction_1
    intent: Change a source connection's state
    question: How do I move an existing source connection to a different state?
  phrasing_ops: 8
  slug: adobe-suite-source-connections-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Spaces API from Adobe Suite — 2 operation(s) for spaces.
  name: Adobe Suite Spaces API
  phrasing_intents:
  - id: createSpace_v1
    intent: Create a space from 3D files (v1)
    question: How do I create a Substance 3D space from a 3D file using the original v1 endpoint?
  - id: createSpace_v2
    intent: Upload files to a new space (v2)
    question: How can I upload several files into a temporary space with the v2 multipart endpoint?
  phrasing_ops: 2
  slug: adobe-suite-spaces-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The SpacesFrameIO API from Adobe Suite — 1 operation(s) for spacesframeio.
  name: Adobe Suite Spaces Frame IO API
  phrasing_intents:
  - id: createSpaceFromFrameIO_v2
    intent: Create a Substance 3D space from a Frame.io folder
    question: Can I use a Frame.io folder as the source for Substance 3D API jobs?
  phrasing_ops: 1
  slug: adobe-suite-spacesframeio-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The SpacesNextFrameIO API from Adobe Suite — 1 operation(s) for spacesnextframeio.
  name: Adobe Suite Spaces Next Frame IO API
  phrasing_intents:
  - id: createSpaceFromNextFrameIO_v2
    intent: Create a Substance 3D space from a Frame.io folder
    question: How do I bring a folder from next.frame.io into a Substance 3D space?
  phrasing_ops: 1
  slug: adobe-suite-spacesnextframeio-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The SpacesURL API from Adobe Suite — 1 operation(s) for spacesurl.
  name: Adobe Suite Spaces URL API
  phrasing_intents:
  - id: createSpaceURL_v2
    intent: Create a Substance 3D space from file URLs
    question: Can I upload files to Substance 3D from URLs instead of sending the bytes?
  phrasing_ops: 1
  slug: adobe-suite-spacesurl-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Split a PDF File into multiple PDF Files
  name: Adobe Suite Split PDF API
  phrasing_intents:
  - id: pdfoperations.splitpdf
    intent: Split a PDF into multiple files
    question: How do I split a large PDF into smaller documents?
  - id: pdfoperations.splitpdf.jobstatus
    intent: Check a PDF split job's status
    question: How do I know when my PDF split job has finished?
  phrasing_ops: 2
  slug: adobe-suite-split-pdf-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The SSL Certificates API from Adobe Suite — 3 operation(s) for ssl certificates.
  name: Adobe Suite SSL Certificates API
  phrasing_intents:
  - id: getCertificateByIdAndProgramId
    intent: Get an SSL certificate in a program
    question: How do I look up one SSL certificate in my Cloud Manager program?
  - id: updateCertificate
    intent: Update an SSL certificate
    question: How do I replace an expiring certificate with a renewed one?
  - id: deleteCertificate
    intent: Delete an SSL certificate
    question: How do I remove an SSL certificate from a program?
  - id: getAllCertificatesForProgram
    intent: List SSL certificates in a program
    question: How do I list all SSL certificates for my program?
  - id: createSslCertificate
    intent: Add a customer-managed SSL certificate
    question: How do I upload my own SSL certificate to a Cloud Manager program?
  - id: createDvCertificate
    intent: Request a domain-validated certificate
    question: Can Adobe issue a domain-validated certificate for my domains instead of me uploading one?
  phrasing_ops: 6
  slug: adobe-suite-ssl-certificates-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The States API from Adobe Suite — 1 operation(s) for states.
  name: Adobe Suite States API
  phrasing_intents:
  - id: statesUpdate
    intent: Signal a change to one or more states
    question: What endpoint notifies the service that some states have changed?
  phrasing_ops: 1
  slug: adobe-suite-states-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Returns {TENANT_ID} along with information regarding IMS Org usage of the Schema Registry such as resource counts, recently created resources, and class usage.
  name: Adobe Suite Stats API
  phrasing_intents:
  - id: retrieveStats
    intent: Get Schema Registry usage and tenant ID
    question: How do I find my tenant ID for the Schema Registry?
  phrasing_ops: 1
  slug: adobe-suite-stats-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Status API from Adobe Suite — 2 operation(s) for status.
  name: Adobe Suite Status API
  phrasing_intents:
  - id: getJobStatus
    intent: Check the status of an Express job
    question: Is my Adobe Express job finished yet?
  phrasing_ops: 1
  slug: adobe-suite-status-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Streaming ingestion allows you to send data from client and server-side devices to Experience Platform in real-time. It drives Real-Time Customer Profile by creating personalized experiences.
  name: Adobe Suite Streaming Ingestion API
  phrasing_intents:
  - id: sendMessage
    intent: Stream one record into Experience Platform
    question: How do I send a single event or record to Experience Platform in real time?
  - id: postBatchOfStreamingMessages
    intent: Stream many records in one request
    question: Can I send multiple streaming messages to Experience Platform in one call?
  phrasing_ops: 2
  slug: adobe-suite-streaming-ingestion-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Subscribe API from Adobe Suite — 10 operation(s) for subscribe.
  name: Adobe Suite Subscribe API
  phrasing_intents:
  - id: getSubscribe
    intent: Get one subscription record
    question: How do I look up a single Workfront subscription record by its ID?
  - id: deleteSubscribe
    intent: Delete a subscription record
    question: Can I delete one subscription record outright?
  - id: getSubscribes
    intent: Get several subscription records by ID
    question: Can I fetch a batch of subscription records if I know their IDs?
  - id: addSubscribes
    intent: Create a subscription record
    question: How do I create a new subscription record directly?
  - id: deleteSubscribes
    intent: Delete several subscription records
    question: Can I delete a batch of subscription records in one call?
  - id: countSubscribes
    intent: Count subscription records
    question: How many subscription records exist?
  - id: searchSubscribes
    intent: Search subscription records
    question: How can I find subscription records matching certain conditions?
  - id: reportSubscribes
    intent: Run a report on subscription records
    question: Can I produce an aggregated report of subscriptions?
  phrasing_ops: 13
  slug: adobe-suite-subscribe-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Customer Subscription Controller V 2
  name: Adobe Suite Subscriptions API
  phrasing_intents:
  - id: findSubscriptionsUsingGET
    intent: List a customer's subscriptions (v2)
    question: How do I list every subscription a reseller customer has using the v2 endpoint?
  - id: findSubscriptionUsingGET
    intent: Get a subscription's details (v2)
    question: What is the current quantity and auto-renewal status of one subscription via v2?
  - id: updateSubscriptionAutoRenewalUsingPATCH
    intent: Change a subscription's auto-renewal (v2)
    question: How do I turn off auto-renewal on a customer's subscription with the v2 API?
  - id: findSubscriptionsUsingGET_1
    intent: List a customer's subscriptions (v3)
    question: Which subscriptions does a customer have according to the current v3 API?
  - id: findSubscriptionUsingGET_1
    intent: Get a subscription's details (v3)
    question: What quantity and renewal status does a subscription show in v3?
  - id: updateSubscriptionAutoRenewalUsingPATCH_1
    intent: Change a subscription's auto-renewal (v3)
    question: How do I switch off auto-renew for a subscription with the v3 API?
  phrasing_ops: 6
  slug: adobe-suite-subscriptions-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Suppression API from Adobe Suite — 7 operation(s) for suppression.
  name: Adobe Suite Suppression API
  phrasing_intents:
  - id: getAddressesId
    intent: List suppressed or allowed email addresses
    question: Which email addresses are on our suppression list?
  - id: addAddressId
    intent: Add an email address to the suppression or allow list
    question: How do I stop messages going to a specific email address?
  - id: getEmailAddressId
    intent: Check one email address's suppression status
    question: Is a particular email address suppressed?
  - id: deleteEmailAddressId
    intent: Remove an email address from suppression
    question: How do I unsuppress an email address so it can receive messages again?
  - id: getDomainsId
    intent: List suppressed or allowed domains
    question: Which whole email domains are we suppressing?
  - id: addDomainId
    intent: Add a domain to the suppression or allow list
    question: How do I block sending to an entire email domain?
  - id: getDomainId
    intent: Check one domain's suppression status
    question: Is a specific email domain suppressed?
  - id: deleteDomainId
    intent: Remove a domain from suppression
    question: How do I unblock a domain so mail can go to it again?
  phrasing_ops: 13
  slug: adobe-suite-suppression-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Tag categories let you organize your tags into meaningful sets, allowing you to provide more context to the tag's purpose.
  name: Adobe Suite Tag categories API
  phrasing_intents:
  - id: listTagCategories
    intent: List unified tag categories
    question: What tag categories exist for organizing tags in Experience Platform?
  - id: createTagCategory
    intent: Create a tag category
    question: How do I create a new category to group unified tags?
  - id: retrieveTagCategory
    intent: Retrieve a tag category
    question: What are the details of one tag category?
  - id: updateTagCategory
    intent: Update a tag category
    question: How do I rename an existing tag category?
  - id: deleteTagCategory
    intent: Delete a tag category
    question: Who is allowed to delete a tag category?
  phrasing_ops: 5
  slug: adobe-suite-tag-categories-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Tags are used to attach information to an object and then be used later to retrieve the object.
  name: Adobe Suite Tags API
  phrasing_intents:
  - id: listTags
    intent: Get aggregated tag values in a namespace (legacy)
    question: What aggregated values exist for all tags in one namespace across my organization?
  - id: getUnifiedtagsTags
    intent: List unified tags
    question: How do I list all the unified tags in Adobe Experience Platform?
  - id: createTag
    intent: Create a unified tag
    question: How do I create a new tag to label objects in Experience Platform?
  - id: retrieveTag
    intent: Get one unified tag
    question: What are the details of a specific unified tag?
  - id: updateTag
    intent: Update a unified tag
    question: How can I rename an existing tag?
  - id: deleteTag
    intent: Delete a unified tag
    question: How do I permanently remove a tag I no longer need?
  - id: validateTags
    intent: Check whether tags are valid
    question: Can I check that a list of tag IDs is valid before applying them?
  phrasing_ops: 7
  slug: adobe-suite-tags-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Target connections create and manage a destination connection to any location where exported data will land. Target connections contain information regarding data destination, data format, and the tar
  name: Adobe Suite Target connections API
  phrasing_intents:
  - id: getTargetConnections
    intent: List destination target connections
    question: Which destination target connections does my Experience Platform org have?
  - id: postTargetConnection
    intent: Create a destination target connection
    question: How do I set up where exported data will land for a destination?
  - id: getTargetConnectionById
    intent: Inspect a target connection by ID
    question: What settings does a specific target connection have?
  - id: deleteTargetConnectionById
    intent: Delete a target connection by ID
    question: Can I remove a destination target connection I no longer export to?
  - id: performAction_2
    intent: Change a target connection's state
    question: Can I enable or disable an existing target connection?
  - id: retrieveTargetConnection
    intent: Retrieve a single target connection
    question: Can I retrieve a single target connection record for a flow service?
  - id: deleteTargetConnection
    intent: Delete a target connection instance
    question: How do I delete an instance of a target connection from the flow service?
  - id: patchTargetConnection
    intent: Update a target connection
    question: How do I change settings on an existing target connection?
  phrasing_ops: 8
  slug: adobe-suite-target-connections-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Task API from Adobe Suite — 35 operation(s) for task.
  name: Adobe Suite Task API
  phrasing_intents:
  - id: getTask
    intent: Look up a single Workfront task
    question: How do I pull the details of one Workfront task by its ID?
  - id: editTask
    intent: Update one task
    question: Can I change the name or dates on an existing task?
  - id: deleteTask
    intent: Delete one task
    question: How do I remove a single task from a project?
  - id: getTasks
    intent: Fetch several tasks by their IDs
    question: Can I retrieve a batch of tasks at once if I already know their IDs?
  - id: editTasks
    intent: Update many tasks in one request
    question: Can I bulk edit a bunch of tasks together instead of one at a time?
  - id: addTasks
    intent: Create a new task or copy an existing one
    question: How do I add a new task to a project in Workfront?
  - id: deleteTasks
    intent: Delete many tasks at once
    question: Can I delete several tasks in a single request?
  - id: countTasks
    intent: Count tasks matching filters
    question: How many tasks are there that match a given filter?
  phrasing_ops: 40
  slug: adobe-suite-task-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Team API from Adobe Suite — 5 operation(s) for team.
  name: Adobe Suite Team API
  phrasing_intents:
  - id: getTeam
    intent: Get a Workfront team
    question: Who is on a particular team in Workfront?
  - id: editTeam
    intent: Edit a Workfront team
    question: How do I update the details of one team?
  - id: deleteTeam
    intent: Delete a Workfront team
    question: How do I delete one team from Workfront?
  - id: getTeams
    intent: Get several teams by ID
    question: Can I load a batch of teams at once when I already know their IDs?
  - id: editTeams
    intent: Bulk edit teams
    question: Can I update many teams in a single call?
  - id: addTeams
    intent: Create a Workfront team
    question: How do I create a new team in Workfront?
  - id: deleteTeams
    intent: Bulk delete teams
    question: Can I delete a group of teams at once?
  - id: countTeams
    intent: Count Workfront teams
    question: How many teams do we have in Workfront?
  phrasing_ops: 10
  slug: adobe-suite-team-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Template API from Adobe Suite — 15 operation(s) for template.
  name: Adobe Suite Template API
  phrasing_intents:
  - id: getTemplate
    intent: Get a single project template
    question: How do I pull up one Workfront project template by its ID?
  - id: editTemplate
    intent: Edit one project template
    question: Can I change the details of one specific template?
  - id: deleteTemplate
    intent: Delete one project template
    question: How do I delete a single template?
  - id: getTemplates
    intent: Get several templates by ID
    question: Can I fetch a handful of templates at once by listing their IDs?
  - id: editTemplates
    intent: Edit many templates at once
    question: Can I push the same edit to a batch of templates in one request?
  - id: addTemplates
    intent: Create or copy a project template
    question: How do I create a new project template?
  - id: deleteTemplates
    intent: Delete many templates at once
    question: Can I delete a list of templates in one call?
  - id: countTemplates
    intent: Count project templates
    question: How many templates do we have in Workfront?
  phrasing_ops: 20
  slug: adobe-suite-template-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Templateassignment API from Adobe Suite — 5 operation(s) for templateassignment.
  name: Adobe Suite Templateassignment API
  phrasing_intents:
  - id: getTemplateAssignment
    intent: Look up one template assignment
    question: How do I view a single assignment on a Workfront project template?
  - id: editTemplateAssignment
    intent: Update one template assignment
    question: Can I change who or what role is assigned on a template task?
  - id: deleteTemplateAssignment
    intent: Delete one template assignment
    question: How do I remove an assignment from a template task?
  - id: getTemplateAssignments
    intent: Fetch several template assignments by ID
    question: Can I retrieve a batch of template assignments when I know their IDs?
  - id: editTemplateAssignments
    intent: Update many template assignments at once
    question: Can I bulk edit several template assignments in one request?
  - id: addTemplateAssignments
    intent: Assign someone to a template task
    question: How do I assign a user, role or team to a task on a project template?
  - id: deleteTemplateAssignments
    intent: Delete many template assignments at once
    question: Can I bulk delete template assignments by listing their IDs?
  - id: countTemplateAssignments
    intent: Count template assignments
    question: How many template assignments match a given filter?
  phrasing_ops: 10
  slug: adobe-suite-templateassignment-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Templatetask API from Adobe Suite — 9 operation(s) for templatetask.
  name: Adobe Suite Templatetask API
  phrasing_intents:
  - id: getTemplateTask
    intent: Get one template task
    question: How do I look up a single task inside a Workfront project template?
  - id: editTemplateTask
    intent: Edit a template task
    question: How do I change the duration or name of one task in a template?
  - id: deleteTemplateTask
    intent: Delete a template task
    question: What's the way to remove one task from a project template?
  - id: getTemplateTasks
    intent: Get several template tasks by ID
    question: Can I fetch multiple template tasks in one call using their IDs?
  - id: editTemplateTasks
    intent: Edit many template tasks at once
    question: Can I update a batch of template tasks in one request?
  - id: addTemplateTasks
    intent: Create or copy a template task
    question: How do I add a new task to a project template?
  - id: deleteTemplateTasks
    intent: Delete several template tasks
    question: Can I delete many template tasks with one call?
  - id: countTemplateTasks
    intent: Count template tasks
    question: How many template tasks exist across our templates?
  phrasing_ops: 14
  slug: adobe-suite-templatetask-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Tenants API from Adobe Suite — 2 operation(s) for tenants.
  name: Adobe Suite Tenants API
  phrasing_intents:
  - id: getTenants
    intent: List Cloud Manager tenants
    question: Which Cloud Manager tenants can my technical account see?
  - id: getTenant
    intent: Get one Cloud Manager tenant
    question: How do I look up a single tenant by its ID?
  phrasing_ops: 2
  slug: adobe-suite-tenants-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Endpoints for Text-to-Avatar operations.
  name: Adobe Suite Text To Avatar API
  phrasing_intents:
  - id: voices
    intent: List available avatar voices
    question: Which voices can my enterprise use for avatar videos?
  - id: avatars
    intent: List available avatars
    question: Which avatars can I use to present a video?
  - id: generate-avatar
    intent: Generate an avatar video from text
    question: How do I turn a script into a talking avatar video?
  phrasing_ops: 3
  slug: adobe-suite-text-to-avatar-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Endpoints for text-to-speech operations.
  name: Adobe Suite Text To Speech API
  phrasing_intents:
  - id: voices
    intent: List available text-to-speech voices
    question: Which voices can I use for text-to-speech in Firefly?
  - id: generate-speech
    intent: Generate speech audio from text
    question: Can I turn a written script into narration audio?
  phrasing_ops: 2
  slug: adobe-suite-text-to-speech-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/authy/activate API from Adobe Suite — 1 operation(s) for tfa/provider/authy/activate.
  name: Adobe Suite Tfa/provider/authy/activate API
  phrasing_intents:
  - id: PostV1TfaProviderAuthyActivate
    intent: Activate Authy two-factor and get an admin token
    question: How do I finish setting up Authy two-factor authentication for a Commerce admin?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-authy-activate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/authy/authenticate API from Adobe Suite — 1 operation(s) for tfa/provider/authy/authenticate.
  name: Adobe Suite Tfa/provider/authy/authenticate API
  phrasing_intents:
  - id: PostV1TfaProviderAuthyAuthenticate
    intent: Get an admin token using an Authy code
    question: How do I get a Commerce admin token when two-factor auth with Authy is on?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-authy-authenticate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/authy/authenticate-onetouch API from Adobe Suite — 1 operation(s) for tfa/provider/authy/authenticate-onetouch.
  name: Adobe Suite Tfa/provider/authy/authenticate Onetouch API
  phrasing_intents:
  - id: PostV1TfaProviderAuthyAuthenticateonetouch
    intent: Get an admin token via Authy OneTouch
    question: What gets me a Commerce admin token after approving an Authy OneTouch prompt?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-authy-authenticate-onetouch-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/authy/configure API from Adobe Suite — 1 operation(s) for tfa/provider/authy/configure.
  name: Adobe Suite Tfa/provider/authy/configure API
  phrasing_intents:
  - id: PostV1TfaProviderAuthyConfigure
    intent: Configure Authy two-factor authentication
    question: How do I set up Authy as the two-factor provider for an admin user?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-authy-configure-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/authy/send-token/{via} API from Adobe Suite — 1 operation(s) for tfa/provider/authy/send-token/{via}.
  name: Adobe Suite Tfa/provider/authy/send Token/{via} API
  phrasing_intents:
  - id: PostV1TfaProviderAuthySendtokenVia
    intent: Send an Authy one-time password
    question: How do I send a two-factor code to a user's device with Authy?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-authy-send-token-via-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/duo_security/activate API from Adobe Suite — 1 operation(s) for tfa/provider/duo_security/activate.
  name: Adobe Suite Tfa/provider/duo Security/activate API
  phrasing_intents:
  - id: PostV1TfaProviderDuo_securityActivate
    intent: Activate Duo Security 2FA and get an admin token
    question: How do I finish activating Duo Security two-factor authentication for an admin?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-duo-security-activate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/duo_security/authenticate API from Adobe Suite — 1 operation(s) for tfa/provider/duo_security/authenticate.
  name: Adobe Suite Tfa/provider/duo Security/authenticate API
  phrasing_intents:
  - id: PostV1TfaProviderDuo_securityAuthenticate
    intent: Get an admin token via Duo 2FA
    question: How do I get an admin token when Duo Security two-factor is enabled?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-duo-security-authenticate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/duo_security/configure API from Adobe Suite — 1 operation(s) for tfa/provider/duo_security/configure.
  name: Adobe Suite Tfa/provider/duo Security/configure API
  phrasing_intents:
  - id: PostV1TfaProviderDuo_securityConfigure
    intent: Get Duo setup details for two-factor auth
    question: How do I get the details needed to configure Duo Security for admin two-factor login?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-duo-security-configure-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/duo_security/get-authentication-data API from Adobe Suite — 1 operation(s) for tfa/provider/duo_security/get-authentication-data.
  name: Adobe Suite Tfa/provider/duo Security/get Authentication Data API
  phrasing_intents:
  - id: PostV1TfaProviderDuo_securityGetauthenticationdata
    intent: Get Duo configuration data for an admin
    question: What information do I need to configure Duo two-factor authentication for an admin user?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-duo-security-get-authentication-data-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/google/activate API from Adobe Suite — 1 operation(s) for tfa/provider/google/activate.
  name: Adobe Suite Tfa/provider/google/activate API
  phrasing_intents:
  - id: PostV1TfaProviderGoogleActivate
    intent: Activate Google Authenticator 2FA for an admin
    question: How do I finish setting up Google Authenticator two-factor for a Commerce admin?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-google-activate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/google/authenticate API from Adobe Suite — 1 operation(s) for tfa/provider/google/authenticate.
  name: Adobe Suite Tfa/provider/google/authenticate API
  phrasing_intents:
  - id: PostV1TfaProviderGoogleAuthenticate
    intent: Get an admin token with Google Authenticator
    question: Can an admin get an API token when two-factor authentication with Google Authenticator is on?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-google-authenticate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/google/configure API from Adobe Suite — 1 operation(s) for tfa/provider/google/configure.
  name: Adobe Suite Tfa/provider/google/configure API
  phrasing_intents:
  - id: PostV1TfaProviderGoogleConfigure
    intent: Get Google Authenticator setup info
    question: How do I get the QR code and secret to set up Google Authenticator for two-factor login?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-google-configure-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/u2fkey/activate API from Adobe Suite — 1 operation(s) for tfa/provider/u2fkey/activate.
  name: Adobe Suite Tfa/provider/u2fkey/activate API
  phrasing_intents:
  - id: PostV1TfaProviderU2fkeyActivate
    intent: Activate a U2F security key for 2FA
    question: How do I activate a U2F hardware key as my two-factor provider?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-u2fkey-activate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/u2fkey/authentication-challenge API from Adobe Suite — 1 operation(s) for tfa/provider/u2fkey/authentication-challenge.
  name: Adobe Suite Tfa/provider/u2fkey/authentication Challenge API
  phrasing_intents:
  - id: PostV1TfaProviderU2fkeyAuthenticationchallenge
    intent: Start a U2F security key challenge
    question: What WebAuthn challenge data do I need before signing in with a security key?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-u2fkey-authentication-challenge-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/u2fkey/configure API from Adobe Suite — 1 operation(s) for tfa/provider/u2fkey/configure.
  name: Adobe Suite Tfa/provider/u2fkey/configure API
  phrasing_intents:
  - id: PostV1TfaProviderU2fkeyConfigure
    intent: Start registering a WebAuthn security key
    question: How do I begin registering a U2F security key for admin two-factor login?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-u2fkey-configure-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/provider/u2fkey/verify API from Adobe Suite — 1 operation(s) for tfa/provider/u2fkey/verify.
  name: Adobe Suite Tfa/provider/u2fkey/verify API
  phrasing_intents:
  - id: PostV1TfaProviderU2fkeyVerify
    intent: Verify a U2F security key and get a token
    question: How does an admin sign in with a U2F security key to get an API token?
  phrasing_ops: 1
  slug: adobe-suite-tfa-provider-u2fkey-verify-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/tfat-providers-to-activate API from Adobe Suite — 1 operation(s) for tfa/tfat-providers-to-activate.
  name: Adobe Suite Tfa/tfat Providers To Activate API
  phrasing_intents:
  - id: GetV1TfaTfatproviderstoactivate
    intent: List two-factor providers still to configure
    question: Which two-factor authentication providers does this admin still need to set up?
  phrasing_ops: 1
  slug: adobe-suite-tfa-tfat-providers-to-activate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The tfa/tfat-user-providers API from Adobe Suite — 1 operation(s) for tfa/tfat-user-providers.
  name: Adobe Suite Tfa/tfat User Providers API
  phrasing_intents:
  - id: GetV1TfaTfatuserproviders
    intent: List a user's available 2FA providers
    question: Which two-factor methods can this admin user sign in with?
  phrasing_ops: 1
  slug: adobe-suite-tfa-tfat-user-providers-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Throttling configuration API from Adobe Suite — 6 operation(s) for throttling configuration.
  name: Adobe Suite Throttling configuration API
  phrasing_intents:
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/post/list_throttlingconfigs.jsonPublic
    intent: List throttling configurations
    question: Which throttling configurations exist in my sandbox?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/post/throttlingconfigs.jsonPublic
    intent: Create a throttling configuration
    question: How do I cap how fast journeys call an external endpoint?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/get/throttlingconfigs_uid.jsonPublic
    intent: Get a throttling configuration
    question: How do I view the settings of one throttling configuration?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/put/throttlingconfigs_uid.jsonPublic
    intent: Update a throttling configuration
    question: How do I change the rate cap on an existing throttling configuration?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/delete/throttlingconfigs_uid.jsonPublic
    intent: Delete a throttling configuration
    question: How do I remove a throttling configuration I no longer need?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/get/throttlingconfigs_uid_candeploy.jsonPublic
    intent: Check if a throttling configuration can be deployed
    question: Is my throttling configuration valid and ready to deploy?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/post/throttlingconfigs_uid_deploy.jsonPublic
    intent: Deploy a throttling configuration
    question: How do I activate a throttling configuration so it starts limiting calls?
  - id: com/adobe/voyager/service/authoring/restapis/v1_0/swaggerendpoints/post/throttlingconfigs_uid_undeploy.jsonPublic
    intent: Undeploy a throttling configuration
    question: How do I stop a deployed throttling configuration from limiting calls?
  phrasing_ops: 8
  slug: adobe-suite-throttling-configuration-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Timesheet API from Adobe Suite — 5 operation(s) for timesheet.
  name: Adobe Suite Timesheet API
  phrasing_intents:
  - id: getTimesheet
    intent: Get a single timesheet
    question: How do I pull up one timesheet by its ID in Workfront?
  - id: editTimesheet
    intent: Edit a single timesheet
    question: How do I update one existing timesheet?
  - id: deleteTimesheet
    intent: Delete a single timesheet
    question: How do I delete one timesheet?
  - id: getTimesheets
    intent: Get several timesheets by ID
    question: Can I fetch multiple timesheets at once if I know their IDs?
  - id: editTimesheets
    intent: Bulk edit multiple timesheets
    question: How do I update many timesheets in one request?
  - id: addTimesheets
    intent: Create a timesheet
    question: How do I create a new timesheet for a user?
  - id: deleteTimesheets
    intent: Bulk delete timesheets
    question: Can I delete several timesheets in one call?
  - id: countTimesheets
    intent: Count timesheets matching filters
    question: How many timesheets are still open this period?
  phrasing_ops: 10
  slug: adobe-suite-timesheet-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Timesheetprofile API from Adobe Suite — 6 operation(s) for timesheetprofile.
  name: Adobe Suite Timesheetprofile API
  phrasing_intents:
  - id: getTimesheetProfile
    intent: Get one timesheet profile
    question: How can I view the settings of a single Workfront timesheet profile?
  - id: editTimesheetProfile
    intent: Edit a single timesheet profile
    question: How do I change the approvers or period on one timesheet profile?
  - id: deleteTimesheetProfile
    intent: Delete one timesheet profile
    question: How do I remove a timesheet profile we no longer use?
  - id: getTimesheetProfiles
    intent: Fetch several timesheet profiles by ID
    question: Can I retrieve multiple timesheet profiles in one call by ID?
  - id: editTimesheetProfiles
    intent: Edit many timesheet profiles at once
    question: Is there a way to update several timesheet profiles in one request?
  - id: addTimesheetProfiles
    intent: Create or copy a timesheet profile
    question: How do I set up a new timesheet profile?
  - id: deleteTimesheetProfiles
    intent: Delete several timesheet profiles at once
    question: Can I delete multiple timesheet profiles in one call?
  - id: replaceTimesheetProfiles
    intent: Replace timesheet profiles with another
    question: How do I move users from an old timesheet profile to a replacement profile?
  phrasing_ops: 11
  slug: adobe-suite-timesheetprofile-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Membership Controller V 2
  name: Adobe Suite Transfers API
  phrasing_intents:
  - id: previewOffersUsingGET
    intent: Preview transfer offers for a membership (v2)
    question: Which offers would carry over if I transfer a membership using the v2 API?
  - id: createTransferUsingPOST
    intent: Transfer subscriptions for a membership (v2)
    question: How do I transfer a customer's VIP subscriptions to a reseller with the v2 endpoint?
  - id: getTransferUsingGET
    intent: Get a subscription transfer's details (v2)
    question: How do I check the status of a transfer through the v2 API?
  - id: previewOffersUsingGET_1
    intent: Preview transfer offers for a membership (v3)
    question: Which offers would move over in a membership transfer on the v3 API?
  - id: createTransferUsingPOST_1
    intent: Transfer subscriptions for a membership (v3)
    question: How do I transfer subscriptions for a membership using the v3 endpoint?
  - id: getTransferUsingGET_1
    intent: Get a subscription transfer's details (v3)
    question: Where do I check a transfer's details on the v3 API?
  phrasing_ops: 6
  slug: adobe-suite-transfers-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Endpoints for transcribing and dubbing audio/video content.
  name: Adobe Suite Translate and lip sync API
  phrasing_intents:
  - id: transcribe
    intent: Transcribe audio or video into captions
    question: How do I generate a transcript and captions for a video?
  - id: dub
    intent: Dub audio or video with optional lip sync
    question: How do I dub a video into another language?
  phrasing_ops: 2
  slug: adobe-suite-translate-and-lip-sync-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Uifilter API from Adobe Suite — 17 operation(s) for uifilter.
  name: Adobe Suite Uifilter API
  phrasing_intents:
  - id: getUIFilter
    intent: Get a saved UI filter by ID
    question: What conditions and settings does a specific saved filter in Workfront contain?
  - id: editUIFilter
    intent: Update a saved UI filter
    question: How do I change the definition of an existing saved filter?
  - id: deleteUIFilter
    intent: Delete a saved UI filter
    question: How do I remove a saved filter I no longer need?
  - id: getUIFilters
    intent: Get several UI filters by their IDs
    question: Can I load multiple saved filters in a single request?
  - id: editUIFilters
    intent: Bulk-update several UI filters
    question: Can I edit many saved filters at once instead of one by one?
  - id: addUIFilters
    intent: Create or copy a UI filter
    question: How do I create a new saved filter for a list view?
  - id: deleteUIFilters
    intent: Delete several UI filters at once
    question: Can I delete a batch of saved filters in one request?
  - id: countUIFilters
    intent: Count UI filters matching criteria
    question: How many saved filters exist in our Workfront instance?
  phrasing_ops: 22
  slug: adobe-suite-uifilter-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Uigroupby API from Adobe Suite — 15 operation(s) for uigroupby.
  name: Adobe Suite Uigroupby API
  phrasing_intents:
  - id: getUIGroupBy
    intent: Look up one list grouping
    question: How do I read the definition of one saved grouping used in Workfront lists?
  - id: editUIGroupBy
    intent: Update one list grouping
    question: What's the call to change how an existing grouping organizes list rows?
  - id: deleteUIGroupBy
    intent: Delete one list grouping
    question: Can I delete a grouping nobody uses anymore?
  - id: getUIGroupBys
    intent: Fetch several list groupings by ID
    question: Can I load multiple groupings at once when I have their IDs?
  - id: editUIGroupBys
    intent: Update many list groupings at once
    question: How do I bulk edit several groupings in one request?
  - id: addUIGroupBys
    intent: Create or copy a list grouping
    question: How do I create a new grouping for organizing list views?
  - id: deleteUIGroupBys
    intent: Delete many list groupings at once
    question: Can I bulk delete a list of groupings by ID?
  - id: countUIGroupBys
    intent: Count list groupings
    question: How many groupings match a given filter?
  phrasing_ops: 20
  slug: adobe-suite-uigroupby-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Uitemplate API from Adobe Suite — 7 operation(s) for uitemplate.
  name: Adobe Suite Uitemplate API
  phrasing_intents:
  - id: getUITemplate
    intent: Get one layout template
    question: What does a specific layout template contain?
  - id: deleteUITemplate
    intent: Delete a layout template
    question: How do I delete one UI layout template?
  - id: getUITemplates
    intent: Get several layout templates by ID
    question: Can I fetch multiple UI templates in one request?
  - id: deleteUITemplates
    intent: Delete several layout templates
    question: Can I bulk delete UI templates?
  - id: countUITemplates
    intent: Count layout templates
    question: How many UI templates are defined?
  - id: searchUITemplates
    intent: Search layout templates
    question: How do I find UI templates by name?
  - id: reportUITemplates
    intent: Run a report on layout templates
    question: Can I get an aggregated report of UI templates?
  - id: uITemplateMigrateCustomersAllLayoutTemplates
    intent: Migrate all legacy layout templates
    question: How do I migrate every legacy layout template to the new experience?
  phrasing_ops: 9
  slug: adobe-suite-uitemplate-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Uiview API from Adobe Suite — 16 operation(s) for uiview.
  name: Adobe Suite Uiview API
  phrasing_intents:
  - id: getUIView
    intent: Get a single UI view
    question: How do I fetch one saved UI view by its ID in Workfront?
  - id: editUIView
    intent: Edit a single UI view
    question: How can I change the settings of one existing UI view?
  - id: deleteUIView
    intent: Delete a single UI view
    question: How do I remove one UI view I no longer need?
  - id: getUIViews
    intent: Get several UI views by their IDs
    question: Can I load several UI views at once if I have their IDs?
  - id: editUIViews
    intent: Bulk edit multiple UI views
    question: How do I update many UI views in a single request?
  - id: addUIViews
    intent: Create or copy a UI view
    question: How do I create a new UI view in Workfront?
  - id: deleteUIViews
    intent: Bulk delete multiple UI views
    question: Can I delete several UI views in one call?
  - id: countUIViews
    intent: Count UI views matching filters
    question: How many UI views exist in our instance?
  phrasing_ops: 21
  slug: adobe-suite-uiview-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Union schemas aggregate the fields of all schemas that implement the same class (such as ExperienceEvent or Profile) into a single schema. They are used by Real-time Customer Profile to merge data tog
  name: Adobe Suite Unions API
  phrasing_intents:
  - id: listUnionSchemas
    intent: List union schemas
    question: Which union schemas exist in my Experience Platform sandbox?
  - id: retrieveUnionSchema
    intent: Get one union schema
    question: How do I view the merged fields of a specific union schema?
  phrasing_ops: 2
  slug: adobe-suite-unions-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Update API from Adobe Suite — 12 operation(s) for update.
  name: Adobe Suite Update API
  phrasing_intents:
  - id: updateAuditSessionCount
    intent: Count audit sessions for a user
    question: How many audit sessions did a user have in a date range?
  - id: updateRecentUpdatesObjIDs
    intent: Get IDs of recently updated objects
    question: Which objects have recent updates?
  - id: getUpdateAuditSession
    intent: Get audit session activity
    question: What did a user change during their audit sessions?
  - id: getUpdateEndorsementUpdates
    intent: Get endorsement updates
    question: What endorsements has a user received lately?
  - id: getUpdateObjectUpdates
    intent: Get the update feed for an object
    question: What updates have been posted on a specific project or task?
  - id: getUpdateObjectUpdatesByCommentID
    intent: Get object updates around a comment
    question: Can I load an object's update feed positioned at a particular comment?
  - id: getUpdateObjectUpdatesMobile
    intent: Get an object's updates for mobile
    question: Is there a mobile-formatted feed of updates for an object?
  - id: getUpdateObjectUpdatesWithNoteAndJournalEntryIndex
    intent: Get object updates from a note/journal index
    question: Can I page an object's updates starting from a given note and journal entry?
  phrasing_ops: 12
  slug: adobe-suite-update-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Image upscaling with the precise upsampler.
  name: Adobe Suite Upscale API
  phrasing_intents:
  - id: preciseUpsamplerV3Async
    intent: Upscale an image to higher resolution
    question: How do I upscale a low-resolution image with Firefly?
  phrasing_ops: 1
  slug: adobe-suite-upscale-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Usage Logs API from Adobe Suite — 1 operation(s) for usage logs.
  name: Adobe Suite Usage Logs API
  phrasing_intents:
  - id: getUsageAccessLogs
    intent: Get Analytics usage and access logs
    question: Who logged into Adobe Analytics or accessed a report suite in a given date range?
  phrasing_ops: 1
  slug: adobe-suite-usage-logs-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The User API from Adobe Suite — 27 operation(s) for user.
  name: Adobe Suite User API
  phrasing_intents:
  - id: getUser
    intent: Get one Workfront user by ID
    question: What details can I pull for a single Workfront user if I know their ID?
  - id: editUser
    intent: Update a single user's profile
    question: How do I change a single user's details in Workfront?
  - id: deleteUser
    intent: Delete a single user
    question: How do I remove one user from Workfront?
  - id: getUsers
    intent: Get several users by their IDs
    question: Can I fetch a batch of Workfront users in one call by listing their IDs?
  - id: editUsers
    intent: Update many users in one request
    question: Can I bulk edit a group of users in a single request?
  - id: addUsers
    intent: Create a new user
    question: How do I add a new person as a user in Workfront?
  - id: deleteUsers
    intent: Delete several users at once
    question: Can I delete a whole list of users in one call?
  - id: replaceUsers
    intent: Replace users with another user
    question: How do I hand over a departing user's assignments to someone else?
  phrasing_ops: 32
  slug: adobe-suite-user-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Marketo Engage provides a set of User Management endpoints allow you to perform CRUD operations on user records in Marketo.
  name: Adobe Suite User Management API
  phrasing_intents:
  - id: getUsersUsingGET
    intent: List all users
    question: How do I get a list of every user in my Marketo instance?
  - id: inviteUserUsingPOST
    intent: Invite a new user by email
    question: How can I send an email invitation to add a new user?
  - id: getRolesUsingGET
    intent: List available roles
    question: What roles can be assigned to users?
  - id: getWorkspacesUsingGET
    intent: List workspaces
    question: Which workspaces exist that users can be given access to?
  - id: deleteUserUsingPOST
    intent: Delete an active user
    question: How do I remove a user who has already accepted their invitation?
  - id: deleteInvitedUserUsingPOST
    intent: Revoke a pending user invitation
    question: Can I cancel an invitation that someone hasn't accepted yet?
  - id: updateUserAttributeUsingPOST
    intent: Update a user's attributes
    question: How do I change a user's name or email address?
  - id: getUserRolesAndWorkspacesUsingGET
    intent: Get a user's roles and workspaces
    question: Which roles and workspaces does a specific user have?
  phrasing_ops: 12
  slug: adobe-suite-user-management-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Sandbox operations available to all users.
  name: Adobe Suite User operations API
  phrasing_intents:
  - id: listAvailableSandboxes
    intent: List sandboxes available to the current user
    question: Which Experience Platform sandboxes can I access with my user token?
  - id: listPackages
    intent: List sandbox tooling packages
    question: Which sandbox tooling packages have been created in my organization?
  - id: createPackage
    intent: Create a multi-artifact sandbox package
    question: How do I bundle schemas and datasets from one sandbox into a package for export?
  - id: updatePackage
    intent: Add or remove artifacts in a package
    question: How do I add another artifact to a sandbox package I already created?
  - id: submitImport
    intent: Submit a package import into a sandbox
    question: Once I've reviewed conflicts, how do I actually import a published package into a sandbox?
  - id: listJobs
    intent: List sandbox export and import jobs
    question: Which sandbox export or import jobs are running or have failed?
  - id: makePackagePublic
    intent: Change a package's visibility to public
    question: How do I make a private sandbox package public so other organizations can pull it?
  - id: lookUpPackage
    intent: Look up a sandbox package
    question: What artifacts and status does a specific sandbox package have?
  phrasing_ops: 22
  slug: adobe-suite-user-operations-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Userapproval API from Adobe Suite — 7 operation(s) for userapproval.
  name: Adobe Suite Userapproval API
  phrasing_intents:
  - id: getUserApproval
    intent: Get a single user approval record
    question: How do I look up one Workfront user approval record by ID?
  - id: deleteUserApproval
    intent: Delete one user approval record
    question: Can I delete a single user approval record?
  - id: getUserApprovals
    intent: Get several user approvals by ID
    question: Can I fetch several user approval records at once by ID?
  - id: addUserApprovals
    intent: Create a user approval record
    question: How do I create a new user approval record?
  - id: deleteUserApprovals
    intent: Delete many user approval records
    question: Can I delete a list of user approval records in one call?
  - id: countUserApprovals
    intent: Count user approval records
    question: How many user approval records are there?
  - id: searchUserApprovals
    intent: Search user approval records
    question: Which user approval records are still waiting on a decision?
  - id: reportUserApprovals
    intent: Run a report on user approvals
    question: Can I get an aggregated report of user approval records?
  phrasing_ops: 10
  slug: adobe-suite-userapproval-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Useravailability API from Adobe Suite — 5 operation(s) for useravailability.
  name: Adobe Suite Useravailability API
  phrasing_intents:
  - id: getUserAvailability
    intent: Get one user availability record
    question: What does a specific user availability entry show?
  - id: deleteUserAvailability
    intent: Delete a user availability record
    question: How do I remove one user availability entry?
  - id: getUserAvailabilitys
    intent: Get several availability records by ID
    question: Can I fetch multiple user availability records in one call?
  - id: addUserAvailabilitys
    intent: Create a user availability record
    question: How do I record a user's availability for capacity planning?
  - id: deleteUserAvailabilitys
    intent: Delete several availability records
    question: Can I bulk delete user availability records?
  - id: countUserAvailabilitys
    intent: Count user availability records
    question: How many user availability records exist?
  - id: searchUserAvailabilitys
    intent: Search user availability records
    question: How do I find availability entries for a particular user?
  - id: reportUserAvailabilitys
    intent: Run a report on user availability
    question: Can I get an aggregated availability report across users?
  phrasing_ops: 8
  slug: adobe-suite-useravailability-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Userdelegation API from Adobe Suite — 5 operation(s) for userdelegation.
  name: Adobe Suite Userdelegation API
  phrasing_intents:
  - id: getUserDelegation
    intent: Get one user delegation by ID
    question: How do I read a single Workfront user delegation?
  - id: editUserDelegation
    intent: Edit a single user delegation
    question: What call changes the dates on one work delegation?
  - id: deleteUserDelegation
    intent: Delete a single user delegation
    question: How do I end and remove one user delegation?
  - id: getUserDelegations
    intent: Get several user delegations by ID
    question: Can I load several delegations by their IDs at once?
  - id: editUserDelegations
    intent: Bulk edit user delegations
    question: How do I update many user delegations in one request?
  - id: addUserDelegations
    intent: Create a user delegation
    question: How do I delegate my work to someone while I am out?
  - id: deleteUserDelegations
    intent: Bulk delete user delegations
    question: Can I delete several user delegations in one call?
  - id: countUserDelegations
    intent: Count user delegations
    question: How many user delegations match a filter?
  phrasing_ops: 10
  slug: adobe-suite-userdelegation-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Userhomecalendarpreference API from Adobe Suite — 5 operation(s) for userhomecalendarpreference.
  name: Adobe Suite Userhomecalendarpreference API
  phrasing_intents:
  - id: getUserHomeCalendarPreference
    intent: Look up one home calendar preference
    question: How do I read a user's Home calendar preference record in Workfront?
  - id: editUserHomeCalendarPreference
    intent: Update one home calendar preference
    question: Can I change a user's Home calendar display settings?
  - id: deleteUserHomeCalendarPreference
    intent: Delete one home calendar preference
    question: How do I remove a single Home calendar preference record?
  - id: getUserHomeCalendarPreferences
    intent: Fetch several home calendar preferences by ID
    question: Can I retrieve many users' calendar preferences at once by ID?
  - id: editUserHomeCalendarPreferences
    intent: Update many home calendar preferences at once
    question: Is there a bulk edit for Home calendar preferences?
  - id: addUserHomeCalendarPreferences
    intent: Create a home calendar preference
    question: How do I create a new Home calendar preference for a user?
  - id: deleteUserHomeCalendarPreferences
    intent: Delete many home calendar preferences
    question: Can I bulk delete Home calendar preferences by ID?
  - id: countUserHomeCalendarPreferences
    intent: Count home calendar preferences
    question: How many Home calendar preference records match a filter?
  phrasing_ops: 10
  slug: adobe-suite-userhomecalendarpreference-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Usernote API from Adobe Suite — 23 operation(s) for usernote.
  name: Adobe Suite Usernote API
  phrasing_intents:
  - id: getUserNote
    intent: Get one Workfront user notification
    question: How do I look up a single user notification by its ID in Workfront?
  - id: getUserNotes
    intent: Fetch several user notes by ID at once
    question: Is there a way to pull a batch of user notes in one call by listing their IDs?
  - id: addUserNotes
    intent: Create a user note
    question: How do I create a new user note in Workfront through the API?
  - id: countUserNotes
    intent: Count user notes matching a filter
    question: How many user notes match a given filter?
  - id: searchUserNotes
    intent: Search user notes with filters
    question: What's the way to search user notes by field values in Workfront?
  - id: reportUserNotes
    intent: Run an aggregate report on user notes
    question: Can I run a grouped or aggregated report over user notes?
  - id: userNoteAcknowledge
    intent: Mark one notification as read
    question: How do I acknowledge a single notification so it stops showing as unread?
  - id: userNoteAcknowledgeAll
    intent: Mark all my notifications as read
    question: Is there a way to clear every unread notification in one go?
  phrasing_ops: 24
  slug: adobe-suite-usernote-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Userobjectpref API from Adobe Suite — 5 operation(s) for userobjectpref.
  name: Adobe Suite Userobjectpref API
  phrasing_intents:
  - id: getUserObjectPref
    intent: Get a user object preference
    question: How do I read one Workfront user object preference by ID?
  - id: deleteUserObjectPref
    intent: Delete a user object preference
    question: How do I delete one saved user object preference?
  - id: getUserObjectPrefs
    intent: Get several user object preferences
    question: How do I fetch many user object preferences in one call?
  - id: deleteUserObjectPrefs
    intent: Bulk delete user object preferences
    question: How do I remove several user object preferences at once?
  - id: countUserObjectPrefs
    intent: Count user object preferences
    question: How many user object preferences are stored?
  - id: searchUserObjectPrefs
    intent: Search user object preferences
    question: How do I search user object preferences for a particular user?
  - id: reportUserObjectPrefs
    intent: Run a report on user object preferences
    question: Can I get grouped report data over user object preferences?
  phrasing_ops: 7
  slug: adobe-suite-userobjectpref-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Userprefvalue API from Adobe Suite — 3 operation(s) for userprefvalue.
  name: Adobe Suite Userprefvalue API
  phrasing_intents:
  - id: getUserPrefValue
    intent: Look up one user preference value
    question: How do I read a single stored user preference value in Workfront?
  - id: deleteUserPrefValue
    intent: Delete one user preference value
    question: How do I clear a single saved user preference?
  - id: getUserPrefValues
    intent: Fetch several user preference values by ID
    question: Can I retrieve a batch of user preference values by ID?
  - id: addUserPrefValues
    intent: Save a new user preference value
    question: How do I store a new preference setting for a user?
  - id: deleteUserPrefValues
    intent: Delete many user preference values
    question: Can I bulk delete saved user preferences by ID?
  - id: searchUserPrefValues
    intent: Search user preference values
    question: How do I find the saved preferences for a particular user?
  phrasing_ops: 6
  slug: adobe-suite-userprefvalue-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Users API from Adobe Suite — 2 operation(s) for users.
  name: Adobe Suite Users API
  phrasing_intents:
  - id: getByGlobalCompanyIdUsers
    intent: List all users in the company
    question: Who are all the Analytics users in my company?
  - id: getCurrentUser
    intent: Get the current Analytics user
    question: Which Adobe Analytics user am I authenticated as?
  phrasing_ops: 2
  slug: adobe-suite-users-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Provides advanced dataset updates with dynamic merging and automatic creation of nested objects, simplifying modifications and reducing errors.
  name: Adobe Suite V2 Datasets API
  phrasing_intents:
  - id: patchDataSetV2
    intent: Update a dataset's description, tags or metadata
    question: How do I change the description or tags on an Experience Platform dataset?
  phrasing_ops: 1
  slug: adobe-suite-v2-datasets-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Variables API from Adobe Suite — 2 operation(s) for variables.
  name: Adobe Suite Variables API
  phrasing_intents:
  - id: getEnvironmentVariables
    intent: List an environment's user variables
    question: Which custom variables are set on my Cloud Service environment?
  - id: patchEnvironmentVariables
    intent: Set or remove environment variables
    question: How do I change several environment variables at once?
  - id: getPipelineVariables
    intent: List a pipeline's user variables
    question: Which build variables are defined on my CI/CD pipeline?
  - id: patchPipelineVariables
    intent: Set or remove pipeline variables
    question: How do I change several pipeline variables in one update?
  phrasing_ops: 4
  slug: adobe-suite-variables-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Work API from Adobe Suite — 24 operation(s) for work.
  name: Adobe Suite Work API
  phrasing_intents:
  - id: getWork
    intent: Get one work item by ID
    question: How can I look up a single Workfront work item when I already have its ID?
  - id: getWorks
    intent: Fetch several work items by ID at once
    question: Is there a way to pull a batch of work items in one call by passing a list of IDs?
  - id: countWorks
    intent: Count work items matching filters
    question: How many work items match a given filter in Workfront?
  - id: searchWorks
    intent: Search work items with filters
    question: How do I search work items by status, assignee or other filters?
  - id: reportWorks
    intent: Run an aggregate report on work items
    question: Can I get grouped or aggregated report data about work items rather than raw records?
  - id: workGetMyAccomplishmentsCount
    intent: Count my completed accomplishments
    question: How many accomplishments have I completed in Workfront?
  - id: workGetMyWorkCount
    intent: Count the work assigned to me
    question: How many items are currently in my work list?
  - id: workGetMyWorkCountFiltered
    intent: Count my assigned work with a filter
    question: Can I count only the part of my assigned work that matches a filter?
  phrasing_ops: 24
  slug: adobe-suite-work-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Workflow collection
  name: Adobe Suite Workflow Resource API
  phrasing_intents:
  - id: getWorkflow
    intent: Get a Campaign workflow
    question: Can I retrieve one Adobe Campaign workflow by its ID?
  phrasing_ops: 1
  slug: adobe-suite-workflow-resource-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: The Workitem API from Adobe Suite — 6 operation(s) for workitem.
  name: Adobe Suite Workitem API
  phrasing_intents:
  - id: getWorkItem
    intent: Get a single work item
    question: How do I look up one work item from someone's work list by ID?
  - id: editWorkItem
    intent: Edit a single work item
    question: How can I update one work item?
  - id: deleteWorkItem
    intent: Delete a single work item
    question: How do I delete one work item?
  - id: getWorkItems
    intent: Get several work items by ID
    question: Can I fetch multiple work items in one call?
  - id: editWorkItems
    intent: Edit many work items in one request
    question: Is there a bulk edit for work items?
  - id: deleteWorkItems
    intent: Delete several work items at once
    question: Can I bulk delete work items by ID?
  - id: countWorkItems
    intent: Count work items
    question: How many work items are in the system?
  - id: searchWorkItems
    intent: Search work items with filters
    question: How do I search work items assigned to a particular user?
  phrasing_ops: 10
  slug: adobe-suite-workitem-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Workspace Controller
  name: Adobe Suite Workspaces API
  phrasing_intents:
  - id: getWorkspaces
    intent: List Workfront Planning workspaces
    question: Which Workfront Planning workspaces can I see?
  - id: getWorkspace
    intent: Get a Planning workspace
    question: What's in one Planning workspace, looked up by its ID?
  phrasing_ops: 2
  slug: adobe-suite-workspaces-api
- baseURL: https://api.adobe.io/sign
  baseurl_source: declared
  description: The Access Request API from Adobe Suite — 11 operation(s) for access request.
  name: Adobe Suite Access Request API
  phrasing_intents:
  - id: getAccessRequest
    intent: Get one access request
    question: How do I view the details of a single access request in Workfront?
  - id: editAccessRequest
    intent: Update an access request
    question: Can I change the details of an existing access request?
  - id: deleteAccessRequest
    intent: Delete an access request
    question: How do I delete one access request?
  - id: getAccessRequests
    intent: Fetch several access requests by ID
    question: Can I load multiple access requests in one call by their IDs?
  - id: editAccessRequests
    intent: Bulk update access requests
    question: How do I edit many access requests in a single request?
  - id: addAccessRequests
    intent: Create an access request
    question: How do I request access to an object in Workfront via the API?
  - id: deleteAccessRequests
    intent: Bulk delete access requests
    question: Can I delete several access requests at once by ID?
  - id: countAccessRequests
    intent: Count access requests
    question: How many access requests match a filter?
  phrasing_ops: 16
  slug: adobe-suite-access-request-api
- baseURL: https://api.adobe.io/sign
  baseurl_source: declared
  description: The Activity Log API from Adobe Suite — 4 operation(s) for activity log.
  name: Adobe Suite Activity Log API
  phrasing_intents:
  - id: getActivityLog
    intent: Get one activity log entry
    question: How do I read a single activity log entry by its ID?
  - id: getActivityLogs
    intent: Fetch several activity log entries by ID
    question: Can I load multiple activity log entries in one request?
  - id: countActivityLogs
    intent: Count activity log entries
    question: How many activity log entries have been recorded?
  - id: searchActivityLogs
    intent: Search the activity log
    question: What activity happened recently, and how do I search the log for it?
  phrasing_ops: 4
  slug: adobe-suite-activity-log-api
- baseURL: https://api.adobe.io/sign
  baseurl_source: declared
  description: The Approval Process API from Adobe Suite — 5 operation(s) for approval process.
  name: Adobe Suite Approval Process API
  phrasing_intents:
  - id: getApprovalProcess
    intent: Look up one approval process
    question: How do I view a single approval process and its setup?
  - id: editApprovalProcess
    intent: Update an approval process
    question: Can I change the stages or approvers of an existing approval process?
  - id: deleteApprovalProcess
    intent: Delete an approval process
    question: How do I remove an approval process we no longer use?
  - id: getApprovalProcesss
    intent: Fetch several approval processes by ID
    question: Can I load multiple approval processes at once by their IDs?
  - id: editApprovalProcesss
    intent: Update many approval processes at once
    question: Is there a bulk edit for approval processes?
  - id: addApprovalProcesss
    intent: Create or copy an approval process
    question: How do I set up a new approval process?
  - id: deleteApprovalProcesss
    intent: Delete many approval processes
    question: Can I delete a list of approval processes in one request?
  - id: countApprovalProcesss
    intent: Count approval processes
    question: How many approval processes are configured?
  phrasing_ops: 10
  slug: adobe-suite-approval-process-api
- baseURL: https://api.adobe.io/sign
  baseurl_source: declared
  description: The Background Job API from Adobe Suite — 5 operation(s) for background job.
  name: Adobe Suite Background Job API
  phrasing_intents:
  - id: getBackgroundJob
    intent: Get a background job
    question: How do I check on one background job by its ID?
  - id: deleteBackgroundJob
    intent: Delete a background job
    question: Can I remove a single background job record?
  - id: getBackgroundJobs
    intent: Fetch several background jobs by ID
    question: Can I retrieve multiple background jobs in one call using their IDs?
  - id: addBackgroundJobs
    intent: Create a background job
    question: How do I create a new background job?
  - id: deleteBackgroundJobs
    intent: Bulk delete background jobs
    question: Is it possible to delete many background jobs in one request?
  - id: countBackgroundJobs
    intent: Count background jobs
    question: How many background jobs are there?
  - id: searchBackgroundJobs
    intent: Search background jobs
    question: What's the way to search background jobs by status or other attributes?
  - id: reportBackgroundJobs
    intent: Report on background jobs
    question: Can I get an aggregated report of background jobs?
  phrasing_ops: 8
  slug: adobe-suite-background-job-api
- baseURL: https://api.adobe.io/sign
  baseurl_source: declared
  description: The Document Request API from Adobe Suite — 5 operation(s) for document request.
  name: Adobe Suite Document Request API
  phrasing_intents:
  - id: getDocumentRequest
    intent: Look up one document request
    question: How do I see the details of a single document request?
  - id: editDocumentRequest
    intent: Update a document request
    question: Can I change an existing request for a document?
  - id: deleteDocumentRequest
    intent: Delete a document request
    question: How do I cancel and remove a document request?
  - id: getDocumentRequests
    intent: Fetch several document requests by ID
    question: Can I retrieve multiple document requests at once by ID?
  - id: editDocumentRequests
    intent: Update many document requests at once
    question: Is there a bulk edit for document requests?
  - id: addDocumentRequests
    intent: Request a document from someone
    question: How do I ask a teammate to provide a document in Workfront?
  - id: deleteDocumentRequests
    intent: Delete many document requests
    question: Can I delete several document requests at once?
  - id: countDocumentRequests
    intent: Count document requests
    question: How many document requests are outstanding?
  phrasing_ops: 10
  slug: adobe-suite-document-request-api
- baseURL: https://api.adobe.io/sign
  baseurl_source: declared
  description: The Exchange Rate API from Adobe Suite — 7 operation(s) for exchange rate.
  name: Adobe Suite Exchange Rate API
  phrasing_intents:
  - id: getExchangeRate
    intent: Get one currency exchange rate
    question: What rate is stored on a specific exchange rate record in Workfront?
  - id: editExchangeRate
    intent: Edit a single exchange rate
    question: How do I change the conversion rate on one existing exchange rate record?
  - id: deleteExchangeRate
    intent: Delete a single exchange rate
    question: Can I remove one exchange rate that was entered by mistake?
  - id: getExchangeRates
    intent: Fetch several exchange rates by ID
    question: Can I fetch a batch of exchange rates in one call when I know their IDs?
  - id: editExchangeRates
    intent: Edit many exchange rates at once
    question: Is it possible to update the rates on many exchange rate records in one request?
  - id: addExchangeRates
    intent: Add a new currency exchange rate
    question: How do I add a new exchange rate for a foreign currency in Workfront?
  - id: deleteExchangeRates
    intent: Delete several exchange rates by ID
    question: Can I remove a batch of exchange rates in a single call?
  - id: countExchangeRates
    intent: Count exchange rates matching filters
    question: How many exchange rates are defined in my Workfront instance?
  phrasing_ops: 12
  slug: adobe-suite-exchange-rate-api
- baseURL: https://api.adobe.io/sign
  baseurl_source: declared
  description: The Financial Data API from Adobe Suite — 5 operation(s) for financial data.
  name: Adobe Suite Financial Data API
  phrasing_intents:
  - id: getFinancialData
    intent: Get one financial data record
    question: What planned and actual figures does a specific financial data record hold?
  - id: getFinancialDatas
    intent: Get several financial data records by ID
    question: Can I fetch multiple financial data records in one call?
  - id: countFinancialDatas
    intent: Count financial data records
    question: How many financial data records are there?
  - id: searchFinancialDatas
    intent: Search financial data
    question: How do I find financial data for a given project or period?
  - id: reportFinancialDatas
    intent: Run a report on financial data
    question: Can I get aggregated totals of financial data grouped by project?
  phrasing_ops: 5
  slug: adobe-suite-financial-data-api
- baseURL: https://api.adobe.io/sign
  baseurl_source: declared
  description: The Hour Type API from Adobe Suite — 11 operation(s) for hour type.
  name: Adobe Suite Hour Type API
  phrasing_intents:
  - id: getHourType
    intent: Get one hour type by ID
    question: How can I see the details of a single Workfront hour type?
  - id: editHourType
    intent: Edit a single hour type
    question: How do I change the name or settings of one existing hour type?
  - id: deleteHourType
    intent: Delete one hour type
    question: How do I remove a single hour type I no longer use?
  - id: getHourTypes
    intent: Fetch several hour types by ID
    question: Can I retrieve a batch of hour types by passing multiple IDs at once?
  - id: editHourTypes
    intent: Edit many hour types in one request
    question: Is there a way to update several hour types together in a single request?
  - id: addHourTypes
    intent: Create a new hour type
    question: How do I add a new hour type for people to log time against?
  - id: deleteHourTypes
    intent: Delete several hour types at once
    question: Can I delete multiple hour types in a single call?
  - id: replaceHourTypes
    intent: Replace hour types with another hour type
    question: How do I swap references to old hour types over to a replacement hour type?
  phrasing_ops: 16
  slug: adobe-suite-hour-type-api
- baseURL: https://api.adobe.io/sign
  baseurl_source: declared
  description: The Journal Entry API from Adobe Suite — 7 operation(s) for journal entry.
  name: Adobe Suite Journal Entry API
  phrasing_intents:
  - id: getJournalEntry
    intent: Get a single journal entry
    question: How do I read one journal entry from Workfront's update history?
  - id: getJournalEntrys
    intent: Get several journal entries by ID
    question: Can I load a list of journal entries by their IDs at once?
  - id: countJournalEntrys
    intent: Count journal entries matching filters
    question: How many journal entries were logged for a project?
  - id: searchJournalEntrys
    intent: Search journal entries
    question: How do I find journal entries recording a particular change?
  - id: reportJournalEntrys
    intent: Run a report over journal entries
    question: Can I get an aggregated report of journal entries?
  - id: journalEntryLike
    intent: Like a journal entry
    question: How do I like an update in someone's journal feed?
  - id: journalEntryUnlike
    intent: Remove a like from a journal entry
    question: How do I take back a like I put on a journal entry?
  phrasing_ops: 7
  slug: adobe-suite-journal-entry-api
- baseURL: https://api.adobe.io/sign
  baseurl_source: declared
  description: The Resource Manager API from Adobe Suite — 5 operation(s) for resource manager.
  name: Adobe Suite Resource Manager API
  phrasing_intents:
  - id: getResourceManager
    intent: Get a single resource manager assignment
    question: How do I look up one resource manager record by ID?
  - id: deleteResourceManager
    intent: Delete a single resource manager record
    question: How do I remove one resource manager from a project?
  - id: getResourceManagers
    intent: Get several resource managers by ID
    question: Can I fetch multiple resource manager records at once?
  - id: addResourceManagers
    intent: Create a resource manager record
    question: How do I add someone as a resource manager?
  - id: deleteResourceManagers
    intent: Delete several resource managers at once
    question: Can I bulk delete resource manager records?
  - id: countResourceManagers
    intent: Count resource manager records
    question: How many resource manager records exist?
  - id: searchResourceManagers
    intent: Search resource managers with filters
    question: How do I find resource managers for a given project?
  - id: reportResourceManagers
    intent: Run a report on resource managers
    question: Can I get aggregated report data about resource managers?
  phrasing_ops: 8
  slug: adobe-suite-resource-manager-api
artifact_total: 535
asyncapis:
- description: ''
  name: Adobe Suite Webhooks
  slug: adobe-suite-webhooks
collections:
- collection_type: open
  name: Bulk Data Insertion API (BDIA)
  slug: open-adobe-suite-analytics-bulk-data-insertion
- collection_type: open
  name: Adobe Analytics Classification API
  slug: open-adobe-suite-analytics-classification
- collection_type: open
  name: Data Repair API
  slug: open-adobe-suite-analytics-data-repair
- collection_type: open
  name: Adobe Analytics APIs
  slug: open-adobe-suite-analytics
- collection_type: open
  name: Adobe CC Libraries APIs Test
  slug: open-adobe-suite-cc-libraries
- collection_type: open
  name: Firefly Services Audio and Video API
  slug: open-adobe-suite-firefly-audio-video
- collection_type: open
  name: Express API
  slug: open-adobe-suite-firefly-express
- collection_type: open
  name: Illustrator API - Firefly Services
  slug: open-adobe-suite-firefly-illustrator
- collection_type: open
  name: Firefly Services - InDesign API
  slug: open-adobe-suite-firefly-indesign
- collection_type: open
  name: Adobe Lightroom API
  slug: open-adobe-suite-firefly-lightroom
- collection_type: open
  name: Photoshop v2 API endpoints
  slug: open-adobe-suite-firefly-photoshop-v2
- collection_type: open
  name: Translate and Lip Sync API
  slug: open-adobe-suite-firefly-translate-lipsync
- collection_type: open
  name: Firefly API
  slug: open-adobe-suite-firefly
- collection_type: open
  name: Lightroom API Documentation
  slug: open-adobe-suite-lightroom
- collection_type: open
  name: Marketo Engage Rest API
  slug: open-adobe-suite-marketo-identity
- collection_type: open
  name: Marketo Engage Rest API
  slug: open-adobe-suite-marketo-user
- collection_type: open
  name: PDF Services API
  slug: open-adobe-suite-pdf-services
- collection_type: open
  name: Commerce Partner API
  slug: open-adobe-suite-vip-marketplace-partners
- collection_type: open
  name: Unified Approvals API (Deprecated)
  slug: open-adobe-suite-workfront-unified-approvals
- collection_type: open
  name: Adobe Workfront API
  slug: open-adobe-suite-workfront-workflow
common:
- group: company
  title: ''
  type: Website
  url: https://www.adobe.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/capabilities/adobe-suite-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/adobe-suite-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/agentic-access/adobe-suite-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-suite-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/authentication/adobe-suite-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adobe-suite-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/security/adobe-suite-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-suite-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/security/adobe-suite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adobe-suite-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com
- group: auth
  title: ''
  type: Authentication
  url: https://developer.adobe.com/developer-console/docs/guides/authentication/
- group: start
  title: ''
  type: Console
  url: https://developer.adobe.com/console/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.adobe.com/apis
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdobeDocs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://developer.adobe.com/support/
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/openapi/
  title: ''
  type: OpenAPI
  url: openapi/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/packages/adobe-suite-packages.yml
  title: ''
  type: Packages
  url: packages/adobe-suite-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/packages/adobe-suite-packages.yml
  title: ''
  type: SDKs
  url: packages/adobe-suite-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/well-known/adobe-suite-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adobe-suite-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/well-known/adobe-suite-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adobe-suite-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/mcp/adobe-suite-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adobe-suite-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/mcp/adobe-suite-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/adobe-suite-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/llms/adobe-suite-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adobe-suite-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/overlays/
  title: ''
  type: Overlay
  url: overlays/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/conformance/adobe-suite-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adobe-suite-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.adobe.com/trust/compliance/compliance-list.html
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/errors/adobe-suite-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adobe-suite-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/lifecycle/adobe-suite-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adobe-suite-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/lifecycle/adobe-suite-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/adobe-suite-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/scopes/adobe-suite-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/adobe-suite-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/security/adobe-suite-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/adobe-suite-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://helpx.adobe.com/security.html/security/policy.ug.html
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/sandbox/adobe-suite-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/adobe-suite-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/conventions/adobe-suite-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adobe-suite-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/conventions/adobe-suite-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/adobe-suite-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/changelog/adobe-suite-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/adobe-suite-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/cli/adobe-suite-cli.yml
  title: ''
  type: CLI
  url: cli/adobe-suite-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/components/adobe-suite-components.yml
  title: ''
  type: Components
  url: components/adobe-suite-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/data-model/adobe-suite-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adobe-suite-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/asyncapi/adobe-suite-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/adobe-suite-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/rate-limits/adobe-suite-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adobe-suite-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/plans/adobe-suite-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adobe-suite-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/finops/adobe-suite-finops.yml
  title: ''
  type: FinOps
  url: finops/adobe-suite-finops.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/graphql/adobe-suite-graphql.md
  title: ''
  type: GraphQL
  url: graphql/adobe-suite-graphql.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.adobe.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/apis
- group: docs
  title: ''
  type: APIReference
  url: https://developer.adobe.com/apis
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.adobe.com/document-services/pricing/main
- group: start
  title: ''
  type: SignUp
  url: https://developer.adobe.com/console/
created: '2024-01-01'
description: 'Adobe operates one of the largest first-party API estates in software: 70 published OpenAPI and Swagger contracts covering 2,857 operations across Creative Cloud, Document Cloud and Experience Cloud. The surface spans generative AI (Firefly image, video, audio and Substance 3D), creative automation (Photoshop, Lightroom, Illustrator, InDesign, Express), document services (PDF Services, Extract, Accessibility Auto-Tag, Acrobat Sign), marketing and data (Analytics, Experience Platform, Journey Optimizer, Target, Campaign, Marketo Engage), commerce, work management (Workfront), and platform operations (Cloud Manager, User Management, Adobe I/O Events, Status). Every API authenticates through Adobe Identity Management Services (IMS) with an OAuth 2.0 access token plus an x-api-key client ID, provisioned per project and workspace in the Adobe Developer Console.'
features:
- AI-powered generative image creation with Firefly
- PDF document creation, conversion, and OCR
- E-signature workflows with Adobe Sign
- Digital marketing analytics and reporting
- Content management and digital asset management
- Stock photo and asset licensing
- Creative Cloud Libraries for shared design assets
- Cross-channel campaign orchestration
- Video and audio AI-powered production
- Commerce and headless storefront APIs
finops:
- name: Adobe Suite Finops
  service_category: API
  slug: adobe-suite-finops
graphqls:
- description: Integrate with Adobe Commerce through REST and GraphQL APIs for managing products, orders, customers, and building headless commerce experiences.
  name: Adobe Suite GraphQL API
  slug: adobe-suite-graphql
image: /assets/icons/adobe-suite.png
integrations:
- Adobe Creative Cloud
- Adobe Experience Cloud
- Adobe Document Cloud
- Microsoft Office 365
- Salesforce
- SAP
- Workday
- Slack
layout: provider
mcp_servers:
- description: ''
  name: Adobe Suite MCP Server
  slug: adobe-suite-mcp-server
modified: '2026-08-13'
name: Adobe Suite
nav: Providers
network: true
overview: 'Adobe Suite publishes 479 APIs on the [APIs.io](https://apis.io/) network, including Accelerated Queries API, Access Control Policies API, Accesslevel API, and 476 more. Tagged areas include Artificial Intelligence, Analytics, Automation, Commerce, and Creative.


  The Adobe Suite catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Adobe Suite''s developer surface includes authentication, developer portal, developer console, getting-started guide, engineering blog, support, sandbox, and 44 more developer resources.'
plans:
- name: Adobe Suite Plans Pricing
  plan_count: 3
  slug: adobe-suite-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 9
  name: Adobe Suite Rate Limits
  slug: adobe-suite-rate-limits
scopes:
- name: Adobe Suite Scopes
  scope_count: 10
  slug: adobe-suite-scopes
  summary_line: 10 scopes
score:
  band: exemplar
  composite: 78.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.0
    catalog_earned_first_party: 24.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 58.2
    developer_ergonomics: 89.9
    discoverability: 71.7
    operational_transparency: 71.1
  previous_composite: 78.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 82.0
      derived: 0
      marker_coverage: 0.0
      total: 470
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-suite/refs/heads/main/screenshots/adobe-suite-2026-06-20T165033.png
security:
- kind: authentication
  name: Adobe Suite Authentication
  slug: adobe-suite-authentication
  summary_line: apiKey/http · 12 schemes
- kind: domain-security
  name: Adobe Suite Domain Security
  slug: adobe-suite-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Suite Vulnerability Disclosure
  slug: adobe-suite-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Adobe Suite Trust Center
  slug: adobe-suite-trust-center
  summary_line: SOC 2 Type 2, SOC 3, ISO 27001:2022, ISO 27017:2015, ISO 27018:2019, ISO 22301:2019, ISO 9001:2015, PCI DSS, HIPAA ready, FedRAMP Tailored, CSA STAR Level 2, C5 (Germany), IRAP Assessed (Australia), ISMAP Registered (Japan), TISAX, CMMC Level 1, GDPR, CCPA, FERPA ready, GLBA ready
slug: adobe-suite
tags:
- Artificial Intelligence
- Analytics
- Automation
- Commerce
- Creative
- Design
- Documents
- Experience
- Marketing
- Personalization
- Video
use_cases:
- Automated creative asset production
- Document workflow automation and e-signatures
- Marketing campaign orchestration and analytics
- Headless commerce and personalization
- AI-powered content generation and editing
- Enterprise user and entitlement management
website: https://www.adobe.com/
---
