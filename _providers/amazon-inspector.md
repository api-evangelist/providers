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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 51
  human_in_the_loop: 4
  name: Amazon Inspector Agentic Access
  operation_count: 53
  slug: amazon-inspector-agentic-access
  summary_line: 53 operations · 51 acting · 4 human-in-the-loop
api_count: 22
apis:
- description: The Accountpermissions API from Amazon Inspector — 1 operation(s) for accountpermissions.
  name: Amazon Inspector Accountpermissions API
  slug: amazon-inspector-accountpermissions-api
- description: The Codesnippet API from Amazon Inspector — 1 operation(s) for codesnippet.
  name: Amazon Inspector Codesnippet API
  slug: amazon-inspector-codesnippet-api
- description: The Configuration API from Amazon Inspector — 2 operation(s) for configuration.
  name: Amazon Inspector Configuration API
  slug: amazon-inspector-configuration-api
- description: The Coverage API from Amazon Inspector — 2 operation(s) for coverage.
  name: Amazon Inspector Coverage API
  slug: amazon-inspector-coverage-api
- description: The Delegatedadminaccounts API from Amazon Inspector — 4 operation(s) for delegatedadminaccounts.
  name: Amazon Inspector Delegatedadminaccounts API
  slug: amazon-inspector-delegatedadminaccounts-api
- description: The Disable API from Amazon Inspector — 1 operation(s) for disable.
  name: Amazon Inspector Disable API
  slug: amazon-inspector-disable-api
- description: The Ec2deepinspectionconfiguration API from Amazon Inspector — 3 operation(s) for ec2deepinspectionconfiguration.
  name: Amazon Inspector Ec2deepinspectionconfiguration API
  slug: amazon-inspector-ec2deepinspectionconfiguration-api
- description: The Ec2deepinspectionstatus API from Amazon Inspector — 2 operation(s) for ec2deepinspectionstatus.
  name: Amazon Inspector Ec2deepinspectionstatus API
  slug: amazon-inspector-ec2deepinspectionstatus-api
- description: The Enable API from Amazon Inspector — 1 operation(s) for enable.
  name: Amazon Inspector Enable API
  slug: amazon-inspector-enable-api
- description: The Encryptionkey API from Amazon Inspector — 3 operation(s) for encryptionkey.
  name: Amazon Inspector Encryptionkey API
  slug: amazon-inspector-encryptionkey-api
- description: The Filters API from Amazon Inspector — 4 operation(s) for filters.
  name: Amazon Inspector Filters API
  slug: amazon-inspector-filters-api
- description: The Findings API from Amazon Inspector — 4 operation(s) for findings.
  name: Amazon Inspector Findings API
  slug: amazon-inspector-findings-api
- description: The Freetrialinfo API from Amazon Inspector — 1 operation(s) for freetrialinfo.
  name: Amazon Inspector Freetrialinfo API
  slug: amazon-inspector-freetrialinfo-api
- description: The Members API from Amazon Inspector — 4 operation(s) for members.
  name: Amazon Inspector Members API
  slug: amazon-inspector-members-api
- description: The Organizationconfiguration API from Amazon Inspector — 2 operation(s) for organizationconfiguration.
  name: Amazon Inspector Organizationconfiguration API
  slug: amazon-inspector-organizationconfiguration-api
- description: The Reporting API from Amazon Inspector — 3 operation(s) for reporting.
  name: Amazon Inspector Reporting API
  slug: amazon-inspector-reporting-api
- description: The Sbomexport API from Amazon Inspector — 3 operation(s) for sbomexport.
  name: Amazon Inspector Sbomexport API
  slug: amazon-inspector-sbomexport-api
- description: Operations for enabling and managing vulnerability scanning
  name: Amazon Inspector Scanning API
  slug: amazon-inspector-scanning-api
- description: The Status API from Amazon Inspector — 1 operation(s) for status.
  name: Amazon Inspector Status API
  slug: amazon-inspector-status-api
- description: The Tags API from Amazon Inspector — 2 operation(s) for tags.
  name: Amazon Inspector Tags API
  slug: amazon-inspector-tags-api
- description: The Usage API from Amazon Inspector — 1 operation(s) for usage.
  name: Amazon Inspector Usage API
  slug: amazon-inspector-usage-api
- description: The Vulnerabilities API from Amazon Inspector — 1 operation(s) for vulnerabilities.
  name: Amazon Inspector Vulnerabilities API
  slug: amazon-inspector-vulnerabilities-api
artifact_total: 618
collections:
- collection_type: open
  name: Amazon Inspector API
  slug: open-amazon-inspector
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-inspector-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-inspector-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-inspector-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-inspector-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-inspector-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/inspector/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/inspector/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/inspector/
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
  url: https://aws.amazon.com/blogs/security/category/security-identity-compliance/amazon-inspector/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/inspector/v2/home
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
  url: rules/amazon-inspector-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-inspector-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-inspector-context.jsonld
created: '2026-03-16'
description: Amazon Inspector is an automated vulnerability management service that continually scans AWS workloads for software vulnerabilities and unintended network exposure, providing detailed findings and prioritized remediation guidance.
examples:
- key_count: 15
  name: Amazon Inspector Example
  slug: amazon-inspector-example
- key_count: 4
  name: Inspector Account Aggregation Example
  slug: inspector-account-aggregation-example
- key_count: 2
  name: Inspector Account Aggregation Response Example
  slug: inspector-account-aggregation-response-example
- key_count: 3
  name: Inspector Account Example
  slug: inspector-account-example
- key_count: 0
  name: Inspector Account Id Set Example
  slug: inspector-account-id-set-example
- key_count: 0
  name: Inspector Account List Example
  slug: inspector-account-list-example
- key_count: 3
  name: Inspector Account State Example
  slug: inspector-account-state-example
- key_count: 0
  name: Inspector Account State List Example
  slug: inspector-account-state-list-example
- key_count: 11
  name: Inspector Aggregation Request Example
  slug: inspector-aggregation-request-example
- key_count: 11
  name: Inspector Aggregation Response Example
  slug: inspector-aggregation-response-example
- key_count: 0
  name: Inspector Aggregation Response List Example
  slug: inspector-aggregation-response-list-example
- key_count: 3
  name: Inspector Ami Aggregation Example
  slug: inspector-ami-aggregation-example
- key_count: 4
  name: Inspector Ami Aggregation Response Example
  slug: inspector-ami-aggregation-response-example
- key_count: 0
  name: Inspector Architecture List Example
  slug: inspector-architecture-list-example
- key_count: 1
  name: Inspector Associate Member Request Example
  slug: inspector-associate-member-request-example
- key_count: 1
  name: Inspector Associate Member Response Example
  slug: inspector-associate-member-response-example
- key_count: 4
  name: Inspector Atig Data Example
  slug: inspector-atig-data-example
- key_count: 4
  name: Inspector Auto Enable Example
  slug: inspector-auto-enable-example
- key_count: 10
  name: Inspector Aws Ec2 Instance Details Example
  slug: inspector-aws-ec2-instance-details-example
- key_count: 7
  name: Inspector Aws Ecr Container Aggregation Example
  slug: inspector-aws-ecr-container-aggregation-example
- key_count: 7
  name: Inspector Aws Ecr Container Aggregation Response Example
  slug: inspector-aws-ecr-container-aggregation-response-example
- key_count: 8
  name: Inspector Aws Ecr Container Image Details Example
  slug: inspector-aws-ecr-container-image-details-example
- key_count: 10
  name: Inspector Aws Lambda Function Details Example
  slug: inspector-aws-lambda-function-details-example
- key_count: 1
  name: Inspector Batch Get Account Status Request Example
  slug: inspector-batch-get-account-status-request-example
- key_count: 2
  name: Inspector Batch Get Account Status Response Example
  slug: inspector-batch-get-account-status-response-example
- key_count: 1
  name: Inspector Batch Get Code Snippet Request Example
  slug: inspector-batch-get-code-snippet-request-example
- key_count: 0
  name: Inspector Batch Get Code Snippet Request Finding Arns List Example
  slug: inspector-batch-get-code-snippet-request-finding-arns-list-example
- key_count: 2
  name: Inspector Batch Get Code Snippet Response Example
  slug: inspector-batch-get-code-snippet-response-example
- key_count: 1
  name: Inspector Batch Get Finding Details Request Example
  slug: inspector-batch-get-finding-details-request-example
- key_count: 2
  name: Inspector Batch Get Finding Details Response Example
  slug: inspector-batch-get-finding-details-response-example
- key_count: 0
  name: Inspector Batch Get Free Trial Info Request Account Ids List Example
  slug: inspector-batch-get-free-trial-info-request-account-ids-list-example
- key_count: 1
  name: Inspector Batch Get Free Trial Info Request Example
  slug: inspector-batch-get-free-trial-info-request-example
- key_count: 2
  name: Inspector Batch Get Free Trial Info Response Example
  slug: inspector-batch-get-free-trial-info-response-example
