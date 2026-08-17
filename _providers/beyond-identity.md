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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 81
  human_in_the_loop: 4
  name: Beyond Identity Agentic Access
  operation_count: 150
  slug: beyond-identity-agentic-access
  summary_line: 150 operations · 81 acting · 4 human-in-the-loop
api_count: 17
apis:
- description: The Next Generation Beyond Identity API provides the latest version of the platform's REST endpoints including updated identity management, credential binding, continuous risk assessment, and policy e
  name: Beyond Identity Next Generation API
  slug: beyond-identity-next-gen-api
- description: An application represents a client application that uses Beyond Identity for authentication. This could be a native app, a single-page application, regular web application, or machine-to-machine appli
  name: Beyond Identity Applications API
  slug: beyond-identity-applications-api
- description: 'A authenticator configuration prescribes how an end user may authenticate themselves to Beyond Identity. Beyond Identity provides a Hosted Web Authenticator which will work out-of-the-box, as well as '
  name: Beyond Identity Authenticator Configurations API
  slug: beyond-identity-authenticator-configurations-api
- description: A credential binding job defines the state of binding a new credential to an identity. The state includes creation of the credential binding job to delivery of the credential binding method to complet
  name: Beyond Identity Credential Binding Jobs API
  slug: beyond-identity-credential-binding-jobs-api
- description: A credential is also known as a passkey. This is the public-private key pair that belongs to an identity.
  name: Beyond Identity Credentials API
  slug: beyond-identity-credentials-api
- description: A group is a logical collection of identities. Groups are commonly used as a predicate in a policy rule.
  name: Beyond Identity Groups API
  slug: beyond-identity-groups-api
- description: An identity is a unique identifier that may be used by an end-user to gain access governed by Beyond Identity.
  name: Beyond Identity Identities API
  slug: beyond-identity-identities-api
- description: Identity providers enable integration with external systems to support IdP-authorized workflows, such as passkey enrollment. They serve as the counterpart to SSO applications, focusing on initiating a
  name: Beyond Identity Identity Provider API
  slug: beyond-identity-identity-provider-api
- description: 'Launch mechanisms, or flow type configurations, define which authentication launch mechanisms are enabled and valid for different platforms (Android, iOS, macOS, Windows, Web, Linux, ChromeOS) within '
  name: Beyond Identity Launch Mechanisms API
  slug: beyond-identity-launch-mechanisms-api
- description: A realm is a unique administrative domain within a tenant. Realms may be used to define multiple development environments or for isolated administrative domains.
  name: Beyond Identity Realms API
  slug: beyond-identity-realms-api
- description: A resource server represents an API server that hosts a set of protected resources and is capable of accepting and responding to protected resource requests using access tokens. Clients can enable the
  name: Beyond Identity Resource Servers API
  slug: beyond-identity-resource-servers-api
- description: The Roles API from Beyond Identity — 8 operation(s) for roles.
  name: Beyond Identity Roles API
  slug: beyond-identity-roles-api
- description: The SCIM API from Beyond Identity — 7 operation(s) for scim.
  name: Beyond Identity SCIM API
  slug: beyond-identity-scim-api
