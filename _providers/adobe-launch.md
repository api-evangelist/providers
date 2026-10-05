---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 150
  human_in_the_loop: 0
  name: Adobe Launch Agentic Access
  operation_count: 299
  slug: adobe-launch-agentic-access
  summary_line: 299 operations · 150 acting
api_count: 7
apis:
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage compiled tag library builds for deployment.
  name: Adobe Launch Builds API
  phrasing_intents:
  - id: listLibraryBuilds
    intent: List a tag library's builds
    question: What builds have been made from a tag library?
  - id: createBuild
    intent: Build a tag library
    question: How do I kick off a build of a tag library without sending a payload?
  - id: getBuild
    intent: Look up a tag build
    question: How can I check whether a tag build succeeded?
  - id: republishBuild
    intent: Republish a tag build
    question: Does republishing a tag build require the build ID in both the path and the payload?
  - id: listBuildsForLibrary
    intent: List builds for an event forwarding library
    question: Which builds exist for my event forwarding library?
  - id: postLibrariesByLibraryIdBuilds
    intent: Compile an event forwarding library
    question: How do I compile an event forwarding library into a deployable build?
  - id: getBuildsByBuildId
    intent: Get an event forwarding build
    question: How do I look up an event forwarding build by its ID?
  - id: patchBuildsByBuildId
    intent: Republish an event forwarding build
    question: Can I republish an existing event forwarding build?
  phrasing_ops: 10
  slug: adobe-launch-builds-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage webhook callbacks triggered by audit events.
  name: Adobe Launch Callbacks API
  phrasing_intents:
  - id: listCallbacks
    intent: List a tag property's callbacks
    question: Which webhook callbacks are registered on my Adobe tags property?
  - id: createCallback
    intent: Register a callback on a tag property
    question: How do I get notified at my URL when something changes in a tags property?
  - id: retrieveCallback
    intent: Look up a callback by ID
    question: Where can I see a callback's URL and subscriptions?
  - id: deleteCallback
    intent: Delete a callback
    question: How do I stop a callback from firing to my endpoint?
  - id: updateCallback
    intent: Update a callback
    question: Can I point an existing callback at a new URL?
  - id: listCallbacksForProperty
    intent: List a property's callbacks with date filters
    question: Can I list callbacks updated since a given date?
  - id: postPropertiesByPropertyIdCallbacks
    intent: Register a callback (alternate)
    question: Is there a propertyId endpoint for creating callbacks?
  - id: getCallback
    intent: Look up a callback (alternate)
    question: Is there a callbackId endpoint for fetching one callback?
  phrasing_ops: 10
  slug: adobe-launch-callbacks-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage organization companies.
  name: Adobe Launch Companies API
  phrasing_intents:
  - id: listCompanies
    intent: List the companies I can access
    question: Which companies does my tags account have access to?
  - id: retrieveCompany
    intent: Get a company's tag details
    question: How can I view one company's details by its ID in the tags API?
  - id: listProperties
    intent: List a company's properties
    question: What properties sit under my company?
  - id: createProperty
    intent: Create a property under a company
    question: How do I add a new web or mobile property to my company?
  - id: listAppConfigurations
    intent: List a company's app configurations
    question: Which mobile app configurations are set up for my company?
  - id: createAppConfiguration
    intent: Create an app configuration for a company
    question: How do I register a mobile app's push messaging credentials for my company?
  - id: getCompany
    intent: Look up a company by ID
    question: How do I get a company's details using its companyId?
  phrasing_ops: 7
  slug: adobe-launch-companies-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage data elements for server-side event processing.
  name: Adobe Launch Data Elements API
  phrasing_intents:
  - id: listPropertyDataElements
    intent: List a tag property's data elements
    question: Which data elements are defined in my tag property?
  - id: createDataElement
    intent: Create a data element in a tag property
    question: How do I add a new data element to a web tag property?
  - id: retrieveDataElement
    intent: Get a tag data element
    question: How can I see how one tag data element is configured?
  - id: updateDataElement
    intent: Update a tag data element
    question: Does the data element ID have to appear in both the path and the payload when editing a tag data element?
  - id: listDataElementNotes
    intent: List the notes on a data element
    question: What notes have been left on a data element?
  - id: createNote
    intent: Add a note to a data element
    question: How do I leave a note on a data element for other editors?
  - id: listEventForwardingDataElements
    intent: List an event forwarding property's data elements
    question: Which data elements exist on my event forwarding property?
  - id: createEventForwardingDataElement
    intent: Create an event forwarding data element
    question: How do I add a data element to a server-side event forwarding property?
  phrasing_ops: 14
  slug: adobe-launch-data-elements-api
- baseURL: https://edge.adobedc.net/ee
  baseurl_source: declared
  description: Send event data directly to the Adobe Experience Platform Edge Network. Supports both interactive (interact) and non-interactive (collect) data collection with authenticated and non-authenticated mode
  name: Adobe Launch Edge Network API
  phrasing_intents:
  - id: interact
    intent: Send one event and get personalization back
    question: How do I send a single event to the Edge Network and get personalization decisions back?
  - id: collect
    intent: Send a batch of events for collection
    question: How do I send many events to the Edge Network in one request?
  phrasing_ops: 2
  slug: adobe-launch-edge-network-api-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage environments for event forwarding builds.
  name: Adobe Launch Environments API
  phrasing_intents:
  - id: listEnvironments
    intent: List a tag property's environments
    question: Which environments does my Adobe tags property have?
  - id: createEnvironment
    intent: Create an environment in a tag property
    question: What do I need to add a development environment to a tags property?
  - id: retrieveEnvironment
    intent: Look up an environment by ID
    question: Where can I see one environment's stage and embed details?
  - id: deleteEnvironment
    intent: Delete an environment
    question: How do I remove an old development environment from a property?
  - id: updateEnvironment
    intent: Update an environment
    question: Can I rename an environment or change its host link?
  - id: listBuilds
    intent: List an environment's builds
    question: Which builds have been deployed to this environment?
  - id: listEnvironmentSecrets
    intent: List an environment's secrets
    question: Which secrets are attached to this environment?
  - id: retrieveEnvironmentHost
    intent: Get the host an environment deploys to
    question: Which host does this environment deploy its builds to?
  phrasing_ops: 18
  slug: adobe-launch-environments-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage extension packages that define capabilities, library modules, and views available to Adobe Experience Platform Tags users.
  name: Adobe Launch Extension Packages API
  phrasing_intents:
  - id: listExtensionPackages
    intent: Browse available extension packages
    question: Which extension packages are available in the tags catalog?
  - id: createExtensionPackage
    intent: Upload a new extension package
    question: How do I upload a new extension package I built?
  - id: retrieveExtensionPackage
    intent: Get a tag extension package
    question: How can I see the details and availability of one extension package?
  - id: updateExtensionPackage
    intent: Replace a development package's archive
    question: Can I upload a new archive to an extension package that is still in development?
  - id: privateReleaseExtensionPackage
    intent: Release privately or discontinue a package
    question: How do I make my tested extension package available to every property in my company?
  - id: retrieveExtensionPackageVersion
    intent: Get a tag extension package's versions
    question: What versions of an extension package have been published over time?
  - id: getExtensionPackage
    intent: Look up an extension package by ID
    question: How do I fetch a specific extension package using its identifier?
  - id: patchExtensionPackagesByExtensionPackageId
    intent: Update, release or discontinue a package
    question: Can one PATCH call both upload a new ZIP and privately release an extension package?
  phrasing_ops: 9
  slug: adobe-launch-extension-packages-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage extensions installed in event forwarding properties.
  name: Adobe Launch Extensions API
  phrasing_intents:
  - id: listExtensions
    intent: List a tag property's extensions
    question: Which extensions are installed on my Adobe tags property?
  - id: createExtension
    intent: Install an extension on a tag property
    question: What's needed to add an extension to a tags property?
  - id: retrieveExtension
    intent: Look up an extension by ID
    question: Where can I see one extension's settings and version?
  - id: deleteExtension
    intent: Delete an extension
    question: How do I uninstall an extension from a tags property?
  - id: reviseExtension
    intent: Revise an extension's settings
    question: How do I change an extension's settings, and does it create a new revision?
  - id: retrievePackageForExtension
    intent: Get the package behind an extension
    question: Which extension package was this installed extension built from?
  - id: listExtensionLibraries
    intent: List libraries that use an extension
    question: Which libraries include this extension?
  - id: retrieveExtensionProperty
    intent: Find the property an extension belongs to
    question: Which property is this extension installed on?
  phrasing_ops: 22
  slug: adobe-launch-extensions-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage hosting destinations for tag library delivery.
  name: Adobe Launch Hosts API
  phrasing_intents:
  - id: listHosts
    intent: List a tag property's hosts
    question: Which hosts can my Adobe tags property deploy builds to?
  - id: createHost
    intent: Create a host for a tag property
    question: How do I set up an SFTP host so builds deploy to my own server?
  - id: retrieveHost
    intent: Look up a host by ID
    question: Where can I see a host's type and connection settings?
  - id: deleteHost
    intent: Delete a host
    question: How do I remove a host I no longer deploy to?
  - id: updateHost
    intent: Update an SFTP host
    question: Which kinds of hosts can be edited after creation?
  - id: retrieveHostProperty
    intent: Find the property a host belongs to
    question: Which property owns this host?
  - id: listHostsForProperty
    intent: List a property's hosts with date filters
    question: Can I list hosts created after a certain date?
  - id: postPropertiesByPropertyIdHosts
    intent: Create a host (alternate)
    question: Is there a propertyId endpoint for creating a host?
  phrasing_ops: 11
  slug: adobe-launch-hosts-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage libraries for event forwarding deployment.
  name: Adobe Launch Libraries API
  phrasing_intents:
  - id: listLibraries
    intent: List a tag property's libraries
    question: Which libraries exist under my Adobe tags property?
  - id: createLibrary
    intent: Create a library in a tag property
    question: How do I start a new library to bundle tag changes for publishing?
  - id: retrieveLibrary
    intent: Look up a library by ID
    question: Where can I see the details and current state of one tags library?
  - id: deleteLibrary
    intent: Delete a library
    question: How do I get rid of a tags library I no longer need?
  - id: updateLibrary
    intent: Rename a library or move it through publishing
    question: How do I submit a library for approval in the publishing flow?
  - id: retrieveLibraryProperty
    intent: Find the property a library belongs to
    question: Which property owns this library?
  - id: listLibraryBuilds
    intent: List the builds of a library
    question: How many times has this library been built, and did the builds succeed?
  - id: createBuild
    intent: Build a library
    question: How do I compile a library into a build so it deploys to its environment?
  phrasing_ops: 43
  slug: adobe-launch-libraries-api
