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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Zitadel Agentic Access
  operation_count: 32
  slug: zitadel-agentic-access
  summary_line: 32 operations · 26 acting
api_count: 11
apis:
- description: The Zitadel Auth API provides endpoints for authenticated users to perform operations on their own accounts, including profile management, session handling, MFA setup, and personal data management. Ac
  name: Zitadel Auth API
  slug: auth-api
- description: The Zitadel Admin API provides instance-level configuration for Zitadel administrators. Used to configure instance-wide settings, default policies, SMTP, SMS providers, and manage identity providers a
  name: Zitadel Admin API
  slug: admin-api
- description: Zitadel implements the OpenID Connect and OAuth 2.0 standards for authentication and authorization flows. Provides authorization code flow, client credentials, device code, token introspection, and us
  name: Zitadel OIDC / OAuth 2.0
  slug: oidc-oauth
- description: Zitadel provides SAML 2.0 single sign-on support, enabling enterprises to integrate with Zitadel using SAML identity federation. Accessible at /saml/v2/.
  name: Zitadel SAML API
  slug: saml-api
- description: Manage OIDC, SAML, and API applications
  name: Zitadel Applications API
  slug: zitadel-applications-api
- description: Manage external identity provider configurations
  name: Zitadel Identity Providers API
  slug: zitadel-identity-providers-api
- description: Manage organizations and organizational domains
  name: Zitadel Organizations API
  slug: zitadel-organizations-api
- description: Manage login, password, and notification policies
  name: Zitadel Policies API
  slug: zitadel-policies-api
- description: Manage projects and project grants
  name: Zitadel Projects API
  slug: zitadel-projects-api
- description: Manage project roles and role grants
  name: Zitadel Roles API
  slug: zitadel-roles-api
- description: Manage human and machine users
  name: Zitadel Users API
  slug: zitadel-users-api
artifact_total: 93
collections:
- collection_type: postman
  name: Zitadel Management Applications API
  slug: postman-zitadel-applications-api
- collection_type: postman
  name: Zitadel Management Applications Identity Providers API
  slug: postman-zitadel-identity-providers-api
- collection_type: postman
  name: Zitadel Management Applications Organizations API
  slug: postman-zitadel-organizations-api
- collection_type: postman
  name: Zitadel Management Applications Policies API
  slug: postman-zitadel-policies-api
- collection_type: postman
  name: Zitadel Management Applications Projects API
  slug: postman-zitadel-projects-api
- collection_type: postman
  name: Zitadel Management Applications Roles API
  slug: postman-zitadel-roles-api
- collection_type: postman
  name: Zitadel Management Applications Users API
  slug: postman-zitadel-users-api
- collection_type: open
  name: Zitadel Management API
  slug: open-zitadel-management
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zitadel/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zitadel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zitadel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zitadel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zitadel-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://zitadel.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zitadel
- group: company
  title: ''
  type: Website
  url: https://zitadel.com
- group: docs
  title: ''
  type: Documentation
  url: https://zitadel.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zitadel
- group: build
  title: ''
  type: SDKs
  url: https://github.com/zitadel/zitadel-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/zitadel/zitadel-java
- group: build
  title: ''
  type: Tools
  url: https://github.com/zitadel/terraform-provider-zitadel
- group: build
  title: ''
  type: Tools
  url: https://github.com/zitadel/zitadel-charts
- group: start
  title: ''
  type: Signup
  url: https://zitadel.cloud/ui/register
- group: commercial
  title: ''
  type: Pricing
  url: https://zitadel.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zitadel.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zitadel.com/legal/terms-of-service
- group: commercial
  title: ''
  type: License
  url: https://github.com/zitadel/zitadel/blob/main/LICENSE
- group: design
  title: ''
  type: JSONLD
  url: json-ld/zitadel-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/zitadel-spectral.yaml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/zitadel-vocabulary.yaml
created: '2026-03-25'
description: Zitadel is an open source identity infrastructure platform providing secure authentication and user management with built-in support for OAuth 2.0, OpenID Connect, SAML 2.0, SCIM, FIDO2, and passkeys. It offers multi-tenancy, fine-grained authorization, and a comprehensive management API for building and operating identity-first applications. Available as cloud-hosted and self-hosted deployments.
examples:
- key_count: 5
  name: Zitadel Management Create Human User Example
  slug: zitadel-management-create-human-user-example
- key_count: 2
  name: Zitadel Management Create Organization Example
  slug: zitadel-management-create-organization-example
- key_count: 4
  name: Zitadel Management Create Project Example
  slug: zitadel-management-create-project-example
- key_count: 2
  name: Zitadel Management List Users Example
  slug: zitadel-management-list-users-example
features:
- description: Native multi-tenant architecture with organizations and projects.
  name: Multi-Tenancy
- description: Standards-compliant OAuth 2.0 and OpenID Connect support.
  name: OAuth 2.0 / OIDC
- description: Enterprise SAML 2.0 single sign-on for identity federation.
  name: SAML 2.0
- description: SCIM-based user provisioning from upstream identity providers.
  name: SCIM
- description: Passwordless authentication with FIDO2 and passkeys.
  name: FIDO2 / Passkeys
- description: Multi-factor authentication including TOTP, U2F, and FIDO2.
  name: MFA
- description: Deploy as a managed cloud service or self-hosted on Kubernetes.
  name: Self-Hosted or Cloud
finops:
- name: Zitadel Finops
  service_category: Identity / Authentication
  slug: zitadel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zitadel.png
integrations:
- description: Terraform provider for declarative Zitadel resource management.
  name: Terraform
- description: Helm charts for Zitadel deployment on Kubernetes.
  name: Kubernetes
