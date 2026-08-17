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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amazon Iam Agentic Access
  operation_count: 25
  slug: amazon-iam-agentic-access
  summary_line: 25 operations
api_count: 5
apis:
- description: Operations for managing IAM access keys
  name: Amazon IAM Access Keys API
  slug: amazon-iam-access-keys-api
- description: Operations for managing IAM groups
  name: Amazon IAM Groups API
  slug: amazon-iam-groups-api
- description: Operations for managing IAM policies
  name: Amazon IAM Policies API
  slug: amazon-iam-policies-api
- description: Operations for managing IAM roles
  name: Amazon IAM Roles API
  slug: amazon-iam-roles-api
- description: Operations for managing IAM users
  name: Amazon IAM Users API
  slug: amazon-iam-users-api
artifact_total: 100
collections:
- collection_type: postman
  name: Amazon IAM Access Keys API
  slug: postman-amazon-iam-access-keys-api
- collection_type: postman
  name: Amazon IAM Access Keys Groups API
  slug: postman-amazon-iam-groups-api
- collection_type: postman
  name: Amazon IAM Access Keys Policies API
  slug: postman-amazon-iam-policies-api
- collection_type: postman
  name: Amazon IAM Access Keys Roles API
  slug: postman-amazon-iam-roles-api
- collection_type: postman
  name: Amazon IAM Access Keys Users API
  slug: postman-amazon-iam-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon IAM Access Keys API
  slug: open-amazon-iam-access-keys-api
- collection_type: open
  name: Amazon IAM Access Keys Groups API
  slug: open-amazon-iam-groups-api
- collection_type: open
  name: Amazon IAM Access Keys Policies API
  slug: open-amazon-iam-policies-api
- collection_type: open
  name: Amazon IAM Access Keys Roles API
  slug: open-amazon-iam-roles-api
- collection_type: open
  name: Amazon IAM Access Keys Users API
  slug: open-amazon-iam-users-api
- collection_type: open
  name: Amazon IAM API
  slug: open-amazon-iam
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-iam/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-iam-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-iam-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-iam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-iam-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-iam-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/iam/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/iam/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/iam/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-iam
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-iam-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-iam-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-iam-vocabulary.yaml
created: '2026-03-16'
description: Amazon Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users, groups, roles, and policies, and use permissions to allow and deny their access to AWS resources. IAM is a feature of your AWS account offered at no additional charge.
examples:
- key_count: 5
  name: Amazon Iam Access Key Example
  slug: amazon-iam-access-key-example
- key_count: 1
  name: Amazon Iam Create Access Key Response Example
  slug: amazon-iam-create-access-key-response-example
- key_count: 1
  name: Amazon Iam Create Group Response Example
  slug: amazon-iam-create-group-response-example
- key_count: 1
  name: Amazon Iam Create Policy Response Example
  slug: amazon-iam-create-policy-response-example
- key_count: 1
  name: Amazon Iam Create Role Response Example
  slug: amazon-iam-create-role-response-example
- key_count: 1
  name: Amazon Iam Create User Response Example
  slug: amazon-iam-create-user-response-example
- key_count: 1
  name: Amazon Iam Get Group Response Example
  slug: amazon-iam-get-group-response-example
- key_count: 1
  name: Amazon Iam Get Policy Response Example
  slug: amazon-iam-get-policy-response-example
- key_count: 1
  name: Amazon Iam Get Role Response Example
  slug: amazon-iam-get-role-response-example
- key_count: 1
  name: Amazon Iam Get User Response Example
  slug: amazon-iam-get-user-response-example
- key_count: 5
  name: Amazon Iam Group Example
  slug: amazon-iam-group-example
- key_count: 1
  name: Amazon Iam List Access Keys Response Example
  slug: amazon-iam-list-access-keys-response-example
- key_count: 1
  name: Amazon Iam List Groups Response Example
  slug: amazon-iam-list-groups-response-example
- key_count: 1
  name: Amazon Iam List Policies Response Example
  slug: amazon-iam-list-policies-response-example
- key_count: 1
  name: Amazon Iam List Roles Response Example
  slug: amazon-iam-list-roles-response-example
- key_count: 1
  name: Amazon Iam List Users Response Example
  slug: amazon-iam-list-users-response-example
- key_count: 10
  name: Amazon Iam Policy Example
  slug: amazon-iam-policy-example
- key_count: 9
  name: Amazon Iam Role Example
  slug: amazon-iam-role-example
- key_count: 2
  name: Amazon Iam Tag Example
  slug: amazon-iam-tag-example
- key_count: 8
  name: Amazon Iam User Example
  slug: amazon-iam-user-example
features:
- description: Create, manage, and delete IAM users with fine-grained permissions.
  name: User Management
- description: Define IAM roles that can be assumed by users, services, or applications.
  name: Role-Based Access Control
- description: Create and attach identity-based and resource-based policies to control access.
  name: Policy Management
- description: Enable MFA for IAM users to add an extra layer of security.
  name: Multi-Factor Authentication
- description: Programmatically manage AWS access keys for long-term credentials.
  name: Access Key Management
- description: Use permission boundaries to define the maximum permissions an entity can have.
  name: Permission Boundaries
- description: Centrally control the maximum available permissions across AWS accounts.
  name: Service Control Policies
finops:
- name: Amazon Iam Finops
  service_category: API
  slug: amazon-iam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-iam.png
json_schemas:
- name: AccessKey
  property_count: 5
  slug: amazon-iam-access-key
- name: CreateAccessKeyResponse
  property_count: 1
  slug: amazon-iam-create-access-key-response
- name: CreateGroupResponse
  property_count: 1
  slug: amazon-iam-create-group-response
- name: CreatePolicyResponse
  property_count: 1
  slug: amazon-iam-create-policy-response
