---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    mcp_server: templated
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.6
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 284
  human_in_the_loop: 24
  name: Acquia Agentic Access
  operation_count: 638
  slug: acquia-agentic-access
  summary_line: 638 operations · 284 acting · 24 human-in-the-loop
api_count: 20
apis:
- description: Acquia Cloud Site Factory API is a powerful tool that allows developers to manage, customize, and automate various aspects of their websites and digital experiences. With this API, users can programma
  name: Acquia Cloud Site Factory API
  slug: acquia-cloud-site-factory-api
- description: The Acquia Content Hub API is a powerful tool that allows users to easily distribute and share content across multiple websites and digital channels. By leveraging this API, content managers can autom
  name: Acquia Content Hub API
  slug: acquia-content-hub-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Account API from Acquia — 23 operation(s) for account.
  name: Acquia Account API
  phrasing_intents:
  - id: getAccount
    intent: Get my account details
    question: What does Acquia have on file for my user account?
  - id: getAccountApplicationHasPermission
    intent: Check if I have a permission on an application
    question: Am I allowed to perform a specific action on an application?
  - id: getAccountApplicationIsAdministrator
    intent: Check if I administer an application
    question: Am I an administrator of this application?
  - id: getAccountApplicationIsOwner
    intent: Check if I own an application
    question: Am I the owner of this application?
  - id: postAccountApplicationMarkRecent
    intent: Mark an application as recently viewed
    question: How do I add an app to my recently viewed list?
  - id: postAccountApplicationStar
    intent: Star an application
    question: How do I favorite an application so it's easy to find?
  - id: postAccountApplicationUnstar
    intent: Unstar an application
    question: Can I remove an app from my favorites?
  - id: getAccountDrushAliasesDownload
    intent: Download my Drush aliases
    question: Where can I download Drush aliases for all my sites?
  phrasing_ops: 27
  slug: acquia-account-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Agreements API from Acquia — 5 operation(s) for agreements.
  name: Acquia Agreements API
  phrasing_intents:
  - id: getAgreements
    intent: List legal agreements awaiting my response
    question: Which Acquia legal agreements have I been invited to accept or decline?
  - id: getAgreement
    intent: View the details of one legal agreement
    question: What does a specific agreement I was invited to actually say?
  - id: postAcceptAgreement
    intent: Accept a legal agreement
    question: How do I accept a legal agreement I've been invited to?
  - id: postDeclineAgreement
    intent: Decline a legal agreement
    question: What happens if I want to reject an agreement I was invited to?
  - id: getInvitees
    intent: List users invited to act on an agreement
    question: Who else has been invited to accept or decline this agreement?
  phrasing_ops: 5
  slug: acquia-agreements-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Application Performance Monitoring Services API from Acquia — 4 operation(s) for application performance monitoring services.
  name: Acquia Application Performance Monitoring Services API
  phrasing_intents:
  - id: getEnvironmentsApmSetting
    intent: See APM tools configured on an environment
    question: Which application performance monitoring tools are hooked up to this environment?
  - id: putEnvironmentsApmSetting
    intent: Configure an APM tool on an environment
    question: How do I switch on a performance monitoring tool for a single environment?
  - id: getSubscriptionApmTypes
    intent: List APM services available to a subscription
    question: What performance monitoring services come with my subscription?
  - id: getSubscriptionApmType
    intent: View one APM service type on a subscription
    question: What are the details of a specific APM service on my subscription?
  - id: postSubscriptionApmOptIn
    intent: Opt a subscription into New Relic Pro APM
    question: Can I enable a New Relic Pro license for every application on a subscription at once?
  phrasing_ops: 5
  slug: acquia-application-performance-monitoring-services-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Applications API from Acquia — 36 operation(s) for applications.
  name: Acquia Applications API
  phrasing_intents:
  - id: getApplications
    intent: List the applications I can access
    question: Which Acquia applications do I have access to through my teams?
  - id: getApplicationByUuid
    intent: Get details of one application
    question: What details can I see about a single hosted application?
  - id: putApplicationByUuid
    intent: Rename an application
    question: Can I change the display name of an existing application?
  - id: getArtifactsByApplicationUuid
    intent: List build artifacts for a Node.js application
    question: Where can I see the build artifacts produced for my Node.js application?
  - id: getArtifactByApplicationUuidAndId
    intent: Get one build artifact of an application
    question: What information is kept about a single build artifact?
  - id: getCodeByApplicationUuid
    intent: List an application's branches and release tags
    question: Which git branches and release tags exist in my application's repository?
  - id: getCodeStudioProject
    intent: Get an application's Code Studio project
    question: Does my application already have a Code Studio project set up?
  - id: postCodeStudioProject
    intent: Create a Code Studio project for an application
    question: How do I set up Code Studio for one of my applications?
  phrasing_ops: 47
  slug: acquia-applications-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Cloud IDE API from Acquia — 1 operation(s) for cloud ide.
  name: Acquia Cloud IDE API
  phrasing_intents:
  - id: getIde
    intent: Get Cloud IDE details
    question: What's the status and URL of a specific Cloud IDE?
  - id: deleteIde
    intent: De-provision a Cloud IDE
    question: How do I delete a Cloud IDE I'm done with?
  phrasing_ops: 2
  slug: acquia-cloud-ide-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Codebases API from Acquia — 8 operation(s) for codebases.
  name: Acquia Codebases API
  phrasing_intents:
  - id: api_codebases_codebaseIdbulk-code-switch_get_collection
    intent: List past bulk code switches on a codebase
    question: What bulk code switches have already been run against a codebase?
  - id: create_bulk_code_switch_resource
    intent: Switch many environments to one git reference
    question: How do I move several environments to the same branch or tag in one go?
  - id: get_bulk_code_switch_resource
    intent: Check on one bulk code switch
    question: Did a particular bulk code switch finish, and which targets did it touch?
  - id: api_applications_applicationIdcodebase_get
    intent: Find the codebase linked to an application
    question: Which codebase is an application built from?
  - id: api_codebases_get_collection
    intent: List all codebases I can access
    question: What codebases do I have access to across Acquia?
  - id: get_codebase_by_id
    intent: View details of one codebase
    question: What are the label, description and details of a specific codebase?
  - id: api_codebases_codebaseId_put
    intent: Rename or redescribe a codebase
    question: How do I change the label shown for a codebase?
  - id: api_codebases_codebaseId_delete
    intent: Delete a codebase
    question: Can I permanently remove a codebase I no longer use?
  phrasing_ops: 12
  slug: acquia-codebases-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Current system health API from Acquia — 1 operation(s) for current system health.
  name: Acquia Current system health API
  phrasing_intents:
  - id: getSystemHealthStatus
    intent: Check the current system health status
    question: Is the Acquia Cloud API healthy right now?
  phrasing_ops: 1
  slug: acquia-current-system-health-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Distributions API from Acquia — 2 operation(s) for distributions.
  name: Acquia Distributions API
  phrasing_intents:
  - id: getDistributions
    intent: List installable Drupal distributions
    question: Which Drupal distributions can I install in an Acquia Cloud environment?
  - id: getDistributionByName
    intent: View details of one Drupal distribution
    question: What are the details of a specific Drupal distribution by name?
  phrasing_ops: 2
  slug: acquia-distributions-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Email API from Acquia — 1 operation(s) for email.
  name: Acquia Email API
  phrasing_intents:
  - id: getEmailStatus
    intent: Get Platform Email status for an environment
    question: Is Platform Email turned on for my environment?
  phrasing_ops: 1
  slug: acquia-email-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Environments API from Acquia — 73 operation(s) for environments.
  name: Acquia Environments API
  phrasing_intents:
  - id: getEnvironment
    intent: View details of one environment
    question: What are the settings and status of a specific Acquia environment?
  - id: putEnvironment
    intent: Change PHP and runtime settings on an environment
    question: How do I raise the PHP memory limit on an environment?
  - id: deleteEnvironment
    intent: Delete a CD environment
    question: Can I tear down a continuous delivery environment I no longer need?
  - id: optionsEnvironment
    intent: See configurable options for an environment
    question: What configuration options are allowed for this environment?
  - id: postEnvironmentsClearCaches
    intent: Clear Varnish and CDN caches for several domains
    question: Can I purge both Varnish and Platform CDN caches for a batch of domains at once?
  - id: postChangeEnvironmentLabel
    intent: Rename an environment's label
    question: How do I change the display label of an environment?
  - id: postDeployArtifact
    intent: Deploy a build artifact to an environment
    question: Can I deploy a specific build artifact to an environment?
  - id: getOperatingSystems
    intent: List operating systems for an environment
    question: Which operating systems can this environment run on?
  phrasing_ops: 102
  slug: acquia-environments-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Identity Providers API from Acquia — 4 operation(s) for identity providers.
  name: Acquia Identity Providers API
  phrasing_intents:
  - id: getIdentityProviders
    intent: List my identity providers
    question: Which SAML identity providers are set up for single sign-on?
  - id: getIdentityProvider
    intent: Get an identity provider
    question: What SSO URL and entity ID does an identity provider use?
  - id: putIdentityProvider
    intent: Update an identity provider
    question: How do I rotate the signing certificate on my identity provider?
  - id: deleteIdentityProvider
    intent: Delete an identity provider
    question: Can I delete an identity provider we stopped using?
  - id: postEnableIdentityProvider
    intent: Enable an identity provider
    question: How do I turn on single sign-on through an identity provider?
  - id: postDisableIdentityProvider
    intent: Disable an identity provider
    question: Can I temporarily turn off an identity provider without deleting it?
  phrasing_ops: 6
  slug: acquia-identity-providers-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Invite API from Acquia — 4 operation(s) for invite.
  name: Acquia Invite API
  phrasing_intents:
  - id: getInviteByToken
    intent: Get details of an invitation
    question: Who sent me this invitation and what does it grant?
  - id: postInviteCancel
    intent: Cancel an invitation
    question: How do I withdraw an invitation I sent by mistake?
  - id: postInviteAcceptByToken
    intent: Accept an invitation
    question: How do I accept an invitation to join a team or organization?
  - id: postInviteDecline
    intent: Decline an invitation
    question: Can I turn down an invitation I received?
  - id: postInviteResend
    intent: Resend an invitation
    question: The invitee lost the email; can I send the invite again?
  phrasing_ops: 5
  slug: acquia-invite-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Messages API from Acquia — 2 operation(s) for messages.
  name: Acquia Messages API
  phrasing_intents:
  - id: postDismissMessage
    intent: Dismiss an in-product message
    question: How do I get rid of a platform message I've already read?
  - id: getMessageFollow
    intent: Follow a message's link
    question: Where does the link in a platform message lead?
  phrasing_ops: 2
  slug: acquia-messages-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Notifications API from Acquia — 1 operation(s) for notifications.
  name: Acquia Notifications API
  phrasing_intents:
  - id: getNotificationByUuid
    intent: Look up a single notification
    question: What is the status of a specific Acquia notification?
  phrasing_ops: 1
  slug: acquia-notifications-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Options API from Acquia — 6 operation(s) for options.
  name: Acquia Options API
  phrasing_intents:
  - id: getOptions
    intent: Browse the available option groups
    question: What option groups can I look up in the Cloud API?
  - id: getCdeSizes
    intent: List continuous delivery environment sizes
    question: What sizes can a CD environment be created in?
  - id: getLogForwarding
    intent: Browse log forwarding option groups
    question: Where do I find the log forwarding option lists?
  - id: getLogForwardingSources
    intent: List log forwarding sources
    question: Which log types can I forward from my environments?
  - id: getLogForwardingConsumers
    intent: List log forwarding destinations
    question: Which logging services can I forward logs to?
  - id: getColors
    intent: List available tag colors
    question: What colors can I use for application tags?
  phrasing_ops: 6
  slug: acquia-options-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Organizations API from Acquia — 18 operation(s) for organizations.
  name: Acquia Organizations API
  phrasing_intents:
  - id: getOrganizations
    intent: List the organizations I belong to
    question: Which Acquia organizations is my account part of?
  - id: getOrganizationByUuid
    intent: View details of one organization
    question: Who owns a specific organization and what are its details?
  - id: putOrganization
    intent: Rename an organization
    question: How do I change the name of my organization?
  - id: deleteOrganization
    intent: Delete an organization
    question: Can I permanently delete an organization I no longer need?
  - id: postChangeOrganizationOwner
    intent: Transfer ownership of an organization
    question: How do I hand ownership of my organization to another user?
  - id: postLeaveOrganization
    intent: Leave an organization
    question: Can I remove myself from an organization I no longer work with?
  - id: getOrganizationAdmins
    intent: List an organization's administrators
    question: Who are the administrators of my organization?
  - id: getOrganizationAdmin
    intent: View one organization administrator
    question: What does the profile of a specific organization admin look like?
  phrasing_ops: 27
  slug: acquia-organizations-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: Private Network Service API
  name: Acquia Private Networks API
  phrasing_intents:
  - id: createPrivateNetwork
    intent: Create a private network
    question: How do I set up a new private network for my subscription in a given region?
  - id: getPrivateNetwork
    intent: Get a private network
    question: What is configured on a specific private network?
  - id: updatePrivateNetwork
    intent: Update a private network's label or description
    question: Can I change the label or description of an existing private network?
  - id: deletePrivateNetwork
    intent: Delete a private network
    question: How do I tear down a private network I no longer need?
  - id: getPrivateNetworksBySubscription
    intent: List private networks in a subscription
    question: Which private networks exist under my subscription?
  - id: addVpnToPrivateNetwork
    intent: Add a VPN to a private network
    question: How do I connect my office network to a private network over VPN?
  - id: getAllVpnsFromPrivateNetwork
    intent: List VPNs on a private network
    question: Which VPN connections are attached to my private network?
  - id: getVpnFromPrivateNetwork
    intent: Get one VPN on a private network
    question: What are the tunnel settings of a particular VPN?
  phrasing_ops: 20
  slug: acquia-private-networks-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Subscriptions API from Acquia — 22 operation(s) for subscriptions.
  name: Acquia Subscriptions API
  phrasing_intents:
  - id: getSubscriptions
    intent: List my subscriptions
    question: Which Acquia subscriptions do I belong to?
  - id: getSubscription
    intent: Get details of a subscription
    question: What details are stored on a single subscription?
  - id: putSubscription
    intent: Rename a subscription
    question: Can I change the name of a subscription?
  - id: getSubscriptionApplications
    intent: List applications in a subscription
    question: Which applications are part of this subscription?
  - id: getCodeStudioSubscriptionMetadata
    intent: Get Code Studio metadata for a subscription
    question: Is Code Studio provisioned on my subscription?
  - id: optionsCodeStudio
    intent: Show Code Studio options for a subscription
    question: What Code Studio options are available on my subscription?
  - id: postEnableCodeStudio
    intent: Enable Code Studio on a subscription
    question: How do I turn on Code Studio for my whole subscription?
  - id: getCodeStudioApplications
    intent: List Code Studio-enabled applications
    question: Which of my subscription's applications use Code Studio?
  phrasing_ops: 31
  slug: acquia-subscriptions-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: The Teams and Permissions API from Acquia — 10 operation(s) for teams and permissions.
  name: Acquia Teams and Permissions API
  phrasing_intents:
  - id: getPermissions
    intent: List all available permissions
    question: What permissions exist in the Acquia Cloud Platform?
  - id: getRole
    intent: Get details of a role
    question: Which permissions does a particular role grant?
  - id: deleteRole
    intent: Delete a role
    question: How do I delete a custom role we no longer use?
  - id: putRoleByUuid
    intent: Update a role
    question: Can I change which permissions a role grants?
  - id: getTeams
    intent: List the teams I can access
    question: Which teams do I have access to?
  - id: getTeam
    intent: Get details of a team
    question: What details are stored about a specific team?
  - id: putTeamsName
    intent: Rename a team
    question: Can I change a team's name?
  - id: deleteTeam
    intent: Delete a team
    question: How do I delete a team entirely?
  phrasing_ops: 17
  slug: acquia-teams-and-permissions-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: OAuth 2.0 token and authorization endpoints.
  name: Acquia Authentication API
  phrasing_intents:
  - id: issueToken
    intent: Get an access token
    question: How do I get an access token for the Acquia Cloud API with my client credentials?
  - id: authorize
    intent: Start the OAuth login and consent flow
    question: Where do I send a user so they can log in and approve my app's access?
  phrasing_ops: 2
  slug: acquia-authentication-api
