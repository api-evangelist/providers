---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
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
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 122
  human_in_the_loop: 6
  name: Wso2 Agentic Access
  operation_count: 268
  slug: wso2-agentic-access
  summary_line: 268 operations · 122 acting · 6 human-in-the-loop
api_count: 7
apis:
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Advanced Policy (Collection) API from WSO2 — 1 operation(s) for advanced policy (collection).
  name: WSO2 Advanced Policy (Collection) API
  phrasing_intents:
  - id: getThrottlingPoliciesAdvanced
    intent: List advanced throttling policies
    question: Which advanced throttling policies are defined in the admin portal?
  - id: postThrottlingPoliciesAdvanced
    intent: Create an advanced throttling policy
    question: Can I add a new advanced throttling policy with its own default limit?
  phrasing_ops: 2
  slug: wso2-advanced-policy-collection-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Advanced Policy (Individual) API from WSO2 — 1 operation(s) for advanced policy (individual).
  name: WSO2 Advanced Policy (Individual) API
  phrasing_intents:
  - id: getThrottlingPoliciesAdvancedByPolicyId
    intent: Get an advanced throttling policy
    question: What limits does one advanced throttling policy set?
  - id: putThrottlingPoliciesAdvancedByPolicyId
    intent: Update an advanced throttling policy
    question: Can I change the default limit of an existing advanced policy?
  - id: deleteThrottlingPoliciesAdvancedByPolicyId
    intent: Delete an advanced throttling policy
    question: Can I remove an advanced throttling policy I no longer use?
  phrasing_ops: 3
  slug: wso2-advanced-policy-individual-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The AIServiceProvider API from WSO2 — 1 operation(s) for aiserviceprovider.
  name: WSO2 AIServiceProvider API
  phrasing_intents:
  - id: updateAIServiceProvider
    intent: Update an AI service provider
    question: How do I change the OpenAPI definition of an AI service provider?
  - id: deleteAIServiceProvider
    intent: Delete an AI service provider
    question: How do I remove an AI service provider from API Manager?
  - id: getAIServiceProvider
    intent: Get an AI service provider
    question: How do I see the configuration of one AI service provider?
  phrasing_ops: 3
  slug: wso2-aiserviceprovider-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The AIServiceProviders API from WSO2 — 1 operation(s) for aiserviceproviders.
  name: WSO2 AIServiceProviders API
  phrasing_intents:
  - id: getAIServiceProviders
    intent: List AI service providers
    question: Which AI service providers are configured in API Manager?
  - id: addAIServiceProvider
    intent: Add an AI service provider
    question: How do I register a new AI service provider with its OpenAPI definition?
  phrasing_ops: 2
  slug: wso2-aiserviceproviders-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Alert Subscriptions API from WSO2 — 1 operation(s) for alert subscriptions.
  name: WSO2 Alert Subscriptions API
  phrasing_intents:
  - id: getSubscribedAlertTypes
    intent: List my admin alert subscriptions
    question: Which admin alerts am I currently subscribed to?
  - id: subscribeToAlerts
    intent: Subscribe to admin alerts
    question: How do I sign up for admin alerts by email?
  - id: unsubscribeAllAlerts
    intent: Unsubscribe from all admin alerts
    question: How do I stop receiving every admin alert at once?
  phrasing_ops: 3
  slug: wso2-alert-subscriptions-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Alerts API from WSO2 — 1 operation(s) for alerts.
  name: WSO2 Alerts API
  phrasing_intents:
  - id: getAdminAlertTypes
    intent: List supported admin alert types
    question: What alert types does the admin dashboard support?
  phrasing_ops: 1
  slug: wso2-alerts-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Api Artifact API from WSO2 — 1 operation(s) for api artifact.
  name: WSO2 Api Artifact API
  phrasing_intents:
  - id: getAPIArtifacts
    intent: Get an API's gateway artifacts
    question: Can I fetch the local entries, sequences and endpoints stored for an API?
  phrasing_ops: 1
  slug: wso2-api-artifact-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The API Categories API from WSO2 — 1 operation(s) for api categories.
  name: WSO2 API Categories API
  phrasing_intents:
  - id: getApiCategories
    intent: List API categories
    question: What API categories can I assign my APIs to?
  phrasing_ops: 1
  slug: wso2-api-categories-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The API Category (Collection) API from WSO2 — 1 operation(s) for api category (collection).
  name: WSO2 API Category (Collection) API
  phrasing_intents:
  - id: getApiCategories
    intent: List API categories
    question: What API categories can I assign my APIs to?
  phrasing_ops: 1
  slug: wso2-api-category-collection-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The API Category (Individual) API from WSO2 — 2 operation(s) for api category (individual).
  name: WSO2 API Category (Individual) API
  phrasing_intents:
  - id: postApiCategories
    intent: Add an API category
    question: Can I create a new category to group APIs in the portal?
  - id: putApiCategoriesByApiCategoryId
    intent: Rename or edit an API category
    question: Can I rename an existing API category?
  - id: deleteApiCategoriesByApiCategoryId
    intent: Delete an API category
    question: Can I delete an API category that is no longer needed?
  phrasing_ops: 3
  slug: wso2-api-category-individual-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The API Chat API from WSO2 — 1 operation(s) for api chat.
  name: WSO2 API Chat API
  phrasing_intents:
  - id: apiChatPost
    intent: Test an API with a natural-language scenario
    question: Can I test an API by describing a test case in plain English?
  phrasing_ops: 1
  slug: wso2-api-chat-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The API Documents API from WSO2 — 3 operation(s) for api documents.
  name: WSO2 API Documents API
  phrasing_intents:
  - id: getApisByApiIdDocuments
    intent: List documents of an API
    question: What documentation is attached to my API?
  - id: getApisByApiIdDocumentsByDocumentId
    intent: Get a document's metadata on an API
    question: Can I see the metadata of a single API document?
  - id: getApisByApiIdDocumentsByDocumentIdContent
    intent: Get an API document's content
    question: Can I read the actual text or file behind an API document?
  phrasing_ops: 3
  slug: wso2-api-documents-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The API Monetization API from WSO2 — 1 operation(s) for api monetization.
  name: WSO2 API Monetization API
  phrasing_intents:
  - id: getSubscriptionsBySubscriptionIdUsage
    intent: Get a subscription's pending invoice
    question: What does a monetized subscriber owe on their pending invoice?
  phrasing_ops: 1
  slug: wso2-api-monetization-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Api Provider Change API from WSO2 — 1 operation(s) for api provider change.
  name: WSO2 Api Provider Change API
  phrasing_intents:
  - id: providerNamePost
    intent: Change an API's provider
    question: How do I transfer an API to a different provider user?
  phrasing_ops: 1
  slug: wso2-api-provider-change-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The APIs API from WSO2 — 9 operation(s) for apis.
  name: WSO2 APIs API
  phrasing_intents:
  - id: getAllAPIs
    intent: Search APIs in the admin portal
    question: Which APIs exist across the admin portal?
  - id: getApisByApiId
    intent: Get full details of an API
    question: What's the full configuration of one of my APIs, including endpoints and policies?
  - id: getApisByApiIdSwagger
    intent: Get an API's OpenAPI definition
    question: How do I download the Swagger or OpenAPI definition of one of my APIs?
  - id: getApisByApiIdAsyncApiSpecification
    intent: Get an API's AsyncAPI definition
    question: Where can I download the AsyncAPI specification of an event-driven API?
  - id: getApisByApiIdGraphqlSchema
    intent: Get a GraphQL API's schema
    question: How do I download the SDL schema of a GraphQL API?
  - id: getWSDLOfAPI
    intent: Get an API's WSDL definition
    question: How do I download the WSDL for a SOAP API?
  - id: getApisByApiIdThumbnail
    intent: Download an API's thumbnail
    question: How do I download the thumbnail image shown for an API?
  - id: getApisByApiIdSubscriptionPolicies
    intent: Get an API's subscription throttling tiers
    question: Which subscription throttling tiers are attached to my API?
  phrasing_ops: 9
  slug: wso2-apis-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Application API from WSO2 — 2 operation(s) for application.
  name: WSO2 Application API
  phrasing_intents:
  - id: updateApplicationSettings
    intent: Change an application's owner or token type
    question: How do I transfer ownership of an application to another user?
  - id: postApplicationsByApplicationIdChangeOwner
    intent: Change an app's owner (deprecated endpoint)
    question: Is there an older, deprecated endpoint just for changing an application's owner?
  phrasing_ops: 2
  slug: wso2-application-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Application (Collection) API from WSO2 — 1 operation(s) for application (collection).
  name: WSO2 Application (Collection) API
  phrasing_intents:
  - id: getApplications
    intent: List or search applications as admin
    question: Which applications does a given user own?
  phrasing_ops: 1
  slug: wso2-application-collection-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Application Keys API from WSO2 — 10 operation(s) for application keys.
  name: WSO2 Application Keys API
  phrasing_intents:
  - id: postApplicationsByApplicationIdGenerateKeys
    intent: Generate consumer keys for an app
    question: Can I generate a consumer key and secret for my application?
  - id: postApplicationsByApplicationIdMapKeys
    intent: Map existing OAuth keys to an app
    question: Can I attach an OAuth client I already have to an application?
  - id: getApplicationsByApplicationIdKeys
    intent: List an app's keys by key type
    question: What production and sandbox keys does my application have?
  - id: getApplicationsByApplicationIdKeysByKeyType
    intent: Get an app's keys of one key type
    question: Can I see just the production key details of my application?
  - id: putApplicationsByApplicationIdKeysByKeyType
    intent: Update grant types by key type
    question: Can I change the callback URL of my production keys by key type?
  - id: postApplicationsByApplicationIdKeysByKeyTypeRegenerateSecret
    intent: Regenerate a secret by key type
    question: Can I rotate the consumer secret of my production keys?
  - id: postApplicationsByApplicationIdKeysByKeyTypeCleanUp
    intent: Clean up failed keys by key type
    question: What do I do when generating production keys failed halfway?
  - id: getApplicationsByApplicationIdOauthKeys
    intent: List an app's OAuth key mappings
    question: Which OAuth key mappings across key managers does my application have?
  phrasing_ops: 13
  slug: wso2-application-keys-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Application Policy (Collection) API from WSO2 — 1 operation(s) for application policy (collection).
  name: WSO2 Application Policy (Collection) API
  phrasing_intents:
  - id: getThrottlingPoliciesApplication
    intent: List application throttling policies
    question: Which application-level throttling policies exist?
  - id: postThrottlingPoliciesApplication
    intent: Create an application throttling policy
    question: Can I add a new application-level throttling tier?
  phrasing_ops: 2
  slug: wso2-application-policy-collection-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Application Policy (Individual) API from WSO2 — 1 operation(s) for application policy (individual).
  name: WSO2 Application Policy (Individual) API
  phrasing_intents:
  - id: getThrottlingPoliciesApplicationByPolicyId
    intent: Get an application throttling policy
    question: What limits does one application throttling tier enforce?
  - id: putThrottlingPoliciesApplicationByPolicyId
    intent: Update an application throttling policy
    question: Can I raise the default limit of an application tier?
  - id: deleteThrottlingPoliciesApplicationByPolicyId
    intent: Delete an application throttling policy
    question: Can I delete an application tier nobody uses anymore?
  phrasing_ops: 3
  slug: wso2-application-policy-individual-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Application Secrets API from WSO2 — 3 operation(s) for application secrets.
  name: WSO2 Application Secrets API
  phrasing_intents:
  - id: generateConsumerSecret
    intent: Generate a new OAuth consumer secret
    question: How do I create an additional consumer secret for my application's OAuth keys?
  - id: getConsumerSecrets
    intent: List an application's consumer secrets
    question: Which consumer secrets exist for my application's OAuth keys?
  - id: revokeConsumerSecret
    intent: Revoke an OAuth consumer secret
    question: How do I revoke a compromised consumer secret?
  phrasing_ops: 3
  slug: wso2-application-secrets-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Application Tokens API from WSO2 — 2 operation(s) for application tokens.
  name: WSO2 Application Tokens API
  phrasing_intents:
  - id: postApplicationsByApplicationIdKeysByKeyTypeGenerateToken
    intent: Generate an access token by key type
    question: Can I get a client-credentials access token for my production keys?
  - id: postApplicationsByApplicationIdOauthKeysByKeyMappingIdGenerateToken
    intent: Generate an access token for a key mapping
    question: Can I generate a token from one specific key manager mapping?
  phrasing_ops: 2
  slug: wso2-application-tokens-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Applications API from WSO2 — 3 operation(s) for applications.
  name: WSO2 Applications API
  phrasing_intents:
  - id: getApplicationsByApplicationId
    intent: Get an application's details
    question: What are the settings of one of my applications?
  - id: deleteApplicationsByApplicationId
    intent: Delete an application
    question: Can I delete an application I no longer use?
  - id: putApplicationsByApplicationId
    intent: Update an application
    question: Can I rename one of my applications or change its tier?
  - id: getApplications
    intent: List or search my applications
    question: Which applications do I have in the developer portal?
  - id: postApplications
    intent: Create a new application
    question: How do I create a new application to subscribe to APIs?
  - id: postApplicationsByApplicationIdResetThrottlePolicy
    intent: Reset an app's throttle for a user
    question: Can I reset the application-level throttle counter for a specific user?
  phrasing_ops: 6
  slug: wso2-applications-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: for accessing artifact compliance.
  name: WSO2 Artifact Compliance API
  phrasing_intents:
  - id: getComplianceStatusListOfAPIs
    intent: List compliance status of every API
    question: Which of our APIs are compliant with governance policies?
  - id: getComplianceSummaryForAPIs
    intent: Summarize API compliance across the org
    question: How many of our APIs pass versus fail governance overall?
  - id: getComplianceByAPIId
    intent: Get compliance details for one API
    question: Why is a particular API failing governance?
  - id: getRulesetValidationResultsByAPIId
    intent: Get ruleset validation results for an API
    question: Which rules in one ruleset did my API violate?
  phrasing_ops: 4
  slug: wso2-artifact-compliance-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Bot Detection Alert Subscriptions API from WSO2 — 2 operation(s) for bot detection alert subscriptions.
  name: WSO2 Bot Detection Alert Subscriptions API
  phrasing_intents:
  - id: getBotDetectionAlertSubscriptions
    intent: List bot detection alert subscribers
    question: Who is signed up to get bot detection email alerts?
  - id: subscribeForBotDetectionAlerts
    intent: Subscribe an email to bot detection alerts
    question: How do I start getting emails when bots are detected?
  - id: unsubscribeFromBotDetectionAlerts
    intent: Unsubscribe from bot detection alerts
    question: How do I stop receiving bot detection alert emails?
  phrasing_ops: 3
  slug: wso2-bot-detection-alert-subscriptions-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Bot Detection Data API from WSO2 — 1 operation(s) for bot detection data.
  name: WSO2 Bot Detection Data API
  phrasing_intents:
  - id: getBotDetectionData
    intent: List bot detection data
    question: What bot activity has been detected against our APIs?
  phrasing_ops: 1
  slug: wso2-bot-detection-data-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Comments API from WSO2 — 6 operation(s) for comments.
  name: WSO2 Comments API
  phrasing_intents:
  - id: getAllCommentsOfAPI
    intent: List comments on an API
    question: What comments have people left on this API in the developer portal?
  - id: addCommentToAPI
    intent: Post a comment on an API
    question: How do I leave a comment on an API in the WSO2 developer portal?
  - id: getCommentOfAPI
    intent: Get one comment on an API
    question: Where can I see the full detail of a single comment on an API, including its replies?
  - id: editCommentOfAPI
    intent: Edit a comment on an API
    question: Can I change the text of a comment I already posted on an API?
  - id: deleteComment
    intent: Delete a comment from an API
    question: How do I remove a comment someone posted on an API?
  - id: getRepliesOfComment
    intent: List replies to an API comment
    question: What replies has a comment on an API received?
  - id: getAllCommentsOfMCPServer
    intent: List comments on an MCP server
    question: What feedback have developers left as comments on an MCP server?
  - id: addCommentToMCPServer
    intent: Post a comment on an MCP server
    question: How do I leave a comment on an MCP server in the developer portal?
  phrasing_ops: 12
  slug: wso2-comments-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Config API from WSO2 — 1 operation(s) for config.
  name: WSO2 Config API
  phrasing_intents:
  - id: getConfigCorrelation
    intent: Check correlation log status
    question: Are correlation logs turned on for the product's components?
  - id: putConfigCorrelation
    intent: Enable or disable correlation logs
    question: Can I turn on correlation logs for just some components?
  phrasing_ops: 2
  slug: wso2-config-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Consumption API from WSO2 — 1 operation(s) for consumption.
  name: WSO2 Consumption API
  phrasing_intents:
  - id: exportConsumptionData
    intent: Export API usage data for a date range
    question: How do I download API consumption data for last month?
  phrasing_ops: 1
  slug: wso2-consumption-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Custom Rules (Collection) API from WSO2 — 1 operation(s) for custom rules (collection).
  name: WSO2 Custom Rules (Collection) API
  phrasing_intents:
  - id: getThrottlingPoliciesCustom
    intent: List custom throttling rules
    question: Which custom throttling rules are defined for the super tenant?
  - id: postThrottlingPoliciesCustom
    intent: Add a custom throttling rule
    question: Can I write a custom throttling rule with a Siddhi query?
  phrasing_ops: 2
  slug: wso2-custom-rules-collection-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Custom Rules (Individual) API from WSO2 — 1 operation(s) for custom rules (individual).
  name: WSO2 Custom Rules (Individual) API
  phrasing_intents:
  - id: getThrottlingPoliciesCustomByRuleId
    intent: Get a custom throttling rule
    question: What Siddhi query does one custom rule run?
  - id: putThrottlingPoliciesCustomByRuleId
    intent: Update a custom throttling rule
    question: Can I change the Siddhi query of an existing custom rule?
  - id: deleteThrottlingPoliciesCustomByRuleId
    intent: Delete a custom throttling rule
    question: Can I delete a custom rule that is no longer needed?
  phrasing_ops: 3
  slug: wso2-custom-rules-individual-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Deny Policies (Collection) API from WSO2 — 1 operation(s) for deny policies (collection).
  name: WSO2 Deny Policies (Collection) API
  phrasing_intents:
  - id: getThrottlingDenyPolicies
    intent: List deny policies
    question: Which deny policies are blocking traffic right now?
  - id: postThrottlingDenyPolicies
    intent: Add a deny policy
    question: Can I block requests from a specific IP or user with a deny policy?
  phrasing_ops: 2
  slug: wso2-deny-policies-collection-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Deny Policy (Individual) API from WSO2 — 1 operation(s) for deny policy (individual).
  name: WSO2 Deny Policy (Individual) API
  phrasing_intents:
  - id: getThrottlingDenyPolicyByConditionId
    intent: Get a deny policy
    question: What does one deny policy block?
  - id: deleteThrottlingDenyPolicyByConditionId
    intent: Delete a deny policy
    question: Can I permanently remove a deny policy?
  - id: patchThrottlingDenyPolicyByConditionId
    intent: Turn a deny policy on or off
    question: Can I temporarily disable a deny policy without deleting it?
  phrasing_ops: 3
  slug: wso2-deny-policy-individual-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Environments API from WSO2 — 3 operation(s) for environments.
  name: WSO2 Environments API
  phrasing_intents:
  - id: getEnvironments
    intent: List gateway environments
    question: Which gateway environments are registered?
  - id: postEnvironments
    intent: Add a gateway environment
    question: Can I register a new gateway environment with its own virtual hosts?
  - id: getEnvironmentsByEnvironmentId
    intent: Get a gateway environment
    question: What is the configuration of one gateway environment?
  - id: putEnvironmentsByEnvironmentId
    intent: Update a gateway environment
    question: Can I change the virtual hosts of an existing environment?
  - id: deleteEnvironmentsByEnvironmentId
    intent: Delete a gateway environment
    question: Can I remove a gateway environment I no longer need?
  - id: getEnvironmentsByEnvironmentIdGateways
    intent: List gateway instances in an environment
    question: Which gateway instances are running in an environment?
  phrasing_ops: 6
  slug: wso2-environments-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Get API Info API from WSO2 — 2 operation(s) for get api info.
  name: WSO2 Get API Info API
  phrasing_intents:
  - id: getApis
    intent: Look up an API by context and version
    question: Can I find an API's stored information from its context and version?
  - id: getApisByApiId
    intent: Get full details of an API
    question: What's the full configuration of one of my APIs, including endpoints and policies?
  phrasing_ops: 2
  slug: wso2-get-api-info-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Get Application Info API from WSO2 — 1 operation(s) for get application info.
  name: WSO2 Get Application Info API
  phrasing_intents:
  - id: getApplications
    intent: Look up an application by name or UUID
    question: Can I fetch stored application information by its name?
  phrasing_ops: 1
  slug: wso2-get-application-info-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Get Subscription Info API from WSO2 — 1 operation(s) for get subscription info.
  name: WSO2 Get Subscription Info API
  phrasing_intents:
  - id: getSubscriptions
    intent: Look up subscription info for an API
    question: Can I get the stored subscription information for an API by its UUID?
  phrasing_ops: 1
  slug: wso2-get-subscription-info-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Global Key Manager (Collection) API from WSO2 — 1 operation(s) for global key manager (collection).
  name: WSO2 Global Key Manager (Collection) API
  phrasing_intents:
  - id: getGlobalKeyManagers
    intent: List global key managers
    question: Which global key managers are shared across all tenants?
  - id: postGlobalKeyManagers
    intent: Add a global key manager
    question: Can I add a key manager that every tenant can use?
  phrasing_ops: 2
  slug: wso2-global-key-manager-collection-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Global Key Manager (Individual) API from WSO2 — 1 operation(s) for global key manager (individual).
  name: WSO2 Global Key Manager (Individual) API
  phrasing_intents:
  - id: getGlobalKeyManagersByKeyManagerId
    intent: Get a global key manager
    question: What endpoints does one global key manager use?
  - id: putGlobalKeyManagersByKeyManagerId
    intent: Update a global key manager
    question: Can I change the endpoints of a global key manager?
  - id: deleteGlobalKeyManagersByKeyManagerId
    intent: Delete a global key manager
    question: Can I remove a global key manager?
  phrasing_ops: 3
  slug: wso2-global-key-manager-individual-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: for managing governance policies.
  name: WSO2 Governance Policies API
  phrasing_intents:
  - id: getGovernancePolicies
    intent: List governance policies
    question: What governance policies are defined for our organization?
  - id: createGovernancePolicy
    intent: Create a governance policy
    question: How do I create a governance policy that enforces rulesets on our APIs?
  - id: getGovernancePolicyById
    intent: Get a governance policy
    question: What rulesets, labels and actions does a specific governance policy have?
  - id: updateGovernancePolicyById
    intent: Update a governance policy
    question: How do I change the rulesets on an existing governance policy?
  - id: deleteGovernancePolicy
    intent: Delete a governance policy
    question: How do I remove a governance policy we no longer need?
  phrasing_ops: 5
  slug: wso2-governance-policies-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The GraphQL Policies API from WSO2 — 2 operation(s) for graphql policies.
  name: WSO2 GraphQL Policies API
  phrasing_intents:
  - id: getApisByApiIdGraphqlPoliciesComplexity
    intent: Get GraphQL query complexity settings
    question: What complexity values are assigned to fields in my GraphQL API?
  - id: getApisByApiIdGraphqlPoliciesComplexityTypes
    intent: List types and fields of a GraphQL schema
    question: Which types and fields does my GraphQL API's schema define?
  phrasing_ops: 2
  slug: wso2-graphql-policies-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Import Export API from WSO2 — 4 operation(s) for import export.
  name: WSO2 Import Export API
  phrasing_intents:
  - id: exportThrottlingPolicy
    intent: Export a throttling policy
    question: How do I export a throttling policy to move it to another environment?
  - id: importThrottlingPolicy
    intent: Import a throttling policy
    question: How do I import a throttling policy from a JSON file?
  - id: getApplicationsExport
    intent: Export an application as a zip
    question: Can I export an application and its details to a zip file?
  - id: postApplicationsImport
    intent: Import an application from a file
    question: Can I import an application archive and keep its original owner?
  phrasing_ops: 4
  slug: wso2-import-export-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Key Manager (Collection) API from WSO2 — 2 operation(s) for key manager (collection).
  name: WSO2 Key Manager (Collection) API
  phrasing_intents:
  - id: getKeyManagers
    intent: List key managers
    question: Which key managers are configured to issue tokens?
  - id: postKeyManagers
    intent: Add a new key manager
    question: Can I register a new identity provider as a key manager?
  - id: postKeyManagersDiscover
    intent: Discover key manager settings from a URL
    question: Can I pull endpoint settings from an identity provider's well-known URL?
  phrasing_ops: 3
  slug: wso2-key-manager-collection-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Key Manager (Individual) API from WSO2 — 3 operation(s) for key manager (individual).
  name: WSO2 Key Manager (Individual) API
  phrasing_intents:
  - id: getKeyManagersByKeyManagerId
    intent: Get a key manager
    question: What endpoints and grant types does one key manager use?
  - id: putKeyManagersByKeyManagerId
    intent: Update a key manager
    question: Can I change the endpoints of a tenant key manager?
  - id: deleteKeyManagersByKeyManagerId
    intent: Delete a key manager
    question: Can I delete a tenant key manager?
  - id: getKeyManagersByKeyManagerIdApiUsages
    intent: List APIs using a key manager
    question: Which APIs rely on a particular key manager?
  - id: getKeyManagersByKeyManagerIdAppUsages
    intent: List applications using a key manager
    question: Which applications have keys from a particular key manager?
  phrasing_ops: 5
  slug: wso2-key-manager-individual-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Key Managers API from WSO2 — 1 operation(s) for key managers.
  name: WSO2 Key Managers API
  phrasing_intents:
  - id: getKeyManagers
    intent: List key managers
    question: Which key managers are configured to issue tokens?
  phrasing_ops: 1
  slug: wso2-key-managers-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Label (Individual) API from WSO2 — 3 operation(s) for label (individual).
  name: WSO2 Label (Individual) API
  phrasing_intents:
  - id: createLabel
    intent: Create a label
    question: How do I create a new label to group APIs?
  - id: updateLabel
    intent: Update a label
    question: Can I rename an existing label?
  - id: deleteLabel
    intent: Delete a label
    question: How do I delete a label we no longer use?
  - id: getLabelUsage
    intent: See where a label is used
    question: Which APIs is a given label attached to?
  phrasing_ops: 4
  slug: wso2-label-individual-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Labels (Collection) API from WSO2 — 1 operation(s) for labels (collection).
  name: WSO2 Labels (Collection) API
  phrasing_intents:
  - id: getAllLabels
    intent: List all labels
    question: What labels are defined in API Manager?
  phrasing_ops: 1
  slug: wso2-labels-collection-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Local Entry API from WSO2 — 1 operation(s) for local entry.
  name: WSO2 Local Entry API
  phrasing_intents:
  - id: getLocalEntries
    intent: Get an API's local entries
    question: Where can I see the local entries stored for an API?
  phrasing_ops: 1
  slug: wso2-local-entry-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Marketplace Assistant API from WSO2 — 2 operation(s) for marketplace assistant.
  name: WSO2 Marketplace Assistant API
  phrasing_intents:
  - id: getMarketplaceAssistantApiCount
    intent: Count APIs known to the marketplace assistant
    question: How many APIs does the marketplace assistant know about?
  - id: marketplaceAssistantExecute
    intent: Ask the marketplace assistant a question
    question: Can I ask the marketplace assistant in plain language to find an API?
  phrasing_ops: 2
  slug: wso2-marketplace-assistant-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The MCP Server Documents API from WSO2 — 3 operation(s) for mcp server documents.
  name: WSO2 MCP Server Documents API
  phrasing_intents:
  - id: getMCPServerDocuments
    intent: List an MCP server's documents
    question: What documentation is published for an MCP server?
  - id: getMCPServerDocument
    intent: Get an MCP server document's metadata
    question: What type and metadata does a specific MCP server document have?
  - id: getMCPServerDocumentContent
    intent: Read an MCP server document's content
    question: How do I read the actual text or file of an MCP server document?
  phrasing_ops: 3
  slug: wso2-mcp-server-documents-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The MCP Servers API from WSO2 — 4 operation(s) for mcp servers.
  name: WSO2 MCP Servers API
  phrasing_intents:
  - id: getAllMCPServers
    intent: Search available MCP servers
    question: What MCP servers are available in the developer portal?
  - id: getMCPServer
    intent: Get full details of an MCP server
    question: How do I see everything about one MCP server, including its full attributes?
  - id: getMCPServerThumbnail
    intent: Download an MCP server's thumbnail
    question: How do I get the thumbnail image for an MCP server?
  - id: getMCPServerSubscriptionPolicies
    intent: List an MCP server's subscription tiers
    question: What throttling tiers can I subscribe to for an MCP server?
  phrasing_ops: 4
  slug: wso2-mcp-servers-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Monetization (Collection) API from WSO2 — 2 operation(s) for monetization (collection).
  name: WSO2 Monetization (Collection) API
  phrasing_intents:
  - id: postMonetizationPublishUsage
    intent: Publish monetized API usage records
    question: Can I push usage records of monetized APIs to the billing engine now?
  - id: getMonetizationPublishUsageStatus
    intent: Check the usage publisher's status
    question: Did the last monetization usage publish run succeed?
  phrasing_ops: 2
  slug: wso2-monetization-collection-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Org Themes API from WSO2 — 4 operation(s) for org themes.
  name: WSO2 Org Themes API
  phrasing_intents:
  - id: getOrgThemes
    intent: List organization themes and publish status
    question: Which developer portal themes has my organization uploaded?
  - id: importOrgTheme
    intent: Import an organization theme zip
    question: How do I upload a custom theme for our developer portal?
  - id: getOrgThemeContent
    intent: Download an org theme as a zip
    question: How do I download the files of an existing org theme?
  - id: deleteOrgTheme
    intent: Delete an organization theme
    question: How do I remove an old org theme?
  - id: updateOrgThemeStatus
    intent: Publish or unpublish an org theme
    question: How do I make an uploaded theme live on the developer portal?
  phrasing_ops: 5
  slug: wso2-org-themes-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Organizations API from WSO2 — 2 operation(s) for organizations.
  name: WSO2 Organizations API
  phrasing_intents:
  - id: getOrganizations
    intent: List organizations
    question: Which organizations are registered?
  - id: postOrganizations
    intent: Add an organization
    question: Can I register a new organization linked to an external ID?
  - id: getOrganizationsByOrganizationId
    intent: Get an organization
    question: What details are stored for one organization?
  - id: putOrganizationsByOrganizationId
    intent: Update an organization
    question: Can I rename an existing organization?
  - id: deleteOrganizationsByOrganizationId
    intent: Delete an organization
    question: Can I delete an organization?
  phrasing_ops: 5
  slug: wso2-organizations-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Platform Gateways API from WSO2 — 3 operation(s) for platform gateways.
  name: WSO2 Platform Gateways API
  phrasing_intents:
  - id: getPlatformGateways
    intent: List platform gateways
    question: Which platform gateways are registered for our organization?
  - id: createPlatformGateway
    intent: Register a platform gateway
    question: How do I register a new platform gateway and get its connection token?
  - id: regeneratePlatformGatewayToken
    intent: Regenerate a gateway's registration token
    question: How do I get a new registration token if a gateway's token was lost?
  - id: updatePlatformGateway
    intent: Update a platform gateway
    question: Can I change a platform gateway's display name or description?
  - id: deletePlatformGateway
    intent: Delete a platform gateway
    question: How do I remove a platform gateway and its tokens?
  phrasing_ops: 5
  slug: wso2-platform-gateways-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: for accessing policy adherence.
  name: WSO2 Policy Adherence API
  phrasing_intents:
  - id: getPolicyAdherenceForAllPolicies
    intent: List adherence status for every policy
    question: How is each governance policy being adhered to across our organization?
  - id: getPolicyAdherenceSummary
    intent: Summarize governance policy adherence
    question: How many governance policies are being followed versus violated overall?
  - id: getPolicyAdherenceByPolicyId
    intent: Get adherence details for one policy
    question: Which artifacts violate a specific governance policy?
  phrasing_ops: 3
  slug: wso2-policy-adherence-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Ratings API from WSO2 — 4 operation(s) for ratings.
  name: WSO2 Ratings API
  phrasing_intents:
  - id: getApisByApiIdRatings
    intent: List all ratings of an API
    question: What ratings have developers given an API in the portal?
  - id: getApisByApiIdUserRating
    intent: Get my own rating of an API
    question: What rating did I personally give this API?
  - id: putApisByApiIdUserRating
    intent: Rate an API or change my rating
    question: Can I give an API a star rating or change the one I gave?
  - id: deleteApisByApiIdUserRating
    intent: Remove my rating from an API
    question: Can I take back the rating I left on an API?
  - id: getMCPServerRatings
    intent: List ratings of an MCP server
    question: What ratings have users given an MCP server?
  - id: getMCPServerRating
    intent: Get my rating of an MCP server
    question: What rating did I give this MCP server?
  - id: addMCPServerRating
    intent: Rate an MCP server
    question: How do I give an MCP server a star rating?
  - id: deleteMCPServerRating
    intent: Remove my rating of an MCP server
    question: How do I withdraw the rating I gave an MCP server?
  phrasing_ops: 8
  slug: wso2-ratings-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Recommendations API from WSO2 — 1 operation(s) for recommendations.
  name: WSO2 Recommendations API
  phrasing_intents:
  - id: getRecommendations
    intent: Get recommended APIs for me
    question: Which APIs does the developer portal recommend for me?
  phrasing_ops: 1
  slug: wso2-recommendations-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Redeploy Api API from WSO2 — 1 operation(s) for redeploy api.
  name: WSO2 Redeploy Api
  phrasing_intents:
  - id: redployAPI
    intent: Redeploy an API to the gateway
    question: How do I force an API to be redeployed on the gateway?
  phrasing_ops: 1
  slug: wso2-redeploy-api-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Register API from WSO2 — 1 operation(s) for register.
  name: WSO2 Register API
  phrasing_intents:
  - id: postRegister
    intent: Register an OAuth client for the REST APIs
    question: Can I dynamically register a client app to call the management REST APIs?
  phrasing_ops: 1
  slug: wso2-register-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Roles API from WSO2 — 1 operation(s) for roles.
  name: WSO2 Roles API
  phrasing_intents:
  - id: validateSystemRole
    intent: Check whether a role exists
    question: Does a given role name already exist?
  phrasing_ops: 1
  slug: wso2-roles-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: for managing rulesets.
  name: WSO2 Rulesets API
  phrasing_intents:
  - id: getRulesets
    intent: List governance rulesets
    question: What rulesets does my organization have for API governance?
  - id: createRuleset
    intent: Create a governance ruleset
    question: How do I upload a new linting ruleset for API definitions in WSO2?
  - id: getRulesetById
    intent: Get a ruleset's details
    question: What are the details and metadata of a specific ruleset?
  - id: updateRulesetById
    intent: Update an existing ruleset
    question: How do I change the rules inside a ruleset I already created?
  - id: deleteRuleset
    intent: Delete a ruleset
    question: How do I remove a ruleset we no longer use?
  - id: getRulesetContent
    intent: Download a ruleset's rule file
    question: Where can I read the raw YAML or JSON rules inside a ruleset?
  - id: getRulesetUsage
    intent: See which policies use a ruleset
    question: Which governance policies depend on this ruleset?
  phrasing_ops: 7
  slug: wso2-rulesets-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The SDKs API from WSO2 — 2 operation(s) for sdks.
  name: WSO2 SDKs API
  phrasing_intents:
  - id: getApisByApiIdSdksByLanguage
    intent: Generate an SDK for an API
    question: Can I download a client SDK for an API in Java or Python?
  - id: getSdkGenLanguages
    intent: List supported SDK languages
    question: Which programming languages can SDKs be generated in?
  phrasing_ops: 2
  slug: wso2-sdks-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Sequence API from WSO2 — 1 operation(s) for sequence.
  name: WSO2 Sequence API
  phrasing_intents:
  - id: getSequences
    intent: Get an API's mediation sequences
    question: How do I fetch the mediation sequences stored for an API?
  phrasing_ops: 1
  slug: wso2-sequence-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Server Startup Healthcheck API from WSO2 — 1 operation(s) for server startup healthcheck.
  name: WSO2 Server Startup Healthcheck API
  phrasing_intents:
  - id: getServerStartupHealthcheck
    intent: Check that APIs deployed at startup
    question: Have all APIs finished deploying since the server started?
  phrasing_ops: 1
  slug: wso2-server-startup-healthcheck-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Services API from WSO2 — 6 operation(s) for services.
  name: WSO2 Services API
  phrasing_intents:
  - id: searchServices
    intent: Search the service catalog
    question: Which services are registered in our service catalog?
  - id: addService
    intent: Add a service to the service catalog
    question: How do I register a new service with its definition in the service catalog?
  - id: getServiceById
    intent: Get a catalog service's details
    question: What details does the catalog hold for a specific service?
  - id: updateService
    intent: Update a catalog service
    question: How do I update a catalog service's metadata and definition?
  - id: deleteService
    intent: Delete a catalog service
    question: How do I remove a service from the service catalog?
  - id: getServiceDefinition
    intent: Get a catalog service's definition
    question: Where can I download the API definition stored for a catalog service?
  - id: getServiceUsage
    intent: List APIs that use a catalog service
    question: Which APIs are built on a particular catalog service?
  - id: importService
    intent: Import a service from an archive
    question: How do I import a service into the catalog from a zip archive?
  phrasing_ops: 9
  slug: wso2-services-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Settings API from WSO2 — 2 operation(s) for settings.
  name: WSO2 Settings API
  phrasing_intents:
  - id: getSettings
    intent: Get publisher settings
    question: What settings is the publisher portal running with?
  - id: getSettingsApplicationAttributes
    intent: List configured application attributes
    question: Which custom attributes can an application have in the developer portal?
  phrasing_ops: 2
  slug: wso2-settings-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Subscription Policy (Collection) API from WSO2 — 1 operation(s) for subscription policy (collection).
  name: WSO2 Subscription Policy (Collection) API
  phrasing_intents:
  - id: getThrottlingPoliciesSubscription
    intent: List subscription throttling policies
    question: Which subscription-level throttling tiers exist?
  - id: postThrottlingPoliciesSubscription
    intent: Create a subscription throttling policy
    question: Can I add a new subscription tier with a default limit?
  phrasing_ops: 2
  slug: wso2-subscription-policy-collection-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Subscription Policy (Individual) API from WSO2 — 1 operation(s) for subscription policy (individual).
  name: WSO2 Subscription Policy (Individual) API
  phrasing_intents:
  - id: getThrottlingPoliciesSubscriptionByPolicyId
    intent: Get a subscription throttling policy
    question: What limits does one subscription tier enforce?
  - id: putThrottlingPoliciesSubscriptionByPolicyId
    intent: Update a subscription throttling policy
    question: Can I raise the default limit of an existing subscription tier?
  - id: deleteThrottlingPoliciesSubscriptionByPolicyId
    intent: Delete a subscription throttling policy
    question: Can I delete a subscription tier?
  phrasing_ops: 3
  slug: wso2-subscription-policy-individual-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Subscriptions API from WSO2 — 4 operation(s) for subscriptions.
  name: WSO2 Subscriptions API
  phrasing_intents:
  - id: getSubscriptions
    intent: List subscriptions to my APIs
    question: Which applications have subscribed to my APIs?
  - id: postSubscriptions
    intent: Subscribe an application to an API
    question: Can I subscribe one of my applications to an API from the developer portal?
  - id: postSubscriptionsMultiple
    intent: Subscribe to several APIs at once
    question: Is there a way to create many API subscriptions in a single request?
  - id: getAdditionalInfoOfAPISubscriptions
    intent: Get extra info on an API's subscriptions
    question: What additional information is attached to the subscriptions on an API?
  - id: getSubscriptionsBySubscriptionId
    intent: Get one subscription's details
    question: What tier and status does one particular subscription have?
  - id: putSubscriptionsBySubscriptionId
    intent: Change an existing subscription
    question: Can I move an existing subscription to a different throttling tier?
  - id: deleteSubscriptionsBySubscriptionId
    intent: Unsubscribe from an API
    question: How do I unsubscribe my application from an API?
  phrasing_ops: 7
  slug: wso2-subscriptions-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The System Scopes API from WSO2 — 3 operation(s) for system scopes.
  name: WSO2 System Scopes API
  phrasing_intents:
  - id: systemScopesScopeNameGet
    intent: Check whether a user has a scope
    question: Does a particular user hold a given system scope?
  - id: systemScopesGet
    intent: List role-to-scope mappings
    question: Which roles are mapped to each system scope in the tenant config?
  - id: updateRolesForScope
    intent: Update roles assigned to scopes
    question: How do I change which roles can use each system scope?
  - id: getSystemScopesRoleAliases
    intent: List role alias mappings
    question: Which role aliases are mapped to the system scope roles?
  - id: putSystemScopesRoleAliases
    intent: Add role alias mappings
    question: Can I alias one role to another for system scope checks?
  phrasing_ops: 5
  slug: wso2-system-scopes-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Tags API from WSO2 — 1 operation(s) for tags.
  name: WSO2 Tags API
  phrasing_intents:
  - id: getTags
    intent: List tags used on APIs
    question: Which tags have been added to APIs in the developer portal?
  phrasing_ops: 1
  slug: wso2-tags-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Tenant Config API from WSO2 — 1 operation(s) for tenant config.
  name: WSO2 Tenant Config API
  phrasing_intents:
  - id: exportTenantConfig
    intent: Export the tenant configuration
    question: How do I download the tenant-config.json used in my deployment?
  - id: updateTenantConfig
    intent: Update the tenant configuration
    question: How do I change tenant-level settings in API Manager?
  phrasing_ops: 2
  slug: wso2-tenant-config-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Tenant Config Schema API from WSO2 — 1 operation(s) for tenant config schema.
  name: WSO2 Tenant Config Schema API
  phrasing_intents:
  - id: exportTenantConfigSchema
    intent: Export the tenant configuration schema
    question: Where can I get the JSON schema that tenant-config.json must follow?
  phrasing_ops: 1
  slug: wso2-tenant-config-schema-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Tenant Logs API from WSO2 — 2 operation(s) for tenant logs.
  name: WSO2 Tenant Logs API
  phrasing_intents:
  - id: getTenantLogsByTenantApis
    intent: List API log levels in a tenant
    question: Which APIs in a tenant have logging turned on?
  - id: getTenantLogsByTenantApisByApiId
    intent: Get one API's log settings
    question: What log level is set on one particular API?
  - id: putTenantLogsByTenantApisByApiId
    intent: Set an API's log level
    question: Can I turn on full request logging for one API?
  phrasing_ops: 3
  slug: wso2-tenant-logs-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Tenant Theme API from WSO2 — 1 operation(s) for tenant theme.
  name: WSO2 Tenant Theme API
  phrasing_intents:
  - id: exportTenantTheme
    intent: Export the DevPortal tenant theme
    question: How do I download our developer portal's tenant theme?
  - id: importTenantTheme
    intent: Import a DevPortal tenant theme
    question: How do I upload a custom theme for our developer portal?
  phrasing_ops: 2
  slug: wso2-tenant-theme-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Tenants API from WSO2 — 3 operation(s) for tenants.
  name: WSO2 Tenants API
  phrasing_intents:
  - id: getTenantInfoByUsername
    intent: Look up a user's tenant
    question: Which tenant does a given user belong to?
  - id: getCustomUrlInfoByTenantDomain
    intent: Get custom URL info for a tenant domain
    question: What custom URLs are configured for a tenant domain?
  - id: getTenants
    intent: List tenants by state
    question: Which tenants are currently active?
  phrasing_ops: 3
  slug: wso2-tenants-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Throttling Policies API from WSO2 — 2 operation(s) for throttling policies.
  name: WSO2 Throttling Policies API
  phrasing_intents:
  - id: getThrottlingPoliciesByPolicyLevel
    intent: List throttling policies of a level
    question: What throttling tiers are available at the application or subscription level?
  - id: getThrottlingPoliciesByPolicyLevelByPolicyId
    intent: Get one throttling policy
    question: What request limits does a named throttling tier enforce?
  phrasing_ops: 2
  slug: wso2-throttling-policies-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Topics API from WSO2 — 1 operation(s) for topics.
  name: WSO2 Topics API
  phrasing_intents:
  - id: getApisByApiIdTopics
    intent: List topics of an async API
    question: Which topics does an event-driven API expose?
  phrasing_ops: 1
  slug: wso2-topics-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Transaction Records API from WSO2 — 1 operation(s) for transaction records.
  name: WSO2 Transaction Records API
  phrasing_intents:
  - id: getTransactionCount
    intent: Count transactions in a time window
    question: How many transactions went through between two points in time?
  phrasing_ops: 1
  slug: wso2-transaction-records-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Undeploy Api API from WSO2 — 1 operation(s) for undeploy api.
  name: WSO2 Undeploy Api
  phrasing_intents:
  - id: undeployAPI
    intent: Undeploy an API from the gateway
    question: How do I take an API off the gateway?
  phrasing_ops: 1
  slug: wso2-undeploy-api-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Unified Search API from WSO2 — 2 operation(s) for unified search.
  name: WSO2 Unified Search API
  phrasing_intents:
  - id: throttlingPolicySearch
    intent: Search throttling policies
    question: How do I find a throttling policy by name?
  - id: getSearch
    intent: Search APIs and their documents by content
    question: Can I search across both APIs and their documentation content at once?
  phrasing_ops: 2
  slug: wso2-unified-search-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Users API from WSO2 — 2 operation(s) for users.
  name: WSO2 Users API
  phrasing_intents:
  - id: organizationInformation
    intent: Get my organization information
    question: Which organization does my logged-in account belong to?
  - id: changeUserPassword
    intent: Change my password
    question: How do I change my password while logged in?
  phrasing_ops: 2
  slug: wso2-users-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Webhooks API from WSO2 — 1 operation(s) for webhooks.
  name: WSO2 Webhooks API
  phrasing_intents:
  - id: getWebhooksSubscriptions
    intent: List an app's webhook subscriptions
    question: Which webhook topics is my application subscribed to?
  phrasing_ops: 1
  slug: wso2-webhooks-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Workflow (Collection) API from WSO2 — 1 operation(s) for workflow (collection).
  name: WSO2 Workflow (Collection) API
  phrasing_intents:
  - id: getWorkflows
    intent: List pending workflow requests
    question: Which approval requests are waiting on me?
  phrasing_ops: 1
  slug: wso2-workflow-collection-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Workflows (Individual) API from WSO2 — 2 operation(s) for workflows (individual).
  name: WSO2 Workflows (Individual) API
  phrasing_intents:
  - id: getWorkflowsByExternalWorkflowRef
    intent: Get a pending workflow request
    question: What exactly is a pending approval request asking for?
  - id: postWorkflowsUpdateWorkflowStatus
    intent: Approve or reject a workflow
    question: Can I approve a pending subscription or app creation request?
  phrasing_ops: 2
  slug: wso2-workflows-individual-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The API Keys API from WSO2 — 16 operation(s) for api keys.
  name: WSO2 API Keys API
  phrasing_intents:
  - id: getAllAPIKeys
    intent: List every API key as an admin
    question: Can an admin see all the API keys issued across the WSO2 API Manager?
  - id: revokeAPIKeyFromAdmin
    intent: Revoke any API key as an admin
    question: How does an administrator revoke someone's API key without going through the API or application?
  - id: generateApiBoundApiKey
    intent: Generate an API key bound to one API
    question: How do I generate a self-contained API key that works only for a single API?
  - id: regenerateAPIBoundAPIKey
    intent: Regenerate an API-bound API key
    question: How do I rotate an API key that was issued directly for an API?
  - id: getAPIBoundAPIKeys
    intent: List API keys bound to an API
    question: Which self-contained keys have been generated directly for a given API?
  - id: revokeAPIBoundAPIKey
    intent: Revoke an API-bound API key
    question: How do I revoke a key that was generated for a specific API rather than an application?
  - id: associateAPIKey
    intent: Link an API-bound key to an application
    question: Can I attach a key generated on an API to an application from the API side?
  - id: dissociateAPIKey
    intent: Unlink an API-bound key from its application
    question: How do I detach an API's key from the application it was linked to, working from the API side?
  phrasing_ops: 16
  slug: wso2-api-keys-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The Endpoints API from WSO2 — 1 operation(s) for endpoints.
  name: WSO2 Endpoints API
  phrasing_intents:
  - id: getEndpoints
    intent: Get an API's stored endpoints
    question: Where can I see the endpoints stored for a deployed API?
  phrasing_ops: 1
  slug: wso2-endpoints-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The LLM Provider API from WSO2 — 1 operation(s) for llm provider.
  name: WSO2 LLM Provider API
  phrasing_intents:
  - id: updateLLMProvider
    intent: Update an LLM provider
    question: How do I change the model list of an LLM provider?
  - id: deleteLLMProvider
    intent: Delete an LLM provider
    question: How do I remove an LLM provider from API Manager?
  - id: getLLMProvider
    intent: Get an LLM provider
    question: How do I see the configuration of one LLM provider?
  phrasing_ops: 3
  slug: wso2-llm-provider-api
