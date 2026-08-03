---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 3
  name: Amazon Audit Manager Agentic Access
  operation_count: 22
  slug: amazon-audit-manager-agentic-access
  summary_line: 22 operations · 12 acting · 3 human-in-the-loop
api_count: 6
apis:
- description: Operations for creating and managing compliance assessments
  name: Amazon Audit Manager Assessments API
  slug: amazon-audit-manager-assessments-api
- description: Operations for managing compliance controls
  name: Amazon Audit Manager Controls API
  slug: amazon-audit-manager-controls-api
- description: Operations for managing audit evidence
  name: Amazon Audit Manager Evidence API
  slug: amazon-audit-manager-evidence-api
- description: Operations for managing compliance frameworks
  name: Amazon Audit Manager Frameworks API
  slug: amazon-audit-manager-frameworks-api
- description: Operations for generating assessment reports
  name: Amazon Audit Manager Reports API
  slug: amazon-audit-manager-reports-api
- description: Operations for configuring Audit Manager settings
  name: Amazon Audit Manager Settings API
  slug: amazon-audit-manager-settings-api
artifact_total: 225
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-audit-manager-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-audit-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-audit-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-audit-manager-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: https://raw.githubusercontent.com/api-evangelist/amazon-audit-manager/refs/heads/main/well-known/amazon-audit-manager-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://raw.githubusercontent.com/api-evangelist/amazon-audit-manager/refs/heads/main/well-known/amazon-audit-manager-security.txt
created: '2026-03-16'
description: AWS Audit Manager helps you continuously audit your AWS usage to simplify how you assess risk and compliance with regulations and industry standards.
examples:
- key_count: 3
  name: Audit Manager Assessment Control Example
  slug: audit-manager-assessment-control-example
- key_count: 3
  name: Audit Manager Assessment Control Set Example
  slug: audit-manager-assessment-control-set-example
- key_count: 3
  name: Audit Manager Assessment Example
  slug: audit-manager-assessment-example
- key_count: 3
  name: Audit Manager Assessment Framework Example
  slug: audit-manager-assessment-framework-example
- key_count: 3
  name: Audit Manager Assessment Framework Metadata Example
  slug: audit-manager-assessment-framework-metadata-example
- key_count: 3
  name: Audit Manager Assessment Metadata Example
  slug: audit-manager-assessment-metadata-example
- key_count: 3
  name: Audit Manager Assessment Metadata Item Example
  slug: audit-manager-assessment-metadata-item-example
- key_count: 3
  name: Audit Manager Assessment Report Example
  slug: audit-manager-assessment-report-example
- key_count: 3
  name: Audit Manager Assessment Report Metadata Example
  slug: audit-manager-assessment-report-metadata-example
- key_count: 3
  name: Audit Manager Assessment Reports Destination Example
  slug: audit-manager-assessment-reports-destination-example
- key_count: 3
  name: Audit Manager Aws Account Example
  slug: audit-manager-aws-account-example
- key_count: 3
  name: Audit Manager Aws Service Example
  slug: audit-manager-aws-service-example
- key_count: 3
  name: Audit Manager Control Comment Example
  slug: audit-manager-control-comment-example
- key_count: 3
  name: Audit Manager Control Example
  slug: audit-manager-control-example
- key_count: 3
  name: Audit Manager Control Mapping Source Example
  slug: audit-manager-control-mapping-source-example
- key_count: 3
  name: Audit Manager Control Metadata Example
  slug: audit-manager-control-metadata-example
- key_count: 3
  name: Audit Manager Control Set Example
  slug: audit-manager-control-set-example
- key_count: 3
  name: Audit Manager Create Assessment Framework Control Example
  slug: audit-manager-create-assessment-framework-control-example
- key_count: 3
  name: Audit Manager Create Assessment Framework Control Set Example
  slug: audit-manager-create-assessment-framework-control-set-example
- key_count: 3
  name: Audit Manager Create Assessment Framework Request Example
  slug: audit-manager-create-assessment-framework-request-example
- key_count: 3
  name: Audit Manager Create Assessment Framework Response Example
  slug: audit-manager-create-assessment-framework-response-example
- key_count: 3
  name: Audit Manager Create Assessment Report Request Example
  slug: audit-manager-create-assessment-report-request-example
