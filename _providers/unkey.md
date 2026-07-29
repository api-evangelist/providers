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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 41
  human_in_the_loop: 4
  name: Unkey Agentic Access
  operation_count: 42
  slug: unkey-agentic-access
  summary_line: 42 operations · 41 acting · 4 human-in-the-loop
api_count: 8
apis:
- description: Analytics query operations
  name: Unkey analytics API
  slug: unkey-analytics-api
- description: API management operations
  name: Unkey apis API
  slug: unkey-apis-api
- description: Deployment operations
  name: Unkey deploy API
  slug: unkey-deploy-api
- description: Identity management operations
  name: Unkey identities API
  slug: unkey-identities-api
- description: API key management operations
  name: Unkey keys API
  slug: unkey-keys-api
- description: Health check operations
  name: Unkey liveness API
  slug: unkey-liveness-api
- description: Permission and role management operations
  name: Unkey permissions API
  slug: unkey-permissions-api
- description: Rate limiting operations
  name: Unkey ratelimit API
  slug: unkey-ratelimit-api
artifact_total: 213
collections:
- collection_type: postman
  name: Unkey analytics API
  slug: postman-unkey-analytics-api
- collection_type: postman
  name: Unkey analytics apis API
  slug: postman-unkey-apis-api
- collection_type: postman
  name: Unkey analytics deploy API
  slug: postman-unkey-deploy-api
- collection_type: postman
  name: Unkey analytics identities API
  slug: postman-unkey-identities-api
- collection_type: postman
  name: Unkey analytics keys API
  slug: postman-unkey-keys-api
- collection_type: postman
  name: Unkey analytics liveness API
  slug: postman-unkey-liveness-api
- collection_type: postman
  name: Unkey analytics permissions API
  slug: postman-unkey-permissions-api
- collection_type: postman
  name: Unkey analytics ratelimit API
  slug: postman-unkey-ratelimit-api
- collection_type: open
  name: Unkey API
  slug: open-unkey
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/unkey/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unkey-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unkey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unkey-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unkeyed
- group: company
  title: ''
  type: Website
  url: https://www.unkey.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.unkey.com/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/unkeyed/unkey
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unkey.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.unkey.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.unkey.com/changelog
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/vocabulary/unkey-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/json-ld/unkey-context.jsonld
created: '2026-03-16'
description: Unkey is the developer platform for modern APIs, providing globally distributed API key management, rate limiting, identity management, analytics, and deployment capabilities. The platform enables API providers to issue, verify, and revoke keys with metadata, expiration, usage credits, permissions, and roles — without managing any infrastructure.
examples:
- key_count: 2
  name: Unkey Create Key Example
  slug: unkey-create-key-example
- key_count: 2
  name: Unkey Get Key Example
  slug: unkey-get-key-example
- key_count: 6
  name: Unkey Identitiescreateidentity Example
  slug: unkey-identitiescreateidentity-example
- key_count: 6
  name: Unkey Identitiesdeleteidentity Example
  slug: unkey-identitiesdeleteidentity-example
- key_count: 6
  name: Unkey Identitiesgetidentity Example
  slug: unkey-identitiesgetidentity-example
- key_count: 6
  name: Unkey Identitieslistidentities Example
  slug: unkey-identitieslistidentities-example
- key_count: 6
  name: Unkey Identitiesupdateidentity Example
  slug: unkey-identitiesupdateidentity-example
- key_count: 6
  name: Unkey Keysupdatekey Example
  slug: unkey-keysupdatekey-example
- key_count: 6
  name: Unkey Keysverifykey Example
  slug: unkey-keysverifykey-example
- key_count: 6
  name: Unkey Liveness Example
  slug: unkey-liveness-example
- key_count: 6
  name: Unkey Permissionscreaterole Example
  slug: unkey-permissionscreaterole-example
- key_count: 6
  name: Unkey Permissionsdeletepermission Example
  slug: unkey-permissionsdeletepermission-example
- key_count: 2
  name: Unkey Ratelimit Limit Example
  slug: unkey-ratelimit-limit-example
- key_count: 6
  name: Unkey Ratelimitdeleteoverride Example
  slug: unkey-ratelimitdeleteoverride-example
- key_count: 6
  name: Unkey Ratelimitgetoverride Example
  slug: unkey-ratelimitgetoverride-example
