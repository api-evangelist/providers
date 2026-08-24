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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Amazon Codeguru Security Agentic Access
  operation_count: 13
  slug: amazon-codeguru-security-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 8
apis:
- description: The AccountConfiguration API from Amazon CodeGuru Security — 1 operation(s) for accountconfiguration.
  name: Amazon CodeGuru Security AccountConfiguration API
  slug: amazon-codeguru-security-accountconfiguration-api
- description: The BatchGetFindings API from Amazon CodeGuru Security — 1 operation(s) for batchgetfindings.
  name: Amazon CodeGuru Security BatchGetFindings API
  slug: amazon-codeguru-security-batchgetfindings-api
- description: The Findings API from Amazon CodeGuru Security — 1 operation(s) for findings.
  name: Amazon CodeGuru Security Findings API
  slug: amazon-codeguru-security-findings-api
- description: The Metrics API from Amazon CodeGuru Security — 2 operation(s) for metrics.
  name: Amazon CodeGuru Security Metrics API
  slug: amazon-codeguru-security-metrics-api
- description: The Scans API from Amazon CodeGuru Security — 2 operation(s) for scans.
  name: Amazon CodeGuru Security Scans API
  slug: amazon-codeguru-security-scans-api
- description: The Tags API from Amazon CodeGuru Security — 2 operation(s) for tags.
  name: Amazon CodeGuru Security Tags API
  slug: amazon-codeguru-security-tags-api
- description: The UpdateAccountConfiguration API from Amazon CodeGuru Security — 1 operation(s) for updateaccountconfiguration.
  name: Amazon CodeGuru Security UpdateAccountConfiguration API
  slug: amazon-codeguru-security-updateaccountconfiguration-api
- description: The UploadUrl API from Amazon CodeGuru Security — 1 operation(s) for uploadurl.
  name: Amazon CodeGuru Security UploadUrl API
  slug: amazon-codeguru-security-uploadurl-api
artifact_total: 262
collections:
- collection_type: postman
  name: Amazon CodeGuru Security AccountConfiguration API
  slug: postman-amazon-codeguru-security-accountconfiguration-api
- collection_type: postman
  name: Amazon CodeGuru Security AccountConfiguration BatchGetFindings API
  slug: postman-amazon-codeguru-security-batchgetfindings-api
- collection_type: postman
  name: Amazon CodeGuru Security AccountConfiguration Findings API
  slug: postman-amazon-codeguru-security-findings-api
- collection_type: postman
  name: Amazon CodeGuru Security AccountConfiguration Metrics API
  slug: postman-amazon-codeguru-security-metrics-api
- collection_type: postman
  name: Amazon CodeGuru Security AccountConfiguration Scans API
  slug: postman-amazon-codeguru-security-scans-api
- collection_type: postman
  name: Amazon CodeGuru Security AccountConfiguration Tags API
  slug: postman-amazon-codeguru-security-tags-api
- collection_type: postman
  name: Amazon CodeGuru Security AccountConfiguration UpdateAccountConfiguration API
  slug: postman-amazon-codeguru-security-updateaccountconfiguration-api
- collection_type: postman
  name: Amazon CodeGuru Security AccountConfiguration UploadUrl API
  slug: postman-amazon-codeguru-security-uploadurl-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon CodeGuru Security AccountConfiguration API
  slug: open-amazon-codeguru-security-accountconfiguration-api
- collection_type: open
  name: Amazon CodeGuru Security AccountConfiguration BatchGetFindings API
  slug: open-amazon-codeguru-security-batchgetfindings-api
- collection_type: open
  name: Amazon CodeGuru Security AccountConfiguration Findings API
  slug: open-amazon-codeguru-security-findings-api
- collection_type: open
  name: Amazon CodeGuru Security AccountConfiguration Metrics API
  slug: open-amazon-codeguru-security-metrics-api
- collection_type: open
  name: Amazon CodeGuru Security AccountConfiguration Scans API
  slug: open-amazon-codeguru-security-scans-api
- collection_type: open
  name: Amazon CodeGuru Security AccountConfiguration Tags API
  slug: open-amazon-codeguru-security-tags-api
- collection_type: open
  name: Amazon CodeGuru Security AccountConfiguration UpdateAccountConfiguration API
  slug: open-amazon-codeguru-security-updateaccountconfiguration-api