- key_count: 1
  name: Inspector Batch Get Member Ec2 Deep Inspection Status Request Example
  slug: inspector-batch-get-member-ec2-deep-inspection-status-request-example
- key_count: 2
  name: Inspector Batch Get Member Ec2 Deep Inspection Status Response Example
  slug: inspector-batch-get-member-ec2-deep-inspection-status-response-example
- key_count: 1
  name: Inspector Batch Update Member Ec2 Deep Inspection Status Request Example
  slug: inspector-batch-update-member-ec2-deep-inspection-status-request-example
- key_count: 2
  name: Inspector Batch Update Member Ec2 Deep Inspection Status Response Example
  slug: inspector-batch-update-member-ec2-deep-inspection-status-response-example
- key_count: 1
  name: Inspector Cancel Findings Report Request Example
  slug: inspector-cancel-findings-report-request-example
- key_count: 1
  name: Inspector Cancel Findings Report Response Example
  slug: inspector-cancel-findings-report-response-example
- key_count: 1
  name: Inspector Cancel Sbom Export Request Example
  slug: inspector-cancel-sbom-export-request-example
- key_count: 1
  name: Inspector Cancel Sbom Export Response Example
  slug: inspector-cancel-sbom-export-response-example
- key_count: 3
  name: Inspector Cisa Data Example
  slug: inspector-cisa-data-example
- key_count: 4
  name: Inspector Code File Path Example
  slug: inspector-code-file-path-example
- key_count: 2
  name: Inspector Code Line Example
  slug: inspector-code-line-example
- key_count: 0
  name: Inspector Code Line List Example
  slug: inspector-code-line-list-example
- key_count: 3
  name: Inspector Code Snippet Error Example
  slug: inspector-code-snippet-error-example
- key_count: 0
  name: Inspector Code Snippet Error List Example
  slug: inspector-code-snippet-error-list-example
- key_count: 5
  name: Inspector Code Snippet Result Example
  slug: inspector-code-snippet-result-example
- key_count: 0
  name: Inspector Code Snippet Result List Example
  slug: inspector-code-snippet-result-list-example
- key_count: 8
  name: Inspector Code Vulnerability Details Example
  slug: inspector-code-vulnerability-details-example
- key_count: 2
  name: Inspector Counts Example
  slug: inspector-counts-example
- key_count: 0
  name: Inspector Counts List Example
  slug: inspector-counts-list-example
- key_count: 2
  name: Inspector Coverage Date Filter Example
  slug: inspector-coverage-date-filter-example
- key_count: 0
  name: Inspector Coverage Date Filter List Example
  slug: inspector-coverage-date-filter-list-example
- key_count: 13
  name: Inspector Coverage Filter Criteria Example
  slug: inspector-coverage-filter-criteria-example
- key_count: 3
  name: Inspector Coverage Map Filter Example
  slug: inspector-coverage-map-filter-example
- key_count: 0
  name: Inspector Coverage Map Filter List Example
  slug: inspector-coverage-map-filter-list-example
- key_count: 2
  name: Inspector Coverage String Filter Example
  slug: inspector-coverage-string-filter-example
- key_count: 0
  name: Inspector Coverage String Filter List Example
  slug: inspector-coverage-string-filter-list-example
- key_count: 7
  name: Inspector Covered Resource Example
  slug: inspector-covered-resource-example
- key_count: 0
  name: Inspector Covered Resources Example
  slug: inspector-covered-resources-example
- key_count: 6
  name: Inspector Create Filter Request Example
  slug: inspector-create-filter-request-example
- key_count: 1
  name: Inspector Create Filter Response Example
  slug: inspector-create-filter-response-example
- key_count: 3
  name: Inspector Create Findings Report Request Example
  slug: inspector-create-findings-report-request-example
- key_count: 1
  name: Inspector Create Findings Report Response Example
  slug: inspector-create-findings-report-response-example
- key_count: 3
  name: Inspector Create Sbom Export Request Example
  slug: inspector-create-sbom-export-request-example
- key_count: 1
  name: Inspector Create Sbom Export Response Example
  slug: inspector-create-sbom-export-response-example
- key_count: 2
  name: Inspector Cvss Score Adjustment Example
  slug: inspector-cvss-score-adjustment-example
- key_count: 0
  name: Inspector Cvss Score Adjustment List Example
  slug: inspector-cvss-score-adjustment-list-example
- key_count: 6
  name: Inspector Cvss Score Details Example
  slug: inspector-cvss-score-details-example
- key_count: 4
  name: Inspector Cvss Score Example
  slug: inspector-cvss-score-example
- key_count: 0
  name: Inspector Cvss Score List Example
  slug: inspector-cvss-score-list-example
- key_count: 2
  name: Inspector Cvss2 Example
  slug: inspector-cvss2-example
- key_count: 2
  name: Inspector Cvss3 Example
  slug: inspector-cvss3-example
- key_count: 0
  name: Inspector Cwe List Example
  slug: inspector-cwe-list-example
- key_count: 0
  name: Inspector Cwes Example
  slug: inspector-cwes-example
- key_count: 2
  name: Inspector Date Filter Example
  slug: inspector-date-filter-example
- key_count: 0
  name: Inspector Date Filter List Example
  slug: inspector-date-filter-list-example
- key_count: 2
  name: Inspector Delegated Admin Account Example
  slug: inspector-delegated-admin-account-example
- key_count: 0
  name: Inspector Delegated Admin Account List Example
  slug: inspector-delegated-admin-account-list-example
- key_count: 2
  name: Inspector Delegated Admin Example
  slug: inspector-delegated-admin-example
- key_count: 1
  name: Inspector Delete Filter Request Example
  slug: inspector-delete-filter-request-example
- key_count: 1
  name: Inspector Delete Filter Response Example
  slug: inspector-delete-filter-response-example
- key_count: 0
  name: Inspector Describe Organization Configuration Request Example
  slug: inspector-describe-organization-configuration-request-example
- key_count: 2
  name: Inspector Describe Organization Configuration Response Example
  slug: inspector-describe-organization-configuration-response-example
- key_count: 3
  name: Inspector Destination Example
  slug: inspector-destination-example
- key_count: 0
  name: Inspector Detection Platforms Example
  slug: inspector-detection-platforms-example
- key_count: 0
  name: Inspector Detector Tag List Example
  slug: inspector-detector-tag-list-example
- key_count: 1
  name: Inspector Disable Delegated Admin Account Request Example
  slug: inspector-disable-delegated-admin-account-request-example
- key_count: 1
  name: Inspector Disable Delegated Admin Account Response Example
  slug: inspector-disable-delegated-admin-account-response-example
- key_count: 2
  name: Inspector Disable Response Example
  slug: inspector-disable-response-example
- key_count: 1
  name: Inspector Disassociate Member Response Example
  slug: inspector-disassociate-member-response-example
- key_count: 6
  name: Inspector Ec2 Instance Aggregation Example
  slug: inspector-ec2-instance-aggregation-example
- key_count: 7
  name: Inspector Ec2 Instance Aggregation Response Example
  slug: inspector-ec2-instance-aggregation-response-example
- key_count: 1
  name: Inspector Enable Delegated Admin Account Response Example
  slug: inspector-enable-delegated-admin-account-response-example
- key_count: 2
  name: Inspector Enable Response Example
  slug: inspector-enable-response-example
- key_count: 0
  name: Inspector Failed Account List Example
  slug: inspector-failed-account-list-example
- key_count: 0
  name: Inspector Failed Member Account Ec2 Deep Inspection Status State List Example
  slug: inspector-failed-member-account-ec2-deep-inspection-status-state-list-example
- key_count: 42
  name: Inspector Filter Criteria Example
  slug: inspector-filter-criteria-example
- key_count: 0
  name: Inspector Finding Arn List Example
  slug: inspector-finding-arn-list-example
- key_count: 0
  name: Inspector Finding Details Error List Example
  slug: inspector-finding-details-error-list-example
- key_count: 0
  name: Inspector Finding Details Example
  slug: inspector-finding-details-example
- key_count: 4
  name: Inspector Finding Type Aggregation Example
  slug: inspector-finding-type-aggregation-example
- key_count: 2
  name: Inspector Finding Type Aggregation Response Example
  slug: inspector-finding-type-aggregation-response-example
- key_count: 0
  name: Inspector Free Trial Account Info List Example
  slug: inspector-free-trial-account-info-list-example
- key_count: 0
  name: Inspector Free Trial Info Error List Example
  slug: inspector-free-trial-info-error-list-example
- key_count: 1
  name: Inspector Get Configuration Response Example
  slug: inspector-get-configuration-response-example
- key_count: 1
  name: Inspector Get Delegated Admin Account Response Example
  slug: inspector-get-delegated-admin-account-response-example
- key_count: 4
  name: Inspector Get Ec2 Deep Inspection Configuration Response Example
  slug: inspector-get-ec2-deep-inspection-configuration-response-example
