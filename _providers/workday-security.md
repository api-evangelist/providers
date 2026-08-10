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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Workday Security Agentic Access
  operation_count: 17
  slug: workday-security-agentic-access
  summary_line: 17 operations · 1 acting
api_count: 13
apis:
- description: 'REST API for retrieving user activity logs and signon data from a Workday tenant. Returns detailed JSON records of user actions including task information, timestamps, IP addresses, activity actions, '
  name: Workday User Activity Logging API
  slug: workday-user-activity-logging-api
- description: Retrieve and monitor Workday account signon events where the username corresponds to a valid Workday account. Provides detailed signon history including timestamps, IP addresses, and authentication me
  name: Workday Security Account Signons API
  slug: workday-security-account-signons-api
- description: Retrieve audit log entries that record system events, configuration changes, and administrative actions for compliance monitoring.
  name: Workday Security Audit Logs API
  slug: workday-security-audit-logs-api
- description: Manage authentication policies and configurations including SSO, SAML, and multi-factor authentication settings.
  name: Workday Security Authentication Configuration API
  slug: workday-security-authentication-configuration-api
- description: Generate and retrieve compliance reports summarizing audit activity, policy adherence, and regulatory compliance status.
  name: Workday Security Compliance Reports API
  slug: workday-security-compliance-reports-api
- description: Manage domain security policies that define which security groups have access to specific Workday functional domains and the permission levels granted.
  name: Workday Security Domain Security Policies API
  slug: workday-security-domain-security-policies-api
- description: Obtain and manage OAuth 2.0 access tokens for authenticating REST API requests to Workday services.
  name: Workday Security OAuth Tokens API
  slug: workday-security-oauth-tokens-api
- description: Access security-specific audit records including permission changes, security group modifications, and access control events.
  name: Workday Security Security Audit API
  slug: workday-security-security-audit-api
- description: Manage the membership of users and integration system users within security groups.
  name: Workday Security Security Group Members API
  slug: workday-security-security-group-members-api
- description: Create, retrieve, and manage security groups that control access to Workday domains, business processes, and securable items.
  name: Workday Security Security Groups API
  slug: workday-security-security-groups-api
- description: Retrieve and manage active authentication sessions including signon history and session metadata.
  name: Workday Security Sessions API
  slug: workday-security-sessions-api
- description: Retrieve and monitor unidentified signon attempts where the provided username does not correspond to a valid Workday account. Used for detecting potential unauthorized access attempts.
  name: Workday Security Unidentified Signons API
  slug: workday-security-unidentified-signons-api
- description: Manage Workday user accounts including account status, credentials, and associated security configurations.
  name: Workday Security User Accounts API
  slug: workday-security-user-accounts-api
artifact_total: 60
collections:
- collection_type: postman
  name: Workday Security Workday Audit and Compliance Account Signons API
  slug: postman-workday-security-account-signons-api
- collection_type: postman
  name: Workday Security Workday Audit and Compliance Account Signons Audit Logs API
  slug: postman-workday-security-audit-logs-api
- collection_type: postman
  name: Workday Security Workday Audit and Compliance Account Signons Authentication Configuration API
  slug: postman-workday-security-authentication-configuration-api
- collection_type: postman
  name: Workday Security Workday Audit and Compliance Account Signons Compliance Reports API
  slug: postman-workday-security-compliance-reports-api
- collection_type: postman
  name: Workday Security Workday Audit and Compliance Account Signons Domain Security Policies API
  slug: postman-workday-security-domain-security-policies-api
- collection_type: postman
  name: Workday Security Workday Audit and Compliance Account Signons OAuth Tokens API
  slug: postman-workday-security-oauth-tokens-api
- collection_type: postman
  name: Workday Security Workday Audit and Compliance Account Signons Security Audit API
  slug: postman-workday-security-security-audit-api
- collection_type: postman
  name: Workday Security Workday Audit and Compliance Account Signons Security Group Members API
  slug: postman-workday-security-security-group-members-api
- collection_type: postman
  name: Workday Security Workday Audit and Compliance Account Signons Security Groups API
  slug: postman-workday-security-security-groups-api
- collection_type: postman
  name: Workday Security Workday Audit and Compliance Account Signons Sessions API
  slug: postman-workday-security-sessions-api
- collection_type: postman
  name: Workday Security Workday Audit and Compliance Account Signons Unidentified Signons API
  slug: postman-workday-security-unidentified-signons-api
- collection_type: postman
  name: Workday Security Workday Audit and Compliance Account Signons User Accounts API
  slug: postman-workday-security-user-accounts-api
- collection_type: open
  name: Workday Security Workday Audit and Compliance API
  slug: open-workday-security-audit
- collection_type: open
  name: Workday Security Workday Authentication API
  slug: open-workday-security-authentication
- collection_type: open
  name: Workday Security Workday Identity Management API
  slug: open-workday-security-identity-management
