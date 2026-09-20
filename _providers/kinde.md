---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: templated
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.5
  scored_at: '2026-09-19'
agentic_access:
- acting_count: 111
  human_in_the_loop: 13
  name: Kinde Agentic Access
  operation_count: 179
  slug: kinde-agentic-access
  summary_line: 179 operations · 111 acting · 13 human-in-the-loop
api_count: 2
apis:
- description: The Kinde Management MCP server bridges AI agents and a Kinde account. It is TENANT-SCOPED — the endpoint is https://{subdomain}.kinde.com/mcp, one per Kinde business — and is authenticated with an En
  name: Kinde MCP Server
  slug: kinde-mcp-server
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The API Keys API from Kinde — 3 operation(s) for api keys.
  name: Kinde API Keys API
  slug: kinde-api-keys-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Applications API from Kinde — 7 operation(s) for applications.
  name: Kinde Applications API
  slug: kinde-applications-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Billing Agreements API from Kinde — 1 operation(s) for billing agreements.
  name: Kinde Billing Agreements API
  slug: kinde-billing-agreements-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Billing API from Kinde — 2 operation(s) for billing.
  name: Kinde Billing API
  slug: kinde-billing-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Billing Entitlements API from Kinde — 1 operation(s) for billing entitlements.
  name: Kinde Billing Entitlements API
  slug: kinde-billing-entitlements-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Billing Meter Usage API from Kinde — 1 operation(s) for billing meter usage.
  name: Kinde Billing Meter Usage API
  slug: kinde-billing-meter-usage-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Business API from Kinde — 1 operation(s) for business.
  name: Kinde Business API
  slug: kinde-business-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Callbacks API from Kinde — 2 operation(s) for callbacks.
  name: Kinde Callbacks API
  slug: kinde-callbacks-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Connected Apps API from Kinde — 3 operation(s) for connected apps.
  name: Kinde Connected Apps API
  slug: kinde-connected-apps-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Connections API from Kinde — 2 operation(s) for connections.
  name: Kinde Connections API
  slug: kinde-connections-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Directories API from Kinde — 2 operation(s) for directories.
  name: Kinde Directories API
  slug: kinde-directories-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Environment variables API from Kinde — 2 operation(s) for environment variables.
  name: Kinde Environment variables API
  slug: kinde-environment-variables-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Environments API from Kinde — 5 operation(s) for environments.
  name: Kinde Environments API
  slug: kinde-environments-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Feature flags API from Kinde — 3 operation(s) for feature flags.
  name: Kinde Feature flags API
  slug: kinde-feature-flags-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Identities API from Kinde — 1 operation(s) for identities.
  name: Kinde Identities API
  slug: kinde-identities-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Industries API from Kinde — 1 operation(s) for industries.
  name: Kinde Industries API
  slug: kinde-industries-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The MFA API from Kinde — 1 operation(s) for mfa.
  name: Kinde MFA API
  slug: kinde-mfa-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Organizations API from Kinde — 25 operation(s) for organizations.
  name: Kinde Organizations API
  slug: kinde-organizations-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Permissions API from Kinde — 3 operation(s) for permissions.
  name: Kinde Permissions API
  slug: kinde-permissions-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Properties API from Kinde — 3 operation(s) for properties.
  name: Kinde Properties API
  slug: kinde-properties-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Property Categories API from Kinde — 2 operation(s) for property categories.
  name: Kinde Property Categories API
  slug: kinde-property-categories-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Roles API from Kinde — 7 operation(s) for roles.
  name: Kinde Roles API
  slug: kinde-roles-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Search API from Kinde — 1 operation(s) for search.
  name: Kinde Search API
  slug: kinde-search-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Self-serve portal API from Kinde — 1 operation(s) for self-serve portal.
  name: Kinde Self-serve portal API
  slug: kinde-self-serve-portal-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Subscribers API from Kinde — 2 operation(s) for subscribers.
  name: Kinde Subscribers API
  slug: kinde-subscribers-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Timezones API from Kinde — 1 operation(s) for timezones.
  name: Kinde Timezones API
  slug: kinde-timezones-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Users API from Kinde — 11 operation(s) for users.
  name: Kinde Users API
  slug: kinde-users-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Webhooks API from Kinde — 4 operation(s) for webhooks.
  name: Kinde Webhooks API
  slug: kinde-webhooks-api
- baseURL: https://{subdomain}.kinde.com/mcp
  baseurl_source: declared
  description: The APIs API from Kinde — 6 operation(s) for apis.
  name: Kinde AP Is API
  slug: kinde-apis-api
