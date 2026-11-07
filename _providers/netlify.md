---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
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
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 73
  human_in_the_loop: 1
  name: Netlify Agentic Access
  operation_count: 133
  slug: netlify-agentic-access
  summary_line: 133 operations · 73 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The accountType API from Netlify — 1 operation(s) for accounttype.
  name: Netlify Account Type API
  phrasing_intents:
  - id: listAccountTypesForUser
    intent: List available team plan types
    question: Which plan types can I choose for a team?
  phrasing_ops: 1
  slug: netlify-accounttype-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Asset API from Netlify — 2 operation(s) for asset.
  name: Netlify Asset API
  phrasing_intents:
  - id: listSiteAssets
    intent: List a site's uploaded assets
    question: What assets have been uploaded to my site?
  - id: createSiteAsset
    intent: Start an asset upload for a site
    question: How do I upload a file as a site asset?
  - id: getSiteAssetInfo
    intent: Get a site asset's details
    question: Can I check the details of one uploaded asset?
  - id: updateSiteAsset
    intent: Update a site asset's state
    question: How do I mark an asset upload as finished?
  - id: deleteSiteAsset
    intent: Delete a site asset
    question: How do I delete an uploaded asset?
  phrasing_ops: 5
  slug: netlify-asset-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The assetPublicSignature API from Netlify — 1 operation(s) for assetpublicsignature.
  name: Netlify Asset Public Signature API
  phrasing_intents:
  - id: getSiteAssetPublicSignature
    intent: Get a public signed URL for an asset
    question: Can I get a public signature to share a private site asset?
  phrasing_ops: 1
  slug: netlify-assetpublicsignature-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Build API from Netlify — 4 operation(s) for build.
  name: Netlify Build API
  phrasing_intents:
  - id: listSiteBuilds
    intent: List a site's builds
    question: What builds have run for my site?
  - id: createSiteBuild
    intent: Trigger a build for a site
    question: How do I trigger a new build of my Netlify site?
  - id: getSiteBuild
    intent: Get a build
    question: What's the status of a particular build?
  - id: notifyBuildStart
    intent: Report that a build has started
    question: How does a build runner signal that a build has begun?
  - id: getAccountBuildStatus
    intent: Get a team's build capacity status
    question: How many builds are running or queued for my team?
  phrasing_ops: 5
  slug: netlify-build-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The buildHook API from Netlify — 2 operation(s) for buildhook.
  name: Netlify Build Hook API
  phrasing_intents:
  - id: listSiteBuildHooks
    intent: List a site's build hooks
    question: What build hook URLs exist for my site?
  - id: createSiteBuildHook
    intent: Create a build hook
    question: How do I get a URL that triggers a build when a CMS publishes?
  - id: getSiteBuildHook
    intent: Get a build hook
    question: Which branch does a particular build hook build?
  - id: updateSiteBuildHook
    intent: Update a build hook
    question: Can I rename a build hook or change its branch?
  - id: deleteSiteBuildHook
    intent: Delete a build hook
    question: How do I revoke a build hook URL?
  phrasing_ops: 5
  slug: netlify-buildhook-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The buildLogMsg API from Netlify — 1 operation(s) for buildlogmsg.
  name: Netlify Build Log Msg API
  phrasing_intents:
  - id: updateSiteBuildLog
    intent: Append a message to a build log
    question: Can I write a custom message into a build's log?
  phrasing_ops: 1
  slug: netlify-buildlogmsg-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Deploy API from Netlify — 8 operation(s) for deploy.
  name: Netlify Deploy API
  phrasing_intents:
  - id: listSiteDeploys
    intent: List a site's deploys
    question: How do I see the deploy history for my site?
  - id: createSiteDeploy
    intent: Create a new deploy for a site
    question: How do I deploy files to my Netlify site through the API?
  - id: getSiteDeploy
    intent: Get a deploy scoped to a site
    question: Can I look up a deploy's details within a specific site?
  - id: updateSiteDeploy
    intent: Update an existing site deploy
    question: Can I add files to a deploy I already created?
  - id: deleteSiteDeploy
    intent: Delete a deploy from a site
    question: Can I delete a specific deploy from my site's history?
  - id: cancelSiteDeploy
    intent: Cancel a running deploy
    question: How do I stop a deploy that's still in progress?
  - id: restoreSiteDeploy
    intent: Restore a previous deploy as live
    question: Can I republish an older deploy of my site?
  - id: rollbackSiteDeploy
    intent: Roll back a site to its previous deploy
    question: Can I quickly undo my latest production deploy?
  phrasing_ops: 13
  slug: netlify-deploy-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The deployedBranch API from Netlify — 1 operation(s) for deployedbranch.
  name: Netlify Deployed Branch API
  phrasing_intents:
  - id: listSiteDeployedBranches
    intent: List a site's deployed branches
    question: Which Git branches currently have deploys on my site?
  phrasing_ops: 1
  slug: netlify-deployedbranch-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The deployKey API from Netlify — 2 operation(s) for deploykey.
  name: Netlify Deploy Key API
  phrasing_intents:
  - id: listDeployKeys
    intent: List deploy keys
    question: What deploy keys exist on my account?
  - id: createDeployKey
    intent: Create a deploy key
    question: How do I generate a new SSH deploy key for a private repo?
  - id: getDeployKey
    intent: Get a deploy key
    question: Can I retrieve the public key of an existing deploy key?
  - id: deleteDeployKey
    intent: Delete a deploy key
    question: How do I delete a deploy key I no longer use?
  phrasing_ops: 4
  slug: netlify-deploykey-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The devServerHook API from Netlify — 2 operation(s) for devserverhook.
  name: Netlify Dev Server Hook API
  phrasing_intents:
  - id: listSiteDevServerHooks
    intent: List a site's dev server hooks
    question: Which dev server hooks are set up for my site?
  - id: createSiteDevServerHook
    intent: Create a dev server hook
    question: How do I create a hook URL that starts a dev server?
  - id: getSiteDevServerHook
    intent: Get a dev server hook
    question: Can I look up one dev server hook's settings?
  - id: updateSiteDevServerHook
    intent: Update a dev server hook
    question: Can I rename a dev server hook?
  - id: deleteSiteDevServerHook
    intent: Delete a dev server hook
    question: How do I delete a dev server hook?
  phrasing_ops: 5
  slug: netlify-devserverhook-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The dnsZone API from Netlify — 6 operation(s) for dnszone.
  name: Netlify Dns Zone API
  phrasing_intents:
  - id: getDNSForSite
    intent: Get DNS zones for a site
    question: Which DNS zones are connected to my site?
  - id: configureDNSForSite
    intent: Configure Netlify DNS for a site
    question: How do I set up Netlify DNS for my site's domain?
  - id: createDnsZone
    intent: Create a DNS zone
    question: Can I create a DNS zone for a domain and link it to a site?
  - id: getDnsZones
    intent: List DNS zones
    question: What DNS zones do I manage?
  - id: getDnsZone
    intent: Get a DNS zone
    question: Can I view the details of one DNS zone?
  - id: deleteDnsZone
    intent: Delete a DNS zone
    question: How do I stop managing a domain's DNS and remove its zone?
  - id: transferDnsZone
    intent: Transfer a DNS zone to another team
    question: Can I move a DNS zone from one team to another?
  - id: getDnsRecords
    intent: List records in a DNS zone
    question: What DNS records are in my zone?
  phrasing_ops: 11
  slug: netlify-dnszone-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The File API from Netlify — 3 operation(s) for file.
  name: Netlify File API
  phrasing_intents:
  - id: listSiteFiles
    intent: List files in a site's live deploy
    question: What files are in my site's currently published deploy?
  - id: getSiteFileByPathName
    intent: Get a site file by path
    question: Can I fetch one file from my site by its path?
  - id: uploadDeployFile
    intent: Upload a file to a deploy
    question: How do I upload a file that a new deploy is asking for?
  phrasing_ops: 3
  slug: netlify-file-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Form API from Netlify — 2 operation(s) for form.
  name: Netlify Form API
  phrasing_intents:
  - id: listSiteForms
    intent: List a site's forms
    question: Which forms has my site detected?
  - id: deleteSiteForm
    intent: Delete a form from a site
    question: How do I delete a form I no longer use?
  phrasing_ops: 2
  slug: netlify-form-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Function API from Netlify — 2 operation(s) for function.
  name: Netlify Function API
  phrasing_intents:
  - id: searchSiteFunctions
    intent: List or search a site's functions
    question: What serverless functions does my site have?
  - id: uploadDeployFunction
    intent: Upload a function to a deploy
    question: How do I upload a serverless function bundle to a deploy?
  phrasing_ops: 2
  slug: netlify-function-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Hook API from Netlify — 3 operation(s) for hook.
  name: Netlify Hook API
  phrasing_intents:
  - id: listHooksBySiteId
    intent: List a site's notification hooks
    question: What notifications are set up for my site's deploys?
  - id: createHookBySiteId
    intent: Add a deploy notification hook
    question: How do I get a webhook when a deploy succeeds or fails?
  - id: getHook
    intent: Get a notification hook
    question: Can I see how a notification hook is configured?
  - id: updateHook
    intent: Update a notification hook
    question: Can I change which event a notification hook listens to?
  - id: deleteHook
    intent: Delete a notification hook
    question: How do I remove a deploy notification?
  - id: enableHook
    intent: Re-enable a disabled notification hook
    question: Can I turn a disabled notification hook back on?
  phrasing_ops: 6
  slug: netlify-hook-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The hookType API from Netlify — 1 operation(s) for hooktype.
  name: Netlify Hook Type API
  phrasing_intents:
  - id: listHookTypes
    intent: List notification hook types
    question: What kinds of notification hooks can I set up?
  phrasing_ops: 1
  slug: netlify-hooktype-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Member API from Netlify — 2 operation(s) for member.
  name: Netlify Member API
  phrasing_intents:
  - id: listMembersForAccount
    intent: List a team's members
    question: Who are the members of my team?
  - id: addMemberToAccount
    intent: Invite a member to a team
    question: How do I invite someone to my Netlify team?
  - id: getAccountMember
    intent: Get a team member
    question: Can I look up one team member's role and access?
  - id: updateAccountMember
    intent: Change a team member's role or access
    question: How do I change a team member's role?
  - id: removeAccountMember
    intent: Remove a member from a team
    question: How do I remove someone from my team?
  phrasing_ops: 5
  slug: netlify-member-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Metadata API from Netlify — 1 operation(s) for metadata.
  name: Netlify Metadata API
  phrasing_intents:
  - id: getSiteMetadata
    intent: Get a site's metadata
    question: What custom metadata is stored on my site?
  - id: updateSiteMetadata
    intent: Update a site's metadata
    question: Can I attach my own metadata to a site?
  phrasing_ops: 2
  slug: netlify-metadata-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Purge API from Netlify — 1 operation(s) for purge.
  name: Netlify Purge API
  phrasing_intents:
  - id: purgeCache
    intent: Purge cached content from the CDN
    question: How do I clear my site's CDN cache without redeploying?
  phrasing_ops: 1
  slug: netlify-purge-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The serviceInstance API from Netlify — 3 operation(s) for serviceinstance.
  name: Netlify Service Instance API
  phrasing_intents:
  - id: listServiceInstancesForSite
    intent: List add-on instances on a site
    question: Which add-on services are installed on my site?
  - id: createServiceInstance
    intent: Install an add-on on a site
    question: How do I add an add-on service to my site?
  - id: showServiceInstance
    intent: Get an add-on instance
    question: Can I see the configuration of an installed add-on?
  - id: updateServiceInstance
    intent: Update an add-on instance
    question: Can I change the settings of an installed add-on?
  - id: deleteServiceInstance
    intent: Remove an add-on from a site
    question: How do I uninstall an add-on from my site?
  phrasing_ops: 5
  slug: netlify-serviceinstance-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Site API from Netlify — 4 operation(s) for site.
  name: Netlify Site API
  phrasing_intents:
  - id: listSites
    intent: List my sites
    question: What sites do I have access to?
  - id: createSite
    intent: Create a new site
    question: How do I create a new Netlify site through the API?
  - id: getSite
    intent: Get a site's details
    question: Can I see a site's settings, URL and published deploy?
  - id: updateSite
    intent: Update a site's settings
    question: Can I rename a site or change its custom domain?
  - id: deleteSite
    intent: Delete a site
    question: How do I permanently delete a site?
  - id: unlinkSiteRepo
    intent: Unlink a site's Git repository
    question: How do I disconnect my site from its Git repo?
  - id: enableSite
    intent: Re-enable a disabled site
    question: Can I turn a site back on after I disabled it?
  - id: disableSite
    intent: Disable a site
    question: How do I take a site offline temporarily without deleting it?
  phrasing_ops: 10
  slug: netlify-site-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The sniCertificate API from Netlify — 1 operation(s) for snicertificate.
  name: Netlify Sni Certificate API
  phrasing_intents:
  - id: provisionSiteTLSCertificate
    intent: Provision or upload a TLS certificate
    question: How do I get a free Let's Encrypt certificate for my site?
  - id: showSiteTLSCertificate
    intent: Get a site's TLS certificate
    question: What TLS certificate is my site using?
  - id: getAllCertificates
    intent: List certificates for a site domain
    question: Which certificates cover a particular domain on my site?
  phrasing_ops: 3
  slug: netlify-snicertificate-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Snippet API from Netlify — 2 operation(s) for snippet.
  name: Netlify Snippet API
  phrasing_intents:
  - id: listSiteSnippets
    intent: List a site's injected snippets
    question: What script snippets are injected into my site's pages?
  - id: createSiteSnippet
    intent: Inject a snippet into a site
    question: How do I add an analytics script to every page of my site?
  - id: getSiteSnippet
    intent: Get an injected snippet
    question: Can I view the code of one injected snippet?
  - id: updateSiteSnippet
    intent: Update an injected snippet
    question: Can I edit a snippet that's already injected?
  - id: deleteSiteSnippet
    intent: Remove an injected snippet
    question: How do I stop injecting a script into my site?
  phrasing_ops: 5
  slug: netlify-snippet-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Submission API from Netlify — 3 operation(s) for submission.
  name: Netlify Submission API
  phrasing_intents:
  - id: listSiteSubmissions
    intent: List all form submissions for a site
    question: Where can I see every form submission across my whole site?
  - id: listFormSubmissions
    intent: List submissions for one form
    question: How do I get the entries submitted to a specific form?
  - id: listFormSubmission
    intent: Get a form submission
    question: Can I look up a single form submission by its ID?
  - id: deleteSubmission
    intent: Delete a form submission
    question: How do I delete a spam form submission?
  phrasing_ops: 4
  slug: netlify-submission-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Ticket API from Netlify — 2 operation(s) for ticket.
  name: Netlify Ticket API
  phrasing_intents:
  - id: createTicket
    intent: Create an OAuth authorization ticket
    question: How does my app start an OAuth ticket flow for a user?
  - id: showTicket
    intent: Check an OAuth ticket's status
    question: Has the user authorized my OAuth ticket yet?
  phrasing_ops: 2
  slug: netlify-ticket-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The User API from Netlify — 1 operation(s) for user.
  name: Netlify User API
  phrasing_intents:
  - id: getCurrentUser
    intent: Get the current user
    question: Which user is my API token authenticated as?
  phrasing_ops: 1
  slug: netlify-user-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The X-Internal API from Netlify — 3 operation(s) for x-internal.
  name: Netlify X-Internal API
  phrasing_intents:
  - id: updatePlugin
    intent: Pin a build plugin version
    question: Can I pin a build plugin to a specific version on my site?
  - id: getLatestPluginRuns
    intent: Get the latest build plugin runs
    question: What happened the last time my build plugins ran?
  - id: createPluginRun
    intent: Record a build plugin run on a deploy
    question: How does a build plugin report its result on a deploy?
  phrasing_ops: 3
  slug: netlify-x-internal-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The agentRunner API from Netlify — 6 operation(s) for agentrunner.
  name: Netlify Agent Runner API
  phrasing_intents:
  - id: listAgentRunners
    intent: List agent runs for a site
    question: Which AI agent runs have been started on my site?
  - id: createAgentRunner
    intent: Start an AI agent run on a site
    question: How do I kick off an AI agent to make changes to my Netlify site?
  - id: createAgentRunnerUploadUrl
    intent: Get an upload URL for an agent run file
    question: Can I attach a file for an agent run to use?
  - id: getAgentRunner
    intent: Get an agent run
    question: What is the status of my agent run?
  - id: updateAgentRunner
    intent: Update an agent run
    question: Can I change an agent run after it's been created?
  - id: deleteAgentRunner
    intent: Delete an agent run
    question: How do I delete an agent run I don't need?
  - id: archiveAgentRunner
    intent: Archive an agent run
    question: How do I archive an agent run without deleting it?
  - id: agentRunnerPullRequest
    intent: Open a pull request from an agent run
    question: Can an agent run open a pull request with its changes?
  phrasing_ops: 9
  slug: netlify-agentrunner-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The agentRunnerHook API from Netlify — 2 operation(s) for agentrunnerhook.
  name: Netlify Agent Runner Hook API
  phrasing_intents:
  - id: listSiteAgentRunnerHooks
    intent: List a site's agent run hooks
    question: Which agent run hooks are set up for my site?
  - id: createSiteAgentRunnerHook
    intent: Create an agent run hook
    question: How do I create a hook URL that kicks off an AI agent run?
  - id: getSiteAgentRunnerHook
    intent: Get an agent run hook
    question: What prompt does a particular agent run hook use?
  - id: updateSiteAgentRunnerHook
    intent: Update an agent run hook
    question: Can I change the prompt an agent run hook sends?
  - id: deleteSiteAgentRunnerHook
    intent: Delete an agent run hook
    question: How do I remove an agent run hook?
  phrasing_ops: 5
  slug: netlify-agentrunnerhook-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The agentRunnerSession API from Netlify — 2 operation(s) for agentrunnersession.
  name: Netlify Agent Runner Session API
  phrasing_intents:
  - id: listAgentRunnerSessions
    intent: List sessions of an agent run
    question: What sessions have happened within an agent run?
  - id: createAgentRunnerSession
    intent: Start a follow-up session in an agent run
    question: How do I send a follow-up prompt to an existing agent run?
  - id: getAgentRunnerSession
    intent: Get an agent run session
    question: Can I see what happened in one session of an agent run?
  - id: updateAgentRunnerSession
    intent: Publish or unpublish an agent run session
    question: Can I mark an agent session as published?
  - id: deleteAgentRunnerSession
    intent: Delete an agent run session
    question: How do I delete a single session from an agent run?
  phrasing_ops: 5
  slug: netlify-agentrunnersession-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The database API from Netlify — 14 operation(s) for database.
  name: Netlify Database API
  phrasing_intents:
  - id: createSiteDatabase
    intent: Create a database for a site
    question: How do I add a database to my Netlify site?
  - id: getSiteDatabase
    intent: Get a site's database connection string
    question: Where do I find the connection string for my site's database?
  - id: deleteSiteDatabase
    intent: Delete a site's database
    question: Can I delete my site's database along with all its branches and snapshots?
  - id: createSiteDatabaseBranch
    intent: Create a database branch
    question: Can I fork a new database branch off an existing parent branch?
  - id: listSiteDatabaseBranches
    intent: List a site's database branches
    question: Which database branches exist for my site and are they running?
  - id: getSiteDatabaseBranch
    intent: Get a database branch connection string
    question: Where do I get the connection string for one particular database branch?
  - id: deleteSiteDatabaseBranch
    intent: Delete a database branch
    question: How do I remove a database branch I no longer need?
  - id: resetSiteDatabaseBranch
    intent: Reset a database branch from its source
    question: Can I re-fork a preview database branch from production to start fresh?
  phrasing_ops: 19
  slug: netlify-database-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The edgeFunction API from Netlify — 1 operation(s) for edgefunction.
  name: Netlify Edge Function API
  phrasing_intents:
  - id: uploadDeployEdgeFunction
    intent: Upload an edge function bundle to a deploy
    question: Can I upload an edge function bundle that a deploy requires?
  phrasing_ops: 1
  slug: netlify-edgefunction-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The service API from Netlify — 3 operation(s) for service.
  name: Netlify Service API
  phrasing_intents:
  - id: getServices
    intent: List available add-on services
    question: What add-on services can I install?
  - id: showService
    intent: Get an add-on service
    question: Can I read the details of one add-on service?
  - id: showServiceManifest
    intent: Get an add-on's manifest
    question: Where do I find the configuration manifest for an add-on?
  phrasing_ops: 3
  slug: netlify-service-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Access Token API from Netlify — 1 operation(s) for access token.
  name: Netlify Access Token API
  phrasing_intents:
  - id: exchangeTicket
    intent: Exchange an OAuth ticket for an access token
    question: Once a user authorizes a ticket, can I swap it for an access token?
  phrasing_ops: 1
  slug: netlify-access-token-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Account Membership API from Netlify — 2 operation(s) for account membership.
  name: Netlify Account Membership API
  phrasing_intents:
  - id: listAccountsForUser
    intent: List my teams
    question: Which teams do I belong to?
  - id: createAccount
    intent: Create a team account
    question: How do I create a new team through the API?
  - id: getAccount
    intent: Get a team account
    question: Can I see a team's plan and billing details?
  - id: updateAccount
    intent: Update a team account
    question: Can I rename my team or change its slug?
  - id: cancelAccount
    intent: Cancel a team account
    question: How do I cancel a team account?
  phrasing_ops: 5
  slug: netlify-account-membership-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The AI Gateway API from Netlify — 3 operation(s) for ai gateway.
  name: Netlify AI Gateway API
  phrasing_intents:
  - id: getAIGatewayProviders
    intent: List AI Gateway providers
    question: Which model providers can I reach through the AI Gateway?
  - id: getAIGatewayToken
    intent: Get an AI Gateway token for a site
    question: Can I get an AI Gateway token scoped to one site?
  - id: getAccountAIGatewayToken
    intent: Get an AI Gateway token for a team
    question: Can I get an AI Gateway token for my whole team instead of one site?
  phrasing_ops: 3
  slug: netlify-ai-gateway-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Audit Log API from Netlify — 1 operation(s) for audit log.
  name: Netlify Audit Log API
  phrasing_intents:
  - id: listAccountAuditEvents
    intent: List a team's audit log events
    question: Who changed what in my team recently?
  phrasing_ops: 1
  slug: netlify-audit-log-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Dev Server API from Netlify — 4 operation(s) for dev server.
  name: Netlify Dev Server API
  phrasing_intents:
  - id: listSiteDevServers
    intent: List a site's dev servers
    question: Which dev servers are running for my site?
  - id: createSiteDevServer
    intent: Start a dev server for a site
    question: How do I spin up a cloud dev server for my site?
  - id: deleteSiteDevServers
    intent: Delete a site's dev servers
    question: Can I shut down all dev servers for a site at once?
  - id: getSiteDevServer
    intent: Get a dev server
    question: What state is my dev server in?
  - id: markDevServerActivity
    intent: Record activity on a dev server
    question: How do I keep a dev server from going idle?
  - id: updateDevServerState
    intent: Update a dev server's state
    question: Can I report a dev server's new state or an error?
  phrasing_ops: 6
  slug: netlify-dev-server-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Environment Variables API from Netlify — 4 operation(s) for environment variables.
  name: Netlify Environment Variables API
  phrasing_intents:
  - id: getEnvVars
    intent: List environment variables for a team or site
    question: How do I see all environment variables for my team?
  - id: createEnvVars
    intent: Create environment variables
    question: How do I add new environment variables to my team?
  - id: getSiteEnvVars
    intent: List a site's environment variables
    question: Can I get a site's environment variables without knowing the account ID?
  - id: getEnvVar
    intent: Get one environment variable
    question: Can I read the values of a single environment variable?
  - id: updateEnvVar
    intent: Replace an environment variable and its values
    question: How do I overwrite all values of an existing environment variable?
  - id: setEnvVarValue
    intent: Set an env var's value for one context
    question: Can I change an env var's value for only the production context?
  - id: deleteEnvVar
    intent: Delete an environment variable
    question: How do I remove an environment variable entirely?
  - id: deleteEnvVarValue
    intent: Delete one value of an environment variable
    question: Can I remove a single context value but keep the variable?
  phrasing_ops: 8
  slug: netlify-environment-variables-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Payment Method API from Netlify — 1 operation(s) for payment method.
  name: Netlify Payment Method API
  phrasing_intents:
  - id: listPaymentMethodsForUser
    intent: List my payment methods
    question: Which payment methods are on file for my account?
  phrasing_ops: 1
  slug: netlify-payment-method-api
