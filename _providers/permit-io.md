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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 146
  human_in_the_loop: 3
  name: Permit Io Agentic Access
  operation_count: 258
  slug: permit-io-agentic-access
  summary_line: 258 operations · 146 acting · 3 human-in-the-loop
api_count: 43
apis:
- description: None
  name: Permit.io Access Requests (EAP) API
  slug: permit-io-access-requests-eap-api
- description: The Activity Log API from Permit.io — 2 operation(s) for activity log.
  name: Permit.io Activity Log API
  slug: permit-io-activity-log-api
- description: The API History API from Permit.io — 4 operation(s) for api history.
  name: Permit.io API History API
  slug: permit-io-api-history-api
- description: The API Keys API from Permit.io — 5 operation(s) for api keys.
  name: Permit.io API Keys API
  slug: permit-io-api-keys-api
- description: The Audit Elements Data API from Permit.io — 1 operation(s) for audit elements data.
  name: Permit.io Audit Elements Data API
  slug: permit-io-audit-elements-data-api
- description: The Audit Log Replay API from Permit.io — 1 operation(s) for audit log replay.
  name: Permit.io Audit Log Replay API
  slug: permit-io-audit-log-replay-api
- description: The Audit Logs API from Permit.io — 2 operation(s) for audit logs.
  name: Permit.io Audit Logs API
  slug: permit-io-audit-logs-api
- description: None
  name: Permit.io Bulk Operations API
  slug: permit-io-bulk-operations-api
- description: Represents a "mini" ABAC rule comprised of (UserSet, Action, ResourceSet). If such tuple exists, it means all users matching the UserSet can perform the Action on the resources matching ResourceSet. E
  name: Permit.io Condition Set Rules API
  slug: permit-io-condition-set-rules-api
- description: Condition sets are sets of objects that are dynamically defined based on conditions on the objects' attributes. Conditions sets allows you the flexibility of ABAC with the simplicity of RBAC. There ar
  name: Permit.io Condition Sets API
  slug: permit-io-condition-sets-api
- description: The Deprecated API from Permit.io — 6 operation(s) for deprecated.
  name: Permit.io Deprecated API
  slug: permit-io-deprecated-api
- description: The Elements Configs (EAP) API from Permit.io — 4 operation(s) for elements configs (eap).
  name: Permit.io Elements Configs (EAP) API
  slug: permit-io-elements-configs-eap-api
- description: None
  name: Permit.io Email Configurations API
  slug: permit-io-email-configurations-api
- description: None
  name: Permit.io Email Templates API
  slug: permit-io-email-templates-api
- description: Environments are silos contained within projects that enables you to safely iterate on changes. Environments allow you to manage your policy throughout your entire development lifecycle, from dev to p
  name: Permit.io Environments API
  slug: permit-io-environments-api
- description: The Groups API from Permit.io — 10 operation(s) for groups.
  name: Permit.io Groups API
  slug: permit-io-groups-api
- description: The Implicit Grants API from Permit.io — 2 operation(s) for implicit grants.
  name: Permit.io Implicit Grants API
  slug: permit-io-implicit-grants-api
- description: The Invites API from Permit.io — 2 operation(s) for invites.
  name: Permit.io Invites API
  slug: permit-io-invites-api
- description: The Members API from Permit.io — 3 operation(s) for members.
  name: Permit.io Members API
  slug: permit-io-members-api
- description: The OPAL Data ( EAP ) API from Permit.io — 6 operation(s) for opal data ( eap ).
  name: Permit.io OPAL Data ( EAP ) API
  slug: permit-io-opal-data-eap-api
- description: The Operation Approval (EAP) API from Permit.io — 6 operation(s) for operation approval (eap).
  name: Permit.io Operation Approval (EAP) API
  slug: permit-io-operation-approval-eap-api
- description: 'The Organizations API gives you access to control and manage your Permit organizations. An organization represents a **single billable account** (i.e: a company using Permit). You may invite your team'
  name: Permit.io Organizations API
  slug: permit-io-organizations-api
- description: The Policy Decision Points API from Permit.io — 6 operation(s) for policy decision points.
  name: Permit.io Policy Decision Points API
  slug: permit-io-policy-decision-points-api
- description: The Policy Git Repositories API from Permit.io — 5 operation(s) for policy git repositories.
  name: Permit.io Policy Git Repositories API
  slug: permit-io-policy-git-repositories-api