- collection_type: open
  name: Amazon CodeGuru Security AccountConfiguration UploadUrl API
  slug: open-amazon-codeguru-security-uploadurl-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-codeguru-security-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-codeguru-security/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-codeguru-security-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-codeguru-security-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-codeguru-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-codeguru-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-codeguru-security-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/codeguru/security
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/codegurusecurity/pricing/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/codegurusecurity/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/codegurusecurity/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/codegurusecurity/
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
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/devops/
- group: start
  title: ''
  type: SignUp
  url: https://portal.aws.amazon.com/gp/aws/developer/registration/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-codeguru-security-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-codeguru-security-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-codeguru-security-context.jsonld
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-codeguru-security-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-codeguru-security-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-codeguru-security-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-codeguru-security-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-codeguru-security-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-codeguru-security-lifecycle.yml
created: '2026-03-16'
description: Amazon CodeGuru Security is a static application security testing (SAST) service that uses machine learning to detect security vulnerabilities in your code. It identifies vulnerabilities such as injection flaws, data exposure risks, and infrastructure-as-code misconfigurations, and provides actionable remediation guidance to help developers fix security issues quickly.
examples:
- key_count: 5
  name: Amazon Codeguru Security Account Findings Metric Example
  slug: amazon-codeguru-security-account-findings-metric-example
- key_count: 4
  name: Amazon Codeguru Security Batch Get Findings Error Example
  slug: amazon-codeguru-security-batch-get-findings-error-example
- key_count: 1
  name: Amazon Codeguru Security Batch Get Findings Request Example
  slug: amazon-codeguru-security-batch-get-findings-request-example
- key_count: 2
  name: Amazon Codeguru Security Batch Get Findings Response Example
  slug: amazon-codeguru-security-batch-get-findings-response-example
- key_count: 2
  name: Amazon Codeguru Security Category With Finding Num Example
  slug: amazon-codeguru-security-category-with-finding-num-example
- key_count: 2
  name: Amazon Codeguru Security Code Line Example
  slug: amazon-codeguru-security-code-line-example
- key_count: 6
  name: Amazon Codeguru Security Create Scan Request Example
  slug: amazon-codeguru-security-create-scan-request-example
- key_count: 5
  name: Amazon Codeguru Security Create Scan Response Example
  slug: amazon-codeguru-security-create-scan-response-example
- key_count: 1
  name: Amazon Codeguru Security Create Upload Url Request Example
  slug: amazon-codeguru-security-create-upload-url-request-example
- key_count: 3
  name: Amazon Codeguru Security Create Upload Url Response Example
  slug: amazon-codeguru-security-create-upload-url-response-example
- key_count: 1
  name: Amazon Codeguru Security Encryption Config Example
  slug: amazon-codeguru-security-encryption-config-example
- key_count: 5
  name: Amazon Codeguru Security File Path Example
  slug: amazon-codeguru-security-file-path-example
- key_count: 8
  name: Amazon Codeguru Security Finding Example
  slug: amazon-codeguru-security-finding-example
- key_count: 2
  name: Amazon Codeguru Security Finding Identifier Example
  slug: amazon-codeguru-security-finding-identifier-example
- key_count: 5
  name: Amazon Codeguru Security Finding Metrics Value Per Severity Example
  slug: amazon-codeguru-security-finding-metrics-value-per-severity-example
- key_count: 0
  name: Amazon Codeguru Security Get Account Configuration Request Example
  slug: amazon-codeguru-security-get-account-configuration-request-example
- key_count: 1
  name: Amazon Codeguru Security Get Account Configuration Response Example
  slug: amazon-codeguru-security-get-account-configuration-response-example
- key_count: 0
  name: Amazon Codeguru Security Get Findings Request Example
  slug: amazon-codeguru-security-get-findings-request-example
- key_count: 2
  name: Amazon Codeguru Security Get Findings Response Example
  slug: amazon-codeguru-security-get-findings-response-example
- key_count: 0
  name: Amazon Codeguru Security Get Metrics Summary Request Example
  slug: amazon-codeguru-security-get-metrics-summary-request-example
- key_count: 1
  name: Amazon Codeguru Security Get Metrics Summary Response Example
  slug: amazon-codeguru-security-get-metrics-summary-response-example
- key_count: 0
  name: Amazon Codeguru Security Get Scan Request Example
  slug: amazon-codeguru-security-get-scan-request-example
- key_count: 8
  name: Amazon Codeguru Security Get Scan Response Example
  slug: amazon-codeguru-security-get-scan-response-example
- key_count: 0
  name: Amazon Codeguru Security List Findings Metrics Request Example
  slug: amazon-codeguru-security-list-findings-metrics-request-example
- key_count: 2
  name: Amazon Codeguru Security List Findings Metrics Response Example
  slug: amazon-codeguru-security-list-findings-metrics-response-example