- baseURL: https://api.netlify.com/api/v1/
  baseurl_source: declared
  description: The Split Test API from Netlify — 4 operation(s) for split test.
  name: Netlify Split Test API
  phrasing_intents:
  - id: createSplitTest
    intent: Create a branch split test
    question: How do I A/B test two branches of my Netlify site?
  - id: getSplitTests
    intent: List a site's split tests
    question: What split tests are configured on my site?
  - id: updateSplitTest
    intent: Update a split test's traffic split
    question: Can I change the traffic percentages in an existing split test?
  - id: getSplitTest
    intent: Get a split test
    question: Can I view one split test's traffic allocation?
  - id: enableSplitTest
    intent: Start a split test
    question: How do I publish a split test so it starts routing traffic?
  - id: disableSplitTest
    intent: Stop a split test
    question: How do I end an A/B test and send all traffic back to one branch?
  phrasing_ops: 6
  slug: netlify-split-test-api
artifact_total: 229
asyncapis:
- description: 'AsyncAPI description of Netlify''s asynchronous event surface. Two documented surfaces are modelled here: 1. Outgoing webhooks (deploy / form / split test notifications). Netlify issues an HTTP POST to'
  name: Netlify Webhooks and Build Hooks
  slug: netlify-webhooks-asyncapi