- baseURL: https://{subdomain}.kinde.com/mcp
  baseurl_source: declared
  description: The OAuth API from Kinde — 3 operation(s) for oauth.
  name: Kinde O Auth API
  slug: kinde-oauth-api
arazzos:
- description: Find an existing user by email and grant them a role within an organization.
  name: Kinde Assign Organization User Role
  slug: kinde-assign-org-user-role-workflow
- description: Stand up a new organization and seed it with existing users and roles.
  name: Kinde Create Organization with Users
  slug: kinde-create-organization-with-users-workflow
- description: Create a permission, create a role, and attach the permission to the role.
  name: Kinde Create Role with Permission
  slug: kinde-create-role-with-permission-workflow
- description: Read the signed-in user's profile, roles, and entitlements, then mint a self-serve portal link.
  name: Kinde End User Self-Serve Portal
  slug: kinde-end-user-self-serve-portal-workflow
- description: Validate roles, create an organization invitation, and poll until it is sent.
  name: Kinde Invite User to Organization
  slug: kinde-invite-user-to-organization-workflow
- description: Create a user with an email identity and import their existing hashed password.
  name: Kinde Migrate User with Password
  slug: kinde-migrate-user-with-password-workflow
- description: Create a user, add them to an organization, and grant a role in one pass.
  name: Kinde Provision User into Organization
  slug: kinde-provision-user-workflow
- description: Create an application, set its callback URLs, create a social connection, and enable it.
  name: Kinde Register Application with Connection
  slug: kinde-register-application-with-connection-workflow
- description: Create an org-overridable feature flag and set its value for one organization.
  name: Kinde Roll Out Feature Flag to Organization
  slug: kinde-rollout-feature-flag-workflow
artifact_total: 103
collections:
- collection_type: postman
  name: Kinde Account API
  slug: postman-kinde-frontend-api
- collection_type: postman
  name: Kinde Management API
  slug: postman-kinde-management-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kinde Account API Keys API
  slug: open-kinde-api-keys-api
- collection_type: open
  name: Kinde Account API Keys APIs API
  slug: open-kinde-apis-api
- collection_type: open
  name: Kinde Account API Keys Applications API
  slug: open-kinde-applications-api
- collection_type: open
  name: Kinde Account API Keys Billing Agreements API
  slug: open-kinde-billing-agreements-api
- collection_type: open
  name: Kinde Account API Keys Billing API
  slug: open-kinde-billing-api
- collection_type: open
  name: Kinde Account API Keys Billing Entitlements API
  slug: open-kinde-billing-entitlements-api
- collection_type: open
  name: Kinde Account API Keys Billing Meter Usage API
  slug: open-kinde-billing-meter-usage-api
- collection_type: open
  name: Kinde Account API Keys Business API
  slug: open-kinde-business-api
- collection_type: open
  name: Kinde Account API Keys Callbacks API
  slug: open-kinde-callbacks-api
- collection_type: open
  name: Kinde Account API Keys Connected Apps API
  slug: open-kinde-connected-apps-api
- collection_type: open
  name: Kinde Account API Keys Connections API
  slug: open-kinde-connections-api
- collection_type: open
  name: Kinde Account API Keys Directories API
  slug: open-kinde-directories-api
- collection_type: open
  name: Kinde Account API Keys Environment variables API
  slug: open-kinde-environment-variables-api
- collection_type: open
  name: Kinde Account API Keys Environments API
  slug: open-kinde-environments-api
- collection_type: open
  name: Kinde Account API Keys Feature flags API
  slug: open-kinde-feature-flags-api
- collection_type: open
  name: Kinde Account API
  slug: open-kinde-frontend-api
- collection_type: open
  name: Kinde Account API Keys Identities API
  slug: open-kinde-identities-api
- collection_type: open
  name: Kinde Account API Keys Industries API
  slug: open-kinde-industries-api
- collection_type: open
  name: Kinde Management API
  slug: open-kinde-management-api
- collection_type: open
  name: Kinde Account API Keys MFA API
  slug: open-kinde-mfa-api
- collection_type: open
  name: Kinde Account API Keys OAuth API
  slug: open-kinde-oauth-api
- collection_type: open
  name: Kinde Account API Keys Organizations API
  slug: open-kinde-organizations-api
- collection_type: open
  name: Kinde Account API Keys Permissions API
  slug: open-kinde-permissions-api
- collection_type: open
  name: Kinde Account API Keys Properties API
  slug: open-kinde-properties-api
- collection_type: open
  name: Kinde Account API Keys Property Categories API
  slug: open-kinde-property-categories-api
- collection_type: open
  name: Kinde Account API Keys Roles API
  slug: open-kinde-roles-api
- collection_type: open
  name: Kinde Account API Keys Search API
  slug: open-kinde-search-api
