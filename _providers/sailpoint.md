---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Sailpoint Agentic Access
  operation_count: 30
  slug: sailpoint-agentic-access
  summary_line: 30 operations · 14 acting
api_count: 7
apis:
- description: The SailPoint Developer Forums are a great place to find solutions to common development problems.
  name: SailPoint
  slug: sailpoint
- description: The NERM V1 API provides endpoints for managing non-employee lifecycle, profiles, risk levels, risk scores, workflows, delegations, forms, roles, and user management within the Non-Employee Risk Manag
  name: SailPoint Non-Employee Risk Management V1 API
  slug: nerm-v1-api
- description: 'The NERM V2025 API provides the latest annual-release endpoints for the Non-Employee Risk Management platform, supporting application integrations and programmatic management of non-employee profiles '
  name: SailPoint Non-Employee Risk Management V2025 API
  slug: nerm-v2025-api
- description: Use this API to implement and customize access profile functionality. Access profiles group entitlements, which represent access rights on sources. For example, an Active Directory source can have mul
  name: SailPoint Access Profiles API
  slug: sailpoint-access-profiles-api
- description: Use this API to implement certification functionality. Certifications enable administrators and designated reviewers to review users' access to entitlements and decide whether to approve, revoke, or r
  name: SailPoint Certifications API
  slug: sailpoint-certifications-api
- description: Use this API to retrieve and manage public identity information. Public identities represent users within the Identity Security Cloud platform, including their attributes, lifecycle state, and manager
  name: SailPoint Identities API
  slug: sailpoint-identities-api
- description: Use this API to implement and customize role functionality. Roles represent the broadest level of access and group one or more access profiles. When you create a role and configure it with role criter
  name: SailPoint Roles API
  slug: sailpoint-roles-api
artifact_total: 76
collections:
- collection_type: postman
  name: Identity Security Cloud V3 Access Profiles API
  slug: postman-sailpoint-access-profiles-api
- collection_type: postman
  name: Identity Security Cloud V3 Access Profiles Certifications API
  slug: postman-sailpoint-certifications-api
- collection_type: postman
  name: Identity Security Cloud V3 Access Profiles Identities API
  slug: postman-sailpoint-identities-api
- collection_type: postman
  name: Identity Security Cloud V3 Access Profiles Roles API
  slug: postman-sailpoint-roles-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Identity Security Cloud V3 API
  slug: open-identity-security-cloud-v3
- collection_type: open
  name: Identity Security Cloud V3 Access Profiles API
  slug: open-sailpoint-access-profiles-api
- collection_type: open
  name: Identity Security Cloud V3 Access Profiles Certifications API
  slug: open-sailpoint-certifications-api
- collection_type: open
  name: Identity Security Cloud V3 Access Profiles Identities API
  slug: open-sailpoint-identities-api
- collection_type: open
  name: Identity Security Cloud V3 Access Profiles Roles API
  slug: open-sailpoint-roles-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sailpoint/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sailpoint-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sailpoint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sailpoint-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sailpoint-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sailpoint-technologies
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sailpoint.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sailpoint.com/idn/api/getting-started
- group: build
  title: ''
  type: SDKs
  url: https://developer.sailpoint.com/idn/tools/sdk
- group: operate
  title: ''
  type: Community
  url: https://developer.sailpoint.com/discuss
- group: company
  title: ''
  type: Blog
  url: https://www.sailpoint.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.sailpoint.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sailpoint.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sailpoint.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sailpoint.com/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: https://developer.sailpoint.com/docs/api/authentication/
- group: build
  title: ''
  type: PostmanCollection
  url: https://developer.sailpoint.com/docs/api/postman-collections/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sailpoint.com/docs/api/getting-started/
- group: design
  title: ''
  type: Versioning
  url: https://developer.sailpoint.com/docs/api/api-versioning-strategy/
- group: docs
  title: ''
  type: OpenAPI Source
  url: https://github.com/sailpoint-oss/api-specs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sailpoint-oss
- group: build
  title: ''
  type: Python SDK
  url: https://developer.sailpoint.com/docs/tools/sdk/python/
- group: build
  title: ''
  type: TypeScript SDK
  url: https://developer.sailpoint.com/docs/tools/sdk/typescript/
- group: build
  title: ''
  type: Go SDK
  url: https://developer.sailpoint.com/docs/tools/sdk/go/
- group: build
  title: ''
  type: PowerShell SDK
  url: https://developer.sailpoint.com/docs/tools/sdk/powershell/
- group: build
  title: ''
  type: CLI
  url: https://developer.sailpoint.com/docs/tools/cli/