- baseURL: https://edge.adobedc.net/ee/va/v1
  baseurl_source: declared
  description: Track media playback events through the Adobe Experience Platform Edge Network. Requires the Streaming Media Collection Add-on. Supports session management, play/pause tracking, buffering, and error r
  name: Adobe Launch Media Edge API
  phrasing_intents:
  - id: mediaSessionStart
    intent: Start a media tracking session
    question: How do I begin tracking a video viewing session through the Edge Network?
  - id: mediaPlay
    intent: Track a media play event
    question: How do I record that playback started or resumed in a media session?
  - id: mediaPing
    intent: Send a media session heartbeat
    question: How often should I ping a media session during playback?
  - id: mediaPauseStart
    intent: Track a media pause event
    question: How do I tell the Edge Network the viewer paused the video?
  - id: mediaBufferStart
    intent: Track a media buffering event
    question: How do I report that a video started buffering?
  - id: mediaBitrateChange
    intent: Track a media bitrate change
    question: How do I report when the stream quality switches to a different bitrate?
  - id: mediaError
    intent: Track a media playback error
    question: How do I report a player error inside a media session?
  - id: mediaSessionComplete
    intent: Complete a media session
    question: How do I mark that a viewer watched the content all the way through?
  phrasing_ops: 9
  slug: adobe-launch-media-edge-api-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage event forwarding properties (edge platform).
  name: Adobe Launch Properties API
  phrasing_intents:
  - id: listProperties
    intent: List a company's tag properties
    question: How do I see every tag property my company owns in Adobe Launch?
  - id: createProperty
    intent: Create a tag property for a company
    question: What do I need to set up a new web or mobile tag property under my company?
  - id: retrieveProperty
    intent: Get a tag property's details
    question: How can I look up the settings of one tag property by its ID?
  - id: deleteProperty
    intent: Delete a tag property
    question: How do I permanently remove a tag property I no longer use?
  - id: updateProperty
    intent: Update a tag property's settings
    question: How do I rename a tag property or change its domains?
  - id: retrievePropertyCompany
    intent: Find the company that owns a tag property
    question: Which company does a particular tag property belong to?
  - id: listCallbacks
    intent: List a property's callbacks
    question: What callback URLs are registered on my tag property?
  - id: createCallback
    intent: Register a callback on a property
    question: How do I get notified at my own URL when things change in a tag property?
  phrasing_ops: 30
  slug: adobe-launch-properties-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage the individual event, condition, and action components within rules.
  name: Adobe Launch Rule Components API
  phrasing_intents:
  - id: listRuleComponents
    intent: List a tag rule's components
    question: Which events, conditions and actions belong to a tag rule?
  - id: createRuleComponent
    intent: Add a component under a tag rule
    question: How do I add an event or action to a tag rule by posting to the rule itself?
  - id: retrieveRuleComponent
    intent: Get a tag rule component
    question: How can I view the settings of one tag rule component?
  - id: deleteRuleComponent
    intent: Delete a tag rule component
    question: How do I remove a condition from a tag rule?
  - id: updateRuleComponent
    intent: Update a tag rule component
    question: Does the component ID need to match in both the path and the payload when editing a tag rule component?
  - id: getRuleComponentExtension
    intent: Find the extension behind a tag rule component
    question: Which extension provides a given tag rule component?
  - id: retrieveRuleComponentOrigin
    intent: Get a rule component's origin revision
    question: Where did this rule component revision originate from?
  - id: listRuleComponentsRelatedRules
    intent: List the rules that use a rule component
    question: Which rules share a particular rule component?
  phrasing_ops: 16
  slug: adobe-launch-rule-components-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage server-side event forwarding rules.
  name: Adobe Launch Rules API
  phrasing_intents:
  - id: listRules
    intent: List a tag property's rules
    question: Which rules are set up on my web tag property?
  - id: createRule
    intent: Create a rule in a tag property
    question: How do I add a rule to a web or mobile tag property?
  - id: retrieveRule
    intent: Get a tag rule's details
    question: How can I pull up a single tag rule by its ID?
  - id: deleteRule
    intent: Delete a tag rule
    question: How do I delete a tag rule we no longer fire?
  - id: updateRule
    intent: Update or revise a tag rule
    question: Can I save a new revision of a tag rule instead of overwriting the current one?
  - id: listRuleComponents
    intent: List a tag rule's components
    question: What events, conditions and actions make up a tag rule?
  - id: createRuleComponent
    intent: Add a component to a tag rule
    question: How do I attach a new event, condition or action to a tag rule?
  - id: listRuleLibraries
    intent: List libraries that include a tag rule
    question: Which libraries is a given tag rule part of?
  phrasing_ops: 23
  slug: adobe-launch-rules-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Search across multiple resource types.
  name: Adobe Launch Search API
  phrasing_intents:
  - id: createSearch
    intent: Search across tag resources
    question: How do I search all my rules and data elements for a name?
  phrasing_ops: 1
  slug: adobe-launch-search-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Manage secrets for authenticating event forwarding rules with external systems. Supports token, simple-http, oauth2, and oauth2-google types.
  name: Adobe Launch Secrets API
  phrasing_intents:
  - id: listPropertySecrets
    intent: List a property's secrets with filters
    question: Which secrets are stored on my tag property?
  - id: createSecret
    intent: Create a secret on a tag property
    question: How do I add a credential to a tag property so rules can use it?
  - id: retrieveSecret
    intent: Get a secret's details
    question: How can I check the status of one secret by its ID?
  - id: deleteSecret
    intent: Delete a secret from a tag property
    question: How do I delete a secret from a tag property?
  - id: testOrRetrySecret
    intent: Test or retry a secret's exchange
    question: Can I manually retry a secret exchange that failed?
  - id: listEnvironmentSecrets
    intent: List secrets scoped to an environment
    question: Which secrets are scoped to a particular tag environment?
  - id: listSecretNotes
    intent: List the notes on a secret
    question: What notes have teammates left on a secret?
  - id: createSecretNote
    intent: Add a note to a secret
    question: How do I leave a note on a secret, such as who owns the credential?
  phrasing_ops: 19
  slug: adobe-launch-secrets-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: The Ad API from Adobe Launch — 3 operation(s) for ad.
  name: Adobe Launch Ad API
  phrasing_intents:
  - id: adStart
    intent: Signal that an ad started
    question: How do I track when an ad begins playing in a media session?
  - id: adComplete
    intent: Signal that an ad finished
    question: How do I record that a viewer watched an ad to the end?
  - id: adSkip
    intent: Signal that an ad was skipped
    question: Can I track when a viewer skips an ad?
  phrasing_ops: 3
  slug: adobe-launch-ad-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: The Ad Break API from Adobe Launch — 2 operation(s) for ad break.
  name: Adobe Launch Ad Break API
  phrasing_intents:
  - id: adBreakStart
    intent: Track the start of an ad break
    question: How do I report that a series of ads began in a video?
  - id: adBreakComplete
    intent: Track the end of an ad break
    question: How do I record that the whole ad series finished?
  phrasing_ops: 2
  slug: adobe-launch-ad-break-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: App configurations allow credentials to be stored and retrieved for later use.
  name: Adobe Launch App configurations API
  phrasing_intents:
  - id: listAppConfigurations
    intent: List a company's app configurations
    question: Which mobile app configurations does my company have in Adobe tags?
  - id: createAppConfiguration
    intent: Create an app configuration
    question: What do I need to set up push messaging credentials for my app?
  - id: retrieveAppConfiguration
    intent: Look up an app configuration
    question: Where can I see the settings of one app configuration?
  - id: deleteAppConfiguration
    intent: Delete an app configuration
    question: How do I remove an app configuration I no longer use?
  - id: updateAppConfiguration
    intent: Update an app configuration
    question: Can I rotate the push credentials in an app configuration?
  - id: retrieveAppConfigurationCompany
    intent: Find the company owning an app configuration
    question: Which company owns this app configuration?
  phrasing_ops: 6
  slug: adobe-launch-app-configurations-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: An audit event is a record of a specific change to another tag resource, generated at the time the change is made. These are system events which can be subscribed to through the use of a callback func
  name: Adobe Launch Audit events API
  phrasing_intents:
  - id: listAuditEvents
    intent: List audit events
    question: What changes have been made across my tag properties recently?
  - id: retrieveAuditEvent
    intent: Get one audit event
    question: How do I see the full details of a single audit event?
  phrasing_ops: 2
  slug: adobe-launch-audit-events-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: The Bitrate API from Adobe Launch — 1 operation(s) for bitrate.
  name: Adobe Launch Bitrate API
  phrasing_intents:
  - id: bitrateChange
    intent: Track a streaming bitrate change
    question: How do I report that the video stream switched bitrate?
  phrasing_ops: 1
  slug: adobe-launch-bitrate-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: The Buffer API from Adobe Launch — 1 operation(s) for buffer.
  name: Adobe Launch Buffer API
  phrasing_intents:
  - id: bufferStart
    intent: Signal that buffering started
    question: How do I report that a video started buffering to Media Edge?
  phrasing_ops: 1
  slug: adobe-launch-buffer-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: The Chapter API from Adobe Launch — 3 operation(s) for chapter.
  name: Adobe Launch Chapter API
  phrasing_intents:
  - id: chapterStart
    intent: Track the start of a media chapter
    question: How do I report that a new chapter began in a video session?
  - id: chapterComplete
    intent: Track the completion of a media chapter
    question: How do I record that a viewer finished a chapter?
  - id: chapterSkip
    intent: Track a skipped media chapter
    question: What should I send when a viewer skips a chapter?
  phrasing_ops: 3
  slug: adobe-launch-chapter-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Real-time events originating client-side, such as browsers or mobile devices
  name: Adobe Launch Client-to-server collection API
  phrasing_intents:
  - id: postV1Interact
    intent: Send one browser event and get a live response
    question: How do I send a single event from a web or mobile client to the Edge Network and get personalization back?
  - id: postV1Collect
    intent: Send a batch of client events without a response
    question: Can I push events from several different end users in one unauthenticated client request?
  - id: postV1IdentityAcquire
    intent: Acquire identities for given namespaces
    question: How do I fetch the visitor's identities for specific identity namespaces from the Edge Network?
  phrasing_ops: 3
  slug: adobe-launch-client-to-server-collection-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: The Download API from Adobe Launch — 1 operation(s) for download.
  name: Adobe Launch Download API
  phrasing_intents:
  - id: downloaded
    intent: Send offline media consumption events
    question: How do I track video watched while the user was offline?
  phrasing_ops: 1
  slug: adobe-launch-download-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: The Error API from Adobe Launch — 1 operation(s) for error.
  name: Adobe Launch Error API
  phrasing_intents:
  - id: error
    intent: Signal a playback error
    question: How do I report a player error during a media session?
  phrasing_ops: 1
  slug: adobe-launch-error-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: An extension package usage authorization is an authorization granted by the package owner to other companies for the private use of the extension package versions.
  name: Adobe Launch Extension package usage authorization API
  phrasing_intents:
  - id: retrieveExtensionPackageUsageAuthorizationForPackage
    intent: List usage authorizations for a package
    question: Which organizations are authorized to use my private extension package?
  - id: createExtensionPackageUsageAuthorization
    intent: Authorize an org to use an extension package
    question: How do I share my private extension package with another organization?
  - id: retrieveExtensionPackageUsageAuthorization
    intent: List all extension package usage authorizations
    question: What extension package usage authorizations exist across my organization?
  - id: deletePackageUsageAuthorization
    intent: Revoke an extension package usage authorization
    question: How do I stop another org from using my extension package?
  - id: updateExtensionPackageUsageAuthorization
    intent: Update an extension package usage authorization
    question: How do I modify a usage authorization on an extension package?
  - id: retrieveDataExtensionPackageUsageAuthorization
    intent: Get the package behind a usage authorization
    question: Which extension package does a usage authorization cover?
  phrasing_ops: 6
  slug: adobe-launch-extension-package-usage-authorization-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Notes are textual annotations that you can add to certain tag resources, such as data elements, extensions, libraries, properties, rules, and rule components.
  name: Adobe Launch Notes API
  phrasing_intents:
  - id: retrieveNote
    intent: Look up a note by ID
    question: How do I read a single tags note when I have its ID?
  - id: listPropertyNotes
    intent: List notes on a property
    question: What notes have been left on my tags property?
  - id: createPropertyNote
    intent: Add a note to a property
    question: How do I leave a note on a whole tags property?
  - id: listDataElementNotes
    intent: List notes on a data element
    question: What notes are attached to this data element?
  - id: createNote
    intent: Add a note to a data element
    question: How do I document why a data element is set up the way it is?
  - id: listSecretNotes
    intent: List notes on a secret
    question: What notes are on this event forwarding secret?
  - id: createSecretNote
    intent: Add a note to a secret
    question: How do I record who owns a secret or when it rotates?
  - id: listExtensionNotes
    intent: List notes on an extension
    question: What notes have been added to this extension?
  phrasing_ops: 15
  slug: adobe-launch-notes-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: The Pause API from Adobe Launch — 1 operation(s) for pause.
  name: Adobe Launch Pause API
  phrasing_intents:
  - id: pauseStart
    intent: Track a media pause
    question: How do I report that a viewer paused a video?
  phrasing_ops: 1
  slug: adobe-launch-pause-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: The Ping API from Adobe Launch — 1 operation(s) for ping.
  name: Adobe Launch Ping API
  phrasing_intents:
  - id: ping
    intent: Send a playback heartbeat ping
    question: How often do I need to send pings during main content playback?
  phrasing_ops: 1
  slug: adobe-launch-ping-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: The Play API from Adobe Launch — 1 operation(s) for play.
  name: Adobe Launch Play API
  phrasing_intents:
  - id: play
    intent: Track media playback starting
    question: How do I report that a video started or resumed playing?
  phrasing_ops: 1
  slug: adobe-launch-play-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Collect specific data for Platform profile(s)
  name: Adobe Launch Profile updates API
  phrasing_intents:
  - id: postV1PrivacySetConsent
    intent: Set a user's marketing consent preferences
    question: How do I record a visitor's opt-in or opt-out for marketing through the Edge Network?
  phrasing_ops: 1
  slug: adobe-launch-profile-updates-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: A profile represents a tags user. Platform does not maintain its own database of users and permissions, and instead relies on Adobe IDs managed by Adobe’s company-wide Identity Management System (IMS)
  name: Adobe Launch Profiles API
  phrasing_intents:
  - id: retrieveUserDetails
    intent: Get the logged-in user's profile
    question: How can I see which user my Reactor access token belongs to?
  phrasing_ops: 1
  slug: adobe-launch-profiles-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: Real-time events forwarded by a private server
  name: Adobe Launch Server-to-server collection API
  phrasing_intents:
  - id: postV2Interact
    intent: Send one server event and get a live response
    question: How do I send a single authenticated event from my server and get personalization decisions back?
  - id: postV2Collect
    intent: Send a batch of server events without a response
    question: How do I push many events from different end users in one authenticated server request?
  phrasing_ops: 2
  slug: adobe-launch-server-to-server-collection-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: The Session API from Adobe Launch — 3 operation(s) for session.
  name: Adobe Launch Session API
  phrasing_intents:
  - id: sessionStart
    intent: Start a Media Edge session
    question: How do I open a new Media Edge session and get its session ID?
  - id: sessionComplete
    intent: Signal the end of main content
    question: How do I tell Media Edge the main content reached its end?
  - id: sessionEnd
    intent: Close an abandoned media session immediately
    question: How do I close a session right away when the viewer abandons the content?
  phrasing_ops: 3
  slug: adobe-launch-session-api
