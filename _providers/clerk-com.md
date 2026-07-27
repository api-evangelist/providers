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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 273
  human_in_the_loop: 16
  name: Clerk Com Agentic Access
  operation_count: 426
  slug: clerk-com-agentic-access
  summary_line: 426 operations · 273 acting · 16 human-in-the-loop
api_count: 76
apis:
- description: The Account Portal API from Clerk — 1 operation(s) for account portal.
  name: Clerk Account Portal API
  slug: clerk-com-account-portal-api
- description: Used to interact with the sessions of the current user.
  name: Clerk Active Sessions API
  slug: clerk-com-active-sessions-api
- description: Allow your users to sign in on behalf of other users.
  name: Clerk Actor Tokens API
  slug: clerk-com-actor-tokens-api
- description: Tasks that allow creating user sessions for agent-based interactions.
  name: Clerk Agent Tasks API
  slug: clerk-com-agent-tasks-api
- description: Allow-lists and Block-lists allow you to control who can sign up or sign in to your application, by restricting access based on the user's email address or phone number.
  name: Clerk Allow-list / Block-list API
  slug: clerk-com-allow-list-block-list-api
- description: Endpoints for managing API Keys
  name: Clerk API Keys API
  slug: clerk-com-api-keys-api
- description: 'An object representing a transfer request for an application between workspaces. The high-level flow for application transfer: 1. The initial workspace can create an application transfer. A single-use'
  name: Clerk Application Transfers API
  slug: clerk-com-application-transfers-api
- description: An object representing a Clerk application. Each `application` can have multiple `instances`, typically one for development and one for production, each with distinct user pools.
  name: Clerk Applications API
  slug: clerk-com-applications-api
- description: Used to interact with the two factor authentication backup codes of the current user.
  name: Clerk Backup Codes API
  slug: clerk-com-backup-codes-api
- description: Modify instance settings that are currently in beta.
  name: Clerk Beta Features API
  slug: clerk-com-beta-features-api
- description: Billing-related endpoints for managing statements and payment attempts.
  name: Clerk Billing API
  slug: clerk-com-billing-api
- description: Used to interact with the checkout flow.
  name: Clerk Checkouts API
  slug: clerk-com-checkouts-api
- description: The Clear Site Data API from Clerk — 1 operation(s) for clear site data.
  name: Clerk Clear Site Data API
  slug: clerk-com-clear-site-data-api
- description: Used to interact with the Client Object.
  name: Clerk Client API
  slug: clerk-com-client-api
- description: The Client object tracks sessions, as well as the state of any sign in and sign up attempts, for a given device.
  name: Clerk Clients API
  slug: clerk-com-clients-api
- description: Operations for managing instance configuration. The config API provides a unified interface for reading and updating instance settings, including authentication methods, SSO connections, and other ins
  name: Clerk Config API
  slug: clerk-com-config-api
- description: The Dev Browser API from Clerk — 2 operation(s) for dev browser.
  name: Clerk Dev Browser API
  slug: clerk-com-dev-browser-api
- description: Used to handle dev browsers.
  name: Clerk DevBrowser API
  slug: clerk-com-devbrowser-api
- description: Domains represent each instance's URLs and DNS setup.
  name: Clerk Domains API
  slug: clerk-com-domains-api
- description: A user can be associated with one or more email addresses, which allows them to be contacted via email.
  name: Clerk Email Addresses API
  slug: clerk-com-email-addresses-api
- description: Email & SMS templates allow you to customize the theming and wording of emails & SMS messages that are sent by your instance.
  name: Clerk Email & SMS Templates API
  slug: clerk-com-email-sms-templates-api
- description: An Enterprise Connection holds configuration data required for facilitating an enterprise SSO flow between your Clerk instance and an identity provider.
  name: Clerk Enterprise Connections API
  slug: clerk-com-enterprise-connections-api
- description: Used to get and update the current Environment
  name: Clerk Environment API
  slug: clerk-com-environment-api
- description: Used to interact with the external accounts of the current user.
  name: Clerk External Accounts API
  slug: clerk-com-external-accounts-api
- description: Used to get the health status of the API.
  name: Clerk Health API
  slug: clerk-com-health-api
- description: Modify the settings of your instance.
  name: Clerk Instance Settings API
  slug: clerk-com-instance-settings-api
- description: Invitations allow you to invite someone to sign up to your application, via email.
  name: Clerk Invitations API
  slug: clerk-com-invitations-api
- description: Retrieve the JSON Web Key Set which can be used to verify the token signatures of the instance.
  name: Clerk JWKS API
  slug: clerk-com-jwks-api