- key_count: 1
  name: Inspector Get Encryption Key Response Example
  slug: inspector-get-encryption-key-response-example
- key_count: 6
  name: Inspector Get Findings Report Status Response Example
  slug: inspector-get-findings-report-status-response-example
- key_count: 1
  name: Inspector Get Member Response Example
  slug: inspector-get-member-response-example
- key_count: 7
  name: Inspector Get Sbom Export Response Example
  slug: inspector-get-sbom-export-response-example
- key_count: 5
  name: Inspector Image Layer Aggregation Example
  slug: inspector-image-layer-aggregation-example
- key_count: 5
  name: Inspector Image Layer Aggregation Response Example
  slug: inspector-image-layer-aggregation-response-example
- key_count: 0
  name: Inspector Image Tag List Example
  slug: inspector-image-tag-list-example
- key_count: 0
  name: Inspector Ip V4 Address List Example
  slug: inspector-ip-v4-address-list-example
- key_count: 0
  name: Inspector Ip V6 Address List Example
  slug: inspector-ip-v6-address-list-example
- key_count: 6
  name: Inspector Lambda Function Aggregation Example
  slug: inspector-lambda-function-aggregation-example
- key_count: 7
  name: Inspector Lambda Function Aggregation Response Example
  slug: inspector-lambda-function-aggregation-response-example
- key_count: 5
  name: Inspector Lambda Layer Aggregation Example
  slug: inspector-lambda-layer-aggregation-example
- key_count: 5
  name: Inspector Lambda Layer Aggregation Response Example
  slug: inspector-lambda-layer-aggregation-response-example
- key_count: 3
  name: Inspector Lambda Vpc Config Example
  slug: inspector-lambda-vpc-config-example
- key_count: 0
  name: Inspector Layer List Example
  slug: inspector-layer-list-example
- key_count: 2
  name: Inspector List Account Permissions Response Example
  slug: inspector-list-account-permissions-response-example
- key_count: 2
  name: Inspector List Coverage Response Example
  slug: inspector-list-coverage-response-example
- key_count: 3
  name: Inspector List Coverage Statistics Response Example
  slug: inspector-list-coverage-statistics-response-example
- key_count: 2
  name: Inspector List Delegated Admin Accounts Response Example
  slug: inspector-list-delegated-admin-accounts-response-example
- key_count: 2
  name: Inspector List Filters Response Example
  slug: inspector-list-filters-response-example
- key_count: 3
  name: Inspector List Finding Aggregations Response Example
  slug: inspector-list-finding-aggregations-response-example
- key_count: 2
  name: Inspector List Findings Response Example
  slug: inspector-list-findings-response-example
- key_count: 2
  name: Inspector List Members Response Example
  slug: inspector-list-members-response-example
- key_count: 1
  name: Inspector List Tags For Resource Response Example
  slug: inspector-list-tags-for-resource-response-example
- key_count: 2
  name: Inspector List Usage Totals Response Example
  slug: inspector-list-usage-totals-response-example
- key_count: 0
  name: Inspector Map Filter List Example
  slug: inspector-map-filter-list-example
- key_count: 2
  name: Inspector Member Account Ec2 Deep Inspection Status Example
  slug: inspector-member-account-ec2-deep-inspection-status-example
- key_count: 0
  name: Inspector Member Account Ec2 Deep Inspection Status List Example
  slug: inspector-member-account-ec2-deep-inspection-status-list-example
- key_count: 0
  name: Inspector Member Account Ec2 Deep Inspection Status State List Example
  slug: inspector-member-account-ec2-deep-inspection-status-state-list-example
- key_count: 0
  name: Inspector Number Filter List Example
  slug: inspector-number-filter-list-example
- key_count: 3
  name: Inspector Package Aggregation Example
  slug: inspector-package-aggregation-example
- key_count: 3
  name: Inspector Package Aggregation Response Example
  slug: inspector-package-aggregation-response-example
- key_count: 0
  name: Inspector Package Filter List Example
  slug: inspector-package-filter-list-example
- key_count: 0
  name: Inspector Port Range Filter List Example
  slug: inspector-port-range-filter-list-example
- key_count: 0
  name: Inspector Reference Urls Example
  slug: inspector-reference-urls-example
- key_count: 3
  name: Inspector Repository Aggregation Example
  slug: inspector-repository-aggregation-example
- key_count: 4
  name: Inspector Repository Aggregation Response Example
  slug: inspector-repository-aggregation-response-example
- key_count: 0
  name: Inspector Reset Encryption Key Response Example
  slug: inspector-reset-encryption-key-response-example
- key_count: 8
  name: Inspector Resource Filter Criteria Example
  slug: inspector-resource-filter-criteria-example
- key_count: 0
  name: Inspector Resource Map Filter List Example
  slug: inspector-resource-map-filter-list-example
- key_count: 4
  name: Inspector Resource Scan Metadata Example
  slug: inspector-resource-scan-metadata-example
- key_count: 4
  name: Inspector Resource State Example
  slug: inspector-resource-state-example
- key_count: 4
  name: Inspector Resource Status Example
  slug: inspector-resource-status-example
- key_count: 0
  name: Inspector Resource String Filter List Example
  slug: inspector-resource-string-filter-list-example
- key_count: 2
  name: Inspector Scan Status Example
  slug: inspector-scan-status-example
- key_count: 2
  name: Inspector Search Vulnerabilities Response Example
  slug: inspector-search-vulnerabilities-response-example
- key_count: 4
  name: Inspector Severity Counts Example
  slug: inspector-severity-counts-example
- key_count: 3
  name: Inspector State Example
  slug: inspector-state-example
- key_count: 2
  name: Inspector String Filter Example
  slug: inspector-string-filter-example
- key_count: 0
  name: Inspector String Filter List Example
  slug: inspector-string-filter-list-example
- key_count: 0
  name: Inspector String List Example
  slug: inspector-string-list-example
- key_count: 0
  name: Inspector Suggested Fixes Example
  slug: inspector-suggested-fixes-example
- key_count: 0
  name: Inspector Tag Map Example
  slug: inspector-tag-map-example
- key_count: 0
  name: Inspector Tag Resource Response Example
  slug: inspector-tag-resource-response-example
- key_count: 0
  name: Inspector Targets Example
  slug: inspector-targets-example
- key_count: 6
  name: Inspector Title Aggregation Example
  slug: inspector-title-aggregation-example
- key_count: 4
  name: Inspector Title Aggregation Response Example
  slug: inspector-title-aggregation-response-example
- key_count: 0
  name: Inspector Ttps Example
  slug: inspector-ttps-example
- key_count: 0
  name: Inspector Untag Resource Response Example
  slug: inspector-untag-resource-response-example
- key_count: 0
  name: Inspector Update Configuration Response Example
  slug: inspector-update-configuration-response-example
- key_count: 4
  name: Inspector Update Ec2 Deep Inspection Configuration Response Example
  slug: inspector-update-ec2-deep-inspection-configuration-response-example
- key_count: 0
  name: Inspector Update Encryption Key Response Example
  slug: inspector-update-encryption-key-response-example
- key_count: 1
  name: Inspector Update Filter Response Example
  slug: inspector-update-filter-response-example
- key_count: 0
  name: Inspector Update Org Ec2 Deep Inspection Configuration Response Example
  slug: inspector-update-org-ec2-deep-inspection-configuration-response-example
- key_count: 1
  name: Inspector Update Organization Configuration Response Example
  slug: inspector-update-organization-configuration-response-example
- key_count: 0
  name: Inspector Vuln Id List Example
  slug: inspector-vuln-id-list-example
features:
- description: Continuously scans EC2, container images, and Lambda functions for software vulnerabilities.
  name: Automated Vulnerability Scanning
- description: Ranks vulnerabilities by exploitability and impact to prioritize remediation.
  name: Risk Scoring
- description: Generates software bill of materials for scanned workloads.
  name: SBOM Export
- description: Manages vulnerability scanning across all accounts in an AWS Organization.
  name: Multi-Account Support
finops:
- name: Amazon Inspector Finops
  service_category: API
  slug: amazon-inspector-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-inspector.png
json_schemas:
- name: Amazon Inspector Finding Definition
  property_count: 15
  slug: amazon-inspector
- name: AccountAggregationResponse
  property_count: 2
  slug: inspector-account-aggregation-response
- name: AccountAggregation
  property_count: 4
  slug: inspector-account-aggregation
- name: AccountIdSet
  property_count: 0
  slug: inspector-account-id-set
- name: AccountList
  property_count: 0
  slug: inspector-account-list
- name: Account
  property_count: 3
  slug: inspector-account
- name: AccountSortBy
  property_count: 0
  slug: inspector-account-sort-by
- name: AccountStateList
  property_count: 0
  slug: inspector-account-state-list
- name: AccountState
  property_count: 3
  slug: inspector-account-state
- name: AggregationFindingType
  property_count: 0
  slug: inspector-aggregation-finding-type