- key_count: 0
  name: Amazon Codeguru Security List Scans Request Example
  slug: amazon-codeguru-security-list-scans-request-example
- key_count: 2
  name: Amazon Codeguru Security List Scans Response Example
  slug: amazon-codeguru-security-list-scans-response-example
- key_count: 0
  name: Amazon Codeguru Security List Tags For Resource Request Example
  slug: amazon-codeguru-security-list-tags-for-resource-request-example
- key_count: 1
  name: Amazon Codeguru Security List Tags For Resource Response Example
  slug: amazon-codeguru-security-list-tags-for-resource-response-example
- key_count: 5
  name: Amazon Codeguru Security Metrics Summary Example
  slug: amazon-codeguru-security-metrics-summary-example
- key_count: 2
  name: Amazon Codeguru Security Recommendation Example
  slug: amazon-codeguru-security-recommendation-example
- key_count: 2
  name: Amazon Codeguru Security Remediation Example
  slug: amazon-codeguru-security-remediation-example
- key_count: 0
  name: Amazon Codeguru Security Request Header Map Example
  slug: amazon-codeguru-security-request-header-map-example
- key_count: 2
  name: Amazon Codeguru Security Resource Example
  slug: amazon-codeguru-security-resource-example
- key_count: 1
  name: Amazon Codeguru Security Resource Id Example
  slug: amazon-codeguru-security-resource-id-example
- key_count: 2
  name: Amazon Codeguru Security Scan Name With Finding Num Example
  slug: amazon-codeguru-security-scan-name-with-finding-num-example
- key_count: 6
  name: Amazon Codeguru Security Scan Summary Example
  slug: amazon-codeguru-security-scan-summary-example
- key_count: 2
  name: Amazon Codeguru Security Suggested Fix Example
  slug: amazon-codeguru-security-suggested-fix-example
- key_count: 0
  name: Amazon Codeguru Security Tag Map Example
  slug: amazon-codeguru-security-tag-map-example
- key_count: 1
  name: Amazon Codeguru Security Tag Resource Request Example
  slug: amazon-codeguru-security-tag-resource-request-example
- key_count: 0
  name: Amazon Codeguru Security Tag Resource Response Example
  slug: amazon-codeguru-security-tag-resource-response-example
- key_count: 0
  name: Amazon Codeguru Security Untag Resource Request Example
  slug: amazon-codeguru-security-untag-resource-request-example
- key_count: 0
  name: Amazon Codeguru Security Untag Resource Response Example
  slug: amazon-codeguru-security-untag-resource-response-example
- key_count: 1
  name: Amazon Codeguru Security Update Account Configuration Request Example
  slug: amazon-codeguru-security-update-account-configuration-request-example
- key_count: 1
  name: Amazon Codeguru Security Update Account Configuration Response Example
  slug: amazon-codeguru-security-update-account-configuration-response-example
- key_count: 5
  name: Amazon Codeguru Security Vulnerability Example
  slug: amazon-codeguru-security-vulnerability-example
features:
- description: Analyze source code for security vulnerabilities without running the application using machine learning-powered SAST.
  name: Static Application Security Testing
- description: Detect security issues in Java, Python, JavaScript, TypeScript, C, C++, C#, Go, Ruby, and Kotlin code.
  name: Multi-Language Support
- description: Detect security misconfigurations in CloudFormation, Terraform, CDK, and other IaC templates.
  name: Infrastructure-as-Code Scanning
- description: Classify findings by severity (Critical, High, Medium, Low, Informational) to help prioritize remediation.
  name: Severity Classification
- description: Provide detailed remediation recommendations including suggested code fixes for each identified vulnerability.
  name: Remediation Guidance
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-codeguru-security.png
integrations:
- description: Run security scans as part of CodeBuild build projects for CI/CD integration.
  name: AWS CodeBuild
- description: Add CodeGuru Security scanning to GitHub Actions workflows.
  name: GitHub Actions
- description: Send security findings to Security Hub for centralized security management.
  name: AWS Security Hub
- description: Store and retrieve code bundles for security scanning from S3.
  name: Amazon S3
json_schemas:
- name: AccountFindingsMetric
  property_count: 5
  slug: amazon-codeguru-security-account-findings-metric
- name: AnalysisType
  property_count: 0
  slug: amazon-codeguru-security-analysis-type
- name: BatchGetFindingsError
  property_count: 4
  slug: amazon-codeguru-security-batch-get-findings-error
- name: BatchGetFindingsErrors
  property_count: 0
  slug: amazon-codeguru-security-batch-get-findings-errors
- name: BatchGetFindingsRequest
  property_count: 1
  slug: amazon-codeguru-security-batch-get-findings-request