- description: The Policy Guards (EAP) API from Permit.io — 5 operation(s) for policy guards (eap).
  name: Permit.io Policy Guards (EAP) API
  slug: permit-io-policy-guards-eap-api
- description: Projects let you manage permissions for different business objectives from a single Permit account. For example, you can create one project called "Billing App" and another project called "Web App". E
  name: Permit.io Projects API
  slug: permit-io-projects-api
- description: Proxy Config is set to enable the Permit Proxy to make proxied requests as part of the Frontend AuthZ.
  name: Permit.io Proxy Config API
  slug: permit-io-proxy-config-api
- description: The Relationship tuples API from Permit.io — 3 operation(s) for relationship tuples.
  name: Permit.io Relationship tuples API
  slug: permit-io-relationship-tuples-api
- description: Resource Action Groups are groups of actions that are assigned to a role as one action.
  name: Permit.io Resource Action Groups API
  slug: permit-io-resource-action-groups-api
- description: Actions are the various ways you can interact with a resource or affect the resource. Each (resource, action) pair defines a unique permission level.
  name: Permit.io Resource Actions API
  slug: permit-io-resource-actions-api
- description: Resource attributes allow you to specify an arbitrary schema attributes that are part of the definition of resource and must be included in any of its instances. Attributes are used to enforce attribu
  name: Permit.io Resource Attributes API
  slug: permit-io-resource-attributes-api
- description: Resource instances are instances of resource types. An instance represents **a single object** in your system on which you'd want to enforce authorization. You can use this API to store tenancy data (
  name: Permit.io Resource Instances API
  slug: permit-io-resource-instances-api
- description: The Resource Relations API from Permit.io — 2 operation(s) for resource relations.
  name: Permit.io Resource Relations API
  slug: permit-io-resource-relations-api
- description: Roles allow you to associate permissions indirectly via a job function. Resource roles allow you to grant roles that are scoped to a resource, thus expressing ownership or arbitrary relationships betw
  name: Permit.io Resource Roles API
  slug: permit-io-resource-roles-api
- description: Resources are *types* of objects or feature names that you wish to protect (or gate) with permissions. For example, if you build a document-sharing app like google docs, you might want to define a "do
  name: Permit.io Resources API
  slug: permit-io-resources-api
- description: 'Role Assignments are RBAC-constructs that state that a actor (i.e: user) is assigned a role within a tenant. With role assignments you can assign or unassign roles to a user. Role assignment define th'
  name: Permit.io Role Assignments API
  slug: permit-io-role-assignments-api
- description: 'Roles allow you to associate permissions indirectly via a job function. The Roles API allows you to manipulate roles: assign or unassign permissions to a role, define hierarchy between roles or define'
  name: Permit.io Roles API
  slug: permit-io-roles-api
- description: The Scope Configurations API from Permit.io — 1 operation(s) for scope configurations.
  name: Permit.io Scope Configurations API
  slug: permit-io-scope-configurations-api
- description: A tenant is a group of users that share a common organizational identity. Each tenant is a silo that can enforce strict boundaries between your customers. You can associate your protected objects with
  name: Permit.io Tenants API
  slug: permit-io-tenants-api
- description: 'User attributes allow you to specify an arbitrary schema attributes that are part of the definition of the User resource. Attributes are used to enforce attribute-based access control policies. *NOTE:'
  name: Permit.io User Attributes API
  slug: permit-io-user-attributes-api
- description: The User Invites API from Permit.io — 3 operation(s) for user invites.
  name: Permit.io User Invites API
  slug: permit-io-user-invites-api
- description: 'Users represent human end-users of your applications that you''d like to enforce permissions on. You must create a user object in Permit.io prior to trying to enforce permissions for that user. A user '
  name: Permit.io Users API
  slug: permit-io-users-api
- description: The Users Elements Data API from Permit.io — 6 operation(s) for users elements data.
  name: Permit.io Users Elements Data API
  slug: permit-io-users-elements-data-api
