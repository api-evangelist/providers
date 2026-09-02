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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Amazon Iam Access Analyzer Agentic Access
  operation_count: 28
  slug: amazon-iam-access-analyzer-agentic-access
  summary_line: 28 operations · 17 acting
api_count: 1
apis:
- description: The Access Preview#analyzerArn API from Amazon IAM Access Analyzer — 1 operation(s) for access preview#analyzerarn.
  name: Amazon IAM Access Analyzer Access Preview#analyzerArn API
  slug: amazon-iam-access-analyzer-access-preview-analyzerarn-api
- description: The Access Preview API from Amazon IAM Access Analyzer — 3 operation(s) for access preview.
  name: Amazon IAM Access Analyzer Access Preview API
  slug: amazon-iam-access-analyzer-access-preview-api
- description: The Analyzed Resource#analyzerArn&resourceArn API from Amazon IAM Access Analyzer — 1 operation(s) for analyzed resource#analyzerarn&resourcearn.
  name: Amazon IAM Access Analyzer Analyzed Resource#analyzerArn&resourceArn API
  slug: amazon-iam-access-analyzer-analyzed-resource-analyzerarn-resourcearn-api
- description: The Analyzed Resource API from Amazon IAM Access Analyzer — 1 operation(s) for analyzed resource.
  name: Amazon IAM Access Analyzer Analyzed Resource API
  slug: amazon-iam-access-analyzer-analyzed-resource-api
- description: The Analyzer API from Amazon IAM Access Analyzer — 4 operation(s) for analyzer.
  name: Amazon IAM Access Analyzer Analyzer API
  slug: amazon-iam-access-analyzer-analyzer-api
- description: The Archive Rule API from Amazon IAM Access Analyzer — 1 operation(s) for archive rule.
  name: Amazon IAM Access Analyzer Archive Rule API
  slug: amazon-iam-access-analyzer-archive-rule-api
- description: The Finding API from Amazon IAM Access Analyzer — 2 operation(s) for finding.
  name: Amazon IAM Access Analyzer Finding API
  slug: amazon-iam-access-analyzer-finding-api
- description: The Policy API from Amazon IAM Access Analyzer — 3 operation(s) for policy.
  name: Amazon IAM Access Analyzer Policy API
  slug: amazon-iam-access-analyzer-policy-api
- description: The Resource API from Amazon IAM Access Analyzer — 1 operation(s) for resource.
  name: Amazon IAM Access Analyzer Resource API
  slug: amazon-iam-access-analyzer-resource-api
- description: The Tags API from Amazon IAM Access Analyzer — 2 operation(s) for tags.
  name: Amazon IAM Access Analyzer Tags API
  slug: amazon-iam-access-analyzer-tags-api
artifact_total: 491
collections:
- collection_type: postman
  name: Access Analyzer Access Preview#analyzerArn API
  slug: postman-amazon-iam-access-analyzer-access-preview-analyzerarn-api
- collection_type: postman
  name: 'Access Analyzer #analyzerArn Access Preview API'
  slug: postman-amazon-iam-access-analyzer-access-preview-api
- collection_type: postman
  name: Access Analyzer Access Preview#analyzerArn Analyzed Resource#analyzerArn&resourceArn API
  slug: postman-amazon-iam-access-analyzer-analyzed-resource-analyzerarn-resourcearn-api
- collection_type: postman
  name: Access Analyzer Access Preview#analyzerArn Analyzed Resource API
  slug: postman-amazon-iam-access-analyzer-analyzed-resource-api
- collection_type: postman
  name: Access Access Preview#analyzerArn Analyzer API
  slug: postman-amazon-iam-access-analyzer-analyzer-api
- collection_type: postman
  name: Access Analyzer Access Preview#analyzerArn Archive Rule API
  slug: postman-amazon-iam-access-analyzer-archive-rule-api
- collection_type: postman
  name: Access Analyzer Access Preview#analyzerArn Finding API
  slug: postman-amazon-iam-access-analyzer-finding-api
- collection_type: postman
  name: Access Analyzer Access Preview#analyzerArn Policy API
  slug: postman-amazon-iam-access-analyzer-policy-api
- collection_type: postman
  name: Access Analyzer Access Preview#analyzerArn Resource API
  slug: postman-amazon-iam-access-analyzer-resource-api
- collection_type: postman
  name: Access Analyzer Access Preview#analyzerArn Tags API
  slug: postman-amazon-iam-access-analyzer-tags-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Access Analyzer Access Preview#analyzerArn Analyzed Resource#analyzerArn&resourceArn API
  slug: open-amazon-iam-access-analyzer-analyzed-resource-analyzerarn-resourcearn-api
- collection_type: open
  name: Access Analyzer Access Preview#analyzerArn Analyzed Resource API
  slug: open-amazon-iam-access-analyzer-analyzed-resource-api
- collection_type: open
  name: Access Access Preview#analyzerArn Analyzer API
  slug: open-amazon-iam-access-analyzer-analyzer-api
- collection_type: open
  name: Access Analyzer Access Preview#analyzerArn Archive Rule API
  slug: open-amazon-iam-access-analyzer-archive-rule-api
- collection_type: open
  name: Access Analyzer Access Preview#analyzerArn Finding API
  slug: open-amazon-iam-access-analyzer-finding-api
- collection_type: open
  name: Access Analyzer Access Preview#analyzerArn Policy API
  slug: open-amazon-iam-access-analyzer-policy-api
- collection_type: open
  name: Access Analyzer Access Preview#analyzerArn Resource API
  slug: open-amazon-iam-access-analyzer-resource-api
- collection_type: open
  name: Access Analyzer Access Preview#analyzerArn Tags API
  slug: open-amazon-iam-access-analyzer-tags-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-iam-access-analyzer/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-iam-access-analyzer-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-iam-access-analyzer-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-iam-access-analyzer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-iam-access-analyzer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-iam-access-analyzer-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/iam/features/analyze-access/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/iam/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html
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
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/tag/iam-access-analyzer/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/access-analyzer/
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
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-iam-access-analyzer-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-iam-access-analyzer-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-iam-access-analyzer-context.jsonld
created: '2026-03-16'
description: AWS IAM Access Analyzer helps you set, verify, and refine your IAM policies by providing a suite of capabilities including findings for external, internal, and unused access, basic and custom policy checks for validating policies, and policy generation to generate fine-grained policies. It uses automated reasoning to identify resources shared with external entities and helps implement least privilege access across your AWS environment.
examples:
- key_count: 6
  name: Iam Access Analyzer Access Preview Example
  slug: iam-access-analyzer-access-preview-example
- key_count: 15
  name: Iam Access Analyzer Access Preview Finding Example
  slug: iam-access-analyzer-access-preview-finding-example
- key_count: 1
  name: Iam Access Analyzer Access Preview Status Reason Example
  slug: iam-access-analyzer-access-preview-status-reason-example
- key_count: 5
  name: Iam Access Analyzer Access Preview Summary Example
  slug: iam-access-analyzer-access-preview-summary-example
- key_count: 2
  name: Iam Access Analyzer Acl Grantee Example
  slug: iam-access-analyzer-acl-grantee-example
- key_count: 11
  name: Iam Access Analyzer Analyzed Resource Example
  slug: iam-access-analyzer-analyzed-resource-example
- key_count: 3
  name: Iam Access Analyzer Analyzed Resource Summary Example
  slug: iam-access-analyzer-analyzed-resource-summary-example
- key_count: 9
  name: Iam Access Analyzer Analyzer Summary Example
  slug: iam-access-analyzer-analyzer-summary-example
- key_count: 3
  name: Iam Access Analyzer Apply Archive Rule Request Example
  slug: iam-access-analyzer-apply-archive-rule-request-example
- key_count: 4
  name: Iam Access Analyzer Archive Rule Summary Example
  slug: iam-access-analyzer-archive-rule-summary-example
- key_count: 0
  name: Iam Access Analyzer Cancel Policy Generation Request Example
  slug: iam-access-analyzer-cancel-policy-generation-request-example
- key_count: 0
  name: Iam Access Analyzer Cancel Policy Generation Response Example
  slug: iam-access-analyzer-cancel-policy-generation-response-example
- key_count: 4
  name: Iam Access Analyzer Cloud Trail Details Example
  slug: iam-access-analyzer-cloud-trail-details-example
- key_count: 3
  name: Iam Access Analyzer Cloud Trail Properties Example
  slug: iam-access-analyzer-cloud-trail-properties-example