- key_count: 6
  name: Unkey Ratelimitlimit Example
  slug: unkey-ratelimitlimit-example
- key_count: 6
  name: Unkey Ratelimitlistoverrides Example
  slug: unkey-ratelimitlistoverrides-example
- key_count: 6
  name: Unkey Ratelimitmultilimit Example
  slug: unkey-ratelimitmultilimit-example
- key_count: 6
  name: Unkey Ratelimitsetoverride Example
  slug: unkey-ratelimitsetoverride-example
- key_count: 2
  name: Unkey Verify Key Example
  slug: unkey-verify-key-example
features:
- 'Free: 0.25 vCPU / 0.25 GB per instance, 1 concurrent build'
- 'Starter $5/mo: 2 vCPU/2 GB, $5 credits, custom domains'
- 'Pro $25/mo: 8 vCPU/8 GB, $25 credits'
- 'Business $50/mo: 32 vCPU/32 GB, $50 credits'
- Predictable usage-based billing on top of subscription
- 'API Keys: create, verify, list, update, delete'
- 'Rate Limiting: standalone evaluations without keys'
- REST API at api.unkey.com
- 'REST rate limit: 60 req/sec Free, 600 req/sec Pro+'
- Identities for tying multiple keys to a user/account
- Permissions and roles per key
- Multi-namespace ratelimit overrides
- OAuth 2.0 + root keys
- Audit log for key/identity events
- Webhooks for key/identity changes
- Open-source self-hostable
finops:
- name: Unkey Finops
  service_category: API Management
  slug: unkey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unkey.png
json_schemas:
- name: BadRequestErrorDetails
  property_count: 0
  slug: unkey-badrequesterrordetails
- name: BadRequestErrorResponse
  property_count: 2
  slug: unkey-badrequesterrorresponse
- name: BaseError
  property_count: 4
  slug: unkey-baseerror
- name: ConflictErrorResponse
  property_count: 2
  slug: unkey-conflicterrorresponse
- name: EmptyResponse
  property_count: 0
  slug: unkey-emptyresponse
- name: ForbiddenErrorResponse
  property_count: 2
  slug: unkey-forbiddenerrorresponse
- name: GoneErrorResponse
  property_count: 2
  slug: unkey-goneerrorresponse
- name: Unkey Identity
  property_count: 7
  slug: unkey-identity
- name: InternalServerErrorResponse
  property_count: 2
  slug: unkey-internalservererrorresponse
- name: Unkey API Key
  property_count: 20
  slug: unkey-key
- name: KeyCreditsData
  property_count: 2
  slug: unkey-keycreditsdata
- name: KeyCreditsRefill
  property_count: 3
  slug: unkey-keycreditsrefill
- name: KeyResponseData
  property_count: 15
  slug: unkey-keyresponsedata
- name: KeysVerifyKeyCredits
  property_count: 1
  slug: unkey-keysverifykeycredits
- name: KeysVerifyKeyRatelimit
  property_count: 4
  slug: unkey-keysverifykeyratelimit
- name: Meta
  property_count: 1
  slug: unkey-meta
- name: NotFoundErrorResponse
  property_count: 2
  slug: unkey-notfounderrorresponse
- name: Pagination
  property_count: 2
  slug: unkey-pagination
- name: Permission
  property_count: 4
  slug: unkey-permission
- name: PreconditionFailedErrorResponse
  property_count: 2
  slug: unkey-preconditionfailederrorresponse
- name: Unkey Rate Limit Result
  property_count: 4
  slug: unkey-ratelimit
- name: RatelimitOverride
  property_count: 4
  slug: unkey-ratelimitoverride
- name: RatelimitRequest
  property_count: 4
  slug: unkey-ratelimitrequest
- name: RatelimitResponse
  property_count: 5
  slug: unkey-ratelimitresponse
- name: Role
  property_count: 4
  slug: unkey-role
- name: ServiceUnavailableErrorResponse
  property_count: 2
  slug: unkey-serviceunavailableerrorresponse
- name: TooManyRequestsErrorResponse
  property_count: 2
  slug: unkey-toomanyrequestserrorresponse
- name: UnauthorizedErrorResponse
  property_count: 2
  slug: unkey-unauthorizederrorresponse
- name: UnprocessableEntityErrorResponse
  property_count: 2
  slug: unkey-unprocessableentityerrorresponse