- name: BatchGetFindingsResponse
  property_count: 2
  slug: amazon-codeguru-security-batch-get-findings-response
- name: CategoriesWithMostFindings
  property_count: 0
  slug: amazon-codeguru-security-categories-with-most-findings
- name: CategoryWithFindingNum
  property_count: 2
  slug: amazon-codeguru-security-category-with-finding-num
- name: ClientToken
  property_count: 0
  slug: amazon-codeguru-security-client-token
- name: CodeLine
  property_count: 2
  slug: amazon-codeguru-security-code-line
- name: CodeSnippet
  property_count: 0
  slug: amazon-codeguru-security-code-snippet
- name: CreateScanRequest
  property_count: 6
  slug: amazon-codeguru-security-create-scan-request
- name: CreateScanResponse
  property_count: 5
  slug: amazon-codeguru-security-create-scan-response
- name: CreateUploadUrlRequest
  property_count: 1
  slug: amazon-codeguru-security-create-upload-url-request
- name: CreateUploadUrlResponse
  property_count: 3
  slug: amazon-codeguru-security-create-upload-url-response
- name: DetectorTags
  property_count: 0
  slug: amazon-codeguru-security-detector-tags
- name: Double
  property_count: 0
  slug: amazon-codeguru-security-double
- name: EncryptionConfig
  property_count: 1
  slug: amazon-codeguru-security-encryption-config
- name: ErrorCode
  property_count: 0
  slug: amazon-codeguru-security-error-code
- name: FilePath
  property_count: 5
  slug: amazon-codeguru-security-file-path
- name: FindingIdentifier
  property_count: 2
  slug: amazon-codeguru-security-finding-identifier
- name: FindingIdentifiers
  property_count: 0
  slug: amazon-codeguru-security-finding-identifiers
- name: FindingMetricsValuePerSeverity
  property_count: 5
  slug: amazon-codeguru-security-finding-metrics-value-per-severity
- name: Finding
  property_count: 16
  slug: amazon-codeguru-security-finding
- name: FindingsMetricList
  property_count: 0
  slug: amazon-codeguru-security-findings-metric-list
- name: Findings
  property_count: 0
  slug: amazon-codeguru-security-findings
- name: GetAccountConfigurationRequest
  property_count: 0
  slug: amazon-codeguru-security-get-account-configuration-request
- name: GetAccountConfigurationResponse
  property_count: 1
  slug: amazon-codeguru-security-get-account-configuration-response
- name: GetFindingsRequestMaxResultsInteger
  property_count: 0
  slug: amazon-codeguru-security-get-findings-request-max-results-integer
- name: GetFindingsRequest
  property_count: 0
  slug: amazon-codeguru-security-get-findings-request
- name: GetFindingsResponse
  property_count: 2
  slug: amazon-codeguru-security-get-findings-response
- name: GetMetricsSummaryRequest
  property_count: 0
  slug: amazon-codeguru-security-get-metrics-summary-request
- name: GetMetricsSummaryResponse
  property_count: 1
  slug: amazon-codeguru-security-get-metrics-summary-response
- name: GetScanRequest
  property_count: 0
  slug: amazon-codeguru-security-get-scan-request
- name: GetScanResponse
  property_count: 8
  slug: amazon-codeguru-security-get-scan-response
- name: HeaderKey
  property_count: 0
  slug: amazon-codeguru-security-header-key
- name: HeaderValue
  property_count: 0
  slug: amazon-codeguru-security-header-value
- name: Integer
  property_count: 0
  slug: amazon-codeguru-security-integer
- name: KmsKeyArn
  property_count: 0
  slug: amazon-codeguru-security-kms-key-arn
- name: ListFindingsMetricsRequestMaxResultsInteger
  property_count: 0
  slug: amazon-codeguru-security-list-findings-metrics-request-max-results-integer
- name: ListFindingsMetricsRequest
  property_count: 0
  slug: amazon-codeguru-security-list-findings-metrics-request
- name: ListFindingsMetricsResponse
  property_count: 2
  slug: amazon-codeguru-security-list-findings-metrics-response
- name: ListScansRequestMaxResultsInteger
  property_count: 0
  slug: amazon-codeguru-security-list-scans-request-max-results-integer
- name: ListScansRequest
  property_count: 0
  slug: amazon-codeguru-security-list-scans-request
- name: ListScansResponse
  property_count: 2
  slug: amazon-codeguru-security-list-scans-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: amazon-codeguru-security-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: amazon-codeguru-security-list-tags-for-resource-response
- name: Long
  property_count: 0
  slug: amazon-codeguru-security-long