- baseURL: https://cloud.acquia.com/api
  baseurl_source: declared
  description: JSON:API resource endpoints for reading and writing entries.
  name: Acquia Content API
  phrasing_intents:
  - id: apiRoot
    intent: Discover the content types a site exposes
    question: Which content resource types can I query on my Drupal site's JSON:API?
  - id: listEntries
    intent: List content entries of one bundle
    question: How do I fetch all the articles on my site through the content API?
  - id: createEntry
    intent: Create a content entry
    question: Can I publish a new article to my site through the content API?
  - id: getEntry
    intent: Get one content entry by UUID
    question: How can I read a single piece of content by its UUID?
  - id: updateEntry
    intent: Update an existing content entry
    question: How do I edit the title or body of an article that's already published?
  - id: deleteEntry
    intent: Delete a content entry
    question: Can I remove a piece of content from my site through the API?
  - id: getRelated
    intent: Fetch the entries a relationship field points to
    question: How do I get the full tags or author records an article references?
  - id: getRelationship
    intent: Read a relationship's linkage identifiers
    question: Can I see just the type and ID an entry points to, without the target's attributes?
  phrasing_ops: 8
  slug: acquia-content-api
artifact_total: 127
asyncapis:
- description: ''
  name: Acquia Source Cms Webhooks
  slug: acquia-source-cms-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Acquia Cloud API Account API
  slug: open-acquia-account-api