- baseURL: https://apis.wso2.com
  baseurl_source: declared
  description: The LLM Providers API from WSO2 — 1 operation(s) for llm providers.
  name: WSO2 LLM Providers API
  phrasing_intents:
  - id: getLLMProviders
    intent: List LLM providers
    question: Which LLM providers are configured in API Manager?
  - id: addLLMProvider
    intent: Add an LLM provider
    question: How do I register a new LLM provider?
  phrasing_ops: 2
  slug: wso2-llm-providers-api
artifact_total: 1343
collections:
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Advanced Policy (Collection) API
  slug: postman-wso2-advanced-policy-collection-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Advanced Policy (Individual) API
  slug: postman-wso2-advanced-policy-individual-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) AIServiceProvider API
  slug: postman-wso2-aiserviceprovider-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) AIServiceProviders API
  slug: postman-wso2-aiserviceproviders-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Alert Subscriptions API
  slug: postman-wso2-alert-subscriptions-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Alerts API
  slug: postman-wso2-alerts-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Api Artifact API
  slug: postman-wso2-api-artifact-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) API Categories API
  slug: postman-wso2-api-categories-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) API Category (Collection) API
  slug: postman-wso2-api-category-collection-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) API Category (Individual) API
  slug: postman-wso2-api-category-individual-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) API Chat API
  slug: postman-wso2-api-chat-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) API Documents API
  slug: postman-wso2-api-documents-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) API Monetization API
  slug: postman-wso2-api-monetization-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Api Provider Change API
  slug: postman-wso2-api-provider-change-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) APIKeys API
  slug: postman-wso2-apikeys-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) APIs API
  slug: postman-wso2-apis-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application API
  slug: postman-wso2-application-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application (Collection) API
  slug: postman-wso2-application-collection-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application Keys API
  slug: postman-wso2-application-keys-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application Policy (Collection) API
  slug: postman-wso2-application-policy-collection-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application Policy (Individual) API
  slug: postman-wso2-application-policy-individual-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application Secrets API
  slug: postman-wso2-application-secrets-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application Tokens API
  slug: postman-wso2-application-tokens-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Applications API
  slug: postman-wso2-applications-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Artifact Compliance API
  slug: postman-wso2-artifact-compliance-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Bot Detection Alert Subscriptions API
  slug: postman-wso2-bot-detection-alert-subscriptions-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Bot Detection Data API
  slug: postman-wso2-bot-detection-data-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Comments API
  slug: postman-wso2-comments-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Config API
  slug: postman-wso2-config-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Consumption API
  slug: postman-wso2-consumption-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Custom Rules (Collection) API
  slug: postman-wso2-custom-rules-collection-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Custom Rules (Individual) API
  slug: postman-wso2-custom-rules-individual-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Deny Policies (Collection) API
  slug: postman-wso2-deny-policies-collection-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Deny Policy (Individual) API
  slug: postman-wso2-deny-policy-individual-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) End Points API
  slug: postman-wso2-end-points-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Environments API
  slug: postman-wso2-environments-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Get API Info API
  slug: postman-wso2-get-api-info-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Get Application Info API
  slug: postman-wso2-get-application-info-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Get Subscription Info API
  slug: postman-wso2-get-subscription-info-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Global Key Manager (Collection) API
  slug: postman-wso2-global-key-manager-collection-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Global Key Manager (Individual) API
  slug: postman-wso2-global-key-manager-individual-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Governance Policies API
  slug: postman-wso2-governance-policies-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) GraphQL Policies API
  slug: postman-wso2-graphql-policies-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Import Export API
  slug: postman-wso2-import-export-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Key Manager (Collection) API
  slug: postman-wso2-key-manager-collection-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Key Manager (Individual) API
  slug: postman-wso2-key-manager-individual-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Key Managers API
  slug: postman-wso2-key-managers-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Label (Individual) API
  slug: postman-wso2-label-individual-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Labels (Collection) API
  slug: postman-wso2-labels-collection-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) LLMProvider API
  slug: postman-wso2-llmprovider-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) LLMProviders API
  slug: postman-wso2-llmproviders-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Local Entry API
  slug: postman-wso2-local-entry-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Marketplace Assistant API
  slug: postman-wso2-marketplace-assistant-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) MCP Server Documents API
  slug: postman-wso2-mcp-server-documents-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) MCP Servers API
  slug: postman-wso2-mcp-servers-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Monetization (Collection) API
  slug: postman-wso2-monetization-collection-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Org Themes API
  slug: postman-wso2-org-themes-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Organizations API
  slug: postman-wso2-organizations-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Platform Gateways API
  slug: postman-wso2-platform-gateways-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Policy Adherence API
  slug: postman-wso2-policy-adherence-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Ratings API
  slug: postman-wso2-ratings-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Recommendations API
  slug: postman-wso2-recommendations-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Redeploy Api API
  slug: postman-wso2-redeploy-api-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Register API
  slug: postman-wso2-register-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Roles API
  slug: postman-wso2-roles-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Rulesets API
  slug: postman-wso2-rulesets-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) SDKs API
  slug: postman-wso2-sdks-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Sequence API
  slug: postman-wso2-sequence-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Server Startup Healthcheck API
  slug: postman-wso2-server-startup-healthcheck-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Services API
  slug: postman-wso2-services-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Settings API
  slug: postman-wso2-settings-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Subscription Policy (Collection) API
  slug: postman-wso2-subscription-policy-collection-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Subscription Policy (Individual) API
  slug: postman-wso2-subscription-policy-individual-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Subscriptions API
  slug: postman-wso2-subscriptions-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) System Scopes API
  slug: postman-wso2-system-scopes-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Tags API
  slug: postman-wso2-tags-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Tenant Config API
  slug: postman-wso2-tenant-config-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Tenant Config Schema API
  slug: postman-wso2-tenant-config-schema-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Tenant Logs API
  slug: postman-wso2-tenant-logs-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Tenant Theme API
  slug: postman-wso2-tenant-theme-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Tenants API
  slug: postman-wso2-tenants-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Throttling Policies API
  slug: postman-wso2-throttling-policies-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Topics API
  slug: postman-wso2-topics-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Transaction Records API
  slug: postman-wso2-transaction-records-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Undeploy Api API
  slug: postman-wso2-undeploy-api-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Unified Search API
  slug: postman-wso2-unified-search-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Users API
  slug: postman-wso2-users-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Webhooks API
  slug: postman-wso2-webhooks-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Workflow (Collection) API
  slug: postman-wso2-workflow-collection-api