- name: MetricsSummary
  property_count: 5
  slug: amazon-codeguru-security-metrics-summary
- name: NextToken
  property_count: 0
  slug: amazon-codeguru-security-next-token
- name: Recommendation
  property_count: 2
  slug: amazon-codeguru-security-recommendation
- name: ReferenceUrls
  property_count: 0
  slug: amazon-codeguru-security-reference-urls
- name: RelatedVulnerabilities
  property_count: 0
  slug: amazon-codeguru-security-related-vulnerabilities
- name: Remediation
  property_count: 2
  slug: amazon-codeguru-security-remediation
- name: RequestHeaderMap
  property_count: 0
  slug: amazon-codeguru-security-request-header-map
- name: ResourceId
  property_count: 1
  slug: amazon-codeguru-security-resource-id
- name: Resource
  property_count: 2
  slug: amazon-codeguru-security-resource
- name: S3Url
  property_count: 0
  slug: amazon-codeguru-security-s3-url
- name: ScanNameArn
  property_count: 0
  slug: amazon-codeguru-security-scan-name-arn
- name: ScanName
  property_count: 0
  slug: amazon-codeguru-security-scan-name
- name: ScanNameWithFindingNum
  property_count: 2
  slug: amazon-codeguru-security-scan-name-with-finding-num
- name: ScanState
  property_count: 0
  slug: amazon-codeguru-security-scan-state
- name: ScanSummaries
  property_count: 0
  slug: amazon-codeguru-security-scan-summaries
- name: ScanSummary
  property_count: 6
  slug: amazon-codeguru-security-scan-summary
- name: ScanType
  property_count: 0
  slug: amazon-codeguru-security-scan-type
- name: ScansWithMostOpenCriticalFindings
  property_count: 0
  slug: amazon-codeguru-security-scans-with-most-open-critical-findings
- name: ScansWithMostOpenFindings
  property_count: 0
  slug: amazon-codeguru-security-scans-with-most-open-findings
- name: Severity
  property_count: 0
  slug: amazon-codeguru-security-severity
- name: Status
  property_count: 0
  slug: amazon-codeguru-security-status
- name: String
  property_count: 0
  slug: amazon-codeguru-security-string
- name: SuggestedFix
  property_count: 2
  slug: amazon-codeguru-security-suggested-fix
- name: SuggestedFixes
  property_count: 0
  slug: amazon-codeguru-security-suggested-fixes
- name: TagKeyList
  property_count: 0
  slug: amazon-codeguru-security-tag-key-list
- name: TagKey
  property_count: 0
  slug: amazon-codeguru-security-tag-key
- name: TagMap
  property_count: 0
  slug: amazon-codeguru-security-tag-map
- name: TagResourceRequest
  property_count: 1
  slug: amazon-codeguru-security-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: amazon-codeguru-security-tag-resource-response
- name: TagValue
  property_count: 0
  slug: amazon-codeguru-security-tag-value
- name: Timestamp
  property_count: 0
  slug: amazon-codeguru-security-timestamp
- name: UntagResourceRequest
  property_count: 0
  slug: amazon-codeguru-security-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: amazon-codeguru-security-untag-resource-response
- name: UpdateAccountConfigurationRequest
  property_count: 1
  slug: amazon-codeguru-security-update-account-configuration-request
- name: UpdateAccountConfigurationResponse
  property_count: 1
  slug: amazon-codeguru-security-update-account-configuration-response
- name: Uuid
  property_count: 0
  slug: amazon-codeguru-security-uuid
- name: Vulnerability
  property_count: 5
  slug: amazon-codeguru-security-vulnerability
json_structures:
- name: Amazon Codeguru Security Account Findings Metric Structure
  property_count: 5
  slug: amazon-codeguru-security-account-findings-metric-structure
- name: Amazon Codeguru Security Analysis Type Structure
  property_count: 0
  slug: amazon-codeguru-security-analysis-type-structure
- name: Amazon Codeguru Security Batch Get Findings Error Structure
  property_count: 4
  slug: amazon-codeguru-security-batch-get-findings-error-structure
- name: Amazon Codeguru Security Batch Get Findings Errors Structure
  property_count: 0
  slug: amazon-codeguru-security-batch-get-findings-errors-structure
- name: Amazon Codeguru Security Batch Get Findings Request Structure
  property_count: 1
  slug: amazon-codeguru-security-batch-get-findings-request-structure
- name: Amazon Codeguru Security Batch Get Findings Response Structure
  property_count: 2
  slug: amazon-codeguru-security-batch-get-findings-response-structure