collections:
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken API
  slug: postman-netlify-accesstoken-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken accountMembership API
  slug: postman-netlify-accountmembership-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken accountType API
  slug: postman-netlify-accounttype-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Asset API
  slug: postman-netlify-asset-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken assetPublicSignature API
  slug: postman-netlify-assetpublicsignature-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken auditLog API
  slug: postman-netlify-auditlog-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Build API
  slug: postman-netlify-build-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken buildHook API
  slug: postman-netlify-buildhook-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken buildLogMsg API
  slug: postman-netlify-buildlogmsg-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Deploy API
  slug: postman-netlify-deploy-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken deployedBranch API
  slug: postman-netlify-deployedbranch-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken deployKey API
  slug: postman-netlify-deploykey-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken devServer API
  slug: postman-netlify-devserver-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken devServerHook API
  slug: postman-netlify-devserverhook-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken dnsZone API
  slug: postman-netlify-dnszone-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken environmentVariables API
  slug: postman-netlify-environmentvariables-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken File API
  slug: postman-netlify-file-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Form API
  slug: postman-netlify-form-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Function API
  slug: postman-netlify-function-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Hook API
  slug: postman-netlify-hook-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken hookType API
  slug: postman-netlify-hooktype-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Member API
  slug: postman-netlify-member-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Metadata API
  slug: postman-netlify-metadata-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken paymentMethod API
  slug: postman-netlify-paymentmethod-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Purge API
  slug: postman-netlify-purge-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken serviceInstance API
  slug: postman-netlify-serviceinstance-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Services API
  slug: postman-netlify-services-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Site API
  slug: postman-netlify-site-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken sniCertificate API
  slug: postman-netlify-snicertificate-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Snippet API
  slug: postman-netlify-snippet-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken splitTest API
  slug: postman-netlify-splittest-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Submission API
  slug: postman-netlify-submission-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken Ticket API
  slug: postman-netlify-ticket-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken User API
  slug: postman-netlify-user-api
