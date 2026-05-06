---
aid: azure-ad
name: Azure Active Directory
description: Microsoft's cloud-based identity and access management service that helps employees sign in and access resources. Azure AD provides OAuth, OpenID Connect, SAML, and other identity protocols for securing applications and managing user identities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - Authorization
  - Identity
  - OAuth
  - OpenID Connect
  - Single Sign-On
url: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: azure-ad:microsoft-graph-api
    name: Microsoft Graph API
    description: The primary API for accessing Azure AD and other Microsoft 365 services.
    humanURL: https://docs.microsoft.com/en-us/graph/overview
    baseURL: https://graph.microsoft.com
    tags:
      - Directory
      - Identity
      - Microsoft 365
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/graph/api/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: Authentication
        url: https://docs.microsoft.com/en-us/graph/auth/
      - type: SDK
        url: https://docs.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: ChangeLog
        url: https://docs.microsoft.com/en-us/graph/changelog
  - aid: azure-ad:azure-ad-b2c-api
    name: Azure AD B2C API
    description: Business-to-consumer identity management solution.
    humanURL: https://docs.microsoft.com/en-us/azure/active-directory-b2c/
    baseURL: https://login.microsoftonline.com
    tags:
      - Authentication
      - B2C
      - Consumer Identity
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/azure/active-directory-b2c/overview
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/active-directory/
  - type: StatusPage
    url: https://status.azure.com
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/azure-active-directory-identity/bg-p/Identity
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: TermsOfService
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/get-started-azure-ad
  - type: Features
    data:
      - name: Single Sign-On
        description: Enable users to sign in once and access all connected apps without re-authenticating.
      - name: Multi-Factor Authentication
        description: Enforce MFA to add an extra layer of security beyond passwords.
      - name: Conditional Access
        description: Define access policies based on user, device, location, and risk signals.
      - name: OAuth 2.0 and OpenID Connect
        description: Industry-standard protocols for authorization and authentication.
      - name: SAML 2.0 Support
        description: Federate with thousands of SAML-based SaaS applications.
      - name: Identity Protection
        description: Detect and respond to identity-based risks with AI-powered signals.
      - name: Privileged Identity Management
        description: Just-in-time privileged access with approval workflows and audit.
      - name: B2B Collaboration
        description: Invite external users from partner organizations to access your resources.
      - name: External Identities
        description: Enable customer and partner identity management with Azure AD B2C and B2B.
  - type: UseCases
    data:
      - name: Enterprise SSO
        description: Provide single sign-on for employees across thousands of SaaS applications.
      - name: Zero Trust Security
        description: Implement zero trust architecture with identity as the control plane.
      - name: Consumer Identity
        description: Build customer-facing login with Azure AD B2C supporting social identities.
      - name: API Security
        description: Secure APIs with OAuth 2.0 tokens issued by Azure AD.
      - name: Hybrid Identity
        description: Extend on-premises Active Directory to the cloud with Azure AD Connect.
  - type: Integrations
    data:
      - name: Microsoft 365
        description: Provides identity and access management for all Microsoft 365 applications.
      - name: Salesforce
        description: SAML-based SSO integration with Salesforce CRM and Platform.
      - name: ServiceNow
        description: Federated SSO and user provisioning for ServiceNow via SAML and SCIM.
      - name: GitHub Enterprise
        description: SAML SSO and SCIM provisioning for GitHub Enterprise organizations.
      - name: AWS
        description: Federate Azure AD with AWS IAM Identity Center for cross-cloud SSO.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