- name: Amazon Codeguru Security Categories With Most Findings Structure
  property_count: 0
  slug: amazon-codeguru-security-categories-with-most-findings-structure
- name: Amazon Codeguru Security Category With Finding Num Structure
  property_count: 2
  slug: amazon-codeguru-security-category-with-finding-num-structure
- name: Amazon Codeguru Security Client Token Structure
  property_count: 0
  slug: amazon-codeguru-security-client-token-structure
- name: Amazon Codeguru Security Code Line Structure
  property_count: 2
  slug: amazon-codeguru-security-code-line-structure
- name: Amazon Codeguru Security Code Snippet Structure
  property_count: 0
  slug: amazon-codeguru-security-code-snippet-structure
- name: Amazon Codeguru Security Create Scan Request Structure
  property_count: 6
  slug: amazon-codeguru-security-create-scan-request-structure
- name: Amazon Codeguru Security Create Scan Response Structure
  property_count: 5
  slug: amazon-codeguru-security-create-scan-response-structure
- name: Amazon Codeguru Security Create Upload Url Request Structure
  property_count: 1
  slug: amazon-codeguru-security-create-upload-url-request-structure
- name: Amazon Codeguru Security Create Upload Url Response Structure
  property_count: 3
  slug: amazon-codeguru-security-create-upload-url-response-structure
- name: Amazon Codeguru Security Detector Tags Structure
  property_count: 0
  slug: amazon-codeguru-security-detector-tags-structure
- name: Amazon Codeguru Security Double Structure
  property_count: 0
  slug: amazon-codeguru-security-double-structure
- name: Amazon Codeguru Security Encryption Config Structure
  property_count: 1
  slug: amazon-codeguru-security-encryption-config-structure
- name: Amazon Codeguru Security Error Code Structure
  property_count: 0
  slug: amazon-codeguru-security-error-code-structure
- name: Amazon Codeguru Security File Path Structure
  property_count: 5
  slug: amazon-codeguru-security-file-path-structure
- name: Amazon Codeguru Security Finding Identifier Structure
  property_count: 2
  slug: amazon-codeguru-security-finding-identifier-structure
- name: Amazon Codeguru Security Finding Identifiers Structure
  property_count: 0
  slug: amazon-codeguru-security-finding-identifiers-structure
- name: Amazon Codeguru Security Finding Metrics Value Per Severity Structure
  property_count: 5
  slug: amazon-codeguru-security-finding-metrics-value-per-severity-structure
- name: Amazon Codeguru Security Finding Structure
  property_count: 16
  slug: amazon-codeguru-security-finding-structure
- name: Amazon Codeguru Security Findings Metric List Structure
  property_count: 0
  slug: amazon-codeguru-security-findings-metric-list-structure
- name: Amazon Codeguru Security Findings Structure
  property_count: 0
  slug: amazon-codeguru-security-findings-structure
- name: Amazon Codeguru Security Get Account Configuration Request Structure
  property_count: 0
  slug: amazon-codeguru-security-get-account-configuration-request-structure
- name: Amazon Codeguru Security Get Account Configuration Response Structure
  property_count: 1
  slug: amazon-codeguru-security-get-account-configuration-response-structure
- name: Amazon Codeguru Security Get Findings Request Max Results Integer Structure
  property_count: 0
  slug: amazon-codeguru-security-get-findings-request-max-results-integer-structure
- name: Amazon Codeguru Security Get Findings Request Structure
  property_count: 0
  slug: amazon-codeguru-security-get-findings-request-structure
- name: Amazon Codeguru Security Get Findings Response Structure
  property_count: 2
  slug: amazon-codeguru-security-get-findings-response-structure
- name: Amazon Codeguru Security Get Metrics Summary Request Structure
  property_count: 0
  slug: amazon-codeguru-security-get-metrics-summary-request-structure
- name: Amazon Codeguru Security Get Metrics Summary Response Structure
  property_count: 1
  slug: amazon-codeguru-security-get-metrics-summary-response-structure
- name: Amazon Codeguru Security Get Scan Request Structure
  property_count: 0
  slug: amazon-codeguru-security-get-scan-request-structure
- name: Amazon Codeguru Security Get Scan Response Structure
  property_count: 8
  slug: amazon-codeguru-security-get-scan-response-structure
- name: Amazon Codeguru Security Header Key Structure
  property_count: 0
  slug: amazon-codeguru-security-header-key-structure
- name: Amazon Codeguru Security Header Value Structure
  property_count: 0
  slug: amazon-codeguru-security-header-value-structure
- name: Amazon Codeguru Security Integer Structure
  property_count: 0
  slug: amazon-codeguru-security-integer-structure