- key_count: 0
  name: Iam Access Analyzer Condition Key Map Example
  slug: iam-access-analyzer-condition-key-map-example
- key_count: 11
  name: Iam Access Analyzer Configuration Example
  slug: iam-access-analyzer-configuration-example
- key_count: 0
  name: Iam Access Analyzer Configurations Map Example
  slug: iam-access-analyzer-configurations-map-example
- key_count: 3
  name: Iam Access Analyzer Create Access Preview Request Example
  slug: iam-access-analyzer-create-access-preview-request-example
- key_count: 1
  name: Iam Access Analyzer Create Access Preview Response Example
  slug: iam-access-analyzer-create-access-preview-response-example
- key_count: 5
  name: Iam Access Analyzer Create Analyzer Request Example
  slug: iam-access-analyzer-create-analyzer-request-example
- key_count: 1
  name: Iam Access Analyzer Create Analyzer Response Example
  slug: iam-access-analyzer-create-analyzer-response-example
- key_count: 3
  name: Iam Access Analyzer Create Archive Rule Request Example
  slug: iam-access-analyzer-create-archive-rule-request-example
- key_count: 4
  name: Iam Access Analyzer Criterion Example
  slug: iam-access-analyzer-criterion-example
- key_count: 0
  name: Iam Access Analyzer Delete Analyzer Request Example
  slug: iam-access-analyzer-delete-analyzer-request-example
- key_count: 0
  name: Iam Access Analyzer Delete Archive Rule Request Example
  slug: iam-access-analyzer-delete-archive-rule-request-example
- key_count: 3
  name: Iam Access Analyzer Ebs Snapshot Configuration Example
  slug: iam-access-analyzer-ebs-snapshot-configuration-example
- key_count: 1
  name: Iam Access Analyzer Ecr Repository Configuration Example
  slug: iam-access-analyzer-ecr-repository-configuration-example
- key_count: 1
  name: Iam Access Analyzer Efs File System Configuration Example
  slug: iam-access-analyzer-efs-file-system-configuration-example
- key_count: 0
  name: Iam Access Analyzer Filter Criteria Map Example
  slug: iam-access-analyzer-filter-criteria-map-example
- key_count: 14
  name: Iam Access Analyzer Finding Example
  slug: iam-access-analyzer-finding-example
- key_count: 2
  name: Iam Access Analyzer Finding Source Detail Example
  slug: iam-access-analyzer-finding-source-detail-example
- key_count: 2
  name: Iam Access Analyzer Finding Source Example
  slug: iam-access-analyzer-finding-source-example
- key_count: 14
  name: Iam Access Analyzer Finding Summary Example
  slug: iam-access-analyzer-finding-summary-example
- key_count: 1
  name: Iam Access Analyzer Generated Policy Example
  slug: iam-access-analyzer-generated-policy-example
- key_count: 3
  name: Iam Access Analyzer Generated Policy Properties Example
  slug: iam-access-analyzer-generated-policy-properties-example
- key_count: 2
  name: Iam Access Analyzer Generated Policy Result Example
  slug: iam-access-analyzer-generated-policy-result-example
- key_count: 0
  name: Iam Access Analyzer Get Access Preview Request Example
  slug: iam-access-analyzer-get-access-preview-request-example
- key_count: 1
  name: Iam Access Analyzer Get Access Preview Response Example
  slug: iam-access-analyzer-get-access-preview-response-example
- key_count: 0
  name: Iam Access Analyzer Get Analyzed Resource Request Example
  slug: iam-access-analyzer-get-analyzed-resource-request-example
- key_count: 1
  name: Iam Access Analyzer Get Analyzed Resource Response Example
  slug: iam-access-analyzer-get-analyzed-resource-response-example
- key_count: 0
  name: Iam Access Analyzer Get Analyzer Request Example
  slug: iam-access-analyzer-get-analyzer-request-example
- key_count: 1
  name: Iam Access Analyzer Get Analyzer Response Example
  slug: iam-access-analyzer-get-analyzer-response-example
- key_count: 0
  name: Iam Access Analyzer Get Archive Rule Request Example
  slug: iam-access-analyzer-get-archive-rule-request-example
- key_count: 1
  name: Iam Access Analyzer Get Archive Rule Response Example
  slug: iam-access-analyzer-get-archive-rule-response-example
- key_count: 0
  name: Iam Access Analyzer Get Finding Request Example
  slug: iam-access-analyzer-get-finding-request-example
- key_count: 1
  name: Iam Access Analyzer Get Finding Response Example
  slug: iam-access-analyzer-get-finding-response-example
- key_count: 0
  name: Iam Access Analyzer Get Generated Policy Request Example
  slug: iam-access-analyzer-get-generated-policy-request-example
- key_count: 2
  name: Iam Access Analyzer Get Generated Policy Response Example
  slug: iam-access-analyzer-get-generated-policy-response-example
- key_count: 1
  name: Iam Access Analyzer Iam Role Configuration Example
  slug: iam-access-analyzer-iam-role-configuration-example
- key_count: 2
  name: Iam Access Analyzer Inline Archive Rule Example
  slug: iam-access-analyzer-inline-archive-rule-example
- key_count: 0
  name: Iam Access Analyzer Internet Configuration Example
  slug: iam-access-analyzer-internet-configuration-example
- key_count: 5
  name: Iam Access Analyzer Job Details Example
  slug: iam-access-analyzer-job-details-example
- key_count: 2
  name: Iam Access Analyzer Job Error Example
  slug: iam-access-analyzer-job-error-example
- key_count: 0
  name: Iam Access Analyzer Kms Constraints Map Example
  slug: iam-access-analyzer-kms-constraints-map-example
- key_count: 5
  name: Iam Access Analyzer Kms Grant Configuration Example
  slug: iam-access-analyzer-kms-grant-configuration-example
- key_count: 2
  name: Iam Access Analyzer Kms Grant Constraints Example
  slug: iam-access-analyzer-kms-grant-constraints-example
- key_count: 2
  name: Iam Access Analyzer Kms Key Configuration Example
  slug: iam-access-analyzer-kms-key-configuration-example
- key_count: 0
  name: Iam Access Analyzer Kms Key Policies Map Example
  slug: iam-access-analyzer-kms-key-policies-map-example
- key_count: 4
  name: Iam Access Analyzer List Access Preview Findings Request Example
  slug: iam-access-analyzer-list-access-preview-findings-request-example
- key_count: 2
  name: Iam Access Analyzer List Access Preview Findings Response Example
  slug: iam-access-analyzer-list-access-preview-findings-response-example
- key_count: 0
  name: Iam Access Analyzer List Access Previews Request Example
  slug: iam-access-analyzer-list-access-previews-request-example
- key_count: 2
  name: Iam Access Analyzer List Access Previews Response Example
  slug: iam-access-analyzer-list-access-previews-response-example
- key_count: 4
  name: Iam Access Analyzer List Analyzed Resources Request Example
  slug: iam-access-analyzer-list-analyzed-resources-request-example
- key_count: 2
  name: Iam Access Analyzer List Analyzed Resources Response Example
  slug: iam-access-analyzer-list-analyzed-resources-response-example
- key_count: 0
  name: Iam Access Analyzer List Analyzers Request Example
  slug: iam-access-analyzer-list-analyzers-request-example
- key_count: 2
  name: Iam Access Analyzer List Analyzers Response Example
  slug: iam-access-analyzer-list-analyzers-response-example
- key_count: 0
  name: Iam Access Analyzer List Archive Rules Request Example
  slug: iam-access-analyzer-list-archive-rules-request-example
- key_count: 2
  name: Iam Access Analyzer List Archive Rules Response Example
  slug: iam-access-analyzer-list-archive-rules-response-example
- key_count: 5
  name: Iam Access Analyzer List Findings Request Example
  slug: iam-access-analyzer-list-findings-request-example
- key_count: 2
  name: Iam Access Analyzer List Findings Response Example
  slug: iam-access-analyzer-list-findings-response-example
- key_count: 0
  name: Iam Access Analyzer List Policy Generations Request Example
  slug: iam-access-analyzer-list-policy-generations-request-example
- key_count: 2
  name: Iam Access Analyzer List Policy Generations Response Example
  slug: iam-access-analyzer-list-policy-generations-response-example
- key_count: 0
  name: Iam Access Analyzer List Tags For Resource Request Example
  slug: iam-access-analyzer-list-tags-for-resource-request-example
- key_count: 1
  name: Iam Access Analyzer List Tags For Resource Response Example
  slug: iam-access-analyzer-list-tags-for-resource-response-example