- description: JWT Templates allow you to generate custom authentication tokens tied to authenticated sessions, enabling you to integrate with third-party services.
  name: Clerk JWT Templates API
  slug: clerk-com-jwt-templates-api
- description: Machine to Machine Tokens are used to manage authentication between Machines.
  name: Clerk M2M Tokens API
  slug: clerk-com-m2m-tokens-api
- description: A Machine represents a machine/server/service which can be used in machine-to-machine authentication.
  name: Clerk Machines API
  slug: clerk-com-machines-api
- description: Used to interact with the members of an organization. The current user must be an administrator to access them.
  name: Clerk Members API
  slug: clerk-com-members-api
- description: Used to interact with the members of an organization. The current user must be an administrator to access them.
  name: Clerk Membership Requests API
  slug: clerk-com-membership-requests-api
- description: Various endpoints that do not belong in any particular category.
  name: Clerk Miscellaneous API
  slug: clerk-com-miscellaneous-api
- description: Endpoints for managing OAuth Access Tokens, which are credentials to access protected resources on behalf of a user.
  name: Clerk OAuth Access Tokens API
  slug: clerk-com-oauth-access-tokens-api
- description: OAuth applications contain data for clients using Clerk as an OAuth2 identity provider.
  name: Clerk OAuth Applications API
  slug: clerk-com-oauth-applications-api
- description: Used to receive callbacks from successful OAuth attempts.
  name: Clerk OAuth2 Callbacks API
  slug: clerk-com-oauth2-callbacks-api
- description: Requests for the OAuth2 authorization flow.
  name: Clerk OAuth2 Identity Provider API
  slug: clerk-com-oauth2-identity-provider-api
- description: Used to interact with an organization and its properties. The current user must be an administrator to access them.
  name: Clerk Organization API
  slug: clerk-com-organization-api
- description: Used to get suggested defaults when creating a new organization.
  name: Clerk Organization Creation Defaults API
  slug: clerk-com-organization-creation-defaults-api
- description: Manage organization domains.
  name: Clerk Organization Domains API
  slug: clerk-com-organization-domains-api
- description: Invite users to an organization.
  name: Clerk Organization Invitations API
  slug: clerk-com-organization-invitations-api
- description: Manage member roles in an organization.
  name: Clerk Organization Memberships API
  slug: clerk-com-organization-memberships-api
- description: Manage organization permissions that define what members can do within an organization.
  name: Clerk Organization Permissions API
  slug: clerk-com-organization-permissions-api
- description: Manage custom roles in an organization.
  name: Clerk Organization Roles API
  slug: clerk-com-organization-roles-api
- description: Organizations are used to group members under a common entity and provide shared access to resources.
  name: Clerk Organizations API
  slug: clerk-com-organizations-api
- description: Used to interact with the current user's organization memberships, invitations and suggestions.
  name: Clerk Organizations Memberships API
  slug: clerk-com-organizations-memberships-api
- description: Used to interact with the passkeys of the logged in user.
  name: Clerk Passkeys API
  slug: clerk-com-passkeys-api
- description: Used to interact with payment attempts for users and organizations.
  name: Clerk Payment Attempts API
  slug: clerk-com-payment-attempts-api
- description: Used to interact with payment methods belonging to users and organizations.
  name: Clerk Payment Methods API
  slug: clerk-com-payment-methods-api
- description: A user can be associated with one or more phone numbers, which allows them to be contacted via SMS.
  name: Clerk Phone Numbers API
  slug: clerk-com-phone-numbers-api
- description: Used to interact with plans that users and organizations can purchase.
  name: Clerk Plans API
  slug: clerk-com-plans-api
- description: Check if a user is using a proxy.
  name: Clerk Proxy Checks API
  slug: clerk-com-proxy-checks-api
- description: The Proxy Health API from Clerk — 1 operation(s) for proxy health.
  name: Clerk Proxy Health API
  slug: clerk-com-proxy-health-api
- description: The Redirect API from Clerk — 1 operation(s) for redirect.
  name: Clerk Redirect API
  slug: clerk-com-redirect-api
- description: Redirect URLs are whitelisted URLs that facilitate secure authentication flows in native applications (e.g. React Native, Expo). In these contexts, Clerk ensures that security-critical nonces are pass
  name: Clerk Redirect URLs API
  slug: clerk-com-redirect-urls-api
- description: Role sets define collections of roles that can be assigned to organization members. Each organization uses one role set to determine the available roles for its members. Role sets support default role
  name: Clerk Role Sets API
  slug: clerk-com-role-sets-api