- baseURL: https://reactor.adobe.io
  baseurl_source: declared
  description: The States API from Adobe Launch — 1 operation(s) for states.
  name: Adobe Launch States API
  phrasing_intents:
  - id: statesUpdate
    intent: Report player state changes
    question: How do I tell Media Edge that a player state changed during playback?
  phrasing_ops: 1
  slug: adobe-launch-states-api
arazzos:
- description: Verify a rule exists, add a new rule component to it, and list the rule's components to confirm.
  name: Adobe Launch Add a Component to an Existing Rule
  slug: adobe-launch-add-rule-component-workflow
- description: Read a property and inventory its rules, data elements, and installed extensions.
  name: Adobe Launch Audit a Property's Contents
  slug: adobe-launch-audit-property-contents-workflow
- description: Create a server-side event forwarding property, then add a rule and a data element to it.
  name: Adobe Launch Bootstrap an Event Forwarding Property
  slug: adobe-launch-bootstrap-event-forwarding-workflow
- description: Stand up a new Tags property, add a rule to it, and attach a first rule component.
  name: Adobe Launch Bootstrap a Property with a Rule
  slug: adobe-launch-bootstrap-property-rule-workflow
- description: Create a data element under a property, then read it back to confirm it persisted.
  name: Adobe Launch Create and Verify a Data Element
  slug: adobe-launch-create-and-verify-data-element-workflow
- description: Create a secret scoped to an environment on an event forwarding property, then read it back.
  name: Adobe Launch Create an Event Forwarding Secret
  slug: adobe-launch-create-event-forwarding-secret-workflow
- description: Find an extension package by name, install it into a property, and read the installed extension back.
  name: Adobe Launch Install an Extension from a Package
  slug: adobe-launch-install-extension-workflow
- description: Create a library, add a rule to it, kick off a build, and poll the build until it finishes.
  name: Adobe Launch Build a Library and Poll for Completion
  slug: adobe-launch-library-build-and-poll-workflow
- description: Create a delivery host on a property, then create an environment that uses it.
  name: Adobe Launch Provision a Host and Environment
  slug: adobe-launch-provision-environment-workflow
- description: Transition an existing library through submit and approve, then compile a build and poll it.
  name: Adobe Launch Submit, Approve, and Build a Library
  slug: adobe-launch-publish-library-workflow
- description: Register a callback on a property to receive build notifications, then read it back.
  name: Adobe Launch Register a Build Callback Webhook
  slug: adobe-launch-register-callback-workflow
- description: Find a library's most recent build, republish it, and poll until the republish completes.
  name: Adobe Launch Republish a Library's Latest Build
  slug: adobe-launch-republish-latest-build-workflow
- description: Search across Tags resources by name for a property, then retrieve the matched property in full.
  name: Adobe Launch Search for a Property and Fetch It
  slug: adobe-launch-search-and-fetch-property-workflow
artifact_total: 529
asyncapis:
- description: ''
  name: Adobe Launch Webhooks
  slug: adobe-launch-webhooks
collections:
- collection_type: postman
  name: Adobe Experience Platform Data Collection API
  slug: postman-data-collection-api
- collection_type: postman
  name: Adobe Experience Platform Event Forwarding API
  slug: postman-event-forwarding-api
- collection_type: postman
  name: Adobe Launch Extension API
  slug: postman-extension-api
- collection_type: postman
  name: Adobe Launch Reactor API
  slug: postman-reactor-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds API
  slug: open-adobe-launch-builds-api
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Callbacks API
  slug: open-adobe-launch-callbacks-api
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Companies API
  slug: open-adobe-launch-companies-api
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Data Elements API
  slug: open-adobe-launch-data-elements-api
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Edge Network API API
  slug: open-adobe-launch-edge-network-api-api