- group: other
  title: ''
  type: Event Triggers
  url: https://developer.sailpoint.com/docs/extensibility/event-triggers/
- group: other
  title: ''
  type: Transforms
  url: https://developer.sailpoint.com/docs/extensibility/transforms/
- group: design
  title: ''
  type: Rules
  url: https://developer.sailpoint.com/docs/extensibility/rules/
- group: other
  title: ''
  type: SaaS Connectivity
  url: https://developer.sailpoint.com/docs/connectivity/saas-connectivity/
- group: company
  title: ''
  type: Developer Blog
  url: https://developer.sailpoint.com/blog/
- group: company
  title: ''
  type: Product News
  url: https://developer.sailpoint.com/discuss/c/announcements/product-news/65
- group: docs
  title: ''
  type: Product Documentation
  url: https://documentation.sailpoint.com/
- group: operate
  title: ''
  type: Compass Community
  url: https://community.sailpoint.com
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/sailpoint
- group: other
  title: ''
  type: CoLab
  url: https://developer.sailpoint.com/discuss/c/colab/59
- group: docs
  title: ''
  type: API Guidelines
  url: https://sailpoint-oss.github.io/sailpoint-api-guidelines/
- group: build
  title: ''
  type: Tools
  url: https://developer.sailpoint.com/docs/tools/
- group: other
  title: ''
  type: Rule Development Kit
  url: https://developer.sailpoint.com/docs/tools/rule-development-kit/
- group: other
  title: ''
  type: UI Development Kit
  url: https://developer.sailpoint.com/docs/tools/ui-development-kit/
- group: other
  title: ''
  type: Extensibility
  url: https://developer.sailpoint.com/docs/extensibility/
- group: agent
  title: ''
  type: MCP Server
  url: https://developer.sailpoint.com/docs/extensibility/mcp-getting-started/
- group: other
  title: ''
  type: Configuration Management
  url: https://developer.sailpoint.com/docs/extensibility/configuration-management/
- group: other
  title: ''
  type: Connectivity
  url: https://developer.sailpoint.com/docs/connectivity/
- group: docs
  title: ''
  type: Guides
  url: https://developer.sailpoint.com/docs/guides/
- group: docs
  title: ''
  type: Java Docs
  url: https://developer.sailpoint.com/docs/extensibility/rules/java-docs/
- group: docs
  title: ''
  type: Identity Security Cloud Documentation
  url: https://developer.sailpoint.com/docs/
created: '2025-02-17'
description: Enterprise identity security and governance platform providing identity management, access governance, and compliance solutions for workforce and non-employee identities. SailPoint delivers cloud-native IAM, certification automation, role mining, AI-driven recommendations, and developer-friendly APIs for integrating identity into any workflow.
examples:
- key_count: 6
  name: Sailpoint Certification Decision Example
  slug: sailpoint-certification-decision-example
- key_count: 6
  name: Sailpoint Create Access Profile Example
  slug: sailpoint-create-access-profile-example
- key_count: 6
  name: Sailpoint List Identities Example
  slug: sailpoint-list-identities-example
finops:
- name: Sailpoint Finops
  service_category: Identity Security / IGA
  slug: sailpoint-finops
image: https://www.sailpoint.com/wp-content/uploads/2021/02/sailpoint-logo.svg
json_schemas:
- name: AccessProfile
  property_count: 13
  slug: sailpoint-accessprofile
- name: AccessProfileBulkDeleteRequest
  property_count: 2
  slug: sailpoint-accessprofilebulkdeleterequest
- name: AccessProfileBulkDeleteResponse
  property_count: 2
  slug: sailpoint-accessprofilebulkdeleteresponse
- name: AccessProfileRef
  property_count: 3
  slug: sailpoint-accessprofileref
- name: AccessProfileSourceRef
  property_count: 3
  slug: sailpoint-accessprofilesourceref
- name: AccessReviewItem
  property_count: 7
  slug: sailpoint-accessreviewitem
- name: AccessSummary
  property_count: 2
  slug: sailpoint-accesssummary
- name: ApprovalScheme
  property_count: 2
  slug: sailpoint-approvalscheme
- name: CampaignReference
  property_count: 7
  slug: sailpoint-campaignreference
- name: CertificationDecision
  property_count: 4
  slug: sailpoint-certificationdecision
- name: CertificationIdentitySummary
  property_count: 4
  slug: sailpoint-certificationidentitysummary
- name: CertificationTask
  property_count: 6
  slug: sailpoint-certificationtask
- name: Entitlement
  property_count: 12
  slug: sailpoint-entitlement
- name: EntitlementRef
  property_count: 3
  slug: sailpoint-entitlementref