- key_count: 2
  name: Iam Access Analyzer Location Example
  slug: iam-access-analyzer-location-example
- key_count: 2
  name: Iam Access Analyzer Network Origin Configuration Example
  slug: iam-access-analyzer-network-origin-configuration-example
- key_count: 4
  name: Iam Access Analyzer Path Element Example
  slug: iam-access-analyzer-path-element-example
- key_count: 1
  name: Iam Access Analyzer Policy Generation Details Example
  slug: iam-access-analyzer-policy-generation-details-example
- key_count: 5
  name: Iam Access Analyzer Policy Generation Example
  slug: iam-access-analyzer-policy-generation-example
- key_count: 3
  name: Iam Access Analyzer Position Example
  slug: iam-access-analyzer-position-example
- key_count: 0
  name: Iam Access Analyzer Principal Map Example
  slug: iam-access-analyzer-principal-map-example
- key_count: 1
  name: Iam Access Analyzer Rds Db Cluster Snapshot Attribute Value Example
  slug: iam-access-analyzer-rds-db-cluster-snapshot-attribute-value-example
- key_count: 0
  name: Iam Access Analyzer Rds Db Cluster Snapshot Attributes Map Example
  slug: iam-access-analyzer-rds-db-cluster-snapshot-attributes-map-example
- key_count: 2
  name: Iam Access Analyzer Rds Db Cluster Snapshot Configuration Example
  slug: iam-access-analyzer-rds-db-cluster-snapshot-configuration-example
- key_count: 1
  name: Iam Access Analyzer Rds Db Snapshot Attribute Value Example
  slug: iam-access-analyzer-rds-db-snapshot-attribute-value-example
- key_count: 0
  name: Iam Access Analyzer Rds Db Snapshot Attributes Map Example
  slug: iam-access-analyzer-rds-db-snapshot-attributes-map-example
- key_count: 2
  name: Iam Access Analyzer Rds Db Snapshot Configuration Example
  slug: iam-access-analyzer-rds-db-snapshot-configuration-example
- key_count: 3
  name: Iam Access Analyzer S3 Access Point Configuration Example
  slug: iam-access-analyzer-s3-access-point-configuration-example
- key_count: 0
  name: Iam Access Analyzer S3 Access Point Configurations Map Example
  slug: iam-access-analyzer-s3-access-point-configurations-map-example
- key_count: 2
  name: Iam Access Analyzer S3 Bucket Acl Grant Configuration Example
  slug: iam-access-analyzer-s3-bucket-acl-grant-configuration-example
- key_count: 4
  name: Iam Access Analyzer S3 Bucket Configuration Example
  slug: iam-access-analyzer-s3-bucket-configuration-example
- key_count: 2
  name: Iam Access Analyzer S3 Public Access Block Configuration Example
  slug: iam-access-analyzer-s3-public-access-block-configuration-example
- key_count: 2
  name: Iam Access Analyzer Secrets Manager Secret Configuration Example
  slug: iam-access-analyzer-secrets-manager-secret-configuration-example
- key_count: 1
  name: Iam Access Analyzer Sns Topic Configuration Example
  slug: iam-access-analyzer-sns-topic-configuration-example
- key_count: 2
  name: Iam Access Analyzer Sort Criteria Example
  slug: iam-access-analyzer-sort-criteria-example
- key_count: 2
  name: Iam Access Analyzer Span Example
  slug: iam-access-analyzer-span-example
- key_count: 1
  name: Iam Access Analyzer Sqs Queue Configuration Example
  slug: iam-access-analyzer-sqs-queue-configuration-example
- key_count: 3
  name: Iam Access Analyzer Start Policy Generation Request Example
  slug: iam-access-analyzer-start-policy-generation-request-example
- key_count: 1
  name: Iam Access Analyzer Start Policy Generation Response Example
  slug: iam-access-analyzer-start-policy-generation-response-example
- key_count: 3
  name: Iam Access Analyzer Start Resource Scan Request Example
  slug: iam-access-analyzer-start-resource-scan-request-example
- key_count: 1
  name: Iam Access Analyzer Status Reason Example
  slug: iam-access-analyzer-status-reason-example
- key_count: 2
  name: Iam Access Analyzer Substring Example
  slug: iam-access-analyzer-substring-example
- key_count: 1
  name: Iam Access Analyzer Tag Resource Request Example
  slug: iam-access-analyzer-tag-resource-request-example
- key_count: 0
  name: Iam Access Analyzer Tag Resource Response Example
  slug: iam-access-analyzer-tag-resource-response-example
- key_count: 0
  name: Iam Access Analyzer Tags Map Example
  slug: iam-access-analyzer-tags-map-example
- key_count: 3
  name: Iam Access Analyzer Trail Example
  slug: iam-access-analyzer-trail-example
- key_count: 3
  name: Iam Access Analyzer Trail Properties Example
  slug: iam-access-analyzer-trail-properties-example
- key_count: 0
  name: Iam Access Analyzer Untag Resource Request Example
  slug: iam-access-analyzer-untag-resource-request-example
- key_count: 0
  name: Iam Access Analyzer Untag Resource Response Example
  slug: iam-access-analyzer-untag-resource-response-example
- key_count: 2
  name: Iam Access Analyzer Update Archive Rule Request Example
  slug: iam-access-analyzer-update-archive-rule-request-example
- key_count: 5
  name: Iam Access Analyzer Update Findings Request Example
  slug: iam-access-analyzer-update-findings-request-example
- key_count: 5
  name: Iam Access Analyzer Validate Policy Finding Example
  slug: iam-access-analyzer-validate-policy-finding-example
- key_count: 4
  name: Iam Access Analyzer Validate Policy Request Example
  slug: iam-access-analyzer-validate-policy-request-example
- key_count: 2
  name: Iam Access Analyzer Validate Policy Response Example
  slug: iam-access-analyzer-validate-policy-response-example
- key_count: 1
  name: Iam Access Analyzer Vpc Configuration Example
  slug: iam-access-analyzer-vpc-configuration-example
features:
- description: Identifies resources shared with external entities outside your AWS organization using automated reasoning.
  name: External Access Analysis
- description: Identifies which principals within your organization have access to selected resources.
  name: Internal Access Analysis
- description: Identifies unused IAM roles, access keys, console passwords, and unused service permissions.
  name: Unused Access Analysis
- description: Validates IAM policies against best practices and custom security standards before deployment.
  name: Policy Validation
- description: Generates fine-grained IAM policies based on actual access activity logged in AWS CloudTrail.
  name: Policy Generation
- description: Preview public and cross-account access to resources before deploying permission changes.
  name: Access Preview
- description: Automatically archive findings that match specified criteria to reduce noise.
  name: Archive Rules
finops:
- name: Amazon Iam Access Analyzer Finops
  service_category: API
  slug: amazon-iam-access-analyzer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-iam-access-analyzer.png
json_schemas:
- name: AccessPreviewFinding
  property_count: 15
  slug: iam-access-analyzer-access-preview-finding
- name: AccessPreviewFindingsList
  property_count: 0
  slug: iam-access-analyzer-access-preview-findings-list
- name: AccessPreview
  property_count: 6
  slug: iam-access-analyzer-access-preview
- name: AccessPreviewStatusReasonCode
  property_count: 0
  slug: iam-access-analyzer-access-preview-status-reason-code
- name: AccessPreviewStatusReason
  property_count: 1
  slug: iam-access-analyzer-access-preview-status-reason
- name: AccessPreviewStatus
  property_count: 0
  slug: iam-access-analyzer-access-preview-status
- name: AccessPreviewSummary
  property_count: 5
  slug: iam-access-analyzer-access-preview-summary
- name: AccessPreviewsList
  property_count: 0
  slug: iam-access-analyzer-access-previews-list
- name: AclGrantee
  property_count: 2
  slug: iam-access-analyzer-acl-grantee
- name: AclPermission
  property_count: 0
  slug: iam-access-analyzer-acl-permission
- name: ActionList
  property_count: 0
  slug: iam-access-analyzer-action-list
- name: AnalyzedResource
  property_count: 11
  slug: iam-access-analyzer-analyzed-resource
- name: AnalyzedResourceSummary
  property_count: 3
  slug: iam-access-analyzer-analyzed-resource-summary
- name: AnalyzedResourcesList
  property_count: 0
  slug: iam-access-analyzer-analyzed-resources-list
- name: AnalyzerStatus
  property_count: 0
  slug: iam-access-analyzer-analyzer-status