- collection_type: open
  name: Acquia Cloud API Account Agreements API
  slug: open-acquia-agreements-api
- collection_type: open
  name: Acquia Cloud API Account Application Performance Monitoring Services API
  slug: open-acquia-application-performance-monitoring-services-api
- collection_type: open
  name: Acquia Cloud API Account Applications API
  slug: open-acquia-applications-api
- collection_type: open
  name: Acquia Cloud API - Account
  slug: open-acquia-cloud-account
- collection_type: open
  name: Acquia Cloud API - Agreements
  slug: open-acquia-cloud-agreements
- collection_type: open
  name: Acquia Cloud API - Application Performance Monitoring Services
  slug: open-acquia-cloud-application-performance-monitoring-services
- collection_type: open
  name: Acquia Cloud API - Applications
  slug: open-acquia-cloud-applications
- collection_type: open
  name: Acquia Cloud API - Cloud IDE
  slug: open-acquia-cloud-cloud-ide
- collection_type: open
  name: Acquia Cloud API - Codebases
  slug: open-acquia-cloud-codebases
- collection_type: open
  name: Acquia Cloud API - Current system health
  slug: open-acquia-cloud-current-system-health
- collection_type: open
  name: Acquia Cloud API - Distributions
  slug: open-acquia-cloud-distributions