- collection_type: open
  name: Adobe Experience Platform Edge Network API
  slug: open-adobe-launch-edge-network-published
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Environments API
  slug: open-adobe-launch-environments-api
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Extension Packages API
  slug: open-adobe-launch-extension-packages-api
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Extensions API
  slug: open-adobe-launch-extensions-api
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Hosts API
  slug: open-adobe-launch-hosts-api
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Libraries API
  slug: open-adobe-launch-libraries-api
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Media Edge API API
  slug: open-adobe-launch-media-edge-api-api
- collection_type: open
  name: Media Edge API
  slug: open-adobe-launch-media-edge-published
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Properties API
  slug: open-adobe-launch-properties-api
- collection_type: open
  name: Reactor API
  slug: open-adobe-launch-reactor-api-published
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Rule Components API
  slug: open-adobe-launch-rule-components-api
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Rules API
  slug: open-adobe-launch-rules-api
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Search API
  slug: open-adobe-launch-search-api
- collection_type: open
  name: Adobe Experience Platform Data Collection Builds Secrets API
  slug: open-adobe-launch-secrets-api
- collection_type: open
  name: Adobe Experience Platform Data Collection API
  slug: open-data-collection-api
- collection_type: open
  name: Adobe Experience Platform Event Forwarding API
  slug: open-event-forwarding-api
- collection_type: open
  name: Adobe Launch Extension API
  slug: open-extension-api
- collection_type: open
  name: Adobe Launch Reactor API
  slug: open-reactor-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.adobe.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/capabilities/adobe-launch-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/adobe-launch-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/agentic-access/adobe-launch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-launch-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/security/adobe-launch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-launch-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/security/adobe-launch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adobe-launch-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/authentication/adobe-launch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adobe-launch-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adobe-launch/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-add-rule-component-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-add-rule-component-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-audit-property-contents-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-audit-property-contents-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-bootstrap-event-forwarding-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-bootstrap-event-forwarding-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-bootstrap-property-rule-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-bootstrap-property-rule-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-create-and-verify-data-element-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-create-and-verify-data-element-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-create-event-forwarding-secret-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-create-event-forwarding-secret-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-install-extension-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-install-extension-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-library-build-and-poll-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-library-build-and-poll-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-provision-environment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-provision-environment-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-publish-library-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-publish-library-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-register-callback-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-register-callback-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-republish-latest-build-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-republish-latest-build-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/arazzo/adobe-launch-search-and-fetch-property-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-launch-search-and-fetch-property-workflow.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy.html
- group: start
  title: ''
  type: Console
  url: https://developer.adobe.com/developer-console/
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/adobetech
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/adobetech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adobe
- group: start
  title: ''
  type: Signup
  url: https://developer.adobe.com/developer-console/
- group: auth
  title: ''
  type: Authentication
  url: https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-authentication
- group: operate
  title: ''
  type: ChangeLog
  url: https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/latest
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@adobe/reactor-sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@adobe/reactor-scaffold
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@adobe/reactor-sandbox
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/packages/adobe-launch-packages.yml
  title: ''
  type: Packages
  url: packages/adobe-launch-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/packages/adobe-launch-packages.yml
  title: ''
  type: SDKs
  url: packages/adobe-launch-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/well-known/adobe-launch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adobe-launch-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/well-known/adobe-launch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adobe-launch-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/security/adobe-launch-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/adobe-launch-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/security/adobe-launch-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/adobe-launch-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/security/adobe-launch-trust-center.yml
  title: ''
  type: Compliance
  url: security/adobe-launch-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/conformance/adobe-launch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adobe-launch-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/llms/adobe-launch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adobe-launch-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/overlays/adobe-launch-reactor-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adobe-launch-reactor-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/overlays/adobe-launch-edge-network-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adobe-launch-edge-network-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/overlays/adobe-launch-media-edge-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adobe-launch-media-edge-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/errors/adobe-launch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adobe-launch-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/lifecycle/adobe-launch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adobe-launch-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/scopes/adobe-launch-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/adobe-launch-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/conventions/adobe-launch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adobe-launch-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/asyncapi/adobe-launch-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/adobe-launch-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/data-model/adobe-launch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adobe-launch-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/changelog/adobe-launch-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/adobe-launch-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/cli/adobe-launch-cli.yml
  title: ''
  type: CLI
  url: cli/adobe-launch-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/components/adobe-launch-components.yml
  title: ''
  type: Components
  url: components/adobe-launch-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/sandbox/adobe-launch-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/adobe-launch-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/plans/adobe-launch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adobe-launch-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/rate-limits/adobe-launch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adobe-launch-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/finops/adobe-launch-finops.yml
  title: ''
  type: FinOps
  url: finops/adobe-launch-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://experienceleague.adobe.com/en/docs/experience-platform/tags/home
- group: docs
  title: ''
  type: APIReference
  url: https://developer.adobe.com/experience-platform-apis/references/reactor
- group: start
  title: ''
  type: GettingStarted
  url: https://experienceleague.adobe.com/en/docs/experience-platform/tags/api/getting-started
- group: operate
  title: ''
  type: Support
  url: https://experienceleague.adobe.com/?support-solution=Experience+Platform
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.adobe.com/
created: '2024-01-15'
description: Adobe Launch, now known as Adobe Experience Platform Tags, is a next-generation tag management system that unifies the client-side marketing ecosystem by empowering developers to build integrations on a robust, extensible platform that partners, clients, and the broader industry can build on and contribute to.
examples:
- key_count: 1
  name: Data Collection Collect Request Example
  slug: data-collection-collect-request-example
- key_count: 1
  name: Data Collection Collect Response Example
  slug: data-collection-collect-response-example
- key_count: 5
  name: Data Collection Error Response Example
  slug: data-collection-error-response-example
- key_count: 1
  name: Data Collection Interact Request Example
  slug: data-collection-interact-request-example
- key_count: 2
  name: Data Collection Interact Response Example
  slug: data-collection-interact-response-example
- key_count: 1
  name: Data Collection Media Error Request Example
  slug: data-collection-media-error-request-example
- key_count: 1
  name: Data Collection Media Event Request Example
  slug: data-collection-media-event-request-example
- key_count: 1
  name: Data Collection Media Session Start Request Example
  slug: data-collection-media-session-start-request-example
- key_count: 2
  name: Data Collection Media Session Start Response Example
  slug: data-collection-media-session-start-response-example
- key_count: 5
  name: Data Collection Xdm Event Example
  slug: data-collection-xdm-event-example
- key_count: 1
  name: Event Forwarding Data Element Create Request Example
  slug: event-forwarding-data-element-create-request-example
- key_count: 1
  name: Event Forwarding Data Element List Response Example
  slug: event-forwarding-data-element-list-response-example
- key_count: 4
  name: Event Forwarding Data Element Resource Example
  slug: event-forwarding-data-element-resource-example
- key_count: 0
  name: Event Forwarding Data Element Single Response Example
  slug: event-forwarding-data-element-single-response-example
- key_count: 1
  name: Event Forwarding Environment List Response Example
  slug: event-forwarding-environment-list-response-example
- key_count: 1
  name: Event Forwarding Environment Single Response Example
  slug: event-forwarding-environment-single-response-example
- key_count: 1
  name: Event Forwarding Error Response Example
  slug: event-forwarding-error-response-example
- key_count: 1
  name: Event Forwarding Extension List Response Example
  slug: event-forwarding-extension-list-response-example
- key_count: 1
  name: Event Forwarding Library Create Request Example
  slug: event-forwarding-library-create-request-example
- key_count: 1
  name: Event Forwarding Library List Response Example
  slug: event-forwarding-library-list-response-example
- key_count: 1
  name: Event Forwarding Library Single Response Example
  slug: event-forwarding-library-single-response-example
- key_count: 1
  name: Event Forwarding Pagination Meta Example
  slug: event-forwarding-pagination-meta-example
- key_count: 5
  name: Event Forwarding Property Attributes Example
  slug: event-forwarding-property-attributes-example
- key_count: 1
  name: Event Forwarding Property Create Request Example
  slug: event-forwarding-property-create-request-example
- key_count: 1
  name: Event Forwarding Property List Response Example
  slug: event-forwarding-property-list-response-example
- key_count: 3
  name: Event Forwarding Property Resource Example
  slug: event-forwarding-property-resource-example
- key_count: 0
  name: Event Forwarding Property Single Response Example
  slug: event-forwarding-property-single-response-example
- key_count: 1
  name: Event Forwarding Property Update Request Example
  slug: event-forwarding-property-update-request-example
- key_count: 2
  name: Event Forwarding Relationship Example
  slug: event-forwarding-relationship-example
- key_count: 1
  name: Event Forwarding Rule Create Request Example
  slug: event-forwarding-rule-create-request-example
- key_count: 1
  name: Event Forwarding Rule List Response Example
  slug: event-forwarding-rule-list-response-example
- key_count: 4
  name: Event Forwarding Rule Resource Example
  slug: event-forwarding-rule-resource-example
- key_count: 0
  name: Event Forwarding Rule Single Response Example
  slug: event-forwarding-rule-single-response-example
- key_count: 1
  name: Event Forwarding Rule Update Request Example
  slug: event-forwarding-rule-update-request-example
- key_count: 6
  name: Event Forwarding Secret Attributes Example
  slug: event-forwarding-secret-attributes-example
- key_count: 1
  name: Event Forwarding Secret Create Request Example
  slug: event-forwarding-secret-create-request-example
- key_count: 1
  name: Event Forwarding Secret List Response Example
  slug: event-forwarding-secret-list-response-example
- key_count: 3
  name: Event Forwarding Secret Resource Example
  slug: event-forwarding-secret-resource-example
- key_count: 0
  name: Event Forwarding Secret Single Response Example
  slug: event-forwarding-secret-single-response-example
- key_count: 1
  name: Event Forwarding Secret Update Request Example
  slug: event-forwarding-secret-update-request-example
- key_count: 1
  name: Extension Error Response Example
  slug: extension-error-response-example
- key_count: 12
  name: Extension Extension Attributes Example
  slug: extension-extension-attributes-example
