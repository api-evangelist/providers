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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Azure Ad Agentic Access
  operation_count: 14
  slug: azure-ad-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 6
apis:
- description: Business-to-consumer identity management solution.
  name: Azure AD B2C API
  slug: azure-ad-b2c-api
- description: Application registrations in Entra ID
  name: Azure Active Directory Applications API
  slug: azure-ad-applications-api
- description: Directory roles and objects
  name: Azure Active Directory Directory API
  slug: azure-ad-directory-api
- description: Microsoft 365 and security groups
  name: Azure Active Directory Groups API
  slug: azure-ad-groups-api
- description: Operations on the signed-in user
  name: Azure Active Directory Me API
  slug: azure-ad-me-api
- description: User accounts in the directory
  name: Azure Active Directory Users API
  slug: azure-ad-users-api
artifact_total: 33
collections:
- collection_type: open
  name: Microsoft Graph API (Azure AD)
  slug: open-azure-ad
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-ad-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-ad-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-ad-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-ad-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AzureAD
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/active-directory/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/azure-active-directory-identity/bg-p/Identity
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/get-started-azure-ad
created: '2024-01-01'
description: Microsoft's cloud-based identity and access management service that helps employees sign in and access resources. Azure AD provides OAuth, OpenID Connect, SAML, and other identity protocols for securing applications and managing user identities.
features:
- description: Enable users to sign in once and access all connected apps without re-authenticating.
  name: Single Sign-On
- description: Enforce MFA to add an extra layer of security beyond passwords.
  name: Multi-Factor Authentication
- description: Define access policies based on user, device, location, and risk signals.
  name: Conditional Access
- description: Industry-standard protocols for authorization and authentication.
  name: OAuth 2.0 and OpenID Connect
- description: Federate with thousands of SAML-based SaaS applications.
  name: SAML 2.0 Support
- description: Detect and respond to identity-based risks with AI-powered signals.
  name: Identity Protection
- description: Just-in-time privileged access with approval workflows and audit.
  name: Privileged Identity Management
- description: Invite external users from partner organizations to access your resources.
  name: B2B Collaboration
- description: Enable customer and partner identity management with Azure AD B2C and B2B.
  name: External Identities
finops:
- name: Azure Ad Finops
  service_category: API
  slug: azure-ad-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-ad.png
integrations:
- description: Provides identity and access management for all Microsoft 365 applications.
  name: Microsoft 365
- description: SAML-based SSO integration with Salesforce CRM and Platform.
  name: Salesforce
- description: Federated SSO and user provisioning for ServiceNow via SAML and SCIM.
  name: ServiceNow
- description: SAML SSO and SCIM provisioning for GitHub Enterprise organizations.
  name: GitHub Enterprise
- description: Federate Azure AD with AWS IAM Identity Center for cross-cloud SSO.
  name: AWS
layout: provider
modified: '2026-04-19'
name: Azure Active Directory
nav: Providers
network: true
overview: 'Azure Active Directory publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Directory API, Groups API, and 2 more. Tagged areas include Authentication, Authorization, Identity, OAuth, and OpenID Connect.


  Azure Active Directory''s developer surface includes authentication, developer portal, documentation, engineering blog, pricing, getting-started guide, and 7 more developer resources.'
plans:
- name: Azure Ad Plans Pricing
  plan_count: 3
  slug: azure-ad-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 5
  name: Azure Ad Rate Limits
  slug: azure-ad-rate-limits
scopes:
- name: Azure Ad Scopes
  scope_count: 8
  slug: azure-ad-scopes
  summary_line: 8 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 42.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 55.2
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/screenshots/azure-ad-2026-06-20T172836.png
security:
- kind: authentication
  name: Azure Ad Authentication
  slug: azure-ad-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Azure Ad Domain Security
  slug: azure-ad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azure-ad
tags:
- Authentication
- Authorization
- Identity
- OAuth
- OpenID Connect
- Single Sign-On
use_cases:
- description: Provide single sign-on for employees across thousands of SaaS applications.
  name: Enterprise SSO
- description: Implement zero trust architecture with identity as the control plane.
  name: Zero Trust Security
- description: Build customer-facing login with Azure AD B2C supporting social identities.
  name: Consumer Identity
- description: Secure APIs with OAuth 2.0 tokens issued by Azure AD.
  name: API Security
- description: Extend on-premises Active Directory to the cloud with Azure AD Connect.
  name: Hybrid Identity
website: https://portal.azure.com
---