- collection_type: open
  name: Acquia Cloud API - Email
  slug: open-acquia-cloud-email
- collection_type: open
  name: Acquia Cloud API - Environments
  slug: open-acquia-cloud-environments
- collection_type: open
  name: Acquia Cloud API Account Cloud IDE API
  slug: open-acquia-cloud-ide-api
- collection_type: open
  name: Acquia Cloud API - Identity Providers
  slug: open-acquia-cloud-identity-providers
- collection_type: open
  name: Acquia Cloud API - Invite
  slug: open-acquia-cloud-invite
- collection_type: open
  name: Acquia Cloud API - Messages
  slug: open-acquia-cloud-messages
- collection_type: open
  name: Acquia Cloud API - Notifications
  slug: open-acquia-cloud-notifications
- collection_type: open
  name: Acquia Cloud API Documentation
  slug: open-acquia-cloud-openapi-full
- collection_type: open
  name: Acquia Cloud API - Options
  slug: open-acquia-cloud-options
- collection_type: open
  name: Acquia Cloud API - Organizations
  slug: open-acquia-cloud-organizations
- collection_type: open
  name: Acquia Cloud API - Private Networks
  slug: open-acquia-cloud-private-networks
- collection_type: open
  name: Acquia Cloud API - Subscriptions
  slug: open-acquia-cloud-subscriptions