- key_count: 1
  name: Extension Extension Install Request Example
  slug: extension-extension-install-request-example
- key_count: 1
  name: Extension Extension List Response Example
  slug: extension-extension-list-response-example
- key_count: 13
  name: Extension Extension Package Attributes Example
  slug: extension-extension-package-attributes-example
- key_count: 1
  name: Extension Extension Package List Response Example
  slug: extension-extension-package-list-response-example
- key_count: 4
  name: Extension Extension Package Resource Example
  slug: extension-extension-package-resource-example
- key_count: 0
  name: Extension Extension Package Single Response Example
  slug: extension-extension-package-single-response-example
- key_count: 1
  name: Extension Extension Package Update Request Example
  slug: extension-extension-package-update-request-example
- key_count: 4
  name: Extension Extension Resource Example
  slug: extension-extension-resource-example
- key_count: 1
  name: Extension Extension Revise Request Example
  slug: extension-extension-revise-request-example
- key_count: 0
  name: Extension Extension Single Response Example
  slug: extension-extension-single-response-example
- key_count: 1
  name: Extension Library List Response Example
  slug: extension-library-list-response-example
- key_count: 1
  name: Extension Pagination Meta Example
  slug: extension-pagination-meta-example
- key_count: 1
  name: Extension Property Single Response Example
  slug: extension-property-single-response-example
- key_count: 2
  name: Extension Relationship Example
  slug: extension-relationship-example
- key_count: 4
  name: Reactor Build Attributes Example
  slug: reactor-build-attributes-example
- key_count: 1
  name: Reactor Build List Response Example
  slug: reactor-build-list-response-example
- key_count: 4
  name: Reactor Build Resource Example
  slug: reactor-build-resource-example
- key_count: 0
  name: Reactor Build Single Response Example
  slug: reactor-build-single-response-example
- key_count: 4
  name: Reactor Callback Attributes Example
  slug: reactor-callback-attributes-example
- key_count: 1
  name: Reactor Callback Create Request Example
  slug: reactor-callback-create-request-example
- key_count: 1
  name: Reactor Callback List Response Example
  slug: reactor-callback-list-response-example
- key_count: 4
  name: Reactor Callback Resource Example
  slug: reactor-callback-resource-example
- key_count: 0
  name: Reactor Callback Single Response Example
  slug: reactor-callback-single-response-example
- key_count: 1
  name: Reactor Callback Update Request Example
  slug: reactor-callback-update-request-example
- key_count: 7
  name: Reactor Company Attributes Example
  slug: reactor-company-attributes-example
- key_count: 1
  name: Reactor Company List Response Example
  slug: reactor-company-list-response-example
- key_count: 4
  name: Reactor Company Resource Example
  slug: reactor-company-resource-example
- key_count: 0
  name: Reactor Company Single Response Example
  slug: reactor-company-single-response-example
- key_count: 13
  name: Reactor Data Element Attributes Example
  slug: reactor-data-element-attributes-example
- key_count: 1
  name: Reactor Data Element Create Request Example
  slug: reactor-data-element-create-request-example
- key_count: 1
  name: Reactor Data Element List Response Example
  slug: reactor-data-element-list-response-example
- key_count: 4
  name: Reactor Data Element Resource Example
  slug: reactor-data-element-resource-example
- key_count: 0
  name: Reactor Data Element Single Response Example
  slug: reactor-data-element-single-response-example
- key_count: 1
  name: Reactor Data Element Update Request Example
  slug: reactor-data-element-update-request-example
- key_count: 9
  name: Reactor Environment Attributes Example
  slug: reactor-environment-attributes-example
- key_count: 1
  name: Reactor Environment Create Request Example
  slug: reactor-environment-create-request-example
- key_count: 1
  name: Reactor Environment List Response Example
  slug: reactor-environment-list-response-example
- key_count: 4
  name: Reactor Environment Resource Example
  slug: reactor-environment-resource-example
- key_count: 0
  name: Reactor Environment Single Response Example
  slug: reactor-environment-single-response-example
- key_count: 1
  name: Reactor Environment Update Request Example
  slug: reactor-environment-update-request-example
- key_count: 1
  name: Reactor Error Response Example
  slug: reactor-error-response-example
- key_count: 12
  name: Reactor Extension Attributes Example
  slug: reactor-extension-attributes-example
- key_count: 1
  name: Reactor Extension Create Request Example
  slug: reactor-extension-create-request-example
- key_count: 1
  name: Reactor Extension List Response Example
  slug: reactor-extension-list-response-example
- key_count: 11
  name: Reactor Extension Package Attributes Example
  slug: reactor-extension-package-attributes-example
- key_count: 1
  name: Reactor Extension Package List Response Example
  slug: reactor-extension-package-list-response-example
- key_count: 3
  name: Reactor Extension Package Resource Example
  slug: reactor-extension-package-resource-example
- key_count: 0
  name: Reactor Extension Package Single Response Example
  slug: reactor-extension-package-single-response-example
- key_count: 4
  name: Reactor Extension Resource Example
  slug: reactor-extension-resource-example
- key_count: 0
  name: Reactor Extension Single Response Example
  slug: reactor-extension-single-response-example
- key_count: 1
  name: Reactor Extension Update Request Example
  slug: reactor-extension-update-request-example
- key_count: 11
  name: Reactor Host Attributes Example
  slug: reactor-host-attributes-example
- key_count: 1
  name: Reactor Host Create Request Example
  slug: reactor-host-create-request-example
- key_count: 1
  name: Reactor Host List Response Example
  slug: reactor-host-list-response-example
- key_count: 4
  name: Reactor Host Resource Example
  slug: reactor-host-resource-example
- key_count: 0
  name: Reactor Host Single Response Example
  slug: reactor-host-single-response-example
- key_count: 1
  name: Reactor Host Update Request Example
  slug: reactor-host-update-request-example
- key_count: 5
  name: Reactor Library Attributes Example
  slug: reactor-library-attributes-example
- key_count: 1
  name: Reactor Library Create Request Example
  slug: reactor-library-create-request-example
- key_count: 1
  name: Reactor Library List Response Example
  slug: reactor-library-list-response-example
- key_count: 4
  name: Reactor Library Resource Example
  slug: reactor-library-resource-example
- key_count: 0
  name: Reactor Library Single Response Example
  slug: reactor-library-single-response-example
- key_count: 1
  name: Reactor Library Update Request Example
  slug: reactor-library-update-request-example
- key_count: 1
  name: Reactor Pagination Meta Example
  slug: reactor-pagination-meta-example
- key_count: 12
  name: Reactor Property Attributes Example
  slug: reactor-property-attributes-example
- key_count: 1
  name: Reactor Property Create Request Example
  slug: reactor-property-create-request-example
- key_count: 1
  name: Reactor Property List Response Example
  slug: reactor-property-list-response-example
- key_count: 4
  name: Reactor Property Resource Example
  slug: reactor-property-resource-example
- key_count: 0
  name: Reactor Property Single Response Example
  slug: reactor-property-single-response-example
- key_count: 1
  name: Reactor Property Update Request Example
  slug: reactor-property-update-request-example
- key_count: 2
  name: Reactor Relationship Example
  slug: reactor-relationship-example
- key_count: 1
  name: Reactor Relationship Request Example
  slug: reactor-relationship-request-example
- key_count: 1
  name: Reactor Relationship Single Request Example
  slug: reactor-relationship-single-request-example
- key_count: 7
  name: Reactor Rule Attributes Example
  slug: reactor-rule-attributes-example
- key_count: 13
  name: Reactor Rule Component Attributes Example
  slug: reactor-rule-component-attributes-example
- key_count: 1
  name: Reactor Rule Component Create Request Example
  slug: reactor-rule-component-create-request-example
- key_count: 1
  name: Reactor Rule Component List Response Example
  slug: reactor-rule-component-list-response-example
- key_count: 4
  name: Reactor Rule Component Resource Example
  slug: reactor-rule-component-resource-example
- key_count: 0
  name: Reactor Rule Component Single Response Example
  slug: reactor-rule-component-single-response-example
- key_count: 1
  name: Reactor Rule Component Update Request Example
  slug: reactor-rule-component-update-request-example
- key_count: 1
  name: Reactor Rule Create Request Example
  slug: reactor-rule-create-request-example
- key_count: 1
  name: Reactor Rule List Response Example
  slug: reactor-rule-list-response-example
- key_count: 4
  name: Reactor Rule Resource Example
  slug: reactor-rule-resource-example
- key_count: 0
  name: Reactor Rule Single Response Example
  slug: reactor-rule-single-response-example
- key_count: 1
  name: Reactor Rule Update Request Example
  slug: reactor-rule-update-request-example
- key_count: 1
  name: Reactor Search Request Example
  slug: reactor-search-request-example
- key_count: 2
  name: Reactor Search Response Example
  slug: reactor-search-response-example
- key_count: 6
  name: Reactor Secret Attributes Example
  slug: reactor-secret-attributes-example
- key_count: 1
  name: Reactor Secret Create Request Example
  slug: reactor-secret-create-request-example
- key_count: 1
  name: Reactor Secret List Response Example
  slug: reactor-secret-list-response-example
- key_count: 4
  name: Reactor Secret Resource Example
  slug: reactor-secret-resource-example
- key_count: 0
  name: Reactor Secret Single Response Example
  slug: reactor-secret-single-response-example
- key_count: 1
  name: Reactor Secret Update Request Example
  slug: reactor-secret-update-request-example
features:
- Next-generation tag management for web and mobile
- Extensible platform with public extension marketplace
- Server-side event forwarding via Edge Network
- Rule-based data collection and routing
- Library versioning with staging and production environments
- JSON API specification-based programmatic management
- Real-time data collection to Edge Network
- Media tracking and analytics integration
finops:
- name: Adobe Launch Finops
  service_category: Tag Management
  slug: adobe-launch-finops
image: /assets/icons/adobe-launch.png
integrations:
- Adobe Analytics
- Adobe Target
- Adobe Audience Manager
- Adobe Experience Platform
- Google Analytics
- Facebook Pixel
- LinkedIn Insight Tag
- Custom JavaScript libraries
- Third-party marketing platforms
json_schemas:
- name: Adobe Experience Platform Tags Build
  property_count: 5
  slug: build