- key_count: 3
  name: Audit Manager Create Assessment Report Response Example
  slug: audit-manager-create-assessment-report-response-example
- key_count: 3
  name: Audit Manager Create Assessment Request Example
  slug: audit-manager-create-assessment-request-example
- key_count: 3
  name: Audit Manager Create Assessment Response Example
  slug: audit-manager-create-assessment-response-example
- key_count: 3
  name: Audit Manager Create Control Mapping Source Example
  slug: audit-manager-create-control-mapping-source-example
- key_count: 3
  name: Audit Manager Create Control Request Example
  slug: audit-manager-create-control-request-example
- key_count: 3
  name: Audit Manager Create Control Response Example
  slug: audit-manager-create-control-response-example
- key_count: 3
  name: Audit Manager Delegation Example
  slug: audit-manager-delegation-example
- key_count: 3
  name: Audit Manager Delete Assessment Framework Response Example
  slug: audit-manager-delete-assessment-framework-response-example
- key_count: 3
  name: Audit Manager Delete Assessment Response Example
  slug: audit-manager-delete-assessment-response-example
- key_count: 3
  name: Audit Manager Delete Control Response Example
  slug: audit-manager-delete-control-response-example
- key_count: 3
  name: Audit Manager Evidence Example
  slug: audit-manager-evidence-example
- key_count: 3
  name: Audit Manager Evidence Folder Example
  slug: audit-manager-evidence-folder-example
- key_count: 3
  name: Audit Manager Framework Example
  slug: audit-manager-framework-example
- key_count: 3
  name: Audit Manager Framework Metadata Example
  slug: audit-manager-framework-metadata-example
- key_count: 3
  name: Audit Manager Get Assessment Framework Response Example
  slug: audit-manager-get-assessment-framework-response-example
- key_count: 3
  name: Audit Manager Get Assessment Response Example
  slug: audit-manager-get-assessment-response-example
- key_count: 3
  name: Audit Manager Get Control Response Example
  slug: audit-manager-get-control-response-example
- key_count: 3
  name: Audit Manager Get Evidence Folders By Assessment Control Response Example
  slug: audit-manager-get-evidence-folders-by-assessment-control-response-example
- key_count: 3
  name: Audit Manager Get Settings Response Example
  slug: audit-manager-get-settings-response-example
- key_count: 3
  name: Audit Manager List Assessment Frameworks Response Example
  slug: audit-manager-list-assessment-frameworks-response-example
- key_count: 3
  name: Audit Manager List Assessment Reports Response Example
  slug: audit-manager-list-assessment-reports-response-example
- key_count: 3
  name: Audit Manager List Assessments Response Example
  slug: audit-manager-list-assessments-response-example
- key_count: 3
  name: Audit Manager List Controls Response Example
  slug: audit-manager-list-controls-response-example
- key_count: 3
  name: Audit Manager List Evidence Response Example
  slug: audit-manager-list-evidence-response-example
- key_count: 3
  name: Audit Manager Resource Example
  slug: audit-manager-resource-example
- key_count: 3
  name: Audit Manager Role Example
  slug: audit-manager-role-example
- key_count: 3
  name: Audit Manager Scope Example
  slug: audit-manager-scope-example
- key_count: 3
  name: Audit Manager Settings Example
  slug: audit-manager-settings-example
- key_count: 3
  name: Audit Manager Source Keyword Example
  slug: audit-manager-source-keyword-example
- key_count: 3
  name: Audit Manager Update Assessment Framework Control Set Example
  slug: audit-manager-update-assessment-framework-control-set-example
- key_count: 3
  name: Audit Manager Update Assessment Framework Request Example
  slug: audit-manager-update-assessment-framework-request-example
- key_count: 3
  name: Audit Manager Update Assessment Framework Response Example
  slug: audit-manager-update-assessment-framework-response-example
- key_count: 3
  name: Audit Manager Update Assessment Request Example
  slug: audit-manager-update-assessment-request-example
- key_count: 3
  name: Audit Manager Update Assessment Response Example
  slug: audit-manager-update-assessment-response-example
- key_count: 3
  name: Audit Manager Update Assessment Status Request Example
  slug: audit-manager-update-assessment-status-request-example
