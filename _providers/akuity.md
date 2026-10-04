---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-10-03'
api_count: 8
apis:
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The ArgoCDService API from Akuity — 111 operation(s) for argocdservice.
  name: Akuity Argo CD Service API
  phrasing_intents:
  - id: ArgoCDService_ListInstanceVersions
    intent: List available Argo CD versions
    question: Which Argo CD versions can I run on a managed Akuity instance?
  - id: ArgoCDService_ListInstances
    intent: List Argo CD instances in an organization
    question: How do I see every Argo CD instance my organization runs?
  - id: ArgoCDService_CreateInstance
    intent: Create an Argo CD instance in an organization
    question: How do I spin up a new managed Argo CD instance for my organization?
  - id: ArgoCDService_GetAIAssistantUsageStats
    intent: Get AI assistant usage statistics
    question: How much has the AI assistant been used on my Argo CD instances?
  - id: ArgoCDService_GetSyncOperationsEvents
    intent: Query sync operation events
    question: Where can I find the history of sync operations across my Argo CD instances?
  - id: ArgoCDService_GetSyncOperationsStats
    intent: Get aggregated sync operation statistics
    question: How many sync operations succeeded or failed over time in my organization?
  - id: ArgoCDService_DeleteInstance
    intent: Delete an Argo CD instance from an organization
    question: How do I tear down an Argo CD instance my organization no longer needs?
  - id: ArgoCDService_GetInstance
    intent: Get an Argo CD instance in an organization
    question: How do I look up the details of one Argo CD instance in my org?
  phrasing_ops: 155
  slug: akuity-argocdservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The CustomRoleService API from Akuity — 2 operation(s) for customroleservice.
  name: Akuity Custom Role Service API
  phrasing_intents:
  - id: CustomRoleService_ListCustomRoles
    intent: List custom roles in an organization
    question: Which custom roles have we defined in our Akuity organization?
  - id: CustomRoleService_CreateCustomRole
    intent: Create a custom role
    question: How do I define a new role with my own permission policy?
  - id: CustomRoleService_DeleteCustomRole
    intent: Delete a custom role
    question: How do I remove a custom role we no longer use?
  - id: CustomRoleService_GetCustomRole
    intent: Get a custom role's definition
    question: What permissions does a particular custom role grant?
  - id: CustomRoleService_UpdateCustomRole
    intent: Update an existing custom role
    question: How do I change the permission policy on an existing custom role?
  phrasing_ops: 5
  slug: akuity-customroleservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The ExtensionService API from Akuity — 6 operation(s) for extensionservice.
  name: Akuity Extension Service API
  phrasing_intents:
  - id: ExtensionService_ListAuditRecordForApplication
    intent: List audit records for an Argo CD application
    question: Who changed my Argo CD application and when?
  - id: ExtensionService_GetSyncOperationsEventsForApplication
    intent: Get sync operation events for an application
    question: What sync operations has my Argo CD application gone through?
  - id: ExtensionService_GetSyncOperationsStatsForApplication
    intent: Get sync operation statistics for an application
    question: How many syncs does my Argo CD application run per day?
  - id: ExtensionService_ListAuditRecordForKargoProjects
    intent: List audit records for a Kargo project
    question: Who made changes in my Kargo project?
  - id: ExtensionService_GetKargoAnalysisLogs
    intent: Get logs from a Kargo analysis run job
    question: Why did my Kargo verification analysis fail?
  - id: ExtensionService_GetExtensionSettings
    intent: Get Kargo extension settings
    question: How is the Kargo UI extension configured?
  phrasing_ops: 6
  slug: akuity-extensionservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The KargoService API from Akuity — 39 operation(s) for kargoservice.
  name: Akuity Kargo Service API
  phrasing_intents:
  - id: KargoService_ListKargoInstances
    intent: List Kargo instances in an organization
    question: Which Kargo instances does my Akuity organization run?
  - id: KargoService_CreateKargoInstance
    intent: Create a Kargo instance at the organization level
    question: How do I spin up a new managed Kargo instance for my organization?
  - id: KargoService_GetPromotionEvents
    intent: Query Kargo promotion events for an organization
    question: What promotions have happened across all Kargo instances in my organization?
  - id: KargoService_GetPromotionStats
    intent: Get Kargo promotion statistics for an organization
    question: How many Kargo promotions ran over time across my whole organization?
  - id: KargoService_GetStageSpecificStats
    intent: Get per-stage Kargo stats for an organization
    question: Which Kargo stages see the most activity across my organization?
  - id: KargoService_DeleteInstance
    intent: Delete a Kargo instance by organization
    question: How do I tear down a Kargo instance I no longer need in my organization?
  - id: KargoService_PatchKargoInstance
    intent: Patch a Kargo instance's settings (org scope)
    question: Can I partially change a Kargo instance's configuration without resending all of it?
  - id: KargoService_UpdateKargoInstanceWorkspace
    intent: Move a Kargo instance to another workspace
    question: How can I transfer a Kargo instance from one workspace to a different one?
  phrasing_ops: 51
  slug: akuity-kargoservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The OrganizationService API from Akuity — 153 operation(s) for organizationservice.
  name: Akuity Organization Service API
  phrasing_intents:
  - id: OrganizationService_ListAvailablePlans
    intent: List available billing plans
    question: What subscription plans can I choose from on Akuity?
  - id: OrganizationService_ListAuthenticatedUserOrganizations
    intent: List the organizations I belong to
    question: Which organizations is my user account a member of?
  - id: OrganizationService_CreateOrganization
    intent: Create a new organization
    question: How do I set up a brand-new organization?
  - id: OrganizationService_DeleteOrganization
    intent: Delete an organization
    question: How do I permanently delete an organization I no longer need?
  - id: OrganizationService_GetOrganization
    intent: Get an organization's details
    question: What details are stored for a specific organization?
  - id: OrganizationService_UpdateOrganization
    intent: Update organization settings
    question: Can I rename my organization or change its MFA and AI settings?
  - id: OrganizationService_ListOrganizationAPIKeys
    intent: List organization-level API keys
    question: Which API keys have been issued at the organization level?
  - id: OrganizationService_CreateOrganizationAPIKey
    intent: Create an organization-level API key
    question: How do I generate an API key that works across the whole organization?
  phrasing_ops: 192
  slug: akuity-organizationservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The SystemService API from Akuity — 14 operation(s) for systemservice.
  name: Akuity System Service API
  phrasing_intents:
  - id: SystemService_GetAnnouncement
    intent: Get the current platform announcement
    question: Is there a current announcement banner on the Akuity Platform?
  - id: SystemService_GetAgentVersion
    intent: Get the current cluster agent version
    question: What version of the cluster agent is the platform currently shipping?
  - id: SystemService_ListAgentVersions
    intent: List available cluster agent versions
    question: Which cluster agent versions can I choose from?
  - id: SystemService_GetArgoCDAgentSizeSpec
    intent: Get Argo CD agent size specifications
    question: What CPU and memory do the different Argo CD agent sizes use?
  - id: SystemService_ListArgoCDExtensions
    intent: List available Argo CD extensions
    question: Which Argo CD UI extensions can I enable on a managed instance?
  - id: SystemService_ListArgoCDVersions
    intent: List supported Argo CD versions
    question: Which Argo CD versions can a managed instance run?
  - id: SystemService_ListValidEmailEvents
    intent: List events that can trigger email notifications
    question: Which platform events can send me email notifications?
  - id: SystemService_ListArgoCDImageUpadterVersions
    intent: List supported Argo CD Image Updater versions
    question: Which Argo CD Image Updater versions are available?
  phrasing_ops: 14
  slug: akuity-systemservice-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The Api Key Service API from Akuity — 4 operation(s) for api key service.
  name: Akuity Api Key Service API
  phrasing_intents:
  - id: APIKeyService_DeleteAPIKey
    intent: Delete an API key
    question: How do I revoke an API key that leaked?
  - id: APIKeyService_GetAPIKey
    intent: Get an API key's details
    question: What permissions and expiry does one of my Akuity API keys have?
  - id: APIKeyService_RegenerateAPIKeySecret
    intent: Regenerate an API key's secret
    question: How do I rotate the secret of an existing API key without creating a new key?
  - id: APIKeyService_DeleteWorkspaceAPIKey
    intent: Delete a workspace API key
    question: How do I revoke an API key issued for a single workspace?
  - id: APIKeyService_GetWorkspaceAPIKey
    intent: Get a workspace API key's details
    question: What does a workspace-scoped API key grant?
  - id: APIKeyService_RegenerateWorkspaceAPIKeySecret
    intent: Regenerate a workspace API key's secret
    question: How do I rotate the secret on a workspace-scoped API key?
  phrasing_ops: 6
  slug: akuity-api-key-service-api