- collection_type: open
  name: Workday Security Groups API
  slug: open-workday-security-security-groups
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday-security/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-security-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workday-security-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workday-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-security-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/workday-security-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://community.workday.com
- group: start
  title: ''
  type: GettingStarted
  url: https://community.workday.com/articles/1317963
- group: docs
  title: ''
  type: Authentication Guide
  url: https://community.workday.com/articles/1311418
- group: auth
  title: ''
  type: Authentication
  url: https://doc.workday.com/admin-guide/en-us/workday-rest-api/workday-rest-api-authentication.html
- group: other
  title: ''
  type: Best Practices
  url: https://community.workday.com/articles/security-best-practices
- group: docs
  title: ''
  type: Documentation
  url: https://community.workday.com/api
- group: docs
  title: ''
  type: Reference
  url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
- group: operate
  title: ''
  type: RateLimits
  url: https://community.workday.com/articles/api-rate-limits
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workday.com
- group: operate
  title: ''
  type: Support
  url: https://www.workday.com/en-us/customer-experience/support.html
- group: company
  title: ''
  type: Website
  url: https://www.workday.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: auth
  title: ''
  type: Security
  url: https://www.workday.com/en-us/why-workday/trust/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.workday.com/en-us/why-workday/trust/compliance.html
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com/en-us/application-development.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/workday
- group: start
  title: ''
  type: Signup
  url: https://resourcecenter.workday.com/
- group: start
  title: ''
  type: Login
  url: https://www.myworkday.com
created: '2024-01-15'
description: Collection of Workday Security APIs for managing authentication, authorization, and security configurations including identity management, security groups, audit logging, privacy, and user activity monitoring.
finops:
- name: Workday Security Finops
  service_category: HR / Finance SaaS
  slug: workday-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-security.png
json_schemas:
- name: AccountRef
  property_count: 3
  slug: workday-security-accountref
- name: AccountSignon
  property_count: 21
  slug: workday-security-accountsignon
- name: ActorRef
  property_count: 3
  slug: workday-security-actorref
- name: AuditLogEntry
  property_count: 12
  slug: workday-security-auditlogentry
- name: AuthenticationPolicy
  property_count: 8
  slug: workday-security-authenticationpolicy
- name: ComplianceReport
  property_count: 9
  slug: workday-security-compliancereport
- name: DomainSecurityPolicy
  property_count: 6
  slug: workday-security-domainsecuritypolicy
- name: DomainSecurityPolicyRef
  property_count: 3
  slug: workday-security-domainsecuritypolicyref
- name: Error
  property_count: 2
  slug: workday-security-error
- name: OAuthError
  property_count: 2
  slug: workday-security-oautherror
- name: PermissionChange
  property_count: 10
  slug: workday-security-permissionchange
- name: PolicyPermission
  property_count: 2
  slug: workday-security-policypermission
- name: SecurityGroup
  property_count: 9
  slug: workday-security-securitygroup
- name: SecurityGroupMember
  property_count: 4
  slug: workday-security-securitygroupmember
- name: SecurityGroupRef
  property_count: 3
  slug: workday-security-securitygroupref
- name: Session
  property_count: 14
  slug: workday-security-session
- name: TargetRef
  property_count: 4
  slug: workday-security-targetref
- name: TokenResponse
  property_count: 5
  slug: workday-security-tokenresponse
- name: UnidentifiedSignon
  property_count: 7
  slug: workday-security-unidentifiedsignon
- name: UserAccount
  property_count: 10
  slug: workday-security-useraccount
- name: WorkerRef
  property_count: 3
  slug: workday-security-workerref
json_structures:
- name: Workday Security Structure
  property_count: 0
  slug: workday-security-structure
layout: provider
modified: '2026-05-19'
name: Workday Security
nav: Providers
network: true
overview: 'Workday Security publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account Signons API, Audit Logs API, Authentication Configuration API, and 9 more. Tagged areas include Access Control, Audit, Authentication, Compliance, and Enterprise.


  The Workday Security catalog on APIs.io includes 1 Spectral governance ruleset.


  Workday Security''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Workday Security Plans Pricing
  plan_count: 1
  slug: workday-security-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 1
  name: Workday Security Rate Limits
  slug: workday-security-rate-limits
rules:
- name: Workday Security API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-security-jsonschema-spectral-rules
scopes:
- name: Workday Security Scopes
  scope_count: 3
  slug: workday-security-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 63.6
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 61.2
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 63.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-security/refs/heads/main/screenshots/workday-security-2026-06-20T201611.png
security:
- kind: authentication
  name: Workday Security Authentication
  slug: workday-security-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Workday Security Domain Security
  slug: workday-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Workday Security Trust Center
  slug: workday-security-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday-security
tags:
- Access Control
- Audit
- Authentication
- Compliance
- Enterprise
- Identity Management
- Privacy
- SAML
- Security
- SSO
website: https://www.workday.com
---