- collection_type: open
  name: Acquia Cloud API - Teams and Permissions
  slug: open-acquia-cloud-teams-and-permissions
- collection_type: open
  name: Acquia Cloud API Account Codebases API
  slug: open-acquia-codebases-api
- collection_type: open
  name: Acquia Cloud API Account Current system health API
  slug: open-acquia-current-system-health-api
- collection_type: open
  name: Acquia Cloud API Account Distributions API
  slug: open-acquia-distributions-api
- collection_type: open
  name: Acquia Cloud API Account Email API
  slug: open-acquia-email-api
- collection_type: open
  name: Acquia Cloud API Account Environments API
  slug: open-acquia-environments-api
- collection_type: open
  name: Acquia Cloud API Account Identity Providers API
  slug: open-acquia-identity-providers-api
- collection_type: open
  name: Acquia Cloud API Account Invite API
  slug: open-acquia-invite-api
- collection_type: open
  name: Acquia Cloud API Account Messages API
  slug: open-acquia-messages-api
- collection_type: open
  name: Acquia Cloud API Account Notifications API
  slug: open-acquia-notifications-api
- collection_type: open
  name: Acquia Cloud API Account Options API
  slug: open-acquia-options-api
- collection_type: open
  name: Acquia Cloud API Account Organizations API
  slug: open-acquia-organizations-api