- description: An SSO configuration defines how end users interact with supported SSO protocols and related services. Each configuration type represents a protocol or integration (e.g., SAML, WS-Federation, OIDC, SC
  name: Beyond Identity SSO Configs API
  slug: beyond-identity-sso-configs-api
- description: A tenant represents an organization in the Beyond Identity Cloud. Tenants contain all data necessary for that organization to operate.
  name: Beyond Identity Tenants API
  slug: beyond-identity-tenants-api
- description: A theme is a collection of configurable assets that unifies the end user login experience with your brand and products. It is primarily used to change the styling of the credential binding email.
  name: Beyond Identity Themes API
  slug: beyond-identity-themes-api
- description: The Tokens API from Beyond Identity — 2 operation(s) for tokens.
  name: Beyond Identity Tokens API
  slug: beyond-identity-tokens-api
artifact_total: 63
collections:
- collection_type: postman
  name: Beyond Identity Secure Access Applications API
  slug: postman-beyond-identity-applications-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Authenticator Configurations API
  slug: postman-beyond-identity-authenticator-configurations-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Credential Binding Jobs API
  slug: postman-beyond-identity-credential-binding-jobs-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Credentials API
  slug: postman-beyond-identity-credentials-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Groups API
  slug: postman-beyond-identity-groups-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Identities API
  slug: postman-beyond-identity-identities-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Identity Provider API
  slug: postman-beyond-identity-identity-provider-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Launch Mechanisms API
  slug: postman-beyond-identity-launch-mechanisms-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Realms API
  slug: postman-beyond-identity-realms-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Resource Servers API
  slug: postman-beyond-identity-resource-servers-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Roles API
  slug: postman-beyond-identity-roles-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications SCIM API
  slug: postman-beyond-identity-scim-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications SSO Configs API
  slug: postman-beyond-identity-sso-configs-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Tenants API
  slug: postman-beyond-identity-tenants-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Themes API
  slug: postman-beyond-identity-themes-api
- collection_type: postman
  name: Beyond Identity Secure Access Applications Tokens API
  slug: postman-beyond-identity-tokens-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Beyond Identity Secure Access Applications API
  slug: open-beyond-identity-applications-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Authenticator Configurations API
  slug: open-beyond-identity-authenticator-configurations-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Credential Binding Jobs API
  slug: open-beyond-identity-credential-binding-jobs-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Credentials API
  slug: open-beyond-identity-credentials-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Groups API
  slug: open-beyond-identity-groups-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Identities API
  slug: open-beyond-identity-identities-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Identity Provider API
  slug: open-beyond-identity-identity-provider-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Launch Mechanisms API
  slug: open-beyond-identity-launch-mechanisms-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Realms API
  slug: open-beyond-identity-realms-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Resource Servers API
  slug: open-beyond-identity-resource-servers-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Roles API
  slug: open-beyond-identity-roles-api
- collection_type: open
  name: Beyond Identity Secure Access Applications SCIM API
  slug: open-beyond-identity-scim-api
- collection_type: open
  name: Beyond Identity Secure Access Applications SSO Configs API
  slug: open-beyond-identity-sso-configs-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Tenants API
  slug: open-beyond-identity-tenants-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Themes API
  slug: open-beyond-identity-themes-api
- collection_type: open
  name: Beyond Identity Secure Access Applications Tokens API
  slug: open-beyond-identity-tokens-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/beyond-identity/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/beyond-identity-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/beyond-identity-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beyond-identity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beyond-identity-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.beyondidentity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.beyondidentity.com/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gobeyondidentity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beyond-identity-inc
- group: other
  title: ''
  type: X
  url: https://twitter.com/beyondidentity
- group: company
  title: ''
  type: Blog
  url: https://www.beyondidentity.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.beyondidentity.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.beyondidentity.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.beyondidentity.com/docs/release-notes/release-notes-changelog
- group: operate
  title: ''
  type: Support
  url: https://support.beyondidentity.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/beyond-identity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/beyond-identity-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/beyond-identity-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/beyond-identity-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/beyond-identity-context.jsonld
created: '2026-06-12'
description: Beyond Identity is a zero-trust passwordless authentication platform that eliminates passwords by binding credentials to physical devices using platform authenticators and cryptographic passkeys. The platform provides REST APIs for managing tenants, realms, identities, and device-bound credentials across workforce and customer identity use cases. Beyond Identity supports continuous risk assessment with device security signals, policy enforcement, and just-in-time access controls. The platform integrates with SCIM, OIDC, and OAuth 2.0 standards and offers multi-region deployment including US, EU, and FedRAMP environments.
examples:
- key_count: 5
  name: Beyond Identity Create Identity Example
  slug: beyond-identity-create-identity-example
- key_count: 5
  name: Beyond Identity Credential Binding Job Example
  slug: beyond-identity-credential-binding-job-example
finops:
- name: Beyond Identity Finops
  service_category: ''
  slug: beyond-identity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beyond-identity.png
json_schemas:
- name: Credential
  property_count: 9
  slug: beyond-identity-credential
- name: Identity
  property_count: 9
  slug: beyond-identity-identity
jsonld:
- class_count: 13
  name: Beyond Identity Context
  property_count: 24
  slug: beyond-identity-context
layout: provider
modified: '2026-06-12'
name: Beyond Identity
nav: Providers
network: true
overview: 'Beyond Identity publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Authenticator Configurations API, Credential Binding Jobs API, and 13 more. Tagged areas include Authentication, Passwordless, Zero Trust, Identity, and Passkeys.


  The Beyond Identity catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Beyond Identity''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, support, and 14 more developer resources.'
plans:
- name: Beyond Identity Plans Pricing
  plan_count: 3
  slug: beyond-identity-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 3
  name: Beyond Identity Rate Limits
  slug: beyond-identity-rate-limits
rules:
- name: Beyond Identity API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: beyond-identity-jsonschema-spectral-rules
score:
  band: strong
  composite: 62.1
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 79.4
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 62.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beyond-identity/refs/heads/main/screenshots/beyond-identity-2026-06-20T173212.png
security:
- kind: authentication
  name: Beyond Identity Authentication
  slug: beyond-identity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Beyond Identity Domain Security
  slug: beyond-identity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Beyond Identity Trust Center
  slug: beyond-identity-trust-center
  summary_line: SOC 2
slug: beyond-identity
tags:
- Authentication
- Passwordless
- Zero Trust
- Identity
- Passkeys
- MFA
- Device Security
- OAuth 2.0
- OIDC
- SCIM
website: https://www.beyondidentity.com/
---