- collection_type: postman
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Workflows (Individual) API
  slug: postman-wso2-workflows-individual-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Advanced Policy (Collection) API
  slug: open-wso2-advanced-policy-collection-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Advanced Policy (Individual) API
  slug: open-wso2-advanced-policy-individual-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) AIServiceProvider API
  slug: open-wso2-aiserviceprovider-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) AIServiceProviders API
  slug: open-wso2-aiserviceproviders-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Alert Subscriptions API
  slug: open-wso2-alert-subscriptions-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Alerts API
  slug: open-wso2-alerts-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Api Artifact API
  slug: open-wso2-api-artifact-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) API Categories API
  slug: open-wso2-api-categories-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) API Category (Collection) API
  slug: open-wso2-api-category-collection-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) API Category (Individual) API
  slug: open-wso2-api-category-individual-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) API Chat API
  slug: open-wso2-api-chat-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) API Documents API
  slug: open-wso2-api-documents-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) API Monetization API
  slug: open-wso2-api-monetization-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Api Provider Change API
  slug: open-wso2-api-provider-change-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) APIKeys API
  slug: open-wso2-apikeys-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) APIs API
  slug: open-wso2-apis-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application API
  slug: open-wso2-application-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application (Collection) API
  slug: open-wso2-application-collection-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application Keys API
  slug: open-wso2-application-keys-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application Policy (Collection) API
  slug: open-wso2-application-policy-collection-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application Policy (Individual) API
  slug: open-wso2-application-policy-individual-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application Secrets API
  slug: open-wso2-application-secrets-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Application Tokens API
  slug: open-wso2-application-tokens-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Applications API
  slug: open-wso2-applications-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Artifact Compliance API
  slug: open-wso2-artifact-compliance-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Bot Detection Alert Subscriptions API
  slug: open-wso2-bot-detection-alert-subscriptions-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Bot Detection Data API
  slug: open-wso2-bot-detection-data-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Comments API
  slug: open-wso2-comments-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Config API
  slug: open-wso2-config-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Consumption API
  slug: open-wso2-consumption-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Custom Rules (Collection) API
  slug: open-wso2-custom-rules-collection-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Custom Rules (Individual) API
  slug: open-wso2-custom-rules-individual-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Deny Policies (Collection) API
  slug: open-wso2-deny-policies-collection-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Deny Policy (Individual) API
  slug: open-wso2-deny-policy-individual-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) End Points API
  slug: open-wso2-end-points-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Environments API
  slug: open-wso2-environments-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Get API Info API
  slug: open-wso2-get-api-info-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Get Application Info API
  slug: open-wso2-get-application-info-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Get Subscription Info API
  slug: open-wso2-get-subscription-info-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Global Key Manager (Collection) API
  slug: open-wso2-global-key-manager-collection-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Global Key Manager (Individual) API
  slug: open-wso2-global-key-manager-individual-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Governance Policies API
  slug: open-wso2-governance-policies-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) GraphQL Policies API
  slug: open-wso2-graphql-policies-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Import Export API
  slug: open-wso2-import-export-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Key Manager (Collection) API
  slug: open-wso2-key-manager-collection-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Key Manager (Individual) API
  slug: open-wso2-key-manager-individual-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Key Managers API
  slug: open-wso2-key-managers-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Label (Individual) API
  slug: open-wso2-label-individual-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Labels (Collection) API
  slug: open-wso2-labels-collection-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) LLMProvider API
  slug: open-wso2-llmprovider-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) LLMProviders API
  slug: open-wso2-llmproviders-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Local Entry API
  slug: open-wso2-local-entry-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Marketplace Assistant API
  slug: open-wso2-marketplace-assistant-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) MCP Server Documents API
  slug: open-wso2-mcp-server-documents-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) MCP Servers API
  slug: open-wso2-mcp-servers-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Monetization (Collection) API
  slug: open-wso2-monetization-collection-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Org Themes API
  slug: open-wso2-org-themes-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Organizations API
  slug: open-wso2-organizations-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Platform Gateways API
  slug: open-wso2-platform-gateways-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Policy Adherence API
  slug: open-wso2-policy-adherence-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Ratings API
  slug: open-wso2-ratings-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Recommendations API
  slug: open-wso2-recommendations-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Redeploy Api API
  slug: open-wso2-redeploy-api-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Register API
  slug: open-wso2-register-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Roles API
  slug: open-wso2-roles-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Rulesets API
  slug: open-wso2-rulesets-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) SDKs API
  slug: open-wso2-sdks-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Sequence API
  slug: open-wso2-sequence-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Server Startup Healthcheck API
  slug: open-wso2-server-startup-healthcheck-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Services API
  slug: open-wso2-services-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Settings API
  slug: open-wso2-settings-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Subscription Policy (Collection) API
  slug: open-wso2-subscription-policy-collection-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Subscription Policy (Individual) API
  slug: open-wso2-subscription-policy-individual-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Subscriptions API
  slug: open-wso2-subscriptions-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) System Scopes API
  slug: open-wso2-system-scopes-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Tags API
  slug: open-wso2-tags-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Tenant Config API
  slug: open-wso2-tenant-config-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Tenant Config Schema API
  slug: open-wso2-tenant-config-schema-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Tenant Logs API
  slug: open-wso2-tenant-logs-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Tenant Theme API
  slug: open-wso2-tenant-theme-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Tenants API
  slug: open-wso2-tenants-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Throttling Policies API
  slug: open-wso2-throttling-policies-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Topics API
  slug: open-wso2-topics-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Transaction Records API
  slug: open-wso2-transaction-records-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Undeploy Api API
  slug: open-wso2-undeploy-api-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Unified Search API
  slug: open-wso2-unified-search-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Users API
  slug: open-wso2-users-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Webhooks API
  slug: open-wso2-webhooks-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Workflow (Collection) API
  slug: open-wso2-workflow-collection-api
- collection_type: open
  name: WSO2 API Manager - Admin Advanced Policy (Collection) Advanced Policy (Collection) Workflows (Individual) API
  slug: open-wso2-workflows-individual-api
common:
- group: commercial
  href: https://artifacts.apis.io/wso2/finops/wso2-finops.yml
  title: ''
  type: FinOps
  url: finops/wso2-finops.yml
- group: design
  href: https://artifacts.apis.io/wso2/rules/wso2-rules.yml
  title: ''
  type: Spectral
  url: rules/wso2-rules.yml
- group: design
  href: https://artifacts.apis.io/wso2/rules/wso2-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/wso2-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/wso2/json-ld/wso2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wso2-context.jsonld
- group: design
  href: https://artifacts.apis.io/wso2/vocabulary/wso2-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wso2-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/wso2/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/wso2/data-model/wso2-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wso2-data-model.yml
- group: build
  href: https://artifacts.apis.io/wso2/cli/wso2-cli.yml
  title: ''
  type: CLI
  url: cli/wso2-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://wso2.com/security
- group: design
  href: https://artifacts.apis.io/wso2/errors/wso2-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wso2-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wso2/conformance/wso2-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wso2-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wso2/llms/wso2-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wso2-llms.txt
- group: agent
  href: https://artifacts.apis.io/wso2/mcp/wso2-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wso2-mcp.yml
- group: other
  href: https://artifacts.apis.io/wso2/hosts/wso2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wso2-hosts.yml
- group: other
  href: https://artifacts.apis.io/wso2/vendors/wso2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wso2-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: http://wso2.com/identity-platform/capabilities/webhooks/
- group: company
  title: ''
  type: Newsroom
  url: https://wso2.com/about/news
- group: start
  title: ''
  type: Login
  url: https://wso2.com/user/login
- group: other
  title: ''
  type: Leadership
  url: https://wso2.com/team/
- group: docs
  title: ''
  type: APIReference
  url: https://wso2.com/api-platform/docs/tools/cli/reference/
- group: other
  href: https://artifacts.apis.io/wso2/vendor-facets/wso2-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/wso2-vendor-facets.yml
- group: operate
  href: https://artifacts.apis.io/wso2/rate-limits/wso2-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wso2-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/wso2/plans/wso2-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wso2-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/wso2/capabilities/wso2-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/wso2-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/wso2/product-apim/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/wso2/product-apim/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/wso2/product-apim/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/wso2/product-apim/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/wso2/product-apim/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/wso2/product-apim/blob/master/LICENSE
- group: build
  title: ''
  type: CLI
  url: https://apim.docs.wso2.com/en/latest/apiops/cli/cicd-using-cli/
- group: auth
  title: ''
  type: Security
  url: https://wso2.com/security
- group: start
  title: ''
  type: Signup
  url: https://wso2.com/user/register
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/wso2/overview
- group: agent
  href: https://artifacts.apis.io/wso2/agentic-access/wso2-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wso2-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/wso2/security/wso2-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/wso2-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/wso2/security/wso2-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/wso2-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/wso2/security/wso2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wso2-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/wso2/authentication/wso2-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wso2-authentication.yml
- group: auth
  href: https://artifacts.apis.io/wso2/scopes/wso2-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/wso2-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wso2
- group: company
  title: ''
  type: Website
  url: https://wso2.com/api-manager/
- group: docs
  title: ''
  type: Documentation
  url: https://apim.docs.wso2.com/en/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://apim.docs.wso2.com/en/latest/get-started/api-manager-quick-start-guide/
- group: company
  title: ''
  type: Blog
  url: https://wso2.com/library/blogs/
- group: commercial
  title: ''
  type: Pricing
  url: https://wso2.com/api-platform/pricing/
- group: company
  title: ''
  type: About
  url: https://wso2.com/about/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/wso2
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wso2.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wso2.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://apim.docs.wso2.com/en/latest/reference/faq/
- group: auth
  title: ''
  type: Authentication
  url: https://apim.docs.wso2.com/en/latest/api-security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://apim.docs.wso2.com/en/latest/get-started/overview/whats-new/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wso2.com/
- group: operate
  title: ''
  type: Community
  url: https://stackoverflow.com/questions/tagged/wso2
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/wso2
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/wso2/product-apim
- group: agent
  title: ''
  type: LlmsText
  url: https://wso2.com/llms.txt
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/wso2/agent-skills/blob/f53805729ad42f76bc616a11906e10de2c7bc0a1/plugins/api-platform/skills/api-design/references/agent-readiness-spectral/ai-readiness.yaml
created: '2026-03-03'
description: WSO2 API Manager is an open-source API management platform supporting REST, SOAP, and GraphQL with flexible hybrid deployment. It provides a unified control plane for managing APIs, AI models, and agents across on-premises, hybrid, and cloud environments. WSO2 is recognized as a Leader in the Forrester Wave API Management Q3 2024 report.
features:
- description: Design, publish, deprecate, and retire APIs across the full lifecycle.
  name: Full API Lifecycle Management