- collection_type: open
  name: Acquia Cloud API Account Private Networks API
  slug: open-acquia-private-networks-api
- collection_type: open
  name: Acquia Cloud API Account Subscriptions API
  slug: open-acquia-subscriptions-api
- collection_type: open
  name: Acquia Cloud API Account Teams and Permissions API
  slug: open-acquia-teams-and-permissions-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/capabilities/acquia-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/acquia-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/overlays/acquia-content-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/acquia-content-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.acquia.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/agentic-access/acquia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/acquia-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/security/acquia-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/acquia-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/security/acquia-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/acquia-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/security/acquia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acquia-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/authentication/acquia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/acquia-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/scopes/acquia-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/acquia-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acquia
- group: company
  title: ''
  type: Partners
  url: https://www.acquia.com/partners
- group: company
  title: ''
  type: Blog
  url: https://www.acquia.com/blog
- group: learn
  title: ''
  type: Webinars
  url: https://www.acquia.com/events/online
- group: auth
  title: ''
  type: Certifications
  url: https://www.acquia.com/support/acquia-training-certification
- group: start
  title: ''
  type: Portal
  url: https://dev.acquia.com/
- group: operate
  title: ''
  type: Support
  url: https://docs.acquia.com/service-offerings/support/support-users-guide#contacting-acquia-support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.acquia.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acquia
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/rules/acquia-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/vocabulary/acquia-vocabulary.yaml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acquia.com/about-us/legal
- group: start
  title: ''
  type: Signup
  url: https://accounts.acquia.com/sign-up
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/packages/acquia-packages.yml
  title: ''
  type: Packages
  url: packages/acquia-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/packages/acquia-packages.yml
  title: ''
  type: SDKs
  url: packages/acquia-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/cli/acquia-cli.yml
  title: ''
  type: CLI
  url: cli/acquia-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/well-known/acquia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/acquia-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/well-known/acquia-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/acquia-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/security/acquia-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/acquia-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/security/acquia-trust-center.yml
  title: ''
  type: Compliance
  url: security/acquia-trust-center.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/mcp/acquia-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/acquia-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/mcp/acquia-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/acquia-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/llms/acquia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acquia-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/conformance/acquia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acquia-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/errors/acquia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/acquia-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/lifecycle/acquia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/acquia-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/lifecycle/acquia-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/acquia-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/conventions/acquia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/acquia-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/changelog/acquia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/acquia-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/components/acquia-components.yml
  title: ''
  type: Components
  url: components/acquia-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/data-model/acquia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/acquia-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/asyncapi/acquia-source-cms-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/acquia-source-cms-webhooks.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/plans/acquia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/acquia-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/rate-limits/acquia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/acquia-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.acquia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://cloudapi-docs.acquia.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.acquia.com/start-here/choose-your-backend
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acquia.com/pricing
- group: operate
  title: ''
  type: Roadmap
  url: https://www.acquia.com/product/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acquia.com/about-us/legal/privacy-policy
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.acquia.com/
created: '2025-02-17'
description: Acquia is a leading provider of digital experience management solutions for organizations looking to enhance their online presence. They offer a range of services, including cloud hosting, digital asset management, and content management, to help businesses create, manage, and optimize their websites and digital experiences.
examples:
- key_count: 10
  name: Acquia Cloud Agreement Example
  slug: acquia-cloud-agreement-example