- name: UpdateKeyCreditsData
  property_count: 2
  slug: unkey-updatekeycreditsdata
- name: UpdateKeyCreditsRefill
  property_count: 3
  slug: unkey-updatekeycreditsrefill
- name: V2AnalyticsGetVerificationsRequestBody
  property_count: 1
  slug: unkey-v2analyticsgetverificationsrequestbody
- name: V2AnalyticsGetVerificationsResponseBody
  property_count: 2
  slug: unkey-v2analyticsgetverificationsresponsebody
- name: V2AnalyticsGetVerificationsResponseData
  property_count: 0
  slug: unkey-v2analyticsgetverificationsresponsedata
- name: V2ApisCreateApiRequestBody
  property_count: 1
  slug: unkey-v2apiscreateapirequestbody
- name: V2ApisCreateApiResponseBody
  property_count: 2
  slug: unkey-v2apiscreateapiresponsebody
- name: V2ApisCreateApiResponseData
  property_count: 1
  slug: unkey-v2apiscreateapiresponsedata
- name: V2ApisDeleteApiRequestBody
  property_count: 1
  slug: unkey-v2apisdeleteapirequestbody
- name: V2ApisDeleteApiResponseBody
  property_count: 2
  slug: unkey-v2apisdeleteapiresponsebody
- name: V2ApisGetApiRequestBody
  property_count: 1
  slug: unkey-v2apisgetapirequestbody
- name: V2ApisGetApiResponseBody
  property_count: 2
  slug: unkey-v2apisgetapiresponsebody
- name: V2ApisGetApiResponseData
  property_count: 2
  slug: unkey-v2apisgetapiresponsedata
- name: V2ApisListKeysRequestBody
  property_count: 6
  slug: unkey-v2apislistkeysrequestbody
- name: V2ApisListKeysResponseBody
  property_count: 3
  slug: unkey-v2apislistkeysresponsebody
- name: V2ApisListKeysResponseData
  property_count: 0
  slug: unkey-v2apislistkeysresponsedata
- name: V2DeployCreateDeploymentRequestBody
  property_count: 7
  slug: unkey-v2deploycreatedeploymentrequestbody
- name: V2DeployCreateDeploymentResponseBody
  property_count: 2
  slug: unkey-v2deploycreatedeploymentresponsebody
- name: V2DeployCreateDeploymentResponseData
  property_count: 1
  slug: unkey-v2deploycreatedeploymentresponsedata
- name: V2DeployDeploymentStep
  property_count: 4
  slug: unkey-v2deploydeploymentstep
- name: V2DeployGetDeploymentRequestBody
  property_count: 1
  slug: unkey-v2deploygetdeploymentrequestbody
- name: V2DeployGetDeploymentResponseBody
  property_count: 2
  slug: unkey-v2deploygetdeploymentresponsebody
- name: V2DeployGetDeploymentResponseData
  property_count: 5
  slug: unkey-v2deploygetdeploymentresponsedata
- name: V2DeployGitCommit
  property_count: 5
  slug: unkey-v2deploygitcommit
- name: V2IdentitiesCreateIdentityRequestBody
  property_count: 3
  slug: unkey-v2identitiescreateidentityrequestbody
- name: V2IdentitiesCreateIdentityResponseBody
  property_count: 2
  slug: unkey-v2identitiescreateidentityresponsebody
- name: V2IdentitiesCreateIdentityResponseData
  property_count: 1
  slug: unkey-v2identitiescreateidentityresponsedata
- name: V2IdentitiesDeleteIdentityRequestBody
  property_count: 1
  slug: unkey-v2identitiesdeleteidentityrequestbody
- name: V2IdentitiesDeleteIdentityResponseBody
  property_count: 1
  slug: unkey-v2identitiesdeleteidentityresponsebody
- name: V2IdentitiesGetIdentityRequestBody
  property_count: 1
  slug: unkey-v2identitiesgetidentityrequestbody
- name: V2IdentitiesGetIdentityResponseBody
  property_count: 2
  slug: unkey-v2identitiesgetidentityresponsebody
- name: V2IdentitiesListIdentitiesRequestBody
  property_count: 2
  slug: unkey-v2identitieslistidentitiesrequestbody
- name: V2IdentitiesListIdentitiesResponseBody
  property_count: 3
  slug: unkey-v2identitieslistidentitiesresponsebody
