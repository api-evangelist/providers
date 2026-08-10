---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Pipedream Agentic Access
  operation_count: 62
  slug: pipedream-agentic-access
  summary_line: 62 operations · 31 acting
api_count: 16
apis:
- description: The Accounts API from Pipedream — 4 operation(s) for accounts.
  name: Pipedream Accounts API
  slug: pipedream-accounts-api
- description: The Actions API from Pipedream — 5 operation(s) for actions.
  name: Pipedream Actions API
  slug: pipedream-actions-api
- description: The App Categories API from Pipedream — 2 operation(s) for app categories.
  name: Pipedream App Categories API
  slug: pipedream-app-categories-api
- description: The Apps API from Pipedream — 6 operation(s) for apps.
  name: Pipedream Apps API
  slug: pipedream-apps-api
- description: The Components API from Pipedream — 4 operation(s) for components.
  name: Pipedream Components API
  slug: pipedream-components-api
- description: The Deployed Triggers API from Pipedream — 7 operation(s) for deployed triggers.
  name: Pipedream Deployed Triggers API
  slug: pipedream-deployed-triggers-api
- description: The File Stash API from Pipedream — 1 operation(s) for file stash.
  name: Pipedream File Stash API
  slug: pipedream-file-stash-api
- description: The MCP API from Pipedream — 1 operation(s) for mcp.
  name: Pipedream MCP API
  slug: pipedream-mcp-api
- description: The OAuth API from Pipedream — 1 operation(s) for oauth.
  name: Pipedream OAuth API
  slug: pipedream-oauth-api
- description: The Projects API from Pipedream — 4 operation(s) for projects.
  name: Pipedream Projects API
  slug: pipedream-projects-api
- description: The Proxy API from Pipedream — 1 operation(s) for proxy.
  name: Pipedream Proxy API
  slug: pipedream-proxy-api
- description: The Tokens API from Pipedream — 2 operation(s) for tokens.
  name: Pipedream Tokens API
  slug: pipedream-tokens-api
- description: The Triggers API from Pipedream — 5 operation(s) for triggers.
  name: Pipedream Triggers API
  slug: pipedream-triggers-api
- description: The Usage API from Pipedream — 1 operation(s) for usage.
  name: Pipedream Usage API
  slug: pipedream-usage-api
- description: The Users API from Pipedream — 1 operation(s) for users.
  name: Pipedream Users API
  slug: pipedream-users-api
- description: The Webhooks API from Pipedream — 2 operation(s) for webhooks.
  name: Pipedream Webhooks API
  slug: pipedream-webhooks-api
arazzos:
- description: List a user's accounts for an app, inspect one, and remove all accounts for that app.
  name: Pipedream Audit and Clean Up Accounts by App
  slug: pipedream-account-audit-cleanup-workflow
- description: Browse app categories, search apps in a category, and retrieve one app's metadata.
  name: Pipedream App Discovery
  slug: pipedream-app-discovery-workflow
- description: Retrieve a component, then fetch the remote options for one of its props.
  name: Pipedream Configure a Component Prop
  slug: pipedream-configure-component-prop-workflow
- description: Mint a Connect token for an end user, connect their account, and confirm it landed.
  name: Pipedream Connect Account Onboarding
  slug: pipedream-connect-account-onboarding-workflow
- description: Find a trigger for an app, deploy it for an external user, and confirm deployment.
  name: Pipedream Deploy a Trigger
  slug: pipedream-deploy-trigger-workflow
- description: Retrieve a deployed trigger, then deactivate it via an update.
  name: Pipedream Pause a Deployed Trigger
  slug: pipedream-pause-deployed-trigger-workflow
- description: Set the project environment webhook URL, then read it back to confirm.
  name: Pipedream Configure Project Environment Webhook
  slug: pipedream-project-environment-webhook-workflow
- description: Create a Connect project, confirm it, and read its app configuration info.
  name: Pipedream Provision a Connect Project
  slug: pipedream-provision-project-workflow
- description: Retrieve a component, then reload its dynamic props from the current configuration.
  name: Pipedream Reload Dynamic Component Props
  slug: pipedream-reload-component-props-workflow
