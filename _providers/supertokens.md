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
  band: agent-aware
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
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 20
  human_in_the_loop: 2
  name: Supertokens Agentic Access
  operation_count: 31
  slug: supertokens-agentic-access
  summary_line: 31 operations · 20 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Email and password sign-up, sign-in, and password management
  name: SuperTokens Email Password API
  slug: supertokens-email-password-api
- description: Email verification token creation and validation
  name: SuperTokens Email Verification API
  slug: supertokens-email-verification-api
- description: Service health and version checks
  name: SuperTokens Health API
  slug: supertokens-health-api
- description: Tenant and app management
  name: SuperTokens Multi Tenancy API
  slug: supertokens-multi-tenancy-api
- description: Passwordless OTP and magic link authentication
  name: SuperTokens Passwordless API
  slug: supertokens-passwordless-api
- description: Session creation, verification, refresh, and revocation
  name: SuperTokens Sessions API
  slug: supertokens-sessions-api
- description: Social/OAuth third-party provider authentication
  name: SuperTokens Third Party API
  slug: supertokens-third-party-api
- description: User metadata storage and retrieval
  name: SuperTokens User Metadata API
  slug: supertokens-user-metadata-api
- description: User role assignment and management
  name: SuperTokens User Roles API
  slug: supertokens-user-roles-api
- description: User management and listing
  name: SuperTokens Users API
  slug: supertokens-users-api
artifact_total: 75
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SuperTokens Core Driver Interface
  slug: open-supertokens-core-driver-interface
- collection_type: open
  name: SuperTokens Core Driver Interface Email Password API
  slug: open-supertokens-email-password-api
- collection_type: open
  name: SuperTokens Core Driver Interface Email Password Email Verification API
  slug: open-supertokens-email-verification-api
- collection_type: open
  name: SuperTokens Core Driver Interface Email Password Health API
  slug: open-supertokens-health-api
- collection_type: open
  name: SuperTokens Core Driver Interface Email Password Multi Tenancy API
  slug: open-supertokens-multi-tenancy-api
- collection_type: open
  name: SuperTokens Core Driver Interface Email Password Passwordless API
  slug: open-supertokens-passwordless-api
- collection_type: open
  name: SuperTokens Core Driver Interface Email Password Sessions API
  slug: open-supertokens-sessions-api
- collection_type: open
  name: SuperTokens Core Driver Interface Email Password Third Party API
  slug: open-supertokens-third-party-api
- collection_type: open
  name: SuperTokens Core Driver Interface Email Password User Metadata API
  slug: open-supertokens-user-metadata-api
- collection_type: open
  name: SuperTokens Core Driver Interface Email Password User Roles API
  slug: open-supertokens-user-roles-api
- collection_type: open
  name: SuperTokens Core Driver Interface Email Password Users API
  slug: open-supertokens-users-api
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/supertokens/supertokens-core/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/supertokens/supertokens-core/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/supertokens/supertokens-core/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/supertokens/supertokens-core/blob/master/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/supertokens-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/supertokens-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://supertokens.com/blog
created: '2026-03-25'
description: SuperTokens is an open source authentication solution providing session management, social login, email/password auth, and passwordless flows for web and mobile apps. It is an open source alternative to Auth0, Firebase Auth, and AWS Cognito. SuperTokens exposes a Core Driver Interface (CDI) HTTP API for backend SDKs to communicate with the supertokens-core service, as well as a Frontend Driver Interface (FDI) for frontend SDK interaction. Available SDKs cover Node.js, Python, Go, Java, React, Flutter, iOS, and Android.
examples:
- key_count: 3
  name: Supertokens Create Session Example
  slug: supertokens-create-session-example
- key_count: 3
  name: Supertokens Signup Example
  slug: supertokens-signup-example
finops:
- name: Supertokens Finops
  service_category: Identity
  slug: supertokens-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/supertokens.png
json_schemas:
- name: ApiVersionResponse
  property_count: 2
  slug: supertokens-apiversionresponse
- name: AssignRoleRequest
  property_count: 3
  slug: supertokens-assignrolerequest
- name: ConsumePasswordlessCodeRequest
  property_count: 4
  slug: supertokens-consumepasswordlesscoderequest
- name: ConsumePasswordlessCodeResponse
  property_count: 3
  slug: supertokens-consumepasswordlesscoderesponse
- name: CreatePasswordlessCodeRequest
  property_count: 3
  slug: supertokens-createpasswordlesscoderequest
- name: CreatePasswordlessCodeResponse
  property_count: 8
  slug: supertokens-createpasswordlesscoderesponse
- name: CreateRoleRequest
  property_count: 2
  slug: supertokens-createrolerequest
- name: CreateSessionRequest
  property_count: 4
  slug: supertokens-createsessionrequest