- collection_type: open
  name: Kinde Account API Keys Self-serve portal API
  slug: open-kinde-self-serve-portal-api
- collection_type: open
  name: Kinde Account API Keys Subscribers API
  slug: open-kinde-subscribers-api
- collection_type: open
  name: Kinde Account API Keys Timezones API
  slug: open-kinde-timezones-api
- collection_type: open
  name: Kinde Account API Keys Users API
  slug: open-kinde-users-api
- collection_type: open
  name: Kinde Account API Keys Webhooks API
  slug: open-kinde-webhooks-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.kinde.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/agentic-access/kinde-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kinde-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/security/kinde-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kinde-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/security/kinde-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kinde-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/security/kinde-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kinde-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/authentication/kinde-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kinde-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/kinde/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-assign-org-user-role-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-assign-org-user-role-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-create-organization-with-users-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-create-organization-with-users-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-create-role-with-permission-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-create-role-with-permission-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-end-user-self-serve-portal-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-end-user-self-serve-portal-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-invite-user-to-organization-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-invite-user-to-organization-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-migrate-user-with-password-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-migrate-user-with-password-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-provision-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-provision-user-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-register-application-with-connection-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-register-application-with-connection-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-rollout-feature-flag-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-rollout-feature-flag-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.kinde.com
- group: start
  title: ''
  type: Login
  url: https://app.kinde.com/admin
- group: start
  title: ''
  type: Signup
  url: https://app.kinde.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://kinde.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://kinde.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kinde.com
- group: operate
  title: ''
  type: StatusPageRSS
  url: https://status.kinde.com/history.rss
- group: operate
  title: ''
  type: StatusPageAtom
  url: https://status.kinde.com/history.atom
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.kinde.com
- group: operate
  title: ''
  type: RoadMap
  url: https://updates.kinde.com/board
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kinde-oss
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.kinde.com/trust-center/agreements/terms-of-service/
- group: auth
  title: ''
  type: TrustCenter
  url: https://docs.kinde.com/trust-center/
- group: operate
  title: ''
  type: Support
  url: mailto:support@kinde.com
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/plans/kinde-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kinde-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/rate-limits/kinde-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kinde-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/finops/kinde-finops.yml
  title: ''
  type: FinOps
  url: finops/kinde-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/vocabulary/kinde-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kinde-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/json-ld/kinde-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kinde-context.jsonld
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-typescript-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-auth-nextjs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-auth-react
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-auth-pkce-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-nodejs-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-node-express
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-node-express-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-remix-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-auth-remix-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-sveltekit-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/nuxt-kinde
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-tsr
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-java-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-dotnet-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-php-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-ruby-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-elixir-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-auth-wordpress
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-flutter-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-sdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/expo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-react-native-sdk-0-7x
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/management-api-js
- group: build
  title: ''
  type: CLI
  url: https://github.com/kinde-oss/kinde-cli
- group: build
  title: ''
  type: CLI
  url: https://github.com/kinde-oss/homebrew-kinde-cli
- group: build
  title: ''
  type: CLI
  url: https://github.com/kinde-oss/scoop-kinde-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/jwt-validator
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/jwt-decoder
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/js-utils
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/webhook
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/kinde-translations
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/infrastructure
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/workflows-runtime
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/terraform-provider-kinde
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/kinde-convex-sync
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/kinde-convex-billing
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/kinde-oss/documentation
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.kinde.com/llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/packages/kinde-packages.yml
  title: ''
  type: Packages
  url: packages/kinde-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/packages/kinde-packages.yml
  title: ''
  type: SDKs
  url: packages/kinde-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/well-known/kinde-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kinde-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/well-known/kinde-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kinde-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/security/kinde-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/kinde-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/conformance/kinde-conformance.yml
  title: ''
  type: Compliance
  url: conformance/kinde-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/conformance/kinde-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kinde-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/conventions/kinde-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kinde-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/conventions/kinde-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/kinde-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/errors/kinde-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kinde-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/lifecycle/kinde-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kinde-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/lifecycle/kinde-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/kinde-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/scopes/kinde-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/kinde-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/data-model/kinde-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kinde-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/sandbox/kinde-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kinde-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/changelog/kinde-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kinde-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/cli/kinde-cli.yml
  title: ''
  type: CLI
  url: cli/kinde-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/components/kinde-components.yml
  title: ''
  type: Components
  url: components/kinde-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/webhooks/kinde-webhooks.yml
  title: ''
  type: Webhooks
  url: webhooks/kinde-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/llms/kinde-www-llms.txt
  title: ''
  type: LlmsText
  url: llms/kinde-www-llms.txt