- description: The Roles API from Clerk — 1 operation(s) for roles.
  name: Clerk Roles API
  slug: clerk-com-roles-api
- description: Used in authentication flows using SAML.
  name: Clerk SAML API
  slug: clerk-com-saml-api
- description: A SAML Connection holds configuration data required for facilitating a SAML SSO flow between your Clerk Instance (SP) and a particular SAML IdP.
  name: Clerk SAML Connections API
  slug: clerk-com-saml-connections-api
- description: The Session object is an abstraction over an HTTP session. It models the period of information exchange between a user and the server. Sessions are created when a user successfully goes through the si
  name: Clerk Sessions API
  slug: clerk-com-sessions-api
- description: 'Sign-in tokens are JWTs that can be used to sign in to an application without specifying any credentials. A sign-in token can be used at most once and they can be consumed from the Frontend API using '
  name: Clerk Sign-in Tokens API
  slug: clerk-com-sign-in-tokens-api
- description: Used to sign in a user in the current client.
  name: Clerk Sign Ins API
  slug: clerk-com-sign-ins-api
- description: Sign-up objects track the progress of a sign-up attempt and store any field collected from user input.
  name: Clerk Sign Ups API
  slug: clerk-com-sign-ups-api
- description: Used to interact with billing statements for users and organizations.
  name: Clerk Statements API
  slug: clerk-com-statements-api
- description: Used to interact with subscription items belonging to users and organizations.
  name: Clerk Subscription Items API
  slug: clerk-com-subscription-items-api
- description: Used to interact with subscriptions belonging to users and organizations.
  name: Clerk Subscriptions API
  slug: clerk-com-subscriptions-api
- description: Tokens meant for use by end-to-end test suites in requests to the Frontend API, so as to bypass bot detection measures.
  name: Clerk Testing Tokens API
  slug: clerk-com-testing-tokens-api
- description: Used to interact with One Time Password authenticators of the current user.
  name: Clerk TOTP API
  slug: clerk-com-totp-api
- description: Used to interact with the properties of the current user.
  name: Clerk User API
  slug: clerk-com-user-api
- description: The user object represents a user that has successfully signed up to your application.
  name: Clerk Users API
  slug: clerk-com-users-api
- description: Used to interact with the waitlist.
  name: Clerk Waitlist API
  slug: clerk-com-waitlist-api
- description: Manage waitlist entries.
  name: Clerk Waitlist Entries API
  slug: clerk-com-waitlist-entries-api
- description: Used to interact with the web3 wallets of the logged in user.
  name: Clerk Web3 Wallets API
  slug: clerk-com-web3-wallets-api
- description: You can configure webhooks to be notified about various events that happen on your instance.
  name: Clerk Webhooks API
  slug: clerk-com-webhooks-api
- description: Well-known endpoints like JWKS, deep linking, and openid-configuration.
  name: Clerk Well Known API
  slug: clerk-com-well-known-api
artifact_total: 144
collections:
- collection_type: open
  name: Clerk Backend API
  slug: open-clerk-backend-api
- collection_type: open
  name: Clerk Frontend API
  slug: open-clerk-frontend-api
- collection_type: open
  name: Clerk Platform API
  slug: open-clerk-platform-api
- collection_type: open
  name: Clerk Webhook Events
  slug: open-clerk-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clerk-com-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clerk-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clerk-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clerk-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://clerk.com
- group: docs
  title: ''
  type: Documentation
  url: https://clerk.com/docs
- group: start
  title: ''
  type: Signup
  url: https://dashboard.clerk.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://dashboard.clerk.com/sign-in
- group: commercial
  title: ''
  type: Pricing
  url: https://clerk.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clerk.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clerk.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://clerk.com/security
- group: company
  title: ''
  type: Blog
  url: https://clerk.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://clerk.com/changelog
- group: operate
  title: ''
  type: ChangelogRSS
  url: https://clerk.com/changelog/atom.xml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clerk.com
- group: operate
  title: ''
  type: Support
  url: https://clerk.com/support
- group: build
  title: ''
  type: GitHub
  url: https://github.com/clerk
- group: docs
  title: ''
  type: OpenAPIRepository
  url: https://github.com/clerk/openapi-specs
- group: other
  title: ''
  type: X
  url: https://x.com/ClerkDev
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/javascript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-csharp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-flutter
- group: build
  title: ''
  type: CLI
  url: https://github.com/clerk/cli
- group: build
  title: ''
  type: CLI
  url: https://github.com/clerk/protect-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/clerk/agent-toolkit-example