- description: Manages REST, GraphQL, gRPC, WebSocket, and Webhook APIs.
  name: Multi-Protocol Support
- description: Routes and manages LLM traffic with guardrails and PII masking.
  name: AI Gateway
- description: Converts REST APIs into Model Context Protocol tools for AI agents.
  name: MCP Gateway
- description: Policy enforcement and compliance checking across API designs.
  name: API Governance
- description: Programmatic OAuth2 client registration following OpenID Connect DCR spec.
  name: Dynamic Client Registration
- description: Subscription tiers, application policies, and advanced rate limiting.
  name: Advanced Throttling
- description: Real-time traffic analytics and usage insights via Moesif integration.
  name: Analytics
- description: Auto-generates client SDKs in multiple languages from API definitions.
  name: SDK Generation
- description: Registers and discovers backend services for API-first integration.
  name: Service Catalog
- description: CI/CD pipeline integration for automated API deployment.
  name: DevOps Integration
- description: Manages APIs across WSO2, Kong, AWS, Azure, and Envoy gateways.
  name: Multi-Gateway Support
finops:
- has_sources: true
  method: derived
  name: Wso2 Finops
  primary_unit: subscription
  service_category: ''
  slug: wso2-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wso2.png
integrations:
- description: AI Gateway supports routing to OpenAI models.
  name: OpenAI
- description: AI Gateway supports routing to Anthropic Claude models.
  name: Anthropic
- description: AI Gateway integrates with Azure OpenAI deployment.
  name: Azure OpenAI
- description: Multi-gateway management includes Kong.
  name: Kong Gateway
- description: Multi-gateway management includes AWS API Gateway.
  name: AWS API Gateway
- description: Analytics integration powered by Moesif.
  name: Moesif
- description: Native Kubernetes deployment support.
  name: Kubernetes
- description: Identity provider integration for OAuth2 flows.
  name: Keycloak
json_schemas:
- name: Additional Gateway Properties
  property_count: 2
  slug: admin-api-additional-property
- name: Advanced Throttling Policy
  property_count: 1
  slug: admin-api-advanced-throttle-policy-info
- name: Advanced Throttling Policy List
  property_count: 2
  slug: admin-api-advanced-throttle-policy-list
- name: Advanced Throttling Policy
  property_count: 2
  slug: admin-api-advanced-throttle-policy
- name: AIServiceProvider
  property_count: 7
  slug: admin-api-ai-service-provider-request
- name: AIServiceProviderResponse
  property_count: 10
  slug: admin-api-ai-service-provider-response
- name: AIServiceProviderSummaryResponseList
  property_count: 2
  slug: admin-api-ai-service-provider-summary-response-list
- name: AIServiceProviderSummaryResponse
  property_count: 6
  slug: admin-api-ai-service-provider-summary-response
- name: AI API Quota Limit object
  property_count: 4
  slug: admin-api-aiapi-quota-limit
- name: Alert Type
  property_count: 2
  slug: admin-api-alert-type
- name: Alert Types List
  property_count: 2
  slug: admin-api-alert-types-list
- name: Alerts Subscription
  property_count: 2
  slug: admin-api-alerts-subscription
- name: API Category List
  property_count: 2
  slug: admin-api-api-category-list
- name: API Category
  property_count: 4
  slug: admin-api-api-category
- name: APIInfoKeyManager
  property_count: 12
  slug: admin-api-api-info-key-manager
- name: API Info List
  property_count: 2
  slug: admin-api-api-info-list
- name: API info object with basic API details
  property_count: 4
  slug: admin-api-api-info
- name: API Keys List
  property_count: 2
  slug: admin-api-api-key-list
- name: API Key revoke request object
  property_count: 1
  slug: admin-api-api-key-revoke-request
- name: API Key details to invoke APIs
  property_count: 9
  slug: admin-api-api-key
- name: ApiResult
  property_count: 4
  slug: admin-api-api-result
- name: ApplicationInfoKeyManager
  property_count: 5
  slug: admin-api-application-info-key-manager
- name: Application info object with basic application details
  property_count: 8
  slug: admin-api-application-info
- name: Application List
  property_count: 3
  slug: admin-api-application-list
- name: Application object with all the application details
  property_count: 11
  slug: admin-api-application
- name: Application Level Throttling Policy List
  property_count: 2
  slug: admin-api-application-throttle-policy-list
- name: Application Throttling Policy
  property_count: 2
  slug: admin-api-application-throttle-policy
- name: ApplicationUpdateRequest
  property_count: 2
  slug: admin-api-application-update-request
- name: Bandwidth Limit object
  property_count: 2
  slug: admin-api-bandwidth-limit
- name: Blocking Conditions List
  property_count: 2
  slug: admin-api-blocking-condition-list
- name: Blocking Conditions
  property_count: 4
  slug: admin-api-blocking-condition
- name: Blocking Conditions Status
  property_count: 2
  slug: admin-api-blocking-condition-status
- name: Bot Detection Alert Subscription List
  property_count: 2
  slug: admin-api-bot-detection-alert-subscription-list
- name: Bot Detection Alert Subscription
  property_count: 2
  slug: admin-api-bot-detection-alert-subscription
- name: Bot Detection Data List
  property_count: 2
  slug: admin-api-bot-detection-data-list
- name: Bot Detection Data
  property_count: 6
  slug: admin-api-bot-detection-data
- name: Burst Limit object
  property_count: 2
  slug: admin-api-burst-limit
- name: Claim Mapping Configuration
  property_count: 2
  slug: admin-api-claim-mapping-entry
- name: Conditional Groups for Throttling
  property_count: 3
  slug: admin-api-conditional-group
- name: Configurable Configuration Constraints
  property_count: 8
  slug: admin-api-configuration-constraint
- name: ContentPublishStatusResponse
  property_count: 2
  slug: admin-api-content-publish-status-response
- name: ContentPublishStatus
  property_count: 1
  slug: admin-api-content-publish-status
- name: Create Platform Gateway Request
  property_count: 6
  slug: admin-api-create-platform-gateway-request
- name: Name-Value pair
  property_count: 2
  slug: admin-api-custom-attribute
- name: Custom Rule List
  property_count: 2
  slug: admin-api-custom-rule-list
- name: Custom Rule
  property_count: 2
  slug: admin-api-custom-rule
- name: Custom url information
  property_count: 4
  slug: admin-api-custom-url-info
- name: Environment List
  property_count: 2
  slug: admin-api-environment-list
- name: Environment
  property_count: 17
  slug: admin-api-environment
- name: Event Count Limit object
  property_count: 1
  slug: admin-api-event-count-limit
- name: Export Throttling Policy
  property_count: 4
  slug: admin-api-export-throttle-policy
- name: File Information including meta data
  property_count: 2
  slug: admin-api-file-info
- name: Gateway Configuration
  property_count: 9
  slug: admin-api-gateway-configuration
- name: Gateway Environment protocols and URIs
  property_count: 2
  slug: admin-api-gateway-environment-protocol-uri
- name: Gateway instance list
  property_count: 2
  slug: admin-api-gateway-instance-list
- name: Gateway instance in the gateway environment
  property_count: 3
  slug: admin-api-gateway-instance
- name: Gateway List
  property_count: 2
  slug: admin-api-gateway-list
- name: Gateway Response With Token
  property_count: 1
  slug: admin-api-gateway-response-with-token
- name: GraphQL Query
  property_count: 2
  slug: admin-api-graph-ql-query
- name: HTTP Header based throttling condition
  property_count: 2
  slug: admin-api-header-condition
- name: IP based throttling condition
  property_count: 4
  slug: admin-api-ip-condition
- name: JWT claim attibute based throttling condition
  property_count: 2
  slug: admin-api-jwt-claims-condition
- name: Key Manager API Usages.
  property_count: 2
  slug: admin-api-key-manager-api-usages
- name: Key Manager Application Usages.
  property_count: 2
  slug: admin-api-key-manager-app-usages
- name: Key Manager Configuration
  property_count: 10
  slug: admin-api-key-manager-configuration
- name: Key Manager Endpoint.
  property_count: 2
  slug: admin-api-key-manager-endpoint
- name: Key Manager Info
  property_count: 8
  slug: admin-api-key-manager-info
- name: Key Manager List
  property_count: 2
  slug: admin-api-key-manager-list
- name: Key Manager
  property_count: 36
  slug: admin-api-key-manager
- name: Key Manager Well-Known Response.
  property_count: 2
  slug: admin-api-key-manager-well-known-response
- name: Label List
  property_count: 3
  slug: admin-api-label-list
- name: Label
  property_count: 3
  slug: admin-api-label
- name: Label Usage
  property_count: 1
  slug: admin-api-label-usage
- name: LLMProvider
  property_count: 6
  slug: admin-api-llm-provider-request
- name: LLMProviderResponse
  property_count: 8
  slug: admin-api-llm-provider-response
- name: LLMProviderSummaryResponseList
  property_count: 2
  slug: admin-api-llm-provider-summary-response-list
- name: LLMProviderSummaryResponse
  property_count: 5
  slug: admin-api-llm-provider-summary-response
- name: Model Provider
  property_count: 2
  slug: admin-api-model-provider
- name: API monetization details object
  property_count: 2
  slug: admin-api-monetization-info
- name: Usage publish status
  property_count: 4
  slug: admin-api-monetization-usage-publish-info
- name: Organization Info
  property_count: 2
  slug: admin-api-organization-info
- name: Organization List
  property_count: 2
  slug: admin-api-organization-list
- name: Organization
  property_count: 5
  slug: admin-api-organization
- name: Pagination
  property_count: 5
  slug: admin-api-pagination-apis
- name: Pagination
  property_count: 5
  slug: admin-api-pagination
- name: Platform Gateway Response
  property_count: 10
  slug: admin-api-platform-gateway-response
- name: Usage publish status
  property_count: 2
  slug: admin-api-publish-status
- name: Query parameter based throttling condition
  property_count: 2
  slug: admin-api-query-parameter-condition
- name: Request Count Limit object
  property_count: 1
  slug: admin-api-request-count-limit
- name: Role alias list
  property_count: 2
  slug: admin-api-role-alias-list
- name: Role alias
  property_count: 2
  slug: admin-api-role-alias
- name: API Scope info object with scope details
  property_count: 4
  slug: admin-api-scope-info
- name: Scope Role Mapping List
  property_count: 2
  slug: admin-api-scope-list
- name: Scope Role
  property_count: 4
  slug: admin-api-scope
- name: Settings
  property_count: 1
  slug: admin-api-scope-settings
- name: Unified Search Result List
  property_count: 3
  slug: admin-api-search-result-list
- name: Settings
  property_count: 11
  slug: admin-api-settings
- name: Subscription Level Throttling Policy List
  property_count: 2
  slug: admin-api-subscription-throttle-policy-list
- name: SubscriptionThrottlePolicyPermission
  property_count: 2
  slug: admin-api-subscription-throttle-policy-permission
- name: Subscription Throttling Policy
  property_count: 9
  slug: admin-api-subscription-throttle-policy
- name: Tenant information
  property_count: 3
  slug: admin-api-tenant-info
- name: Throttling Conditions
  property_count: 6
  slug: admin-api-throttle-condition
- name: Throttle Limit Base
  property_count: 2
  slug: admin-api-throttle-limit-base
- name: Throttle Limit
  property_count: 5
  slug: admin-api-throttle-limit
- name: Policy List
  property_count: 2
  slug: admin-api-throttle-policy-details-list
- name: Generic Policy
  property_count: 7
  slug: admin-api-throttle-policy-details
- name: Throttle Policy List
  property_count: 3
  slug: admin-api-throttle-policy-list
- name: Generic Throttling Policy
  property_count: 6
  slug: admin-api-throttle-policy
- name: Token handling Configuration
  property_count: 4
  slug: admin-api-token-validation
- name: TransactionCount
  property_count: 1
  slug: admin-api-transaction-count
- name: Update Platform Gateway Request
  property_count: 6
  slug: admin-api-update-platform-gateway-request
- name: Virtual Host
  property_count: 8
  slug: admin-api-v-host
- name: Workflow info object with basic workflow details
  property_count: 7
  slug: admin-api-workflow-info
- name: WorkflowList
  property_count: 4
  slug: admin-api-workflow-list
- name: workflow Response
  property_count: 2
  slug: admin-api-workflow-response
- name: workflow
  property_count: 3
  slug: admin-api-workflow
- name: DCRResult
  property_count: 10
  slug: dcr-api-dcr-result
- name: DCR
  property_count: 7
  slug: dcr-api-dcr
- name: Properties for correlation components
  property_count: 2
  slug: devops-api-correlation-component-property
- name: Correlation Component INFO object
  property_count: 3
  slug: devops-api-correlation-component
- name: correlation-components
  property_count: 1
  slug: devops-api-correlation-components-list
- name: API Info object with log details
  property_count: 3
  slug: devops-api-logging-api-input
- name: apis
  property_count: 1
  slug: devops-api-logging-api-output-list
- name: API Info object with log details
  property_count: 5
  slug: devops-api-logging-api-output
- name: Additional Subscription Info List
  property_count: 3
  slug: devportal-api-additional-subscription-info-list
- name: Additional Information of subscriptions related to an API
  property_count: 7
  slug: devportal-api-additional-subscription-info
- name: API Advertise info object with advertise details
  property_count: 6
  slug: devportal-api-advertise-info
- name: APIBusinessInformation
  property_count: 4
  slug: devportal-api-api-business-information
- name: API Category List
  property_count: 2
  slug: devportal-api-api-category-list
- name: API Category
  property_count: 3
  slug: devportal-api-api-category
- name: API Chat request
  property_count: 4
  slug: devportal-api-api-chat-request
- name: API Chat response
  property_count: 5
  slug: devportal-api-api-chat-response
- name: API Definition Search Result
  property_count: 8
  slug: devportal-api-api-definition-search-result
- name: API Info List
  property_count: 2
  slug: devportal-api-api-info-list
- name: API Info object with basic API details.
  property_count: 23
  slug: devportal-api-api-info
- name: API Key association
  property_count: 7
  slug: devportal-api-api-key-association-info
- name: API Key Associations List
  property_count: 2
  slug: devportal-api-api-key-association-list
- name: API Key association
  property_count: 3
  slug: devportal-api-api-key-association
- name: API Key dissociation request object
  property_count: 1
  slug: devportal-api-api-key-dissociate-request
- name: API Key generation request object
  property_count: 3
  slug: devportal-api-api-key-generate-request
- name: API Key details to invoke APIs
  property_count: 5
  slug: devportal-api-api-key-info
- name: API Keys List
  property_count: 2
  slug: devportal-api-api-key-list
- name: API Key renewal request object
  property_count: 1
  slug: devportal-api-api-key-renew-request
- name: API Key revoke request object
  property_count: 2
  slug: devportal-api-api-key-revoke-request
- name: API Key details to invoke APIs
  property_count: 3
  slug: devportal-api-api-key
- name: API List
  property_count: 3
  slug: devportal-api-api-list
- name: API monetization object
  property_count: 1
  slug: devportal-api-api-monetization-info
- name: API monetization usage object
  property_count: 1
  slug: devportal-api-api-monetization-usage
- name: Operation
  property_count: 3
  slug: devportal-api-api-operations
- name: API object
  property_count: 40
  slug: devportal-api-api
- name: API Result
  property_count: 11
  slug: devportal-api-api-search-result
- name: API with API Key
  property_count: 4
  slug: devportal-api-api-with-key-info
- name: API Key association request object
  property_count: 2
  slug: devportal-api-apiapi-key-associate-request
- name: API Key generation request object
  property_count: 4
  slug: devportal-api-apiapi-key-generate-request
- name: API Key details to invoke APIs
  property_count: 6
  slug: devportal-api-apiapi-key-info
- name: API Keys List
  property_count: 2
  slug: devportal-api-apiapi-key-list
- name: API Key revoke request object
  property_count: 1
  slug: devportal-api-apiapi-key-revoke-request
- name: API Key association request object
  property_count: 2
  slug: devportal-api-app-api-key-associate-request
- name: Application Attributes List
  property_count: 2
  slug: devportal-api-application-attribute-list
- name: Application attributes
  property_count: 6
  slug: devportal-api-application-attribute
- name: Application Configuration Constraint
  property_count: 2
  slug: devportal-api-application-configuration-constraint
- name: Application info object with basic application details
  property_count: 12
  slug: devportal-api-application-info
- name: Application key generation request object
  property_count: 9
  slug: devportal-api-application-key-generate-request
- name: Application Keys List
  property_count: 2
  slug: devportal-api-application-key-list
- name: Application key provision request object
  property_count: 4
  slug: devportal-api-application-key-mapping-request
- name: Application key details after re generating consumer secret
  property_count: 2
  slug: devportal-api-application-key-re-generate-response
- name: Application key details
  property_count: 13
  slug: devportal-api-application-key
- name: Application List
  property_count: 3
  slug: devportal-api-application-list
- name: Application
  property_count: 16
  slug: devportal-api-application
- name: Reset application level throttling
  property_count: 1
  slug: devportal-api-application-throttle-reset
- name: Application access token generation request object
  property_count: 6
  slug: devportal-api-application-token-generate-request
- name: Application token details to invoke APIs
  property_count: 3
  slug: devportal-api-application-token
- name: ChatMessage
  property_count: 2
  slug: devportal-api-chat-message
- name: Comments List
  property_count: 3
  slug: devportal-api-comment-list
- name: Comment
  property_count: 10
  slug: devportal-api-comment
- name: CommenterInfo
  property_count: 3
  slug: devportal-api-commenter-info
- name: ConsumerSecretCreationRequest
  property_count: 1
  slug: devportal-api-consumer-secret-creation-request
- name: ConsumerSecretDeletionRequest
  property_count: 2
  slug: devportal-api-consumer-secret-deletion-request
- name: Client Secret List
  property_count: 2
  slug: devportal-api-consumer-secret-list
- name: ConsumerSecret
  property_count: 3
  slug: devportal-api-consumer-secret
- name: Current and new passowrd of the user
  property_count: 2
  slug: devportal-api-current-and-new-passwords
- name: Document List
  property_count: 3
  slug: devportal-api-document-list
- name: Document
  property_count: 7
  slug: devportal-api-document
- name: Document Result
  property_count: 12
  slug: devportal-api-document-search-result
- name: GraphQL Custom Complexity Info
  property_count: 3
  slug: devportal-api-graph-ql-custom-complexity-info
- name: GraphQL Query Complexity Info
  property_count: 1
  slug: devportal-api-graph-ql-query-complexity-info
- name: List of types and corresponding fields of the GraphQL Schema
  property_count: 1
  slug: devportal-api-graph-ql-schema-type-list
- name: Single type and corresponding fields found within the GraphQL Schema
  property_count: 2
  slug: devportal-api-graph-ql-schema-type
- name: Key Manager application Configuration
  property_count: 10
  slug: devportal-api-key-manager-application-configuration
- name: Key Manager Info
  property_count: 19
  slug: devportal-api-key-manager-info
- name: Key Manager List
  property_count: 2
  slug: devportal-api-key-manager-list
- name: MarketplaceAssistantApiCountResponse
  property_count: 2
  slug: devportal-api-marketplace-assistant-api-count-response
- name: MarketplaceAssistantApi
  property_count: 3
  slug: devportal-api-marketplace-assistant-api
- name: MarketplaceAssistantRequest
  property_count: 2
  slug: devportal-api-marketplace-assistant-request
- name: MarketplaceAssistantResponse
  property_count: 2
  slug: devportal-api-marketplace-assistant-response
- name: Monetization
  property_count: 5
  slug: devportal-api-monetization-info
- name: Organization Info
  property_count: 2
  slug: devportal-api-organization-info
- name: Pagination
  property_count: 5
  slug: devportal-api-pagination
- name: Patch request body
  property_count: 2
  slug: devportal-api-patch-request-body
- name: Post request body
  property_count: 2
  slug: devportal-api-post-request-body
- name: Rating List
  property_count: 5
  slug: devportal-api-rating-list
- name: Rating
  property_count: 4
  slug: devportal-api-rating
- name: API recommendations
  property_count: 2
  slug: devportal-api-recommendations
- name: Recommended API
  property_count: 3
  slug: devportal-api-recommended-api
- name: API Chat sample query record
  property_count: 2
  slug: devportal-api-sample-query
- name: API Scope info object with scope details
  property_count: 4
  slug: devportal-api-scope-info
- name: Scope list
  property_count: 3
  slug: devportal-api-scope-list
- name: Search Result List
  property_count: 3
  slug: devportal-api-search-result-list
- name: Search Result
  property_count: 4
  slug: devportal-api-search-result
- name: Settings
  property_count: 23
  slug: devportal-api-settings
- name: SolaceTopics
  property_count: 2
  slug: devportal-api-solace-topics
- name: Subscribed APIs with non-associated API keys
  property_count: 2
  slug: devportal-api-subscribed-api-with-api-key-list
- name: Subscription List
  property_count: 3
  slug: devportal-api-subscription-list
- name: Subscription
  property_count: 9
  slug: devportal-api-subscription
- name: Tag List
  property_count: 3
  slug: devportal-api-tag-list
- name: Tag
  property_count: 2
  slug: devportal-api-tag
- name: Tenant list
  property_count: 3
  slug: devportal-api-tenant-list
- name: Tenant
  property_count: 2
  slug: devportal-api-tenant
- name: Throttling Policy List
  property_count: 3
  slug: devportal-api-throttling-policy-list
- name: Throttling Policy Permission info object with throttling policy permission details
  property_count: 2
  slug: devportal-api-throttling-policy-permission-info
- name: Throttling Policy
  property_count: 15
  slug: devportal-api-throttling-policy
- name: Topic List
  property_count: 3
  slug: devportal-api-topic-list
- name: Topic
  property_count: 3
  slug: devportal-api-topic
- name: User
  property_count: 5
  slug: devportal-api-user
- name: Subscribed Webhook List
  property_count: 3
  slug: devportal-api-webhook-subscription-list