- description: Retrieve a trigger webhook, then regenerate its signing key and confirm the new key.
  name: Pipedream Rotate a Trigger Webhook Signing Key
  slug: pipedream-rotate-trigger-webhook-key-workflow
- description: Find an action for an app, inspect its props, and run it for an external user.
  name: Pipedream Discover and Run an Action
  slug: pipedream-run-action-for-app-workflow
- description: Confirm a deployed trigger, set its webhook listeners, then read them back.
  name: Pipedream Route Trigger Events to Webhooks
  slug: pipedream-set-trigger-webhooks-workflow
- description: Confirm a deployed trigger, bind it to Pipedream workflows, then read them back.
  name: Pipedream Route Trigger Events to Workflows
  slug: pipedream-set-trigger-workflows-workflow
- description: Create a Connect token for a user and validate it against a target app.
  name: Pipedream Connect Token Mint and Validate
  slug: pipedream-token-validation-workflow
- description: Retrieve a deployed trigger, then poll its most recent emitted events.
  name: Pipedream Inspect Deployed Trigger Events
  slug: pipedream-trigger-events-poll-workflow
- description: Read a project's current settings, apply updates, and confirm the new values.
  name: Pipedream Update Connect Project Settings
  slug: pipedream-update-project-settings-workflow
- description: List external users for a project, then pull Connect usage records for a window.
  name: Pipedream Connect Usage and Users Report
  slug: pipedream-usage-and-users-report-workflow
- description: List a user's accounts and deployed triggers, then delete the user and all their resources.
  name: Pipedream Offboard an External User
  slug: pipedream-user-offboarding-workflow
artifact_total: 234
collections:
- collection_type: postman
  name: Pipedream MCP Server Accounts API
  slug: postman-pipedream-accounts-api
- collection_type: postman
  name: Pipedream MCP Server Accounts Actions API
  slug: postman-pipedream-actions-api
- collection_type: postman
  name: Pipedream MCP Server Accounts App Categories API
  slug: postman-pipedream-app-categories-api
- collection_type: postman
  name: Pipedream MCP Server Accounts Apps API
  slug: postman-pipedream-apps-api
- collection_type: postman
  name: Pipedream MCP Server Accounts Components API
  slug: postman-pipedream-components-api
- collection_type: postman
  name: Pipedream MCP Server Accounts Deployed Triggers API
  slug: postman-pipedream-deployed-triggers-api
- collection_type: postman
  name: Pipedream MCP Server Accounts File Stash API
  slug: postman-pipedream-file-stash-api
- collection_type: postman
  name: Pipedream Server Accounts MCP API
  slug: postman-pipedream-mcp-api
- collection_type: postman
  name: Pipedream MCP Server Accounts OAuth API
  slug: postman-pipedream-oauth-api
- collection_type: postman
  name: Pipedream MCP Server Accounts Projects API
  slug: postman-pipedream-projects-api
- collection_type: postman
  name: Pipedream MCP Server Accounts Proxy API
  slug: postman-pipedream-proxy-api
- collection_type: postman
  name: Pipedream MCP Server Accounts Tokens API
  slug: postman-pipedream-tokens-api
- collection_type: postman
  name: Pipedream MCP Server Accounts Triggers API
  slug: postman-pipedream-triggers-api
- collection_type: postman
  name: Pipedream MCP Server Accounts Usage API
  slug: postman-pipedream-usage-api
- collection_type: postman
  name: Pipedream MCP Server Accounts Users API
  slug: postman-pipedream-users-api
- collection_type: postman
  name: Pipedream MCP Server Accounts Webhooks API
  slug: postman-pipedream-webhooks-api
- collection_type: open
  name: Pipedream MCP Server
  slug: open-pipedream-mcp
- collection_type: open
  name: Pipedream API
  slug: open-pipedream
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/pipedream/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pipedream-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pipedream-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pipedream-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pipedream-scopes.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-account-audit-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-app-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-configure-component-prop-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-connect-account-onboarding-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-deploy-trigger-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-pause-deployed-trigger-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-project-environment-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-provision-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-reload-component-props-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-rotate-trigger-webhook-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-run-action-for-app-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-set-trigger-webhooks-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-set-trigger-workflows-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-token-validation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-trigger-events-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-update-project-settings-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-usage-and-users-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pipedream-user-offboarding-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://pipedream.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pipedream.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://pipedream.com/docs/quickstart/
- group: auth
  title: ''
  type: Authentication
  url: https://pipedream.com/docs/rest-api/auth