- key_count: 3
  name: Audit Manager Update Assessment Status Response Example
  slug: audit-manager-update-assessment-status-response-example
- key_count: 3
  name: Audit Manager Update Control Request Example
  slug: audit-manager-update-control-request-example
- key_count: 3
  name: Audit Manager Update Control Response Example
  slug: audit-manager-update-control-response-example
- key_count: 3
  name: Audit Manager Update Settings Request Example
  slug: audit-manager-update-settings-request-example
- key_count: 3
  name: Audit Manager Update Settings Response Example
  slug: audit-manager-update-settings-response-example
features:
- Continuous compliance monitoring with automated evidence collection
- Pre-built frameworks for SOC 2, PCI DSS, HIPAA, GDPR, and more
- Custom framework and control creation for internal policies
- Automated evidence collection from AWS Config, Security Hub, and CloudTrail
- Evidence folder organization by control and control set
- Assessment delegation to process owners and resource owners
- Assessment report generation in PDF format
- Multi-account support through AWS Organizations
- Evidence finder for cross-assessment evidence search
- Integration with AWS Security Hub for security findings
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-audit-manager.png
integrations:
- AWS Config
- AWS Security Hub
- AWS CloudTrail
- AWS IAM
- Amazon S3
- Amazon SNS
- AWS Organizations
- AWS KMS
- Amazon CloudWatch
- AWS Systems Manager
json_schemas:
- name: AssessmentControl
  property_count: 0
  slug: audit-manager-assessment-control
- name: AssessmentControlSet
  property_count: 0
  slug: audit-manager-assessment-control-set
- name: AssessmentFrameworkMetadata
  property_count: 0
  slug: audit-manager-assessment-framework-metadata
- name: AssessmentFramework
  property_count: 0
  slug: audit-manager-assessment-framework
- name: AssessmentMetadataItem
  property_count: 0
  slug: audit-manager-assessment-metadata-item
- name: AssessmentMetadata
  property_count: 0
  slug: audit-manager-assessment-metadata
- name: AssessmentReportMetadata
  property_count: 0
  slug: audit-manager-assessment-report-metadata
- name: AssessmentReport
  property_count: 0
  slug: audit-manager-assessment-report
- name: AssessmentReportsDestination
  property_count: 0
  slug: audit-manager-assessment-reports-destination
- name: Assessment
  property_count: 0
  slug: audit-manager-assessment
- name: AWSAccount
  property_count: 0
  slug: audit-manager-aws-account
- name: AWSService
  property_count: 0
  slug: audit-manager-aws-service
- name: ControlComment
  property_count: 0
  slug: audit-manager-control-comment
- name: ControlMappingSource
  property_count: 0
  slug: audit-manager-control-mapping-source
- name: ControlMetadata
  property_count: 0
  slug: audit-manager-control-metadata
- name: Control
  property_count: 0
  slug: audit-manager-control
- name: ControlSet
  property_count: 0
  slug: audit-manager-control-set
- name: CreateAssessmentFrameworkControl
  property_count: 0
  slug: audit-manager-create-assessment-framework-control
- name: CreateAssessmentFrameworkControlSet
  property_count: 0
  slug: audit-manager-create-assessment-framework-control-set
- name: CreateAssessmentFrameworkRequest
  property_count: 0
  slug: audit-manager-create-assessment-framework-request
- name: CreateAssessmentFrameworkResponse
  property_count: 0
  slug: audit-manager-create-assessment-framework-response
- name: CreateAssessmentReportRequest
  property_count: 0
  slug: audit-manager-create-assessment-report-request
- name: CreateAssessmentReportResponse
  property_count: 0
  slug: audit-manager-create-assessment-report-response
- name: CreateAssessmentRequest
  property_count: 0
  slug: audit-manager-create-assessment-request
- name: CreateAssessmentResponse
  property_count: 0
  slug: audit-manager-create-assessment-response
- name: CreateControlMappingSource
  property_count: 0
  slug: audit-manager-create-control-mapping-source
- name: CreateControlRequest
  property_count: 0
  slug: audit-manager-create-control-request
- name: CreateControlResponse
  property_count: 0
  slug: audit-manager-create-control-response
- name: Delegation
  property_count: 0
  slug: audit-manager-delegation