- name: AnalyzerSummary
  property_count: 9
  slug: iam-access-analyzer-analyzer-summary
- name: AnalyzersList
  property_count: 0
  slug: iam-access-analyzer-analyzers-list
- name: ApplyArchiveRuleRequest
  property_count: 3
  slug: iam-access-analyzer-apply-archive-rule-request
- name: ArchiveRuleSummary
  property_count: 4
  slug: iam-access-analyzer-archive-rule-summary
- name: ArchiveRulesList
  property_count: 0
  slug: iam-access-analyzer-archive-rules-list
- name: CancelPolicyGenerationRequest
  property_count: 0
  slug: iam-access-analyzer-cancel-policy-generation-request
- name: CancelPolicyGenerationResponse
  property_count: 0
  slug: iam-access-analyzer-cancel-policy-generation-response
- name: CloudTrailDetails
  property_count: 4
  slug: iam-access-analyzer-cloud-trail-details
- name: CloudTrailProperties
  property_count: 3
  slug: iam-access-analyzer-cloud-trail-properties
- name: ConditionKeyMap
  property_count: 0
  slug: iam-access-analyzer-condition-key-map
- name: Configuration
  property_count: 11
  slug: iam-access-analyzer-configuration
- name: ConfigurationsMap
  property_count: 0
  slug: iam-access-analyzer-configurations-map
- name: CreateAccessPreviewRequest
  property_count: 3
  slug: iam-access-analyzer-create-access-preview-request
- name: CreateAccessPreviewResponse
  property_count: 1
  slug: iam-access-analyzer-create-access-preview-response
- name: CreateAnalyzerRequest
  property_count: 5
  slug: iam-access-analyzer-create-analyzer-request
- name: CreateAnalyzerResponse
  property_count: 1
  slug: iam-access-analyzer-create-analyzer-response
- name: CreateArchiveRuleRequest
  property_count: 3
  slug: iam-access-analyzer-create-archive-rule-request
- name: Criterion
  property_count: 4
  slug: iam-access-analyzer-criterion
- name: DeleteAnalyzerRequest
  property_count: 0
  slug: iam-access-analyzer-delete-analyzer-request
- name: DeleteArchiveRuleRequest
  property_count: 0
  slug: iam-access-analyzer-delete-archive-rule-request
- name: EbsGroupList
  property_count: 0
  slug: iam-access-analyzer-ebs-group-list
- name: EbsSnapshotConfiguration
  property_count: 3
  slug: iam-access-analyzer-ebs-snapshot-configuration
- name: EbsUserIdList
  property_count: 0
  slug: iam-access-analyzer-ebs-user-id-list
- name: EcrRepositoryConfiguration
  property_count: 1
  slug: iam-access-analyzer-ecr-repository-configuration
- name: EfsFileSystemConfiguration
  property_count: 1
  slug: iam-access-analyzer-efs-file-system-configuration
- name: FilterCriteriaMap
  property_count: 0
  slug: iam-access-analyzer-filter-criteria-map
- name: FindingChangeType
  property_count: 0
  slug: iam-access-analyzer-finding-change-type
- name: FindingIdList
  property_count: 0
  slug: iam-access-analyzer-finding-id-list
- name: Finding
  property_count: 14
  slug: iam-access-analyzer-finding
- name: FindingSourceDetail
  property_count: 2
  slug: iam-access-analyzer-finding-source-detail
- name: FindingSourceList
  property_count: 0
  slug: iam-access-analyzer-finding-source-list
- name: FindingSource
  property_count: 2
  slug: iam-access-analyzer-finding-source
- name: FindingSourceType
  property_count: 0
  slug: iam-access-analyzer-finding-source-type
- name: FindingStatus
  property_count: 0
  slug: iam-access-analyzer-finding-status
- name: FindingStatusUpdate
  property_count: 0
  slug: iam-access-analyzer-finding-status-update
- name: FindingSummary
  property_count: 14
  slug: iam-access-analyzer-finding-summary
- name: FindingsList
  property_count: 0
  slug: iam-access-analyzer-findings-list
- name: GeneratedPolicyList
  property_count: 0
  slug: iam-access-analyzer-generated-policy-list
- name: GeneratedPolicyProperties
  property_count: 3
  slug: iam-access-analyzer-generated-policy-properties
- name: GeneratedPolicyResult
  property_count: 2
  slug: iam-access-analyzer-generated-policy-result
- name: GeneratedPolicy
  property_count: 1
  slug: iam-access-analyzer-generated-policy
- name: GetAccessPreviewRequest
  property_count: 0
  slug: iam-access-analyzer-get-access-preview-request
- name: GetAccessPreviewResponse
  property_count: 1
  slug: iam-access-analyzer-get-access-preview-response
- name: GetAnalyzedResourceRequest
  property_count: 0
  slug: iam-access-analyzer-get-analyzed-resource-request
- name: GetAnalyzedResourceResponse
  property_count: 1
  slug: iam-access-analyzer-get-analyzed-resource-response
- name: GetAnalyzerRequest
  property_count: 0
  slug: iam-access-analyzer-get-analyzer-request
- name: GetAnalyzerResponse
  property_count: 1
  slug: iam-access-analyzer-get-analyzer-response
- name: GetArchiveRuleRequest
  property_count: 0
  slug: iam-access-analyzer-get-archive-rule-request
- name: GetArchiveRuleResponse
  property_count: 1
  slug: iam-access-analyzer-get-archive-rule-response
- name: GetFindingRequest
  property_count: 0
  slug: iam-access-analyzer-get-finding-request
- name: GetFindingResponse
  property_count: 1
  slug: iam-access-analyzer-get-finding-response
- name: GetGeneratedPolicyRequest
  property_count: 0
  slug: iam-access-analyzer-get-generated-policy-request
- name: GetGeneratedPolicyResponse
  property_count: 2
  slug: iam-access-analyzer-get-generated-policy-response
- name: IamRoleConfiguration
  property_count: 1
  slug: iam-access-analyzer-iam-role-configuration
- name: InlineArchiveRule
  property_count: 2
  slug: iam-access-analyzer-inline-archive-rule
- name: InlineArchiveRulesList
  property_count: 0
  slug: iam-access-analyzer-inline-archive-rules-list
- name: InternetConfiguration
  property_count: 0
  slug: iam-access-analyzer-internet-configuration
- name: JobDetails
  property_count: 5
  slug: iam-access-analyzer-job-details
- name: JobErrorCode
  property_count: 0
  slug: iam-access-analyzer-job-error-code
- name: JobError
  property_count: 2
  slug: iam-access-analyzer-job-error
- name: JobStatus
  property_count: 0
  slug: iam-access-analyzer-job-status
- name: KmsConstraintsMap
  property_count: 0
  slug: iam-access-analyzer-kms-constraints-map
- name: KmsGrantConfiguration
  property_count: 5
  slug: iam-access-analyzer-kms-grant-configuration
- name: KmsGrantConfigurationsList
  property_count: 0
  slug: iam-access-analyzer-kms-grant-configurations-list
- name: KmsGrantConstraints
  property_count: 2
  slug: iam-access-analyzer-kms-grant-constraints
- name: KmsGrantOperation
  property_count: 0
  slug: iam-access-analyzer-kms-grant-operation
- name: KmsGrantOperationsList
  property_count: 0
  slug: iam-access-analyzer-kms-grant-operations-list
- name: KmsKeyConfiguration
  property_count: 2
  slug: iam-access-analyzer-kms-key-configuration
- name: KmsKeyPoliciesMap
  property_count: 0
  slug: iam-access-analyzer-kms-key-policies-map
- name: ListAccessPreviewFindingsRequest
  property_count: 4
  slug: iam-access-analyzer-list-access-preview-findings-request
- name: ListAccessPreviewFindingsResponse
  property_count: 2
  slug: iam-access-analyzer-list-access-preview-findings-response
- name: ListAccessPreviewsRequest
  property_count: 0
  slug: iam-access-analyzer-list-access-previews-request
- name: ListAccessPreviewsResponse
  property_count: 2
  slug: iam-access-analyzer-list-access-previews-response
- name: ListAnalyzedResourcesRequest
  property_count: 4
  slug: iam-access-analyzer-list-analyzed-resources-request
- name: ListAnalyzedResourcesResponse
  property_count: 2
  slug: iam-access-analyzer-list-analyzed-resources-response
- name: ListAnalyzersRequest
  property_count: 0
  slug: iam-access-analyzer-list-analyzers-request
