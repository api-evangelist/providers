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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Azure Ad Agentic Access
  operation_count: 14
  slug: azure-ad-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 9
apis:
- description: Business-to-consumer identity management solution.
  name: Azure AD B2C API
  slug: azure-ad-b2c-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Application registrations in Entra ID
  name: Azure Active Directory Applications API
  slug: azure-ad-applications-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Directory roles and objects
  name: Azure Active Directory Directory API
  slug: azure-ad-directory-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Microsoft 365 and security groups
  name: Azure Active Directory Groups API
  slug: azure-ad-groups-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations on the signed-in user
  name: Azure Active Directory Me API
  slug: azure-ad-me-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: User accounts in the directory
  name: Azure Active Directory Users API
  slug: azure-ad-users-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Authentication methods, Conditional Access policies, identity providers, cross-tenant access policies and External ID (B2X) user flows in Microsoft Entra ID.
  name: Microsoft Entra ID Sign-Ins and Policies API
  slug: azure-ad-signins-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Entitlement management, access packages, access reviews, privileged identity management and lifecycle workflows.
  name: Microsoft Entra ID Governance API
  slug: azure-ad-governance-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Generic directory object operations - check member groups and objects, resolve objects by id, validate properties - plus the tenant public key infrastructure.
  name: Microsoft Entra ID Directory Objects API
  slug: azure-ad-directory-objects-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Subscription lifecycle for Microsoft Graph change notifications - push events for created, updated and deleted directory objects over webhooks, Azure Event Hubs or Azure Event Grid.
  name: Microsoft Entra ID Change Notifications API
  slug: azure-ad-change-notifications-api
artifact_total: 47
asyncapis:
- description: ''
  name: Azure Ad Change Notifications Webhooks
  slug: azure-ad-change-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Graph API (Azure AD) Applications API
  slug: open-azure-ad-applications-api
- collection_type: open
  name: Microsoft Graph API (Azure AD) Applications Directory API
  slug: open-azure-ad-directory-api
- collection_type: open
  name: Microsoft Graph API (Azure AD) Applications Groups API
  slug: open-azure-ad-groups-api
- collection_type: open
  name: Microsoft Graph API (Azure AD) Applications Me API
  slug: open-azure-ad-me-api
- collection_type: open
  name: Microsoft Graph API (Azure AD) Applications Users API
  slug: open-azure-ad-users-api
- collection_type: open
  name: Microsoft Graph API (Azure AD)
  slug: open-azure-ad
common:
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id
- group: build
  title: ''
  type: SDKs
  url: packages/azure-ad-packages.yml
- group: auth
  title: ''
  type: Security
  url: security/azure-ad-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/azure-ad-lifecycle.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/azure-ad-conventions.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/azure-ad-trust-center.yml
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/graph/api/overview
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/azure-ad-change-notifications-webhooks.yml
- group: start
  title: ''
  type: Console
  url: https://developer.microsoft.com/en-us/graph/graph-explorer
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/microsoftgraph
- group: start
  title: ''
  type: SignUp
  url: https://azure.microsoft.com/en-us/free/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.microsoft.com/en-us/microsoft-365/roadmap
- group: operate
  title: ''
  type: Support
  url: https://developer.microsoft.com/en-us/graph/support
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/graph
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/azure-ad-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/azure-ad-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/azure-ad-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/azure-ad-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/azure-ad-components.yml
- group: build
  title: ''
  type: CLI
  url: cli/azure-ad-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/azure-ad-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/azure-ad-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/azure-ad-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/azure-ad-problem-types.yml
- group: auth
  title: ''
  type: Compliance
  url: security/azure-ad-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/azure-ad-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/azure-ad-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/azure-ad-tool-crosswalk.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/azure-ad-mcp.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/azure-ad-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/azure-ad-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/azure-ad-packages.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-ad-vulnerability-disclosure.yml
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
  url: https://www.microsoft.com/en-us/security/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.microsoft.com/en-us/security/blog/feed/
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
mcp_servers:
- description: Microsoft's own hosted MCP server for querying enterprise identity and directory data in a Microsoft Entra tenant with natural language. Rather than projecting one tool per Graph operation, it ships t
  name: Microsoft MCP Server for Enterprise
  slug: microsoft-mcp-server-for-enterprise
modified: '2026-09-06'
name: Microsoft Entra ID (formerly Azure AD)
nav: Providers
network: true
overview: 'Microsoft Entra ID (formerly Azure AD) publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Azure Active Directory Applications API, Azure Active Directory Directory API, Azure Active Directory Groups API, and 6 more. Tagged areas include Authentication, Authorization, Identity, OpenID Connect, and Single Sign-On.


  The Microsoft Entra ID (formerly Azure AD) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Microsoft Entra ID (formerly Azure AD)''s developer surface includes API reference, developer console, signup flow, support, sandbox, CLI, changelog, and 41 more developer resources.'
plans:
- name: Azure Ad Plans Pricing
  plan_count: 10
  slug: azure-ad-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 8
  name: Azure Ad Rate Limits
  slug: azure-ad-rate-limits
scopes:
- name: Azure Ad Scopes
  scope_count: 39
  slug: azure-ad-scopes
  summary_line: 39 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: exemplar
  composite: 77.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.1
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 52.0
    developer_ergonomics: 82.7
    discoverability: 81.5
    operational_transparency: 97.4
  previous_composite: 71.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: rising
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/screenshots/azure-ad-2026-06-20T172836.png
security:
- kind: authentication
  name: Azure Ad Authentication
  slug: azure-ad-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Azure Ad Domain Security
  slug: azure-ad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure Ad Vulnerability Disclosure
  slug: azure-ad-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Azure Ad Trust Center
  slug: azure-ad-trust-center
  summary_line: FedRAMP, NIST SP 800-53, HIPAA / HITECH, SOX
slug: azure-ad
tags:
- Authentication
- Authorization
- Identity
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
website: https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id
---