- key_count: 11
  name: Acquia Cloud Application Example
  slug: acquia-cloud-application-example
- key_count: 22
  name: Acquia Cloud Environment Example
  slug: acquia-cloud-environment-example
- key_count: 2
  name: Acquia Cloud Error Example
  slug: acquia-cloud-error-example
- key_count: 5
  name: Acquia Cloud Ide Example
  slug: acquia-cloud-ide-example
- key_count: 11
  name: Acquia Cloud Invite Example
  slug: acquia-cloud-invite-example
- key_count: 14
  name: Acquia Cloud Notification Example
  slug: acquia-cloud-notification-example
- key_count: 12
  name: Acquia Cloud Organization Example
  slug: acquia-cloud-organization-example
- key_count: 6
  name: Acquia Cloud Ssh Key Example
  slug: acquia-cloud-ssh-key-example
- key_count: 12
  name: Acquia Cloud Subscription Example
  slug: acquia-cloud-subscription-example
- key_count: 6
  name: Acquia Cloud Team Example
  slug: acquia-cloud-team-example
- key_count: 20
  name: Acquia Cloud User Example
  slug: acquia-cloud-user-example
- key_count: 11
  name: Acquia Cloud Ux Message Example
  slug: acquia-cloud-ux-message-example
features:
- description: Managed Drupal hosting on Acquia Cloud with auto-scaling, CDN, and DDoS protection.
  name: Cloud Hosting
- description: Programmatic management of Drupal applications, environments, and deployments via Cloud API.
  name: Application Management
- description: Acquia Cloud Site Factory for managing hundreds of Drupal sites from a centralized platform.
  name: Multi-Site Factory
- description: Acquia Content Hub for distributing and synchronizing Drupal content across multiple sites.
  name: Content Syndication
- description: Browser-based Cloud IDE for remote Drupal development with pre-configured environments.
  name: Cloud IDE
- description: Secure API access via OAuth2 authorization code flow with scoped tokens.
  name: OAuth2 Authentication
finops:
- name: Acquia Finops
  service_category: Digital Experience Platform
  slug: acquia-finops
image: /assets/icons/acquia.png
json_schemas:
- name: Agreement
  property_count: 10
  slug: acquia-cloud-agreement
- name: Application
  property_count: 11
  slug: acquia-cloud-application
- name: Environment
  property_count: 22
  slug: acquia-cloud-environment
- name: Error
  property_count: 2
  slug: acquia-cloud-error
- name: Ide
  property_count: 5
  slug: acquia-cloud-ide
- name: Invite
  property_count: 11
  slug: acquia-cloud-invite
- name: Notification
  property_count: 14
  slug: acquia-cloud-notification
- name: Organization
  property_count: 12
  slug: acquia-cloud-organization
- name: Ssh Key
  property_count: 6
  slug: acquia-cloud-ssh-key
- name: Subscription
  property_count: 12
  slug: acquia-cloud-subscription
- name: Team
  property_count: 6
  slug: acquia-cloud-team
- name: User
  property_count: 20
  slug: acquia-cloud-user
- name: Ux Message
  property_count: 11
  slug: acquia-cloud-ux-message
json_structures:
- name: Acquia Cloud Agreement Structure
  property_count: 10
  slug: acquia-cloud-agreement-structure