- name: ListAnalyzersResponse
  property_count: 2
  slug: iam-access-analyzer-list-analyzers-response
- name: ListArchiveRulesRequest
  property_count: 0
  slug: iam-access-analyzer-list-archive-rules-request
- name: ListArchiveRulesResponse
  property_count: 2
  slug: iam-access-analyzer-list-archive-rules-response
- name: ListFindingsRequest
  property_count: 5
  slug: iam-access-analyzer-list-findings-request
- name: ListFindingsResponse
  property_count: 2
  slug: iam-access-analyzer-list-findings-response
- name: ListPolicyGenerationsRequest
  property_count: 0
  slug: iam-access-analyzer-list-policy-generations-request
- name: ListPolicyGenerationsResponse
  property_count: 2
  slug: iam-access-analyzer-list-policy-generations-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: iam-access-analyzer-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: iam-access-analyzer-list-tags-for-resource-response
- name: Locale
  property_count: 0
  slug: iam-access-analyzer-locale
- name: LocationList
  property_count: 0
  slug: iam-access-analyzer-location-list
- name: Location
  property_count: 2
  slug: iam-access-analyzer-location
- name: NetworkOriginConfiguration
  property_count: 2
  slug: iam-access-analyzer-network-origin-configuration
- name: OrderBy
  property_count: 0
  slug: iam-access-analyzer-order-by
- name: PathElementList
  property_count: 0
  slug: iam-access-analyzer-path-element-list
- name: PathElement
  property_count: 4
  slug: iam-access-analyzer-path-element
- name: PolicyGenerationDetails
  property_count: 1
  slug: iam-access-analyzer-policy-generation-details
- name: PolicyGenerationList
  property_count: 0
  slug: iam-access-analyzer-policy-generation-list
- name: PolicyGeneration
  property_count: 5
  slug: iam-access-analyzer-policy-generation
- name: PolicyType
  property_count: 0
  slug: iam-access-analyzer-policy-type
- name: Position
  property_count: 3
  slug: iam-access-analyzer-position
- name: PrincipalMap
  property_count: 0
  slug: iam-access-analyzer-principal-map
- name: RdsDbClusterSnapshotAccountIdsList
  property_count: 0
  slug: iam-access-analyzer-rds-db-cluster-snapshot-account-ids-list
- name: RdsDbClusterSnapshotAttributeValue
  property_count: 1
  slug: iam-access-analyzer-rds-db-cluster-snapshot-attribute-value
- name: RdsDbClusterSnapshotAttributesMap
  property_count: 0
  slug: iam-access-analyzer-rds-db-cluster-snapshot-attributes-map
- name: RdsDbClusterSnapshotConfiguration
  property_count: 2
  slug: iam-access-analyzer-rds-db-cluster-snapshot-configuration
- name: RdsDbSnapshotAccountIdsList
  property_count: 0
  slug: iam-access-analyzer-rds-db-snapshot-account-ids-list
- name: RdsDbSnapshotAttributeValue
  property_count: 1
  slug: iam-access-analyzer-rds-db-snapshot-attribute-value
- name: RdsDbSnapshotAttributesMap
  property_count: 0
  slug: iam-access-analyzer-rds-db-snapshot-attributes-map
- name: RdsDbSnapshotConfiguration
  property_count: 2
  slug: iam-access-analyzer-rds-db-snapshot-configuration
- name: ReasonCode
  property_count: 0
  slug: iam-access-analyzer-reason-code
- name: RegionList
  property_count: 0
  slug: iam-access-analyzer-region-list
- name: ResourceType
  property_count: 0
  slug: iam-access-analyzer-resource-type
- name: S3AccessPointConfiguration
  property_count: 3
  slug: iam-access-analyzer-s3-access-point-configuration
- name: S3AccessPointConfigurationsMap
  property_count: 0
  slug: iam-access-analyzer-s3-access-point-configurations-map
- name: S3BucketAclGrantConfiguration
  property_count: 2
  slug: iam-access-analyzer-s3-bucket-acl-grant-configuration
- name: S3BucketAclGrantConfigurationsList
  property_count: 0
  slug: iam-access-analyzer-s3-bucket-acl-grant-configurations-list
- name: S3BucketConfiguration
  property_count: 4
  slug: iam-access-analyzer-s3-bucket-configuration
- name: S3PublicAccessBlockConfiguration
  property_count: 2
  slug: iam-access-analyzer-s3-public-access-block-configuration
- name: SecretsManagerSecretConfiguration
  property_count: 2
  slug: iam-access-analyzer-secrets-manager-secret-configuration
- name: SharedViaList
  property_count: 0
  slug: iam-access-analyzer-shared-via-list
- name: SnsTopicConfiguration
  property_count: 1
  slug: iam-access-analyzer-sns-topic-configuration
- name: SortCriteria
  property_count: 2
  slug: iam-access-analyzer-sort-criteria
- name: Span
  property_count: 2
  slug: iam-access-analyzer-span
- name: SqsQueueConfiguration
  property_count: 1
  slug: iam-access-analyzer-sqs-queue-configuration
- name: StartPolicyGenerationRequest
  property_count: 3
  slug: iam-access-analyzer-start-policy-generation-request
- name: StartPolicyGenerationResponse
  property_count: 1
  slug: iam-access-analyzer-start-policy-generation-response
- name: StartResourceScanRequest
  property_count: 3
  slug: iam-access-analyzer-start-resource-scan-request
- name: StatusReason
  property_count: 1
  slug: iam-access-analyzer-status-reason
- name: Substring
  property_count: 2
  slug: iam-access-analyzer-substring
- name: TagKeys
  property_count: 0
  slug: iam-access-analyzer-tag-keys
- name: TagResourceRequest
  property_count: 1
  slug: iam-access-analyzer-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: iam-access-analyzer-tag-resource-response
- name: TagsMap
  property_count: 0
  slug: iam-access-analyzer-tags-map
- name: TrailList
  property_count: 0
  slug: iam-access-analyzer-trail-list
- name: TrailPropertiesList
  property_count: 0
  slug: iam-access-analyzer-trail-properties-list
- name: TrailProperties
  property_count: 3
  slug: iam-access-analyzer-trail-properties
- name: Trail
  property_count: 3
  slug: iam-access-analyzer-trail
- name: Type
  property_count: 0
  slug: iam-access-analyzer-type
- name: UntagResourceRequest
  property_count: 0
  slug: iam-access-analyzer-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: iam-access-analyzer-untag-resource-response
- name: UpdateArchiveRuleRequest
  property_count: 2
  slug: iam-access-analyzer-update-archive-rule-request
- name: UpdateFindingsRequest
  property_count: 5
  slug: iam-access-analyzer-update-findings-request
- name: ValidatePolicyFindingList
  property_count: 0
  slug: iam-access-analyzer-validate-policy-finding-list
- name: ValidatePolicyFinding
  property_count: 5
  slug: iam-access-analyzer-validate-policy-finding
- name: ValidatePolicyFindingType
  property_count: 0
  slug: iam-access-analyzer-validate-policy-finding-type
- name: ValidatePolicyRequest
  property_count: 4
  slug: iam-access-analyzer-validate-policy-request
- name: ValidatePolicyResourceType
  property_count: 0
  slug: iam-access-analyzer-validate-policy-resource-type
- name: ValidatePolicyResponse
  property_count: 2
  slug: iam-access-analyzer-validate-policy-response
- name: ValueList
  property_count: 0
  slug: iam-access-analyzer-value-list
- name: VpcConfiguration
  property_count: 1
  slug: iam-access-analyzer-vpc-configuration
json_structures:
- name: Iam Access Analyzer Access Preview Finding Structure
  property_count: 15
  slug: iam-access-analyzer-access-preview-finding-structure
- name: Iam Access Analyzer Access Preview Findings List Structure
  property_count: 0
  slug: iam-access-analyzer-access-preview-findings-list-structure
- name: Iam Access Analyzer Access Preview Status Reason Code Structure
  property_count: 0
  slug: iam-access-analyzer-access-preview-status-reason-code-structure
- name: Iam Access Analyzer Access Preview Status Reason Structure
  property_count: 1
  slug: iam-access-analyzer-access-preview-status-reason-structure
- name: Iam Access Analyzer Access Preview Status Structure
  property_count: 0
  slug: iam-access-analyzer-access-preview-status-structure
- name: Iam Access Analyzer Access Preview Structure
  property_count: 6
  slug: iam-access-analyzer-access-preview-structure