- group: docs
  title: ''
  type: OpenAPI
  url: https://pipedream.com/docs/pipedream_openapi_swagger.json
- group: company
  title: ''
  type: Blog
  url: https://pipedream.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://pipedream.com/docs/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pipedream.com/
- group: operate
  title: ''
  type: StatusFeed
  url: https://status.pipedream.com/history.atom
- group: operate
  title: ''
  type: Support
  url: https://pipedream.com/support
- group: operate
  title: ''
  type: Forums
  url: https://pipedream.com/community/
- group: commercial
  title: ''
  type: Pricing
  url: https://pipedream.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://pipedream.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://pipedream.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pipedream.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pipedream.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://pipedream.com/docs/privacy-and-security
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pipedreamhq
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/PipedreamHQ
- group: other
  title: ''
  type: SourceRepo
  url: https://github.com/PipedreamHQ/pipedream
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PipedreamHQ/pipedream-sdk-typescript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PipedreamHQ/pipedream-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PipedreamHQ/pipedream-sdk-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PipedreamHQ/pipedream-go
- group: build
  title: ''
  type: CLI
  url: https://github.com/PipedreamHQ/homebrew-pd-cli
- group: build
  title: ''
  type: SamplesRepo
  url: https://github.com/PipedreamHQ/pipedream-connect-examples
- group: build
  title: ''
  type: SamplesRepo
  url: https://github.com/PipedreamHQ/mcp-chat
- group: commercial
  title: ''
  type: Plans
  url: plans/pipedream-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pipedream-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pipedream-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/pipedream-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/pipedream-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/pipedream-rules.yml
- group: other
  title: ''
  type: AcquisitionAnnouncement
  url: https://pipedream.com/blog/pipedream-to-be-acquired-by-workday/
- group: agent
  title: ''
  type: LlmsText
  url: https://pipedream.com/llms.txt
created: '2026-03-03'
description: 'Pipedream is a developer-centric integration platform providing three product lines: Workflows (code-level event-driven automation in Node.js/Python/Go/Bash), Connect (an embedded integration toolkit for adding customer-facing integrations and AI agents to applications, with managed OAuth for 3,000+ APIs), and a hosted MCP server exposing 10,000+ tools over JSON-RPC for AI agents. Pipedream announced an acquisition agreement with Workday on 2025-11-19.'
examples:
- key_count: 2
  name: Pipedream Create Connect Token Example
  slug: pipedream-create-connect-token-example
- key_count: 2
  name: Pipedream Deploy Trigger Example
  slug: pipedream-deploy-trigger-example
- key_count: 2
  name: Pipedream List Accounts Example
  slug: pipedream-list-accounts-example
- key_count: 2
  name: Pipedream List Apps Example
  slug: pipedream-list-apps-example
- key_count: 2
  name: Pipedream Mcp Tools Call Example
  slug: pipedream-mcp-tools-call-example
- key_count: 2
  name: Pipedream Mcp Tools List Example
  slug: pipedream-mcp-tools-list-example
- key_count: 2
  name: Pipedream Oauth Token Example
  slug: pipedream-oauth-token-example
- key_count: 2
  name: Pipedream Proxy Request Example
  slug: pipedream-proxy-request-example
- key_count: 2
  name: Pipedream Run Action Example
  slug: pipedream-run-action-example