- name: AggregationRequest
  property_count: 11
  slug: inspector-aggregation-request
- name: AggregationResourceType
  property_count: 0
  slug: inspector-aggregation-resource-type
- name: AggregationResponseList
  property_count: 0
  slug: inspector-aggregation-response-list
- name: AggregationResponse
  property_count: 11
  slug: inspector-aggregation-response
- name: AggregationType
  property_count: 0
  slug: inspector-aggregation-type
- name: AmiAggregationResponse
  property_count: 4
  slug: inspector-ami-aggregation-response
- name: AmiAggregation
  property_count: 3
  slug: inspector-ami-aggregation
- name: AmiSortBy
  property_count: 0
  slug: inspector-ami-sort-by
- name: ArchitectureList
  property_count: 0
  slug: inspector-architecture-list
- name: Architecture
  property_count: 0
  slug: inspector-architecture
- name: AssociateMemberRequest
  property_count: 1
  slug: inspector-associate-member-request
- name: AssociateMemberResponse
  property_count: 1
  slug: inspector-associate-member-response
- name: AtigData
  property_count: 4
  slug: inspector-atig-data
- name: AutoEnable
  property_count: 4
  slug: inspector-auto-enable
- name: AwsEc2InstanceDetails
  property_count: 10
  slug: inspector-aws-ec2-instance-details
- name: AwsEcrContainerAggregationResponse
  property_count: 7
  slug: inspector-aws-ecr-container-aggregation-response
- name: AwsEcrContainerAggregation
  property_count: 7
  slug: inspector-aws-ecr-container-aggregation
- name: AwsEcrContainerImageDetails
  property_count: 8
  slug: inspector-aws-ecr-container-image-details
- name: AwsEcrContainerSortBy
  property_count: 0
  slug: inspector-aws-ecr-container-sort-by
- name: AwsLambdaFunctionDetails
  property_count: 10
  slug: inspector-aws-lambda-function-details
- name: BatchGetAccountStatusRequest
  property_count: 1
  slug: inspector-batch-get-account-status-request
- name: BatchGetAccountStatusResponse
  property_count: 2
  slug: inspector-batch-get-account-status-response
- name: BatchGetCodeSnippetRequestFindingArnsList
  property_count: 0
  slug: inspector-batch-get-code-snippet-request-finding-arns-list
- name: BatchGetCodeSnippetRequest
  property_count: 1
  slug: inspector-batch-get-code-snippet-request
- name: BatchGetCodeSnippetResponse
  property_count: 2
  slug: inspector-batch-get-code-snippet-response
- name: BatchGetFindingDetailsRequest
  property_count: 1
  slug: inspector-batch-get-finding-details-request
- name: BatchGetFindingDetailsResponse
  property_count: 2
  slug: inspector-batch-get-finding-details-response
- name: BatchGetFreeTrialInfoRequestAccountIdsList
  property_count: 0
  slug: inspector-batch-get-free-trial-info-request-account-ids-list
- name: BatchGetFreeTrialInfoRequest
  property_count: 1
  slug: inspector-batch-get-free-trial-info-request
- name: BatchGetFreeTrialInfoResponse
  property_count: 2
  slug: inspector-batch-get-free-trial-info-response
- name: BatchGetMemberEc2DeepInspectionStatusRequest
  property_count: 1
  slug: inspector-batch-get-member-ec2-deep-inspection-status-request
- name: BatchGetMemberEc2DeepInspectionStatusResponse
  property_count: 2
  slug: inspector-batch-get-member-ec2-deep-inspection-status-response
- name: BatchUpdateMemberEc2DeepInspectionStatusRequest
  property_count: 1
  slug: inspector-batch-update-member-ec2-deep-inspection-status-request
- name: BatchUpdateMemberEc2DeepInspectionStatusResponse
  property_count: 2
  slug: inspector-batch-update-member-ec2-deep-inspection-status-response
- name: CancelFindingsReportRequest
  property_count: 1
  slug: inspector-cancel-findings-report-request
- name: CancelFindingsReportResponse
  property_count: 1
  slug: inspector-cancel-findings-report-response
- name: CancelSbomExportRequest
  property_count: 1
  slug: inspector-cancel-sbom-export-request
- name: CancelSbomExportResponse
  property_count: 1
  slug: inspector-cancel-sbom-export-response
- name: CisaData
  property_count: 3
  slug: inspector-cisa-data
- name: CodeFilePath
  property_count: 4
  slug: inspector-code-file-path
- name: CodeLineList
  property_count: 0
  slug: inspector-code-line-list
- name: CodeLine
  property_count: 2
  slug: inspector-code-line
- name: CodeSnippetErrorCode
  property_count: 0
  slug: inspector-code-snippet-error-code
- name: CodeSnippetErrorList
  property_count: 0
  slug: inspector-code-snippet-error-list
- name: CodeSnippetError
  property_count: 3
  slug: inspector-code-snippet-error
- name: CodeSnippetResultList
  property_count: 0
  slug: inspector-code-snippet-result-list
- name: CodeSnippetResult
  property_count: 5
  slug: inspector-code-snippet-result
- name: CodeVulnerabilityDetails
  property_count: 8
  slug: inspector-code-vulnerability-details
- name: CountsList
  property_count: 0
  slug: inspector-counts-list
- name: Counts
  property_count: 2
  slug: inspector-counts
- name: CoverageDateFilterList
  property_count: 0
  slug: inspector-coverage-date-filter-list
- name: CoverageDateFilter
  property_count: 2
  slug: inspector-coverage-date-filter
- name: CoverageFilterCriteria
  property_count: 13
  slug: inspector-coverage-filter-criteria
- name: CoverageMapComparison
  property_count: 0
  slug: inspector-coverage-map-comparison
- name: CoverageMapFilterList
  property_count: 0
  slug: inspector-coverage-map-filter-list
- name: CoverageMapFilter
  property_count: 3
  slug: inspector-coverage-map-filter
- name: CoverageResourceType
  property_count: 0
  slug: inspector-coverage-resource-type
- name: CoverageStringComparison
  property_count: 0
  slug: inspector-coverage-string-comparison
- name: CoverageStringFilterList
  property_count: 0
  slug: inspector-coverage-string-filter-list
- name: CoverageStringFilter
  property_count: 2
  slug: inspector-coverage-string-filter
- name: CoveredResource
  property_count: 7
  slug: inspector-covered-resource
- name: CoveredResources
  property_count: 0
  slug: inspector-covered-resources
- name: CreateFilterRequest
  property_count: 6
  slug: inspector-create-filter-request
- name: CreateFilterResponse
  property_count: 1
  slug: inspector-create-filter-response
- name: CreateFindingsReportRequest
  property_count: 3
  slug: inspector-create-findings-report-request
- name: CreateFindingsReportResponse
  property_count: 1
  slug: inspector-create-findings-report-response
- name: CreateSbomExportRequest
  property_count: 3
  slug: inspector-create-sbom-export-request
- name: CreateSbomExportResponse
  property_count: 1
  slug: inspector-create-sbom-export-response
- name: Currency
  property_count: 0
  slug: inspector-currency
- name: CvssScoreAdjustmentList
  property_count: 0
  slug: inspector-cvss-score-adjustment-list
- name: CvssScoreAdjustment
  property_count: 2
  slug: inspector-cvss-score-adjustment
- name: CvssScoreDetails
  property_count: 6
  slug: inspector-cvss-score-details
- name: CvssScoreList
  property_count: 0
  slug: inspector-cvss-score-list
- name: CvssScore
  property_count: 4
  slug: inspector-cvss-score
- name: Cvss2
  property_count: 2
  slug: inspector-cvss2
- name: Cvss3
  property_count: 2
  slug: inspector-cvss3
- name: CweList
  property_count: 0
  slug: inspector-cwe-list
- name: Cwes
  property_count: 0
  slug: inspector-cwes
- name: DateFilterList
  property_count: 0
  slug: inspector-date-filter-list
- name: DateFilter
  property_count: 2
  slug: inspector-date-filter
- name: DelegatedAdminAccountList
  property_count: 0
  slug: inspector-delegated-admin-account-list
- name: DelegatedAdminAccount
  property_count: 2
  slug: inspector-delegated-admin-account
- name: DelegatedAdmin
  property_count: 2
  slug: inspector-delegated-admin
- name: DelegatedAdminStatus
  property_count: 0
  slug: inspector-delegated-admin-status
- name: DeleteFilterRequest
  property_count: 1
  slug: inspector-delete-filter-request
- name: DeleteFilterResponse
  property_count: 1
  slug: inspector-delete-filter-response
- name: DescribeOrganizationConfigurationRequest
  property_count: 0
  slug: inspector-describe-organization-configuration-request
- name: DescribeOrganizationConfigurationResponse
  property_count: 2
  slug: inspector-describe-organization-configuration-response
- name: Destination
  property_count: 3
  slug: inspector-destination
- name: DetectionPlatforms
  property_count: 0
  slug: inspector-detection-platforms