- name: Iam Access Analyzer Access Preview Summary Structure
  property_count: 5
  slug: iam-access-analyzer-access-preview-summary-structure
- name: Iam Access Analyzer Access Previews List Structure
  property_count: 0
  slug: iam-access-analyzer-access-previews-list-structure
- name: Iam Access Analyzer Acl Grantee Structure
  property_count: 2
  slug: iam-access-analyzer-acl-grantee-structure
- name: Iam Access Analyzer Acl Permission Structure
  property_count: 0
  slug: iam-access-analyzer-acl-permission-structure
- name: Iam Access Analyzer Action List Structure
  property_count: 0
  slug: iam-access-analyzer-action-list-structure
- name: Iam Access Analyzer Analyzed Resource Structure
  property_count: 11
  slug: iam-access-analyzer-analyzed-resource-structure
- name: Iam Access Analyzer Analyzed Resource Summary Structure
  property_count: 3
  slug: iam-access-analyzer-analyzed-resource-summary-structure
- name: Iam Access Analyzer Analyzed Resources List Structure
  property_count: 0
  slug: iam-access-analyzer-analyzed-resources-list-structure
- name: Iam Access Analyzer Analyzer Status Structure
  property_count: 0
  slug: iam-access-analyzer-analyzer-status-structure
- name: Iam Access Analyzer Analyzer Summary Structure
  property_count: 9
  slug: iam-access-analyzer-analyzer-summary-structure
- name: Iam Access Analyzer Analyzers List Structure
  property_count: 0
  slug: iam-access-analyzer-analyzers-list-structure
- name: Iam Access Analyzer Apply Archive Rule Request Structure
  property_count: 3
  slug: iam-access-analyzer-apply-archive-rule-request-structure
- name: Iam Access Analyzer Archive Rule Summary Structure
  property_count: 4
  slug: iam-access-analyzer-archive-rule-summary-structure
- name: Iam Access Analyzer Archive Rules List Structure
  property_count: 0
  slug: iam-access-analyzer-archive-rules-list-structure
- name: Iam Access Analyzer Cancel Policy Generation Request Structure
  property_count: 0
  slug: iam-access-analyzer-cancel-policy-generation-request-structure
- name: Iam Access Analyzer Cancel Policy Generation Response Structure
  property_count: 0
  slug: iam-access-analyzer-cancel-policy-generation-response-structure
- name: Iam Access Analyzer Cloud Trail Details Structure
  property_count: 4
  slug: iam-access-analyzer-cloud-trail-details-structure
- name: Iam Access Analyzer Cloud Trail Properties Structure
  property_count: 3
  slug: iam-access-analyzer-cloud-trail-properties-structure
- name: Iam Access Analyzer Condition Key Map Structure
  property_count: 0
  slug: iam-access-analyzer-condition-key-map-structure
- name: Iam Access Analyzer Configuration Structure
  property_count: 11
  slug: iam-access-analyzer-configuration-structure
- name: Iam Access Analyzer Configurations Map Structure
  property_count: 0
  slug: iam-access-analyzer-configurations-map-structure
- name: Iam Access Analyzer Create Access Preview Request Structure
  property_count: 3
  slug: iam-access-analyzer-create-access-preview-request-structure
- name: Iam Access Analyzer Create Access Preview Response Structure
  property_count: 1
  slug: iam-access-analyzer-create-access-preview-response-structure
- name: Iam Access Analyzer Create Analyzer Request Structure
  property_count: 5
  slug: iam-access-analyzer-create-analyzer-request-structure
- name: Iam Access Analyzer Create Analyzer Response Structure
  property_count: 1
  slug: iam-access-analyzer-create-analyzer-response-structure
- name: Iam Access Analyzer Create Archive Rule Request Structure
  property_count: 3
  slug: iam-access-analyzer-create-archive-rule-request-structure
- name: Iam Access Analyzer Criterion Structure
  property_count: 4
  slug: iam-access-analyzer-criterion-structure
- name: Iam Access Analyzer Delete Analyzer Request Structure
  property_count: 0
  slug: iam-access-analyzer-delete-analyzer-request-structure
- name: Iam Access Analyzer Delete Archive Rule Request Structure
  property_count: 0
  slug: iam-access-analyzer-delete-archive-rule-request-structure
- name: Iam Access Analyzer Ebs Group List Structure
  property_count: 0
  slug: iam-access-analyzer-ebs-group-list-structure
- name: Iam Access Analyzer Ebs Snapshot Configuration Structure
  property_count: 3
  slug: iam-access-analyzer-ebs-snapshot-configuration-structure
- name: Iam Access Analyzer Ebs User Id List Structure
  property_count: 0
  slug: iam-access-analyzer-ebs-user-id-list-structure
- name: Iam Access Analyzer Ecr Repository Configuration Structure
  property_count: 1
  slug: iam-access-analyzer-ecr-repository-configuration-structure
- name: Iam Access Analyzer Efs File System Configuration Structure
  property_count: 1
  slug: iam-access-analyzer-efs-file-system-configuration-structure
- name: Iam Access Analyzer Filter Criteria Map Structure
  property_count: 0
  slug: iam-access-analyzer-filter-criteria-map-structure
- name: Iam Access Analyzer Finding Change Type Structure
  property_count: 0
  slug: iam-access-analyzer-finding-change-type-structure
- name: Iam Access Analyzer Finding Id List Structure
  property_count: 0
  slug: iam-access-analyzer-finding-id-list-structure
- name: Iam Access Analyzer Finding Source Detail Structure
  property_count: 2
  slug: iam-access-analyzer-finding-source-detail-structure
- name: Iam Access Analyzer Finding Source List Structure
  property_count: 0
  slug: iam-access-analyzer-finding-source-list-structure
- name: Iam Access Analyzer Finding Source Structure
  property_count: 2
  slug: iam-access-analyzer-finding-source-structure
- name: Iam Access Analyzer Finding Source Type Structure
  property_count: 0
  slug: iam-access-analyzer-finding-source-type-structure
- name: Iam Access Analyzer Finding Status Structure
  property_count: 0
  slug: iam-access-analyzer-finding-status-structure
- name: Iam Access Analyzer Finding Status Update Structure
  property_count: 0
  slug: iam-access-analyzer-finding-status-update-structure
- name: Iam Access Analyzer Finding Structure
  property_count: 14
  slug: iam-access-analyzer-finding-structure
- name: Iam Access Analyzer Finding Summary Structure
  property_count: 14
  slug: iam-access-analyzer-finding-summary-structure
- name: Iam Access Analyzer Findings List Structure
  property_count: 0
  slug: iam-access-analyzer-findings-list-structure
- name: Iam Access Analyzer Generated Policy List Structure
  property_count: 0
  slug: iam-access-analyzer-generated-policy-list-structure
- name: Iam Access Analyzer Generated Policy Properties Structure
  property_count: 3
  slug: iam-access-analyzer-generated-policy-properties-structure
- name: Iam Access Analyzer Generated Policy Result Structure
  property_count: 2
  slug: iam-access-analyzer-generated-policy-result-structure
- name: Iam Access Analyzer Generated Policy Structure
  property_count: 1
  slug: iam-access-analyzer-generated-policy-structure
- name: Iam Access Analyzer Get Access Preview Request Structure
  property_count: 0
  slug: iam-access-analyzer-get-access-preview-request-structure
- name: Iam Access Analyzer Get Access Preview Response Structure
  property_count: 1
  slug: iam-access-analyzer-get-access-preview-response-structure
- name: Iam Access Analyzer Get Analyzed Resource Request Structure
  property_count: 0
  slug: iam-access-analyzer-get-analyzed-resource-request-structure
- name: Iam Access Analyzer Get Analyzed Resource Response Structure
  property_count: 1
  slug: iam-access-analyzer-get-analyzed-resource-response-structure
- name: Iam Access Analyzer Get Analyzer Request Structure
  property_count: 0
  slug: iam-access-analyzer-get-analyzer-request-structure
- name: Iam Access Analyzer Get Analyzer Response Structure
  property_count: 1
  slug: iam-access-analyzer-get-analyzer-response-structure
- name: Iam Access Analyzer Get Archive Rule Request Structure
  property_count: 0
  slug: iam-access-analyzer-get-archive-rule-request-structure
- name: Iam Access Analyzer Get Archive Rule Response Structure
  property_count: 1
  slug: iam-access-analyzer-get-archive-rule-response-structure
- name: Iam Access Analyzer Get Finding Request Structure
  property_count: 0
  slug: iam-access-analyzer-get-finding-request-structure