- name: Amazon Codeguru Security Kms Key Arn Structure
  property_count: 0
  slug: amazon-codeguru-security-kms-key-arn-structure
- name: Amazon Codeguru Security List Findings Metrics Request Max Results Integer Structure
  property_count: 0
  slug: amazon-codeguru-security-list-findings-metrics-request-max-results-integer-structure
- name: Amazon Codeguru Security List Findings Metrics Request Structure
  property_count: 0
  slug: amazon-codeguru-security-list-findings-metrics-request-structure
- name: Amazon Codeguru Security List Findings Metrics Response Structure
  property_count: 2
  slug: amazon-codeguru-security-list-findings-metrics-response-structure
- name: Amazon Codeguru Security List Scans Request Max Results Integer Structure
  property_count: 0
  slug: amazon-codeguru-security-list-scans-request-max-results-integer-structure
- name: Amazon Codeguru Security List Scans Request Structure
  property_count: 0
  slug: amazon-codeguru-security-list-scans-request-structure
- name: Amazon Codeguru Security List Scans Response Structure
  property_count: 2
  slug: amazon-codeguru-security-list-scans-response-structure
- name: Amazon Codeguru Security List Tags For Resource Request Structure
  property_count: 0
  slug: amazon-codeguru-security-list-tags-for-resource-request-structure
- name: Amazon Codeguru Security List Tags For Resource Response Structure
  property_count: 1
  slug: amazon-codeguru-security-list-tags-for-resource-response-structure
- name: Amazon Codeguru Security Long Structure
  property_count: 0
  slug: amazon-codeguru-security-long-structure
- name: Amazon Codeguru Security Metrics Summary Structure
  property_count: 5
  slug: amazon-codeguru-security-metrics-summary-structure
- name: Amazon Codeguru Security Next Token Structure
  property_count: 0
  slug: amazon-codeguru-security-next-token-structure
- name: Amazon Codeguru Security Recommendation Structure
  property_count: 2
  slug: amazon-codeguru-security-recommendation-structure
- name: Amazon Codeguru Security Reference Urls Structure
  property_count: 0
  slug: amazon-codeguru-security-reference-urls-structure
- name: Amazon Codeguru Security Related Vulnerabilities Structure
  property_count: 0
  slug: amazon-codeguru-security-related-vulnerabilities-structure
- name: Amazon Codeguru Security Remediation Structure
  property_count: 2
  slug: amazon-codeguru-security-remediation-structure
- name: Amazon Codeguru Security Request Header Map Structure
  property_count: 0
  slug: amazon-codeguru-security-request-header-map-structure
- name: Amazon Codeguru Security Resource Id Structure
  property_count: 1
  slug: amazon-codeguru-security-resource-id-structure
- name: Amazon Codeguru Security Resource Structure
  property_count: 2
  slug: amazon-codeguru-security-resource-structure
- name: Amazon Codeguru Security S3 Url Structure
  property_count: 0
  slug: amazon-codeguru-security-s3-url-structure
- name: Amazon Codeguru Security Scan Name Arn Structure
  property_count: 0
  slug: amazon-codeguru-security-scan-name-arn-structure
- name: Amazon Codeguru Security Scan Name Structure
  property_count: 0
  slug: amazon-codeguru-security-scan-name-structure
- name: Amazon Codeguru Security Scan Name With Finding Num Structure
  property_count: 2
  slug: amazon-codeguru-security-scan-name-with-finding-num-structure
- name: Amazon Codeguru Security Scan State Structure
  property_count: 0
  slug: amazon-codeguru-security-scan-state-structure
- name: Amazon Codeguru Security Scan Summaries Structure
  property_count: 0
  slug: amazon-codeguru-security-scan-summaries-structure
- name: Amazon Codeguru Security Scan Summary Structure
  property_count: 6
  slug: amazon-codeguru-security-scan-summary-structure
- name: Amazon Codeguru Security Scan Type Structure
  property_count: 0
  slug: amazon-codeguru-security-scan-type-structure
- name: Amazon Codeguru Security Scans With Most Open Critical Findings Structure
  property_count: 0
  slug: amazon-codeguru-security-scans-with-most-open-critical-findings-structure
- name: Amazon Codeguru Security Scans With Most Open Findings Structure
  property_count: 0
  slug: amazon-codeguru-security-scans-with-most-open-findings-structure
- name: Amazon Codeguru Security Severity Structure
  property_count: 0
  slug: amazon-codeguru-security-severity-structure
- name: Amazon Codeguru Security Status Structure
  property_count: 0
  slug: amazon-codeguru-security-status-structure