- description: External identity provider integration with Google.
  name: Google Login
- description: External identity provider integration with GitHub.
  name: GitHub Login
- description: Federation with SAML identity providers.
  name: SAML IdPs
json_schemas:
- name: Application
  property_count: 4
  slug: zitadel-application
- name: AppResponse
  property_count: 4
  slug: zitadel-appresponse
- name: CreateApiAppRequest
  property_count: 2
  slug: zitadel-createapiapprequest
- name: CreateHumanUserRequest
  property_count: 6
  slug: zitadel-createhumanuserrequest
- name: CreateMachineUserRequest
  property_count: 4
  slug: zitadel-createmachineuserrequest
- name: CreateOidcAppRequest
  property_count: 11
  slug: zitadel-createoidcapprequest
- name: CreateProjectRequest
  property_count: 4
  slug: zitadel-createprojectrequest
- name: CreateUserResponse
  property_count: 2
  slug: zitadel-createuserresponse
- name: Error
  property_count: 3
  slug: zitadel-error
- name: HumanEmail
  property_count: 2
  slug: zitadel-humanemail
- name: HumanPhone
  property_count: 2
  slug: zitadel-humanphone
- name: HumanProfile
  property_count: 7
  slug: zitadel-humanprofile
- name: HumanUser
  property_count: 5
  slug: zitadel-humanuser
- name: ListDetails
  property_count: 3
  slug: zitadel-listdetails
- name: ListOrgsRequest
  property_count: 2
  slug: zitadel-listorgsrequest
- name: ListOrgsResponse
  property_count: 2
  slug: zitadel-listorgsresponse
- name: ListProjectsResponse
  property_count: 2
  slug: zitadel-listprojectsresponse
- name: ListQuery
  property_count: 3
  slug: zitadel-listquery
- name: ListUsersRequest
  property_count: 2
  slug: zitadel-listusersrequest
- name: ListUsersResponse
  property_count: 2
  slug: zitadel-listusersresponse
- name: LoginPolicy
  property_count: 13
  slug: zitadel-loginpolicy
- name: MachineUser
  property_count: 3
  slug: zitadel-machineuser
- name: Application
  property_count: 5
  slug: zitadel-management-application
- name: HumanUser
  property_count: 3
  slug: zitadel-management-human-user
- name: MachineUser
  property_count: 3
  slug: zitadel-management-machine-user
- name: ObjectDetails
  property_count: 4
  slug: zitadel-management-object-details
- name: Organization
  property_count: 5
  slug: zitadel-management-organization
- name: Project
  property_count: 7
  slug: zitadel-management-project
- name: User
  property_count: 8
  slug: zitadel-management-user
- name: Membership
  property_count: 4
  slug: zitadel-membership
- name: ObjectDetails
  property_count: 4
  slug: zitadel-objectdetails
- name: Organization
  property_count: 5
  slug: zitadel-organization
- name: OrgResponse
  property_count: 1
  slug: zitadel-orgresponse
- name: Project
  property_count: 8
  slug: zitadel-project
- name: ProjectResponse
  property_count: 1
  slug: zitadel-projectresponse
- name: User
  property_count: 7
  slug: zitadel-user
- name: UserResponse
  property_count: 1
  slug: zitadel-userresponse
json_structures:
- name: Zitadel Management Application Structure
  property_count: 4
  slug: zitadel-management-application-structure
- name: Zitadel Management Human User Structure
  property_count: 3
  slug: zitadel-management-human-user-structure
- name: Zitadel Management Machine User Structure
  property_count: 3
  slug: zitadel-management-machine-user-structure
- name: Zitadel Management Organization Structure
  property_count: 4
  slug: zitadel-management-organization-structure
- name: Zitadel Management Project Structure
  property_count: 6
  slug: zitadel-management-project-structure
- name: Zitadel Management User Structure
  property_count: 7
  slug: zitadel-management-user-structure
- name: Zitadel Structure
  property_count: 0
  slug: zitadel-structure
jsonld:
- class_count: 6
  name: Zitadel Context
  property_count: 15
  slug: zitadel-context
layout: provider
modified: '2026-05-19'
name: Zitadel
nav: Providers
network: true
overview: 'Zitadel publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Identity Providers API, Organizations API, and 4 more. Tagged areas include Authentication, Authorization, Identity Management, Open Source, and OAuth 2.0.


  The Zitadel catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Zitadel''s developer surface includes authentication, engineering blog, documentation, tooling, signup flow, pricing, and 16 more developer resources.'
plans:
- name: Zitadel Plans Pricing
  plan_count: 3
  slug: zitadel-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 2
  name: Zitadel Rate Limits
  slug: zitadel-rate-limits
rules:
- name: Zitadel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: zitadel-jsonschema-spectral-rules
- name: Zitadel API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: zitadel-spectral
score:
  band: strong
  composite: 58.1
  delta: -3.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 76.8
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zitadel/refs/heads/main/screenshots/zitadel-2026-06-20T201924.png
security:
- kind: authentication
  name: Zitadel Authentication
  slug: zitadel-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zitadel Domain Security
  slug: zitadel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zitadel Vulnerability Disclosure
  slug: zitadel-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zitadel
tags:
- Authentication
- Authorization
- Identity Management
- Open Source
- OAuth 2.0
- OIDC
use_cases:
- description: B2C identity for customer-facing applications and portals.
  name: Customer Identity
- description: B2B/B2E identity for employees, contractors, and partners.
  name: Workforce Identity
- description: Service account identity and OAuth client credentials flow.
  name: Machine Identity
- description: Tenant-isolated identity for multi-tenant SaaS applications.
  name: SaaS Multi-Tenancy
website: https://zitadel.com
---