- name: Iam Access Analyzer Get Finding Response Structure
  property_count: 1
  slug: iam-access-analyzer-get-finding-response-structure
- name: Iam Access Analyzer Get Generated Policy Request Structure
  property_count: 0
  slug: iam-access-analyzer-get-generated-policy-request-structure
- name: Iam Access Analyzer Get Generated Policy Response Structure
  property_count: 2
  slug: iam-access-analyzer-get-generated-policy-response-structure
- name: Iam Access Analyzer Iam Role Configuration Structure
  property_count: 1
  slug: iam-access-analyzer-iam-role-configuration-structure
- name: Iam Access Analyzer Inline Archive Rule Structure
  property_count: 2
  slug: iam-access-analyzer-inline-archive-rule-structure
- name: Iam Access Analyzer Inline Archive Rules List Structure
  property_count: 0
  slug: iam-access-analyzer-inline-archive-rules-list-structure
- name: Iam Access Analyzer Internet Configuration Structure
  property_count: 0
  slug: iam-access-analyzer-internet-configuration-structure
- name: Iam Access Analyzer Job Details Structure
  property_count: 5
  slug: iam-access-analyzer-job-details-structure
- name: Iam Access Analyzer Job Error Code Structure
  property_count: 0
  slug: iam-access-analyzer-job-error-code-structure
- name: Iam Access Analyzer Job Error Structure
  property_count: 2
  slug: iam-access-analyzer-job-error-structure
- name: Iam Access Analyzer Job Status Structure
  property_count: 0
  slug: iam-access-analyzer-job-status-structure
- name: Iam Access Analyzer Kms Constraints Map Structure
  property_count: 0
  slug: iam-access-analyzer-kms-constraints-map-structure
- name: Iam Access Analyzer Kms Grant Configuration Structure
  property_count: 5
  slug: iam-access-analyzer-kms-grant-configuration-structure
- name: Iam Access Analyzer Kms Grant Configurations List Structure
  property_count: 0
  slug: iam-access-analyzer-kms-grant-configurations-list-structure
- name: Iam Access Analyzer Kms Grant Constraints Structure
  property_count: 2
  slug: iam-access-analyzer-kms-grant-constraints-structure
- name: Iam Access Analyzer Kms Grant Operation Structure
  property_count: 0
  slug: iam-access-analyzer-kms-grant-operation-structure
- name: Iam Access Analyzer Kms Grant Operations List Structure
  property_count: 0
  slug: iam-access-analyzer-kms-grant-operations-list-structure
- name: Iam Access Analyzer Kms Key Configuration Structure
  property_count: 2
  slug: iam-access-analyzer-kms-key-configuration-structure
- name: Iam Access Analyzer Kms Key Policies Map Structure
  property_count: 0
  slug: iam-access-analyzer-kms-key-policies-map-structure
- name: Iam Access Analyzer List Access Preview Findings Request Structure
  property_count: 4
  slug: iam-access-analyzer-list-access-preview-findings-request-structure
- name: Iam Access Analyzer List Access Preview Findings Response Structure
  property_count: 2
  slug: iam-access-analyzer-list-access-preview-findings-response-structure
- name: Iam Access Analyzer List Access Previews Request Structure
  property_count: 0
  slug: iam-access-analyzer-list-access-previews-request-structure
- name: Iam Access Analyzer List Access Previews Response Structure
  property_count: 2
  slug: iam-access-analyzer-list-access-previews-response-structure
- name: Iam Access Analyzer List Analyzed Resources Request Structure
  property_count: 4
  slug: iam-access-analyzer-list-analyzed-resources-request-structure
- name: Iam Access Analyzer List Analyzed Resources Response Structure
  property_count: 2
  slug: iam-access-analyzer-list-analyzed-resources-response-structure
- name: Iam Access Analyzer List Analyzers Request Structure
  property_count: 0
  slug: iam-access-analyzer-list-analyzers-request-structure
- name: Iam Access Analyzer List Analyzers Response Structure
  property_count: 2
  slug: iam-access-analyzer-list-analyzers-response-structure
- name: Iam Access Analyzer List Archive Rules Request Structure
  property_count: 0
  slug: iam-access-analyzer-list-archive-rules-request-structure
- name: Iam Access Analyzer List Archive Rules Response Structure
  property_count: 2
  slug: iam-access-analyzer-list-archive-rules-response-structure
- name: Iam Access Analyzer List Findings Request Structure
  property_count: 5
  slug: iam-access-analyzer-list-findings-request-structure
- name: Iam Access Analyzer List Findings Response Structure
  property_count: 2
  slug: iam-access-analyzer-list-findings-response-structure
- name: Iam Access Analyzer List Policy Generations Request Structure
  property_count: 0
  slug: iam-access-analyzer-list-policy-generations-request-structure
- name: Iam Access Analyzer List Policy Generations Response Structure
  property_count: 2
  slug: iam-access-analyzer-list-policy-generations-response-structure
- name: Iam Access Analyzer List Tags For Resource Request Structure
  property_count: 0
  slug: iam-access-analyzer-list-tags-for-resource-request-structure
- name: Iam Access Analyzer List Tags For Resource Response Structure
  property_count: 1
  slug: iam-access-analyzer-list-tags-for-resource-response-structure
- name: Iam Access Analyzer Locale Structure
  property_count: 0
  slug: iam-access-analyzer-locale-structure
- name: Iam Access Analyzer Location List Structure
  property_count: 0
  slug: iam-access-analyzer-location-list-structure
- name: Iam Access Analyzer Location Structure
  property_count: 2
  slug: iam-access-analyzer-location-structure
- name: Iam Access Analyzer Network Origin Configuration Structure
  property_count: 2
  slug: iam-access-analyzer-network-origin-configuration-structure
- name: Iam Access Analyzer Order By Structure
  property_count: 0
  slug: iam-access-analyzer-order-by-structure
- name: Iam Access Analyzer Path Element List Structure
  property_count: 0
  slug: iam-access-analyzer-path-element-list-structure
- name: Iam Access Analyzer Path Element Structure
  property_count: 4
  slug: iam-access-analyzer-path-element-structure
- name: Iam Access Analyzer Policy Generation Details Structure
  property_count: 1
  slug: iam-access-analyzer-policy-generation-details-structure
- name: Iam Access Analyzer Policy Generation List Structure
  property_count: 0
  slug: iam-access-analyzer-policy-generation-list-structure
- name: Iam Access Analyzer Policy Generation Structure
  property_count: 5
  slug: iam-access-analyzer-policy-generation-structure
- name: Iam Access Analyzer Policy Type Structure
  property_count: 0
  slug: iam-access-analyzer-policy-type-structure
- name: Iam Access Analyzer Position Structure
  property_count: 3
  slug: iam-access-analyzer-position-structure
- name: Iam Access Analyzer Principal Map Structure
  property_count: 0
  slug: iam-access-analyzer-principal-map-structure
- name: Iam Access Analyzer Rds Db Cluster Snapshot Account Ids List Structure
  property_count: 0
  slug: iam-access-analyzer-rds-db-cluster-snapshot-account-ids-list-structure
- name: Iam Access Analyzer Rds Db Cluster Snapshot Attribute Value Structure
  property_count: 1
  slug: iam-access-analyzer-rds-db-cluster-snapshot-attribute-value-structure
- name: Iam Access Analyzer Rds Db Cluster Snapshot Attributes Map Structure
  property_count: 0
  slug: iam-access-analyzer-rds-db-cluster-snapshot-attributes-map-structure
- name: Iam Access Analyzer Rds Db Cluster Snapshot Configuration Structure
  property_count: 2
  slug: iam-access-analyzer-rds-db-cluster-snapshot-configuration-structure
- name: Iam Access Analyzer Rds Db Snapshot Account Ids List Structure
  property_count: 0
  slug: iam-access-analyzer-rds-db-snapshot-account-ids-list-structure
- name: Iam Access Analyzer Rds Db Snapshot Attribute Value Structure
  property_count: 1
  slug: iam-access-analyzer-rds-db-snapshot-attribute-value-structure
- name: Iam Access Analyzer Rds Db Snapshot Attributes Map Structure
  property_count: 0
  slug: iam-access-analyzer-rds-db-snapshot-attributes-map-structure
- name: Iam Access Analyzer Rds Db Snapshot Configuration Structure
  property_count: 2
  slug: iam-access-analyzer-rds-db-snapshot-configuration-structure