- baseURL: https://akuity.cloud/api/v1
  baseurl_source: declared
  description: The Auth Service API from Akuity — 4 operation(s) for auth service.
  name: Akuity Auth Service API
  phrasing_intents:
  - id: AuthService_GetDeviceCode
    intent: Start a device login and get a device code
    question: How does a CLI start the device login flow for the Akuity Platform?
  - id: AuthService_GetDeviceToken
    intent: Exchange a device code for a token
    question: After approving a device login, how do I get the access token?
  - id: AuthService_RefreshAccessToken
    intent: Refresh an access token
    question: My session token expired; how do I refresh it?
  - id: AuthService_GetOIDCProviderDetails
    intent: Look up OIDC provider details from a discovery URL
    question: Can the platform read my identity provider's OIDC discovery document?
  phrasing_ops: 4
  slug: akuity-auth-service-api
artifact_total: 23
asyncapis:
- description: ''
  name: Akuity Notifications Webhooks
  slug: akuity-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Akuity Platform API — API Keys API Key Service API
  slug: open-akuity-apikeyservice-api
- collection_type: open
  name: Akuity Platform API — Argo CD Argo CD Service API
  slug: open-akuity-argocdservice-api
- collection_type: open
  name: Akuity Platform API — Auth Auth Service API
  slug: open-akuity-authservice-api