- name: DetectorTagList
  property_count: 0
  slug: inspector-detector-tag-list
- name: DisableDelegatedAdminAccountRequest
  property_count: 1
  slug: inspector-disable-delegated-admin-account-request
- name: DisableDelegatedAdminAccountResponse
  property_count: 1
  slug: inspector-disable-delegated-admin-account-response
- name: DisableResponse
  property_count: 2
  slug: inspector-disable-response
- name: DisassociateMemberResponse
  property_count: 1
  slug: inspector-disassociate-member-response
- name: Ec2InstanceAggregationResponse
  property_count: 7
  slug: inspector-ec2-instance-aggregation-response
- name: Ec2InstanceAggregation
  property_count: 6
  slug: inspector-ec2-instance-aggregation
- name: EcrRescanDuration
  property_count: 0
  slug: inspector-ecr-rescan-duration
- name: EnableDelegatedAdminAccountResponse
  property_count: 1
  slug: inspector-enable-delegated-admin-account-response
- name: EnableResponse
  property_count: 2
  slug: inspector-enable-response
- name: FailedAccountList
  property_count: 0
  slug: inspector-failed-account-list
- name: FailedMemberAccountEc2DeepInspectionStatusStateList
  property_count: 0
  slug: inspector-failed-member-account-ec2-deep-inspection-status-state-list
- name: FilterAction
  property_count: 0
  slug: inspector-filter-action
- name: FilterCriteria
  property_count: 42
  slug: inspector-filter-criteria
- name: FindingArnList
  property_count: 0
  slug: inspector-finding-arn-list
- name: FindingDetailsErrorList
  property_count: 0
  slug: inspector-finding-details-error-list
- name: FindingDetails
  property_count: 0
  slug: inspector-finding-details
- name: FindingTypeAggregationResponse
  property_count: 2
  slug: inspector-finding-type-aggregation-response
- name: FindingTypeAggregation
  property_count: 4
  slug: inspector-finding-type-aggregation
- name: FreeTrialAccountInfoList
  property_count: 0
  slug: inspector-free-trial-account-info-list
- name: FreeTrialInfoErrorList
  property_count: 0
  slug: inspector-free-trial-info-error-list
- name: GetConfigurationResponse
  property_count: 1
  slug: inspector-get-configuration-response
- name: GetDelegatedAdminAccountResponse
  property_count: 1
  slug: inspector-get-delegated-admin-account-response
- name: GetEc2DeepInspectionConfigurationResponse
  property_count: 4
  slug: inspector-get-ec2-deep-inspection-configuration-response
- name: GetEncryptionKeyResponse
  property_count: 1
  slug: inspector-get-encryption-key-response
- name: GetFindingsReportStatusResponse
  property_count: 6
  slug: inspector-get-findings-report-status-response
- name: GetMemberResponse
  property_count: 1
  slug: inspector-get-member-response
- name: GetSbomExportResponse
  property_count: 7
  slug: inspector-get-sbom-export-response
- name: GroupKey
  property_count: 0
  slug: inspector-group-key
- name: ImageLayerAggregationResponse
  property_count: 5
  slug: inspector-image-layer-aggregation-response
- name: ImageLayerAggregation
  property_count: 5
  slug: inspector-image-layer-aggregation
- name: ImageTagList
  property_count: 0
  slug: inspector-image-tag-list
- name: IpV4AddressList
  property_count: 0
  slug: inspector-ip-v4-address-list
- name: IpV6AddressList
  property_count: 0
  slug: inspector-ip-v6-address-list
- name: LambdaFunctionAggregationResponse
  property_count: 7
  slug: inspector-lambda-function-aggregation-response
- name: LambdaFunctionAggregation
  property_count: 6
  slug: inspector-lambda-function-aggregation
- name: LambdaLayerAggregationResponse
  property_count: 5
  slug: inspector-lambda-layer-aggregation-response
- name: LambdaLayerAggregation
  property_count: 5
  slug: inspector-lambda-layer-aggregation
- name: LambdaVpcConfig
  property_count: 3
  slug: inspector-lambda-vpc-config
- name: LayerList
  property_count: 0
  slug: inspector-layer-list
- name: ListAccountPermissionsResponse
  property_count: 2
  slug: inspector-list-account-permissions-response
- name: ListCoverageResponse
  property_count: 2
  slug: inspector-list-coverage-response
- name: ListCoverageStatisticsResponse
  property_count: 3
  slug: inspector-list-coverage-statistics-response
- name: ListDelegatedAdminAccountsResponse
  property_count: 2
  slug: inspector-list-delegated-admin-accounts-response
- name: ListFiltersResponse
  property_count: 2
  slug: inspector-list-filters-response
- name: ListFindingAggregationsResponse
  property_count: 3
  slug: inspector-list-finding-aggregations-response
- name: ListFindingsResponse
  property_count: 2
  slug: inspector-list-findings-response
- name: ListMembersResponse
  property_count: 2
  slug: inspector-list-members-response
- name: ListTagsForResourceResponse
  property_count: 1
  slug: inspector-list-tags-for-resource-response
- name: ListUsageTotalsResponse
  property_count: 2
  slug: inspector-list-usage-totals-response
- name: MapFilterList
  property_count: 0
  slug: inspector-map-filter-list
- name: MemberAccountEc2DeepInspectionStatusList
  property_count: 0
  slug: inspector-member-account-ec2-deep-inspection-status-list
- name: MemberAccountEc2DeepInspectionStatus
  property_count: 2
  slug: inspector-member-account-ec2-deep-inspection-status
- name: MemberAccountEc2DeepInspectionStatusStateList
  property_count: 0
  slug: inspector-member-account-ec2-deep-inspection-status-state-list
- name: NumberFilterList
  property_count: 0
  slug: inspector-number-filter-list
- name: PackageAggregationResponse
  property_count: 3
  slug: inspector-package-aggregation-response
- name: PackageAggregation
  property_count: 3
  slug: inspector-package-aggregation
- name: PackageFilterList
  property_count: 0
  slug: inspector-package-filter-list
- name: PackageType
  property_count: 0
  slug: inspector-package-type
- name: PortRangeFilterList
  property_count: 0
  slug: inspector-port-range-filter-list
- name: ReferenceUrls
  property_count: 0
  slug: inspector-reference-urls
- name: RelationshipStatus
  property_count: 0
  slug: inspector-relationship-status
- name: ReportFormat
  property_count: 0
  slug: inspector-report-format
- name: RepositoryAggregationResponse
  property_count: 4
  slug: inspector-repository-aggregation-response
- name: RepositoryAggregation
  property_count: 3
  slug: inspector-repository-aggregation
- name: ResetEncryptionKeyResponse
  property_count: 0
  slug: inspector-reset-encryption-key-response
- name: ResourceFilterCriteria
  property_count: 8
  slug: inspector-resource-filter-criteria
- name: ResourceMapFilterList
  property_count: 0
  slug: inspector-resource-map-filter-list
- name: ResourceScanMetadata
  property_count: 4
  slug: inspector-resource-scan-metadata
- name: ResourceScanType
  property_count: 0
  slug: inspector-resource-scan-type
- name: ResourceState
  property_count: 4
  slug: inspector-resource-state
- name: ResourceStatus
  property_count: 4
  slug: inspector-resource-status
- name: ResourceStringFilterList
  property_count: 0
  slug: inspector-resource-string-filter-list
- name: Runtime
  property_count: 0
  slug: inspector-runtime
- name: SbomReportFormat
  property_count: 0
  slug: inspector-sbom-report-format
- name: ScanStatus
  property_count: 2
  slug: inspector-scan-status
- name: ScanType
  property_count: 0
  slug: inspector-scan-type
- name: SearchVulnerabilitiesResponse
  property_count: 2
  slug: inspector-search-vulnerabilities-response
- name: SeverityCounts
  property_count: 4
  slug: inspector-severity-counts
- name: SortField
  property_count: 0
  slug: inspector-sort-field
- name: SortOrder
  property_count: 0
  slug: inspector-sort-order
- name: State
  property_count: 3
  slug: inspector-state
- name: Status
  property_count: 0
  slug: inspector-status
- name: StringFilterList
  property_count: 0
  slug: inspector-string-filter-list
- name: StringFilter
  property_count: 2
  slug: inspector-string-filter
- name: StringList
  property_count: 0
  slug: inspector-string-list
- name: SuggestedFixes
  property_count: 0
  slug: inspector-suggested-fixes
- name: TagMap
  property_count: 0
  slug: inspector-tag-map
- name: TagResourceResponse
  property_count: 0
  slug: inspector-tag-resource-response
- name: Targets
  property_count: 0
  slug: inspector-targets
- name: TitleAggregationResponse
  property_count: 4
  slug: inspector-title-aggregation-response
- name: TitleAggregation
  property_count: 6
  slug: inspector-title-aggregation
- name: Ttps
  property_count: 0
  slug: inspector-ttps