- collection_type: postman
  name: Netlify Netlify's API documentation accessToken X-Internal API
  slug: postman-netlify-x-internal-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken API
  slug: open-netlify-accesstoken-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken accountMembership API
  slug: open-netlify-accountmembership-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken accountType API
  slug: open-netlify-accounttype-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Asset API
  slug: open-netlify-asset-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken assetPublicSignature API
  slug: open-netlify-assetpublicsignature-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken auditLog API
  slug: open-netlify-auditlog-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Build API
  slug: open-netlify-build-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken buildHook API
  slug: open-netlify-buildhook-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken buildLogMsg API
  slug: open-netlify-buildlogmsg-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Deploy API
  slug: open-netlify-deploy-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken deployedBranch API
  slug: open-netlify-deployedbranch-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken deployKey API
  slug: open-netlify-deploykey-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken devServer API
  slug: open-netlify-devserver-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken devServerHook API
  slug: open-netlify-devserverhook-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken dnsZone API
  slug: open-netlify-dnszone-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken environmentVariables API
  slug: open-netlify-environmentvariables-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken File API
  slug: open-netlify-file-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Form API
  slug: open-netlify-form-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Function API
  slug: open-netlify-function-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Hook API
  slug: open-netlify-hook-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken hookType API
  slug: open-netlify-hooktype-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Member API
  slug: open-netlify-member-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Metadata API
  slug: open-netlify-metadata-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken paymentMethod API
  slug: open-netlify-paymentmethod-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Purge API
  slug: open-netlify-purge-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken serviceInstance API
  slug: open-netlify-serviceinstance-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Services API
  slug: open-netlify-services-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Site API
  slug: open-netlify-site-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken sniCertificate API
  slug: open-netlify-snicertificate-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Snippet API
  slug: open-netlify-snippet-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken splitTest API
  slug: open-netlify-splittest-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Submission API
  slug: open-netlify-submission-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken Ticket API
  slug: open-netlify-ticket-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken User API
  slug: open-netlify-user-api