- name: Iam Access Analyzer Reason Code Structure
  property_count: 0
  slug: iam-access-analyzer-reason-code-structure
- name: Iam Access Analyzer Region List Structure
  property_count: 0
  slug: iam-access-analyzer-region-list-structure
- name: Iam Access Analyzer Resource Type Structure
  property_count: 0
  slug: iam-access-analyzer-resource-type-structure
- name: Iam Access Analyzer S3 Access Point Configuration Structure
  property_count: 3
  slug: iam-access-analyzer-s3-access-point-configuration-structure
- name: Iam Access Analyzer S3 Access Point Configurations Map Structure
  property_count: 0
  slug: iam-access-analyzer-s3-access-point-configurations-map-structure
- name: Iam Access Analyzer S3 Bucket Acl Grant Configuration Structure
  property_count: 2
  slug: iam-access-analyzer-s3-bucket-acl-grant-configuration-structure
- name: Iam Access Analyzer S3 Bucket Acl Grant Configurations List Structure
  property_count: 0
  slug: iam-access-analyzer-s3-bucket-acl-grant-configurations-list-structure
- name: Iam Access Analyzer S3 Bucket Configuration Structure
  property_count: 4
  slug: iam-access-analyzer-s3-bucket-configuration-structure
- name: Iam Access Analyzer S3 Public Access Block Configuration Structure
  property_count: 2
  slug: iam-access-analyzer-s3-public-access-block-configuration-structure
- name: Iam Access Analyzer Secrets Manager Secret Configuration Structure
  property_count: 2
  slug: iam-access-analyzer-secrets-manager-secret-configuration-structure
- name: Iam Access Analyzer Shared Via List Structure
  property_count: 0
  slug: iam-access-analyzer-shared-via-list-structure
- name: Iam Access Analyzer Sns Topic Configuration Structure
  property_count: 1
  slug: iam-access-analyzer-sns-topic-configuration-structure
- name: Iam Access Analyzer Sort Criteria Structure
  property_count: 2
  slug: iam-access-analyzer-sort-criteria-structure
- name: Iam Access Analyzer Span Structure
  property_count: 2
  slug: iam-access-analyzer-span-structure
- name: Iam Access Analyzer Sqs Queue Configuration Structure
  property_count: 1
  slug: iam-access-analyzer-sqs-queue-configuration-structure
- name: Iam Access Analyzer Start Policy Generation Request Structure
  property_count: 3
  slug: iam-access-analyzer-start-policy-generation-request-structure
- name: Iam Access Analyzer Start Policy Generation Response Structure
  property_count: 1
  slug: iam-access-analyzer-start-policy-generation-response-structure
- name: Iam Access Analyzer Start Resource Scan Request Structure
  property_count: 3
  slug: iam-access-analyzer-start-resource-scan-request-structure
- name: Iam Access Analyzer Status Reason Structure
  property_count: 1
  slug: iam-access-analyzer-status-reason-structure
- name: Iam Access Analyzer Substring Structure
  property_count: 2
  slug: iam-access-analyzer-substring-structure
- name: Iam Access Analyzer Tag Keys Structure
  property_count: 0
  slug: iam-access-analyzer-tag-keys-structure
- name: Iam Access Analyzer Tag Resource Request Structure
  property_count: 1
  slug: iam-access-analyzer-tag-resource-request-structure
- name: Iam Access Analyzer Tag Resource Response Structure
  property_count: 0
  slug: iam-access-analyzer-tag-resource-response-structure
- name: Iam Access Analyzer Tags Map Structure
  property_count: 0
  slug: iam-access-analyzer-tags-map-structure
- name: Iam Access Analyzer Trail List Structure
  property_count: 0
  slug: iam-access-analyzer-trail-list-structure
- name: Iam Access Analyzer Trail Properties List Structure
  property_count: 0
  slug: iam-access-analyzer-trail-properties-list-structure
- name: Iam Access Analyzer Trail Properties Structure
  property_count: 3
  slug: iam-access-analyzer-trail-properties-structure
- name: Iam Access Analyzer Trail Structure
  property_count: 3
  slug: iam-access-analyzer-trail-structure
- name: Iam Access Analyzer Type Structure
  property_count: 0
  slug: iam-access-analyzer-type-structure
- name: Iam Access Analyzer Untag Resource Request Structure
  property_count: 0
  slug: iam-access-analyzer-untag-resource-request-structure
- name: Iam Access Analyzer Untag Resource Response Structure
  property_count: 0
  slug: iam-access-analyzer-untag-resource-response-structure
- name: Iam Access Analyzer Update Archive Rule Request Structure
  property_count: 2
  slug: iam-access-analyzer-update-archive-rule-request-structure
- name: Iam Access Analyzer Update Findings Request Structure
  property_count: 5
  slug: iam-access-analyzer-update-findings-request-structure
- name: Iam Access Analyzer Validate Policy Finding List Structure
  property_count: 0
  slug: iam-access-analyzer-validate-policy-finding-list-structure
- name: Iam Access Analyzer Validate Policy Finding Structure
  property_count: 5
  slug: iam-access-analyzer-validate-policy-finding-structure
- name: Iam Access Analyzer Validate Policy Finding Type Structure
  property_count: 0
  slug: iam-access-analyzer-validate-policy-finding-type-structure
- name: Iam Access Analyzer Validate Policy Request Structure
  property_count: 4
  slug: iam-access-analyzer-validate-policy-request-structure
- name: Iam Access Analyzer Validate Policy Resource Type Structure
  property_count: 0
  slug: iam-access-analyzer-validate-policy-resource-type-structure
- name: Iam Access Analyzer Validate Policy Response Structure
  property_count: 2
  slug: iam-access-analyzer-validate-policy-response-structure
- name: Iam Access Analyzer Value List Structure
  property_count: 0
  slug: iam-access-analyzer-value-list-structure
- name: Iam Access Analyzer Vpc Configuration Structure
  property_count: 1
  slug: iam-access-analyzer-vpc-configuration-structure
jsonld:
- class_count: 116
  name: Amazon Iam Access Analyzer Context
  property_count: 146
  slug: amazon-iam-access-analyzer-context
layout: provider
modified: '2026-05-19'
name: Amazon IAM Access Analyzer
nav: Providers
network: true
overview: 'Amazon IAM Access Analyzer publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Access Preview#analyzerArn API, Access Preview API, Analyzed Resource#analyzerArn&resourceArn API, and 7 more. Tagged areas include Access Control, Compliance, IAM, Policy Management, and Security.


  The Amazon IAM Access Analyzer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon IAM Access Analyzer''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 15 more developer resources.'
plans:
- name: Amazon Iam Access Analyzer Plans Pricing
  plan_count: 3
  slug: amazon-iam-access-analyzer-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Amazon Iam Access Analyzer Rate Limits
  slug: amazon-iam-access-analyzer-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon IAM Access Analyzer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-iam-access-analyzer-jsonschema-spectral-rules
- effective_rule_count: 70
  extends:
  - spectral:oas
  name: Amazon IAM Access Analyzer API Rules
  rule_count: 29
  severity_counts:
    error: 10
    hint: 0
    info: 4
    warn: 15
  slug: amazon-iam-access-analyzer-spectral-rules
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 65.4
    developer_ergonomics: 61.9
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-iam-access-analyzer/refs/heads/main/screenshots/amazon-iam-access-analyzer-2026-06-20T171702.png
security:
- kind: authentication
  name: Amazon Iam Access Analyzer Authentication
  slug: amazon-iam-access-analyzer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Iam Access Analyzer Domain Security
  slug: amazon-iam-access-analyzer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Iam Access Analyzer Vulnerability Disclosure
  slug: amazon-iam-access-analyzer-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Iam Access Analyzer Trust Center
  slug: amazon-iam-access-analyzer-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-iam-access-analyzer
tags:
- Access Control
- Compliance
- IAM
- Policy Management
- Security
use_cases:
- description: Analyze actual API activity to generate minimal permission policies that implement least privilege access.
  name: Least Privilege Enforcement
- description: Continuously monitor for unintended external access to sensitive resources like S3 buckets and IAM roles.
  name: Security Compliance Auditing
- description: Integrate policy checks into deployment pipelines to catch overpermissive policies before they reach production.
  name: CI/CD Policy Validation
- description: Identify and remediate unused access across IAM users, roles, and service accounts organization-wide.
  name: Access Governance
- description: Identify all resources shared across AWS accounts and validate the intent of each cross-account permission.
  name: Cross-Account Access Review
website: https://aws.amazon.com/iam/
---