- name: Webhook Subscription
  property_count: 6
  slug: devportal-api-webhook-subscription
- name: workflow Response
  property_count: 2
  slug: devportal-api-workflow-response
- name: Action
  property_count: 3
  slug: governance-api-action
- name: APIMGovernancePolicyList
  property_count: 3
  slug: governance-api-apim-governance-policy-list
- name: APIMGovernancePolicy
  property_count: 11
  slug: governance-api-apim-governance-policy
- name: ArtifactComplianceDetails
  property_count: 4
  slug: governance-api-artifact-compliance-details
- name: ArtifactComplianceForPolicy
  property_count: 3
  slug: governance-api-artifact-compliance-for-policy
- name: ArtifactComplianceList
  property_count: 3
  slug: governance-api-artifact-compliance-list
- name: ArtifactComplianceStatus
  property_count: 5
  slug: governance-api-artifact-compliance-status
- name: ArtifactComplianceSummaryForPolicy
  property_count: 2
  slug: governance-api-artifact-compliance-summary-for-policy
- name: ArtifactComplianceSummary
  property_count: 5
  slug: governance-api-artifact-compliance-summary
- name: ArtifactInfo
  property_count: 5
  slug: governance-api-artifact-info
- name: Pagination
  property_count: 5
  slug: governance-api-pagination
- name: PolicyAdherenceDetails
  property_count: 4
  slug: governance-api-policy-adherence-details
- name: PolicyAdherenceList
  property_count: 3
  slug: governance-api-policy-adherence-list
- name: PolicyAdherenceStatus
  property_count: 4
  slug: governance-api-policy-adherence-status
- name: PolicyAdherenceSummary
  property_count: 4
  slug: governance-api-policy-adherence-summary
- name: PolicyAdherenceWithRulesets
  property_count: 4
  slug: governance-api-policy-adherence-with-rulesets
- name: RuleValidationResult
  property_count: 7
  slug: governance-api-rule-validation-result
- name: RulesetInfo
  property_count: 12
  slug: governance-api-ruleset-info
- name: RulesetInput
  property_count: 8
  slug: governance-api-ruleset-input
- name: RulesetList
  property_count: 3
  slug: governance-api-ruleset-list
- name: RulesetValidationResult
  property_count: 5
  slug: governance-api-ruleset-validation-result
- name: RulesetValidationResultWithoutRules
  property_count: 4
  slug: governance-api-ruleset-validation-result-without-rules
- name: SeverityBasedRuleViolationCount
  property_count: 2
  slug: governance-api-severity-based-rule-violation-count
- name: Additional Gateway Properties
  property_count: 2
  slug: publisher-api-additional-property
- name: API Advertise info object with advertise details
  property_count: 6
  slug: publisher-api-advertise-info
- name: AIServiceProviderEndpointAuthenticationConfiguration
  property_count: 3
  slug: publisher-api-ai-service-provider-endpoint-authentication-configuration
- name: AIServiceProviderEndpointConfiguration
  property_count: 3
  slug: publisher-api-ai-service-provider-endpoint-configuration
- name: AIServiceProviderResponse
  property_count: 8
  slug: publisher-api-ai-service-provider-response
- name: AIServiceProviderSummaryResponseList
  property_count: 2
  slug: publisher-api-ai-service-provider-summary-response-list
- name: AIServiceProviderSummaryResponse
  property_count: 6
  slug: publisher-api-ai-service-provider-summary-response
- name: APIBusinessInformation
  property_count: 4
  slug: publisher-api-api-business-information
- name: API Category List
  property_count: 2
  slug: publisher-api-api-category-list
- name: API Category
  property_count: 3
  slug: publisher-api-api-category
- name: APICorsConfiguration
  property_count: 5
  slug: publisher-api-api-cors-configuration
- name: API Definition Search Result
  property_count: 10
  slug: publisher-api-api-definition-search-result
- name: Endpoints List
  property_count: 3
  slug: publisher-api-api-endpoint-list
- name: Endpoint
  property_count: 5
  slug: publisher-api-api-endpoint
- name: API Endpoint url validation response
  property_count: 3
  slug: publisher-api-api-endpoint-validation-response
- name: API External Store List
  property_count: 2
  slug: publisher-api-api-external-store-list
- name: API External Store
  property_count: 2
  slug: publisher-api-api-external-store
- name: API Info object with basic API details.
  property_count: 30
  slug: publisher-api-api-info
- name: API Key details to invoke APIs
  property_count: 2
  slug: publisher-api-api-key
- name: API List
  property_count: 3
  slug: publisher-api-api-list
- name: APIMaxTps
  property_count: 5
  slug: publisher-api-api-max-tps
- name: API metadata List
  property_count: 3
  slug: publisher-api-api-metadata-list
- name: API Info object with basic minimal API details.
  property_count: 5
  slug: publisher-api-api-metadata
- name: API monetization object
  property_count: 2
  slug: publisher-api-api-monetization-info
- name: API monetization usage object
  property_count: 1
  slug: publisher-api-api-monetization-usage
- name: API Operation Mapping
  property_count: 5
  slug: publisher-api-api-operation-mapping
- name: API Operation Level Policies
  property_count: 3
  slug: publisher-api-api-operation-policies
- name: Operation
  property_count: 14
  slug: publisher-api-api-operations
- name: APIProductBusinessInformation
  property_count: 4
  slug: publisher-api-api-product-business-information
- name: API Info object with basic API details.
  property_count: 20
  slug: publisher-api-api-product-info
- name: API Product List
  property_count: 3
  slug: publisher-api-api-product-list
- name: APIProduct is outdated status
  property_count: 1
  slug: publisher-api-api-product-outdated-status
- name: API Product object
  property_count: 46
  slug: publisher-api-api-product
- name: API Result
  property_count: 16
  slug: publisher-api-api-product-search-result
- name: API revenue data object
  property_count: 1
  slug: publisher-api-api-revenue
- name: API Info object with basic Revisioned API details
  property_count: 1
  slug: publisher-api-api-revision-api-info
- name: API Revision to Deployment mapped object with basic API deployment details
  property_count: 1
  slug: publisher-api-api-revision-deployment-list
- name: APIRevisionDeployment Info object with basic API deployment details
  property_count: 10
  slug: publisher-api-api-revision-deployment
- name: API Revisions List
  property_count: 2
  slug: publisher-api-api-revision-list
- name: API Info object with basic API details
  property_count: 6
  slug: publisher-api-api-revision
- name: API object
  property_count: 69
  slug: publisher-api-api
- name: APIScope
  property_count: 2
  slug: publisher-api-api-scope
- name: API Result
  property_count: 19
  slug: publisher-api-api-search-result
- name: Application info object with basic application details
  property_count: 5
  slug: publisher-api-application-info
- name: Application
  property_count: 6
  slug: publisher-api-application
- name: AsyncAPI Specification Validation Response
  property_count: 4
  slug: publisher-api-async-api-specification-validation-response
- name: Resource for Audit Report
  property_count: 4
  slug: publisher-api-audit-report
- name: BackendList
  property_count: 2
  slug: publisher-api-backend-list
- name: API Operation Backend Mapping
  property_count: 2
  slug: publisher-api-backend-operation-mapping
- name: Backend Operation
  property_count: 2
  slug: publisher-api-backend-operation
- name: Backend Data
  property_count: 4
  slug: publisher-api-backend
- name: Bandwidth Limit object
  property_count: 2
  slug: publisher-api-bandwidth-limit
- name: Certificate
  property_count: 2
  slug: publisher-api-cert-metadata
- name: Certificate information
  property_count: 4
  slug: publisher-api-certificate-info
- name: Certificate Valid period
  property_count: 2
  slug: publisher-api-certificate-validity
- name: Certificates
  property_count: 3
  slug: publisher-api-certificates
- name: Claim
  property_count: 3
  slug: publisher-api-claim
- name: Client certificate meta data
  property_count: 3
  slug: publisher-api-client-cert-metadata
- name: Client Certificates
  property_count: 3
  slug: publisher-api-client-certificates
- name: Comments List
  property_count: 3
  slug: publisher-api-comment-list
- name: Comment request body
  property_count: 2
  slug: publisher-api-comment-request
- name: Comment
  property_count: 10
  slug: publisher-api-comment
- name: CommenterInfo
  property_count: 3
  slug: publisher-api-commenter-info
- name: ContentPublishStatusResponse
  property_count: 2
  slug: publisher-api-content-publish-status-response
- name: ContentPublishStatus
  property_count: 1
  slug: publisher-api-content-publish-status
- name: Name-Value pair
  property_count: 2
  slug: publisher-api-custom-attribute
- name: DesignAssistantAPIPayloadResponse
  property_count: 1
  slug: publisher-api-design-assistant-api-payload-response
- name: DesignAssistantChatQuery
  property_count: 2
  slug: publisher-api-design-assistant-chat-query
- name: DesignAssistantChatResponse
  property_count: 8
  slug: publisher-api-design-assistant-chat-response
- name: DesignAssistantGenAPIPayload
  property_count: 1
  slug: publisher-api-design-assistant-gen-api-payload
- name: Document List
  property_count: 3
  slug: publisher-api-document-list
- name: Document
  property_count: 14
  slug: publisher-api-document
- name: Document Result
  property_count: 14
  slug: publisher-api-document-search-result
- name: Endpoint Configuration
  property_count: 3
  slug: publisher-api-endpoint-config
- name: Endpoint List
  property_count: 2
  slug: publisher-api-endpoint-list
- name: Endpoints
  property_count: 6
  slug: publisher-api-endpoint
- name: Environment List
  property_count: 2
  slug: publisher-api-environment-list
- name: Envionment specific API properties request body
  property_count: 0
  slug: publisher-api-environment-properties
- name: Environment
  property_count: 13
  slug: publisher-api-environment
- name: Event Count Limit object
  property_count: 1
  slug: publisher-api-event-count-limit
- name: External Store List
  property_count: 2
  slug: publisher-api-external-store-list
- name: External Store
  property_count: 4
  slug: publisher-api-external-store
- name: File Information including meta data
  property_count: 2
  slug: publisher-api-file-info
- name: Gateway Environment protocols and URIs
  property_count: 2
  slug: publisher-api-gateway-environment-protocol-uri
- name: Details to map, deploy, undeploy policy mappings to gateways
  property_count: 3
  slug: publisher-api-gateway-policy-deployment
- name: Gateway Policy Mapping List
  property_count: 3
  slug: publisher-api-gateway-policy-mapping-data-list
- name: Gateway Policy Mapping and Deployment Information
  property_count: 4
  slug: publisher-api-gateway-policy-mapping-deployment-info
- name: Gateway Policy Mapping Information
  property_count: 3
  slug: publisher-api-gateway-policy-mapping-info
- name: Gateway Policy Mappings
  property_count: 5
  slug: publisher-api-gateway-policy-mappings
- name: GraphQL Custom Complexity Info
  property_count: 3
  slug: publisher-api-graph-ql-custom-complexity-info
- name: GraphQL Query Complexity Info
  property_count: 1
  slug: publisher-api-graph-ql-query-complexity-info
- name: GraphQL Query
  property_count: 2
  slug: publisher-api-graph-ql-query
- name: GraphQL Schema
  property_count: 2
  slug: publisher-api-graph-ql-schema
- name: List of types and corresponding fields of the GraphQL Schema
  property_count: 1
  slug: publisher-api-graph-ql-schema-type-list
- name: Single type and corresponding fields found within the GraphQL Schema
  property_count: 2
  slug: publisher-api-graph-ql-schema-type
- name: GraphQL API definition validation Response
  property_count: 3
  slug: publisher-api-graph-ql-validation-response
- name: Import API Response
  property_count: 2
  slug: publisher-api-import-api-response
- name: IntegratedAPIResponse
  property_count: 3
  slug: publisher-api-integrated-api-response
- name: Key Manager Info
  property_count: 7
  slug: publisher-api-key-manager-info
- name: Key Manager List
  property_count: 2
  slug: publisher-api-key-manager-list
- name: Label List
  property_count: 3
  slug: publisher-api-label-list
- name: Label
  property_count: 3
  slug: publisher-api-label
- name: Lifecycle history item
  property_count: 4
  slug: publisher-api-lifecycle-history-item
- name: Lifecycle history item list
  property_count: 2
  slug: publisher-api-lifecycle-history
- name: Lifecycle State
  property_count: 3
  slug: publisher-api-lifecycle-state
- name: LLMProviderEndpointConfiguration
  property_count: 2
  slug: publisher-api-llm-provider-endpoint-configuration
- name: LLMProviderResponse
  property_count: 7
  slug: publisher-api-llm-provider-response
- name: LLMProviderSummaryResponseList
  property_count: 2
  slug: publisher-api-llm-provider-summary-response-list
- name: LLMProviderSummaryResponse
  property_count: 5
  slug: publisher-api-llm-provider-summary-response
- name: MaxTps
  property_count: 4
  slug: publisher-api-max-tps
- name: MCP Server metadata List
  property_count: 2
  slug: publisher-api-mcp-server-metadata-list
- name: MCP Server Info object with basic minimal details.
  property_count: 5
  slug: publisher-api-mcp-server-metadata
- name: MCP Server Operation Level Policies
  property_count: 3
  slug: publisher-api-mcp-server-operation-policies
- name: MCPServerOperation
  property_count: 13
  slug: publisher-api-mcp-server-operation
- name: MCP Server object
  property_count: 51
  slug: publisher-api-mcp-server
- name: MCPServerScope
  property_count: 2
  slug: publisher-api-mcp-server-scope
- name: MCP URL Validation Request
  property_count: 2
  slug: publisher-api-mcp-server-validation-request
- name: MCP Server validation Response
  property_count: 4
  slug: publisher-api-mcp-server-validation-response
- name: Mediation Policy
  property_count: 4
  slug: publisher-api-mediation-policy
- name: Mock Response Payload info object
  property_count: 3
  slug: publisher-api-mock-response-payload-info
- name: Mock Response Payload list
  property_count: 1
  slug: publisher-api-mock-response-payload-list
- name: Model Provider
  property_count: 2
  slug: publisher-api-model-provider
- name: Monetization attribute object
  property_count: 6
  slug: publisher-api-monetization-attribute
- name: API monetization details object
  property_count: 2
  slug: publisher-api-monetization-info
- name: OpenAPI Definition Validation Response
  property_count: 4
  slug: publisher-api-open-api-definition-validation-response
- name: Operation policy List
  property_count: 3
  slug: publisher-api-operation-policy-data-list
- name: Operation Policy Data
  property_count: 12
  slug: publisher-api-operation-policy-data
- name: API Operation Policy
  property_count: 5
  slug: publisher-api-operation-policy
- name: OperationPolicySpecAttribute
  property_count: 8
  slug: publisher-api-operation-policy-spec-attribute
- name: Organization Info
  property_count: 2
  slug: publisher-api-organization-info
- name: Organization List
  property_count: 2
  slug: publisher-api-organization-list
- name: Organization based Subscription Policies
  property_count: 2
  slug: publisher-api-organization-policies
- name: Organization
  property_count: 5
  slug: publisher-api-organization
- name: Pagination
  property_count: 5
  slug: publisher-api-pagination
- name: ProductAPI
  property_count: 4
  slug: publisher-api-product-api
- name: Request Count Limit object
  property_count: 1
  slug: publisher-api-request-count-limit
- name: Label ID List for Request
  property_count: 1
  slug: publisher-api-request-label-list
- name: ResourcePath List
  property_count: 3
  slug: publisher-api-resource-path-list
- name: ResourcePath
  property_count: 3
  slug: publisher-api-resource-path
- name: Resource policy Info object with conversion policy resource details.
  property_count: 4
  slug: publisher-api-resource-policy-info
- name: Resource policy List
  property_count: 2
  slug: publisher-api-resource-policy-list
- name: Scope List
  property_count: 3
  slug: publisher-api-scope-list
- name: Scope
  property_count: 6
  slug: publisher-api-scope
- name: Unified Search Result List
  property_count: 3
  slug: publisher-api-search-result-list
- name: Search Result
  property_count: 4
  slug: publisher-api-search-result
- name: SecurityAuditAttributeDTO
  property_count: 5
  slug: publisher-api-security-audit-attribute
- name: MCP Server Security Information
  property_count: 3
  slug: publisher-api-security-info
- name: Sequence Backend List
  property_count: 2
  slug: publisher-api-sequence-backend-list
- name: Sequence Backend
  property_count: 4
  slug: publisher-api-sequence-backend
- name: SettingsDTO
  property_count: 24
  slug: publisher-api-settings
- name: Entity using shared scope
  property_count: 7
  slug: publisher-api-shared-scope-usage-entity
- name: SharedScopeUsage
  property_count: 4
  slug: publisher-api-shared-scope-usage
- name: API object using shared scope
  property_count: 6
  slug: publisher-api-shared-scope-used-api-info
- name: API resource object using shared scope
  property_count: 2
  slug: publisher-api-shared-scope-used-api-resource-info
- name: Resource object using shared scope
  property_count: 2
  slug: publisher-api-shared-scope-used-resource-info
- name: Subscriber Contact attribute object
  property_count: 2
  slug: publisher-api-subscriber-contact-attribute
- name: SubscriberInfo
  property_count: 2
  slug: publisher-api-subscriber-info
- name: Subscription List
  property_count: 3
  slug: publisher-api-subscription-list
- name: Subscription policy list
  property_count: 3
  slug: publisher-api-subscription-policy-list
- name: Subscription Throttling Policy
  property_count: 16
  slug: publisher-api-subscription-policy
- name: Subscription
  property_count: 4
  slug: publisher-api-subscription
- name: SubscriptionThrottlePolicyPermission
  property_count: 2
  slug: publisher-api-subscription-throttle-policy-permission
- name: SubtypeConfiguration
  property_count: 2
  slug: publisher-api-subtype-configuration
- name: Tenant list
  property_count: 3
  slug: publisher-api-tenant-list
- name: Tenant
  property_count: 2
  slug: publisher-api-tenant
- name: Threat Protection Policy List
  property_count: 1
  slug: publisher-api-threat-protection-policy-list
- name: Threat Protection Policy Schema
  property_count: 4
  slug: publisher-api-threat-protection-policy
- name: Throttle Limit Base
  property_count: 2
  slug: publisher-api-throttle-limit-base
- name: Throttle Limit
  property_count: 4
  slug: publisher-api-throttle-limit
- name: Generic Throttling Policy
  property_count: 6
  slug: publisher-api-throttle-policy
- name: Throttling policy list
  property_count: 3
  slug: publisher-api-throttling-policy-list
- name: Tier
  property_count: 18
  slug: publisher-api-throttling-policy
- name: Topic List
  property_count: 3
  slug: publisher-api-topic-list
- name: Topic object
  property_count: 4
  slug: publisher-api-topic
- name: Virtual Host
  property_count: 10
  slug: publisher-api-v-host
- name: WebsubSubscriptionConfiguration
  property_count: 4
  slug: publisher-api-websub-subscription-configuration
- name: Workflow info object with basic workflow details
  property_count: 7
  slug: publisher-api-workflow-info
- name: WorkflowList
  property_count: 4
  slug: publisher-api-workflow-list
- name: workflow Response
  property_count: 3
  slug: publisher-api-workflow-response
- name: workflow
  property_count: 3
  slug: publisher-api-workflow
- name: WSDL information of the API. This is only available if the API is a SOAP API.
  property_count: 1
  slug: publisher-api-wsdl-info
- name: WSDL Definition Validation Response
  property_count: 3
  slug: publisher-api-wsdl-validation-response
- name: API Info object with basic API details.
  property_count: 6
  slug: service-catalog-api-api-info
- name: API List
  property_count: 2
  slug: service-catalog-api-api-list
- name: Pagination
  property_count: 5
  slug: service-catalog-api-pagination
- name: Services List
  property_count: 2
  slug: service-catalog-api-service-info-list
- name: The Service Info object
  property_count: 5
  slug: service-catalog-api-service-info
- name: Services List
  property_count: 3
  slug: service-catalog-api-service-list-expanded
- name: Paginated List of Services in Service Catalog
  property_count: 2
  slug: service-catalog-api-service-list
- name: The Service Schema object
  property_count: 3
  slug: service-catalog-api-service-schema
- name: The Service Object
  property_count: 14
  slug: service-catalog-api-service
- name: SettingsDTO
  property_count: 1
  slug: service-catalog-api-settings
- name: Json array of md5 hash values of Service Catalog Entry objects
  property_count: 2
  slug: service-catalog-api-verifier
- name: Additional Subscription Info List
  property_count: 3
  slug: wso2-additional-subscription-info-list
- name: Advanced Throttling Policy List
  property_count: 2
  slug: wso2-advanced-throttle-policy-list
- name: Advanced Throttling Policy
  property_count: 8
  slug: wso2-advanced-throttle-policy
- name: AIServiceProvider
  property_count: 7
  slug: wso2-aiservice-provider-request
- name: AIServiceProviderResponse
  property_count: 10
  slug: wso2-aiservice-provider-response
- name: AIServiceProviderSummaryResponseList
  property_count: 2
  slug: wso2-aiservice-provider-summary-response-list
- name: Alert Types List
  property_count: 2
  slug: wso2-alert-types-list
- name: Alerts Subscription
  property_count: 2
  slug: wso2-alerts-subscription
- name: API Chat request
  property_count: 4
  slug: wso2-api-chat-request
- name: API Chat response
  property_count: 5
  slug: wso2-api-chat-response
- name: API object
  property_count: 40
  slug: wso2-api
- name: API Key generation request object
  property_count: 4
  slug: wso2-apiapikey-generate-request
- name: API Artifact Response
  property_count: 1
  slug: wso2-apiartifact
- name: API Category List
  property_count: 2
  slug: wso2-apicategory-list
- name: API Category
  property_count: 4
  slug: wso2-apicategory
- name: API Info List
  property_count: 2
  slug: wso2-apiinfo-list
- name: Subscription Information for API.
  property_count: 12
  slug: wso2-apiinfo
- name: API Key details to invoke APIs
  property_count: 3
  slug: wso2-apikey-2
- name: API Key association
  property_count: 3
  slug: wso2-apikey-association