- collection_type: open
  name: Akuity Platform API — Custom Roles Custom Role Service API
  slug: open-akuity-customroleservice-api
- collection_type: open
  name: Akuity Platform API — Extension Extension Service API
  slug: open-akuity-extensionservice-api
- collection_type: open
  name: Akuity Platform API — Kargo Kargo Service API
  slug: open-akuity-kargoservice-api
- collection_type: open
  name: Akuity Platform API — Organization Organization Service API
  slug: open-akuity-organizationservice-api
- collection_type: open
  name: Akuity Platform API — System System Service API
  slug: open-akuity-systemservice-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/mcp/akuity-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/akuity-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/security/akuity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akuity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://akuity.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.akuity.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.akuity.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.akuity.io/akuity-portal/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.akuity.io/argocd/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://akuity.io/connect-with-akuity
- group: operate
  title: ''
  type: Community
  url: https://akuity.community/
- group: company
  title: ''
  type: Blog
  url: https://akuity.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akuity
- group: commercial
  title: ''
  type: Pricing
  url: https://akuity.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://akuity.cloud
- group: start
  title: ''
  type: Login
  url: https://akuity.cloud
- group: commercial
  title: ''
  type: TermsOfService
  url: https://akuity.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://akuity.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.akuity.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/security/akuity-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/akuity-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://akuity.io/security-compliance
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/security/akuity-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/akuity-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/security/akuity-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/akuity-vulnerability-disclosure.yml
- group: learn
  title: ''
  type: Training
  url: https://academy.akuity.io/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/llms/akuity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/akuity-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/packages/akuity-packages.yml
  title: ''
  type: Packages
  url: packages/akuity-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/packages/akuity-packages.yml
  title: ''
  type: SDKs
  url: packages/akuity-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/cli/akuity-cli.yml
  title: ''
  type: CLI
  url: cli/akuity-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/authentication/akuity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/akuity-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/conventions/akuity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/akuity-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/errors/akuity-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/akuity-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/lifecycle/akuity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/akuity-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/changelog/akuity-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/akuity-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/conformance/akuity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/akuity-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/data-model/akuity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/akuity-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/components/akuity-components.yml
  title: ''
  type: Components
  url: components/akuity-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/asyncapi/akuity-notifications-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/akuity-notifications-webhooks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/overlays/akuity-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/akuity-platform-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/plans/akuity-plans.yml
  title: ''
  type: Plans
  url: plans/akuity-plans.yml
created: '2026-08-06'
description: 'Akuity is the enterprise software delivery company founded by the creators of Argo CD and Kargo. The Akuity Platform is its commercial, fully-managed offering: hosted, enterprise-grade Argo CD control planes for GitOps continuous delivery, managed Kargo for multi-stage progressive promotion, the Akuity Agent for connecting target Kubernetes clusters, and Akuity Intelligence — an AI layer adding multi-cluster insight dashboards, on-call and promotion advisor agents, and AI-assisted remediation. The platform is controlled by a REST API at https://akuity.cloud/api/v1/, an `akuity` CLI, a Terraform provider and a Crossplane provider, all of which speak the same grpc-gateway service surface. Akuity runs on AWS with US and EU data residency and maintains SOC 2 Type II, ISO 27001:2022, PCI DSS 4.0.1, HIPAA-aligned and CSA STAR Level 1 posture.'
image: https://framerusercontent.com/images/GquIfu25ll0uHAbX9oobc0UUUE.png
layout: provider
modified: '2026-08-06'
name: Akuity
nav: Providers
network: true
overview: 'Akuity publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Argo CD Service API, Custom Role Service API, Extension Service API, and 5 more. Tagged areas include GitOps, Continuous Delivery, Kubernetes, ArgoCD, and Kargo.


  The Akuity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Akuity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Akuity Plans
  plan_count: 3
  slug: akuity-plans
random_paper: 3
score:
  band: exemplar
  composite: 72.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 58.3
    developer_ergonomics: 73.2
    discoverability: 78.6
    operational_transparency: 52.6
  previous_composite: 72.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/akuity/refs/heads/main/screenshots/akuity-2026-08-07T161137.png
security:
- kind: authentication
  name: Akuity Authentication
  slug: akuity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Akuity Domain Security
  slug: akuity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Akuity Vulnerability Disclosure
  slug: akuity-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Akuity Trust Center
  slug: akuity-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, PCI DSS v4.0.1, HIPAA, CSA STAR Level 1, GDPR
slug: akuity
tags:
- GitOps
- Continuous Delivery
- Kubernetes
- ArgoCD
- Kargo
- Platform Engineering
- DevOps
- Progressive Delivery
- Cloud-Native
- AIOps
- Developer Tools
website: https://akuity.io
---