- name: V2IdentitiesListIdentitiesResponseData
  property_count: 0
  slug: unkey-v2identitieslistidentitiesresponsedata
- name: V2IdentitiesUpdateIdentityRequestBody
  property_count: 3
  slug: unkey-v2identitiesupdateidentityrequestbody
- name: V2IdentitiesUpdateIdentityResponseBody
  property_count: 2
  slug: unkey-v2identitiesupdateidentityresponsebody
- name: V2KeysAddPermissionsRequestBody
  property_count: 2
  slug: unkey-v2keysaddpermissionsrequestbody
- name: V2KeysAddPermissionsResponseBody
  property_count: 2
  slug: unkey-v2keysaddpermissionsresponsebody
- name: V2KeysAddPermissionsResponseData
  property_count: 0
  slug: unkey-v2keysaddpermissionsresponsedata
- name: V2KeysAddRolesRequestBody
  property_count: 2
  slug: unkey-v2keysaddrolesrequestbody
- name: V2KeysAddRolesResponseBody
  property_count: 2
  slug: unkey-v2keysaddrolesresponsebody
- name: V2KeysAddRolesResponseData
  property_count: 0
  slug: unkey-v2keysaddrolesresponsedata
- name: V2KeysCreateKeyRequestBody
  property_count: 13
  slug: unkey-v2keyscreatekeyrequestbody
- name: V2KeysCreateKeyResponseBody
  property_count: 2
  slug: unkey-v2keyscreatekeyresponsebody
- name: V2KeysCreateKeyResponseData
  property_count: 2
  slug: unkey-v2keyscreatekeyresponsedata
- name: V2KeysDeleteKeyRequestBody
  property_count: 2
  slug: unkey-v2keysdeletekeyrequestbody
- name: V2KeysDeleteKeyResponseBody
  property_count: 2
  slug: unkey-v2keysdeletekeyresponsebody
- name: V2KeysGetKeyRequestBody
  property_count: 2
  slug: unkey-v2keysgetkeyrequestbody
- name: V2KeysGetKeyResponseBody
  property_count: 2
  slug: unkey-v2keysgetkeyresponsebody
- name: V2KeysMigrateKeyData
  property_count: 10
  slug: unkey-v2keysmigratekeydata
- name: V2KeysMigrateKeysMigration
  property_count: 2
  slug: unkey-v2keysmigratekeysmigration
- name: V2KeysMigrateKeysRequestBody
  property_count: 3
  slug: unkey-v2keysmigratekeysrequestbody
- name: V2KeysMigrateKeysResponseBody
  property_count: 2
  slug: unkey-v2keysmigratekeysresponsebody
- name: V2KeysMigrateKeysResponseData
  property_count: 2
  slug: unkey-v2keysmigratekeysresponsedata
- name: V2KeysRemovePermissionsRequestBody
  property_count: 2
  slug: unkey-v2keysremovepermissionsrequestbody
- name: V2KeysRemovePermissionsResponseBody
  property_count: 2
  slug: unkey-v2keysremovepermissionsresponsebody
- name: V2KeysRemovePermissionsResponseData
  property_count: 0
  slug: unkey-v2keysremovepermissionsresponsedata
- name: V2KeysRemoveRolesRequestBody
  property_count: 2
  slug: unkey-v2keysremoverolesrequestbody
- name: V2KeysRemoveRolesResponseBody
  property_count: 2
  slug: unkey-v2keysremoverolesresponsebody
- name: V2KeysRemoveRolesResponseData
  property_count: 0
  slug: unkey-v2keysremoverolesresponsedata
- name: V2KeysRerollKeyRequestBody
  property_count: 2
  slug: unkey-v2keysrerollkeyrequestbody
- name: V2KeysRerollKeyResponseBody
  property_count: 2
  slug: unkey-v2keysrerollkeyresponsebody
- name: V2KeysRerollKeyResponseData
  property_count: 2
  slug: unkey-v2keysrerollkeyresponsedata
- name: V2KeysSetPermissionsRequestBody
  property_count: 2
  slug: unkey-v2keyssetpermissionsrequestbody
- name: V2KeysSetPermissionsResponseBody
  property_count: 2
  slug: unkey-v2keyssetpermissionsresponsebody
- name: V2KeysSetPermissionsResponseData
  property_count: 0
  slug: unkey-v2keyssetpermissionsresponsedata