- name: DeleteAssessmentFrameworkResponse
  property_count: 0
  slug: audit-manager-delete-assessment-framework-response
- name: DeleteAssessmentResponse
  property_count: 0
  slug: audit-manager-delete-assessment-response
- name: DeleteControlResponse
  property_count: 0
  slug: audit-manager-delete-control-response
- name: EvidenceFolder
  property_count: 0
  slug: audit-manager-evidence-folder
- name: Evidence
  property_count: 0
  slug: audit-manager-evidence
- name: FrameworkMetadata
  property_count: 0
  slug: audit-manager-framework-metadata
- name: Framework
  property_count: 0
  slug: audit-manager-framework
- name: GetAssessmentFrameworkResponse
  property_count: 0
  slug: audit-manager-get-assessment-framework-response
- name: GetAssessmentResponse
  property_count: 0
  slug: audit-manager-get-assessment-response
- name: GetControlResponse
  property_count: 0
  slug: audit-manager-get-control-response
- name: GetEvidenceFoldersByAssessmentControlResponse
  property_count: 0
  slug: audit-manager-get-evidence-folders-by-assessment-control-response
- name: GetSettingsResponse
  property_count: 0
  slug: audit-manager-get-settings-response
- name: ListAssessmentFrameworksResponse
  property_count: 0
  slug: audit-manager-list-assessment-frameworks-response
- name: ListAssessmentReportsResponse
  property_count: 0
  slug: audit-manager-list-assessment-reports-response
- name: ListAssessmentsResponse
  property_count: 0
  slug: audit-manager-list-assessments-response
- name: ListControlsResponse
  property_count: 0
  slug: audit-manager-list-controls-response
- name: ListEvidenceResponse
  property_count: 0
  slug: audit-manager-list-evidence-response
- name: Resource
  property_count: 0
  slug: audit-manager-resource
- name: Role
  property_count: 0
  slug: audit-manager-role
- name: Scope
  property_count: 0
  slug: audit-manager-scope
- name: Settings
  property_count: 0
  slug: audit-manager-settings
- name: SourceKeyword
  property_count: 0
  slug: audit-manager-source-keyword
- name: UpdateAssessmentFrameworkControlSet
  property_count: 0
  slug: audit-manager-update-assessment-framework-control-set
- name: UpdateAssessmentFrameworkRequest
  property_count: 0
  slug: audit-manager-update-assessment-framework-request
- name: UpdateAssessmentFrameworkResponse
  property_count: 0
  slug: audit-manager-update-assessment-framework-response
- name: UpdateAssessmentRequest
  property_count: 0
  slug: audit-manager-update-assessment-request
- name: UpdateAssessmentResponse
  property_count: 0
  slug: audit-manager-update-assessment-response
- name: UpdateAssessmentStatusRequest
  property_count: 0
  slug: audit-manager-update-assessment-status-request
- name: UpdateAssessmentStatusResponse
  property_count: 0
  slug: audit-manager-update-assessment-status-response
- name: UpdateControlRequest
  property_count: 0
  slug: audit-manager-update-control-request
- name: UpdateControlResponse
  property_count: 0
  slug: audit-manager-update-control-response
- name: UpdateSettingsRequest
  property_count: 0
  slug: audit-manager-update-settings-request
- name: UpdateSettingsResponse
  property_count: 0
  slug: audit-manager-update-settings-response
json_structures:
- name: Audit Manager Assessment Control Set Structure
  property_count: 0
  slug: audit-manager-assessment-control-set-structure
- name: Audit Manager Assessment Control Structure
  property_count: 0
  slug: audit-manager-assessment-control-structure
- name: Audit Manager Assessment Framework Metadata Structure
  property_count: 0
  slug: audit-manager-assessment-framework-metadata-structure
- name: Audit Manager Assessment Framework Structure
  property_count: 0
  slug: audit-manager-assessment-framework-structure
- name: Audit Manager Assessment Metadata Item Structure
  property_count: 0
  slug: audit-manager-assessment-metadata-item-structure
- name: Audit Manager Assessment Metadata Structure
  property_count: 0
  slug: audit-manager-assessment-metadata-structure
- name: Audit Manager Assessment Report Metadata Structure
  property_count: 0
  slug: audit-manager-assessment-report-metadata-structure
