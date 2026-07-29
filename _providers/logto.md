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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 223
  human_in_the_loop: 6
  name: Logto Agentic Access
  operation_count: 335
  slug: logto-agentic-access
  summary_line: 335 operations · 223 acting · 6 human-in-the-loop
api_count: 39
apis:
- description: Customize your account API settings.
  name: Logto Account center API
  slug: logto-account-center-api
- description: Application represents your registered software program or service that has been authorized to access user information and perform actions on behalf of users within the system. Currently, Logto suppor
  name: Logto Applications API
  slug: logto-applications-api
- description: Audit logs are used to track end-user activities in Logto sign-in experience and other flows. It does not include activities in Logto Console.
  name: Logto Audit logs API
  slug: logto-audit-logs-api
- description: Authentication endpoints for third-party integrations and identity providers.
  name: Logto Authn API
  slug: logto-authn-api
- description: Setup the captcha provider.
  name: Logto Captcha provider API
  slug: logto-captcha-provider-api
- description: Endpoints for managing Logto global configurations for the tenant, such as admin console config and OIDC signing keys. See [🔑 Signing keys](https://docs.logto.io/docs/recipes/signing-keys-rotation/) t
  name: Logto Configs API
  slug: logto-configs-api
- description: Connector factories are used to create connectors. They can be treated as preconfigured templates for connectors.
  name: Logto Connector factories API
  slug: logto-connector-factories-api
- description: Connectors are the bridge between Logto and other third-party vendors who provide short message service (SMS), email service, or user information on wildly accepted social media. To learn more about c
  name: Logto Connectors API
  slug: logto-connectors-api
- description: Endpoints for managing custom phrases that allow you to customize the phrases displayed in the sign-in experience. See [Localized language](https://docs.logto.io/docs/recipes/customize-sie/localized-l
  name: Logto Custom phrases API
  slug: logto-custom-phrases-api
- description: An admin feature used to create a customized user profile form, which is used to collect additional user information upon successful registrations.
  name: Logto Custom profile fields API
  slug: logto-custom-profile-fields-api
- description: Endpoints that power the dashboard page of Console to show the statistics of the current tenant.
  name: Logto Dashboard API
  slug: logto-dashboard-api
- description: Custom domain lets you present a consistent brand by having your own domain name on the sign-in and registration pages. See [🌍 Custom domain](https://docs.logto.io/docs/recipes/custom-domain/) for mor
  name: Logto Domains API
  slug: logto-domains-api
- description: Manage custom i18n email templates for various types of emails, such as sign-in verification codes and password resets.
  name: Logto Email templates API
  slug: logto-email-templates-api
- description: The Experience endpoints allow end-users to interact with Logto for identity verification and profile completion.
  name: Logto Experience API
  slug: logto-experience-api
- description: Hook enables you to effortlessly receive real-time updates regarding specific events, such as user registration, sign-in, or password reset. See [🪝 Webhooks] to get started and learn more.
  name: Logto Hooks API
  slug: logto-hooks-api
- description: Account routes provide functionality for managing user profile for the end user to interact directly with access tokens.
  name: Logto My account API
  slug: logto-my-account-api
- description: One-time tokens are used for various authentication and verification purposes. They are typically sent via email and have an expiration time.
  name: Logto One-time tokens API
  slug: logto-one-time-tokens-api
- description: Organization invitations are used to invite users to join an organization. They are sent via email and contain a link that the user can click to accept the invitation and join the organization.
  name: Logto Organization invitations API
  slug: logto-organization-invitations-api
- description: Organization roles are used to define a set of organization scopes that can be assigned to users. Every organization role is a part of the organization template. Organization roles will only be meanin
  name: Logto Organization roles API
  slug: logto-organization-roles-api
- description: 'Organization scopes (permissions) are used to define actions that can be performed on a organization. Every organization scope is a part of the organization template. Organization scopes will only be '
  name: Logto Organization scopes API
  slug: logto-organization-scopes-api
- description: Organization is a concept that brings together multiple identities (mostly users). Logto supports multiple organizations, and each organization can have multiple users. Every organization shares the s
  name: Logto Organizations API
  slug: logto-organizations-api
- description: Resources (API resources) represent the APIs that you want to protect with Logto. Each resource has a unique indicator (URI) and a set of scopes (permissions). The resources will be used in the author
  name: Logto Resources API
  slug: logto-resources-api
- description: Role management for API resource RBAC (role-based access control). See [🔐 Role-based access control (RBAC)](https://docs.logto.io/docs/recipes/rbac/) to get started with role-based access control.
  name: Logto Roles API
  slug: logto-roles-api
- description: SAML (Security Assertion Markup Language) applications represent applications that use SAML protocol for single sign-on (SSO). These endpoints allow you to manage SAML applications, including their co
  name: Logto SAML applications API
  slug: logto-saml-applications-api
- description: Endpoints for SAML (Security Assertion Markup Language) applications auth flow.
  name: Logto SAML applications auth flow API
  slug: logto-saml-applications-auth-flow-api
- description: Secrets are used to store sensitive information such as API keys, third-party tokens, and other confidential data in Logto's Secret Vault.
  name: Logto Secrets API
  slug: logto-secrets-api
- description: Sentinel activities are used to track and manage user authentication attempts, including successful and failed attempts. Based on your sentinel policy settings, Logto will automatically block users af
  name: Logto Sentinel activities API
  slug: logto-sentinel-activities-api
- description: Endpoints for customizing Logto sign-in experience. See [🎨 Customize sign-in experience](https://docs.logto.io/docs/recipes/customize-sie/) to learn more about how the configuration works and reflects
  name: Logto Sign-in experience API
  slug: logto-sign-in-experience-api
- description: Endpoints for SSO (single sign-on) connector providers. SSO connector providers provide the metadata and configuration templates for creating SSO connectors.
  name: Logto SSO connector providers API
  slug: logto-sso-connector-providers-api
- description: Endpoints for managing single sign-on (SSO) connectors. Your sign-in experience can use these well-configured SSO connectors to authenticate users and sync user attributes from external identity provi
  name: Logto SSO connectors API
  slug: logto-sso-connectors-api
- description: Endpoints for health check.
  name: Logto Status API
  slug: logto-status-api
- description: The subject token API provides the ability to create a new subject token for the use of impersonating the user.
  name: Logto Subject tokens API
  slug: logto-subject-tokens-api
- description: Endpoints for the Swagger JSON document.
  name: Logto Swagger.json API
  slug: logto-swagger-json-api
- description: Endpoints for system constants and information.
  name: Logto Systems API
  slug: logto-systems-api
- description: Endpoints for managing user uploaded assets.
  name: Logto User assets API
  slug: logto-user-assets-api
- description: Endpoints for user management. Including creating, updating, deleting, and querying users with flexible filters. In addition to the endpoints, see [🧑‍🚀 Manage users](https://docs.logto.io/docs/recipes
  name: Logto Users API
  slug: logto-users-api
- description: Endpoints for handling verification codes. It is helpful when building a custom profile page in your app. See [👤 User profile](https://docs.logto.io/docs/recipes/user-profile/#optional-validate-verifi
  name: Logto Verification codes API
  slug: logto-verification-codes-api
- description: Endpoints for creating and validating verification records, which can be used in Profile routes.
  name: Logto Verifications API
  slug: logto-verifications-api
- description: Well-Known routes provide information and resources that can be discovered by clients without the need for authentication.
  name: Logto Well-known API
  slug: logto-well-known-api
artifact_total: 46
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/logto-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/logto-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/logto-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/logto
- group: company
  title: ''
  type: Website
  url: https://logto.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logto.io
- group: docs
  title: ''
  type: OpenAPI
  url: https://openapi.logto.io/source.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/logto-io
- group: agent
  title: ''
  type: LlmsText
  url: https://openapi.logto.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.logto.io/rss.xml
created: '2026-03-25'
description: Logto is an open source identity infrastructure platform with authentication, authorization, user management, and multi-tenancy supporting OIDC, OAuth, and SAML.
finops:
- name: Logto Finops
  service_category: API
  slug: logto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logto.png
layout: provider
modified: '2026-05-19'
name: Logto
nav: Providers
network: true
overview: 'Logto publishes 39 APIs on the [APIs.io](https://apis.io/) network, including Account center API, Applications API, Audit logs API, and 36 more. Tagged areas include Authentication, Authorization, Identity, OIDC, and OAuth.


  Logto''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Logto Plans Pricing
  plan_count: 3
  slug: logto-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 5
  name: Logto Rate Limits
  slug: logto-rate-limits
scopes:
- name: Logto Scopes
  scope_count: 1
  slug: logto-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 36.1
  delta: -1.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.0
    developer_ergonomics: 21.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 39
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/logto/refs/heads/main/screenshots/logto-2026-06-20T184700.png
security:
- kind: authentication
  name: Logto Authentication
  slug: logto-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Logto Domain Security
  slug: logto-domain-security
  summary_line: TLSv1.3 · DMARC
slug: logto
tags:
- Authentication
- Authorization
- Identity
- OIDC
- OAuth
- SAML
- Open Source
website: https://logto.io
---