features:
- 'Free: 100 credits/day (1 credit = 30 sec compute @ 256 MB)'
- 'Basic $29/mo: 2,000 credits/day, 30-day event history'
- 'Advanced $79/mo: 10,000 credits/day, 1-year history, custom domains'
- 'Business custom: unlimited credits, SSO/SAML, audit logs'
- 3,000+ integrated apps
- 10,000+ pre-built tools (exposed as MCP)
- Code-level workflow editor (Node.js, Python, Go, Bash)
- HTTP source endpoints (5 MB max event size)
- Schedule (cron) sources
- Webhook destinations with signing keys
- 'Connect: managed OAuth for 3,000+ APIs'
- 'Connect Proxy: signed custom HTTP requests on behalf of end-users'
- 'Connect File Stash: end-user file storage'
- 'MCP Server: hosted at remote.mcp.pipedream.net/v3 (SSE + streamable HTTP)'
- Native MCP support for OpenAI / Claude / Gemini / Vercel AI SDK
- 'REST API: 60 req/min/user limit'
- 'HTTP source: 100 req/sec/endpoint'
- Step caching for memoization
- Open-source workflow components (MIT)
finops:
- name: Pipedream Finops
  service_category: Workflow Automation
  slug: pipedream-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Pipedream developer-first workflow automation platform. Pipedream exposes its capabilities today via a REST API at `api.pipedream.com/v1` and a hosted MCP s
  name: Pipedream GraphQL Schema
  slug: pipedream-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pipedream.png
json_schemas:
- name: Pipedream Account
  property_count: 14
  slug: pipedream-account
- name: AccountId
  property_count: 0
  slug: pipedream-accountid
- name: Pipedream App
  property_count: 9
  slug: pipedream-app
- name: AppAuthType
  property_count: 0
  slug: pipedream-appauthtype
- name: Pipedream AppCategory
  property_count: 3
  slug: pipedream-appcategory
- name: BackendClientOpts
  property_count: 4
  slug: pipedream-backendclientopts
- name: ClientOpts
  property_count: 3
  slug: pipedream-clientopts
- name: Pipedream Component
  property_count: 8
  slug: pipedream-component
- name: ComponentStash
  property_count: 0
  slug: pipedream-componentstash
- name: ComponentType
  property_count: 0
  slug: pipedream-componenttype
- name: ConfigurableProp
  property_count: 0
  slug: pipedream-configurableprop
- name: ConfigurablePropAirtableBaseId
  property_count: 0
  slug: pipedream-configurablepropairtablebaseid
- name: ConfigurablePropAirtableFieldId
  property_count: 0
  slug: pipedream-configurablepropairtablefieldid
- name: ConfigurablePropAirtableTableId
  property_count: 0
  slug: pipedream-configurablepropairtabletableid
- name: ConfigurablePropAirtableViewId
  property_count: 0
  slug: pipedream-configurablepropairtableviewid
- name: ConfigurablePropAlert
  property_count: 0
  slug: pipedream-configurablepropalert
- name: ConfigurablePropAlertType
  property_count: 0
  slug: pipedream-configurablepropalerttype
- name: ConfigurablePropAny
  property_count: 0
  slug: pipedream-configurablepropany
- name: ConfigurablePropApp
  property_count: 0
  slug: pipedream-configurablepropapp
- name: ConfigurablePropApphook
  property_count: 0
  slug: pipedream-configurablepropapphook
- name: ConfigurablePropBase
  property_count: 12
  slug: pipedream-configurablepropbase
- name: ConfigurablePropBoolean
  property_count: 0
  slug: pipedream-configurablepropboolean
- name: ConfigurablePropDataStore
  property_count: 0
  slug: pipedream-configurablepropdatastore
- name: ConfigurablePropDb
  property_count: 0
  slug: pipedream-configurablepropdb
- name: ConfigurablePropDir
  property_count: 0
  slug: pipedream-configurablepropdir
- name: ConfigurablePropDirAccessMode
  property_count: 0
  slug: pipedream-configurablepropdiraccessmode
- name: ConfigurablePropDiscord
  property_count: 0
  slug: pipedream-configurablepropdiscord
- name: ConfigurablePropDiscordChannel
  property_count: 0
  slug: pipedream-configurablepropdiscordchannel
- name: ConfigurablePropDiscordChannelArray
  property_count: 0
  slug: pipedream-configurablepropdiscordchannelarray
- name: ConfigurablePropHttp
  property_count: 0
  slug: pipedream-configurableprophttp
- name: ConfigurablePropHttpRequest
  property_count: 0
  slug: pipedream-configurableprophttprequest
- name: ConfigurablePropInteger
  property_count: 0
  slug: pipedream-configurablepropinteger