artifact_total: 96
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Access Requests (EAP) API
  slug: open-permit-io-access-requests-eap-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Activity Log API
  slug: open-permit-io-activity-log-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) API History API
  slug: open-permit-io-api-history-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) API Keys API
  slug: open-permit-io-api-keys-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Audit Elements Data API
  slug: open-permit-io-audit-elements-data-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Audit Log Replay API
  slug: open-permit-io-audit-log-replay-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Audit Logs API
  slug: open-permit-io-audit-logs-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Bulk Operations API
  slug: open-permit-io-bulk-operations-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Condition Set Rules API
  slug: open-permit-io-condition-set-rules-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Condition Sets API
  slug: open-permit-io-condition-sets-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Deprecated API
  slug: open-permit-io-deprecated-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Elements Configs (EAP) API
  slug: open-permit-io-elements-configs-eap-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Email Configurations API
  slug: open-permit-io-email-configurations-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Email Templates API
  slug: open-permit-io-email-templates-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Environments API
  slug: open-permit-io-environments-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Groups API
  slug: open-permit-io-groups-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Implicit Grants API
  slug: open-permit-io-implicit-grants-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Invites API
  slug: open-permit-io-invites-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Members API
  slug: open-permit-io-members-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) OPAL Data ( EAP ) API
  slug: open-permit-io-opal-data-eap-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Operation Approval (EAP) API
  slug: open-permit-io-operation-approval-eap-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Organizations API
  slug: open-permit-io-organizations-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Policy Decision Points API
  slug: open-permit-io-policy-decision-points-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Policy Git Repositories API
  slug: open-permit-io-policy-git-repositories-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Policy Guards (EAP) API
  slug: open-permit-io-policy-guards-eap-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Projects API
  slug: open-permit-io-projects-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Proxy Config API
  slug: open-permit-io-proxy-config-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Relationship tuples API
  slug: open-permit-io-relationship-tuples-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Resource Action Groups API
  slug: open-permit-io-resource-action-groups-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Resource Actions API
  slug: open-permit-io-resource-actions-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Resource Attributes API
  slug: open-permit-io-resource-attributes-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Resource Instances API
  slug: open-permit-io-resource-instances-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Resource Relations API
  slug: open-permit-io-resource-relations-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Resource Roles API
  slug: open-permit-io-resource-roles-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Resources API
  slug: open-permit-io-resources-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Role Assignments API
  slug: open-permit-io-role-assignments-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Roles API
  slug: open-permit-io-roles-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Scope Configurations API
  slug: open-permit-io-scope-configurations-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Tenants API
  slug: open-permit-io-tenants-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) User Attributes API
  slug: open-permit-io-user-attributes-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) User Invites API
  slug: open-permit-io-user-invites-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Users API
  slug: open-permit-io-users-api
- collection_type: open
  name: Permit.io Access Requests (EAP) Access Requests (EAP) Users Elements Data API
  slug: open-permit-io-users-elements-data-api
- collection_type: open
  name: Permit.io API
  slug: open-permit-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/permit-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/permit-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/permit-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/permit-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/permit-io-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/permitio
- group: company
  title: ''
  type: Website
  url: https://www.permit.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.permit.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.permit.io/v2/redoc
- group: start
  title: ''
  type: Signup
  url: https://app.permit.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/permitio
- group: company
  title: ''
  type: Blog
  url: https://www.permit.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.permit.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.permit.io
created: '2025-02-08'
description: Permit.io is an authorization-as-a-service platform that helps developers build, manage, and enforce fine-grained access control in their applications. It provides a Policy Decision Point (PDP), management API, REST API, and permission query APIs for role-based, attribute-based, and relationship-based access control with support for bulk checks, data filtering, and URL-based enforcement.
finops:
- name: Permit Io Finops
  service_category: API
  slug: permit-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/permit-io.png
layout: provider
modified: '2026-05-19'
name: Permit.io
nav: Providers
network: true
overview: 'Permit.io publishes 43 APIs on the [APIs.io](https://apis.io/) network, including Access Requests (EAP) API, Activity Log API, API History API, and 40 more. Tagged areas include Access Control, Authorization, Identity, Policy, and Security.


  Permit.io''s developer surface includes authentication, documentation, API reference, signup flow, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Permit Io Plans Pricing
  plan_count: 3
  slug: permit-io-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Permit Io Rate Limits
  slug: permit-io-rate-limits
score:
  band: developing
  composite: 41.2
  delta: 2.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 56.8
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 43
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 34.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/permit-io/refs/heads/main/screenshots/permit-io-2026-06-20T191609.png
security:
- kind: authentication
  name: Permit Io Authentication
  slug: permit-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Permit Io Domain Security
  slug: permit-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Permit Io Vulnerability Disclosure
  slug: permit-io-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Permit Io Trust Center
  slug: permit-io-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: permit-io
tags:
- Access Control
- Authorization
- Identity
- Policy
- Security
website: https://www.permit.io
---
