---
aid: amazon-iam-identity-center
name: Amazon IAM Identity Center
description: AWS IAM Identity Center (successor to AWS Single Sign-On) is where you create, or connect, your workforce identities in AWS once and manage access centrally across your AWS organization. You can create user identities directly in IAM Identity Center, or bring them from Microsoft Active Directory, and then use IAM Identity Center to manage user access to AWS accounts and business applications with single sign-on.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Access Control
  - Authentication
  - AWS
  - Identity Management
  - Single Sign-On
url: https://raw.githubusercontent.com/api-evangelist/amazon-iam-identity-center/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-iam-identity-center:aws-sso-admin-api
    name: AWS IAM Identity Center SSO Admin API
    description: Manages permission sets, account assignments, instances, and SSO configurations for centralized identity and access management across AWS accounts and organizations.
    humanURL: https://aws.amazon.com/iam/identity-center/
    baseURL: https://sso.amazonaws.com
    tags:
      - Access Control
      - Identity Management
      - Single Sign-On
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-iam-identity-center-sso-admin-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/iam/identity-center/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/iam/identity-center/pricing/
      - type: FAQ
        url: https://aws.amazon.com/iam/identity-center/faqs/
  - aid: amazon-iam-identity-center:aws-identitystore-api
    name: AWS IAM Identity Center Identity Store API
    description: Manages users, groups, and group memberships in the IAM Identity Center identity store, enabling programmatic provisioning of workforce identities.
    humanURL: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html
    baseURL: https://identitystore.amazonaws.com
    tags:
      - Groups
      - Identity Management
      - Users
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html
      - type: OpenAPI
        url: openapi/amazon-iam-identity-center-identitystore-openapi-original.yml
common:
  - type: Portal
    url: https://aws.amazon.com/iam/identity-center/
  - type: Website
    url: https://aws.amazon.com/iam/identity-center/
  - type: Documentation
    url: https://docs.aws.amazon.com/singlesignon/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/security/tag/aws-iam-identity-center/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/singlesignon/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-iam-identity-center-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/sso-admin.yaml
  - type: NaftikoCapability
    url: capabilities/shared/identitystore.yaml
  - type: NaftikoCapability
    url: capabilities/identity-access-management.yaml
  - type: Vocabulary
    url: vocabulary/amazon-iam-identity-center-vocabulary.yaml
  - type: JSONLD
    url: json-ld/amazon-iam-identity-center-context.jsonld
  - type: Features
    data:
      - name: Workforce Identity Management
        description: Create and manage workforce user identities directly or connect from an external identity provider.
      - name: Single Sign-On
        description: Enable employees to sign in once and access all assigned AWS accounts and business applications.
      - name: Centralized Access Management
        description: Manage access to multiple AWS accounts from a single place using permission sets.
      - name: External Identity Provider Integration
        description: Connect Microsoft Active Directory, Okta, Azure AD, and other SAML 2.0 identity providers.
      - name: Permission Set Management
        description: Define and reuse permission policies that can be assigned to users across multiple AWS accounts.
      - name: Automated Provisioning
        description: Automatically provision and de-provision users and groups using SCIM 2.0.
  - type: UseCases
    data:
      - name: Workforce SSO
        description: Enable employees to access all AWS accounts and business apps with a single set of credentials.
      - name: Centralized AWS Account Access
        description: Manage access to dozens or hundreds of AWS accounts from a single control plane.
      - name: Just-in-Time Access
        description: Grant temporary elevated access to AWS accounts without permanent permissions.
      - name: Compliance and Audit
        description: Centralize access logging and produce audit reports for security compliance reviews.
  - type: Integrations
    data:
      - name: Microsoft Active Directory
        description: Sync users and groups from Active Directory for SSO and access management.
      - name: Okta
        description: Connect Okta as an external identity provider using SAML 2.0 and SCIM.
      - name: Azure Active Directory
        description: Federate with Azure AD for identity synchronization and SSO.
      - name: AWS Organizations
        description: Manage access across all accounts in an AWS Organization from a single SSO configuration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