- name: EntitlementSourceRef
  property_count: 3
  slug: sailpoint-entitlementsourceref
- name: ErrorResponseDto
  property_count: 4
  slug: sailpoint-errorresponsedto
- name: SailPoint Identity Security Cloud Core Models
  property_count: 0
  slug: sailpoint-identity
- name: IdentityAttribute
  property_count: 3
  slug: sailpoint-identityattribute
- name: IdentityCertification
  property_count: 17
  slug: sailpoint-identitycertification
- name: IdentityCertificationDecisionSummary
  property_count: 3
  slug: sailpoint-identitycertificationdecisionsummary
- name: IdentityProfile
  property_count: 11
  slug: sailpoint-identityprofile
- name: IdentityReference
  property_count: 3
  slug: sailpoint-identityreference
- name: JsonPatchOperation
  property_count: 3
  slug: sailpoint-jsonpatchoperation
- name: OwnerReference
  property_count: 3
  slug: sailpoint-ownerreference
- name: PublicIdentity
  property_count: 8
  slug: sailpoint-publicidentity
- name: Reassignment
  property_count: 2
  slug: sailpoint-reassignment
- name: Requestability
  property_count: 3
  slug: sailpoint-requestability
- name: RequestabilityForRole
  property_count: 3
  slug: sailpoint-requestabilityforrole
- name: Reviewer
  property_count: 6
  slug: sailpoint-reviewer
- name: ReviewReassign
  property_count: 3
  slug: sailpoint-reviewreassign
- name: ReviewRecommendation
  property_count: 3
  slug: sailpoint-reviewrecommendation
- name: Revocability
  property_count: 3
  slug: sailpoint-revocability
- name: RevocabilityForRole
  property_count: 3
  slug: sailpoint-revocabilityforrole
- name: Role
  property_count: 15
  slug: sailpoint-role
- name: RoleBulkDeleteRequest
  property_count: 1
  slug: sailpoint-rolebulkdeleterequest
- name: RoleCriteriaKey
  property_count: 3
  slug: sailpoint-rolecriteriakey
- name: RoleCriteriaLevel1
  property_count: 4
  slug: sailpoint-rolecriterialevel1
- name: RoleCriteriaLevel2
  property_count: 4
  slug: sailpoint-rolecriterialevel2
- name: RoleCriteriaLevel3
  property_count: 3
  slug: sailpoint-rolecriterialevel3
- name: RoleIdentity
  property_count: 5
  slug: sailpoint-roleidentity
- name: RoleMembershipIdentity
  property_count: 4
  slug: sailpoint-rolemembershipidentity
- name: RoleMembershipSelector
  property_count: 3
  slug: sailpoint-rolemembershipselector
- name: SourceReference
  property_count: 3
  slug: sailpoint-sourcereference
- name: TaskResultSimplified
  property_count: 3
  slug: sailpoint-taskresultsimplified
json_structures:
- name: Sailpoint Identity Security Cloud Structure
  property_count: 0
  slug: sailpoint-identity-security-cloud-structure
- name: Sailpoint Structure
  property_count: 0
  slug: sailpoint-structure
jsonld:
- class_count: 0
  name: Sailpoint Context
  property_count: 19
  slug: sailpoint-context
layout: provider
modified: '2026-05-19'
name: SailPoint
nav: Providers
network: true
overview: 'SailPoint publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Access Profiles API, Certifications API, Identities API, and 1 more. Tagged areas include Access Governance, Compliance, IAM, Identity Management, and Identity Security.


  The SailPoint catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SailPoint''s developer surface includes authentication, getting-started guide, engineering blog, support, CLI, tooling, and 41 more developer resources.'
plans:
- name: Sailpoint Plans Pricing
  plan_count: 1
  slug: sailpoint-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 1
  name: Sailpoint Rate Limits
  slug: sailpoint-rate-limits
rules:
- name: SailPoint API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: sailpoint-jsonschema-spectral-rules
- name: SailPoint API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 6
  slug: sailpoint-rules
scopes:
- name: Sailpoint Scopes
  scope_count: 11
  slug: sailpoint-scopes
  summary_line: 11 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 57.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 75.6
    developer_ergonomics: 63.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 57.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sailpoint/refs/heads/main/screenshots/sailpoint-2026-06-20T193336.png
security:
- kind: authentication
  name: Sailpoint Authentication
  slug: sailpoint-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Sailpoint Domain Security
  slug: sailpoint-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sailpoint
tags:
- Access Governance
- Compliance
- IAM
- Identity Management
- Identity Security
- Security
website: https://developer.sailpoint.com
---