- group: operate
  title: ''
  type: HelpCenter
  url: https://kinde.com/support/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kinde.com/kinde-apis/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.kinde.com/trust-center/privacy-and-compliance/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.kinde.com/trust-center/privacy-and-compliance/compliance/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/overlays/kinde-management-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kinde-management-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/overlays/kinde-account-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kinde-account-api-overlay.yaml
created: '2026-05-22'
description: Kinde is a developer-first authentication and customer identity platform that bundles authentication (passwords, passwordless, social, enterprise SSO), authorization (roles, permissions, scopes), B2B organizations, billing, and feature flags into a single integrated product. Founded in Australia, Kinde positions itself as "the fully integrated developer platform — secure and monetize your product from day one" and is used by over 70,000 developers. The platform exposes a Management API for tenant administration and an Account API for end-user self-service flows, both backed by published OpenAPI specs and a large open-source SDK ecosystem on GitHub (TypeScript, React, Next.js, Python, Go, Java, .NET, PHP, Ruby, Elixir, Flutter, iOS, Android, Expo, React Native, SvelteKit, Nuxt, Remix, TanStack Start) plus a Go-based CLI, a Terraform provider, and a Model Context Protocol (MCP) server for AI agents.
examples:
- key_count: 2
  name: Kinde Create Application Example
  slug: kinde-create-application-example
- key_count: 2
  name: Kinde Create Feature Flag Example
  slug: kinde-create-feature-flag-example
- key_count: 2
  name: Kinde Create Organization Example
  slug: kinde-create-organization-example
- key_count: 2
  name: Kinde Create Role Example
  slug: kinde-create-role-example
- key_count: 2
  name: Kinde Create User Example
  slug: kinde-create-user-example
- key_count: 2
  name: Kinde Create Webhook Example
  slug: kinde-create-webhook-example
finops:
- name: Kinde Finops
  service_category: Identity
  slug: kinde-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kinde.png
json_schemas:
- name: Application
  property_count: 10
  slug: kinde-application
- name: FeatureFlag
  property_count: 6
  slug: kinde-feature-flag
- name: Organization
  property_count: 11
  slug: kinde-organization
- name: Permission
  property_count: 4
  slug: kinde-permission
- name: Role
  property_count: 5
  slug: kinde-role
- name: User
  property_count: 15
  slug: kinde-user
- name: Webhook
  property_count: 8
  slug: kinde-webhook
json_structures:
- name: Kinde Organization Structure
  property_count: 0
  slug: kinde-organization-structure
- name: Kinde User Structure
  property_count: 0
  slug: kinde-user-structure
jsonld:
- class_count: 36
  name: Kinde Context
  property_count: 9
  slug: kinde-context
layout: provider
mcp_servers:
- description: 'Kinde ships TWO distinct MCP surfaces and they must not be conflated. (1) The Kinde Management MCP Server: a Kinde-authored remote MCP server exposing a read-and-create subset of the Kinde Management '
  name: Kinde MCP Server
  slug: kinde-mcp-server
modified: '2026-09-12'
name: Kinde
nav: Providers
network: true
overview: 'Kinde publishes 30 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Applications API, Billing Agreements API, and 27 more. Tagged areas include Authentication, Authorization, Customer Identity, Identity Management, and OpenID Connect.


  The Kinde catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Kinde''s developer surface includes authentication, developer portal, signup flow, pricing, engineering blog, changelog, GitHub presence, and 96 more developer resources.'
plans:
- name: Kinde Plans Pricing
  plan_count: 5
  slug: kinde-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Kinde Rate Limits
  slug: kinde-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Kinde API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: kinde-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Kinde API Rules
  rule_count: 12
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 8
  slug: kinde-rules
scopes:
- name: Kinde Scopes
  scope_count: 0
  slug: kinde-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 86.1
  coverage:
    artifact_dirs: 37
    catalog_earned: 88.5
    catalog_earned_first_party: 12.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 47.0
    contract_quality: 74.5
    developer_ergonomics: 91.1
    discoverability: 70.4
    operational_transparency: 92.1
  previous_composite: 86.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 90.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: true
    score: 66.7
screenshot: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/screenshots/kinde-2026-06-20T184038.png
security:
- kind: authentication
  name: Kinde Authentication
  slug: kinde-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kinde Domain Security
  slug: kinde-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kinde Vulnerability Disclosure
  slug: kinde-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Kinde Trust Center
  slug: kinde-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: kinde
tags:
- Authentication
- Authorization
- Customer Identity
- Identity Management
- OpenID Connect
- SSO
- Multi-Factor Authentication
- Role-Based Access Control
- Feature Flags
- Billing
- B2B
- Software-as-a-Service
- Developer Platform
website: https://www.kinde.com/
---