- name: CollectRequest
  property_count: 1
  slug: data-collection-collect-request
- name: CollectResponse
  property_count: 1
  slug: data-collection-collect-response
- name: ErrorResponse
  property_count: 5
  slug: data-collection-error-response
- name: InteractRequest
  property_count: 1
  slug: data-collection-interact-request
- name: InteractResponse
  property_count: 2
  slug: data-collection-interact-response
- name: MediaErrorRequest
  property_count: 1
  slug: data-collection-media-error-request
- name: MediaEventRequest
  property_count: 1
  slug: data-collection-media-event-request
- name: MediaSessionStartRequest
  property_count: 1
  slug: data-collection-media-session-start-request
- name: MediaSessionStartResponse
  property_count: 2
  slug: data-collection-media-session-start-response
- name: XDMEvent
  property_count: 5
  slug: data-collection-xdm-event
- name: Adobe Experience Platform Tags Data Element
  property_count: 5
  slug: data-element
- name: DataElementCreateRequest
  property_count: 1
  slug: event-forwarding-data-element-create-request
- name: DataElementListResponse
  property_count: 1
  slug: event-forwarding-data-element-list-response
- name: DataElementResource
  property_count: 4
  slug: event-forwarding-data-element-resource
- name: DataElementSingleResponse
  property_count: 0
  slug: event-forwarding-data-element-single-response
- name: EnvironmentListResponse
  property_count: 1
  slug: event-forwarding-environment-list-response
- name: EnvironmentSingleResponse
  property_count: 1
  slug: event-forwarding-environment-single-response
- name: ErrorResponse
  property_count: 1
  slug: event-forwarding-error-response
- name: ExtensionListResponse
  property_count: 1
  slug: event-forwarding-extension-list-response
- name: LibraryCreateRequest
  property_count: 1
  slug: event-forwarding-library-create-request
- name: LibraryListResponse
  property_count: 1
  slug: event-forwarding-library-list-response
- name: LibrarySingleResponse
  property_count: 1
  slug: event-forwarding-library-single-response
- name: PaginationMeta
  property_count: 1
  slug: event-forwarding-pagination-meta
- name: PropertyAttributes
  property_count: 5
  slug: event-forwarding-property-attributes
- name: PropertyCreateRequest
  property_count: 1
  slug: event-forwarding-property-create-request
- name: PropertyListResponse
  property_count: 1
  slug: event-forwarding-property-list-response
- name: PropertyResource
  property_count: 3
  slug: event-forwarding-property-resource
- name: PropertySingleResponse
  property_count: 0
  slug: event-forwarding-property-single-response
- name: PropertyUpdateRequest
  property_count: 1
  slug: event-forwarding-property-update-request
- name: Relationship
  property_count: 2
  slug: event-forwarding-relationship
- name: RuleCreateRequest
  property_count: 1
  slug: event-forwarding-rule-create-request
- name: RuleListResponse
  property_count: 1
  slug: event-forwarding-rule-list-response
- name: RuleResource
  property_count: 4
  slug: event-forwarding-rule-resource
- name: RuleSingleResponse
  property_count: 0
  slug: event-forwarding-rule-single-response
- name: RuleUpdateRequest
  property_count: 1
  slug: event-forwarding-rule-update-request
- name: SecretAttributes
  property_count: 6
  slug: event-forwarding-secret-attributes
- name: SecretCreateRequest
  property_count: 1
  slug: event-forwarding-secret-create-request
- name: SecretListResponse
  property_count: 1
  slug: event-forwarding-secret-list-response
- name: SecretResource
  property_count: 3
  slug: event-forwarding-secret-resource
- name: SecretSingleResponse
  property_count: 0
  slug: event-forwarding-secret-single-response
- name: SecretUpdateRequest
  property_count: 1
  slug: event-forwarding-secret-update-request
- name: ErrorResponse
  property_count: 1
  slug: extension-error-response
- name: ExtensionAttributes
  property_count: 12
  slug: extension-extension-attributes
- name: ExtensionInstallRequest
  property_count: 1
  slug: extension-extension-install-request
- name: ExtensionListResponse
  property_count: 1
  slug: extension-extension-list-response
- name: ExtensionPackageAttributes
  property_count: 13
  slug: extension-extension-package-attributes
- name: ExtensionPackageListResponse
  property_count: 1
  slug: extension-extension-package-list-response
- name: ExtensionPackageResource
  property_count: 4
  slug: extension-extension-package-resource
- name: ExtensionPackageSingleResponse
  property_count: 0
  slug: extension-extension-package-single-response
- name: ExtensionPackageUpdateRequest
  property_count: 1
  slug: extension-extension-package-update-request
- name: ExtensionResource
  property_count: 4
  slug: extension-extension-resource
- name: ExtensionReviseRequest
  property_count: 1
  slug: extension-extension-revise-request
- name: ExtensionSingleResponse
  property_count: 0
  slug: extension-extension-single-response
- name: LibraryListResponse
  property_count: 1
  slug: extension-library-list-response
- name: PaginationMeta
  property_count: 1
  slug: extension-pagination-meta
- name: PropertySingleResponse
  property_count: 1
  slug: extension-property-single-response
- name: Relationship
  property_count: 2
  slug: extension-relationship
- name: Adobe Experience Platform Tags Extension
  property_count: 5
  slug: extension
- name: Adobe Experience Platform Tags Library
  property_count: 6
  slug: library
- name: Adobe Experience Platform Tags Property
  property_count: 5
  slug: property
- name: BuildAttributes
  property_count: 4
  slug: reactor-build-attributes
- name: BuildListResponse
  property_count: 1
  slug: reactor-build-list-response
- name: BuildResource
  property_count: 4
  slug: reactor-build-resource
- name: BuildSingleResponse
  property_count: 0
  slug: reactor-build-single-response
- name: CallbackAttributes
  property_count: 4
  slug: reactor-callback-attributes
- name: CallbackCreateRequest
  property_count: 1
  slug: reactor-callback-create-request
- name: CallbackListResponse
  property_count: 1
  slug: reactor-callback-list-response
- name: CallbackResource
  property_count: 4
  slug: reactor-callback-resource
- name: CallbackSingleResponse
  property_count: 0
  slug: reactor-callback-single-response
- name: CallbackUpdateRequest
  property_count: 1
  slug: reactor-callback-update-request
- name: CompanyAttributes
  property_count: 7
  slug: reactor-company-attributes
- name: CompanyListResponse
  property_count: 1
  slug: reactor-company-list-response
- name: CompanyResource
  property_count: 4
  slug: reactor-company-resource
- name: CompanySingleResponse
  property_count: 0
  slug: reactor-company-single-response
- name: DataElementAttributes
  property_count: 13
  slug: reactor-data-element-attributes
- name: DataElementCreateRequest
  property_count: 1
  slug: reactor-data-element-create-request
- name: DataElementListResponse
  property_count: 1
  slug: reactor-data-element-list-response
- name: DataElementResource
  property_count: 4
  slug: reactor-data-element-resource
- name: DataElementSingleResponse
  property_count: 0
  slug: reactor-data-element-single-response
- name: DataElementUpdateRequest
  property_count: 1
  slug: reactor-data-element-update-request
- name: EnvironmentAttributes
  property_count: 9
  slug: reactor-environment-attributes
- name: EnvironmentCreateRequest
  property_count: 1
  slug: reactor-environment-create-request
- name: EnvironmentListResponse
  property_count: 1
  slug: reactor-environment-list-response
- name: EnvironmentResource
  property_count: 4
  slug: reactor-environment-resource
- name: EnvironmentSingleResponse
  property_count: 0
  slug: reactor-environment-single-response
- name: EnvironmentUpdateRequest
  property_count: 1
  slug: reactor-environment-update-request
- name: ErrorResponse
  property_count: 1
  slug: reactor-error-response
- name: ExtensionAttributes
  property_count: 12
  slug: reactor-extension-attributes
- name: ExtensionCreateRequest
  property_count: 1
  slug: reactor-extension-create-request
- name: ExtensionListResponse
  property_count: 1
  slug: reactor-extension-list-response
- name: ExtensionPackageAttributes
  property_count: 11
  slug: reactor-extension-package-attributes
- name: ExtensionPackageListResponse
  property_count: 1
  slug: reactor-extension-package-list-response
- name: ExtensionPackageResource
  property_count: 3
  slug: reactor-extension-package-resource
- name: ExtensionPackageSingleResponse
  property_count: 0
  slug: reactor-extension-package-single-response
- name: ExtensionResource
  property_count: 4
  slug: reactor-extension-resource
- name: ExtensionSingleResponse
  property_count: 0
  slug: reactor-extension-single-response
- name: ExtensionUpdateRequest
  property_count: 1
  slug: reactor-extension-update-request
- name: HostAttributes
  property_count: 11
  slug: reactor-host-attributes
- name: HostCreateRequest
  property_count: 1
  slug: reactor-host-create-request
- name: HostListResponse
  property_count: 1
  slug: reactor-host-list-response
- name: HostResource
  property_count: 4
  slug: reactor-host-resource
- name: HostSingleResponse
  property_count: 0
  slug: reactor-host-single-response
- name: HostUpdateRequest
  property_count: 1
  slug: reactor-host-update-request
- name: LibraryAttributes
  property_count: 5
  slug: reactor-library-attributes
- name: LibraryCreateRequest
  property_count: 1
  slug: reactor-library-create-request
- name: LibraryListResponse
  property_count: 1
  slug: reactor-library-list-response
- name: LibraryResource
  property_count: 4
  slug: reactor-library-resource
- name: LibrarySingleResponse
  property_count: 0
  slug: reactor-library-single-response
- name: LibraryUpdateRequest
  property_count: 1
  slug: reactor-library-update-request
- name: PaginationMeta
  property_count: 1
  slug: reactor-pagination-meta
- name: PropertyAttributes
  property_count: 12
  slug: reactor-property-attributes