- name: UntagResourceResponse
  property_count: 0
  slug: inspector-untag-resource-response
- name: UpdateConfigurationResponse
  property_count: 0
  slug: inspector-update-configuration-response
- name: UpdateEc2DeepInspectionConfigurationResponse
  property_count: 4
  slug: inspector-update-ec2-deep-inspection-configuration-response
- name: UpdateEncryptionKeyResponse
  property_count: 0
  slug: inspector-update-encryption-key-response
- name: UpdateFilterResponse
  property_count: 1
  slug: inspector-update-filter-response
- name: UpdateOrgEc2DeepInspectionConfigurationResponse
  property_count: 0
  slug: inspector-update-org-ec2-deep-inspection-configuration-response
- name: UpdateOrganizationConfigurationResponse
  property_count: 1
  slug: inspector-update-organization-configuration-response
- name: VulnIdList
  property_count: 0
  slug: inspector-vuln-id-list
json_structures:
- name: Amazon Inspector Structure
  property_count: 15
  slug: amazon-inspector-structure
- name: Inspector Account Aggregation Response Structure
  property_count: 2
  slug: inspector-account-aggregation-response-structure
- name: Inspector Account Aggregation Structure
  property_count: 4
  slug: inspector-account-aggregation-structure
- name: Inspector Account Id Set Structure
  property_count: 0
  slug: inspector-account-id-set-structure
- name: Inspector Account List Structure
  property_count: 0
  slug: inspector-account-list-structure
- name: Inspector Account Sort By Structure
  property_count: 0
  slug: inspector-account-sort-by-structure
- name: Inspector Account State List Structure
  property_count: 0
  slug: inspector-account-state-list-structure
- name: Inspector Account State Structure
  property_count: 3
  slug: inspector-account-state-structure
- name: Inspector Account Structure
  property_count: 3
  slug: inspector-account-structure
- name: Inspector Aggregation Finding Type Structure
  property_count: 0
  slug: inspector-aggregation-finding-type-structure
- name: Inspector Aggregation Request Structure
  property_count: 11
  slug: inspector-aggregation-request-structure
- name: Inspector Aggregation Resource Type Structure
  property_count: 0
  slug: inspector-aggregation-resource-type-structure
- name: Inspector Aggregation Response List Structure
  property_count: 0
  slug: inspector-aggregation-response-list-structure
- name: Inspector Aggregation Response Structure
  property_count: 11
  slug: inspector-aggregation-response-structure
- name: Inspector Aggregation Type Structure
  property_count: 0
  slug: inspector-aggregation-type-structure
- name: Inspector Ami Aggregation Response Structure
  property_count: 4
  slug: inspector-ami-aggregation-response-structure
- name: Inspector Ami Aggregation Structure
  property_count: 3
  slug: inspector-ami-aggregation-structure
- name: Inspector Ami Sort By Structure
  property_count: 0
  slug: inspector-ami-sort-by-structure
- name: Inspector Architecture List Structure
  property_count: 0
  slug: inspector-architecture-list-structure
- name: Inspector Architecture Structure
  property_count: 0
  slug: inspector-architecture-structure
- name: Inspector Associate Member Request Structure
  property_count: 1
  slug: inspector-associate-member-request-structure
- name: Inspector Associate Member Response Structure
  property_count: 1
  slug: inspector-associate-member-response-structure
- name: Inspector Atig Data Structure
  property_count: 4
  slug: inspector-atig-data-structure
- name: Inspector Auto Enable Structure
  property_count: 4
  slug: inspector-auto-enable-structure
- name: Inspector Aws Ec2 Instance Details Structure
  property_count: 10
  slug: inspector-aws-ec2-instance-details-structure
- name: Inspector Aws Ecr Container Aggregation Response Structure
  property_count: 7
  slug: inspector-aws-ecr-container-aggregation-response-structure
- name: Inspector Aws Ecr Container Aggregation Structure
  property_count: 7
  slug: inspector-aws-ecr-container-aggregation-structure
- name: Inspector Aws Ecr Container Image Details Structure
  property_count: 8
  slug: inspector-aws-ecr-container-image-details-structure
- name: Inspector Aws Ecr Container Sort By Structure
  property_count: 0
  slug: inspector-aws-ecr-container-sort-by-structure
- name: Inspector Aws Lambda Function Details Structure
  property_count: 10
  slug: inspector-aws-lambda-function-details-structure
- name: Inspector Batch Get Account Status Request Structure
  property_count: 1
  slug: inspector-batch-get-account-status-request-structure
- name: Inspector Batch Get Account Status Response Structure
  property_count: 2
  slug: inspector-batch-get-account-status-response-structure
- name: Inspector Batch Get Code Snippet Request Finding Arns List Structure
  property_count: 0
  slug: inspector-batch-get-code-snippet-request-finding-arns-list-structure
- name: Inspector Batch Get Code Snippet Request Structure
  property_count: 1
  slug: inspector-batch-get-code-snippet-request-structure
- name: Inspector Batch Get Code Snippet Response Structure
  property_count: 2
  slug: inspector-batch-get-code-snippet-response-structure
- name: Inspector Batch Get Finding Details Request Structure
  property_count: 1
  slug: inspector-batch-get-finding-details-request-structure
- name: Inspector Batch Get Finding Details Response Structure
  property_count: 2
  slug: inspector-batch-get-finding-details-response-structure
- name: Inspector Batch Get Free Trial Info Request Account Ids List Structure
  property_count: 0
  slug: inspector-batch-get-free-trial-info-request-account-ids-list-structure
- name: Inspector Batch Get Free Trial Info Request Structure
  property_count: 1
  slug: inspector-batch-get-free-trial-info-request-structure
- name: Inspector Batch Get Free Trial Info Response Structure
  property_count: 2
  slug: inspector-batch-get-free-trial-info-response-structure
- name: Inspector Batch Get Member Ec2 Deep Inspection Status Request Structure
  property_count: 1
  slug: inspector-batch-get-member-ec2-deep-inspection-status-request-structure
- name: Inspector Batch Get Member Ec2 Deep Inspection Status Response Structure
  property_count: 2
  slug: inspector-batch-get-member-ec2-deep-inspection-status-response-structure
- name: Inspector Batch Update Member Ec2 Deep Inspection Status Request Structure
  property_count: 1
  slug: inspector-batch-update-member-ec2-deep-inspection-status-request-structure
- name: Inspector Batch Update Member Ec2 Deep Inspection Status Response Structure
  property_count: 2
  slug: inspector-batch-update-member-ec2-deep-inspection-status-response-structure
- name: Inspector Cancel Findings Report Request Structure
  property_count: 1
  slug: inspector-cancel-findings-report-request-structure
- name: Inspector Cancel Findings Report Response Structure
  property_count: 1
  slug: inspector-cancel-findings-report-response-structure
- name: Inspector Cancel Sbom Export Request Structure
  property_count: 1
  slug: inspector-cancel-sbom-export-request-structure
- name: Inspector Cancel Sbom Export Response Structure
  property_count: 1
  slug: inspector-cancel-sbom-export-response-structure
- name: Inspector Cisa Data Structure
  property_count: 3
  slug: inspector-cisa-data-structure
- name: Inspector Code File Path Structure
  property_count: 4
  slug: inspector-code-file-path-structure
- name: Inspector Code Line List Structure
  property_count: 0
  slug: inspector-code-line-list-structure
- name: Inspector Code Line Structure
  property_count: 2
  slug: inspector-code-line-structure
- name: Inspector Code Snippet Error Code Structure
  property_count: 0
  slug: inspector-code-snippet-error-code-structure
- name: Inspector Code Snippet Error List Structure
  property_count: 0
  slug: inspector-code-snippet-error-list-structure
- name: Inspector Code Snippet Error Structure
  property_count: 3
  slug: inspector-code-snippet-error-structure
- name: Inspector Code Snippet Result List Structure
  property_count: 0
  slug: inspector-code-snippet-result-list-structure
- name: Inspector Code Snippet Result Structure
  property_count: 5
  slug: inspector-code-snippet-result-structure
- name: Inspector Code Vulnerability Details Structure
  property_count: 8
  slug: inspector-code-vulnerability-details-structure
- name: Inspector Counts List Structure
  property_count: 0
  slug: inspector-counts-list-structure
- name: Inspector Counts Structure
  property_count: 2
  slug: inspector-counts-structure
- name: Inspector Coverage Date Filter List Structure
  property_count: 0
  slug: inspector-coverage-date-filter-list-structure
- name: Inspector Coverage Date Filter Structure
  property_count: 2
  slug: inspector-coverage-date-filter-structure
- name: Inspector Coverage Filter Criteria Structure
  property_count: 13
  slug: inspector-coverage-filter-criteria-structure
- name: Inspector Coverage Map Comparison Structure
  property_count: 0
  slug: inspector-coverage-map-comparison-structure
- name: Inspector Coverage Map Filter List Structure
  property_count: 0
  slug: inspector-coverage-map-filter-list-structure