- name: ConfigurablePropIntegerArray
  property_count: 0
  slug: pipedream-configurablepropintegerarray
- name: ConfigurablePropObject
  property_count: 0
  slug: pipedream-configurablepropobject
- name: ConfigurablePropSql
  property_count: 0
  slug: pipedream-configurablepropsql
- name: ConfigurablePropSqlAuth
  property_count: 1
  slug: pipedream-configurablepropsqlauth
- name: ConfigurablePropString
  property_count: 0
  slug: pipedream-configurablepropstring
- name: ConfigurablePropStringArray
  property_count: 0
  slug: pipedream-configurablepropstringarray
- name: ConfigurablePropStringFormat
  property_count: 0
  slug: pipedream-configurablepropstringformat
- name: ConfigurablePropTimer
  property_count: 0
  slug: pipedream-configurableproptimer
- name: ConfigurablePropTimerDefault
  property_count: 0
  slug: pipedream-configurableproptimerdefault
- name: ConfigurablePropTimerOption
  property_count: 0
  slug: pipedream-configurableproptimeroption
- name: ConfigurablePropTimerStatic
  property_count: 0
  slug: pipedream-configurableproptimerstatic
- name: ConfiguredProps
  property_count: 0
  slug: pipedream-configuredprops
- name: ConfiguredPropValue
  property_count: 0
  slug: pipedream-configuredpropvalue
- name: ConfiguredPropValueAny
  property_count: 0
  slug: pipedream-configuredpropvalueany
- name: ConfiguredPropValueApp
  property_count: 1
  slug: pipedream-configuredpropvalueapp
- name: ConfiguredPropValueBoolean
  property_count: 0
  slug: pipedream-configuredpropvalueboolean
- name: ConfiguredPropValueInteger
  property_count: 0
  slug: pipedream-configuredpropvalueinteger
- name: ConfiguredPropValueObject
  property_count: 0
  slug: pipedream-configuredpropvalueobject
- name: ConfiguredPropValueSql
  property_count: 4
  slug: pipedream-configuredpropvaluesql
- name: ConfiguredPropValueString
  property_count: 0
  slug: pipedream-configuredpropvaluestring
- name: ConfiguredPropValueStringArray
  property_count: 0
  slug: pipedream-configuredpropvaluestringarray
- name: ConfigurePropOptions
  property_count: 0
  slug: pipedream-configurepropoptions
- name: ConfigurePropOpts
  property_count: 10
  slug: pipedream-configurepropopts
- name: ConfigurePropResponse
  property_count: 5
  slug: pipedream-configurepropresponse
- name: Pipedream ConnectToken
  property_count: 0
  slug: pipedream-connecttoken
- name: Pipedream ConnectUsage
  property_count: 6
  slug: pipedream-connectusage
- name: ConnectUsageResponse
  property_count: 1
  slug: pipedream-connectusageresponse
- name: CreateAccountOpts
  property_count: 5
  slug: pipedream-createaccountopts
- name: CreateOAuthTokenOpts
  property_count: 4
  slug: pipedream-createoauthtokenopts
- name: CreateOAuthTokenResponse
  property_count: 3
  slug: pipedream-createoauthtokenresponse
- name: CreateProjectOpts
  property_count: 4
  slug: pipedream-createprojectopts
- name: CreateTokenOpts
  property_count: 8
  slug: pipedream-createtokenopts
- name: CreateTokenResponse
  property_count: 3
  slug: pipedream-createtokenresponse
- name: DeleteTriggerOpts
  property_count: 1
  slug: pipedream-deletetriggeropts
- name: DeployedComponent
  property_count: 15
  slug: pipedream-deployedcomponent
- name: DeployTriggerOpts
  property_count: 8
  slug: pipedream-deploytriggeropts
- name: DeployTriggerResponse
  property_count: 1
  slug: pipedream-deploytriggerresponse
- name: DynamicProps
  property_count: 2
  slug: pipedream-dynamicprops
- name: EmittedEvent
  property_count: 4
  slug: pipedream-emittedevent
- name: Emitter
  property_count: 0
  slug: pipedream-emitter
- name: EmitterType
  property_count: 0
  slug: pipedream-emittertype