- group: build
  title: ''
  type: Tools
  url: https://github.com/clerk/agentpass
- group: build
  title: ''
  type: Tools
  url: https://github.com/clerk/mcp-tools
- group: build
  title: ''
  type: Tools
  url: https://github.com/clerk/migration-tool
- group: commercial
  title: ''
  type: Plans
  url: plans/clerk-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clerk-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clerk-com-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/clerk-com-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clerk-com-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-user-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-user-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-session-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-session-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-organization-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-organization-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-organizationmembership-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-organizationmembership-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-organizationinvitation-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-organizationinvitation-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-invitation-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-invitation-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-emailaddress-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-emailaddress-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-phonenumber-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-phonenumber-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-client-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-client-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-oauthapplication-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-oauthapplication-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-samlconnection-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-samlconnection-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-jwttemplate-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-jwttemplate-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-signintoken-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-signintoken-structure.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/clerk-actortoken-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/clerk-actortoken-structure.json
- group: agent
  title: ''
  type: LlmsText
  url: https://clerk.com/llms.txt
created: '2026-05-22'
description: Clerk is a complete user management and authentication infrastructure platform offering embeddable UI components, flexible APIs, and admin dashboards. It provides full-stack authentication including multi-factor authentication, social sign-on, passkeys, organizations for B2B SaaS, billing, session management, and machine-to-machine authentication, with SDKs spanning Next.js, React, Expo, iOS, Android, Go, Python, Ruby, Java, PHP, and C#.
examples:
- key_count: 9
  name: Clerk Actortoken Example
  slug: clerk-actortoken-example
- key_count: 7
  name: Clerk Backend Api Getapikeys 200
  slug: clerk-backend-api-getapikeys-200
- key_count: 7
  name: Clerk Backend Api Getm2Mtokens 200
  slug: clerk-backend-api-getm2mtokens-200
- key_count: 7
  name: Clerk Backend Api Verifyoauthaccesstoken 200
  slug: clerk-backend-api-verifyoauthaccesstoken-200
- key_count: 10
  name: Clerk Client Example
  slug: clerk-client-example
- key_count: 9
  name: Clerk Emailaddress Example
  slug: clerk-emailaddress-example
- key_count: 7
  name: Clerk Frontend Api Getapikeys 200
  slug: clerk-frontend-api-getapikeys-200
- key_count: 7
  name: Clerk Frontend Api Gethealth 200
  slug: clerk-frontend-api-gethealth-200
- key_count: 7
  name: Clerk Frontend Api Getorganizationcreationdefaults 200
  slug: clerk-frontend-api-getorganizationcreationdefaults-200
- key_count: 10
  name: Clerk Invitation Example
  slug: clerk-invitation-example
- key_count: 10
  name: Clerk Jwttemplate Example
  slug: clerk-jwttemplate-example
- key_count: 21
  name: Clerk Oauthapplication Example
  slug: clerk-oauthapplication-example
- key_count: 18
  name: Clerk Organization Example
  slug: clerk-organization-example
- key_count: 15
  name: Clerk Organizationinvitation Example
  slug: clerk-organizationinvitation-example
- key_count: 11
  name: Clerk Organizationmembership Example
  slug: clerk-organizationmembership-example
- key_count: 11
  name: Clerk Phonenumber Example
  slug: clerk-phonenumber-example
- key_count: 7
  name: Clerk Platform Api Platformgetconfig 200
  slug: clerk-platform-api-platformgetconfig-200
- key_count: 7
  name: Clerk Platform Api Platformlistapplicationdomains 200
  slug: clerk-platform-api-platformlistapplicationdomains-200
- key_count: 7
  name: Clerk Platform Api Platformlistapplications 200
  slug: clerk-platform-api-platformlistapplications-200
- key_count: 7
  name: Clerk Platform Api Platformlistapplicationtransfers 200
  slug: clerk-platform-api-platformlistapplicationtransfers-200
- key_count: 7
  name: Clerk Platform Api Platformlistinstanceusers 200
  slug: clerk-platform-api-platformlistinstanceusers-200
- key_count: 7
  name: Clerk Platform Api Platformlistjwttemplates 200
  slug: clerk-platform-api-platformlistjwttemplates-200
- key_count: 7
  name: Clerk Platform Api Platformlistredirecturls 200
  slug: clerk-platform-api-platformlistredirecturls-200
- key_count: 14
  name: Clerk Session Example
  slug: clerk-session-example
- key_count: 8
  name: Clerk Signintoken Example
  slug: clerk-signintoken-example