- name: V2KeysSetRolesRequestBody
  property_count: 2
  slug: unkey-v2keyssetrolesrequestbody
- name: V2KeysSetRolesResponseBody
  property_count: 2
  slug: unkey-v2keyssetrolesresponsebody
- name: V2KeysSetRolesResponseData
  property_count: 0
  slug: unkey-v2keyssetrolesresponsedata
- name: V2KeysUpdateCreditsRequestBody
  property_count: 3
  slug: unkey-v2keysupdatecreditsrequestbody
- name: V2KeysUpdateCreditsResponseBody
  property_count: 2
  slug: unkey-v2keysupdatecreditsresponsebody
- name: V2KeysUpdateKeyRequestBody
  property_count: 10
  slug: unkey-v2keysupdatekeyrequestbody
- name: V2KeysUpdateKeyResponseBody
  property_count: 2
  slug: unkey-v2keysupdatekeyresponsebody
- name: V2KeysVerifyKeyRequestBody
  property_count: 6
  slug: unkey-v2keysverifykeyrequestbody
- name: V2KeysVerifyKeyResponseBody
  property_count: 2
  slug: unkey-v2keysverifykeyresponsebody
- name: V2KeysVerifyKeyResponseData
  property_count: 12
  slug: unkey-v2keysverifykeyresponsedata
- name: V2KeysWhoamiRequestBody
  property_count: 1
  slug: unkey-v2keyswhoamirequestbody
- name: V2KeysWhoamiResponseBody
  property_count: 2
  slug: unkey-v2keyswhoamiresponsebody
- name: V2LivenessResponseBody
  property_count: 2
  slug: unkey-v2livenessresponsebody
- name: V2LivenessResponseData
  property_count: 1
  slug: unkey-v2livenessresponsedata
- name: V2PermissionsCreatePermissionRequestBody
  property_count: 3
  slug: unkey-v2permissionscreatepermissionrequestbody
- name: V2PermissionsCreatePermissionResponseBody
  property_count: 2
  slug: unkey-v2permissionscreatepermissionresponsebody
- name: V2PermissionsCreatePermissionResponseData
  property_count: 1
  slug: unkey-v2permissionscreatepermissionresponsedata
- name: V2PermissionsCreateRoleRequestBody
  property_count: 2
  slug: unkey-v2permissionscreaterolerequestbody
- name: V2PermissionsCreateRoleResponseBody
  property_count: 2
  slug: unkey-v2permissionscreateroleresponsebody
- name: V2PermissionsCreateRoleResponseData
  property_count: 1
  slug: unkey-v2permissionscreateroleresponsedata
- name: V2PermissionsDeletePermissionRequestBody
  property_count: 1
  slug: unkey-v2permissionsdeletepermissionrequestbody
- name: V2PermissionsDeletePermissionResponseBody
  property_count: 2
  slug: unkey-v2permissionsdeletepermissionresponsebody
- name: V2PermissionsDeleteRoleRequestBody
  property_count: 1
  slug: unkey-v2permissionsdeleterolerequestbody
- name: V2PermissionsDeleteRoleResponseBody
  property_count: 2
  slug: unkey-v2permissionsdeleteroleresponsebody
- name: V2PermissionsGetPermissionRequestBody
  property_count: 1
  slug: unkey-v2permissionsgetpermissionrequestbody
- name: V2PermissionsGetPermissionResponseBody
  property_count: 2
  slug: unkey-v2permissionsgetpermissionresponsebody
- name: V2PermissionsGetRoleRequestBody
  property_count: 1
  slug: unkey-v2permissionsgetrolerequestbody
- name: V2PermissionsGetRoleResponseBody
  property_count: 2
  slug: unkey-v2permissionsgetroleresponsebody
- name: V2PermissionsListPermissionsRequestBody
  property_count: 2
  slug: unkey-v2permissionslistpermissionsrequestbody
- name: V2PermissionsListPermissionsResponseBody
  property_count: 3
  slug: unkey-v2permissionslistpermissionsresponsebody
- name: V2PermissionsListPermissionsResponseData
  property_count: 0
  slug: unkey-v2permissionslistpermissionsresponsedata
- name: V2PermissionsListRolesRequestBody
  property_count: 2
  slug: unkey-v2permissionslistrolesrequestbody
- name: V2PermissionsListRolesResponseBody
  property_count: 3
  slug: unkey-v2permissionslistrolesresponsebody