- name: Audit Manager Assessment Report Structure
  property_count: 0
  slug: audit-manager-assessment-report-structure
- name: Audit Manager Assessment Reports Destination Structure
  property_count: 0
  slug: audit-manager-assessment-reports-destination-structure
- name: Audit Manager Assessment Structure
  property_count: 0
  slug: audit-manager-assessment-structure
- name: Audit Manager Aws Account Structure
  property_count: 0
  slug: audit-manager-aws-account-structure
- name: Audit Manager Aws Service Structure
  property_count: 0
  slug: audit-manager-aws-service-structure
- name: Audit Manager Control Comment Structure
  property_count: 0
  slug: audit-manager-control-comment-structure
- name: Audit Manager Control Mapping Source Structure
  property_count: 0
  slug: audit-manager-control-mapping-source-structure
- name: Audit Manager Control Metadata Structure
  property_count: 0
  slug: audit-manager-control-metadata-structure
- name: Audit Manager Control Set Structure
  property_count: 0
  slug: audit-manager-control-set-structure
- name: Audit Manager Control Structure
  property_count: 0
  slug: audit-manager-control-structure
- name: Audit Manager Create Assessment Framework Control Set Structure
  property_count: 0
  slug: audit-manager-create-assessment-framework-control-set-structure
- name: Audit Manager Create Assessment Framework Control Structure
  property_count: 0
  slug: audit-manager-create-assessment-framework-control-structure
- name: Audit Manager Create Assessment Framework Request Structure
  property_count: 0
  slug: audit-manager-create-assessment-framework-request-structure
- name: Audit Manager Create Assessment Framework Response Structure
  property_count: 0
  slug: audit-manager-create-assessment-framework-response-structure
- name: Audit Manager Create Assessment Report Request Structure
  property_count: 0
  slug: audit-manager-create-assessment-report-request-structure
- name: Audit Manager Create Assessment Report Response Structure
  property_count: 0
  slug: audit-manager-create-assessment-report-response-structure
- name: Audit Manager Create Assessment Request Structure
  property_count: 0
  slug: audit-manager-create-assessment-request-structure
- name: Audit Manager Create Assessment Response Structure
  property_count: 0
  slug: audit-manager-create-assessment-response-structure
- name: Audit Manager Create Control Mapping Source Structure
  property_count: 0
  slug: audit-manager-create-control-mapping-source-structure
- name: Audit Manager Create Control Request Structure
  property_count: 0
  slug: audit-manager-create-control-request-structure
- name: Audit Manager Create Control Response Structure
  property_count: 0
  slug: audit-manager-create-control-response-structure
- name: Audit Manager Delegation Structure
  property_count: 0
  slug: audit-manager-delegation-structure
- name: Audit Manager Delete Assessment Framework Response Structure
  property_count: 0
  slug: audit-manager-delete-assessment-framework-response-structure
- name: Audit Manager Delete Assessment Response Structure
  property_count: 0
  slug: audit-manager-delete-assessment-response-structure
- name: Audit Manager Delete Control Response Structure
  property_count: 0
  slug: audit-manager-delete-control-response-structure
- name: Audit Manager Evidence Folder Structure
  property_count: 0
  slug: audit-manager-evidence-folder-structure
- name: Audit Manager Evidence Structure
  property_count: 0
  slug: audit-manager-evidence-structure
- name: Audit Manager Framework Metadata Structure
  property_count: 0
  slug: audit-manager-framework-metadata-structure
- name: Audit Manager Framework Structure
  property_count: 0
  slug: audit-manager-framework-structure
- name: Audit Manager Get Assessment Framework Response Structure
  property_count: 0
  slug: audit-manager-get-assessment-framework-response-structure
- name: Audit Manager Get Assessment Response Structure
  property_count: 0
  slug: audit-manager-get-assessment-response-structure
- name: Audit Manager Get Control Response Structure
  property_count: 0
  slug: audit-manager-get-control-response-structure
- name: Audit Manager Get Evidence Folders By Assessment Control Response Structure
  property_count: 0
  slug: audit-manager-get-evidence-folders-by-assessment-control-response-structure
- name: Audit Manager Get Settings Response Structure
  property_count: 0
  slug: audit-manager-get-settings-response-structure