- collection_type: open
  name: Netlify Netlify's API documentation accessToken X-Internal API
  slug: open-netlify-x-internal-api
common:
- group: commercial
  href: https://artifacts.apis.io/netlify/finops/netlify-finops.yml
  title: ''
  type: FinOps
  url: finops/netlify-finops.yml
- group: other
  href: https://artifacts.apis.io/netlify/vendor-facets/netlify-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/netlify-vendor-facets.yml
- group: other
  href: https://artifacts.apis.io/netlify/overlays/netlify-accesstoken-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/netlify-accesstoken-overlay.yaml
- group: other
  href: https://artifacts.apis.io/netlify/overlays/netlify-accountmembership-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/netlify-accountmembership-overlay.yaml
- group: other
  href: https://artifacts.apis.io/netlify/overlays/netlify-auditlog-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/netlify-auditlog-overlay.yaml
- group: other
  href: https://artifacts.apis.io/netlify/overlays/netlify-devserver-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/netlify-devserver-overlay.yaml
- group: other
  href: https://artifacts.apis.io/netlify/overlays/netlify-environmentvariables-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/netlify-environmentvariables-overlay.yaml
- group: other
  href: https://artifacts.apis.io/netlify/overlays/netlify-paymentmethod-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/netlify-paymentmethod-overlay.yaml