- name: CreateSessionResponse
  property_count: 5
  slug: supertokens-createsessionresponse
- name: EmailVerificationTokenRequest
  property_count: 3
  slug: supertokens-emailverificationtokenrequest
- name: EmailVerificationTokenResponse
  property_count: 2
  slug: supertokens-emailverificationtokenresponse
- name: ErrorResponse
  property_count: 2
  slug: supertokens-errorresponse
- name: GetSessionResponse
  property_count: 3
  slug: supertokens-getsessionresponse
- name: IsEmailVerifiedResponse
  property_count: 2
  slug: supertokens-isemailverifiedresponse
- name: ListRolesResponse
  property_count: 2
  slug: supertokens-listrolesresponse
- name: ListTenantsResponse
  property_count: 2
  slug: supertokens-listtenantsresponse
- name: ListUsersResponse
  property_count: 3
  slug: supertokens-listusersresponse
- name: RefreshSessionRequest
  property_count: 3
  slug: supertokens-refreshsessionrequest
- name: RemoveSessionsRequest
  property_count: 2
  slug: supertokens-removesessionsrequest
- name: RemoveSessionsResponse
  property_count: 2
  slug: supertokens-removesessionsresponse
- name: ResetPasswordRequest
  property_count: 3
  slug: supertokens-resetpasswordrequest
- name: ResetPasswordTokenRequest
  property_count: 2
  slug: supertokens-resetpasswordtokenrequest
- name: ResetPasswordTokenResponse
  property_count: 2
  slug: supertokens-resetpasswordtokenresponse
- name: SuperTokens Session
  property_count: 8
  slug: supertokens-session
- name: SessionDataResponse
  property_count: 2
  slug: supertokens-sessiondataresponse
- name: SignInRequest
  property_count: 3
  slug: supertokens-signinrequest
- name: SignInResponse
  property_count: 2
  slug: supertokens-signinresponse
- name: SignUpRequest
  property_count: 3
  slug: supertokens-signuprequest
- name: SignUpResponse
  property_count: 2
  slug: supertokens-signupresponse
- name: StatusResponse
  property_count: 1
  slug: supertokens-statusresponse
- name: TenantRequest
  property_count: 5
  slug: supertokens-tenantrequest
- name: TenantResponse
  property_count: 3
  slug: supertokens-tenantresponse
- name: ThirdPartySignInUpRequest
  property_count: 4
  slug: supertokens-thirdpartysigninuprequest
- name: ThirdPartySignInUpResponse
  property_count: 3
  slug: supertokens-thirdpartysigninupresponse
- name: Token
  property_count: 3
  slug: supertokens-token
- name: UpdateSessionDataRequest
  property_count: 2
  slug: supertokens-updatesessiondatarequest
- name: UpdateUserMetadataRequest
  property_count: 2
  slug: supertokens-updateusermetadatarequest
- name: User
  property_count: 7
  slug: supertokens-user
- name: UserMetadataResponse
  property_count: 2
  slug: supertokens-usermetadataresponse
- name: UserRolesResponse
  property_count: 2
  slug: supertokens-userrolesresponse
- name: VerifyEmailRequest
  property_count: 3
  slug: supertokens-verifyemailrequest
json_structures:
- name: Supertokens Session Structure
  property_count: 0
  slug: supertokens-session-structure
- name: Supertokens Structure
  property_count: 0
  slug: supertokens-structure
jsonld:
- class_count: 7
  name: Supertokens Context
  property_count: 11
  slug: supertokens-context
layout: provider
modified: '2026-05-30'
name: SuperTokens
nav: Providers
network: true
overview: 'SuperTokens publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Email Password API, Email Verification API, Health API, and 7 more. Tagged areas include Authentication, Open-Source, Session Management, Social Login, and Passwordless.


  The SuperTokens catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SuperTokens'' developer surface includes authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Supertokens Plans Pricing
  plan_count: 3
  slug: supertokens-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Supertokens Rate Limits
  slug: supertokens-rate-limits
rules:
- effective_rule_count: 10
  extends: []
  name: SuperTokens API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: supertokens-cdi-rules
- effective_rule_count: 5
  extends: []
  name: SuperTokens API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: supertokens-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 35.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 54.5
    contract_quality: 62.4
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 54.5
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 100.0
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/supertokens/refs/heads/main/screenshots/supertokens-2026-06-20T194732.png
security:
- kind: authentication
  name: Supertokens Authentication
  slug: supertokens-authentication
  summary_line: apiKey · 1 scheme
slug: supertokens
tags:
- Authentication
- Open-Source
- Session Management
- Social Login
- Passwordless
- Identity
- Authorization
- Multi-Tenancy
- Node.js
- Self-Hosted
---