- name: PropertyCreateRequest
  property_count: 1
  slug: reactor-property-create-request
- name: PropertyListResponse
  property_count: 1
  slug: reactor-property-list-response
- name: PropertyResource
  property_count: 4
  slug: reactor-property-resource
- name: PropertySingleResponse
  property_count: 0
  slug: reactor-property-single-response
- name: PropertyUpdateRequest
  property_count: 1
  slug: reactor-property-update-request
- name: RelationshipRequest
  property_count: 1
  slug: reactor-relationship-request
- name: Relationship
  property_count: 2
  slug: reactor-relationship
- name: RelationshipSingleRequest
  property_count: 1
  slug: reactor-relationship-single-request
- name: RuleAttributes
  property_count: 7
  slug: reactor-rule-attributes
- name: RuleComponentAttributes
  property_count: 13
  slug: reactor-rule-component-attributes
- name: RuleComponentCreateRequest
  property_count: 1
  slug: reactor-rule-component-create-request
- name: RuleComponentListResponse
  property_count: 1
  slug: reactor-rule-component-list-response
- name: RuleComponentResource
  property_count: 4
  slug: reactor-rule-component-resource
- name: RuleComponentSingleResponse
  property_count: 0
  slug: reactor-rule-component-single-response
- name: RuleComponentUpdateRequest
  property_count: 1
  slug: reactor-rule-component-update-request
- name: RuleCreateRequest
  property_count: 1
  slug: reactor-rule-create-request
- name: RuleListResponse
  property_count: 1
  slug: reactor-rule-list-response
- name: RuleResource
  property_count: 4
  slug: reactor-rule-resource
- name: RuleSingleResponse
  property_count: 0
  slug: reactor-rule-single-response
- name: RuleUpdateRequest
  property_count: 1
  slug: reactor-rule-update-request
- name: SearchRequest
  property_count: 1
  slug: reactor-search-request
- name: SearchResponse
  property_count: 2
  slug: reactor-search-response
- name: SecretAttributes
  property_count: 6
  slug: reactor-secret-attributes
- name: SecretCreateRequest
  property_count: 1
  slug: reactor-secret-create-request
- name: SecretListResponse
  property_count: 1
  slug: reactor-secret-list-response
- name: SecretResource
  property_count: 4
  slug: reactor-secret-resource
- name: SecretSingleResponse
  property_count: 0
  slug: reactor-secret-single-response
- name: SecretUpdateRequest
  property_count: 1
  slug: reactor-secret-update-request
- name: Adobe Experience Platform Tags Rule
  property_count: 5
  slug: rule
json_structures:
- name: Data Collection Collect Request Structure
  property_count: 1
  slug: data-collection-collect-request-structure
- name: Data Collection Collect Response Structure
  property_count: 1
  slug: data-collection-collect-response-structure
- name: Data Collection Error Response Structure
  property_count: 5
  slug: data-collection-error-response-structure
- name: Data Collection Interact Request Structure
  property_count: 1
  slug: data-collection-interact-request-structure
- name: Data Collection Interact Response Structure
  property_count: 2
  slug: data-collection-interact-response-structure
- name: Data Collection Media Error Request Structure
  property_count: 1
  slug: data-collection-media-error-request-structure
- name: Data Collection Media Event Request Structure
  property_count: 1
  slug: data-collection-media-event-request-structure
- name: Data Collection Media Session Start Request Structure
  property_count: 1
  slug: data-collection-media-session-start-request-structure
- name: Data Collection Media Session Start Response Structure
  property_count: 2
  slug: data-collection-media-session-start-response-structure
- name: Data Collection Xdm Event Structure
  property_count: 5
  slug: data-collection-xdm-event-structure
- name: Event Forwarding Data Element Create Request Structure
  property_count: 1
  slug: event-forwarding-data-element-create-request-structure
- name: Event Forwarding Data Element List Response Structure
  property_count: 1
  slug: event-forwarding-data-element-list-response-structure
- name: Event Forwarding Data Element Resource Structure
  property_count: 4
  slug: event-forwarding-data-element-resource-structure
- name: Event Forwarding Data Element Single Response Structure
  property_count: 0
  slug: event-forwarding-data-element-single-response-structure
- name: Event Forwarding Environment List Response Structure
  property_count: 1
  slug: event-forwarding-environment-list-response-structure
- name: Event Forwarding Environment Single Response Structure
  property_count: 1
  slug: event-forwarding-environment-single-response-structure
- name: Event Forwarding Error Response Structure
  property_count: 1
  slug: event-forwarding-error-response-structure
- name: Event Forwarding Extension List Response Structure
  property_count: 1
  slug: event-forwarding-extension-list-response-structure
- name: Event Forwarding Library Create Request Structure
  property_count: 1
  slug: event-forwarding-library-create-request-structure
- name: Event Forwarding Library List Response Structure
  property_count: 1
  slug: event-forwarding-library-list-response-structure
- name: Event Forwarding Library Single Response Structure
  property_count: 1
  slug: event-forwarding-library-single-response-structure
- name: Event Forwarding Pagination Meta Structure
  property_count: 1
  slug: event-forwarding-pagination-meta-structure
- name: Event Forwarding Property Attributes Structure
  property_count: 5
  slug: event-forwarding-property-attributes-structure
- name: Event Forwarding Property Create Request Structure
  property_count: 1
  slug: event-forwarding-property-create-request-structure
- name: Event Forwarding Property List Response Structure
  property_count: 1
  slug: event-forwarding-property-list-response-structure
- name: Event Forwarding Property Resource Structure
  property_count: 3
  slug: event-forwarding-property-resource-structure
- name: Event Forwarding Property Single Response Structure
  property_count: 0
  slug: event-forwarding-property-single-response-structure
- name: Event Forwarding Property Update Request Structure
  property_count: 1
  slug: event-forwarding-property-update-request-structure
- name: Event Forwarding Relationship Structure
  property_count: 2
  slug: event-forwarding-relationship-structure
- name: Event Forwarding Rule Create Request Structure
  property_count: 1
  slug: event-forwarding-rule-create-request-structure
- name: Event Forwarding Rule List Response Structure
  property_count: 1
  slug: event-forwarding-rule-list-response-structure
- name: Event Forwarding Rule Resource Structure
  property_count: 4
  slug: event-forwarding-rule-resource-structure
- name: Event Forwarding Rule Single Response Structure
  property_count: 0
  slug: event-forwarding-rule-single-response-structure
- name: Event Forwarding Rule Update Request Structure
  property_count: 1
  slug: event-forwarding-rule-update-request-structure
- name: Event Forwarding Secret Attributes Structure
  property_count: 6
  slug: event-forwarding-secret-attributes-structure
- name: Event Forwarding Secret Create Request Structure
  property_count: 1
  slug: event-forwarding-secret-create-request-structure
- name: Event Forwarding Secret List Response Structure
  property_count: 1
  slug: event-forwarding-secret-list-response-structure
- name: Event Forwarding Secret Resource Structure
  property_count: 3
  slug: event-forwarding-secret-resource-structure
- name: Event Forwarding Secret Single Response Structure
  property_count: 0
  slug: event-forwarding-secret-single-response-structure
- name: Event Forwarding Secret Update Request Structure
  property_count: 1
  slug: event-forwarding-secret-update-request-structure
- name: Extension Error Response Structure
  property_count: 1
  slug: extension-error-response-structure
- name: Extension Extension Attributes Structure
  property_count: 12
  slug: extension-extension-attributes-structure
- name: Extension Extension Install Request Structure
  property_count: 1
  slug: extension-extension-install-request-structure
- name: Extension Extension List Response Structure
  property_count: 1
  slug: extension-extension-list-response-structure
- name: Extension Extension Package Attributes Structure
  property_count: 13
  slug: extension-extension-package-attributes-structure
- name: Extension Extension Package List Response Structure
  property_count: 1
  slug: extension-extension-package-list-response-structure
- name: Extension Extension Package Resource Structure
  property_count: 4
  slug: extension-extension-package-resource-structure
- name: Extension Extension Package Single Response Structure
  property_count: 0
  slug: extension-extension-package-single-response-structure
- name: Extension Extension Package Update Request Structure
  property_count: 1
  slug: extension-extension-package-update-request-structure
- name: Extension Extension Resource Structure
  property_count: 4
  slug: extension-extension-resource-structure
- name: Extension Extension Revise Request Structure
  property_count: 1
  slug: extension-extension-revise-request-structure
- name: Extension Extension Single Response Structure
  property_count: 0
  slug: extension-extension-single-response-structure
- name: Extension Library List Response Structure
  property_count: 1
  slug: extension-library-list-response-structure
- name: Extension Pagination Meta Structure
  property_count: 1
  slug: extension-pagination-meta-structure
- name: Extension Property Single Response Structure
  property_count: 1
  slug: extension-property-single-response-structure
- name: Extension Relationship Structure
  property_count: 2
  slug: extension-relationship-structure
- name: Reactor Build Attributes Structure
  property_count: 4
  slug: reactor-build-attributes-structure
- name: Reactor Build List Response Structure
  property_count: 1
  slug: reactor-build-list-response-structure
- name: Reactor Build Resource Structure
  property_count: 4
  slug: reactor-build-resource-structure
- name: Reactor Build Single Response Structure
  property_count: 0
  slug: reactor-build-single-response-structure
- name: Reactor Callback Attributes Structure
  property_count: 4
  slug: reactor-callback-attributes-structure
- name: Reactor Callback Create Request Structure
  property_count: 1
  slug: reactor-callback-create-request-structure
- name: Reactor Callback List Response Structure
  property_count: 1
  slug: reactor-callback-list-response-structure
- name: Reactor Callback Resource Structure
  property_count: 4
  slug: reactor-callback-resource-structure
- name: Reactor Callback Single Response Structure
  property_count: 0
  slug: reactor-callback-single-response-structure
- name: Reactor Callback Update Request Structure
  property_count: 1
  slug: reactor-callback-update-request-structure
- name: Reactor Company Attributes Structure
  property_count: 7
  slug: reactor-company-attributes-structure