- name: Inspector Coverage Map Filter Structure
  property_count: 3
  slug: inspector-coverage-map-filter-structure
- name: Inspector Coverage Resource Type Structure
  property_count: 0
  slug: inspector-coverage-resource-type-structure
- name: Inspector Coverage String Comparison Structure
  property_count: 0
  slug: inspector-coverage-string-comparison-structure
- name: Inspector Coverage String Filter List Structure
  property_count: 0
  slug: inspector-coverage-string-filter-list-structure
- name: Inspector Coverage String Filter Structure
  property_count: 2
  slug: inspector-coverage-string-filter-structure
- name: Inspector Covered Resource Structure
  property_count: 7
  slug: inspector-covered-resource-structure
- name: Inspector Covered Resources Structure
  property_count: 0
  slug: inspector-covered-resources-structure
- name: Inspector Create Filter Request Structure
  property_count: 6
  slug: inspector-create-filter-request-structure
- name: Inspector Create Filter Response Structure
  property_count: 1
  slug: inspector-create-filter-response-structure
- name: Inspector Create Findings Report Request Structure
  property_count: 3
  slug: inspector-create-findings-report-request-structure
- name: Inspector Create Findings Report Response Structure
  property_count: 1
  slug: inspector-create-findings-report-response-structure
- name: Inspector Create Sbom Export Request Structure
  property_count: 3
  slug: inspector-create-sbom-export-request-structure
- name: Inspector Create Sbom Export Response Structure
  property_count: 1
  slug: inspector-create-sbom-export-response-structure
- name: Inspector Currency Structure
  property_count: 0
  slug: inspector-currency-structure
- name: Inspector Cvss Score Adjustment List Structure
  property_count: 0
  slug: inspector-cvss-score-adjustment-list-structure
- name: Inspector Cvss Score Adjustment Structure
  property_count: 2
  slug: inspector-cvss-score-adjustment-structure
- name: Inspector Cvss Score Details Structure
  property_count: 6
  slug: inspector-cvss-score-details-structure
- name: Inspector Cvss Score List Structure
  property_count: 0
  slug: inspector-cvss-score-list-structure
- name: Inspector Cvss Score Structure
  property_count: 4
  slug: inspector-cvss-score-structure
- name: Inspector Cvss2 Structure
  property_count: 2
  slug: inspector-cvss2-structure
- name: Inspector Cvss3 Structure
  property_count: 2
  slug: inspector-cvss3-structure
- name: Inspector Cwe List Structure
  property_count: 0
  slug: inspector-cwe-list-structure
- name: Inspector Cwes Structure
  property_count: 0
  slug: inspector-cwes-structure
- name: Inspector Date Filter List Structure
  property_count: 0
  slug: inspector-date-filter-list-structure
- name: Inspector Date Filter Structure
  property_count: 2
  slug: inspector-date-filter-structure
- name: Inspector Delegated Admin Account List Structure
  property_count: 0
  slug: inspector-delegated-admin-account-list-structure
- name: Inspector Delegated Admin Account Structure
  property_count: 2
  slug: inspector-delegated-admin-account-structure
- name: Inspector Delegated Admin Status Structure
  property_count: 0
  slug: inspector-delegated-admin-status-structure
- name: Inspector Delegated Admin Structure
  property_count: 2
  slug: inspector-delegated-admin-structure
- name: Inspector Delete Filter Request Structure
  property_count: 1
  slug: inspector-delete-filter-request-structure
- name: Inspector Delete Filter Response Structure
  property_count: 1
  slug: inspector-delete-filter-response-structure
- name: Inspector Describe Organization Configuration Request Structure
  property_count: 0
  slug: inspector-describe-organization-configuration-request-structure
- name: Inspector Describe Organization Configuration Response Structure
  property_count: 2
  slug: inspector-describe-organization-configuration-response-structure
- name: Inspector Destination Structure
  property_count: 3
  slug: inspector-destination-structure
- name: Inspector Detection Platforms Structure
  property_count: 0
  slug: inspector-detection-platforms-structure
- name: Inspector Detector Tag List Structure
  property_count: 0
  slug: inspector-detector-tag-list-structure
- name: Inspector Disable Delegated Admin Account Request Structure
  property_count: 1
  slug: inspector-disable-delegated-admin-account-request-structure
- name: Inspector Disable Delegated Admin Account Response Structure
  property_count: 1
  slug: inspector-disable-delegated-admin-account-response-structure
- name: Inspector Disable Response Structure
  property_count: 2
  slug: inspector-disable-response-structure
- name: Inspector Disassociate Member Response Structure
  property_count: 1
  slug: inspector-disassociate-member-response-structure
- name: Inspector Ec2 Instance Aggregation Response Structure
  property_count: 7
  slug: inspector-ec2-instance-aggregation-response-structure
- name: Inspector Ec2 Instance Aggregation Structure
  property_count: 6
  slug: inspector-ec2-instance-aggregation-structure
- name: Inspector Ecr Rescan Duration Structure
  property_count: 0
  slug: inspector-ecr-rescan-duration-structure
- name: Inspector Enable Delegated Admin Account Response Structure
  property_count: 1
  slug: inspector-enable-delegated-admin-account-response-structure
- name: Inspector Enable Response Structure
  property_count: 2
  slug: inspector-enable-response-structure
- name: Inspector Failed Account List Structure
  property_count: 0
  slug: inspector-failed-account-list-structure
- name: Inspector Failed Member Account Ec2 Deep Inspection Status State List Structure
  property_count: 0
  slug: inspector-failed-member-account-ec2-deep-inspection-status-state-list-structure
- name: Inspector Filter Action Structure
  property_count: 0
  slug: inspector-filter-action-structure
- name: Inspector Filter Criteria Structure
  property_count: 42
  slug: inspector-filter-criteria-structure
- name: Inspector Finding Arn List Structure
  property_count: 0
  slug: inspector-finding-arn-list-structure
- name: Inspector Finding Details Error List Structure
  property_count: 0
  slug: inspector-finding-details-error-list-structure
- name: Inspector Finding Details Structure
  property_count: 0
  slug: inspector-finding-details-structure
- name: Inspector Finding Type Aggregation Response Structure
  property_count: 2
  slug: inspector-finding-type-aggregation-response-structure
- name: Inspector Finding Type Aggregation Structure
  property_count: 4
  slug: inspector-finding-type-aggregation-structure
- name: Inspector Free Trial Account Info List Structure
  property_count: 0
  slug: inspector-free-trial-account-info-list-structure
- name: Inspector Free Trial Info Error List Structure
  property_count: 0
  slug: inspector-free-trial-info-error-list-structure
- name: Inspector Get Configuration Response Structure
  property_count: 1
  slug: inspector-get-configuration-response-structure
- name: Inspector Get Delegated Admin Account Response Structure
  property_count: 1
  slug: inspector-get-delegated-admin-account-response-structure
- name: Inspector Get Ec2 Deep Inspection Configuration Response Structure
  property_count: 4
  slug: inspector-get-ec2-deep-inspection-configuration-response-structure
- name: Inspector Get Encryption Key Response Structure
  property_count: 1
  slug: inspector-get-encryption-key-response-structure
- name: Inspector Get Findings Report Status Response Structure
  property_count: 6
  slug: inspector-get-findings-report-status-response-structure
- name: Inspector Get Member Response Structure
  property_count: 1
  slug: inspector-get-member-response-structure
- name: Inspector Get Sbom Export Response Structure
  property_count: 7
  slug: inspector-get-sbom-export-response-structure
- name: Inspector Group Key Structure
  property_count: 0
  slug: inspector-group-key-structure
- name: Inspector Image Layer Aggregation Response Structure
  property_count: 5
  slug: inspector-image-layer-aggregation-response-structure
- name: Inspector Image Layer Aggregation Structure
  property_count: 5
  slug: inspector-image-layer-aggregation-structure
- name: Inspector Image Tag List Structure
  property_count: 0
  slug: inspector-image-tag-list-structure
- name: Inspector Ip V4 Address List Structure
  property_count: 0
  slug: inspector-ip-v4-address-list-structure
- name: Inspector Ip V6 Address List Structure
  property_count: 0
  slug: inspector-ip-v6-address-list-structure
- name: Inspector Lambda Function Aggregation Response Structure
  property_count: 7
  slug: inspector-lambda-function-aggregation-response-structure
- name: Inspector Lambda Function Aggregation Structure
  property_count: 6
  slug: inspector-lambda-function-aggregation-structure
- name: Inspector Lambda Layer Aggregation Response Structure
  property_count: 5
  slug: inspector-lambda-layer-aggregation-response-structure
- name: Inspector Lambda Layer Aggregation Structure
  property_count: 5
  slug: inspector-lambda-layer-aggregation-structure
- name: Inspector Lambda Vpc Config Structure
  property_count: 3
  slug: inspector-lambda-vpc-config-structure