- group: other
  href: https://artifacts.apis.io/netlify/overlays/netlify-splittest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/netlify-splittest-overlay.yaml
- group: other
  href: https://artifacts.apis.io/netlify/overlays/netlify-services-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/netlify-services-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.netlify.com/
- group: other
  href: https://artifacts.apis.io/netlify/capabilities/netlify-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/netlify-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/netlify/open-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/netlify/open-api/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/netlify/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/netlify/open-api/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/netlify/open-api/blob/master/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/netlify/overview
- group: agent
  href: https://artifacts.apis.io/netlify/agentic-access/netlify-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/netlify-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/netlify/security/netlify-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/netlify-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/netlify/security/netlify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netlify-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/netlify/authentication/netlify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/netlify-authentication.yml
- group: auth
  href: https://artifacts.apis.io/netlify/scopes/netlify-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/netlify-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netlify
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.netlify.com/legal/terms-of-use/
- group: company
  title: ''
  type: Blog
  url: https://netlify.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://netlify.com/changelog/
- group: operate
  title: ''
  type: Change Log RSS
  url: https://www.netlify.com/changelog/feed.xml
- group: operate
  title: ''
  type: Forums
  url: https://answers.netlify.com/
- group: operate
  title: ''
  type: Support
  url: https://www.netlify.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.netlify.com/privacy/
- group: start
  title: ''
  type: Signup
  url: https://app.netlify.com/signup
- group: start
  title: ''
  type: Portal
  url: https://app.netlify.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.netlifystatus.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.netlify.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.netlify.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.netlify.com/start/get-started-guide/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.netlify.com/api-and-cli-guides/api-guides/get-started-with-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netlify
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/netlify/open-api
- group: build
  title: ''
  type: CLI Repository
  url: https://github.com/netlify/cli
- group: docs
  title: ''
  type: CLI Documentation
  url: https://cli.netlify.com/
- group: build
  title: ''
  type: SDKs
  url: https://developers.netlify.com/sdk/
- group: company
  title: ''
  type: About
  url: https://www.netlify.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://www.netlify.com/contact/
- group: auth
  title: ''
  type: Security
  url: https://www.netlify.com/security/
- group: auth
  title: ''
  type: GDPR Policy
  url: https://www.netlify.com/gdpr-ccpa/
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/netlify
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/netlify/netlify-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.netlify.com/llms.txt
- group: build
  href: https://artifacts.apis.io/netlify/packages/netlify-packages.yml
  title: ''
  type: Packages
  url: packages/netlify-packages.yml
- group: build
  href: https://artifacts.apis.io/netlify/packages/netlify-packages.yml
  title: ''
  type: SDKs
  url: packages/netlify-packages.yml
- group: build
  href: https://artifacts.apis.io/netlify/cli/netlify-cli.yml
  title: ''
  type: CLI
  url: cli/netlify-cli.yml
- group: design
  href: https://artifacts.apis.io/netlify/components/netlify-components.yml
  title: ''
  type: Components
  url: components/netlify-components.yml
- group: agent
  href: https://artifacts.apis.io/netlify/well-known/netlify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/netlify-well-known.yml
- group: other
  href: https://artifacts.apis.io/netlify/well-known/netlify-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/netlify-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/netlify/mcp/netlify-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/netlify-mcp.yml
- group: build
  href: https://artifacts.apis.io/netlify/mcp/netlify-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/netlify-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/netlify/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/netlify/llms/netlify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/netlify-llms.txt
- group: design
  href: https://artifacts.apis.io/netlify/conventions/netlify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/netlify-conventions.yml
