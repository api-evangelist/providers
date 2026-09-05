---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 93
  human_in_the_loop: 7
  name: Tyk Agentic Access
  operation_count: 176
  slug: tyk-agentic-access
  summary_line: 176 operations · 93 acting · 7 human-in-the-loop
api_count: 4
apis:
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: These APIs helps you get,add and delete (CRUD) a list of additional (custom) permissions for your Dashboard users. You can use the created additional permissions with Open Policy Agent (OPA). <br/> On
  name: Tyk Additional Permissions API
  slug: tyk-additional-permissions-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The Tyk Dashboard provides a full set of analytics functions and graphs that you can use to segment and view your API traffic and activity.
  name: Tyk Analytics API
  slug: tyk-analytics-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: Use the endpoints under this tags to update,add ,delete and fetch the classic APIs.
  name: Tyk APIs API
  slug: tyk-apis-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: An API template is an asset managed by Tyk Dashboard that is used as the starting point - a blueprint - from which you can create a new Tyk OAS API definition. <br/> Templates are used only during the
  name: Tyk Assets API
  slug: tyk-assets-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The AuditLogs API from Tyk — 1 operation(s) for auditlogs.
  name: Tyk AuditLogs API
  slug: tyk-auditlogs-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: An API request made using Basic Authentication will have an Authorization header that contains the API key. The value of the Authorization header will be in the form:</br> `Basic base64Encode(username
  name: Tyk Basic Authentication API
  slug: tyk-basic-authentication-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: Tyk supports batch requests, so a client makes a single request to the API but gets a compound response object back. This is especially handy if clients have complex requests that have multiple synchr
  name: Tyk Batch Requests API
  slug: tyk-batch-requests-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: Sometimes a cache might contain stale data, or it may just need to be cleared because of an invalid configuration. This call will purge all keys associated with a cache on an API-by-API basis.
  name: Tyk Cache Invalidation API
  slug: tyk-cache-invalidation-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: Use the endpoints under this tag to manage your certificates. You can add, delete and list certificates using these endpoints.
  name: Tyk Certificates API
  slug: tyk-certificates-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: Use the endpoints under this tag to manage your certificates. You can add, delete and list certificates using these endpoints.
  name: Tyk Certs API
  slug: tyk-certs-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The CertsTag API from Tyk — 1 operation(s) for certstag.
  name: Tyk CertsTag API
  slug: tyk-certstag-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The Config API from Tyk — 1 operation(s) for config.
  name: Tyk Config API
  slug: tyk-config-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: Since the Dashboard can have multiple URLs associated with it. It is possible to force a URL reload by calling an API endpoint of the Dashboard API.
  name: Tyk Dashboard URL Reload API
  slug: tyk-dashboard-url-reload-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The Dataplanes API from Tyk — 1 operation(s) for dataplanes.
  name: Tyk Dataplanes API
  slug: tyk-dataplanes-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The Debug API from Tyk — 3 operation(s) for debug.
  name: Tyk Debug API
  slug: tyk-debug-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The Env API from Tyk — 1 operation(s) for env.
  name: Tyk Env API
  slug: tyk-env-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: To make Tyk installations more portable, the Export API enables you to export key configuration objects required to back-up and re-deploy a basic Tyk Pro installation.
  name: Tyk Export API
  slug: tyk-export-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The Health API from Tyk — 1 operation(s) for health.
  name: Tyk Health API
  slug: tyk-health-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: Check health status of the Tyk Gateway and loaded APIs.
  name: Tyk Health Checking API
  slug: tyk-health-checking-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: Force restart of the Gateway or whole cluster.
  name: Tyk Hot Reload API
  slug: tyk-hot-reload-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The import API enables you to add Organisations, APIs and Policies back into a Tyk installation while retaining their base IDs so that they work together.
  name: Tyk Import API
  slug: tyk-import-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: All keys that are used to access services via Tyk correspond to a session object that informs Tyk about the context of this particular token, like access rules and rate/quota allowance.
  name: Tyk Keys API
  slug: tyk-keys-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The Liveness API from Tyk — 1 operation(s) for liveness.
  name: Tyk Liveness API
  slug: tyk-liveness-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: Tyk allows you to work with APIs that you ve designed with the OpenAPI Specification version 3.0.x, making it even easier to get your API up and running. Use the endpoints in this tag to create,delete
  name: Tyk OAS APIs API
  slug: tyk-oas-apis-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: Use the endpoints in this tag to manage OAuth flow.
  name: Tyk Oauth API
  slug: tyk-oauth-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: 'The Tyk Dashboard permission system can be extended by writing custom rules using an Open Policy Agent (OPA). The rules engine works on top of your Dashboard API, which means you can control not only '
  name: Tyk Open Policy Agent API
  slug: tyk-open-policy-agent-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: It is possible to force API quota and rate limit across all keys that belong to a specific organisation ID. Rate limiting at an organisation level is useful for creating tiered access levels and trial
  name: Tyk Organisation Quotas API
  slug: tyk-organisation-quotas-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The organisations API gives the ability to manage your Tyk organisation(s).
  name: Tyk Organisations API
  slug: tyk-organisations-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: 'Policies are a template that enable you to create access rules, usage quota and rate limits that can be applied to multiple keys. They are a useful way to manage large groups of users, and to enforce '
  name: Tyk Policies API
  slug: tyk-policies-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The Readiness API from Tyk — 1 operation(s) for readiness.
  name: Tyk Readiness API
  slug: tyk-readiness-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: Get OAS schema.
  name: Tyk Schema API
  slug: tyk-schema-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The Dashboard SSO API allows you to implement custom authentication schemes for the Dashboard and Portal. Our Tyk Identity Broker (TIB) internally also uses this API.
  name: Tyk Single Sign On API
  slug: tyk-single-sign-on-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The Streams APIs API from Tyk — 2 operation(s) for streams apis.
  name: Tyk Streams APIs API
  slug: tyk-streams-apis-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: System API.
  name: Tyk System API
  slug: tyk-system-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The Tyk API from Tyk — 3 operation(s) for tyk.
  name: Tyk Tyk API
  slug: tyk-tyk-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: '**Note: Applies only to Tyk Gateway Community Edition** <br/>'
  name: Tyk Tyk OAS APIs API
  slug: tyk-tyk-oas-apis-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: 'When you have a large number of users and teams with different access requirements, instead of setting permissions per user, you can create a user group and configure the permissions for all users in '
  name: Tyk UserGroup API
  slug: tyk-usergroup-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: The admin portion of the users API gives you the ability to manage password reset policies for your Dashboard users.
  name: Tyk Users API
  slug: tyk-users-api
- baseURL: https://tyk.io/
  baseurl_source: declared
  description: Webhooks are a great way to let external applications know about the status of a user, an API or an event that has occurred in the Tyk gateway <br/> You can create webhooks that you can then re-use in
  name: Tyk Webhooks API
  slug: tyk-webhooks-api
artifact_total: 801
collections:
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions API
  slug: postman-tyk-additional-permissions-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Analytics API
  slug: postman-tyk-analytics-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions APIs API
  slug: postman-tyk-apis-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Assets API
  slug: postman-tyk-assets-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions AuditLogs API
  slug: postman-tyk-auditlogs-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Basic Authentication API
  slug: postman-tyk-basic-authentication-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Batch Requests API
  slug: postman-tyk-batch-requests-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Cache Invalidation API
  slug: postman-tyk-cache-invalidation-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Certificates API
  slug: postman-tyk-certificates-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Certs API
  slug: postman-tyk-certs-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions CertsTag API
  slug: postman-tyk-certstag-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Config API
  slug: postman-tyk-config-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Dashboard URL Reload API
  slug: postman-tyk-dashboard-url-reload-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Dataplanes API
  slug: postman-tyk-dataplanes-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Debug API
  slug: postman-tyk-debug-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Env API
  slug: postman-tyk-env-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Export API
  slug: postman-tyk-export-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Health API
  slug: postman-tyk-health-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Health Checking API
  slug: postman-tyk-health-checking-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Hot Reload API
  slug: postman-tyk-hot-reload-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Import API
  slug: postman-tyk-import-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Keys API
  slug: postman-tyk-keys-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Liveness API
  slug: postman-tyk-liveness-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions OAS APIs API
  slug: postman-tyk-oas-apis-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Oauth API
  slug: postman-tyk-oauth-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Open Policy Agent API
  slug: postman-tyk-open-policy-agent-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Organisation Quotas API
  slug: postman-tyk-organisation-quotas-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Organisations API
  slug: postman-tyk-organisations-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Policies API
  slug: postman-tyk-policies-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Readiness API
  slug: postman-tyk-readiness-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Schema API
  slug: postman-tyk-schema-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Single Sign On API
  slug: postman-tyk-single-sign-on-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Streams APIs API
  slug: postman-tyk-streams-apis-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions System API
  slug: postman-tyk-system-api
- collection_type: postman
  name: Dashboard Admin Additional Permissions Tyk API
  slug: postman-tyk-tyk-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Tyk OAS APIs API
  slug: postman-tyk-tyk-oas-apis-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions UserGroup API
  slug: postman-tyk-usergroup-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Users API
  slug: postman-tyk-users-api
- collection_type: postman
  name: Tyk Dashboard Admin Additional Permissions Webhooks API
  slug: postman-tyk-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions API
  slug: open-tyk-additional-permissions-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Analytics API
  slug: open-tyk-analytics-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions APIs API
  slug: open-tyk-apis-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Assets API
  slug: open-tyk-assets-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions AuditLogs API
  slug: open-tyk-auditlogs-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Basic Authentication API
  slug: open-tyk-basic-authentication-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Batch Requests API
  slug: open-tyk-batch-requests-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Cache Invalidation API
  slug: open-tyk-cache-invalidation-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Certificates API
  slug: open-tyk-certificates-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Certs API
  slug: open-tyk-certs-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions CertsTag API
  slug: open-tyk-certstag-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Config API
  slug: open-tyk-config-api
- collection_type: open
  name: Tyk Dashboard Admin API
  slug: open-tyk-dashboard-admin-api
- collection_type: open
  name: Tyk Dashboard API
  slug: open-tyk-dashboard-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Dashboard URL Reload API
  slug: open-tyk-dashboard-url-reload-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Dataplanes API
  slug: open-tyk-dataplanes-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Debug API
  slug: open-tyk-debug-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Env API
  slug: open-tyk-env-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Export API
  slug: open-tyk-export-api
- collection_type: open
  name: Tyk Gateway API
  slug: open-tyk-gateway-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Health API
  slug: open-tyk-health-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Health Checking API
  slug: open-tyk-health-checking-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Hot Reload API
  slug: open-tyk-hot-reload-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Import API
  slug: open-tyk-import-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Keys API
  slug: open-tyk-keys-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Liveness API
  slug: open-tyk-liveness-api
- collection_type: open
  name: Tyk MDCB Data Planes and Diagnostics API
  slug: open-tyk-mdcb-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions OAS APIs API
  slug: open-tyk-oas-apis-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Oauth API
  slug: open-tyk-oauth-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Open Policy Agent API
  slug: open-tyk-open-policy-agent-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Organisation Quotas API
  slug: open-tyk-organisation-quotas-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Organisations API
  slug: open-tyk-organisations-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Policies API
  slug: open-tyk-policies-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Readiness API
  slug: open-tyk-readiness-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Schema API
  slug: open-tyk-schema-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Single Sign On API
  slug: open-tyk-single-sign-on-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Streams APIs API
  slug: open-tyk-streams-apis-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions System API
  slug: open-tyk-system-api
- collection_type: open
  name: Dashboard Admin Additional Permissions Tyk API
  slug: open-tyk-tyk-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Tyk OAS APIs API
  slug: open-tyk-tyk-oas-apis-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions UserGroup API
  slug: open-tyk-usergroup-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Users API
  slug: open-tyk-users-api
- collection_type: open
  name: Tyk Dashboard Admin Additional Permissions Webhooks API
  slug: open-tyk-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tyk-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/TykTechnologies/tyk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/TykTechnologies/tyk/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/TykTechnologies/tyk/blob/master/CONTRIBUTING.md
- group: auth
  title: ''
  type: Security
  url: https://tyk.io/responsible-disclosure/
- group: auth
  title: ''
  type: Compliance
  url: https://tyk.io/gdpr
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tyk.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tyk.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tyk.io/terms-conditions
- group: start
  title: ''
  type: Signup
  url: https://tyk.io/sign-up/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tyk/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tyk-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tyk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tyk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tyk-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tyk
- group: start
  title: ''
  type: Portal
  url: https://tyk.io/
- group: docs
  title: ''
  type: Documentation
  url: https://tyk.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://tyk.io/docs/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://tyk.io/docs/basic-config-and-security/security/authentication-authorization/
- group: company
  title: ''
  type: Blog
  url: https://tyk.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://tyk.io/docs/developer-support/release-notes/dashboard
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TykTechnologies
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/TykTechnologies/tyk
- group: operate
  title: ''
  type: Support
  url: https://community.tyk.io/
- group: operate
  title: ''
  type: FAQ
  url: https://tyk.io/docs/frequently-asked-questions/
- group: commercial
  title: ''
  type: Pricing
  url: https://tyk.io/price-comparison/
- group: build
  title: ''
  type: CLI
  url: https://github.com/TykTechnologies/tyk-cli
- group: build
  title: Go Gateway SDK
  type: SDKs
  url: https://github.com/TykTechnologies/tyk
- group: design
  title: ''
  type: SpectralRules
  url: rules/tyk-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tyk-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/TykTechnologies/tyk-dashboard-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://tyk.io/docs/llms.txt
created: '2026-03-18'
description: Tyk is an open-source API gateway and management platform supporting REST, GraphQL, gRPC, and Async APIs with a developer portal, analytics, and flexible deployment across cloud, on-premise, and hybrid environments.
examples:
- key_count: 9
  name: Tyk Gateway Access Definition Example
  slug: tyk-gateway-access-definition-example
- key_count: 2
  name: Tyk Gateway Access Spec Example
  slug: tyk-gateway-access-spec-example
- key_count: 2
  name: Tyk Gateway Allowance Example
  slug: tyk-gateway-allowance-example
- key_count: 3
  name: Tyk Gateway Analytics Plugin Config Example
  slug: tyk-gateway-analytics-plugin-config-example
- key_count: 1
  name: Tyk Gateway Api All Certificate Basics Example
  slug: tyk-gateway-api-all-certificate-basics-example
- key_count: 1
  name: Tyk Gateway Api All Certificates Example
  slug: tyk-gateway-api-all-certificates-example
- key_count: 1
  name: Tyk Gateway Api All Keys Example
  slug: tyk-gateway-api-all-keys-example
- key_count: 3
  name: Tyk Gateway Api Certificate Status Message Example
  slug: tyk-gateway-api-certificate-status-message-example
- key_count: 74
  name: Tyk Gateway Api Definition Example
  slug: tyk-gateway-api-definition-example
- key_count: 9
  name: Tyk Gateway Api Limit Example
  slug: tyk-gateway-api-limit-example
- key_count: 4
  name: Tyk Gateway Api Modify Key Success Example
  slug: tyk-gateway-api-modify-key-success-example
- key_count: 2
  name: Tyk Gateway Api Status Message Example
  slug: tyk-gateway-api-status-message-example
- key_count: 9
  name: Tyk Gateway Auth Config Example
  slug: tyk-gateway-auth-config-example
- key_count: 3
  name: Tyk Gateway Auth Provider Meta Example
  slug: tyk-gateway-auth-provider-meta-example
- key_count: 2
  name: Tyk Gateway Auth Source Example
  slug: tyk-gateway-auth-source-example
- key_count: 0
  name: Tyk Gateway Auth Sources Example
  slug: tyk-gateway-auth-sources-example
- key_count: 3
  name: Tyk Gateway Authentication Example
  slug: tyk-gateway-authentication-example
- key_count: 4
  name: Tyk Gateway Authentication Plugin Example
  slug: tyk-gateway-authentication-plugin-example
- key_count: 2
  name: Tyk Gateway Basic Auth Data Example
  slug: tyk-gateway-basic-auth-data-example
- key_count: 3
  name: Tyk Gateway Batch Reply Unit Example
  slug: tyk-gateway-batch-reply-unit-example
- key_count: 2
  name: Tyk Gateway Batch Request Structure Example
  slug: tyk-gateway-batch-request-structure-example
- key_count: 0
  name: Tyk Gateway Boolean Query Param Example
  slug: tyk-gateway-boolean-query-param-example
- key_count: 7
  name: Tyk Gateway Cache Example
  slug: tyk-gateway-cache-example
- key_count: 6
  name: Tyk Gateway Cache Meta Example
  slug: tyk-gateway-cache-meta-example
- key_count: 7
  name: Tyk Gateway Cache Options Example
  slug: tyk-gateway-cache-options-example
- key_count: 4
  name: Tyk Gateway Cache Plugin Example
  slug: tyk-gateway-cache-plugin-example
- key_count: 1
  name: Tyk Gateway Certificate Pinning Example
  slug: tyk-gateway-certificate-pinning-example
- key_count: 8
  name: Tyk Gateway Certs Certificate Basics Example
  slug: tyk-gateway-certs-certificate-basics-example
- key_count: 7
  name: Tyk Gateway Certs Certificate Meta Example
  slug: tyk-gateway-certs-certificate-meta-example
- key_count: 2
  name: Tyk Gateway Check Command Example
  slug: tyk-gateway-check-command-example
- key_count: 5
  name: Tyk Gateway Circuit Breaker Example
  slug: tyk-gateway-circuit-breaker-example
- key_count: 7
  name: Tyk Gateway Circuit Breaker Meta Example
  slug: tyk-gateway-circuit-breaker-meta-example
- key_count: 2
  name: Tyk Gateway Client Certificates Example
  slug: tyk-gateway-client-certificates-example
- key_count: 2
  name: Tyk Gateway Client To Policy Example
  slug: tyk-gateway-client-to-policy-example
- key_count: 1
  name: Tyk Gateway Context Variables Example
  slug: tyk-gateway-context-variables-example
- key_count: 9
  name: Tyk Gateway Cors Config Example
  slug: tyk-gateway-cors-config-example
- key_count: 9
  name: Tyk Gateway Cors Example
  slug: tyk-gateway-cors-example
- key_count: 1
  name: Tyk Gateway Custom Plugin Authentication Example
  slug: tyk-gateway-custom-plugin-authentication-example
- key_count: 5
  name: Tyk Gateway Custom Plugin Example
  slug: tyk-gateway-custom-plugin-example
- key_count: 0
  name: Tyk Gateway Custom Plugins Example
  slug: tyk-gateway-custom-plugins-example
- key_count: 2
  name: Tyk Gateway Datasource Mapping Configuration Example
  slug: tyk-gateway-datasource-mapping-configuration-example
- key_count: 2
  name: Tyk Gateway Datasource Source Config Example
  slug: tyk-gateway-datasource-source-config-example
- key_count: 2
  name: Tyk Gateway Datasource Type Field Configuration Example
  slug: tyk-gateway-datasource-type-field-configuration-example
- key_count: 1
  name: Tyk Gateway Detailed Activity Logs Example
  slug: tyk-gateway-detailed-activity-logs-example
- key_count: 1
  name: Tyk Gateway Detailed Tracing Example
  slug: tyk-gateway-detailed-tracing-example
- key_count: 3
  name: Tyk Gateway Domain Example
  slug: tyk-gateway-domain-example
- key_count: 2
  name: Tyk Gateway Domain To Certificate Example
  slug: tyk-gateway-domain-to-certificate-example
- key_count: 5
  name: Tyk Gateway End Point Meta Example
  slug: tyk-gateway-end-point-meta-example
- key_count: 1
  name: Tyk Gateway Endpoint Example
  slug: tyk-gateway-endpoint-example
- key_count: 1
  name: Tyk Gateway Endpoint Method Example
  slug: tyk-gateway-endpoint-method-example
- key_count: 4
  name: Tyk Gateway Endpoint Method Meta Example
  slug: tyk-gateway-endpoint-method-meta-example
- key_count: 0
  name: Tyk Gateway Endpoint Methods Example
  slug: tyk-gateway-endpoint-methods-example
- key_count: 4
  name: Tyk Gateway Endpoint Post Plugin Example
  slug: tyk-gateway-endpoint-post-plugin-example
- key_count: 0
  name: Tyk Gateway Endpoint Post Plugins Example
  slug: tyk-gateway-endpoint-post-plugins-example
- key_count: 0
  name: Tyk Gateway Endpoints Example
  slug: tyk-gateway-endpoints-example
- key_count: 2
  name: Tyk Gateway Enforce Timeout Example
  slug: tyk-gateway-enforce-timeout-example
- key_count: 5
  name: Tyk Gateway Event Handler Example
  slug: tyk-gateway-event-handler-example
- key_count: 1
  name: Tyk Gateway Event Handler Meta Config Example
  slug: tyk-gateway-event-handler-meta-config-example
- key_count: 2
  name: Tyk Gateway Event Handler Trigger Config Example
  slug: tyk-gateway-event-handler-trigger-config-example
- key_count: 0
  name: Tyk Gateway Event Handlers Example
  slug: tyk-gateway-event-handlers-example
- key_count: 26
  name: Tyk Gateway Extended Paths Set Example
  slug: tyk-gateway-extended-paths-set-example
- key_count: 2
  name: Tyk Gateway External O Auth Example
  slug: tyk-gateway-external-o-auth-example
- key_count: 2
  name: Tyk Gateway Field Access Definition Example
  slug: tyk-gateway-field-access-definition-example
- key_count: 1
  name: Tyk Gateway Field Limits Example
  slug: tyk-gateway-field-limits-example
- key_count: 4
  name: Tyk Gateway From Oas Examples Example
  slug: tyk-gateway-from-oas-examples-example
- key_count: 2
  name: Tyk Gateway Gateway Tags Example
  slug: tyk-gateway-gateway-tags-example
- key_count: 0
  name: Tyk Gateway Global Example
  slug: tyk-gateway-global-example
- key_count: 3
  name: Tyk Gateway Global Rate Limit Example
  slug: tyk-gateway-global-rate-limit-example
- key_count: 5
  name: Tyk Gateway Go Plugin Meta Example
  slug: tyk-gateway-go-plugin-meta-example
- key_count: 0
  name: Tyk Gateway Graph Access Definition Example
  slug: tyk-gateway-graph-access-definition-example
- key_count: 6
  name: Tyk Gateway Graph Ql Config Example
  slug: tyk-gateway-graph-ql-config-example
- key_count: 3
  name: Tyk Gateway Graph Ql Engine Config Example
  slug: tyk-gateway-graph-ql-engine-config-example
- key_count: 5
  name: Tyk Gateway Graph Ql Engine Data Source Example
  slug: tyk-gateway-graph-ql-engine-data-source-example
- key_count: 4
  name: Tyk Gateway Graph Ql Field Config Example
  slug: tyk-gateway-graph-ql-field-config-example
- key_count: 1
  name: Tyk Gateway Graph Ql Introspection Config Example
  slug: tyk-gateway-graph-ql-introspection-config-example
- key_count: 2
  name: Tyk Gateway Graph Ql Playground Example
  slug: tyk-gateway-graph-ql-playground-example
- key_count: 4
  name: Tyk Gateway Graph Ql Proxy Config Example
  slug: tyk-gateway-graph-ql-proxy-config-example
- key_count: 1
  name: Tyk Gateway Graph Ql Proxy Features Config Example
  slug: tyk-gateway-graph-ql-proxy-features-config-example
- key_count: 1
  name: Tyk Gateway Graph Ql Response Extensions Example
  slug: tyk-gateway-graph-ql-response-extensions-example
- key_count: 1
  name: Tyk Gateway Graph Ql Subgraph Config Example
  slug: tyk-gateway-graph-ql-subgraph-config-example
- key_count: 6
  name: Tyk Gateway Graph Ql Subgraph Entity Example
  slug: tyk-gateway-graph-ql-subgraph-entity-example
- key_count: 5
  name: Tyk Gateway Graph Ql Supergraph Config Example
  slug: tyk-gateway-graph-ql-supergraph-config-example
- key_count: 2
  name: Tyk Gateway Graph Ql Type Fields Example
  slug: tyk-gateway-graph-ql-type-fields-example
- key_count: 2
  name: Tyk Gateway Graphql Type Example
  slug: tyk-gateway-graphql-type-example
- key_count: 4
  name: Tyk Gateway Hard Timeout Meta Example
  slug: tyk-gateway-hard-timeout-meta-example
- key_count: 2
  name: Tyk Gateway Header Example
  slug: tyk-gateway-header-example
- key_count: 6
  name: Tyk Gateway Header Injection Meta Example
  slug: tyk-gateway-header-injection-meta-example
- key_count: 0
  name: Tyk Gateway Headers Example
  slug: tyk-gateway-headers-example
- key_count: 5
  name: Tyk Gateway Health Check Item Example
  slug: tyk-gateway-health-check-item-example
- key_count: 5
  name: Tyk Gateway Health Check Response Example
  slug: tyk-gateway-health-check-response-example
- key_count: 3
  name: Tyk Gateway Hmac Example
  slug: tyk-gateway-hmac-example
- key_count: 8
  name: Tyk Gateway Host Check Object Example
  slug: tyk-gateway-host-check-object-example
- key_count: 0
  name: Tyk Gateway Http Header Example
  slug: tyk-gateway-http-header-example
- key_count: 5
  name: Tyk Gateway Id Extractor Config Example
  slug: tyk-gateway-id-extractor-config-example
- key_count: 3
  name: Tyk Gateway Id Extractor Example
  slug: tyk-gateway-id-extractor-example
- key_count: 5
  name: Tyk Gateway Info Example
  slug: tyk-gateway-info-example
- key_count: 1
  name: Tyk Gateway Internal Example
  slug: tyk-gateway-internal-example
- key_count: 3
  name: Tyk Gateway Internal Meta Example
  slug: tyk-gateway-internal-meta-example
- key_count: 2
  name: Tyk Gateway Introspection Cache Example
  slug: tyk-gateway-introspection-cache-example
- key_count: 5
  name: Tyk Gateway Introspection Example
  slug: tyk-gateway-introspection-example
- key_count: 1
  name: Tyk Gateway Jwt Data Example
  slug: tyk-gateway-jwt-data-example
- key_count: 7
  name: Tyk Gateway Jwt Validation Example
  slug: tyk-gateway-jwt-validation-example
- key_count: 2
  name: Tyk Gateway Listen Path Example
  slug: tyk-gateway-listen-path-example
- key_count: 4
  name: Tyk Gateway Method Transform Meta Example
  slug: tyk-gateway-method-transform-meta-example
- key_count: 5
  name: Tyk Gateway Middleware Definition Example
  slug: tyk-gateway-middleware-definition-example
- key_count: 0
  name: Tyk Gateway Middleware Example
  slug: tyk-gateway-middleware-example
- key_count: 4
  name: Tyk Gateway Middleware Id Extractor Example
  slug: tyk-gateway-middleware-id-extractor-example
- key_count: 5
  name: Tyk Gateway Middleware Section Example
  slug: tyk-gateway-middleware-section-example
- key_count: 3
  name: Tyk Gateway Mock Response Example
  slug: tyk-gateway-mock-response-example
- key_count: 7
  name: Tyk Gateway Mock Response Meta Example
  slug: tyk-gateway-mock-response-meta-example
- key_count: 1
  name: Tyk Gateway Monitor Example
  slug: tyk-gateway-monitor-example
- key_count: 2
  name: Tyk Gateway Mutual Tls Example
  slug: tyk-gateway-mutual-tls-example
- key_count: 7
  name: Tyk Gateway New Client Request Example
  slug: tyk-gateway-new-client-request-example
- key_count: 2
  name: Tyk Gateway Notifications Manager Example
  slug: tyk-gateway-notifications-manager-example
- key_count: 2
  name: Tyk Gateway O Auth Client Token Example
  slug: tyk-gateway-o-auth-client-token-example
- key_count: 3
  name: Tyk Gateway Oas Schema Response Example
  slug: tyk-gateway-oas-schema-response-example
- key_count: 2
  name: Tyk Gateway Oid Provider Config Example
  slug: tyk-gateway-oid-provider-config-example
- key_count: 3
  name: Tyk Gateway Oidc Example
  slug: tyk-gateway-oidc-example
- key_count: 2
  name: Tyk Gateway Open Id Options Example
  slug: tyk-gateway-open-id-options-example
- key_count: 0
  name: Tyk Gateway Operation Example
  slug: tyk-gateway-operation-example
- key_count: 0
  name: Tyk Gateway Operations Example
  slug: tyk-gateway-operations-example
- key_count: 1
  name: Tyk Gateway Paginated O Auth Client Tokens Example
  slug: tyk-gateway-paginated-o-auth-client-tokens-example
- key_count: 3
  name: Tyk Gateway Pagination Status Example
  slug: tyk-gateway-pagination-status-example
- key_count: 4
  name: Tyk Gateway Persist Graph Ql Meta Example
  slug: tyk-gateway-persist-graph-ql-meta-example
- key_count: 2
  name: Tyk Gateway Pinned Public Key Example
  slug: tyk-gateway-pinned-public-key-example
- key_count: 0
  name: Tyk Gateway Pinned Public Keys Example
  slug: tyk-gateway-pinned-public-keys-example
- key_count: 0
  name: Tyk Gateway Pkix Name Example
  slug: tyk-gateway-pkix-name-example
- key_count: 2
  name: Tyk Gateway Plugin Bundle Example
  slug: tyk-gateway-plugin-bundle-example
- key_count: 2
  name: Tyk Gateway Plugin Config Data Example
  slug: tyk-gateway-plugin-config-data-example
- key_count: 1
  name: Tyk Gateway Plugin Config Example
  slug: tyk-gateway-plugin-config-example
- key_count: 21
  name: Tyk Gateway Policy Example
  slug: tyk-gateway-policy-example
- key_count: 5
  name: Tyk Gateway Policy Partitions Example
  slug: tyk-gateway-policy-partitions-example
- key_count: 2
  name: Tyk Gateway Policy Update Obj Example
  slug: tyk-gateway-policy-update-obj-example
- key_count: 0
  name: Tyk Gateway Post Authentication Plugin Example
  slug: tyk-gateway-post-authentication-plugin-example
- key_count: 0
  name: Tyk Gateway Post Plugin Example
  slug: tyk-gateway-post-plugin-example
- key_count: 0
  name: Tyk Gateway Pre Plugin Example
  slug: tyk-gateway-pre-plugin-example
- key_count: 0
  name: Tyk Gateway Provider Example
  slug: tyk-gateway-provider-example
- key_count: 2
  name: Tyk Gateway Provider Type2 Example
  slug: tyk-gateway-provider-type2-example
- key_count: 9
  name: Tyk Gateway Proxy Config Example
  slug: tyk-gateway-proxy-config-example
- key_count: 3
  name: Tyk Gateway Rate Limit Endpoint Example
  slug: tyk-gateway-rate-limit-endpoint-example
- key_count: 3
  name: Tyk Gateway Rate Limit Example
  slug: tyk-gateway-rate-limit-example
- key_count: 5
  name: Tyk Gateway Rate Limit Meta Example
  slug: tyk-gateway-rate-limit-meta-example
- key_count: 5
  name: Tyk Gateway Rate Limit Smoothing Example
  slug: tyk-gateway-rate-limit-smoothing-example
- key_count: 2
  name: Tyk Gateway Rate Limit Type2 Example
  slug: tyk-gateway-rate-limit-type2-example
- key_count: 4
  name: Tyk Gateway Request Definition Example
  slug: tyk-gateway-request-definition-example
- key_count: 2
  name: Tyk Gateway Request Headers Rewrite Config Example
  slug: tyk-gateway-request-headers-rewrite-config-example
- key_count: 7
  name: Tyk Gateway Request Signing Meta Example
  slug: tyk-gateway-request-signing-meta-example
- key_count: 2
  name: Tyk Gateway Request Size Limit Example
  slug: tyk-gateway-request-size-limit-example
- key_count: 4
  name: Tyk Gateway Request Size Meta Example
  slug: tyk-gateway-request-size-meta-example
- key_count: 0
  name: Tyk Gateway Response Plugin Example
  slug: tyk-gateway-response-plugin-example
- key_count: 2
  name: Tyk Gateway Response Processor Example
  slug: tyk-gateway-response-processor-example
- key_count: 2
  name: Tyk Gateway Routing Trigger Example
  slug: tyk-gateway-routing-trigger-example
- key_count: 5
  name: Tyk Gateway Routing Trigger Options Example
  slug: tyk-gateway-routing-trigger-options-example
- key_count: 2
  name: Tyk Gateway Scope Claim Example
  slug: tyk-gateway-scope-claim-example
- key_count: 2
  name: Tyk Gateway Scope To Policy Example
  slug: tyk-gateway-scope-to-policy-example
- key_count: 0
  name: Tyk Gateway Scopes Example
  slug: tyk-gateway-scopes-example
- key_count: 2
  name: Tyk Gateway Scopes Type2 Example
  slug: tyk-gateway-scopes-type2-example
- key_count: 0
  name: Tyk Gateway Security Schemes Example
  slug: tyk-gateway-security-schemes-example
- key_count: 0
  name: Tyk Gateway Server Example
  slug: tyk-gateway-server-example
- key_count: 2
  name: Tyk Gateway Service Discovery Cache Example
  slug: tyk-gateway-service-discovery-cache-example
- key_count: 11
  name: Tyk Gateway Service Discovery Configuration Example
  slug: tyk-gateway-service-discovery-configuration-example
- key_count: 10
  name: Tyk Gateway Service Discovery Example
  slug: tyk-gateway-service-discovery-example
- key_count: 3
  name: Tyk Gateway Session Provider Meta Example
  slug: tyk-gateway-session-provider-meta-example
- key_count: 34
  name: Tyk Gateway Session State Example
  slug: tyk-gateway-session-state-example
- key_count: 8
  name: Tyk Gateway Signature Config Example
  slug: tyk-gateway-signature-config-example
- key_count: 2
  name: Tyk Gateway State Example
  slug: tyk-gateway-state-example
- key_count: 2
  name: Tyk Gateway String Regex Map Example
  slug: tyk-gateway-string-regex-map-example
- key_count: 4
  name: Tyk Gateway Template Data Example
  slug: tyk-gateway-template-data-example
- key_count: 3
  name: Tyk Gateway Template Meta Example
  slug: tyk-gateway-template-meta-example
- key_count: 0
  name: Tyk Gateway Test Example
  slug: tyk-gateway-test-example
- key_count: 3
  name: Tyk Gateway Trace Http Request Example
  slug: tyk-gateway-trace-http-request-example
- key_count: 0
  name: Tyk Gateway Trace Request Example
  slug: tyk-gateway-trace-request-example
- key_count: 3
  name: Tyk Gateway Trace Response Example
  slug: tyk-gateway-trace-response-example
- key_count: 1
  name: Tyk Gateway Track Endpoint Example
  slug: tyk-gateway-track-endpoint-example
- key_count: 3
  name: Tyk Gateway Track Endpoint Meta Example
  slug: tyk-gateway-track-endpoint-meta-example
- key_count: 1
  name: Tyk Gateway Traffic Logs Example
  slug: tyk-gateway-traffic-logs-example
- key_count: 4
  name: Tyk Gateway Transform Body Example
  slug: tyk-gateway-transform-body-example
- key_count: 2
  name: Tyk Gateway Transform Headers Example
  slug: tyk-gateway-transform-headers-example
- key_count: 3
  name: Tyk Gateway Transform Jq Meta Example
  slug: tyk-gateway-transform-jq-meta-example
- key_count: 2
  name: Tyk Gateway Transform Request Method Example
  slug: tyk-gateway-transform-request-method-example
- key_count: 2
  name: Tyk Gateway Udg Global Header Example
  slug: tyk-gateway-udg-global-header-example
- key_count: 1
  name: Tyk Gateway Upstream Example
  slug: tyk-gateway-upstream-example
- key_count: 2
  name: Tyk Gateway Uptime Tests Config Example
  slug: tyk-gateway-uptime-tests-config-example
- key_count: 1
  name: Tyk Gateway Uptime Tests Example
  slug: tyk-gateway-uptime-tests-example
- key_count: 4
  name: Tyk Gateway Url Rewrite Example
  slug: tyk-gateway-url-rewrite-example
- key_count: 6
  name: Tyk Gateway Url Rewrite Meta Example
  slug: tyk-gateway-url-rewrite-meta-example
- key_count: 4
  name: Tyk Gateway Url Rewrite Rule Example
  slug: tyk-gateway-url-rewrite-rule-example
- key_count: 3
  name: Tyk Gateway Url Rewrite Trigger Example
  slug: tyk-gateway-url-rewrite-trigger-example
- key_count: 6
  name: Tyk Gateway Validate Path Meta Example
  slug: tyk-gateway-validate-path-meta-example
- key_count: 2
  name: Tyk Gateway Validate Request Example
  slug: tyk-gateway-validate-request-example
- key_count: 4
  name: Tyk Gateway Validate Request Meta Example
  slug: tyk-gateway-validate-request-meta-example
- key_count: 3
  name: Tyk Gateway Version Data Example
  slug: tyk-gateway-version-data-example
- key_count: 10
  name: Tyk Gateway Version Definition Example
  slug: tyk-gateway-version-definition-example
- key_count: 13
  name: Tyk Gateway Version Info Example
  slug: tyk-gateway-version-info-example
- key_count: 6
  name: Tyk Gateway Version Meta Example
  slug: tyk-gateway-version-meta-example
- key_count: 2
  name: Tyk Gateway Version Metas Example
  slug: tyk-gateway-version-metas-example
- key_count: 2
  name: Tyk Gateway Version To Id Example
  slug: tyk-gateway-version-to-id-example
- key_count: 9
  name: Tyk Gateway Versioning Example
  slug: tyk-gateway-versioning-example
- key_count: 7
  name: Tyk Gateway Virtual Endpoint Example
  slug: tyk-gateway-virtual-endpoint-example
- key_count: 8
  name: Tyk Gateway Virtual Meta Example
  slug: tyk-gateway-virtual-meta-example
- key_count: 0
  name: Tyk Gateway X Tyk Api Gateway Example
  slug: tyk-gateway-x-tyk-api-gateway-example
- key_count: 3
  name: Tyk Mdcb Component Readiness Example
  slug: tyk-mdcb-component-readiness-example
- key_count: 3
  name: Tyk Mdcb Component Readiness Failure Example
  slug: tyk-mdcb-component-readiness-failure-example
- key_count: 3
  name: Tyk Mdcb Component Status Example
  slug: tyk-mdcb-component-status-example
- key_count: 30
  name: Tyk Mdcb Config Status Example
  slug: tyk-mdcb-config-status-example
- key_count: 1
  name: Tyk Mdcb Error Example
  slug: tyk-mdcb-error-example
- key_count: 0
  name: Tyk Mdcb Health Example
  slug: tyk-mdcb-health-example
- key_count: 3
  name: Tyk Mdcb Host Details Example
  slug: tyk-mdcb-host-details-example
- key_count: 2
  name: Tyk Mdcb Liveness Status Example
  slug: tyk-mdcb-liveness-status-example
- key_count: 6
  name: Tyk Mdcb Node Example
  slug: tyk-mdcb-node-example
- key_count: 3
  name: Tyk Mdcb Readiness Failure Example
  slug: tyk-mdcb-readiness-failure-example
- key_count: 3
  name: Tyk Mdcb Readiness Status Example
  slug: tyk-mdcb-readiness-status-example
- key_count: 2
  name: Tyk Mdcb Stats Example
  slug: tyk-mdcb-stats-example
features:
- description: High-performance, open-source API gateway supporting REST, GraphQL, gRPC, TCP, and async APIs with low-latency request proxying.
  name: API Gateway
- description: Configurable rate limiting and throttling policies to protect backend services from traffic spikes and abuse.
  name: Rate Limiting
- description: Multiple authentication methods including API keys, JWT, OAuth 2.0, mutual TLS, OpenID Connect, and basic auth.
  name: Authentication
- description: Real-time API analytics, traffic monitoring, and detailed logging with export to multiple backend stores.
  name: Analytics and Monitoring
- description: Customizable developer portal for API documentation, key management, and developer onboarding.
  name: Developer Portal
- description: Native GraphQL proxy and Universal Data Graph for federating REST and GraphQL APIs into a single graph endpoint.
  name: GraphQL Support
- description: Built-in support for API versioning with URL, header, and query parameter-based version routing.
  name: API Versioning
- description: Centralized access control policies for managing rate limits, quotas, and access rights across multiple APIs.
  name: Policy Management
- description: MDCB enables synchronization of API configurations and keys across geographically distributed gateway clusters.
  name: Multi Data Center
- description: Extensible middleware plugin system supporting Go, Python, JavaScript, Lua, and gRPC-based custom plugins.
  name: Plugin System
- description: Tyk AI Studio provides an AI gateway for managing, governing, and interacting with AI models across your organization.
  name: AI Gateway
finops:
- name: Tyk Finops
  service_category: API Management
  slug: tyk-finops
graphqls:
- description: ''
  name: Tyk GraphQL API
  slug: tyk-graphql
image: /assets/icons/tyk.png
integrations:
- description: Tyk Operator provides native Kubernetes integration for managing API definitions and policies as custom resources.
  name: Kubernetes
- description: Infrastructure-as-code provider for managing Tyk configurations through Terraform.
  name: Terraform
- description: Integration with Keycloak for OAuth 2.0 and OpenID Connect authentication flows.
  name: Keycloak
- description: Support for Auth0 as an identity provider for JWT validation and OAuth 2.0 token management.
  name: Auth0
- description: Export gateway metrics to Prometheus for monitoring and alerting with Grafana dashboards.
  name: Prometheus
- description: Distributed tracing integration with OpenTelemetry for end-to-end request visibility.
  name: OpenTelemetry
- description: Backstage plugin for viewing and managing Tyk API definitions from within the Backstage developer portal.
  name: Backstage
- description: CI/CD integration for automated API deployment and configuration updates through Jenkins pipelines.
  name: Jenkins
- description: Ansible playbooks for automated Tyk gateway and dashboard provisioning and configuration.
  name: Ansible
- description: Official Helm charts for deploying Tyk components on Kubernetes clusters.
  name: Helm Charts
json_schemas:
- name: AccessDefinition
  property_count: 9
  slug: tyk-gateway-access-definition
- name: AccessSpec
  property_count: 2
  slug: tyk-gateway-access-spec
- name: Allowance
  property_count: 2
  slug: tyk-gateway-allowance
- name: AnalyticsPluginConfig
  property_count: 3
  slug: tyk-gateway-analytics-plugin-config
- name: APIAllCertificateBasics
  property_count: 1
  slug: tyk-gateway-api-all-certificate-basics
- name: APIAllCertificates
  property_count: 1
  slug: tyk-gateway-api-all-certificates
- name: ApiAllKeys
  property_count: 1
  slug: tyk-gateway-api-all-keys
- name: APICertificateStatusMessage
  property_count: 3
  slug: tyk-gateway-api-certificate-status-message
- name: APIDefinition
  property_count: 74
  slug: tyk-gateway-api-definition
- name: APILimit
  property_count: 9
  slug: tyk-gateway-api-limit
- name: ApiModifyKeySuccess
  property_count: 4
  slug: tyk-gateway-api-modify-key-success
- name: ApiStatusMessage
  property_count: 2
  slug: tyk-gateway-api-status-message
- name: AuthConfig
  property_count: 9
  slug: tyk-gateway-auth-config
- name: AuthProviderMeta
  property_count: 3
  slug: tyk-gateway-auth-provider-meta
- name: AuthSource
  property_count: 2
  slug: tyk-gateway-auth-source
- name: AuthSources
  property_count: 0
  slug: tyk-gateway-auth-sources
- name: AuthenticationPlugin
  property_count: 4
  slug: tyk-gateway-authentication-plugin
- name: Authentication
  property_count: 3
  slug: tyk-gateway-authentication
- name: BasicAuthData
  property_count: 2
  slug: tyk-gateway-basic-auth-data
- name: BatchReplyUnit
  property_count: 3
  slug: tyk-gateway-batch-reply-unit
- name: BatchRequestStructure
  property_count: 2
  slug: tyk-gateway-batch-request-structure
- name: BooleanQueryParam
  property_count: 0
  slug: tyk-gateway-boolean-query-param
- name: CacheMeta
  property_count: 6
  slug: tyk-gateway-cache-meta
- name: CacheOptions
  property_count: 7
  slug: tyk-gateway-cache-options
- name: CachePlugin
  property_count: 4
  slug: tyk-gateway-cache-plugin
- name: Cache
  property_count: 7
  slug: tyk-gateway-cache
- name: CertificatePinning
  property_count: 1
  slug: tyk-gateway-certificate-pinning
- name: CertsCertificateBasics
  property_count: 8
  slug: tyk-gateway-certs-certificate-basics
- name: CertsCertificateMeta
  property_count: 7
  slug: tyk-gateway-certs-certificate-meta
- name: CheckCommand
  property_count: 2
  slug: tyk-gateway-check-command
- name: CircuitBreakerMeta
  property_count: 7
  slug: tyk-gateway-circuit-breaker-meta
- name: CircuitBreaker
  property_count: 5
  slug: tyk-gateway-circuit-breaker
- name: ClientCertificates
  property_count: 2
  slug: tyk-gateway-client-certificates
- name: ClientToPolicy
  property_count: 2
  slug: tyk-gateway-client-to-policy
- name: ContextVariables
  property_count: 1
  slug: tyk-gateway-context-variables
- name: CORSConfig
  property_count: 9
  slug: tyk-gateway-cors-config
- name: CORS
  property_count: 9
  slug: tyk-gateway-cors
- name: CustomPluginAuthentication
  property_count: 1
  slug: tyk-gateway-custom-plugin-authentication
- name: CustomPlugin
  property_count: 5
  slug: tyk-gateway-custom-plugin
- name: CustomPlugins
  property_count: 0
  slug: tyk-gateway-custom-plugins
- name: DatasourceMappingConfiguration
  property_count: 2
  slug: tyk-gateway-datasource-mapping-configuration
- name: DatasourceSourceConfig
  property_count: 2
  slug: tyk-gateway-datasource-source-config
- name: DatasourceTypeFieldConfiguration
  property_count: 2
  slug: tyk-gateway-datasource-type-field-configuration
- name: DetailedActivityLogs
  property_count: 1
  slug: tyk-gateway-detailed-activity-logs
- name: DetailedTracing
  property_count: 1
  slug: tyk-gateway-detailed-tracing
- name: Domain
  property_count: 3
  slug: tyk-gateway-domain
- name: DomainToCertificate
  property_count: 2
  slug: tyk-gateway-domain-to-certificate
- name: EndPointMeta
  property_count: 5
  slug: tyk-gateway-end-point-meta
- name: EndpointMethodMeta
  property_count: 4
  slug: tyk-gateway-endpoint-method-meta
- name: EndpointMethod
  property_count: 1
  slug: tyk-gateway-endpoint-method
- name: EndpointMethods
  property_count: 0
  slug: tyk-gateway-endpoint-methods
- name: EndpointPostPlugin
  property_count: 4
  slug: tyk-gateway-endpoint-post-plugin
- name: EndpointPostPlugins
  property_count: 0
  slug: tyk-gateway-endpoint-post-plugins
- name: Endpoint
  property_count: 1
  slug: tyk-gateway-endpoint
- name: Endpoints
  property_count: 0
  slug: tyk-gateway-endpoints
- name: EnforceTimeout
  property_count: 2
  slug: tyk-gateway-enforce-timeout
- name: EventHandlerMetaConfig
  property_count: 1
  slug: tyk-gateway-event-handler-meta-config
- name: EventHandler
  property_count: 5
  slug: tyk-gateway-event-handler
- name: EventHandlerTriggerConfig
  property_count: 2
  slug: tyk-gateway-event-handler-trigger-config
- name: EventHandlers
  property_count: 0
  slug: tyk-gateway-event-handlers
- name: ExtendedPathsSet
  property_count: 26
  slug: tyk-gateway-extended-paths-set
- name: ExternalOAuth
  property_count: 2
  slug: tyk-gateway-external-o-auth
- name: FieldAccessDefinition
  property_count: 2
  slug: tyk-gateway-field-access-definition
- name: FieldLimits
  property_count: 1
  slug: tyk-gateway-field-limits
- name: FromOASExamples
  property_count: 4
  slug: tyk-gateway-from-oas-examples
- name: GatewayTags
  property_count: 2
  slug: tyk-gateway-gateway-tags
- name: GlobalRateLimit
  property_count: 3
  slug: tyk-gateway-global-rate-limit
- name: Global
  property_count: 0
  slug: tyk-gateway-global
- name: GoPluginMeta
  property_count: 5
  slug: tyk-gateway-go-plugin-meta
- name: GraphAccessDefinition
  property_count: 0
  slug: tyk-gateway-graph-access-definition
- name: GraphQLConfig
  property_count: 6
  slug: tyk-gateway-graph-ql-config
- name: GraphQLEngineConfig
  property_count: 3
  slug: tyk-gateway-graph-ql-engine-config
- name: GraphQLEngineDataSource
  property_count: 5
  slug: tyk-gateway-graph-ql-engine-data-source
- name: GraphQLFieldConfig
  property_count: 4
  slug: tyk-gateway-graph-ql-field-config
- name: GraphQLIntrospectionConfig
  property_count: 1
  slug: tyk-gateway-graph-ql-introspection-config
- name: GraphQLPlayground
  property_count: 2
  slug: tyk-gateway-graph-ql-playground
- name: GraphQLProxyConfig
  property_count: 4
  slug: tyk-gateway-graph-ql-proxy-config
- name: GraphQLProxyFeaturesConfig
  property_count: 1
  slug: tyk-gateway-graph-ql-proxy-features-config
- name: GraphQLResponseExtensions
  property_count: 1
  slug: tyk-gateway-graph-ql-response-extensions
- name: GraphQLSubgraphConfig
  property_count: 1
  slug: tyk-gateway-graph-ql-subgraph-config
- name: GraphQLSubgraphEntity
  property_count: 6
  slug: tyk-gateway-graph-ql-subgraph-entity
- name: GraphQLSupergraphConfig
  property_count: 5
  slug: tyk-gateway-graph-ql-supergraph-config
- name: GraphQLTypeFields
  property_count: 2
  slug: tyk-gateway-graph-ql-type-fields
- name: GraphqlType
  property_count: 2
  slug: tyk-gateway-graphql-type
- name: HardTimeoutMeta
  property_count: 4
  slug: tyk-gateway-hard-timeout-meta
- name: HeaderInjectionMeta
  property_count: 6
  slug: tyk-gateway-header-injection-meta
- name: Header
  property_count: 2
  slug: tyk-gateway-header
- name: Headers
  property_count: 0
  slug: tyk-gateway-headers
- name: HealthCheckItem
  property_count: 5
  slug: tyk-gateway-health-check-item
- name: HealthCheckResponse
  property_count: 5
  slug: tyk-gateway-health-check-response
- name: HMAC
  property_count: 3
  slug: tyk-gateway-hmac
- name: HostCheckObject
  property_count: 8
  slug: tyk-gateway-host-check-object
- name: HttpHeader
  property_count: 0
  slug: tyk-gateway-http-header
- name: IDExtractorConfig
  property_count: 5
  slug: tyk-gateway-id-extractor-config
- name: IDExtractor
  property_count: 3
  slug: tyk-gateway-id-extractor
- name: Info
  property_count: 5
  slug: tyk-gateway-info
- name: InternalMeta
  property_count: 3
  slug: tyk-gateway-internal-meta
- name: Internal
  property_count: 1
  slug: tyk-gateway-internal
- name: IntrospectionCache
  property_count: 2
  slug: tyk-gateway-introspection-cache
- name: Introspection
  property_count: 5
  slug: tyk-gateway-introspection
- name: JWTData
  property_count: 1
  slug: tyk-gateway-jwt-data
- name: JWTValidation
  property_count: 7
  slug: tyk-gateway-jwt-validation
- name: ListenPath
  property_count: 2
  slug: tyk-gateway-listen-path
- name: MethodTransformMeta
  property_count: 4
  slug: tyk-gateway-method-transform-meta
- name: MiddlewareDefinition
  property_count: 5
  slug: tyk-gateway-middleware-definition
- name: MiddlewareIdExtractor
  property_count: 4
  slug: tyk-gateway-middleware-id-extractor
- name: Middleware
  property_count: 0
  slug: tyk-gateway-middleware
- name: MiddlewareSection
  property_count: 5
  slug: tyk-gateway-middleware-section
- name: MockResponseMeta
  property_count: 7
  slug: tyk-gateway-mock-response-meta
- name: MockResponse
  property_count: 3
  slug: tyk-gateway-mock-response
- name: Monitor
  property_count: 1
  slug: tyk-gateway-monitor
- name: MutualTLS
  property_count: 2
  slug: tyk-gateway-mutual-tls
- name: NewClientRequest
  property_count: 7
  slug: tyk-gateway-new-client-request
- name: NotificationsManager
  property_count: 2
  slug: tyk-gateway-notifications-manager
- name: OAuthClientToken
  property_count: 2
  slug: tyk-gateway-o-auth-client-token
- name: OASSchemaResponse
  property_count: 3
  slug: tyk-gateway-oas-schema-response
- name: OIDProviderConfig
  property_count: 2
  slug: tyk-gateway-oid-provider-config
- name: OIDC
  property_count: 3
  slug: tyk-gateway-oidc
- name: OpenIDOptions
  property_count: 2
  slug: tyk-gateway-open-id-options
- name: Operation
  property_count: 0
  slug: tyk-gateway-operation
- name: Operations
  property_count: 0
  slug: tyk-gateway-operations
- name: PaginatedOAuthClientTokens
  property_count: 1
  slug: tyk-gateway-paginated-o-auth-client-tokens
- name: PaginationStatus
  property_count: 3
  slug: tyk-gateway-pagination-status
- name: PersistGraphQLMeta
  property_count: 4
  slug: tyk-gateway-persist-graph-ql-meta
- name: PinnedPublicKey
  property_count: 2
  slug: tyk-gateway-pinned-public-key
- name: PinnedPublicKeys
  property_count: 0
  slug: tyk-gateway-pinned-public-keys
- name: PkixName
  property_count: 0
  slug: tyk-gateway-pkix-name
- name: PluginBundle
  property_count: 2
  slug: tyk-gateway-plugin-bundle
- name: PluginConfigData
  property_count: 2
  slug: tyk-gateway-plugin-config-data
- name: PluginConfig
  property_count: 1
  slug: tyk-gateway-plugin-config
- name: PolicyPartitions
  property_count: 5
  slug: tyk-gateway-policy-partitions
- name: Policy
  property_count: 21
  slug: tyk-gateway-policy
- name: PolicyUpdateObj
  property_count: 2
  slug: tyk-gateway-policy-update-obj
- name: PostAuthenticationPlugin
  property_count: 0
  slug: tyk-gateway-post-authentication-plugin
- name: PostPlugin
  property_count: 0
  slug: tyk-gateway-post-plugin
- name: PrePlugin
  property_count: 0
  slug: tyk-gateway-pre-plugin
- name: Provider
  property_count: 0
  slug: tyk-gateway-provider
- name: ProviderType2
  property_count: 2
  slug: tyk-gateway-provider-type2
- name: ProxyConfig
  property_count: 9
  slug: tyk-gateway-proxy-config
- name: RateLimitEndpoint
  property_count: 3
  slug: tyk-gateway-rate-limit-endpoint
- name: RateLimitMeta
  property_count: 5
  slug: tyk-gateway-rate-limit-meta
- name: RateLimit
  property_count: 3
  slug: tyk-gateway-rate-limit
- name: RateLimitSmoothing
  property_count: 5
  slug: tyk-gateway-rate-limit-smoothing
- name: RateLimitType2
  property_count: 2
  slug: tyk-gateway-rate-limit-type2
- name: RequestDefinition
  property_count: 4
  slug: tyk-gateway-request-definition
- name: RequestHeadersRewriteConfig
  property_count: 2
  slug: tyk-gateway-request-headers-rewrite-config
- name: RequestSigningMeta
  property_count: 7
  slug: tyk-gateway-request-signing-meta
- name: RequestSizeLimit
  property_count: 2
  slug: tyk-gateway-request-size-limit
- name: RequestSizeMeta
  property_count: 4
  slug: tyk-gateway-request-size-meta
- name: ResponsePlugin
  property_count: 0
  slug: tyk-gateway-response-plugin
- name: ResponseProcessor
  property_count: 2
  slug: tyk-gateway-response-processor
- name: RoutingTriggerOptions
  property_count: 5
  slug: tyk-gateway-routing-trigger-options
- name: RoutingTrigger
  property_count: 2
  slug: tyk-gateway-routing-trigger
- name: ScopeClaim
  property_count: 2
  slug: tyk-gateway-scope-claim
- name: ScopeToPolicy
  property_count: 2
  slug: tyk-gateway-scope-to-policy
- name: Scopes
  property_count: 0
  slug: tyk-gateway-scopes
- name: ScopesType2
  property_count: 2
  slug: tyk-gateway-scopes-type2
- name: SecuritySchemes
  property_count: 0
  slug: tyk-gateway-security-schemes
- name: Server
  property_count: 0
  slug: tyk-gateway-server
- name: ServiceDiscoveryCache
  property_count: 2
  slug: tyk-gateway-service-discovery-cache
- name: ServiceDiscoveryConfiguration
  property_count: 11
  slug: tyk-gateway-service-discovery-configuration
- name: ServiceDiscovery
  property_count: 10
  slug: tyk-gateway-service-discovery
- name: SessionProviderMeta
  property_count: 3
  slug: tyk-gateway-session-provider-meta
- name: SessionState
  property_count: 34
  slug: tyk-gateway-session-state
- name: SignatureConfig
  property_count: 8
  slug: tyk-gateway-signature-config
- name: State
  property_count: 2
  slug: tyk-gateway-state
- name: StringRegexMap
  property_count: 2
  slug: tyk-gateway-string-regex-map
- name: TemplateData
  property_count: 4
  slug: tyk-gateway-template-data
- name: TemplateMeta
  property_count: 3
  slug: tyk-gateway-template-meta
- name: Test
  property_count: 0
  slug: tyk-gateway-test
- name: TraceHttpRequest
  property_count: 3
  slug: tyk-gateway-trace-http-request
- name: TraceRequest
  property_count: 0
  slug: tyk-gateway-trace-request
- name: TraceResponse
  property_count: 3
  slug: tyk-gateway-trace-response
- name: TrackEndpointMeta
  property_count: 3
  slug: tyk-gateway-track-endpoint-meta
- name: TrackEndpoint
  property_count: 1
  slug: tyk-gateway-track-endpoint
- name: TrafficLogs
  property_count: 1
  slug: tyk-gateway-traffic-logs
- name: TransformBody
  property_count: 4
  slug: tyk-gateway-transform-body
- name: TransformHeaders
  property_count: 2
  slug: tyk-gateway-transform-headers
- name: TransformJQMeta
  property_count: 3
  slug: tyk-gateway-transform-jq-meta
- name: TransformRequestMethod
  property_count: 2
  slug: tyk-gateway-transform-request-method
- name: UDGGlobalHeader
  property_count: 2
  slug: tyk-gateway-udg-global-header
- name: Upstream
  property_count: 1
  slug: tyk-gateway-upstream
- name: UptimeTestsConfig
  property_count: 2
  slug: tyk-gateway-uptime-tests-config
- name: UptimeTests
  property_count: 1
  slug: tyk-gateway-uptime-tests
- name: URLRewriteMeta
  property_count: 6
  slug: tyk-gateway-url-rewrite-meta
- name: URLRewriteRule
  property_count: 4
  slug: tyk-gateway-url-rewrite-rule
- name: URLRewrite
  property_count: 4
  slug: tyk-gateway-url-rewrite
- name: URLRewriteTrigger
  property_count: 3
  slug: tyk-gateway-url-rewrite-trigger
- name: ValidatePathMeta
  property_count: 6
  slug: tyk-gateway-validate-path-meta
- name: ValidateRequestMeta
  property_count: 4
  slug: tyk-gateway-validate-request-meta
- name: ValidateRequest
  property_count: 2
  slug: tyk-gateway-validate-request
- name: VersionData
  property_count: 3
  slug: tyk-gateway-version-data
- name: VersionDefinition
  property_count: 10
  slug: tyk-gateway-version-definition
- name: VersionInfo
  property_count: 13
  slug: tyk-gateway-version-info
- name: VersionMeta
  property_count: 6
  slug: tyk-gateway-version-meta
- name: VersionMetas
  property_count: 2
  slug: tyk-gateway-version-metas
- name: VersionToID
  property_count: 2
  slug: tyk-gateway-version-to-id
- name: Versioning
  property_count: 9
  slug: tyk-gateway-versioning
- name: VirtualEndpoint
  property_count: 7
  slug: tyk-gateway-virtual-endpoint
- name: VirtualMeta
  property_count: 8
  slug: tyk-gateway-virtual-meta
- name: XTykAPIGateway
  property_count: 0
  slug: tyk-gateway-x-tyk-api-gateway
- name: ComponentReadinessFailure
  property_count: 3
  slug: tyk-mdcb-component-readiness-failure
- name: ComponentReadiness
  property_count: 3
  slug: tyk-mdcb-component-readiness
- name: ComponentStatus
  property_count: 3
  slug: tyk-mdcb-component-status
- name: ConfigStatus
  property_count: 30
  slug: tyk-mdcb-config-status
- name: Error
  property_count: 1
  slug: tyk-mdcb-error
- name: Health
  property_count: 0
  slug: tyk-mdcb-health
- name: HostDetails
  property_count: 3
  slug: tyk-mdcb-host-details
- name: LivenessStatus
  property_count: 2
  slug: tyk-mdcb-liveness-status
- name: Node
  property_count: 6
  slug: tyk-mdcb-node
- name: ReadinessFailure
  property_count: 3
  slug: tyk-mdcb-readiness-failure
- name: ReadinessStatus
  property_count: 3
  slug: tyk-mdcb-readiness-status
- name: Stats
  property_count: 2
  slug: tyk-mdcb-stats
json_structures:
- name: Tyk Gateway Access Definition Structure
  property_count: 9
  slug: tyk-gateway-access-definition-structure
- name: Tyk Gateway Access Spec Structure
  property_count: 2
  slug: tyk-gateway-access-spec-structure
- name: Tyk Gateway Allowance Structure
  property_count: 2
  slug: tyk-gateway-allowance-structure
- name: Tyk Gateway Analytics Plugin Config Structure
  property_count: 3
  slug: tyk-gateway-analytics-plugin-config-structure
- name: Tyk Gateway Api All Certificate Basics Structure
  property_count: 1
  slug: tyk-gateway-api-all-certificate-basics-structure
- name: Tyk Gateway Api All Certificates Structure
  property_count: 1
  slug: tyk-gateway-api-all-certificates-structure
- name: Tyk Gateway Api All Keys Structure
  property_count: 1
  slug: tyk-gateway-api-all-keys-structure
- name: Tyk Gateway Api Certificate Status Message Structure
  property_count: 3
  slug: tyk-gateway-api-certificate-status-message-structure
- name: Tyk Gateway Api Definition Structure
  property_count: 74
  slug: tyk-gateway-api-definition-structure
- name: Tyk Gateway Api Limit Structure
  property_count: 9
  slug: tyk-gateway-api-limit-structure
- name: Tyk Gateway Api Modify Key Success Structure
  property_count: 4
  slug: tyk-gateway-api-modify-key-success-structure
- name: Tyk Gateway Api Status Message Structure
  property_count: 2
  slug: tyk-gateway-api-status-message-structure
- name: Tyk Gateway Auth Config Structure
  property_count: 9
  slug: tyk-gateway-auth-config-structure
- name: Tyk Gateway Auth Provider Meta Structure
  property_count: 3
  slug: tyk-gateway-auth-provider-meta-structure
- name: Tyk Gateway Auth Source Structure
  property_count: 2
  slug: tyk-gateway-auth-source-structure
- name: Tyk Gateway Auth Sources Structure
  property_count: 0
  slug: tyk-gateway-auth-sources-structure
- name: Tyk Gateway Authentication Plugin Structure
  property_count: 4
  slug: tyk-gateway-authentication-plugin-structure
- name: Tyk Gateway Authentication Structure
  property_count: 3
  slug: tyk-gateway-authentication-structure
- name: Tyk Gateway Basic Auth Data Structure
  property_count: 2
  slug: tyk-gateway-basic-auth-data-structure
- name: Tyk Gateway Batch Reply Unit Structure
  property_count: 3
  slug: tyk-gateway-batch-reply-unit-structure
- name: Tyk Gateway Batch Request Structure Structure
  property_count: 2
  slug: tyk-gateway-batch-request-structure-structure
- name: Tyk Gateway Boolean Query Param Structure
  property_count: 0
  slug: tyk-gateway-boolean-query-param-structure
- name: Tyk Gateway Cache Meta Structure
  property_count: 6
  slug: tyk-gateway-cache-meta-structure
- name: Tyk Gateway Cache Options Structure
  property_count: 7
  slug: tyk-gateway-cache-options-structure
- name: Tyk Gateway Cache Plugin Structure
  property_count: 4
  slug: tyk-gateway-cache-plugin-structure
- name: Tyk Gateway Cache Structure
  property_count: 7
  slug: tyk-gateway-cache-structure
- name: Tyk Gateway Certificate Pinning Structure
  property_count: 1
  slug: tyk-gateway-certificate-pinning-structure
- name: Tyk Gateway Certs Certificate Basics Structure
  property_count: 8
  slug: tyk-gateway-certs-certificate-basics-structure
- name: Tyk Gateway Certs Certificate Meta Structure
  property_count: 7
  slug: tyk-gateway-certs-certificate-meta-structure
- name: Tyk Gateway Check Command Structure
  property_count: 2
  slug: tyk-gateway-check-command-structure
- name: Tyk Gateway Circuit Breaker Meta Structure
  property_count: 7
  slug: tyk-gateway-circuit-breaker-meta-structure
- name: Tyk Gateway Circuit Breaker Structure
  property_count: 5
  slug: tyk-gateway-circuit-breaker-structure
- name: Tyk Gateway Client Certificates Structure
  property_count: 2
  slug: tyk-gateway-client-certificates-structure
- name: Tyk Gateway Client To Policy Structure
  property_count: 2
  slug: tyk-gateway-client-to-policy-structure
- name: Tyk Gateway Context Variables Structure
  property_count: 1
  slug: tyk-gateway-context-variables-structure
- name: Tyk Gateway Cors Config Structure
  property_count: 9
  slug: tyk-gateway-cors-config-structure
- name: Tyk Gateway Cors Structure
  property_count: 9
  slug: tyk-gateway-cors-structure
- name: Tyk Gateway Custom Plugin Authentication Structure
  property_count: 1
  slug: tyk-gateway-custom-plugin-authentication-structure
- name: Tyk Gateway Custom Plugin Structure
  property_count: 5
  slug: tyk-gateway-custom-plugin-structure
- name: Tyk Gateway Custom Plugins Structure
  property_count: 0
  slug: tyk-gateway-custom-plugins-structure
- name: Tyk Gateway Datasource Mapping Configuration Structure
  property_count: 2
  slug: tyk-gateway-datasource-mapping-configuration-structure
- name: Tyk Gateway Datasource Source Config Structure
  property_count: 2
  slug: tyk-gateway-datasource-source-config-structure
- name: Tyk Gateway Datasource Type Field Configuration Structure
  property_count: 2
  slug: tyk-gateway-datasource-type-field-configuration-structure
- name: Tyk Gateway Detailed Activity Logs Structure
  property_count: 1
  slug: tyk-gateway-detailed-activity-logs-structure
- name: Tyk Gateway Detailed Tracing Structure
  property_count: 1
  slug: tyk-gateway-detailed-tracing-structure
- name: Tyk Gateway Domain Structure
  property_count: 3
  slug: tyk-gateway-domain-structure
- name: Tyk Gateway Domain To Certificate Structure
  property_count: 2
  slug: tyk-gateway-domain-to-certificate-structure
- name: Tyk Gateway End Point Meta Structure
  property_count: 5
  slug: tyk-gateway-end-point-meta-structure
- name: Tyk Gateway Endpoint Method Meta Structure
  property_count: 4
  slug: tyk-gateway-endpoint-method-meta-structure
- name: Tyk Gateway Endpoint Method Structure
  property_count: 1
  slug: tyk-gateway-endpoint-method-structure
- name: Tyk Gateway Endpoint Methods Structure
  property_count: 0
  slug: tyk-gateway-endpoint-methods-structure
- name: Tyk Gateway Endpoint Post Plugin Structure
  property_count: 4
  slug: tyk-gateway-endpoint-post-plugin-structure
- name: Tyk Gateway Endpoint Post Plugins Structure
  property_count: 0
  slug: tyk-gateway-endpoint-post-plugins-structure
- name: Tyk Gateway Endpoint Structure
  property_count: 1
  slug: tyk-gateway-endpoint-structure
- name: Tyk Gateway Endpoints Structure
  property_count: 0
  slug: tyk-gateway-endpoints-structure
- name: Tyk Gateway Enforce Timeout Structure
  property_count: 2
  slug: tyk-gateway-enforce-timeout-structure
- name: Tyk Gateway Event Handler Meta Config Structure
  property_count: 1
  slug: tyk-gateway-event-handler-meta-config-structure
- name: Tyk Gateway Event Handler Structure
  property_count: 5
  slug: tyk-gateway-event-handler-structure
- name: Tyk Gateway Event Handler Trigger Config Structure
  property_count: 2
  slug: tyk-gateway-event-handler-trigger-config-structure
- name: Tyk Gateway Event Handlers Structure
  property_count: 0
  slug: tyk-gateway-event-handlers-structure
- name: Tyk Gateway Extended Paths Set Structure
  property_count: 26
  slug: tyk-gateway-extended-paths-set-structure
- name: Tyk Gateway External O Auth Structure
  property_count: 2
  slug: tyk-gateway-external-o-auth-structure
- name: Tyk Gateway Field Access Definition Structure
  property_count: 2
  slug: tyk-gateway-field-access-definition-structure
- name: Tyk Gateway Field Limits Structure
  property_count: 1
  slug: tyk-gateway-field-limits-structure
- name: Tyk Gateway From Oas Examples Structure
  property_count: 4
  slug: tyk-gateway-from-oas-examples-structure
- name: Tyk Gateway Gateway Tags Structure
  property_count: 2
  slug: tyk-gateway-gateway-tags-structure
- name: Tyk Gateway Global Rate Limit Structure
  property_count: 3
  slug: tyk-gateway-global-rate-limit-structure
- name: Tyk Gateway Global Structure
  property_count: 0
  slug: tyk-gateway-global-structure
- name: Tyk Gateway Go Plugin Meta Structure
  property_count: 5
  slug: tyk-gateway-go-plugin-meta-structure
- name: Tyk Gateway Graph Access Definition Structure
  property_count: 0
  slug: tyk-gateway-graph-access-definition-structure
- name: Tyk Gateway Graph Ql Config Structure
  property_count: 6
  slug: tyk-gateway-graph-ql-config-structure
- name: Tyk Gateway Graph Ql Engine Config Structure
  property_count: 3
  slug: tyk-gateway-graph-ql-engine-config-structure
- name: Tyk Gateway Graph Ql Engine Data Source Structure
  property_count: 5
  slug: tyk-gateway-graph-ql-engine-data-source-structure
- name: Tyk Gateway Graph Ql Field Config Structure
  property_count: 4
  slug: tyk-gateway-graph-ql-field-config-structure
- name: Tyk Gateway Graph Ql Introspection Config Structure
  property_count: 1
  slug: tyk-gateway-graph-ql-introspection-config-structure
- name: Tyk Gateway Graph Ql Playground Structure
  property_count: 2
  slug: tyk-gateway-graph-ql-playground-structure
- name: Tyk Gateway Graph Ql Proxy Config Structure
  property_count: 4
  slug: tyk-gateway-graph-ql-proxy-config-structure
- name: Tyk Gateway Graph Ql Proxy Features Config Structure
  property_count: 1
  slug: tyk-gateway-graph-ql-proxy-features-config-structure
- name: Tyk Gateway Graph Ql Response Extensions Structure
  property_count: 1
  slug: tyk-gateway-graph-ql-response-extensions-structure
- name: Tyk Gateway Graph Ql Subgraph Config Structure
  property_count: 1
  slug: tyk-gateway-graph-ql-subgraph-config-structure
- name: Tyk Gateway Graph Ql Subgraph Entity Structure
  property_count: 6
  slug: tyk-gateway-graph-ql-subgraph-entity-structure
- name: Tyk Gateway Graph Ql Supergraph Config Structure
  property_count: 5
  slug: tyk-gateway-graph-ql-supergraph-config-structure
- name: Tyk Gateway Graph Ql Type Fields Structure
  property_count: 2
  slug: tyk-gateway-graph-ql-type-fields-structure
- name: Tyk Gateway Graphql Type Structure
  property_count: 2
  slug: tyk-gateway-graphql-type-structure
- name: Tyk Gateway Hard Timeout Meta Structure
  property_count: 4
  slug: tyk-gateway-hard-timeout-meta-structure
- name: Tyk Gateway Header Injection Meta Structure
  property_count: 6
  slug: tyk-gateway-header-injection-meta-structure
- name: Tyk Gateway Header Structure
  property_count: 2
  slug: tyk-gateway-header-structure
- name: Tyk Gateway Headers Structure
  property_count: 0
  slug: tyk-gateway-headers-structure
- name: Tyk Gateway Health Check Item Structure
  property_count: 5
  slug: tyk-gateway-health-check-item-structure
- name: Tyk Gateway Health Check Response Structure
  property_count: 5
  slug: tyk-gateway-health-check-response-structure
- name: Tyk Gateway Hmac Structure
  property_count: 3
  slug: tyk-gateway-hmac-structure
- name: Tyk Gateway Host Check Object Structure
  property_count: 8
  slug: tyk-gateway-host-check-object-structure
- name: Tyk Gateway Http Header Structure
  property_count: 0
  slug: tyk-gateway-http-header-structure
- name: Tyk Gateway Id Extractor Config Structure
  property_count: 5
  slug: tyk-gateway-id-extractor-config-structure
- name: Tyk Gateway Id Extractor Structure
  property_count: 3
  slug: tyk-gateway-id-extractor-structure
- name: Tyk Gateway Info Structure
  property_count: 5
  slug: tyk-gateway-info-structure
- name: Tyk Gateway Internal Meta Structure
  property_count: 3
  slug: tyk-gateway-internal-meta-structure
- name: Tyk Gateway Internal Structure
  property_count: 1
  slug: tyk-gateway-internal-structure
- name: Tyk Gateway Introspection Cache Structure
  property_count: 2
  slug: tyk-gateway-introspection-cache-structure
- name: Tyk Gateway Introspection Structure
  property_count: 5
  slug: tyk-gateway-introspection-structure
- name: Tyk Gateway Jwt Data Structure
  property_count: 1
  slug: tyk-gateway-jwt-data-structure
- name: Tyk Gateway Jwt Validation Structure
  property_count: 7
  slug: tyk-gateway-jwt-validation-structure
- name: Tyk Gateway Listen Path Structure
  property_count: 2
  slug: tyk-gateway-listen-path-structure
- name: Tyk Gateway Method Transform Meta Structure
  property_count: 4
  slug: tyk-gateway-method-transform-meta-structure
- name: Tyk Gateway Middleware Definition Structure
  property_count: 5
  slug: tyk-gateway-middleware-definition-structure
- name: Tyk Gateway Middleware Id Extractor Structure
  property_count: 4
  slug: tyk-gateway-middleware-id-extractor-structure
- name: Tyk Gateway Middleware Section Structure
  property_count: 5
  slug: tyk-gateway-middleware-section-structure
- name: Tyk Gateway Middleware Structure
  property_count: 0
  slug: tyk-gateway-middleware-structure
- name: Tyk Gateway Mock Response Meta Structure
  property_count: 7
  slug: tyk-gateway-mock-response-meta-structure
- name: Tyk Gateway Mock Response Structure
  property_count: 3
  slug: tyk-gateway-mock-response-structure
- name: Tyk Gateway Monitor Structure
  property_count: 1
  slug: tyk-gateway-monitor-structure
- name: Tyk Gateway Mutual Tls Structure
  property_count: 2
  slug: tyk-gateway-mutual-tls-structure
- name: Tyk Gateway New Client Request Structure
  property_count: 7
  slug: tyk-gateway-new-client-request-structure
- name: Tyk Gateway Notifications Manager Structure
  property_count: 2
  slug: tyk-gateway-notifications-manager-structure
- name: Tyk Gateway O Auth Client Token Structure
  property_count: 2
  slug: tyk-gateway-o-auth-client-token-structure
- name: Tyk Gateway Oas Schema Response Structure
  property_count: 3
  slug: tyk-gateway-oas-schema-response-structure
- name: Tyk Gateway Oid Provider Config Structure
  property_count: 2
  slug: tyk-gateway-oid-provider-config-structure
- name: Tyk Gateway Oidc Structure
  property_count: 3
  slug: tyk-gateway-oidc-structure
- name: Tyk Gateway Open Id Options Structure
  property_count: 2
  slug: tyk-gateway-open-id-options-structure
- name: Tyk Gateway Operation Structure
  property_count: 0
  slug: tyk-gateway-operation-structure
- name: Tyk Gateway Operations Structure
  property_count: 0
  slug: tyk-gateway-operations-structure
- name: Tyk Gateway Paginated O Auth Client Tokens Structure
  property_count: 1
  slug: tyk-gateway-paginated-o-auth-client-tokens-structure
- name: Tyk Gateway Pagination Status Structure
  property_count: 3
  slug: tyk-gateway-pagination-status-structure
- name: Tyk Gateway Persist Graph Ql Meta Structure
  property_count: 4
  slug: tyk-gateway-persist-graph-ql-meta-structure
- name: Tyk Gateway Pinned Public Key Structure
  property_count: 2
  slug: tyk-gateway-pinned-public-key-structure
- name: Tyk Gateway Pinned Public Keys Structure
  property_count: 0
  slug: tyk-gateway-pinned-public-keys-structure
- name: Tyk Gateway Pkix Name Structure
  property_count: 0
  slug: tyk-gateway-pkix-name-structure
- name: Tyk Gateway Plugin Bundle Structure
  property_count: 2
  slug: tyk-gateway-plugin-bundle-structure
- name: Tyk Gateway Plugin Config Data Structure
  property_count: 2
  slug: tyk-gateway-plugin-config-data-structure
- name: Tyk Gateway Plugin Config Structure
  property_count: 1
  slug: tyk-gateway-plugin-config-structure
- name: Tyk Gateway Policy Partitions Structure
  property_count: 5
  slug: tyk-gateway-policy-partitions-structure
- name: Tyk Gateway Policy Structure
  property_count: 21
  slug: tyk-gateway-policy-structure
- name: Tyk Gateway Policy Update Obj Structure
  property_count: 2
  slug: tyk-gateway-policy-update-obj-structure
- name: Tyk Gateway Post Authentication Plugin Structure
  property_count: 0
  slug: tyk-gateway-post-authentication-plugin-structure
- name: Tyk Gateway Post Plugin Structure
  property_count: 0
  slug: tyk-gateway-post-plugin-structure
- name: Tyk Gateway Pre Plugin Structure
  property_count: 0
  slug: tyk-gateway-pre-plugin-structure
- name: Tyk Gateway Provider Structure
  property_count: 0
  slug: tyk-gateway-provider-structure
- name: Tyk Gateway Provider Type2 Structure
  property_count: 2
  slug: tyk-gateway-provider-type2-structure
- name: Tyk Gateway Proxy Config Structure
  property_count: 9
  slug: tyk-gateway-proxy-config-structure
- name: Tyk Gateway Rate Limit Endpoint Structure
  property_count: 3
  slug: tyk-gateway-rate-limit-endpoint-structure
- name: Tyk Gateway Rate Limit Meta Structure
  property_count: 5
  slug: tyk-gateway-rate-limit-meta-structure
- name: Tyk Gateway Rate Limit Smoothing Structure
  property_count: 5
  slug: tyk-gateway-rate-limit-smoothing-structure
- name: Tyk Gateway Rate Limit Structure
  property_count: 3
  slug: tyk-gateway-rate-limit-structure
- name: Tyk Gateway Rate Limit Type2 Structure
  property_count: 2
  slug: tyk-gateway-rate-limit-type2-structure
- name: Tyk Gateway Request Definition Structure
  property_count: 4
  slug: tyk-gateway-request-definition-structure
- name: Tyk Gateway Request Headers Rewrite Config Structure
  property_count: 2
  slug: tyk-gateway-request-headers-rewrite-config-structure
- name: Tyk Gateway Request Signing Meta Structure
  property_count: 7
  slug: tyk-gateway-request-signing-meta-structure
- name: Tyk Gateway Request Size Limit Structure
  property_count: 2
  slug: tyk-gateway-request-size-limit-structure
- name: Tyk Gateway Request Size Meta Structure
  property_count: 4
  slug: tyk-gateway-request-size-meta-structure
- name: Tyk Gateway Response Plugin Structure
  property_count: 0
  slug: tyk-gateway-response-plugin-structure
- name: Tyk Gateway Response Processor Structure
  property_count: 2
  slug: tyk-gateway-response-processor-structure
- name: Tyk Gateway Routing Trigger Options Structure
  property_count: 5
  slug: tyk-gateway-routing-trigger-options-structure
- name: Tyk Gateway Routing Trigger Structure
  property_count: 2
  slug: tyk-gateway-routing-trigger-structure
- name: Tyk Gateway Scope Claim Structure
  property_count: 2
  slug: tyk-gateway-scope-claim-structure
- name: Tyk Gateway Scope To Policy Structure
  property_count: 2
  slug: tyk-gateway-scope-to-policy-structure
- name: Tyk Gateway Scopes Structure
  property_count: 0
  slug: tyk-gateway-scopes-structure
- name: Tyk Gateway Scopes Type2 Structure
  property_count: 2
  slug: tyk-gateway-scopes-type2-structure
- name: Tyk Gateway Security Schemes Structure
  property_count: 0
  slug: tyk-gateway-security-schemes-structure
- name: Tyk Gateway Server Structure
  property_count: 0
  slug: tyk-gateway-server-structure
- name: Tyk Gateway Service Discovery Cache Structure
  property_count: 2
  slug: tyk-gateway-service-discovery-cache-structure
- name: Tyk Gateway Service Discovery Configuration Structure
  property_count: 11
  slug: tyk-gateway-service-discovery-configuration-structure
- name: Tyk Gateway Service Discovery Structure
  property_count: 10
  slug: tyk-gateway-service-discovery-structure
- name: Tyk Gateway Session Provider Meta Structure
  property_count: 3
  slug: tyk-gateway-session-provider-meta-structure
- name: Tyk Gateway Session State Structure
  property_count: 34
  slug: tyk-gateway-session-state-structure
- name: Tyk Gateway Signature Config Structure
  property_count: 8
  slug: tyk-gateway-signature-config-structure
- name: Tyk Gateway State Structure
  property_count: 2
  slug: tyk-gateway-state-structure
- name: Tyk Gateway String Regex Map Structure
  property_count: 2
  slug: tyk-gateway-string-regex-map-structure
- name: Tyk Gateway Template Data Structure
  property_count: 4
  slug: tyk-gateway-template-data-structure
- name: Tyk Gateway Template Meta Structure
  property_count: 3
  slug: tyk-gateway-template-meta-structure
- name: Tyk Gateway Test Structure
  property_count: 0
  slug: tyk-gateway-test-structure
- name: Tyk Gateway Trace Http Request Structure
  property_count: 3
  slug: tyk-gateway-trace-http-request-structure
- name: Tyk Gateway Trace Request Structure
  property_count: 0
  slug: tyk-gateway-trace-request-structure
- name: Tyk Gateway Trace Response Structure
  property_count: 3
  slug: tyk-gateway-trace-response-structure
- name: Tyk Gateway Track Endpoint Meta Structure
  property_count: 3
  slug: tyk-gateway-track-endpoint-meta-structure
- name: Tyk Gateway Track Endpoint Structure
  property_count: 1
  slug: tyk-gateway-track-endpoint-structure
- name: Tyk Gateway Traffic Logs Structure
  property_count: 1
  slug: tyk-gateway-traffic-logs-structure
- name: Tyk Gateway Transform Body Structure
  property_count: 4
  slug: tyk-gateway-transform-body-structure
- name: Tyk Gateway Transform Headers Structure
  property_count: 2
  slug: tyk-gateway-transform-headers-structure
- name: Tyk Gateway Transform Jq Meta Structure
  property_count: 3
  slug: tyk-gateway-transform-jq-meta-structure
- name: Tyk Gateway Transform Request Method Structure
  property_count: 2
  slug: tyk-gateway-transform-request-method-structure
- name: Tyk Gateway Udg Global Header Structure
  property_count: 2
  slug: tyk-gateway-udg-global-header-structure
- name: Tyk Gateway Upstream Structure
  property_count: 1
  slug: tyk-gateway-upstream-structure
- name: Tyk Gateway Uptime Tests Config Structure
  property_count: 2
  slug: tyk-gateway-uptime-tests-config-structure
- name: Tyk Gateway Uptime Tests Structure
  property_count: 1
  slug: tyk-gateway-uptime-tests-structure
- name: Tyk Gateway Url Rewrite Meta Structure
  property_count: 6
  slug: tyk-gateway-url-rewrite-meta-structure
- name: Tyk Gateway Url Rewrite Rule Structure
  property_count: 4
  slug: tyk-gateway-url-rewrite-rule-structure
- name: Tyk Gateway Url Rewrite Structure
  property_count: 4
  slug: tyk-gateway-url-rewrite-structure
- name: Tyk Gateway Url Rewrite Trigger Structure
  property_count: 3
  slug: tyk-gateway-url-rewrite-trigger-structure
- name: Tyk Gateway Validate Path Meta Structure
  property_count: 6
  slug: tyk-gateway-validate-path-meta-structure
- name: Tyk Gateway Validate Request Meta Structure
  property_count: 4
  slug: tyk-gateway-validate-request-meta-structure
- name: Tyk Gateway Validate Request Structure
  property_count: 2
  slug: tyk-gateway-validate-request-structure
- name: Tyk Gateway Version Data Structure
  property_count: 3
  slug: tyk-gateway-version-data-structure
- name: Tyk Gateway Version Definition Structure
  property_count: 10
  slug: tyk-gateway-version-definition-structure
- name: Tyk Gateway Version Info Structure
  property_count: 13
  slug: tyk-gateway-version-info-structure
- name: Tyk Gateway Version Meta Structure
  property_count: 6
  slug: tyk-gateway-version-meta-structure
- name: Tyk Gateway Version Metas Structure
  property_count: 2
  slug: tyk-gateway-version-metas-structure
- name: Tyk Gateway Version To Id Structure
  property_count: 2
  slug: tyk-gateway-version-to-id-structure
- name: Tyk Gateway Versioning Structure
  property_count: 9
  slug: tyk-gateway-versioning-structure
- name: Tyk Gateway Virtual Endpoint Structure
  property_count: 7
  slug: tyk-gateway-virtual-endpoint-structure
- name: Tyk Gateway Virtual Meta Structure
  property_count: 8
  slug: tyk-gateway-virtual-meta-structure
- name: Tyk Gateway X Tyk Api Gateway Structure
  property_count: 0
  slug: tyk-gateway-x-tyk-api-gateway-structure
- name: Tyk Mdcb Component Readiness Failure Structure
  property_count: 3
  slug: tyk-mdcb-component-readiness-failure-structure
- name: Tyk Mdcb Component Readiness Structure
  property_count: 3
  slug: tyk-mdcb-component-readiness-structure
- name: Tyk Mdcb Component Status Structure
  property_count: 3
  slug: tyk-mdcb-component-status-structure
- name: Tyk Mdcb Config Status Structure
  property_count: 30
  slug: tyk-mdcb-config-status-structure
- name: Tyk Mdcb Error Structure
  property_count: 1
  slug: tyk-mdcb-error-structure
- name: Tyk Mdcb Health Structure
  property_count: 0
  slug: tyk-mdcb-health-structure
- name: Tyk Mdcb Host Details Structure
  property_count: 3
  slug: tyk-mdcb-host-details-structure
- name: Tyk Mdcb Liveness Status Structure
  property_count: 2
  slug: tyk-mdcb-liveness-status-structure
- name: Tyk Mdcb Node Structure
  property_count: 6
  slug: tyk-mdcb-node-structure
- name: Tyk Mdcb Readiness Failure Structure
  property_count: 3
  slug: tyk-mdcb-readiness-failure-structure
- name: Tyk Mdcb Readiness Status Structure
  property_count: 3
  slug: tyk-mdcb-readiness-status-structure
- name: Tyk Mdcb Stats Structure
  property_count: 2
  slug: tyk-mdcb-stats-structure
jsonld:
- class_count: 0
  name: Tyk Gateway Context
  property_count: 0
  slug: tyk-gateway-context
- class_count: 0
  name: Tyk Mdcb Context
  property_count: 0
  slug: tyk-mdcb-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-08-03'
name: Tyk
nav: Providers
network: true
overview: 'Tyk publishes 39 APIs on the [APIs.io](https://apis.io/) network, including Additional Permissions API, Analytics API, APIs API, and 36 more. Tagged areas include API Gateway, API Management, GraphQL, and Open-Source.


  The Tyk catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Tyk''s developer surface includes signup flow, authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, and 26 more developer resources.'
plans:
- name: Tyk Plans Pricing
  plan_count: 5
  slug: tyk-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Tyk Rate Limits
  slug: tyk-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tyk API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tyk-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Tyk API Rules
  rule_count: 16
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 8
  slug: tyk-spectral-rules
score:
  band: strong
  composite: 58.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 28.8
    contract_quality: 65.8
    developer_ergonomics: 65.5
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 52.6
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 39
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tyk/refs/heads/main/screenshots/tyk-2026-06-20T195900.png
security:
- kind: authentication
  name: Tyk Authentication
  slug: tyk-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Tyk Domain Security
  slug: tyk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tyk Vulnerability Disclosure
  slug: tyk-vulnerability-disclosure
  summary_line: disclosure policy published
slug: tyk
tags:
- API Gateway
- API Management
- GraphQL
- Open-Source
use_cases:
- description: Enable API-as-a-product strategies with tiered plans, usage tracking, and developer self-service through the portal.
  name: API Monetization
- description: Centralize traffic management, authentication, and observability for microservices architectures.
  name: Microservices Gateway
- description: Deploy gateways across cloud, on-premise, and hybrid environments with centralized management.
  name: Multi-Cloud API Management
- description: Wrap legacy SOAP and XML APIs with modern REST or GraphQL interfaces using Tyk's transformation middleware.
  name: Legacy API Modernization
- description: Manage third-party developer access with fine-grained policies, quota management, and analytics per consumer.
  name: Partner API Program
- description: Govern and manage AI model APIs with rate limiting, access control, and usage analytics through Tyk AI Studio.
  name: AI API Management
website: https://tyk.io/
---