- name: API Key generation request object
  property_count: 3
  slug: wso2-apikey-generate-request
- name: API Key revoke request object
  property_count: 2
  slug: wso2-apikey-revoke-request-2
- name: API List
  property_count: 2
  slug: wso2-apilist
- name: APIMGovernancePolicyList
  property_count: 3
  slug: wso2-apimgovernance-policy-list
- name: APIMGovernancePolicy
  property_count: 11
  slug: wso2-apimgovernance-policy
- name: API monetization usage object
  property_count: 1
  slug: wso2-apimonetization-usage
- name: API Key association request object
  property_count: 2
  slug: wso2-app-apikey-associate-request
- name: Application
  property_count: 16
  slug: wso2-application-2
- name: Application Attributes List
  property_count: 2
  slug: wso2-application-attribute-list
- name: Application info object with basic application details
  property_count: 12
  slug: wso2-application-info
- name: Application key generation request object
  property_count: 9
  slug: wso2-application-key-generate-request
- name: Application Keys List
  property_count: 2
  slug: wso2-application-key-list
- name: Application key provision request object
  property_count: 4
  slug: wso2-application-key-mapping-request
- name: Application key details after re generating consumer secret
  property_count: 2
  slug: wso2-application-key-re-generate-response
- name: Application key details
  property_count: 13
  slug: wso2-application-key
- name: Application List
  property_count: 3
  slug: wso2-application-list
- name: Application object with all the application details
  property_count: 11
  slug: wso2-application
- name: Application Level Throttling Policy List
  property_count: 2
  slug: wso2-application-throttle-policy-list
- name: Application Throttling Policy
  property_count: 8
  slug: wso2-application-throttle-policy
- name: Reset application level throttling
  property_count: 1
  slug: wso2-application-throttle-reset
- name: Application access token generation request object
  property_count: 6
  slug: wso2-application-token-generate-request
- name: Application token details to invoke APIs
  property_count: 3
  slug: wso2-application-token
- name: ApplicationUpdateRequest
  property_count: 2
  slug: wso2-application-update-request
- name: ArtifactComplianceDetails
  property_count: 4
  slug: wso2-artifact-compliance-details
- name: ArtifactComplianceList
  property_count: 3
  slug: wso2-artifact-compliance-list
- name: ArtifactComplianceSummary
  property_count: 5
  slug: wso2-artifact-compliance-summary
- name: Blocking Conditions List
  property_count: 2
  slug: wso2-blocking-condition-list
- name: Blocking Conditions
  property_count: 4
  slug: wso2-blocking-condition
- name: Blocking Conditions Status
  property_count: 2
  slug: wso2-blocking-condition-status
- name: Bot Detection Alert Subscription List
  property_count: 2
  slug: wso2-bot-detection-alert-subscription-list
- name: Bot Detection Alert Subscription
  property_count: 2
  slug: wso2-bot-detection-alert-subscription
- name: Bot Detection Data List
  property_count: 2
  slug: wso2-bot-detection-data-list
- name: Comments List
  property_count: 3
  slug: wso2-comment-list
- name: Comment
  property_count: 10
  slug: wso2-comment
- name: ConsumerSecretCreationRequest
  property_count: 1
  slug: wso2-consumer-secret-creation-request
- name: ConsumerSecretDeletionRequest
  property_count: 2
  slug: wso2-consumer-secret-deletion-request
- name: Client Secret List
  property_count: 2
  slug: wso2-consumer-secret-list
- name: ConsumerSecret
  property_count: 3
  slug: wso2-consumer-secret
- name: ContentPublishStatusResponse
  property_count: 2
  slug: wso2-content-publish-status-response
- name: ContentPublishStatus
  property_count: 1
  slug: wso2-content-publish-status
- name: correlation-components
  property_count: 1
  slug: wso2-correlation-components-list
- name: Create Platform Gateway Request
  property_count: 6
  slug: wso2-create-platform-gateway-request
- name: Current and new passowrd of the user
  property_count: 2
  slug: wso2-current-and-new-passwords
- name: Custom Rule List
  property_count: 2
  slug: wso2-custom-rule-list
- name: Custom Rule
  property_count: 8
  slug: wso2-custom-rule
- name: Custom url information
  property_count: 4
  slug: wso2-custom-url-info
- name: DCR
  property_count: 7
  slug: wso2-dcr
- name: DCRResult
  property_count: 10
  slug: wso2-dcrresult
- name: Deploy API Response
  property_count: 2
  slug: wso2-deploy-response
- name: Document List
  property_count: 3
  slug: wso2-document-list
- name: Document
  property_count: 7
  slug: wso2-document
- name: Endpoints Response
  property_count: 1
  slug: wso2-endpoints
- name: Environment List
  property_count: 2
  slug: wso2-environment-list
- name: Environment
  property_count: 17
  slug: wso2-environment
- name: Export Throttling Policy
  property_count: 4
  slug: wso2-export-throttle-policy
- name: Gateway instance list
  property_count: 2
  slug: wso2-gateway-instance-list
- name: Gateway List
  property_count: 2
  slug: wso2-gateway-list
- name: Gateway Response With Token
  property_count: 11
  slug: wso2-gateway-response-with-token
- name: GraphQL Query Complexity Info
  property_count: 1
  slug: wso2-graph-qlquery-complexity-info
- name: List of types and corresponding fields of the GraphQL Schema
  property_count: 1
  slug: wso2-graph-qlschema-type-list
- name: Key Manager API Usages.
  property_count: 2
  slug: wso2-key-manager-apiusages
- name: Key Manager Application Usages.
  property_count: 2
  slug: wso2-key-manager-app-usages
- name: Key Manager List
  property_count: 2
  slug: wso2-key-manager-list
- name: Key Manager
  property_count: 36
  slug: wso2-key-manager
- name: Key Manager Well-Known Response.
  property_count: 2
  slug: wso2-key-manager-well-known-response
- name: Label List
  property_count: 3
  slug: wso2-label-list
- name: Label
  property_count: 3
  slug: wso2-label
- name: Label Usage
  property_count: 1
  slug: wso2-label-usage
- name: LLMProvider
  property_count: 6
  slug: wso2-llmprovider-request
- name: LLMProviderResponse
  property_count: 8
  slug: wso2-llmprovider-response
- name: LLMProviderSummaryResponseList
  property_count: 2
  slug: wso2-llmprovider-summary-response-list
- name: LocalEntry Response
  property_count: 1
  slug: wso2-local-entry
- name: API Info object with log details
  property_count: 3
  slug: wso2-logging-api-input
- name: apis
  property_count: 1
  slug: wso2-logging-api-output-list
- name: MarketplaceAssistantApiCountResponse
  property_count: 2
  slug: wso2-marketplace-assistant-api-count-response
- name: MarketplaceAssistantRequest
  property_count: 2
  slug: wso2-marketplace-assistant-request
- name: MarketplaceAssistantResponse
  property_count: 2
  slug: wso2-marketplace-assistant-response
- name: Usage publish status
  property_count: 4
  slug: wso2-monetization-usage-publish-info
- name: Organization Info
  property_count: 2
  slug: wso2-organization-info
- name: Organization List
  property_count: 2
  slug: wso2-organization-list
- name: Organization
  property_count: 5
  slug: wso2-organization
- name: Patch request body
  property_count: 2
  slug: wso2-patch-request-body
- name: Platform Gateway Response
  property_count: 10
  slug: wso2-platform-gateway-response
- name: PolicyAdherenceDetails
  property_count: 4
  slug: wso2-policy-adherence-details
- name: PolicyAdherenceList
  property_count: 3
  slug: wso2-policy-adherence-list
- name: PolicyAdherenceSummary
  property_count: 4
  slug: wso2-policy-adherence-summary
- name: Post request body
  property_count: 2
  slug: wso2-post-request-body
- name: Usage publish status
  property_count: 2
  slug: wso2-publish-status
- name: Rating List
  property_count: 5
  slug: wso2-rating-list
- name: Rating
  property_count: 4
  slug: wso2-rating
- name: API recommendations
  property_count: 2
  slug: wso2-recommendations
- name: Role alias list
  property_count: 2
  slug: wso2-role-alias-list
- name: RulesetInfo
  property_count: 12
  slug: wso2-ruleset-info
- name: RulesetInput
  property_count: 8
  slug: wso2-ruleset-input
- name: RulesetList
  property_count: 3
  slug: wso2-ruleset-list
- name: RulesetValidationResult
  property_count: 5
  slug: wso2-ruleset-validation-result
- name: Scope Role Mapping List
  property_count: 2
  slug: wso2-scope-list
- name: Settings
  property_count: 1
  slug: wso2-scope-settings
- name: Unified Search Result List
  property_count: 3
  slug: wso2-search-result-list
- name: Sequences Response
  property_count: 1
  slug: wso2-sequences
- name: Services List
  property_count: 2
  slug: wso2-service-info-list
- name: Paginated List of Services in Service Catalog
  property_count: 2
  slug: wso2-service-list
- name: The Service Schema object
  property_count: 3
  slug: wso2-service-schema
- name: The Service Object
  property_count: 14
  slug: wso2-service
- name: Settings
  property_count: 11
  slug: wso2-settings
- name: Subscription List
  property_count: 3
  slug: wso2-subscription-list
- name: Subscription
  property_count: 5
  slug: wso2-subscription
- name: Subscription Level Throttling Policy List
  property_count: 2
  slug: wso2-subscription-throttle-policy-list
- name: Subscription Throttling Policy
  property_count: 17
  slug: wso2-subscription-throttle-policy
- name: Tag List
  property_count: 3
  slug: wso2-tag-list
- name: Tenant information
  property_count: 3
  slug: wso2-tenant-info
- name: Tenant list
  property_count: 3
  slug: wso2-tenant-list
- name: Policy List
  property_count: 2
  slug: wso2-throttle-policy-details-list
- name: Throttling Policy List
  property_count: 3
  slug: wso2-throttling-policy-list
- name: Throttling Policy
  property_count: 15
  slug: wso2-throttling-policy
- name: Topic List
  property_count: 3
  slug: wso2-topic-list
- name: TransactionCount
  property_count: 1
  slug: wso2-transaction-count
- name: Update Platform Gateway Request
  property_count: 6
  slug: wso2-update-platform-gateway-request
- name: Subscribed Webhook List
  property_count: 3
  slug: wso2-webhook-subscription-list
- name: Workflow info object with basic workflow details
  property_count: 7
  slug: wso2-workflow-info
- name: WorkflowList
  property_count: 4
  slug: wso2-workflow-list
- name: workflow Response
  property_count: 2
  slug: wso2-workflow-response
- name: workflow
  property_count: 3
  slug: wso2-workflow
json_structures:
- name: Admin Api Additional Property Structure
  property_count: 2
  slug: admin-api-additional-property-structure
- name: Admin Api Advanced Throttle Policy Info Structure
  property_count: 0
  slug: admin-api-advanced-throttle-policy-info-structure
- name: Admin Api Advanced Throttle Policy List Structure
  property_count: 2
  slug: admin-api-advanced-throttle-policy-list-structure
- name: Admin Api Advanced Throttle Policy Structure
  property_count: 0
  slug: admin-api-advanced-throttle-policy-structure
- name: Admin Api Ai Service Provider Request Structure
  property_count: 7
  slug: admin-api-ai-service-provider-request-structure
- name: Admin Api Ai Service Provider Response Structure
  property_count: 10
  slug: admin-api-ai-service-provider-response-structure
- name: Admin Api Ai Service Provider Summary Response List Structure
  property_count: 2
  slug: admin-api-ai-service-provider-summary-response-list-structure
- name: Admin Api Ai Service Provider Summary Response Structure
  property_count: 6
  slug: admin-api-ai-service-provider-summary-response-structure
- name: Admin Api Aiapi Quota Limit Structure
  property_count: 0
  slug: admin-api-aiapi-quota-limit-structure
- name: Admin Api Alert Type Structure
  property_count: 2
  slug: admin-api-alert-type-structure
- name: Admin Api Alert Types List Structure
  property_count: 2
  slug: admin-api-alert-types-list-structure
- name: Admin Api Alerts Subscription Structure
  property_count: 2
  slug: admin-api-alerts-subscription-structure
- name: Admin Api Api Category List Structure
  property_count: 2
  slug: admin-api-api-category-list-structure
- name: Admin Api Api Category Structure
  property_count: 4
  slug: admin-api-api-category-structure
- name: Admin Api Api Info Key Manager Structure
  property_count: 12
  slug: admin-api-api-info-key-manager-structure
- name: Admin Api Api Info List Structure
  property_count: 2
  slug: admin-api-api-info-list-structure
- name: Admin Api Api Info Structure
  property_count: 4
  slug: admin-api-api-info-structure
- name: Admin Api Api Key List Structure
  property_count: 2
  slug: admin-api-api-key-list-structure
- name: Admin Api Api Key Revoke Request Structure
  property_count: 1
  slug: admin-api-api-key-revoke-request-structure
- name: Admin Api Api Key Structure
  property_count: 9
  slug: admin-api-api-key-structure
- name: Admin Api Api Result Structure
  property_count: 4
  slug: admin-api-api-result-structure
- name: Admin Api Application Info Key Manager Structure
  property_count: 5
  slug: admin-api-application-info-key-manager-structure
- name: Admin Api Application Info Structure
  property_count: 8
  slug: admin-api-application-info-structure
- name: Admin Api Application List Structure
  property_count: 3
  slug: admin-api-application-list-structure
- name: Admin Api Application Structure
  property_count: 11
  slug: admin-api-application-structure
- name: Admin Api Application Throttle Policy List Structure
  property_count: 2
  slug: admin-api-application-throttle-policy-list-structure
- name: Admin Api Application Throttle Policy Structure
  property_count: 0
  slug: admin-api-application-throttle-policy-structure
- name: Admin Api Application Update Request Structure
  property_count: 2
  slug: admin-api-application-update-request-structure
- name: Admin Api Bandwidth Limit Structure
  property_count: 0
  slug: admin-api-bandwidth-limit-structure
- name: Admin Api Blocking Condition List Structure
  property_count: 2
  slug: admin-api-blocking-condition-list-structure
- name: Admin Api Blocking Condition Status Structure
  property_count: 2
  slug: admin-api-blocking-condition-status-structure
- name: Admin Api Blocking Condition Structure
  property_count: 4
  slug: admin-api-blocking-condition-structure
- name: Admin Api Bot Detection Alert Subscription List Structure
  property_count: 2
  slug: admin-api-bot-detection-alert-subscription-list-structure
- name: Admin Api Bot Detection Alert Subscription Structure
  property_count: 2
  slug: admin-api-bot-detection-alert-subscription-structure
- name: Admin Api Bot Detection Data List Structure
  property_count: 2
  slug: admin-api-bot-detection-data-list-structure
- name: Admin Api Bot Detection Data Structure
  property_count: 6
  slug: admin-api-bot-detection-data-structure
- name: Admin Api Burst Limit Structure
  property_count: 2
  slug: admin-api-burst-limit-structure
- name: Admin Api Claim Mapping Entry Structure
  property_count: 2
  slug: admin-api-claim-mapping-entry-structure
- name: Admin Api Conditional Group Structure
  property_count: 3
  slug: admin-api-conditional-group-structure
- name: Admin Api Configuration Constraint Structure
  property_count: 8
  slug: admin-api-configuration-constraint-structure
- name: Admin Api Content Publish Status Response Structure
  property_count: 2
  slug: admin-api-content-publish-status-response-structure
- name: Admin Api Content Publish Status Structure
  property_count: 1
  slug: admin-api-content-publish-status-structure
- name: Admin Api Create Platform Gateway Request Structure
  property_count: 6
  slug: admin-api-create-platform-gateway-request-structure
- name: Admin Api Custom Attribute Structure
  property_count: 2
  slug: admin-api-custom-attribute-structure
- name: Admin Api Custom Rule List Structure
  property_count: 2
  slug: admin-api-custom-rule-list-structure
- name: Admin Api Custom Rule Structure
  property_count: 0
  slug: admin-api-custom-rule-structure
- name: Admin Api Custom Url Info Structure
  property_count: 4
  slug: admin-api-custom-url-info-structure
- name: Admin Api Environment List Structure
  property_count: 2
  slug: admin-api-environment-list-structure
- name: Admin Api Environment Structure
  property_count: 17
  slug: admin-api-environment-structure
- name: Admin Api Event Count Limit Structure
  property_count: 0
  slug: admin-api-event-count-limit-structure
- name: Admin Api Export Throttle Policy Structure
  property_count: 4
  slug: admin-api-export-throttle-policy-structure
- name: Admin Api File Info Structure
  property_count: 2
  slug: admin-api-file-info-structure
- name: Admin Api Gateway Configuration Structure
  property_count: 9
  slug: admin-api-gateway-configuration-structure
- name: Admin Api Gateway Environment Protocol Uri Structure
  property_count: 2
  slug: admin-api-gateway-environment-protocol-uri-structure
- name: Admin Api Gateway Instance List Structure
  property_count: 2
  slug: admin-api-gateway-instance-list-structure
- name: Admin Api Gateway Instance Structure
  property_count: 3
  slug: admin-api-gateway-instance-structure
- name: Admin Api Gateway List Structure
  property_count: 2
  slug: admin-api-gateway-list-structure
- name: Admin Api Gateway Response With Token Structure
  property_count: 0
  slug: admin-api-gateway-response-with-token-structure
- name: Admin Api Graph Ql Query Structure
  property_count: 2
  slug: admin-api-graph-ql-query-structure
- name: Admin Api Header Condition Structure
  property_count: 2
  slug: admin-api-header-condition-structure
- name: Admin Api Ip Condition Structure
  property_count: 4
  slug: admin-api-ip-condition-structure
- name: Admin Api Jwt Claims Condition Structure
  property_count: 2
  slug: admin-api-jwt-claims-condition-structure
- name: Admin Api Key Manager Api Usages Structure
  property_count: 2
  slug: admin-api-key-manager-api-usages-structure
- name: Admin Api Key Manager App Usages Structure
  property_count: 2
  slug: admin-api-key-manager-app-usages-structure
- name: Admin Api Key Manager Configuration Structure
  property_count: 10
  slug: admin-api-key-manager-configuration-structure
- name: Admin Api Key Manager Endpoint Structure
  property_count: 2
  slug: admin-api-key-manager-endpoint-structure
- name: Admin Api Key Manager Info Structure
  property_count: 8
  slug: admin-api-key-manager-info-structure
- name: Admin Api Key Manager List Structure
  property_count: 2
  slug: admin-api-key-manager-list-structure
- name: Admin Api Key Manager Structure
  property_count: 36
  slug: admin-api-key-manager-structure
- name: Admin Api Key Manager Well Known Response Structure
  property_count: 2
  slug: admin-api-key-manager-well-known-response-structure
- name: Admin Api Label List Structure
  property_count: 3
  slug: admin-api-label-list-structure
- name: Admin Api Label Structure
  property_count: 3
  slug: admin-api-label-structure
- name: Admin Api Label Usage Structure
  property_count: 1
  slug: admin-api-label-usage-structure
- name: Admin Api Llm Provider Request Structure
  property_count: 6
  slug: admin-api-llm-provider-request-structure
- name: Admin Api Llm Provider Response Structure
  property_count: 8
  slug: admin-api-llm-provider-response-structure
- name: Admin Api Llm Provider Summary Response List Structure
  property_count: 2
  slug: admin-api-llm-provider-summary-response-list-structure
- name: Admin Api Llm Provider Summary Response Structure
  property_count: 5
  slug: admin-api-llm-provider-summary-response-structure
- name: Admin Api Model Provider Structure
  property_count: 2
  slug: admin-api-model-provider-structure
- name: Admin Api Monetization Info Structure
  property_count: 2
  slug: admin-api-monetization-info-structure
- name: Admin Api Monetization Usage Publish Info Structure
  property_count: 4
  slug: admin-api-monetization-usage-publish-info-structure
- name: Admin Api Organization Info Structure
  property_count: 2
  slug: admin-api-organization-info-structure
- name: Admin Api Organization List Structure
  property_count: 2
  slug: admin-api-organization-list-structure
- name: Admin Api Organization Structure
  property_count: 5
  slug: admin-api-organization-structure
- name: Admin Api Pagination Apis Structure
  property_count: 5
  slug: admin-api-pagination-apis-structure
- name: Admin Api Pagination Structure
  property_count: 5
  slug: admin-api-pagination-structure
- name: Admin Api Platform Gateway Response Structure
  property_count: 10
  slug: admin-api-platform-gateway-response-structure
- name: Admin Api Publish Status Structure
  property_count: 2
  slug: admin-api-publish-status-structure
- name: Admin Api Query Parameter Condition Structure
  property_count: 2
  slug: admin-api-query-parameter-condition-structure
- name: Admin Api Request Count Limit Structure
  property_count: 0
  slug: admin-api-request-count-limit-structure
- name: Admin Api Role Alias List Structure
  property_count: 2
  slug: admin-api-role-alias-list-structure
- name: Admin Api Role Alias Structure
  property_count: 2
  slug: admin-api-role-alias-structure
- name: Admin Api Scope Info Structure
  property_count: 4
  slug: admin-api-scope-info-structure
- name: Admin Api Scope List Structure
  property_count: 2
  slug: admin-api-scope-list-structure
- name: Admin Api Scope Settings Structure
  property_count: 1
  slug: admin-api-scope-settings-structure
- name: Admin Api Scope Structure
  property_count: 4
  slug: admin-api-scope-structure
- name: Admin Api Search Result List Structure
  property_count: 3
  slug: admin-api-search-result-list-structure
- name: Admin Api Settings Structure
  property_count: 11
  slug: admin-api-settings-structure
- name: Admin Api Subscription Throttle Policy List Structure
  property_count: 2
  slug: admin-api-subscription-throttle-policy-list-structure
- name: Admin Api Subscription Throttle Policy Permission Structure
  property_count: 2
  slug: admin-api-subscription-throttle-policy-permission-structure
- name: Admin Api Subscription Throttle Policy Structure
  property_count: 0
  slug: admin-api-subscription-throttle-policy-structure