- group: design
  href: https://artifacts.apis.io/netlify/errors/netlify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/netlify-problem-types.yml
- group: design
  href: https://artifacts.apis.io/netlify/lifecycle/netlify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/netlify-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/netlify/changelog/netlify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/netlify-changelog.yml
- group: design
  href: https://artifacts.apis.io/netlify/conformance/netlify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/netlify-conformance.yml
- group: auth
  href: https://artifacts.apis.io/netlify/security/netlify-trust-center.yml
  title: ''
  type: Compliance
  url: security/netlify-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/netlify/security/netlify-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/netlify-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/netlify/security/netlify-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/netlify-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/netlify/data-model/netlify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/netlify-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/netlify/plans/netlify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/netlify-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/netlify/rate-limits/netlify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/netlify-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/netlify/asyncapi/netlify-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/netlify-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/netlify/vocabulary/netlify-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/netlify-vocabulary.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.netlify.com/
- group: docs
  title: ''
  type: APIReference
  url: https://open-api.netlify.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.netlify.com/signup
- group: operate
  title: ''
  type: HelpCenter
  url: https://answers.netlify.com/
- group: agent
  title: ''
  type: AgentSkillSource
  url: https://github.com/netlify/context-and-tools
created: '2023-11-14'
description: 'Netlify is a cloud platform for building, deploying and scaling modern web applications, with continuous deployment from Git, serverless and edge functions, a global CDN, forms, identity, Postgres storage and an image CDN. Its public REST API at https://api.netlify.com/api/v1 is described by an OpenAPI that Netlify maintains in the open at github.com/netlify/open-api and serves at open-api.netlify.com, covering deploys, sites, DNS, builds, forms, environment variables and split tests. Netlify also ships an unusually complete agent surface: an RFC 9727 API catalog at the domain root, an OAuth-gated remote MCP server, fifteen published Agent Skills, an llms.txt, and a Markdown twin of every documentation page.'
features:
- 'Free: 300 credits/mo, unlimited deploy previews, global CDN'
- 'Personal at $9/mo: 1,000 credits, smart secret detection'
- 'Pro at $20/mo: 3,000 credits, 3+ concurrent builds, private repos'
- 'Enterprise custom: custom credit allocation, 99.99% SLA, SSO/SCIM'
- REST API at api.netlify.com
- 'Open API: 500 req/min/token rate limit'
- 'Deploy creates: 3/min/site'
- 'Build concurrency: 1 Free/Personal, 3 Pro'
- Edge Functions (Deno runtime)
- Functions (Node serverless)
- Netlify Forms
- Netlify Identity / Auth
- Netlify Database (Postgres)
- Netlify Blobs (object store)
- Image CDN with transformations
- Webhooks for build events
finops:
- has_sources: true
  method: derived
  name: Netlify Finops
  primary_unit: team
  service_category: ''
  slug: netlify-finops
  template: false