- key_count: 46
  name: Clerk User Example
  slug: clerk-user-example
finops:
- name: Clerk Com Finops
  service_category: ''
  slug: clerk-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clerk-com.png
json_schemas:
- name: Clerk ActorToken
  property_count: 9
  slug: clerk-actortoken
- name: Clerk Client
  property_count: 10
  slug: clerk-client
- name: Clerk EmailAddress
  property_count: 9
  slug: clerk-emailaddress
- name: Clerk Invitation
  property_count: 10
  slug: clerk-invitation
- name: Clerk JWTTemplate
  property_count: 10
  slug: clerk-jwttemplate
- name: Clerk OAuthApplication
  property_count: 21
  slug: clerk-oauthapplication
- name: Clerk Organization
  property_count: 18
  slug: clerk-organization
- name: Clerk OrganizationInvitation
  property_count: 15
  slug: clerk-organizationinvitation
- name: Clerk OrganizationMembership
  property_count: 11
  slug: clerk-organizationmembership
- name: Clerk PhoneNumber
  property_count: 11
  slug: clerk-phonenumber
- name: Clerk SAMLConnection
  property_count: 27
  slug: clerk-samlconnection
- name: Clerk Session
  property_count: 14
  slug: clerk-session
- name: Clerk SignInToken
  property_count: 8
  slug: clerk-signintoken
- name: Clerk User
  property_count: 46
  slug: clerk-user
json_structures:
- name: Clerk Actortoken Structure
  property_count: 0
  slug: clerk-actortoken-structure
- name: Clerk Client Structure
  property_count: 0
  slug: clerk-client-structure
- name: Clerk Emailaddress Structure
  property_count: 0
  slug: clerk-emailaddress-structure
- name: Clerk Invitation Structure
  property_count: 0
  slug: clerk-invitation-structure
- name: Clerk Jwttemplate Structure
  property_count: 0
  slug: clerk-jwttemplate-structure
- name: Clerk Oauthapplication Structure
  property_count: 0
  slug: clerk-oauthapplication-structure
- name: Clerk Organization Structure
  property_count: 0
  slug: clerk-organization-structure
- name: Clerk Organizationinvitation Structure
  property_count: 0
  slug: clerk-organizationinvitation-structure
- name: Clerk Organizationmembership Structure
  property_count: 0
  slug: clerk-organizationmembership-structure
- name: Clerk Phonenumber Structure
  property_count: 0
  slug: clerk-phonenumber-structure
- name: Clerk Samlconnection Structure
  property_count: 0
  slug: clerk-samlconnection-structure
- name: Clerk Session Structure
  property_count: 0
  slug: clerk-session-structure
- name: Clerk Signintoken Structure
  property_count: 0
  slug: clerk-signintoken-structure
- name: Clerk User Structure
  property_count: 0
  slug: clerk-user-structure
jsonld:
- class_count: 66
  name: Clerk Com Context
  property_count: 6
  slug: clerk-com-context
layout: provider
modified: '2026-05-22'
name: Clerk
nav: Providers
network: true
overview: 'Clerk publishes 76 APIs on the [APIs.io](https://apis.io/) network, including Account Portal API, Active Sessions API, Actor Tokens API, and 73 more. Tagged areas include Authentication, Authorization, B2B SaaS, CIAM, and Identity Management.


  The Clerk catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Clerk''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, changelog, support, and 63 more developer resources.'
plans:
- name: Clerk Com Plans Pricing
  plan_count: 4
  slug: clerk-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Clerk Com Rate Limits
  slug: clerk-com-rate-limits
rules:
- name: Clerk API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: clerk-com-jsonschema-spectral-rules
- name: Clerk API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 4
    warn: 3
  slug: clerk-rules
score:
  band: strong
  composite: 68.5
  delta: 2.5
  facets:
    commercial_clarity: 84.2
    contract_quality: 65.2
    developer_ergonomics: 47.8
    discoverability: 92.5
    governance: 86.8
    operational_transparency: 47.4
  previous_composite: 66.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clerk-com/refs/heads/main/screenshots/clerk-com-2026-06-20T174512.png
security:
- kind: authentication
  name: Clerk Com Authentication
  slug: clerk-com-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Clerk Com Domain Security
  slug: clerk-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clerk Com Vulnerability Disclosure
  slug: clerk-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clerk-com
tags:
- Authentication
- Authorization
- B2B SaaS
- CIAM
- Identity Management
- MFA
- OAuth
- OpenID Connect
- Organizations
- Passkeys
- SAML
- Security
- Sessions
- SSO
- User Management
website: https://clerk.com
---