- name: ErrorResponse
  property_count: 3
  slug: pipedream-errorresponse
- name: ExternalUser
  property_count: 4
  slug: pipedream-externaluser
- name: GetAccountsResponse
  property_count: 2
  slug: pipedream-getaccountsresponse
- name: GetAppCategoryResponse
  property_count: 0
  slug: pipedream-getappcategoryresponse
- name: GetAppResponse
  property_count: 1
  slug: pipedream-getappresponse
- name: GetAppsResponse
  property_count: 2
  slug: pipedream-getappsresponse
- name: GetComponentResponse
  property_count: 1
  slug: pipedream-getcomponentresponse
- name: GetComponentsResponse
  property_count: 2
  slug: pipedream-getcomponentsresponse
- name: GetTriggerEventsResponse
  property_count: 1
  slug: pipedream-gettriggereventsresponse
- name: GetTriggerResponse
  property_count: 1
  slug: pipedream-gettriggerresponse
- name: GetTriggersResponse
  property_count: 2
  slug: pipedream-gettriggersresponse
- name: GetTriggerWebhooksResponse
  property_count: 2
  slug: pipedream-gettriggerwebhooksresponse
- name: GetTriggerWorkflowsResponse
  property_count: 1
  slug: pipedream-gettriggerworkflowsresponse
- name: GetUsersResponse
  property_count: 2
  slug: pipedream-getusersresponse
- name: GetWebhookResponse
  property_count: 1
  slug: pipedream-getwebhookresponse
- name: GetWebhookWithSigningKeyResponse
  property_count: 1
  slug: pipedream-getwebhookwithsigningkeyresponse
- name: HttpInterface
  property_count: 7
  slug: pipedream-httpinterface
- name: HttpRequestAuth
  property_count: 4
  slug: pipedream-httprequestauth
- name: HttpRequestBody
  property_count: 5
  slug: pipedream-httprequestbody
- name: HttpRequestConfig
  property_count: 7
  slug: pipedream-httprequestconfig
- name: HttpRequestField
  property_count: 2
  slug: pipedream-httprequestfield
- name: JsonRpcRequest
  property_count: 4
  slug: pipedream-jsonrpcrequest
- name: JsonRpcResponse
  property_count: 4
  slug: pipedream-jsonrpcresponse
- name: ListAccountsResponse
  property_count: 2
  slug: pipedream-listaccountsresponse
- name: ListAppCategoriesResponse
  property_count: 0
  slug: pipedream-listappcategoriesresponse
- name: ListAppsResponse
  property_count: 2
  slug: pipedream-listappsresponse
- name: ListProjectsResponse
  property_count: 2
  slug: pipedream-listprojectsresponse
- name: Observation
  property_count: 4
  slug: pipedream-observation
- name: ObservationError
  property_count: 3
  slug: pipedream-observationerror
- name: PageInfo
  property_count: 4
  slug: pipedream-pageinfo
- name: Pipedream Project
  property_count: 5
  slug: pipedream-project
- name: ProjectEnvironment
  property_count: 0
  slug: pipedream-projectenvironment
- name: ProjectInfoResponse
  property_count: 1
  slug: pipedream-projectinforesponse
- name: ProjectInfoResponseApp
  property_count: 2
  slug: pipedream-projectinforesponseapp
- name: PropOption
  property_count: 2
  slug: pipedream-propoption
- name: PropOptionNested
  property_count: 1
  slug: pipedream-propoptionnested
- name: PropOptionValue
  property_count: 0
  slug: pipedream-propoptionvalue
- name: ProxyResponse
  property_count: 0
  slug: pipedream-proxyresponse
- name: ProxyResponseBinary
  property_count: 0
  slug: pipedream-proxyresponsebinary
- name: ReloadPropsOpts
  property_count: 6
  slug: pipedream-reloadpropsopts
- name: ReloadPropsResponse
  property_count: 3
  slug: pipedream-reloadpropsresponse
- name: RunActionOpts
  property_count: 6
  slug: pipedream-runactionopts
- name: RunActionOptsStashId
  property_count: 0
  slug: pipedream-runactionoptsstashid
- name: RunActionResponse
  property_count: 4
  slug: pipedream-runactionresponse