- name: Acquia Cloud Application Structure
  property_count: 11
  slug: acquia-cloud-application-structure
- name: Acquia Cloud Environment Structure
  property_count: 22
  slug: acquia-cloud-environment-structure
- name: Acquia Cloud Error Structure
  property_count: 2
  slug: acquia-cloud-error-structure
- name: Acquia Cloud Ide Structure
  property_count: 5
  slug: acquia-cloud-ide-structure
- name: Acquia Cloud Invite Structure
  property_count: 11
  slug: acquia-cloud-invite-structure
- name: Acquia Cloud Notification Structure
  property_count: 14
  slug: acquia-cloud-notification-structure
- name: Acquia Cloud Organization Structure
  property_count: 12
  slug: acquia-cloud-organization-structure
- name: Acquia Cloud Ssh Key Structure
  property_count: 6
  slug: acquia-cloud-ssh-key-structure
- name: Acquia Cloud Subscription Structure
  property_count: 12
  slug: acquia-cloud-subscription-structure
- name: Acquia Cloud Team Structure
  property_count: 6
  slug: acquia-cloud-team-structure
- name: Acquia Cloud User Structure
  property_count: 20
  slug: acquia-cloud-user-structure
- name: Acquia Cloud Ux Message Structure
  property_count: 11
  slug: acquia-cloud-ux-message-structure
jsonld:
- class_count: 17
  name: Acquia Context
  property_count: 73
  slug: acquia-context
layout: provider
mcp_servers:
- description: Acquia ships a first-party MCP server with Source CMS. Every Source CMS site exposes it at its own `/mcp` path, so the endpoint is per-tenant rather than a single shared Acquia-hosted URL. The catalog
  name: Acquia Source MCP
  slug: acquia-source-mcp
modified: '2026-08-30'
name: Acquia
nav: Providers
network: true
overview: 'Acquia publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Account API, Agreements API, Application Performance Monitoring Services API, and 20 more. Tagged areas include Content, Experience, Drupal, DXP, and CMS.


  The Acquia catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Acquia''s developer surface includes authentication, engineering blog, developer portal, support, signup flow, CLI, changelog, and 44 more developer resources.'
plans:
- name: Acquia Plans Pricing
  plan_count: 8
  slug: acquia-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Acquia Rate Limits
  slug: acquia-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Acquia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: acquia-jsonschema-spectral-rules
- effective_rule_count: 78
  extends:
  - spectral:oas
  name: Acquia API Rules
  rule_count: 37
  severity_counts:
    error: 14
    hint: 0
    info: 9
    warn: 14
  slug: acquia-spectral-rules
scopes:
- name: Acquia Scopes
  scope_count: 1
  slug: acquia-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: exemplar
  composite: 76.8
  coverage:
    artifact_dirs: 33
    catalog_earned: 70.0
    catalog_earned_first_party: 12.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 62.4
    developer_ergonomics: 73.8
    discoverability: 65.0
    operational_transparency: 65.8
  previous_composite: 76.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: first-party
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
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/acquia/refs/heads/main/screenshots/acquia-2026-06-20T163944.png
security:
- kind: authentication
  name: Acquia Authentication
  slug: acquia-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Acquia Domain Security
  slug: acquia-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Acquia Vulnerability Disclosure
  slug: acquia-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Acquia Trust Center
  slug: acquia-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: acquia
tags:
- Content
- Experience
- Drupal
- DXP
- CMS
- Digital Asset Management
- Cloud Hosting
- Headless
- Content Management
- Headless CMS
use_cases:
- description: Integrate Acquia Cloud API into CI/CD pipelines for automated code deployment and cache clearing.
  name: Automated Deployment Pipelines
- description: Manage dev, staging, and production Drupal environments programmatically.
  name: Multi-Environment Management
- description: Automate team provisioning, SSH key management, and organizational access control.
  name: Platform Administration
- description: Use Content Hub API to distribute content across a network of Drupal sites.
  name: Content Distribution
- description: Manage decoupled Drupal applications with Next.js or other frontend frameworks via Acquia APIs.
  name: Headless Drupal
website: https://www.acquia.com/
---