- name: Admin Api Tenant Info Structure
  property_count: 3
  slug: admin-api-tenant-info-structure
- name: Admin Api Throttle Condition Structure
  property_count: 6
  slug: admin-api-throttle-condition-structure
- name: Admin Api Throttle Limit Base Structure
  property_count: 2
  slug: admin-api-throttle-limit-base-structure
- name: Admin Api Throttle Limit Structure
  property_count: 5
  slug: admin-api-throttle-limit-structure
- name: Admin Api Throttle Policy Details List Structure
  property_count: 2
  slug: admin-api-throttle-policy-details-list-structure
- name: Admin Api Throttle Policy Details Structure
  property_count: 7
  slug: admin-api-throttle-policy-details-structure
- name: Admin Api Throttle Policy List Structure
  property_count: 3
  slug: admin-api-throttle-policy-list-structure
- name: Admin Api Throttle Policy Structure
  property_count: 6
  slug: admin-api-throttle-policy-structure
- name: Admin Api Token Validation Structure
  property_count: 4
  slug: admin-api-token-validation-structure
- name: Admin Api Transaction Count Structure
  property_count: 1
  slug: admin-api-transaction-count-structure
- name: Admin Api Update Platform Gateway Request Structure
  property_count: 6
  slug: admin-api-update-platform-gateway-request-structure
- name: Admin Api V Host Structure
  property_count: 8
  slug: admin-api-v-host-structure
- name: Admin Api Workflow Info Structure
  property_count: 7
  slug: admin-api-workflow-info-structure
- name: Admin Api Workflow List Structure
  property_count: 4
  slug: admin-api-workflow-list-structure
- name: Admin Api Workflow Response Structure
  property_count: 2
  slug: admin-api-workflow-response-structure
- name: Admin Api Workflow Structure
  property_count: 3
  slug: admin-api-workflow-structure
- name: Dcr Api Dcr Result Structure
  property_count: 10
  slug: dcr-api-dcr-result-structure
- name: Dcr Api Dcr Structure
  property_count: 7
  slug: dcr-api-dcr-structure
- name: Devops Api Correlation Component Property Structure
  property_count: 2
  slug: devops-api-correlation-component-property-structure
- name: Devops Api Correlation Component Structure
  property_count: 3
  slug: devops-api-correlation-component-structure
- name: Devops Api Correlation Components List Structure
  property_count: 1
  slug: devops-api-correlation-components-list-structure
- name: Devops Api Logging Api Input Structure
  property_count: 3
  slug: devops-api-logging-api-input-structure
- name: Devops Api Logging Api Output List Structure
  property_count: 1
  slug: devops-api-logging-api-output-list-structure
- name: Devops Api Logging Api Output Structure
  property_count: 5
  slug: devops-api-logging-api-output-structure
- name: Devportal Api Additional Subscription Info List Structure
  property_count: 3
  slug: devportal-api-additional-subscription-info-list-structure
- name: Devportal Api Additional Subscription Info Structure
  property_count: 7
  slug: devportal-api-additional-subscription-info-structure
- name: Devportal Api Advertise Info Structure
  property_count: 6
  slug: devportal-api-advertise-info-structure
- name: Devportal Api Api Business Information Structure
  property_count: 4
  slug: devportal-api-api-business-information-structure
- name: Devportal Api Api Category List Structure
  property_count: 2
  slug: devportal-api-api-category-list-structure
- name: Devportal Api Api Category Structure
  property_count: 3
  slug: devportal-api-api-category-structure
- name: Devportal Api Api Chat Request Structure
  property_count: 4
  slug: devportal-api-api-chat-request-structure
- name: Devportal Api Api Chat Response Structure
  property_count: 5
  slug: devportal-api-api-chat-response-structure
- name: Devportal Api Api Definition Search Result Structure
  property_count: 0
  slug: devportal-api-api-definition-search-result-structure
- name: Devportal Api Api Info List Structure
  property_count: 2
  slug: devportal-api-api-info-list-structure
- name: Devportal Api Api Info Structure
  property_count: 23
  slug: devportal-api-api-info-structure
- name: Devportal Api Api Key Association Info Structure
  property_count: 7
  slug: devportal-api-api-key-association-info-structure
- name: Devportal Api Api Key Association List Structure
  property_count: 2
  slug: devportal-api-api-key-association-list-structure
- name: Devportal Api Api Key Association Structure
  property_count: 3
  slug: devportal-api-api-key-association-structure
- name: Devportal Api Api Key Dissociate Request Structure
  property_count: 1
  slug: devportal-api-api-key-dissociate-request-structure
- name: Devportal Api Api Key Generate Request Structure
  property_count: 3
  slug: devportal-api-api-key-generate-request-structure
- name: Devportal Api Api Key Info Structure
  property_count: 5
  slug: devportal-api-api-key-info-structure
- name: Devportal Api Api Key List Structure
  property_count: 2
  slug: devportal-api-api-key-list-structure
- name: Devportal Api Api Key Renew Request Structure
  property_count: 1
  slug: devportal-api-api-key-renew-request-structure
- name: Devportal Api Api Key Revoke Request Structure
  property_count: 2
  slug: devportal-api-api-key-revoke-request-structure
- name: Devportal Api Api Key Structure
  property_count: 3
  slug: devportal-api-api-key-structure
- name: Devportal Api Api List Structure
  property_count: 3
  slug: devportal-api-api-list-structure
- name: Devportal Api Api Monetization Info Structure
  property_count: 1
  slug: devportal-api-api-monetization-info-structure
- name: Devportal Api Api Monetization Usage Structure
  property_count: 1
  slug: devportal-api-api-monetization-usage-structure
- name: Devportal Api Api Operations Structure
  property_count: 3
  slug: devportal-api-api-operations-structure
- name: Devportal Api Api Search Result Structure
  property_count: 0
  slug: devportal-api-api-search-result-structure
- name: Devportal Api Api Structure
  property_count: 40
  slug: devportal-api-api-structure
- name: Devportal Api Api With Key Info Structure
  property_count: 4
  slug: devportal-api-api-with-key-info-structure
- name: Devportal Api Apiapi Key Associate Request Structure
  property_count: 2
  slug: devportal-api-apiapi-key-associate-request-structure
- name: Devportal Api Apiapi Key Generate Request Structure
  property_count: 4
  slug: devportal-api-apiapi-key-generate-request-structure
- name: Devportal Api Apiapi Key Info Structure
  property_count: 6
  slug: devportal-api-apiapi-key-info-structure
- name: Devportal Api Apiapi Key List Structure
  property_count: 2
  slug: devportal-api-apiapi-key-list-structure
- name: Devportal Api Apiapi Key Revoke Request Structure
  property_count: 1
  slug: devportal-api-apiapi-key-revoke-request-structure
- name: Devportal Api App Api Key Associate Request Structure
  property_count: 2
  slug: devportal-api-app-api-key-associate-request-structure
- name: Devportal Api Application Attribute List Structure
  property_count: 2
  slug: devportal-api-application-attribute-list-structure
- name: Devportal Api Application Attribute Structure
  property_count: 6
  slug: devportal-api-application-attribute-structure
- name: Devportal Api Application Configuration Constraint Structure
  property_count: 2
  slug: devportal-api-application-configuration-constraint-structure
- name: Devportal Api Application Info Structure
  property_count: 12
  slug: devportal-api-application-info-structure
- name: Devportal Api Application Key Generate Request Structure
  property_count: 9
  slug: devportal-api-application-key-generate-request-structure
- name: Devportal Api Application Key List Structure
  property_count: 2
  slug: devportal-api-application-key-list-structure
- name: Devportal Api Application Key Mapping Request Structure
  property_count: 4
  slug: devportal-api-application-key-mapping-request-structure
- name: Devportal Api Application Key Re Generate Response Structure
  property_count: 2
  slug: devportal-api-application-key-re-generate-response-structure
- name: Devportal Api Application Key Structure
  property_count: 13
  slug: devportal-api-application-key-structure
- name: Devportal Api Application List Structure
  property_count: 3
  slug: devportal-api-application-list-structure
- name: Devportal Api Application Structure
  property_count: 16
  slug: devportal-api-application-structure
- name: Devportal Api Application Throttle Reset Structure
  property_count: 1
  slug: devportal-api-application-throttle-reset-structure
- name: Devportal Api Application Token Generate Request Structure
  property_count: 6
  slug: devportal-api-application-token-generate-request-structure
- name: Devportal Api Application Token Structure
  property_count: 3
  slug: devportal-api-application-token-structure
- name: Devportal Api Chat Message Structure
  property_count: 2
  slug: devportal-api-chat-message-structure
- name: Devportal Api Comment List Structure
  property_count: 3
  slug: devportal-api-comment-list-structure
- name: Devportal Api Comment Structure
  property_count: 10
  slug: devportal-api-comment-structure
- name: Devportal Api Commenter Info Structure
  property_count: 3
  slug: devportal-api-commenter-info-structure
- name: Devportal Api Consumer Secret Creation Request Structure
  property_count: 1
  slug: devportal-api-consumer-secret-creation-request-structure
- name: Devportal Api Consumer Secret Deletion Request Structure
  property_count: 2
  slug: devportal-api-consumer-secret-deletion-request-structure
- name: Devportal Api Consumer Secret List Structure
  property_count: 2
  slug: devportal-api-consumer-secret-list-structure
- name: Devportal Api Consumer Secret Structure
  property_count: 3
  slug: devportal-api-consumer-secret-structure
- name: Devportal Api Current And New Passwords Structure
  property_count: 2
  slug: devportal-api-current-and-new-passwords-structure
- name: Devportal Api Document List Structure
  property_count: 3
  slug: devportal-api-document-list-structure
- name: Devportal Api Document Search Result Structure
  property_count: 0
  slug: devportal-api-document-search-result-structure
- name: Devportal Api Document Structure
  property_count: 7
  slug: devportal-api-document-structure
- name: Devportal Api Graph Ql Custom Complexity Info Structure
  property_count: 3
  slug: devportal-api-graph-ql-custom-complexity-info-structure
- name: Devportal Api Graph Ql Query Complexity Info Structure
  property_count: 1
  slug: devportal-api-graph-ql-query-complexity-info-structure
- name: Devportal Api Graph Ql Schema Type List Structure
  property_count: 1
  slug: devportal-api-graph-ql-schema-type-list-structure
- name: Devportal Api Graph Ql Schema Type Structure
  property_count: 2
  slug: devportal-api-graph-ql-schema-type-structure
- name: Devportal Api Key Manager Application Configuration Structure
  property_count: 10
  slug: devportal-api-key-manager-application-configuration-structure
- name: Devportal Api Key Manager Info Structure
  property_count: 19
  slug: devportal-api-key-manager-info-structure
- name: Devportal Api Key Manager List Structure
  property_count: 2
  slug: devportal-api-key-manager-list-structure
- name: Devportal Api Marketplace Assistant Api Count Response Structure
  property_count: 2
  slug: devportal-api-marketplace-assistant-api-count-response-structure
- name: Devportal Api Marketplace Assistant Api Structure
  property_count: 3
  slug: devportal-api-marketplace-assistant-api-structure
- name: Devportal Api Marketplace Assistant Request Structure
  property_count: 2
  slug: devportal-api-marketplace-assistant-request-structure
- name: Devportal Api Marketplace Assistant Response Structure
  property_count: 2
  slug: devportal-api-marketplace-assistant-response-structure
- name: Devportal Api Monetization Info Structure
  property_count: 5
  slug: devportal-api-monetization-info-structure
- name: Devportal Api Organization Info Structure
  property_count: 2
  slug: devportal-api-organization-info-structure
- name: Devportal Api Pagination Structure
  property_count: 5
  slug: devportal-api-pagination-structure
- name: Devportal Api Patch Request Body Structure
  property_count: 2
  slug: devportal-api-patch-request-body-structure
- name: Devportal Api Post Request Body Structure
  property_count: 2
  slug: devportal-api-post-request-body-structure
- name: Devportal Api Rating List Structure
  property_count: 5
  slug: devportal-api-rating-list-structure
- name: Devportal Api Rating Structure
  property_count: 4
  slug: devportal-api-rating-structure
- name: Devportal Api Recommendations Structure
  property_count: 2
  slug: devportal-api-recommendations-structure
- name: Devportal Api Recommended Api Structure
  property_count: 3
  slug: devportal-api-recommended-api-structure
- name: Devportal Api Sample Query Structure
  property_count: 2
  slug: devportal-api-sample-query-structure
- name: Devportal Api Scope Info Structure
  property_count: 4
  slug: devportal-api-scope-info-structure
- name: Devportal Api Scope List Structure
  property_count: 3
  slug: devportal-api-scope-list-structure
- name: Devportal Api Search Result List Structure
  property_count: 3
  slug: devportal-api-search-result-list-structure
- name: Devportal Api Search Result Structure
  property_count: 4
  slug: devportal-api-search-result-structure
- name: Devportal Api Settings Structure
  property_count: 23
  slug: devportal-api-settings-structure
- name: Devportal Api Solace Topics Structure
  property_count: 2
  slug: devportal-api-solace-topics-structure
- name: Devportal Api Subscribed Api With Api Key List Structure
  property_count: 2
  slug: devportal-api-subscribed-api-with-api-key-list-structure
- name: Devportal Api Subscription List Structure
  property_count: 3
  slug: devportal-api-subscription-list-structure
- name: Devportal Api Subscription Structure
  property_count: 9
  slug: devportal-api-subscription-structure
- name: Devportal Api Tag List Structure
  property_count: 3
  slug: devportal-api-tag-list-structure
- name: Devportal Api Tag Structure
  property_count: 2
  slug: devportal-api-tag-structure
- name: Devportal Api Tenant List Structure
  property_count: 3
  slug: devportal-api-tenant-list-structure
- name: Devportal Api Tenant Structure
  property_count: 2
  slug: devportal-api-tenant-structure
- name: Devportal Api Throttling Policy List Structure
  property_count: 3
  slug: devportal-api-throttling-policy-list-structure
- name: Devportal Api Throttling Policy Permission Info Structure
  property_count: 2
  slug: devportal-api-throttling-policy-permission-info-structure
- name: Devportal Api Throttling Policy Structure
  property_count: 15
  slug: devportal-api-throttling-policy-structure
- name: Devportal Api Topic List Structure
  property_count: 3
  slug: devportal-api-topic-list-structure
- name: Devportal Api Topic Structure
  property_count: 3
  slug: devportal-api-topic-structure
- name: Devportal Api User Structure
  property_count: 5
  slug: devportal-api-user-structure
- name: Devportal Api Webhook Subscription List Structure
  property_count: 3
  slug: devportal-api-webhook-subscription-list-structure
- name: Devportal Api Webhook Subscription Structure
  property_count: 6
  slug: devportal-api-webhook-subscription-structure
- name: Devportal Api Workflow Response Structure
  property_count: 2
  slug: devportal-api-workflow-response-structure
- name: Governance Api Action Structure
  property_count: 3
  slug: governance-api-action-structure
- name: Governance Api Apim Governance Policy List Structure
  property_count: 3
  slug: governance-api-apim-governance-policy-list-structure
- name: Governance Api Apim Governance Policy Structure
  property_count: 11
  slug: governance-api-apim-governance-policy-structure
- name: Governance Api Artifact Compliance Details Structure
  property_count: 4
  slug: governance-api-artifact-compliance-details-structure
- name: Governance Api Artifact Compliance For Policy Structure
  property_count: 3
  slug: governance-api-artifact-compliance-for-policy-structure
- name: Governance Api Artifact Compliance List Structure
  property_count: 3
  slug: governance-api-artifact-compliance-list-structure
- name: Governance Api Artifact Compliance Status Structure
  property_count: 5
  slug: governance-api-artifact-compliance-status-structure
- name: Governance Api Artifact Compliance Summary For Policy Structure
  property_count: 2
  slug: governance-api-artifact-compliance-summary-for-policy-structure
- name: Governance Api Artifact Compliance Summary Structure
  property_count: 5
  slug: governance-api-artifact-compliance-summary-structure
- name: Governance Api Artifact Info Structure
  property_count: 5
  slug: governance-api-artifact-info-structure
- name: Governance Api Pagination Structure
  property_count: 5
  slug: governance-api-pagination-structure
- name: Governance Api Policy Adherence Details Structure
  property_count: 4
  slug: governance-api-policy-adherence-details-structure
- name: Governance Api Policy Adherence List Structure
  property_count: 3
  slug: governance-api-policy-adherence-list-structure
- name: Governance Api Policy Adherence Status Structure
  property_count: 4
  slug: governance-api-policy-adherence-status-structure
- name: Governance Api Policy Adherence Summary Structure
  property_count: 4
  slug: governance-api-policy-adherence-summary-structure
- name: Governance Api Policy Adherence With Rulesets Structure
  property_count: 4
  slug: governance-api-policy-adherence-with-rulesets-structure
- name: Governance Api Rule Validation Result Structure
  property_count: 7
  slug: governance-api-rule-validation-result-structure
- name: Governance Api Ruleset Info Structure
  property_count: 12
  slug: governance-api-ruleset-info-structure
- name: Governance Api Ruleset Input Structure
  property_count: 8
  slug: governance-api-ruleset-input-structure
- name: Governance Api Ruleset List Structure
  property_count: 3
  slug: governance-api-ruleset-list-structure
- name: Governance Api Ruleset Validation Result Structure
  property_count: 5
  slug: governance-api-ruleset-validation-result-structure
- name: Governance Api Ruleset Validation Result Without Rules Structure
  property_count: 4
  slug: governance-api-ruleset-validation-result-without-rules-structure
- name: Governance Api Severity Based Rule Violation Count Structure
  property_count: 2
  slug: governance-api-severity-based-rule-violation-count-structure
- name: Publisher Api Additional Property Structure
  property_count: 2
  slug: publisher-api-additional-property-structure
- name: Publisher Api Advertise Info Structure
  property_count: 6
  slug: publisher-api-advertise-info-structure
- name: Publisher Api Ai Service Provider Endpoint Authentication Configuration Structure
  property_count: 3
  slug: publisher-api-ai-service-provider-endpoint-authentication-configuration-structure
- name: Publisher Api Ai Service Provider Endpoint Configuration Structure
  property_count: 3
  slug: publisher-api-ai-service-provider-endpoint-configuration-structure
- name: Publisher Api Ai Service Provider Response Structure
  property_count: 8
  slug: publisher-api-ai-service-provider-response-structure
- name: Publisher Api Ai Service Provider Summary Response List Structure
  property_count: 2
  slug: publisher-api-ai-service-provider-summary-response-list-structure
- name: Publisher Api Ai Service Provider Summary Response Structure
  property_count: 6
  slug: publisher-api-ai-service-provider-summary-response-structure
- name: Publisher Api Api Business Information Structure
  property_count: 4
  slug: publisher-api-api-business-information-structure
- name: Publisher Api Api Category List Structure
  property_count: 2
  slug: publisher-api-api-category-list-structure
- name: Publisher Api Api Category Structure
  property_count: 3
  slug: publisher-api-api-category-structure
- name: Publisher Api Api Cors Configuration Structure
  property_count: 5
  slug: publisher-api-api-cors-configuration-structure
- name: Publisher Api Api Definition Search Result Structure
  property_count: 0
  slug: publisher-api-api-definition-search-result-structure
- name: Publisher Api Api Endpoint List Structure
  property_count: 3
  slug: publisher-api-api-endpoint-list-structure
- name: Publisher Api Api Endpoint Structure
  property_count: 5
  slug: publisher-api-api-endpoint-structure
- name: Publisher Api Api Endpoint Validation Response Structure
  property_count: 3
  slug: publisher-api-api-endpoint-validation-response-structure
- name: Publisher Api Api External Store List Structure
  property_count: 2
  slug: publisher-api-api-external-store-list-structure
- name: Publisher Api Api External Store Structure
  property_count: 2
  slug: publisher-api-api-external-store-structure
- name: Publisher Api Api Info Structure
  property_count: 30
  slug: publisher-api-api-info-structure
- name: Publisher Api Api Key Structure
  property_count: 2
  slug: publisher-api-api-key-structure
- name: Publisher Api Api List Structure
  property_count: 3
  slug: publisher-api-api-list-structure
- name: Publisher Api Api Max Tps Structure
  property_count: 5
  slug: publisher-api-api-max-tps-structure
- name: Publisher Api Api Metadata List Structure
  property_count: 3
  slug: publisher-api-api-metadata-list-structure
- name: Publisher Api Api Metadata Structure
  property_count: 5
  slug: publisher-api-api-metadata-structure
- name: Publisher Api Api Monetization Info Structure
  property_count: 2
  slug: publisher-api-api-monetization-info-structure
- name: Publisher Api Api Monetization Usage Structure
  property_count: 1
  slug: publisher-api-api-monetization-usage-structure
- name: Publisher Api Api Operation Mapping Structure
  property_count: 5
  slug: publisher-api-api-operation-mapping-structure
- name: Publisher Api Api Operation Policies Structure
  property_count: 3
  slug: publisher-api-api-operation-policies-structure
- name: Publisher Api Api Operations Structure
  property_count: 14
  slug: publisher-api-api-operations-structure
- name: Publisher Api Api Product Business Information Structure
  property_count: 4
  slug: publisher-api-api-product-business-information-structure
- name: Publisher Api Api Product Info Structure
  property_count: 20
  slug: publisher-api-api-product-info-structure
- name: Publisher Api Api Product List Structure
  property_count: 3
  slug: publisher-api-api-product-list-structure
- name: Publisher Api Api Product Outdated Status Structure
  property_count: 1
  slug: publisher-api-api-product-outdated-status-structure
- name: Publisher Api Api Product Search Result Structure
  property_count: 0
  slug: publisher-api-api-product-search-result-structure
- name: Publisher Api Api Product Structure
  property_count: 46
  slug: publisher-api-api-product-structure
- name: Publisher Api Api Revenue Structure
  property_count: 1
  slug: publisher-api-api-revenue-structure
- name: Publisher Api Api Revision Api Info Structure
  property_count: 1
  slug: publisher-api-api-revision-api-info-structure
- name: Publisher Api Api Revision Deployment List Structure
  property_count: 1
  slug: publisher-api-api-revision-deployment-list-structure