- name: Inspector Layer List Structure
  property_count: 0
  slug: inspector-layer-list-structure
- name: Inspector List Account Permissions Response Structure
  property_count: 2
  slug: inspector-list-account-permissions-response-structure
- name: Inspector List Coverage Response Structure
  property_count: 2
  slug: inspector-list-coverage-response-structure
- name: Inspector List Coverage Statistics Response Structure
  property_count: 3
  slug: inspector-list-coverage-statistics-response-structure
- name: Inspector List Delegated Admin Accounts Response Structure
  property_count: 2
  slug: inspector-list-delegated-admin-accounts-response-structure
- name: Inspector List Filters Response Structure
  property_count: 2
  slug: inspector-list-filters-response-structure
- name: Inspector List Finding Aggregations Response Structure
  property_count: 3
  slug: inspector-list-finding-aggregations-response-structure
- name: Inspector List Findings Response Structure
  property_count: 2
  slug: inspector-list-findings-response-structure
- name: Inspector List Members Response Structure
  property_count: 2
  slug: inspector-list-members-response-structure
- name: Inspector List Tags For Resource Response Structure
  property_count: 1
  slug: inspector-list-tags-for-resource-response-structure
- name: Inspector List Usage Totals Response Structure
  property_count: 2
  slug: inspector-list-usage-totals-response-structure
- name: Inspector Map Filter List Structure
  property_count: 0
  slug: inspector-map-filter-list-structure
- name: Inspector Member Account Ec2 Deep Inspection Status List Structure
  property_count: 0
  slug: inspector-member-account-ec2-deep-inspection-status-list-structure
- name: Inspector Member Account Ec2 Deep Inspection Status State List Structure
  property_count: 0
  slug: inspector-member-account-ec2-deep-inspection-status-state-list-structure
- name: Inspector Member Account Ec2 Deep Inspection Status Structure
  property_count: 2
  slug: inspector-member-account-ec2-deep-inspection-status-structure
- name: Inspector Number Filter List Structure
  property_count: 0
  slug: inspector-number-filter-list-structure
- name: Inspector Package Aggregation Response Structure
  property_count: 3
  slug: inspector-package-aggregation-response-structure
- name: Inspector Package Aggregation Structure
  property_count: 3
  slug: inspector-package-aggregation-structure
- name: Inspector Package Filter List Structure
  property_count: 0
  slug: inspector-package-filter-list-structure
- name: Inspector Package Type Structure
  property_count: 0
  slug: inspector-package-type-structure
- name: Inspector Port Range Filter List Structure
  property_count: 0
  slug: inspector-port-range-filter-list-structure
- name: Inspector Reference Urls Structure
  property_count: 0
  slug: inspector-reference-urls-structure
- name: Inspector Relationship Status Structure
  property_count: 0
  slug: inspector-relationship-status-structure
- name: Inspector Report Format Structure
  property_count: 0
  slug: inspector-report-format-structure
- name: Inspector Repository Aggregation Response Structure
  property_count: 4
  slug: inspector-repository-aggregation-response-structure
- name: Inspector Repository Aggregation Structure
  property_count: 3
  slug: inspector-repository-aggregation-structure
- name: Inspector Reset Encryption Key Response Structure
  property_count: 0
  slug: inspector-reset-encryption-key-response-structure
- name: Inspector Resource Filter Criteria Structure
  property_count: 8
  slug: inspector-resource-filter-criteria-structure
- name: Inspector Resource Map Filter List Structure
  property_count: 0
  slug: inspector-resource-map-filter-list-structure
- name: Inspector Resource Scan Metadata Structure
  property_count: 4
  slug: inspector-resource-scan-metadata-structure
- name: Inspector Resource Scan Type Structure
  property_count: 0
  slug: inspector-resource-scan-type-structure
- name: Inspector Resource State Structure
  property_count: 4
  slug: inspector-resource-state-structure
- name: Inspector Resource Status Structure
  property_count: 4
  slug: inspector-resource-status-structure
- name: Inspector Resource String Filter List Structure
  property_count: 0
  slug: inspector-resource-string-filter-list-structure
- name: Inspector Runtime Structure
  property_count: 0
  slug: inspector-runtime-structure
- name: Inspector Sbom Report Format Structure
  property_count: 0
  slug: inspector-sbom-report-format-structure
- name: Inspector Scan Status Structure
  property_count: 2
  slug: inspector-scan-status-structure
- name: Inspector Scan Type Structure
  property_count: 0
  slug: inspector-scan-type-structure
- name: Inspector Search Vulnerabilities Response Structure
  property_count: 2
  slug: inspector-search-vulnerabilities-response-structure
- name: Inspector Severity Counts Structure
  property_count: 4
  slug: inspector-severity-counts-structure
- name: Inspector Sort Field Structure
  property_count: 0
  slug: inspector-sort-field-structure
- name: Inspector Sort Order Structure
  property_count: 0
  slug: inspector-sort-order-structure
- name: Inspector State Structure
  property_count: 3
  slug: inspector-state-structure
- name: Inspector Status Structure
  property_count: 0
  slug: inspector-status-structure
- name: Inspector String Filter List Structure
  property_count: 0
  slug: inspector-string-filter-list-structure
- name: Inspector String Filter Structure
  property_count: 2
  slug: inspector-string-filter-structure
- name: Inspector String List Structure
  property_count: 0
  slug: inspector-string-list-structure
- name: Inspector Suggested Fixes Structure
  property_count: 0
  slug: inspector-suggested-fixes-structure
- name: Inspector Tag Map Structure
  property_count: 0
  slug: inspector-tag-map-structure
- name: Inspector Tag Resource Response Structure
  property_count: 0
  slug: inspector-tag-resource-response-structure
- name: Inspector Targets Structure
  property_count: 0
  slug: inspector-targets-structure
- name: Inspector Title Aggregation Response Structure
  property_count: 4
  slug: inspector-title-aggregation-response-structure
- name: Inspector Title Aggregation Structure
  property_count: 6
  slug: inspector-title-aggregation-structure
- name: Inspector Ttps Structure
  property_count: 0
  slug: inspector-ttps-structure
- name: Inspector Untag Resource Response Structure
  property_count: 0
  slug: inspector-untag-resource-response-structure
- name: Inspector Update Configuration Response Structure
  property_count: 0
  slug: inspector-update-configuration-response-structure
- name: Inspector Update Ec2 Deep Inspection Configuration Response Structure
  property_count: 4
  slug: inspector-update-ec2-deep-inspection-configuration-response-structure
- name: Inspector Update Encryption Key Response Structure
  property_count: 0
  slug: inspector-update-encryption-key-response-structure
- name: Inspector Update Filter Response Structure
  property_count: 1
  slug: inspector-update-filter-response-structure
- name: Inspector Update Org Ec2 Deep Inspection Configuration Response Structure
  property_count: 0
  slug: inspector-update-org-ec2-deep-inspection-configuration-response-structure
- name: Inspector Update Organization Configuration Response Structure
  property_count: 1
  slug: inspector-update-organization-configuration-response-structure
- name: Inspector Vuln Id List Structure
  property_count: 0
  slug: inspector-vuln-id-list-structure
jsonld:
- class_count: 102
  name: Amazon Inspector Context
  property_count: 226
  slug: amazon-inspector-context
layout: provider
modified: '2026-05-19'
name: Amazon Inspector
nav: Providers
network: true
overview: 'Amazon Inspector publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Accountpermissions API, Codesnippet API, Configuration API, and 19 more. Tagged areas include Compliance, Container Security, EC2, Lambda, and Security.


  The Amazon Inspector catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Inspector''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 14 more developer resources.'
plans:
- name: Amazon Inspector Plans Pricing
  plan_count: 3
  slug: amazon-inspector-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 5
  name: Amazon Inspector Rate Limits
  slug: amazon-inspector-rate-limits
rules:
- name: Amazon Inspector API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-inspector-jsonschema-spectral-rules
- name: Amazon Inspector API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 10
  slug: amazon-inspector-spectral-rules
score:
  band: strong
  composite: 65.4
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 67.3
    developer_ergonomics: 41.3
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 65.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-inspector/refs/heads/main/screenshots/amazon-inspector-2026-06-20T171705.png
security:
- kind: authentication
  name: Amazon Inspector Authentication
  slug: amazon-inspector-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Inspector Domain Security
  slug: amazon-inspector-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Inspector Vulnerability Disclosure
  slug: amazon-inspector-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Inspector Trust Center
  slug: amazon-inspector-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-inspector
tags:
- Compliance
- Container Security
- EC2
- Lambda
- Security
- Vulnerability Scanning
use_cases:
- description: Automatically scan container images in ECR during build pipelines.
  name: CI/CD Security Scanning
- description: Generate vulnerability reports for SOC 2, PCI DSS compliance.
  name: Compliance Reporting
- description: Prioritize OS patches based on exploitability scores.
  name: Patch Prioritization
website: https://aws.amazon.com/inspector/
---