- name: Reactor Company List Response Structure
  property_count: 1
  slug: reactor-company-list-response-structure
- name: Reactor Company Resource Structure
  property_count: 4
  slug: reactor-company-resource-structure
- name: Reactor Company Single Response Structure
  property_count: 0
  slug: reactor-company-single-response-structure
- name: Reactor Data Element Attributes Structure
  property_count: 13
  slug: reactor-data-element-attributes-structure
- name: Reactor Data Element Create Request Structure
  property_count: 1
  slug: reactor-data-element-create-request-structure
- name: Reactor Data Element List Response Structure
  property_count: 1
  slug: reactor-data-element-list-response-structure
- name: Reactor Data Element Resource Structure
  property_count: 4
  slug: reactor-data-element-resource-structure
- name: Reactor Data Element Single Response Structure
  property_count: 0
  slug: reactor-data-element-single-response-structure
- name: Reactor Data Element Update Request Structure
  property_count: 1
  slug: reactor-data-element-update-request-structure
- name: Reactor Environment Attributes Structure
  property_count: 9
  slug: reactor-environment-attributes-structure
- name: Reactor Environment Create Request Structure
  property_count: 1
  slug: reactor-environment-create-request-structure
- name: Reactor Environment List Response Structure
  property_count: 1
  slug: reactor-environment-list-response-structure
- name: Reactor Environment Resource Structure
  property_count: 4
  slug: reactor-environment-resource-structure
- name: Reactor Environment Single Response Structure
  property_count: 0
  slug: reactor-environment-single-response-structure
- name: Reactor Environment Update Request Structure
  property_count: 1
  slug: reactor-environment-update-request-structure
- name: Reactor Error Response Structure
  property_count: 1
  slug: reactor-error-response-structure
- name: Reactor Extension Attributes Structure
  property_count: 12
  slug: reactor-extension-attributes-structure
- name: Reactor Extension Create Request Structure
  property_count: 1
  slug: reactor-extension-create-request-structure
- name: Reactor Extension List Response Structure
  property_count: 1
  slug: reactor-extension-list-response-structure
- name: Reactor Extension Package Attributes Structure
  property_count: 11
  slug: reactor-extension-package-attributes-structure
- name: Reactor Extension Package List Response Structure
  property_count: 1
  slug: reactor-extension-package-list-response-structure
- name: Reactor Extension Package Resource Structure
  property_count: 3
  slug: reactor-extension-package-resource-structure
- name: Reactor Extension Package Single Response Structure
  property_count: 0
  slug: reactor-extension-package-single-response-structure
- name: Reactor Extension Resource Structure
  property_count: 4
  slug: reactor-extension-resource-structure
- name: Reactor Extension Single Response Structure
  property_count: 0
  slug: reactor-extension-single-response-structure
- name: Reactor Extension Update Request Structure
  property_count: 1
  slug: reactor-extension-update-request-structure
- name: Reactor Host Attributes Structure
  property_count: 11
  slug: reactor-host-attributes-structure
- name: Reactor Host Create Request Structure
  property_count: 1
  slug: reactor-host-create-request-structure
- name: Reactor Host List Response Structure
  property_count: 1
  slug: reactor-host-list-response-structure
- name: Reactor Host Resource Structure
  property_count: 4
  slug: reactor-host-resource-structure
- name: Reactor Host Single Response Structure
  property_count: 0
  slug: reactor-host-single-response-structure
- name: Reactor Host Update Request Structure
  property_count: 1
  slug: reactor-host-update-request-structure
- name: Reactor Library Attributes Structure
  property_count: 5
  slug: reactor-library-attributes-structure
- name: Reactor Library Create Request Structure
  property_count: 1
  slug: reactor-library-create-request-structure
- name: Reactor Library List Response Structure
  property_count: 1
  slug: reactor-library-list-response-structure
- name: Reactor Library Resource Structure
  property_count: 4
  slug: reactor-library-resource-structure
- name: Reactor Library Single Response Structure
  property_count: 0
  slug: reactor-library-single-response-structure
- name: Reactor Library Update Request Structure
  property_count: 1
  slug: reactor-library-update-request-structure
- name: Reactor Pagination Meta Structure
  property_count: 1
  slug: reactor-pagination-meta-structure
- name: Reactor Property Attributes Structure
  property_count: 12
  slug: reactor-property-attributes-structure
- name: Reactor Property Create Request Structure
  property_count: 1
  slug: reactor-property-create-request-structure
- name: Reactor Property List Response Structure
  property_count: 1
  slug: reactor-property-list-response-structure
- name: Reactor Property Resource Structure
  property_count: 4
  slug: reactor-property-resource-structure
- name: Reactor Property Single Response Structure
  property_count: 0
  slug: reactor-property-single-response-structure
- name: Reactor Property Update Request Structure
  property_count: 1
  slug: reactor-property-update-request-structure
- name: Reactor Relationship Request Structure
  property_count: 1
  slug: reactor-relationship-request-structure
- name: Reactor Relationship Single Request Structure
  property_count: 1
  slug: reactor-relationship-single-request-structure
- name: Reactor Relationship Structure
  property_count: 2
  slug: reactor-relationship-structure
- name: Reactor Rule Attributes Structure
  property_count: 7
  slug: reactor-rule-attributes-structure
- name: Reactor Rule Component Attributes Structure
  property_count: 13
  slug: reactor-rule-component-attributes-structure
- name: Reactor Rule Component Create Request Structure
  property_count: 1
  slug: reactor-rule-component-create-request-structure
- name: Reactor Rule Component List Response Structure
  property_count: 1
  slug: reactor-rule-component-list-response-structure
- name: Reactor Rule Component Resource Structure
  property_count: 4
  slug: reactor-rule-component-resource-structure
- name: Reactor Rule Component Single Response Structure
  property_count: 0
  slug: reactor-rule-component-single-response-structure
- name: Reactor Rule Component Update Request Structure
  property_count: 1
  slug: reactor-rule-component-update-request-structure
- name: Reactor Rule Create Request Structure
  property_count: 1
  slug: reactor-rule-create-request-structure
- name: Reactor Rule List Response Structure
  property_count: 1
  slug: reactor-rule-list-response-structure
- name: Reactor Rule Resource Structure
  property_count: 4
  slug: reactor-rule-resource-structure
- name: Reactor Rule Single Response Structure
  property_count: 0
  slug: reactor-rule-single-response-structure
- name: Reactor Rule Update Request Structure
  property_count: 1
  slug: reactor-rule-update-request-structure
- name: Reactor Search Request Structure
  property_count: 1
  slug: reactor-search-request-structure
- name: Reactor Search Response Structure
  property_count: 2
  slug: reactor-search-response-structure
- name: Reactor Secret Attributes Structure
  property_count: 6
  slug: reactor-secret-attributes-structure
- name: Reactor Secret Create Request Structure
  property_count: 1
  slug: reactor-secret-create-request-structure
- name: Reactor Secret List Response Structure
  property_count: 1
  slug: reactor-secret-list-response-structure
- name: Reactor Secret Resource Structure
  property_count: 4
  slug: reactor-secret-resource-structure
- name: Reactor Secret Single Response Structure
  property_count: 0
  slug: reactor-secret-single-response-structure
- name: Reactor Secret Update Request Structure
  property_count: 1
  slug: reactor-secret-update-request-structure
jsonld:
- class_count: 67
  name: context Context
  property_count: 30
  slug: context
- class_count: 0
  name: Data Collection Context
  property_count: 0
  slug: data-collection-context
- class_count: 0
  name: Event Forwarding Context
  property_count: 0
  slug: event-forwarding-context
- class_count: 0
  name: Extension Context
  property_count: 0
  slug: extension-context
- class_count: 0
  name: Reactor Context
  property_count: 0
  slug: reactor-context
layout: provider
modified: '2026-09-16'
name: Adobe Launch
nav: Providers
network: true
overview: 'Adobe Launch publishes 36 APIs on the [APIs.io](https://apis.io/) network, including Builds API, Callbacks API, Companies API, and 33 more. Tagged areas include Data Collection, Edge Network, Event Forwarding, Marketing Technology, and Tag Management.


  The Adobe Launch catalog on APIs.io includes 1 event-driven AsyncAPI specification, 5 JSON-LD contexts, and 2 Spectral governance rulesets.


  Adobe Launch''s developer surface includes authentication, developer console, developer portal, engineering blog, signup flow, changelog, CLI, and 58 more developer resources.'
plans:
- name: Adobe Launch Plans Pricing
  plan_count: 1
  slug: adobe-launch-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Adobe Launch Rate Limits
  slug: adobe-launch-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Adobe Launch API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: adobe-launch-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Adobe Launch API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 6
  slug: adobe-launch-spectral-rules
scopes:
- name: Adobe Launch Scopes
  scope_count: 5
  slug: adobe-launch-scopes
  summary_line: 5 scopes · client_credentials
score:
  band: exemplar
  composite: 74.8
  coverage:
    artifact_dirs: 37
    catalog_earned: 87.5
    catalog_earned_first_party: 20.0
    catalog_gap: 27.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.8
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 70.7
    developer_ergonomics: 91.1
    discoverability: 73.2
    operational_transparency: 76.3
  previous_composite: 72.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/screenshots/adobe-launch-2026-06-20T164946.png
security:
- kind: authentication
  name: Adobe Launch Authentication
  slug: adobe-launch-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Adobe Launch Domain Security
  slug: adobe-launch-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Launch Vulnerability Disclosure
  slug: adobe-launch-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Adobe Launch Trust Center
  slug: adobe-launch-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27002, FedRAMP, PCI DSS, HIPAA, BSI C5
slug: adobe-launch
tags:
- Data Collection
- Edge Network
- Event Forwarding
- Marketing Technology
- Tag Management
use_cases:
- Unified tag management across marketing tools
- Server-side event forwarding for privacy compliance
- Custom extension development for third-party integrations
- Real-time data collection from web and mobile applications
- Media analytics tracking for video and audio content
- A/B testing and personalization data routing
- Cross-platform data collection orchestration
website: https://www.adobe.com/
---