- name: Publisher Api Api Revision Deployment Structure
  property_count: 10
  slug: publisher-api-api-revision-deployment-structure
- name: Publisher Api Api Revision List Structure
  property_count: 2
  slug: publisher-api-api-revision-list-structure
- name: Publisher Api Api Revision Structure
  property_count: 6
  slug: publisher-api-api-revision-structure
- name: Publisher Api Api Scope Structure
  property_count: 2
  slug: publisher-api-api-scope-structure
- name: Publisher Api Api Search Result Structure
  property_count: 0
  slug: publisher-api-api-search-result-structure
- name: Publisher Api Api Structure
  property_count: 69
  slug: publisher-api-api-structure
- name: Publisher Api Application Info Structure
  property_count: 5
  slug: publisher-api-application-info-structure
- name: Publisher Api Application Structure
  property_count: 6
  slug: publisher-api-application-structure
- name: Publisher Api Async Api Specification Validation Response Structure
  property_count: 4
  slug: publisher-api-async-api-specification-validation-response-structure
- name: Publisher Api Audit Report Structure
  property_count: 4
  slug: publisher-api-audit-report-structure
- name: Publisher Api Backend List Structure
  property_count: 2
  slug: publisher-api-backend-list-structure
- name: Publisher Api Backend Operation Mapping Structure
  property_count: 2
  slug: publisher-api-backend-operation-mapping-structure
- name: Publisher Api Backend Operation Structure
  property_count: 2
  slug: publisher-api-backend-operation-structure
- name: Publisher Api Backend Structure
  property_count: 4
  slug: publisher-api-backend-structure
- name: Publisher Api Bandwidth Limit Structure
  property_count: 0
  slug: publisher-api-bandwidth-limit-structure
- name: Publisher Api Cert Metadata Structure
  property_count: 2
  slug: publisher-api-cert-metadata-structure
- name: Publisher Api Certificate Info Structure
  property_count: 4
  slug: publisher-api-certificate-info-structure
- name: Publisher Api Certificate Validity Structure
  property_count: 2
  slug: publisher-api-certificate-validity-structure
- name: Publisher Api Certificates Structure
  property_count: 3
  slug: publisher-api-certificates-structure
- name: Publisher Api Claim Structure
  property_count: 3
  slug: publisher-api-claim-structure
- name: Publisher Api Client Cert Metadata Structure
  property_count: 3
  slug: publisher-api-client-cert-metadata-structure
- name: Publisher Api Client Certificates Structure
  property_count: 3
  slug: publisher-api-client-certificates-structure
- name: Publisher Api Comment List Structure
  property_count: 3
  slug: publisher-api-comment-list-structure
- name: Publisher Api Comment Request Structure
  property_count: 2
  slug: publisher-api-comment-request-structure
- name: Publisher Api Comment Structure
  property_count: 10
  slug: publisher-api-comment-structure
- name: Publisher Api Commenter Info Structure
  property_count: 3
  slug: publisher-api-commenter-info-structure
- name: Publisher Api Content Publish Status Response Structure
  property_count: 2
  slug: publisher-api-content-publish-status-response-structure
- name: Publisher Api Content Publish Status Structure
  property_count: 1
  slug: publisher-api-content-publish-status-structure
- name: Publisher Api Custom Attribute Structure
  property_count: 2
  slug: publisher-api-custom-attribute-structure
- name: Publisher Api Design Assistant Api Payload Response Structure
  property_count: 1
  slug: publisher-api-design-assistant-api-payload-response-structure
- name: Publisher Api Design Assistant Chat Query Structure
  property_count: 2
  slug: publisher-api-design-assistant-chat-query-structure
- name: Publisher Api Design Assistant Chat Response Structure
  property_count: 8
  slug: publisher-api-design-assistant-chat-response-structure
- name: Publisher Api Design Assistant Gen Api Payload Structure
  property_count: 1
  slug: publisher-api-design-assistant-gen-api-payload-structure
- name: Publisher Api Document List Structure
  property_count: 3
  slug: publisher-api-document-list-structure
- name: Publisher Api Document Search Result Structure
  property_count: 0
  slug: publisher-api-document-search-result-structure
- name: Publisher Api Document Structure
  property_count: 14
  slug: publisher-api-document-structure
- name: Publisher Api Endpoint Config Structure
  property_count: 3
  slug: publisher-api-endpoint-config-structure
- name: Publisher Api Endpoint List Structure
  property_count: 2
  slug: publisher-api-endpoint-list-structure
- name: Publisher Api Endpoint Structure
  property_count: 6
  slug: publisher-api-endpoint-structure
- name: Publisher Api Environment List Structure
  property_count: 2
  slug: publisher-api-environment-list-structure
- name: Publisher Api Environment Properties Structure
  property_count: 0
  slug: publisher-api-environment-properties-structure
- name: Publisher Api Environment Structure
  property_count: 13
  slug: publisher-api-environment-structure
- name: Publisher Api Event Count Limit Structure
  property_count: 0
  slug: publisher-api-event-count-limit-structure
- name: Publisher Api External Store List Structure
  property_count: 2
  slug: publisher-api-external-store-list-structure
- name: Publisher Api External Store Structure
  property_count: 4
  slug: publisher-api-external-store-structure
- name: Publisher Api File Info Structure
  property_count: 2
  slug: publisher-api-file-info-structure
- name: Publisher Api Gateway Environment Protocol Uri Structure
  property_count: 2
  slug: publisher-api-gateway-environment-protocol-uri-structure
- name: Publisher Api Gateway Policy Deployment Structure
  property_count: 3
  slug: publisher-api-gateway-policy-deployment-structure
- name: Publisher Api Gateway Policy Mapping Data List Structure
  property_count: 3
  slug: publisher-api-gateway-policy-mapping-data-list-structure
- name: Publisher Api Gateway Policy Mapping Deployment Info Structure
  property_count: 4
  slug: publisher-api-gateway-policy-mapping-deployment-info-structure
- name: Publisher Api Gateway Policy Mapping Info Structure
  property_count: 3
  slug: publisher-api-gateway-policy-mapping-info-structure
- name: Publisher Api Gateway Policy Mappings Structure
  property_count: 5
  slug: publisher-api-gateway-policy-mappings-structure
- name: Publisher Api Graph Ql Custom Complexity Info Structure
  property_count: 3
  slug: publisher-api-graph-ql-custom-complexity-info-structure
- name: Publisher Api Graph Ql Query Complexity Info Structure
  property_count: 1
  slug: publisher-api-graph-ql-query-complexity-info-structure
- name: Publisher Api Graph Ql Query Structure
  property_count: 2
  slug: publisher-api-graph-ql-query-structure
- name: Publisher Api Graph Ql Schema Structure
  property_count: 2
  slug: publisher-api-graph-ql-schema-structure
- name: Publisher Api Graph Ql Schema Type List Structure
  property_count: 1
  slug: publisher-api-graph-ql-schema-type-list-structure
- name: Publisher Api Graph Ql Schema Type Structure
  property_count: 2
  slug: publisher-api-graph-ql-schema-type-structure
- name: Publisher Api Graph Ql Validation Response Structure
  property_count: 3
  slug: publisher-api-graph-ql-validation-response-structure
- name: Publisher Api Import Api Response Structure
  property_count: 2
  slug: publisher-api-import-api-response-structure
- name: Publisher Api Integrated Api Response Structure
  property_count: 3
  slug: publisher-api-integrated-api-response-structure
- name: Publisher Api Key Manager Info Structure
  property_count: 7
  slug: publisher-api-key-manager-info-structure
- name: Publisher Api Key Manager List Structure
  property_count: 2
  slug: publisher-api-key-manager-list-structure
- name: Publisher Api Label List Structure
  property_count: 3
  slug: publisher-api-label-list-structure
- name: Publisher Api Label Structure
  property_count: 3
  slug: publisher-api-label-structure
- name: Publisher Api Lifecycle History Item Structure
  property_count: 4
  slug: publisher-api-lifecycle-history-item-structure
- name: Publisher Api Lifecycle History Structure
  property_count: 2
  slug: publisher-api-lifecycle-history-structure
- name: Publisher Api Lifecycle State Structure
  property_count: 3
  slug: publisher-api-lifecycle-state-structure
- name: Publisher Api Llm Provider Endpoint Configuration Structure
  property_count: 2
  slug: publisher-api-llm-provider-endpoint-configuration-structure
- name: Publisher Api Llm Provider Response Structure
  property_count: 7
  slug: publisher-api-llm-provider-response-structure
- name: Publisher Api Llm Provider Summary Response List Structure
  property_count: 2
  slug: publisher-api-llm-provider-summary-response-list-structure
- name: Publisher Api Llm Provider Summary Response Structure
  property_count: 5
  slug: publisher-api-llm-provider-summary-response-structure
- name: Publisher Api Max Tps Structure
  property_count: 4
  slug: publisher-api-max-tps-structure
- name: Publisher Api Mcp Server Metadata List Structure
  property_count: 2
  slug: publisher-api-mcp-server-metadata-list-structure
- name: Publisher Api Mcp Server Metadata Structure
  property_count: 5
  slug: publisher-api-mcp-server-metadata-structure
- name: Publisher Api Mcp Server Operation Policies Structure
  property_count: 3
  slug: publisher-api-mcp-server-operation-policies-structure
- name: Publisher Api Mcp Server Operation Structure
  property_count: 13
  slug: publisher-api-mcp-server-operation-structure
- name: Publisher Api Mcp Server Scope Structure
  property_count: 2
  slug: publisher-api-mcp-server-scope-structure
- name: Publisher Api Mcp Server Structure
  property_count: 51
  slug: publisher-api-mcp-server-structure
- name: Publisher Api Mcp Server Validation Request Structure
  property_count: 2
  slug: publisher-api-mcp-server-validation-request-structure
- name: Publisher Api Mcp Server Validation Response Structure
  property_count: 4
  slug: publisher-api-mcp-server-validation-response-structure
- name: Publisher Api Mediation Policy Structure
  property_count: 4
  slug: publisher-api-mediation-policy-structure
- name: Publisher Api Mock Response Payload Info Structure
  property_count: 3
  slug: publisher-api-mock-response-payload-info-structure
- name: Publisher Api Mock Response Payload List Structure
  property_count: 1
  slug: publisher-api-mock-response-payload-list-structure
- name: Publisher Api Model Provider Structure
  property_count: 2
  slug: publisher-api-model-provider-structure
- name: Publisher Api Monetization Attribute Structure
  property_count: 6
  slug: publisher-api-monetization-attribute-structure
- name: Publisher Api Monetization Info Structure
  property_count: 2
  slug: publisher-api-monetization-info-structure
- name: Publisher Api Open Api Definition Validation Response Structure
  property_count: 4
  slug: publisher-api-open-api-definition-validation-response-structure
- name: Publisher Api Operation Policy Data List Structure
  property_count: 3
  slug: publisher-api-operation-policy-data-list-structure
- name: Publisher Api Operation Policy Data Structure
  property_count: 12
  slug: publisher-api-operation-policy-data-structure
- name: Publisher Api Operation Policy Spec Attribute Structure
  property_count: 8
  slug: publisher-api-operation-policy-spec-attribute-structure
- name: Publisher Api Operation Policy Structure
  property_count: 5
  slug: publisher-api-operation-policy-structure
- name: Publisher Api Organization Info Structure
  property_count: 2
  slug: publisher-api-organization-info-structure
- name: Publisher Api Organization List Structure
  property_count: 2
  slug: publisher-api-organization-list-structure
- name: Publisher Api Organization Policies Structure
  property_count: 2
  slug: publisher-api-organization-policies-structure
- name: Publisher Api Organization Structure
  property_count: 5
  slug: publisher-api-organization-structure
- name: Publisher Api Pagination Structure
  property_count: 5
  slug: publisher-api-pagination-structure
- name: Publisher Api Product Api Structure
  property_count: 4
  slug: publisher-api-product-api-structure
- name: Publisher Api Request Count Limit Structure
  property_count: 0
  slug: publisher-api-request-count-limit-structure
- name: Publisher Api Request Label List Structure
  property_count: 1
  slug: publisher-api-request-label-list-structure
- name: Publisher Api Resource Path List Structure
  property_count: 3
  slug: publisher-api-resource-path-list-structure
- name: Publisher Api Resource Path Structure
  property_count: 3
  slug: publisher-api-resource-path-structure
- name: Publisher Api Resource Policy Info Structure
  property_count: 4
  slug: publisher-api-resource-policy-info-structure
- name: Publisher Api Resource Policy List Structure
  property_count: 2
  slug: publisher-api-resource-policy-list-structure
- name: Publisher Api Scope List Structure
  property_count: 3
  slug: publisher-api-scope-list-structure
- name: Publisher Api Scope Structure
  property_count: 6
  slug: publisher-api-scope-structure
- name: Publisher Api Search Result List Structure
  property_count: 3
  slug: publisher-api-search-result-list-structure
- name: Publisher Api Search Result Structure
  property_count: 4
  slug: publisher-api-search-result-structure
- name: Publisher Api Security Audit Attribute Structure
  property_count: 5
  slug: publisher-api-security-audit-attribute-structure
- name: Publisher Api Security Info Structure
  property_count: 3
  slug: publisher-api-security-info-structure
- name: Publisher Api Sequence Backend List Structure
  property_count: 2
  slug: publisher-api-sequence-backend-list-structure
- name: Publisher Api Sequence Backend Structure
  property_count: 4
  slug: publisher-api-sequence-backend-structure
- name: Publisher Api Settings Structure
  property_count: 24
  slug: publisher-api-settings-structure
- name: Publisher Api Shared Scope Usage Entity Structure
  property_count: 7
  slug: publisher-api-shared-scope-usage-entity-structure
- name: Publisher Api Shared Scope Usage Structure
  property_count: 4
  slug: publisher-api-shared-scope-usage-structure
- name: Publisher Api Shared Scope Used Api Info Structure
  property_count: 6
  slug: publisher-api-shared-scope-used-api-info-structure
- name: Publisher Api Shared Scope Used Api Resource Info Structure
  property_count: 2
  slug: publisher-api-shared-scope-used-api-resource-info-structure
- name: Publisher Api Shared Scope Used Resource Info Structure
  property_count: 2
  slug: publisher-api-shared-scope-used-resource-info-structure
- name: Publisher Api Subscriber Contact Attribute Structure
  property_count: 2
  slug: publisher-api-subscriber-contact-attribute-structure
- name: Publisher Api Subscriber Info Structure
  property_count: 2
  slug: publisher-api-subscriber-info-structure
- name: Publisher Api Subscription List Structure
  property_count: 3
  slug: publisher-api-subscription-list-structure
- name: Publisher Api Subscription Policy List Structure
  property_count: 3
  slug: publisher-api-subscription-policy-list-structure
- name: Publisher Api Subscription Policy Structure
  property_count: 0
  slug: publisher-api-subscription-policy-structure
- name: Publisher Api Subscription Structure
  property_count: 4
  slug: publisher-api-subscription-structure
- name: Publisher Api Subscription Throttle Policy Permission Structure
  property_count: 2
  slug: publisher-api-subscription-throttle-policy-permission-structure
- name: Publisher Api Subtype Configuration Structure
  property_count: 2
  slug: publisher-api-subtype-configuration-structure
- name: Publisher Api Tenant List Structure
  property_count: 3
  slug: publisher-api-tenant-list-structure
- name: Publisher Api Tenant Structure
  property_count: 2
  slug: publisher-api-tenant-structure
- name: Publisher Api Threat Protection Policy List Structure
  property_count: 1
  slug: publisher-api-threat-protection-policy-list-structure
- name: Publisher Api Threat Protection Policy Structure
  property_count: 4
  slug: publisher-api-threat-protection-policy-structure
- name: Publisher Api Throttle Limit Base Structure
  property_count: 2
  slug: publisher-api-throttle-limit-base-structure
- name: Publisher Api Throttle Limit Structure
  property_count: 4
  slug: publisher-api-throttle-limit-structure
- name: Publisher Api Throttle Policy Structure
  property_count: 6
  slug: publisher-api-throttle-policy-structure
- name: Publisher Api Throttling Policy List Structure
  property_count: 3
  slug: publisher-api-throttling-policy-list-structure
- name: Publisher Api Throttling Policy Structure
  property_count: 18
  slug: publisher-api-throttling-policy-structure
- name: Publisher Api Topic List Structure
  property_count: 3
  slug: publisher-api-topic-list-structure
- name: Publisher Api Topic Structure
  property_count: 4
  slug: publisher-api-topic-structure
- name: Publisher Api V Host Structure
  property_count: 10
  slug: publisher-api-v-host-structure
- name: Publisher Api Websub Subscription Configuration Structure
  property_count: 4
  slug: publisher-api-websub-subscription-configuration-structure
- name: Publisher Api Workflow Info Structure
  property_count: 7
  slug: publisher-api-workflow-info-structure
- name: Publisher Api Workflow List Structure
  property_count: 4
  slug: publisher-api-workflow-list-structure
- name: Publisher Api Workflow Response Structure
  property_count: 3
  slug: publisher-api-workflow-response-structure
- name: Publisher Api Workflow Structure
  property_count: 3
  slug: publisher-api-workflow-structure
- name: Publisher Api Wsdl Info Structure
  property_count: 1
  slug: publisher-api-wsdl-info-structure
- name: Publisher Api Wsdl Validation Response Structure
  property_count: 3
  slug: publisher-api-wsdl-validation-response-structure
- name: Service Catalog Api Api Info Structure
  property_count: 6
  slug: service-catalog-api-api-info-structure
- name: Service Catalog Api Api List Structure
  property_count: 2
  slug: service-catalog-api-api-list-structure
- name: Service Catalog Api Pagination Structure
  property_count: 5
  slug: service-catalog-api-pagination-structure
- name: Service Catalog Api Service Info List Structure
  property_count: 2
  slug: service-catalog-api-service-info-list-structure
- name: Service Catalog Api Service Info Structure
  property_count: 5
  slug: service-catalog-api-service-info-structure
- name: Service Catalog Api Service List Expanded Structure
  property_count: 3
  slug: service-catalog-api-service-list-expanded-structure
- name: Service Catalog Api Service List Structure
  property_count: 2
  slug: service-catalog-api-service-list-structure
- name: Service Catalog Api Service Schema Structure
  property_count: 3
  slug: service-catalog-api-service-schema-structure
- name: Service Catalog Api Service Structure
  property_count: 14
  slug: service-catalog-api-service-structure
- name: Service Catalog Api Settings Structure
  property_count: 1
  slug: service-catalog-api-settings-structure
- name: Service Catalog Api Verifier Structure
  property_count: 2
  slug: service-catalog-api-verifier-structure
jsonld:
- class_count: 120
  name: Wso2 Context
  property_count: 235
  slug: wso2-context
layout: provider
mcp_servers:
- description: Remote MCP server at apis.wso2.com requiring OAuth.
  name: WSO2 MCP Server
  slug: wso2-mcp-yml
modified: '2026-09-16'
name: WSO2
nav: Providers
network: true
overview: 'WSO2 publishes 90 API contracts indexed on the [APIs.io](https://apis.io/) network, including Advanced Policy (Collection) API, Advanced Policy (Individual) API, AIServiceProvider API, and 87 more. Tagged areas include API Management, Gateways, Open Source, API Lifecycle, and GraphQL.


  The WSO2 catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  WSO2''s developer surface includes CLI, API reference, signup flow, authentication, documentation, getting-started guide, engineering blog, and 52 more developer resources.'
plans:
- name: Wso2 Plans Pricing
  plan_count: 3
  slug: wso2-plans-pricing
- name: Wso2 Price Estimates
  plan_count: 0
  slug: wso2-price-estimates
random_paper: 11
rate_limits:
- limit_count: 6
  name: Wso2 Rate Limits
  slug: wso2-rate-limits
rules:
- authorship: provider
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: WSO2 — agent skills rules
  rule_count: 69
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 69
  slug: wso2-agent-skills-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: WSO2 — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wso2-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: WSO2 API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 7
  slug: wso2-rules
scopes:
- name: Wso2 Scopes
  scope_count: 51
  slug: wso2-scopes
  summary_line: 51 scopes · password
score:
  band: exemplar
  composite: 82.9
  coverage:
    artifact_dirs: 35
    catalog_earned: 106.3
    catalog_earned_first_party: 42.0
    catalog_gap: 8.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 93.4
    contract_governance: 62.9
    contract_quality: 68.2
    developer_ergonomics: 54.2
    discoverability: 81.7
    operational_transparency: 82.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  open_source:
    applies: true
    score: 100.0
  previous_composite: 84.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 78.0
      total: 91
    mcp: derived
    skills: derived
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
    score: 33.3
screenshot: https://apis.io/screenshots/wso2/wso2-2026-06-20T201634.png
security:
- kind: authentication
  name: Wso2 Authentication
  slug: wso2-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Wso2 Domain Security
  slug: wso2-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Wso2 Vulnerability Disclosure
  slug: wso2-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Wso2 Trust Center
  slug: wso2-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
skill_count: 4
skills:
- name: wso2-generate-and-associate-api-key
  slug: wso2-generate-and-associate-api-key
- name: wso2-generate-application-token
  slug: wso2-generate-application-token
- name: wso2-get-api-definition
  slug: wso2-get-api-definition
- name: wso2-modify-application
  slug: wso2-modify-application
slug: wso2
tags:
- API Management
- Gateways
- Open Source
- API Lifecycle
- GraphQL
- SOAP
- REST
- Identity Federation
- API Gateway
use_cases:
- description: Centrally manage the full lifecycle of all enterprise APIs.
  name: API Program Management
- description: Developer portal for API discovery, subscription, and key management.
  name: Developer Self-Service
- description: Expose REST APIs as MCP tools for AI and agent consumption.
  name: AI Agent Integration
- description: Route, monitor, and govern traffic to large language model APIs.
  name: LLM Traffic Management
- description: Enforce API design standards and validate compliance across teams.
  name: Compliance and Governance
- description: Define subscription tiers and billing for API usage-based monetization.
  name: B2B API Monetization
website: https://wso2.com/api-manager/
---