- name: SetWebhookOpts
  property_count: 1
  slug: pipedream-setwebhookopts
- name: SetWebhookResponse
  property_count: 1
  slug: pipedream-setwebhookresponse
- name: StartConnectOpts
  property_count: 1
  slug: pipedream-startconnectopts
- name: StashId
  property_count: 0
  slug: pipedream-stashid
- name: TimerCron
  property_count: 1
  slug: pipedream-timercron
- name: TimerInterface
  property_count: 8
  slug: pipedream-timerinterface
- name: TimerInterval
  property_count: 1
  slug: pipedream-timerinterval
- name: ToolAnnotations
  property_count: 5
  slug: pipedream-toolannotations
- name: TriggerWebhook
  property_count: 4
  slug: pipedream-triggerwebhook
- name: UpdateProjectLogoOpts
  property_count: 1
  slug: pipedream-updateprojectlogoopts
- name: UpdateProjectOpts
  property_count: 4
  slug: pipedream-updateprojectopts
- name: UpdateTriggerOpts
  property_count: 4
  slug: pipedream-updatetriggeropts
- name: UpdateTriggerWebhooksOpts
  property_count: 1
  slug: pipedream-updatetriggerwebhooksopts
- name: UpdateTriggerWorkflowsOpts
  property_count: 1
  slug: pipedream-updatetriggerworkflowsopts
- name: ValidateTokenResponse
  property_count: 10
  slug: pipedream-validatetokenresponse
- name: Webhook
  property_count: 5
  slug: pipedream-webhook
- name: WebhookWithOptionalSigningKey
  property_count: 6
  slug: pipedream-webhookwithoptionalsigningkey
- name: WebhookWithSigningKey
  property_count: 6
  slug: pipedream-webhookwithsigningkey
json_structures:
- name: Pipedream Account Structure
  property_count: 14
  slug: pipedream-account-structure
- name: Pipedream App Structure
  property_count: 9
  slug: pipedream-app-structure
- name: Pipedream Appcategory Structure
  property_count: 3
  slug: pipedream-appcategory-structure
- name: Pipedream Component Structure
  property_count: 8
  slug: pipedream-component-structure
- name: Pipedream Connecttoken Structure
  property_count: 0
  slug: pipedream-connecttoken-structure
- name: Pipedream Connectusage Structure
  property_count: 6
  slug: pipedream-connectusage-structure
- name: Pipedream Project Structure
  property_count: 5
  slug: pipedream-project-structure
- name: Pipedream Structure
  property_count: 0
  slug: pipedream-structure
jsonld:
- class_count: 40
  name: Pipedream Context
  property_count: 1
  slug: pipedream-context
layout: provider
modified: '2026-05-22'
name: Pipedream
nav: Providers
network: true
overview: 'Pipedream publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Actions API, App Categories API, and 13 more. Tagged areas include ProCode_API_Composition, Workflows, Connect, MCP, and Embedded Integrations.


  The Pipedream catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Pipedream''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, support, and 51 more developer resources.'
plans:
- name: Pipedream Plans Pricing
  plan_count: 4
  slug: pipedream-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 4
  name: Pipedream Rate Limits
  slug: pipedream-rate-limits
rules:
- name: Pipedream API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: pipedream-jsonschema-spectral-rules
- name: Pipedream API Rules
  rule_count: 9
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 7
  slug: pipedream-rules
scopes:
- name: Pipedream Scopes
  scope_count: 16
  slug: pipedream-scopes
  summary_line: 16 scopes · clientCredentials
score:
  band: exemplar
  composite: 72.8
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 72.3
    developer_ergonomics: 71.7
    discoverability: 50.0
    governance: 68.8
    operational_transparency: 78.9
  previous_composite: 72.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pipedream/refs/heads/main/screenshots/pipedream-2026-06-20T191726.png
security:
- kind: authentication
  name: Pipedream Authentication
  slug: pipedream-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Pipedream Domain Security
  slug: pipedream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pipedream
tags:
- ProCode_API_Composition
- Workflows
- Connect
- MCP
- Embedded Integrations
- Managed Auth
- AI Agents
website: https://pipedream.com/
---