- name: Audit Manager List Assessment Frameworks Response Structure
  property_count: 0
  slug: audit-manager-list-assessment-frameworks-response-structure
- name: Audit Manager List Assessment Reports Response Structure
  property_count: 0
  slug: audit-manager-list-assessment-reports-response-structure
- name: Audit Manager List Assessments Response Structure
  property_count: 0
  slug: audit-manager-list-assessments-response-structure
- name: Audit Manager List Controls Response Structure
  property_count: 0
  slug: audit-manager-list-controls-response-structure
- name: Audit Manager List Evidence Response Structure
  property_count: 0
  slug: audit-manager-list-evidence-response-structure
- name: Audit Manager Resource Structure
  property_count: 0
  slug: audit-manager-resource-structure
- name: Audit Manager Role Structure
  property_count: 0
  slug: audit-manager-role-structure
- name: Audit Manager Scope Structure
  property_count: 0
  slug: audit-manager-scope-structure
- name: Audit Manager Settings Structure
  property_count: 0
  slug: audit-manager-settings-structure
- name: Audit Manager Source Keyword Structure
  property_count: 0
  slug: audit-manager-source-keyword-structure
- name: Audit Manager Update Assessment Framework Control Set Structure
  property_count: 0
  slug: audit-manager-update-assessment-framework-control-set-structure
- name: Audit Manager Update Assessment Framework Request Structure
  property_count: 0
  slug: audit-manager-update-assessment-framework-request-structure
- name: Audit Manager Update Assessment Framework Response Structure
  property_count: 0
  slug: audit-manager-update-assessment-framework-response-structure
- name: Audit Manager Update Assessment Request Structure
  property_count: 0
  slug: audit-manager-update-assessment-request-structure
- name: Audit Manager Update Assessment Response Structure
  property_count: 0
  slug: audit-manager-update-assessment-response-structure
- name: Audit Manager Update Assessment Status Request Structure
  property_count: 0
  slug: audit-manager-update-assessment-status-request-structure
- name: Audit Manager Update Assessment Status Response Structure
  property_count: 0
  slug: audit-manager-update-assessment-status-response-structure
- name: Audit Manager Update Control Request Structure
  property_count: 0
  slug: audit-manager-update-control-request-structure
- name: Audit Manager Update Control Response Structure
  property_count: 0
  slug: audit-manager-update-control-response-structure
- name: Audit Manager Update Settings Request Structure
  property_count: 0
  slug: audit-manager-update-settings-request-structure
- name: Audit Manager Update Settings Response Structure
  property_count: 0
  slug: audit-manager-update-settings-response-structure
jsonld:
- class_count: 6
  name: Amazon Audit Manager Context
  property_count: 0
  slug: amazon-audit-manager-context
layout: provider
modified: '2026-06-20'
name: Amazon Audit Manager
nav: Providers
network: true
overview: 'Amazon Audit Manager publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Assessments API, Controls API, Evidence API, and 3 more. Tagged areas include Amazon Audit Manager, Compliance, Audit, and Risk Management.


  The Amazon Audit Manager catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Audit Manager''s developer surface includes authentication and 5 more developer resources.'
random_paper: 7
rules:
- name: Amazon Audit Manager API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-audit-manager-jsonschema-spectral-rules
- name: Amazon Audit Manager API Rules
  rule_count: 23
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 11
  slug: amazon-audit-manager-spectral-rules
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 79.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 69.8
    operational_transparency: 0.0
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-audit-manager/refs/heads/main/screenshots/amazon-audit-manager-2026-07-25T195931.png
security:
- kind: authentication
  name: Amazon Audit Manager Authentication
  slug: amazon-audit-manager-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Audit Manager Domain Security
  slug: amazon-audit-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Audit Manager Vulnerability Disclosure
  slug: amazon-audit-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amazon-audit-manager
tags:
- Amazon Audit Manager
- Compliance
- Audit
- Risk Management
use_cases:
- Automate SOC 2 compliance evidence collection
- Prepare for PCI DSS and HIPAA audits with continuous monitoring
- Build custom compliance frameworks for internal policies
- Delegate control reviews to business process owners
- Generate audit-ready reports for external auditors
- Monitor compliance posture across multiple AWS accounts
---
