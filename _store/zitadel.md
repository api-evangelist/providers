---
aid: zitadel
name: Zitadel
description: Zitadel is an open source identity infrastructure platform providing secure authentication and user management with built-in support for OAuth 2.0, OpenID Connect, SAML 2.0, SCIM, FIDO2, and passkeys. It offers multi-tenancy, fine-grained authorization, and a comprehensive management API for building and operating identity-first applications. Available as cloud-hosted and self-hosted deployments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - Identity Management
  - Open Source
  - OAuth 2.0
  - OIDC
url: https://raw.githubusercontent.com/api-evangelist/zitadel/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: zitadel:management-api
    name: Zitadel Management API
    description: The Zitadel Management API provides administrative operations for managing users, organizations, projects, applications, roles, policies, and identity providers within a Zitadel instance. Accessible via REST at /management/v1/ and via gRPC. Supports comprehensive CRUD operations for all identity management resources.
    humanURL: https://zitadel.com/docs/reference/api/management
    tags:
      - Identity Management
      - Authentication
      - User Management
      - Organizations
    properties:
      - type: Documentation
        url: https://zitadel.com/docs/reference/api/management
      - type: GitHubRepository
        url: https://github.com/zitadel/zitadel
      - type: OpenAPI
        url: openapi/zitadel-management-openapi.yml
      - type: JSONSchema
        url: json-schema/zitadel-management-user-schema.json
      - type: JSONSchema
        url: json-schema/zitadel-management-human-user-schema.json
      - type: JSONSchema
        url: json-schema/zitadel-management-machine-user-schema.json
      - type: JSONSchema
        url: json-schema/zitadel-management-organization-schema.json
      - type: JSONSchema
        url: json-schema/zitadel-management-project-schema.json
      - type: JSONSchema
        url: json-schema/zitadel-management-application-schema.json
      - type: JSONSchema
        url: json-schema/zitadel-management-object-details-schema.json
      - type: JSONStructure
        url: json-structure/zitadel-management-user-structure.json
      - type: JSONStructure
        url: json-structure/zitadel-management-human-user-structure.json
      - type: JSONStructure
        url: json-structure/zitadel-management-machine-user-structure.json
      - type: JSONStructure
        url: json-structure/zitadel-management-organization-structure.json
      - type: JSONStructure
        url: json-structure/zitadel-management-project-structure.json
      - type: JSONStructure
        url: json-structure/zitadel-management-application-structure.json
      - type: Example
        url: examples/zitadel-management-list-users-example.json
      - type: Example
        url: examples/zitadel-management-create-human-user-example.json
      - type: Example
        url: examples/zitadel-management-create-organization-example.json
      - type: Example
        url: examples/zitadel-management-create-project-example.json
  - aid: zitadel:auth-api
    name: Zitadel Auth API
    description: The Zitadel Auth API provides endpoints for authenticated users to perform operations on their own accounts, including profile management, session handling, MFA setup, and personal data management. Accessible at /auth/v1/.
    humanURL: https://zitadel.com/docs/apis/introduction
    tags:
      - Authentication
      - User Profile
      - Session Management
      - MFA
    properties:
      - type: Documentation
        url: https://zitadel.com/docs/apis/introduction
  - aid: zitadel:admin-api
    name: Zitadel Admin API
    description: The Zitadel Admin API provides instance-level configuration for Zitadel administrators. Used to configure instance-wide settings, default policies, SMTP, SMS providers, and manage identity providers at the system level. Accessible at /admin/v1/.
    humanURL: https://zitadel.com/docs/apis/introduction
    tags:
      - Administration
      - Identity Management
      - Configuration
    properties:
      - type: Documentation
        url: https://zitadel.com/docs/apis/introduction
  - aid: zitadel:oidc-oauth
    name: Zitadel OIDC / OAuth 2.0
    description: Zitadel implements the OpenID Connect and OAuth 2.0 standards for authentication and authorization flows. Provides authorization code flow, client credentials, device code, token introspection, and userinfo endpoints. Available at /oauth/v2/ and /oidc/v1/.
    humanURL: https://zitadel.com/docs/guides/integrate/login/oidc
    tags:
      - OAuth 2.0
      - OpenID Connect
      - Authentication
      - Authorization
    properties:
      - type: Documentation
        url: https://zitadel.com/docs/guides/integrate/login/oidc
  - aid: zitadel:saml-api
    name: Zitadel SAML API
    description: Zitadel provides SAML 2.0 single sign-on support, enabling enterprises to integrate with Zitadel using SAML identity federation. Accessible at /saml/v2/.
    humanURL: https://zitadel.com/docs/guides/integrate/login/saml
    tags:
      - SAML
      - Single Sign-On
      - Authentication
    properties:
      - type: Documentation
        url: https://zitadel.com/docs/guides/integrate/login/saml