graphqls:
- description: Netlify offered a GraphQL API through its Netlify Graph developer preview (built on the OneGraph platform, which Netlify acquired in 2021). The API was accessible at `https://graph.netlify.com/graphql
  name: Netlify GraphQL API
  slug: netlify-graphql
image: https://www.netlify.com/v3/img/components/logomark.png
json_schemas:
- name: accessToken
  property_count: 5
  slug: netlify-accesstoken
- name: accountAddMemberSetup
  property_count: 2
  slug: netlify-accountaddmembersetup
- name: accountMembership
  property_count: 16
  slug: netlify-accountmembership
- name: accountSetup
  property_count: 5
  slug: netlify-accountsetup
- name: accountType
  property_count: 8
  slug: netlify-accounttype
- name: accountUpdateMemberSetup
  property_count: 3
  slug: netlify-accountupdatemembersetup
- name: accountUpdateSetup
  property_count: 7
  slug: netlify-accountupdatesetup
- name: accountUsageCapability
  property_count: 2
  slug: netlify-accountusagecapability
- name: asset
  property_count: 12
  slug: netlify-asset
- name: assetForm
  property_count: 2
  slug: netlify-assetform
- name: assetPublicSignature
  property_count: 1
  slug: netlify-assetpublicsignature
- name: assetSignature
  property_count: 2
  slug: netlify-assetsignature
- name: auditLog
  property_count: 3
  slug: netlify-auditlog
- name: build
  property_count: 6
  slug: netlify-build
- name: buildHook
  property_count: 6
  slug: netlify-buildhook
- name: buildHookSetup
  property_count: 2
  slug: netlify-buildhooksetup
- name: buildLogMsg
  property_count: 3
  slug: netlify-buildlogmsg
- name: buildSetup
  property_count: 2
  slug: netlify-buildsetup
- name: buildStatus
  property_count: 5
  slug: netlify-buildstatus
- name: deploy
  property_count: 30
  slug: netlify-deploy
- name: deployedBranch
  property_count: 6
  slug: netlify-deployedbranch
- name: deployFiles
  property_count: 9
  slug: netlify-deployfiles
- name: deployKey
  property_count: 3
  slug: netlify-deploykey
- name: devServer
  property_count: 12
  slug: netlify-devserver
- name: devServerHook
  property_count: 7
  slug: netlify-devserverhook
- name: devServerHookSetup
  property_count: 3
  slug: netlify-devserverhooksetup
- name: dnsRecord
  property_count: 11
  slug: netlify-dnsrecord
- name: dnsRecordCreate
  property_count: 9
  slug: netlify-dnsrecordcreate
- name: dnsRecords
  property_count: 0
  slug: netlify-dnsrecords
- name: dnsZone
  property_count: 16
  slug: netlify-dnszone
- name: dnsZones
  property_count: 0
  slug: netlify-dnszones
- name: dnsZoneSetup
  property_count: 3
  slug: netlify-dnszonesetup
- name: envVar
  property_count: 6
  slug: netlify-envvar
- name: envVarUser
  property_count: 4
  slug: netlify-envvaruser
- name: envVarValue
  property_count: 4
  slug: netlify-envvarvalue
- name: error
  property_count: 2
  slug: netlify-error
- name: excludedFunctionRoute
  property_count: 3
  slug: netlify-excludedfunctionroute
- name: file
  property_count: 5
  slug: netlify-file
- name: form
  property_count: 7
  slug: netlify-form
- name: function
  property_count: 3
  slug: netlify-function
- name: functionConfig
  property_count: 7
  slug: netlify-functionconfig
- name: functionRoute
  property_count: 5
  slug: netlify-functionroute
- name: functionSchedule
  property_count: 2
  slug: netlify-functionschedule
- name: hook
  property_count: 8
  slug: netlify-hook
- name: hookType
  property_count: 3
  slug: netlify-hooktype
- name: member
  property_count: 5
  slug: netlify-member
- name: metadata
  property_count: 0
  slug: netlify-metadata
- name: paymentMethod
  property_count: 7
  slug: netlify-paymentmethod
- name: plugin
  property_count: 2
  slug: netlify-plugin
- name: pluginParams
  property_count: 1
  slug: netlify-pluginparams
- name: pluginRun
  property_count: 1
  slug: netlify-pluginrun
- name: pluginRunData
  property_count: 7
  slug: netlify-pluginrundata
- name: purge
  property_count: 3
  slug: netlify-purge
- name: repoInfo
  property_count: 15
  slug: netlify-repoinfo
- name: service
  property_count: 13
  slug: netlify-service
- name: serviceInstance
  property_count: 12
  slug: netlify-serviceinstance
- name: site
  property_count: 35
  slug: netlify-site
- name: siteFunction
  property_count: 6
  slug: netlify-sitefunction
- name: siteSetup
  property_count: 1
  slug: netlify-sitesetup
- name: sniCertificate
  property_count: 5
  slug: netlify-snicertificate
- name: snippet
  property_count: 7
  slug: netlify-snippet
- name: splitTest
  property_count: 9
  slug: netlify-splittest
- name: splitTests
  property_count: 0
  slug: netlify-splittests
- name: splitTestSetup
  property_count: 1
  slug: netlify-splittestsetup
- name: submission
  property_count: 12
  slug: netlify-submission
- name: ticket
  property_count: 4
  slug: netlify-ticket
- name: trafficRulesAggregateConfig
  property_count: 1
  slug: netlify-trafficrulesaggregateconfig
- name: trafficRulesConfig
  property_count: 1
  slug: netlify-trafficrulesconfig
- name: trafficRulesRateLimitConfig
  property_count: 3
  slug: netlify-trafficrulesratelimitconfig
- name: user
  property_count: 11
  slug: netlify-user
json_structures:
- name: Netlify Structure
  property_count: 0
  slug: netlify-structure
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: 'Netlify ships an official MCP server in BOTH deployments. A hosted remote server answers Streamable HTTP at https://netlify-mcp.netlify.app/mcp behind OAuth, and the identical build runs locally over '
  name: Netlify MCP Server
  slug: netlify-mcp-server
modified: '2026-08-27'
name: Netlify
nav: Providers
network: true
overview: 'Netlify publishes 41 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Type API, Asset API, Asset Public Signature API, and 38 more. Tagged areas include CDN, Cloud, Continuous Deployment, Developer Tools, and Edge Computing.


  The Netlify catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Netlify''s developer surface includes authentication, engineering blog, changelog, support, signup flow, developer portal, pricing, and 71 more developer resources.'
plans:
- name: Netlify Plans Pricing
  plan_count: 11
  slug: netlify-plans-pricing
- name: Netlify Price Estimates
  plan_count: 0
  slug: netlify-price-estimates
random_paper: 19
rate_limits:
- limit_count: 5
  name: Netlify Rate Limits
  slug: netlify-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Netlify — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: netlify-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Netlify — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: netlify-jsonschema-spectral-rules
scopes:
- name: Netlify Scopes
  scope_count: 0
  slug: netlify-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 72.8
  coverage:
    artifact_dirs: 39
    catalog_earned: 73.0
    catalog_earned_first_party: 24.0
    catalog_gap: 42.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 86.8
    contract_governance: 31.8
    contract_quality: 55.5
    developer_ergonomics: 79.8
    discoverability: 75.0
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  open_source:
    applies: true
    score: 65.0
  previous_composite: 72.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 41
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/netlify/netlify-2026-06-20T190259.png
security:
- kind: authentication
  name: Netlify Authentication
  slug: netlify-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Netlify Domain Security
  slug: netlify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Netlify Vulnerability Disclosure
  slug: netlify-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Netlify Trust Center
  slug: netlify-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, PCI DSS, HIPAA, GDPR
skill_count: 15
skills:
- name: netlify-access-control
  slug: netlify-access-control
- name: netlify-agent-runner
  slug: netlify-agent-runner
- name: netlify-ai-gateway
  slug: netlify-ai-gateway
- name: netlify-blobs
  slug: netlify-blobs
- name: netlify-caching
  slug: netlify-caching
- name: netlify-config
  slug: netlify-config
- name: netlify-database
  slug: netlify-database
- name: netlify-deploy
  slug: netlify-deploy
- name: netlify-edge-functions
  slug: netlify-edge-functions
- name: netlify-forms
  slug: netlify-forms
- name: netlify-frameworks
  slug: netlify-frameworks
- name: netlify-functions
  slug: netlify-functions
- name: netlify-identity
  slug: netlify-identity
- name: netlify-image-cdn
  slug: netlify-image-cdn
- name: netlify-mcp-servers
  slug: netlify-mcp-servers
slug: netlify
tags:
- CDN
- Cloud
- Continuous Deployment
- Developer Tools
- Edge Computing
- JAMstack
- Serverless
- Serverless Functions
- Static Sites
- Web Hosting
- Websites
- Netlify
website: https://www.netlify.com/
---