- name: Amazon Codeguru Security String Structure
  property_count: 0
  slug: amazon-codeguru-security-string-structure
- name: Amazon Codeguru Security Suggested Fix Structure
  property_count: 2
  slug: amazon-codeguru-security-suggested-fix-structure
- name: Amazon Codeguru Security Suggested Fixes Structure
  property_count: 0
  slug: amazon-codeguru-security-suggested-fixes-structure
- name: Amazon Codeguru Security Tag Key List Structure
  property_count: 0
  slug: amazon-codeguru-security-tag-key-list-structure
- name: Amazon Codeguru Security Tag Key Structure
  property_count: 0
  slug: amazon-codeguru-security-tag-key-structure
- name: Amazon Codeguru Security Tag Map Structure
  property_count: 0
  slug: amazon-codeguru-security-tag-map-structure
- name: Amazon Codeguru Security Tag Resource Request Structure
  property_count: 1
  slug: amazon-codeguru-security-tag-resource-request-structure
- name: Amazon Codeguru Security Tag Resource Response Structure
  property_count: 0
  slug: amazon-codeguru-security-tag-resource-response-structure
- name: Amazon Codeguru Security Tag Value Structure
  property_count: 0
  slug: amazon-codeguru-security-tag-value-structure
- name: Amazon Codeguru Security Timestamp Structure
  property_count: 0
  slug: amazon-codeguru-security-timestamp-structure
- name: Amazon Codeguru Security Untag Resource Request Structure
  property_count: 0
  slug: amazon-codeguru-security-untag-resource-request-structure
- name: Amazon Codeguru Security Untag Resource Response Structure
  property_count: 0
  slug: amazon-codeguru-security-untag-resource-response-structure
- name: Amazon Codeguru Security Update Account Configuration Request Structure
  property_count: 1
  slug: amazon-codeguru-security-update-account-configuration-request-structure
- name: Amazon Codeguru Security Update Account Configuration Response Structure
  property_count: 1
  slug: amazon-codeguru-security-update-account-configuration-response-structure
- name: Amazon Codeguru Security Uuid Structure
  property_count: 0
  slug: amazon-codeguru-security-uuid-structure
- name: Amazon Codeguru Security Vulnerability Structure
  property_count: 5
  slug: amazon-codeguru-security-vulnerability-structure
jsonld:
- class_count: 49
  name: Amazon Codeguru Security Context
  property_count: 70
  slug: amazon-codeguru-security-context
layout: provider
mcp_servers:
- description: ''
  name: Amazon CodeGuru Security MCP Server
  slug: amazon-codeguru-security-mcp-server
modified: '2026-06-20'
name: Amazon CodeGuru Security
nav: Providers
network: true
overview: 'Amazon CodeGuru Security publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AccountConfiguration API, BatchGetFindings API, Findings API, and 5 more. Tagged areas include Amazon, Security, SAST, Code Analysis, and DevSecOps.


  The Amazon CodeGuru Security catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon CodeGuru Security''s developer surface includes authentication, getting-started guide, pricing, developer console, developer portal, documentation, engineering blog, and 20 more developer resources.'
random_paper: 8
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon CodeGuru Security API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-codeguru-security-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Amazon CodeGuru Security API Rules
  rule_count: 17
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 10
  slug: amazon-codeguru-security-spectral-rules
score:
  band: developing
  composite: 47.6
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 45.5
    contract_quality: 69.9
    developer_ergonomics: 28.6
    discoverability: 81.5
    governance: 45.5
    operational_transparency: 18.4
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-codeguru-security/refs/heads/main/screenshots/amazon-codeguru-security-2026-07-25T200005.png
security:
- kind: authentication
  name: Amazon Codeguru Security Authentication
  slug: amazon-codeguru-security-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Codeguru Security Domain Security
  slug: amazon-codeguru-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Codeguru Security Vulnerability Disclosure
  slug: amazon-codeguru-security-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Codeguru Security Trust Center
  slug: amazon-codeguru-security-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-codeguru-security
tags:
- Amazon
- Security
- SAST
- Code Analysis
- DevSecOps
- Developer Tools
use_cases:
- description: Integrate security scanning into CI/CD pipelines to detect vulnerabilities before code reaches production.
  name: DevSecOps Integration
- description: Run security scans on existing codebases to identify and remediate vulnerabilities for compliance audits.
  name: Security Audit and Compliance
- description: Scan infrastructure-as-code templates for security misconfigurations before provisioning cloud resources.
  name: IaC Security Validation
website: https://aws.amazon.com/codegurusecurity/
---