common:
  - type: Website
    url: https://zitadel.com
  - type: Documentation
    url: https://zitadel.com/docs
  - type: GitHubOrganization
    url: https://github.com/zitadel
  - type: SDK
    url: https://github.com/zitadel/zitadel-go
    name: zitadel-go (Go)
  - type: SDK
    url: https://github.com/zitadel/zitadel-java
    name: zitadel-java (Java)
  - type: Tools
    url: https://github.com/zitadel/terraform-provider-zitadel
    name: Terraform Provider for Zitadel
  - type: Tools
    url: https://github.com/zitadel/zitadel-charts
    name: Zitadel Helm Charts
  - type: SignUp
    url: https://zitadel.cloud/ui/register
  - type: Pricing
    url: https://zitadel.com/pricing
  - type: PrivacyPolicy
    url: https://zitadel.com/legal/privacy-policy
  - type: TermsOfService
    url: https://zitadel.com/legal/terms-of-service
  - type: License
    url: https://github.com/zitadel/zitadel/blob/main/LICENSE
    name: GNU AGPLv3
  - type: JSONLD
    url: json-ld/zitadel-context.jsonld
  - type: SpectralRules
    url: rules/zitadel-spectral.yaml
  - type: NaftikoCapability
    url: capabilities/identity-onboarding.yaml
  - type: Vocabulary
    url: vocabulary/zitadel-vocabulary.yaml
  - data:
      - name: Multi-Tenancy
        description: Native multi-tenant architecture with organizations and projects.
      - name: OAuth 2.0 / OIDC
        description: Standards-compliant OAuth 2.0 and OpenID Connect support.
      - name: SAML 2.0
        description: Enterprise SAML 2.0 single sign-on for identity federation.
      - name: SCIM
        description: SCIM-based user provisioning from upstream identity providers.
      - name: FIDO2 / Passkeys
        description: Passwordless authentication with FIDO2 and passkeys.
      - name: MFA
        description: Multi-factor authentication including TOTP, U2F, and FIDO2.
      - name: Self-Hosted or Cloud
        description: Deploy as a managed cloud service or self-hosted on Kubernetes.
    name: Features
    type: Features
  - data:
      - name: Customer Identity
        description: B2C identity for customer-facing applications and portals.
      - name: Workforce Identity
        description: B2B/B2E identity for employees, contractors, and partners.
      - name: Machine Identity
        description: Service account identity and OAuth client credentials flow.
      - name: SaaS Multi-Tenancy
        description: Tenant-isolated identity for multi-tenant SaaS applications.
    name: UseCases
    type: UseCases
  - data:
      - name: Terraform
        description: Terraform provider for declarative Zitadel resource management.
      - name: Kubernetes
        description: Helm charts for Zitadel deployment on Kubernetes.
      - name: Google Login
        description: External identity provider integration with Google.
      - name: GitHub Login
        description: External identity provider integration with GitHub.
      - name: SAML IdPs
        description: Federation with SAML identity providers.
    name: Integrations
    type: Integrations
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