- name: V2PermissionsListRolesResponseData
  property_count: 0
  slug: unkey-v2permissionslistrolesresponsedata
- name: V2RatelimitDeleteOverrideRequestBody
  property_count: 2
  slug: unkey-v2ratelimitdeleteoverriderequestbody
- name: V2RatelimitDeleteOverrideResponseBody
  property_count: 2
  slug: unkey-v2ratelimitdeleteoverrideresponsebody
- name: V2RatelimitDeleteOverrideResponseData
  property_count: 0
  slug: unkey-v2ratelimitdeleteoverrideresponsedata
- name: V2RatelimitGetOverrideRequestBody
  property_count: 2
  slug: unkey-v2ratelimitgetoverriderequestbody
- name: V2RatelimitGetOverrideResponseBody
  property_count: 2
  slug: unkey-v2ratelimitgetoverrideresponsebody
- name: V2RatelimitLimitRequestBody
  property_count: 5
  slug: unkey-v2ratelimitlimitrequestbody
- name: V2RatelimitLimitResponseBody
  property_count: 2
  slug: unkey-v2ratelimitlimitresponsebody
- name: V2RatelimitLimitResponseData
  property_count: 5
  slug: unkey-v2ratelimitlimitresponsedata
- name: V2RatelimitListOverridesRequestBody
  property_count: 3
  slug: unkey-v2ratelimitlistoverridesrequestbody
- name: V2RatelimitListOverridesResponseBody
  property_count: 3
  slug: unkey-v2ratelimitlistoverridesresponsebody
- name: V2RatelimitListOverridesResponseData
  property_count: 0
  slug: unkey-v2ratelimitlistoverridesresponsedata
- name: V2RatelimitMultiLimitCheck
  property_count: 7
  slug: unkey-v2ratelimitmultilimitcheck
- name: V2RatelimitMultiLimitRequestBody
  property_count: 0
  slug: unkey-v2ratelimitmultilimitrequestbody
- name: V2RatelimitMultiLimitResponseBody
  property_count: 2
  slug: unkey-v2ratelimitmultilimitresponsebody
- name: V2RatelimitMultiLimitResponseData
  property_count: 2
  slug: unkey-v2ratelimitmultilimitresponsedata
- name: V2RatelimitSetOverrideRequestBody
  property_count: 4
  slug: unkey-v2ratelimitsetoverriderequestbody
- name: V2RatelimitSetOverrideResponseBody
  property_count: 2
  slug: unkey-v2ratelimitsetoverrideresponsebody
- name: V2RatelimitSetOverrideResponseData
  property_count: 1
  slug: unkey-v2ratelimitsetoverrideresponsedata
- name: ValidationError
  property_count: 3
  slug: unkey-validationerror
- name: VerifyKeyRatelimitData
  property_count: 8
  slug: unkey-verifykeyratelimitdata
json_structures:
- name: Unkey Key Structure
  property_count: 0
  slug: unkey-key-structure
- name: Unkey Structure
  property_count: 0
  slug: unkey-structure
jsonld:
- class_count: 10
  name: Unkey Context
  property_count: 33
  slug: unkey-context
layout: provider
modified: '2026-05-19'
name: Unkey
nav: Providers
network: true
overview: 'Unkey publishes 8 APIs on the [APIs.io](https://apis.io/) network, including analytics API, apis API, deploy API, and 5 more. Tagged areas include API Keys, Rate Limiting, Authentication, Developer Platform, and Access Control.


  The Unkey catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Unkey''s developer surface includes authentication, documentation, GitHub presence, pricing, engineering blog, changelog, and 7 more developer resources.'
plans:
- name: Unkey Plans Pricing
  plan_count: 4
  slug: unkey-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Unkey Rate Limits
  slug: unkey-rate-limits
rules:
- name: Unkey API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: unkey-jsonschema-spectral-rules
- name: Unkey API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 7
  slug: unkey-rules
score:
  band: strong
  composite: 56.8
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 76.4
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 60.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/screenshots/unkey-2026-06-20T200401.png
security:
- kind: authentication
  name: Unkey Authentication
  slug: unkey-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unkey Domain Security
  slug: unkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unkey
tags:
- API Keys
- Rate Limiting
- Authentication
- Developer Platform
- Access Control
- Identity
- Analytics
website: https://www.unkey.com
---