- name: CreateRoleResponse
  property_count: 1
  slug: amazon-iam-create-role-response
- name: CreateUserResponse
  property_count: 1
  slug: amazon-iam-create-user-response
- name: GetGroupResponse
  property_count: 1
  slug: amazon-iam-get-group-response
- name: GetPolicyResponse
  property_count: 1
  slug: amazon-iam-get-policy-response
- name: GetRoleResponse
  property_count: 1
  slug: amazon-iam-get-role-response
- name: GetUserResponse
  property_count: 1
  slug: amazon-iam-get-user-response
- name: Group
  property_count: 5
  slug: amazon-iam-group
- name: ListAccessKeysResponse
  property_count: 1
  slug: amazon-iam-list-access-keys-response
- name: ListGroupsResponse
  property_count: 1
  slug: amazon-iam-list-groups-response
- name: ListPoliciesResponse
  property_count: 1
  slug: amazon-iam-list-policies-response
- name: ListRolesResponse
  property_count: 1
  slug: amazon-iam-list-roles-response
- name: ListUsersResponse
  property_count: 1
  slug: amazon-iam-list-users-response
- name: Policy
  property_count: 10
  slug: amazon-iam-policy
- name: Role
  property_count: 9
  slug: amazon-iam-role
- name: Tag
  property_count: 2
  slug: amazon-iam-tag
- name: AWS IAM User
  property_count: 8
  slug: amazon-iam-user
json_structures:
- name: Amazon Iam Access Key Structure
  property_count: 5
  slug: amazon-iam-access-key-structure
- name: Amazon Iam Create Access Key Response Structure
  property_count: 1
  slug: amazon-iam-create-access-key-response-structure
- name: Amazon Iam Create Group Response Structure
  property_count: 1
  slug: amazon-iam-create-group-response-structure
- name: Amazon Iam Create Policy Response Structure
  property_count: 1
  slug: amazon-iam-create-policy-response-structure
- name: Amazon Iam Create Role Response Structure
  property_count: 1
  slug: amazon-iam-create-role-response-structure
- name: Amazon Iam Create User Response Structure
  property_count: 1
  slug: amazon-iam-create-user-response-structure
- name: Amazon Iam Get Group Response Structure
  property_count: 1
  slug: amazon-iam-get-group-response-structure
- name: Amazon Iam Get Policy Response Structure
  property_count: 1
  slug: amazon-iam-get-policy-response-structure
- name: Amazon Iam Get Role Response Structure
  property_count: 1
  slug: amazon-iam-get-role-response-structure
- name: Amazon Iam Get User Response Structure
  property_count: 1
  slug: amazon-iam-get-user-response-structure
- name: Amazon Iam Group Structure
  property_count: 5
  slug: amazon-iam-group-structure
- name: Amazon Iam List Access Keys Response Structure
  property_count: 1
  slug: amazon-iam-list-access-keys-response-structure
- name: Amazon Iam List Groups Response Structure
  property_count: 1
  slug: amazon-iam-list-groups-response-structure
- name: Amazon Iam List Policies Response Structure
  property_count: 1
  slug: amazon-iam-list-policies-response-structure
- name: Amazon Iam List Roles Response Structure
  property_count: 1
  slug: amazon-iam-list-roles-response-structure
- name: Amazon Iam List Users Response Structure
  property_count: 1
  slug: amazon-iam-list-users-response-structure
- name: Amazon Iam Policy Structure
  property_count: 10
  slug: amazon-iam-policy-structure
- name: Amazon Iam Role Structure
  property_count: 9
  slug: amazon-iam-role-structure
- name: Amazon Iam Tag Structure
  property_count: 2
  slug: amazon-iam-tag-structure
- name: Amazon Iam User Structure
  property_count: 8
  slug: amazon-iam-user-structure
jsonld:
- class_count: 0
  name: Amazon Iam Context
  property_count: 6
  slug: amazon-iam-context
layout: provider
modified: '2026-05-19'
name: Amazon IAM
nav: Providers
network: true
overview: 'Amazon IAM publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Access Keys API, Groups API, Policies API, and 2 more. Tagged areas include Access Management, Authentication, Authorization, Identity, and Security.


  The Amazon IAM catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon IAM''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 17 more developer resources.'
plans:
- name: Amazon Iam Plans Pricing
  plan_count: 3
  slug: amazon-iam-plans-pricing
random_paper: 108
rate_limits:
- limit_count: 5
  name: Amazon Iam Rate Limits
  slug: amazon-iam-rate-limits
rules:
- name: Amazon IAM API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-iam-jsonschema-spectral-rules
- name: Amazon IAM API Rules
  rule_count: 25
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 13
  slug: amazon-iam-spectral-rules
score:
  band: strong
  composite: 57.9
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 70.9
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-iam/refs/heads/main/screenshots/amazon-iam-2026-06-20T171703.png
security:
- kind: authentication
  name: Amazon Iam Authentication
  slug: amazon-iam-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Iam Domain Security
  slug: amazon-iam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Iam Vulnerability Disclosure
  slug: amazon-iam-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Iam Trust Center
  slug: amazon-iam-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-iam
tags:
- Access Management
- Authentication
- Authorization
- Identity
- Security
use_cases:
- description: Grant only the permissions required for specific tasks to reduce the attack surface.
  name: Least Privilege Access
- description: Enable users in one AWS account to assume roles in another account.
  name: Cross-Account Access
- description: Allow AWS services to access other services on your behalf through service roles.
  name: Service-to-Service Authorization
- description: Use STS to issue temporary security credentials for short-lived access.
  name: Temporary Credentials
- description: Audit IAM configurations to ensure compliance with security policies and regulations.
  name: Security Compliance
website: https://aws.amazon.com/iam/
---
