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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Amazon Codeguru Reviewer Agentic Access
  operation_count: 14
  slug: amazon-codeguru-reviewer-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 5
apis:
- description: The Associations API from Amazon CodeGuru Reviewer — 2 operation(s) for associations.
  name: Amazon CodeGuru Reviewer Associations API
  slug: amazon-codeguru-reviewer-associations-api
- description: The Codereviews API from Amazon CodeGuru Reviewer — 3 operation(s) for codereviews.
  name: Amazon CodeGuru Reviewer Codereviews API
  slug: amazon-codeguru-reviewer-codereviews-api
- description: The Codereviews#Type API from Amazon CodeGuru Reviewer — 1 operation(s) for codereviews#type.
  name: Amazon CodeGuru Reviewer Codereviews#Type API
  slug: amazon-codeguru-reviewer-codereviews-type-api
- description: The Feedback API from Amazon CodeGuru Reviewer — 3 operation(s) for feedback.
  name: Amazon CodeGuru Reviewer Feedback API
  slug: amazon-codeguru-reviewer-feedback-api
- description: The Tags API from Amazon CodeGuru Reviewer — 2 operation(s) for tags.
  name: Amazon CodeGuru Reviewer Tags API
  slug: amazon-codeguru-reviewer-tags-api
artifact_total: 331
collections:
- collection_type: postman
  name: Amazon CodeGuru Reviewer Associations API
  slug: postman-amazon-codeguru-reviewer-associations-api
- collection_type: postman
  name: Amazon CodeGuru Reviewer Associations Codereviews API
  slug: postman-amazon-codeguru-reviewer-codereviews-api
- collection_type: postman
  name: Amazon CodeGuru Reviewer Associations Codereviews#Type API
  slug: postman-amazon-codeguru-reviewer-codereviews-type-api
- collection_type: postman
  name: Amazon CodeGuru Reviewer Associations Feedback API
  slug: postman-amazon-codeguru-reviewer-feedback-api
- collection_type: postman
  name: Amazon CodeGuru Reviewer Associations Tags API
  slug: postman-amazon-codeguru-reviewer-tags-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-codeguru-reviewer/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-codeguru-reviewer-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-codeguru-reviewer-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-codeguru-reviewer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-codeguru-reviewer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-codeguru-reviewer-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/codeguru/reviewer
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/codegurureviewer/pricing/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/codegurureviewer/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/codegurureviewer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/codegurureviewer/
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
  url: rules/amazon-codeguru-reviewer-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-codeguru-reviewer-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-codeguru-reviewer-context.jsonld
- group: build
  title: ''
  type: Packages
  url: packages/amazon-codeguru-reviewer-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-codeguru-reviewer-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-codeguru-reviewer-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-codeguru-reviewer-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/devops/tag/amazon-codeguru-reviewer/feed/
created: '2026-03-16'
description: Amazon CodeGuru Reviewer is an automated code review service that uses machine learning and AWS best practices to identify security vulnerabilities, bugs, and hard-to-detect issues in your Java and Python code. It provides intelligent recommendations to help improve code quality and find defects that may be difficult to detect through manual code reviews.
examples:
- key_count: 4
  name: Amazon Codeguru Reviewer Associate Repository Request Example
  slug: amazon-codeguru-reviewer-associate-repository-request-example
- key_count: 2
  name: Amazon Codeguru Reviewer Associate Repository Response Example
  slug: amazon-codeguru-reviewer-associate-repository-response-example
- key_count: 2
  name: Amazon Codeguru Reviewer Branch Diff Source Code Type Example
  slug: amazon-codeguru-reviewer-branch-diff-source-code-type-example
- key_count: 2
  name: Amazon Codeguru Reviewer Code Artifacts Example
  slug: amazon-codeguru-reviewer-code-artifacts-example
- key_count: 1
  name: Amazon Codeguru Reviewer Code Commit Repository Example
  slug: amazon-codeguru-reviewer-code-commit-repository-example
- key_count: 8
  name: Amazon Codeguru Reviewer Code Review Example
  slug: amazon-codeguru-reviewer-code-review-example
- key_count: 8
  name: Amazon Codeguru Reviewer Code Review Summary Example
  slug: amazon-codeguru-reviewer-code-review-summary-example
- key_count: 2
  name: Amazon Codeguru Reviewer Code Review Type Example
  slug: amazon-codeguru-reviewer-code-review-type-example
- key_count: 3
  name: Amazon Codeguru Reviewer Commit Diff Source Code Type Example
  slug: amazon-codeguru-reviewer-commit-diff-source-code-type-example
- key_count: 4
  name: Amazon Codeguru Reviewer Create Code Review Request Example
  slug: amazon-codeguru-reviewer-create-code-review-request-example
- key_count: 1
  name: Amazon Codeguru Reviewer Create Code Review Response Example
  slug: amazon-codeguru-reviewer-create-code-review-response-example
- key_count: 0
  name: Amazon Codeguru Reviewer Describe Code Review Request Example
  slug: amazon-codeguru-reviewer-describe-code-review-request-example
- key_count: 1
  name: Amazon Codeguru Reviewer Describe Code Review Response Example
  slug: amazon-codeguru-reviewer-describe-code-review-response-example
- key_count: 0
  name: Amazon Codeguru Reviewer Describe Recommendation Feedback Request Example
  slug: amazon-codeguru-reviewer-describe-recommendation-feedback-request-example
- key_count: 1
  name: Amazon Codeguru Reviewer Describe Recommendation Feedback Response Example
  slug: amazon-codeguru-reviewer-describe-recommendation-feedback-response-example
- key_count: 0
  name: Amazon Codeguru Reviewer Describe Repository Association Request Example
  slug: amazon-codeguru-reviewer-describe-repository-association-request-example
- key_count: 2
  name: Amazon Codeguru Reviewer Describe Repository Association Response Example
  slug: amazon-codeguru-reviewer-describe-repository-association-response-example
- key_count: 0
  name: Amazon Codeguru Reviewer Disassociate Repository Request Example
  slug: amazon-codeguru-reviewer-disassociate-repository-request-example
- key_count: 2
  name: Amazon Codeguru Reviewer Disassociate Repository Response Example
  slug: amazon-codeguru-reviewer-disassociate-repository-response-example
- key_count: 2
  name: Amazon Codeguru Reviewer Event Info Example
  slug: amazon-codeguru-reviewer-event-info-example
- key_count: 2
  name: Amazon Codeguru Reviewer Kms Key Details Example
  slug: amazon-codeguru-reviewer-kms-key-details-example
- key_count: 0
  name: Amazon Codeguru Reviewer List Code Reviews Request Example
  slug: amazon-codeguru-reviewer-list-code-reviews-request-example
- key_count: 2
  name: Amazon Codeguru Reviewer List Code Reviews Response Example
  slug: amazon-codeguru-reviewer-list-code-reviews-response-example
- key_count: 0
  name: Amazon Codeguru Reviewer List Recommendation Feedback Request Example
  slug: amazon-codeguru-reviewer-list-recommendation-feedback-request-example
- key_count: 2
  name: Amazon Codeguru Reviewer List Recommendation Feedback Response Example
  slug: amazon-codeguru-reviewer-list-recommendation-feedback-response-example
- key_count: 0
  name: Amazon Codeguru Reviewer List Recommendations Request Example
  slug: amazon-codeguru-reviewer-list-recommendations-request-example
- key_count: 2
  name: Amazon Codeguru Reviewer List Recommendations Response Example
  slug: amazon-codeguru-reviewer-list-recommendations-response-example
- key_count: 0
  name: Amazon Codeguru Reviewer List Repository Associations Request Example
  slug: amazon-codeguru-reviewer-list-repository-associations-request-example
- key_count: 2
  name: Amazon Codeguru Reviewer List Repository Associations Response Example
  slug: amazon-codeguru-reviewer-list-repository-associations-response-example
- key_count: 0
  name: Amazon Codeguru Reviewer List Tags For Resource Request Example
  slug: amazon-codeguru-reviewer-list-tags-for-resource-request-example
- key_count: 1
  name: Amazon Codeguru Reviewer List Tags For Resource Response Example
  slug: amazon-codeguru-reviewer-list-tags-for-resource-response-example
- key_count: 3
  name: Amazon Codeguru Reviewer Metrics Example
  slug: amazon-codeguru-reviewer-metrics-example
- key_count: 3
  name: Amazon Codeguru Reviewer Metrics Summary Example
  slug: amazon-codeguru-reviewer-metrics-summary-example
- key_count: 3
  name: Amazon Codeguru Reviewer Put Recommendation Feedback Request Example
  slug: amazon-codeguru-reviewer-put-recommendation-feedback-request-example
- key_count: 0
  name: Amazon Codeguru Reviewer Put Recommendation Feedback Response Example
  slug: amazon-codeguru-reviewer-put-recommendation-feedback-response-example
- key_count: 6
  name: Amazon Codeguru Reviewer Recommendation Feedback Example
  slug: amazon-codeguru-reviewer-recommendation-feedback-example
- key_count: 3
  name: Amazon Codeguru Reviewer Recommendation Feedback Summary Example
  slug: amazon-codeguru-reviewer-recommendation-feedback-summary-example
- key_count: 8
  name: Amazon Codeguru Reviewer Recommendation Summary Example
  slug: amazon-codeguru-reviewer-recommendation-summary-example
- key_count: 2
  name: Amazon Codeguru Reviewer Repository Analysis Example
  slug: amazon-codeguru-reviewer-repository-analysis-example
- key_count: 8
  name: Amazon Codeguru Reviewer Repository Association Example
  slug: amazon-codeguru-reviewer-repository-association-example
- key_count: 8
  name: Amazon Codeguru Reviewer Repository Association Summary Example
  slug: amazon-codeguru-reviewer-repository-association-summary-example
- key_count: 4
  name: Amazon Codeguru Reviewer Repository Example
  slug: amazon-codeguru-reviewer-repository-example
- key_count: 1
  name: Amazon Codeguru Reviewer Repository Head Source Code Type Example
  slug: amazon-codeguru-reviewer-repository-head-source-code-type-example
- key_count: 4
  name: Amazon Codeguru Reviewer Request Metadata Example
  slug: amazon-codeguru-reviewer-request-metadata-example
- key_count: 5
  name: Amazon Codeguru Reviewer Rule Metadata Example
  slug: amazon-codeguru-reviewer-rule-metadata-example
- key_count: 2
  name: Amazon Codeguru Reviewer S3 Bucket Repository Example
  slug: amazon-codeguru-reviewer-s3-bucket-repository-example
- key_count: 2
  name: Amazon Codeguru Reviewer S3 Repository Details Example
  slug: amazon-codeguru-reviewer-s3-repository-details-example
- key_count: 2
  name: Amazon Codeguru Reviewer S3 Repository Example
  slug: amazon-codeguru-reviewer-s3-repository-example
- key_count: 5
  name: Amazon Codeguru Reviewer Source Code Type Example
  slug: amazon-codeguru-reviewer-source-code-type-example
- key_count: 0
  name: Amazon Codeguru Reviewer Tag Map Example
  slug: amazon-codeguru-reviewer-tag-map-example
- key_count: 1
  name: Amazon Codeguru Reviewer Tag Resource Request Example
  slug: amazon-codeguru-reviewer-tag-resource-request-example
- key_count: 0
  name: Amazon Codeguru Reviewer Tag Resource Response Example
  slug: amazon-codeguru-reviewer-tag-resource-response-example
- key_count: 3
  name: Amazon Codeguru Reviewer Third Party Source Repository Example
  slug: amazon-codeguru-reviewer-third-party-source-repository-example
- key_count: 0
  name: Amazon Codeguru Reviewer Untag Resource Request Example
  slug: amazon-codeguru-reviewer-untag-resource-request-example
- key_count: 0
  name: Amazon Codeguru Reviewer Untag Resource Response Example
  slug: amazon-codeguru-reviewer-untag-resource-response-example
features:
- description: Automatically analyze code changes in pull requests and provide recommendations for bugs, security vulnerabilities, and code quality issues.
  name: Automated Code Review
- description: Detect security vulnerabilities including OWASP Top 10, input validation issues, encryption problems, and AWS API security best practices.
  name: Security Analysis
- description: Analyze Java and Python code with language-specific recommendations based on AWS best practices.
  name: Java and Python Support
- description: Connect CodeGuru Reviewer to GitHub, GitHub Enterprise, Bitbucket, CodeCommit, and S3 repositories.
  name: Repository Association
- description: Automatically trigger code reviews on new pull requests and post recommendations as inline comments.
  name: Pull Request Integration
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-codeguru-reviewer.png
integrations:
- description: Associate GitHub repositories for automated code reviews on pull requests.
  name: GitHub
- description: Connect self-hosted GitHub Enterprise repositories for automated code review.
  name: GitHub Enterprise
- description: Integrate with Bitbucket repositories for pull request code reviews.
  name: Bitbucket
- description: Analyze CodeCommit repositories and pull requests natively.
  name: AWS CodeCommit
- description: Associate S3 buckets for one-time code analysis.
  name: Amazon S3
- description: Combine code review recommendations with profiling insights for comprehensive code quality.
  name: Amazon CodeGuru Profiler
json_schemas:
- name: AnalysisType
  property_count: 0
  slug: amazon-codeguru-reviewer-analysis-type
- name: AnalysisTypes
  property_count: 0
  slug: amazon-codeguru-reviewer-analysis-types
- name: Arn
  property_count: 0
  slug: amazon-codeguru-reviewer-arn
- name: AssociateRepositoryRequest
  property_count: 4
  slug: amazon-codeguru-reviewer-associate-repository-request
- name: AssociateRepositoryResponse
  property_count: 2
  slug: amazon-codeguru-reviewer-associate-repository-response
- name: AssociationArn
  property_count: 0
  slug: amazon-codeguru-reviewer-association-arn
- name: AssociationId
  property_count: 0
  slug: amazon-codeguru-reviewer-association-id
- name: BranchDiffSourceCodeType
  property_count: 2
  slug: amazon-codeguru-reviewer-branch-diff-source-code-type
- name: BranchName
  property_count: 0
  slug: amazon-codeguru-reviewer-branch-name
- name: BuildArtifactsObjectKey
  property_count: 0
  slug: amazon-codeguru-reviewer-build-artifacts-object-key
- name: ClientRequestToken
  property_count: 0
  slug: amazon-codeguru-reviewer-client-request-token
- name: CodeArtifacts
  property_count: 2
  slug: amazon-codeguru-reviewer-code-artifacts
- name: CodeCommitRepository
  property_count: 1
  slug: amazon-codeguru-reviewer-code-commit-repository
- name: CodeReviewName
  property_count: 0
  slug: amazon-codeguru-reviewer-code-review-name
- name: CodeReview
  property_count: 16
  slug: amazon-codeguru-reviewer-code-review
- name: CodeReviewSummaries
  property_count: 0
  slug: amazon-codeguru-reviewer-code-review-summaries
- name: CodeReviewSummary
  property_count: 12
  slug: amazon-codeguru-reviewer-code-review-summary
- name: CodeReviewType
  property_count: 2
  slug: amazon-codeguru-reviewer-code-review-type
- name: CommitDiffSourceCodeType
  property_count: 3
  slug: amazon-codeguru-reviewer-commit-diff-source-code-type
- name: CommitId
  property_count: 0
  slug: amazon-codeguru-reviewer-commit-id
- name: ConfigFileState
  property_count: 0
  slug: amazon-codeguru-reviewer-config-file-state
- name: ConnectionArn
  property_count: 0
  slug: amazon-codeguru-reviewer-connection-arn
- name: CreateCodeReviewRequest
  property_count: 4
  slug: amazon-codeguru-reviewer-create-code-review-request
- name: CreateCodeReviewResponse
  property_count: 1
  slug: amazon-codeguru-reviewer-create-code-review-response
- name: DescribeCodeReviewRequest
  property_count: 0
  slug: amazon-codeguru-reviewer-describe-code-review-request
- name: DescribeCodeReviewResponse
  property_count: 1
  slug: amazon-codeguru-reviewer-describe-code-review-response
- name: DescribeRecommendationFeedbackRequest
  property_count: 0
  slug: amazon-codeguru-reviewer-describe-recommendation-feedback-request
- name: DescribeRecommendationFeedbackResponse
  property_count: 1
  slug: amazon-codeguru-reviewer-describe-recommendation-feedback-response
- name: DescribeRepositoryAssociationRequest
  property_count: 0
  slug: amazon-codeguru-reviewer-describe-repository-association-request
- name: DescribeRepositoryAssociationResponse
  property_count: 2
  slug: amazon-codeguru-reviewer-describe-repository-association-response
- name: DisassociateRepositoryRequest
  property_count: 0
  slug: amazon-codeguru-reviewer-disassociate-repository-request
- name: DisassociateRepositoryResponse
  property_count: 2
  slug: amazon-codeguru-reviewer-disassociate-repository-response
- name: EncryptionOption
  property_count: 0
  slug: amazon-codeguru-reviewer-encryption-option
- name: EventInfo
  property_count: 2
  slug: amazon-codeguru-reviewer-event-info
- name: EventName
  property_count: 0
  slug: amazon-codeguru-reviewer-event-name
- name: EventState
  property_count: 0
  slug: amazon-codeguru-reviewer-event-state
- name: FilePath
  property_count: 0
  slug: amazon-codeguru-reviewer-file-path
- name: FindingsCount
  property_count: 0
  slug: amazon-codeguru-reviewer-findings-count
- name: JobState
  property_count: 0
  slug: amazon-codeguru-reviewer-job-state
- name: JobStates
  property_count: 0
  slug: amazon-codeguru-reviewer-job-states
- name: KMSKeyDetails
  property_count: 2
  slug: amazon-codeguru-reviewer-kms-key-details
- name: KMSKeyId
  property_count: 0
  slug: amazon-codeguru-reviewer-kms-key-id
- name: LineNumber
  property_count: 0
  slug: amazon-codeguru-reviewer-line-number
- name: LinesOfCodeCount
  property_count: 0
  slug: amazon-codeguru-reviewer-lines-of-code-count
- name: ListCodeReviewsMaxResults
  property_count: 0
  slug: amazon-codeguru-reviewer-list-code-reviews-max-results
- name: ListCodeReviewsRequest
  property_count: 0
  slug: amazon-codeguru-reviewer-list-code-reviews-request
- name: ListCodeReviewsResponse
  property_count: 2
  slug: amazon-codeguru-reviewer-list-code-reviews-response
- name: ListRecommendationFeedbackRequest
  property_count: 0
  slug: amazon-codeguru-reviewer-list-recommendation-feedback-request
- name: ListRecommendationFeedbackResponse
  property_count: 2
  slug: amazon-codeguru-reviewer-list-recommendation-feedback-response
- name: ListRecommendationsMaxResults
  property_count: 0
  slug: amazon-codeguru-reviewer-list-recommendations-max-results
- name: ListRecommendationsRequest
  property_count: 0
  slug: amazon-codeguru-reviewer-list-recommendations-request
- name: ListRecommendationsResponse
  property_count: 2
  slug: amazon-codeguru-reviewer-list-recommendations-response
- name: ListRepositoryAssociationsRequest
  property_count: 0
  slug: amazon-codeguru-reviewer-list-repository-associations-request
- name: ListRepositoryAssociationsResponse
  property_count: 2
  slug: amazon-codeguru-reviewer-list-repository-associations-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: amazon-codeguru-reviewer-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: amazon-codeguru-reviewer-list-tags-for-resource-response
- name: LongDescription
  property_count: 0
  slug: amazon-codeguru-reviewer-long-description
- name: MaxResults
  property_count: 0
  slug: amazon-codeguru-reviewer-max-results
- name: Metrics
  property_count: 3
  slug: amazon-codeguru-reviewer-metrics
- name: MetricsSummary
  property_count: 3
  slug: amazon-codeguru-reviewer-metrics-summary
- name: Name
  property_count: 0
  slug: amazon-codeguru-reviewer-name
- name: Names
  property_count: 0
  slug: amazon-codeguru-reviewer-names
- name: NextToken
  property_count: 0
  slug: amazon-codeguru-reviewer-next-token
- name: NotFoundException
  property_count: 0
  slug: amazon-codeguru-reviewer-not-found-exception
- name: Owner
  property_count: 0
  slug: amazon-codeguru-reviewer-owner
- name: Owners
  property_count: 0
  slug: amazon-codeguru-reviewer-owners
- name: ProviderType
  property_count: 0
  slug: amazon-codeguru-reviewer-provider-type
- name: ProviderTypes
  property_count: 0
  slug: amazon-codeguru-reviewer-provider-types
- name: PullRequestId
  property_count: 0
  slug: amazon-codeguru-reviewer-pull-request-id
- name: PutRecommendationFeedbackRequest
  property_count: 3
  slug: amazon-codeguru-reviewer-put-recommendation-feedback-request
- name: PutRecommendationFeedbackResponse
  property_count: 0
  slug: amazon-codeguru-reviewer-put-recommendation-feedback-response
- name: Reaction
  property_count: 0
  slug: amazon-codeguru-reviewer-reaction
- name: Reactions
  property_count: 0
  slug: amazon-codeguru-reviewer-reactions
- name: RecommendationCategory
  property_count: 0
  slug: amazon-codeguru-reviewer-recommendation-category
- name: RecommendationFeedback
  property_count: 6
  slug: amazon-codeguru-reviewer-recommendation-feedback
- name: RecommendationFeedbackSummaries
  property_count: 0
  slug: amazon-codeguru-reviewer-recommendation-feedback-summaries
- name: RecommendationFeedbackSummary
  property_count: 3
  slug: amazon-codeguru-reviewer-recommendation-feedback-summary
- name: RecommendationId
  property_count: 0
  slug: amazon-codeguru-reviewer-recommendation-id
- name: RecommendationIds
  property_count: 0
  slug: amazon-codeguru-reviewer-recommendation-ids
- name: RecommendationSummaries
  property_count: 0
  slug: amazon-codeguru-reviewer-recommendation-summaries
- name: RecommendationSummary
  property_count: 8
  slug: amazon-codeguru-reviewer-recommendation-summary
- name: RepositoryAnalysis
  property_count: 2
  slug: amazon-codeguru-reviewer-repository-analysis
- name: RepositoryAssociation
  property_count: 12
  slug: amazon-codeguru-reviewer-repository-association
- name: RepositoryAssociationState
  property_count: 0
  slug: amazon-codeguru-reviewer-repository-association-state
- name: RepositoryAssociationStates
  property_count: 0
  slug: amazon-codeguru-reviewer-repository-association-states
- name: RepositoryAssociationSummaries
  property_count: 0
  slug: amazon-codeguru-reviewer-repository-association-summaries
- name: RepositoryAssociationSummary
  property_count: 8
  slug: amazon-codeguru-reviewer-repository-association-summary
- name: RepositoryHeadSourceCodeType
  property_count: 1
  slug: amazon-codeguru-reviewer-repository-head-source-code-type
- name: RepositoryNames
  property_count: 0
  slug: amazon-codeguru-reviewer-repository-names
- name: Repository
  property_count: 4
  slug: amazon-codeguru-reviewer-repository
- name: RequestId
  property_count: 0
  slug: amazon-codeguru-reviewer-request-id
- name: RequestMetadata
  property_count: 4
  slug: amazon-codeguru-reviewer-request-metadata
- name: Requester
  property_count: 0
  slug: amazon-codeguru-reviewer-requester
- name: RuleId
  property_count: 0
  slug: amazon-codeguru-reviewer-rule-id
- name: RuleMetadata
  property_count: 5
  slug: amazon-codeguru-reviewer-rule-metadata
- name: RuleName
  property_count: 0
  slug: amazon-codeguru-reviewer-rule-name
- name: RuleTag
  property_count: 0
  slug: amazon-codeguru-reviewer-rule-tag
- name: RuleTags
  property_count: 0
  slug: amazon-codeguru-reviewer-rule-tags
- name: S3BucketName
  property_count: 0
  slug: amazon-codeguru-reviewer-s3-bucket-name
- name: S3BucketRepository
  property_count: 2
  slug: amazon-codeguru-reviewer-s3-bucket-repository
- name: S3RepositoryDetails
  property_count: 2
  slug: amazon-codeguru-reviewer-s3-repository-details
- name: S3Repository
  property_count: 2
  slug: amazon-codeguru-reviewer-s3-repository
- name: Severity
  property_count: 0
  slug: amazon-codeguru-reviewer-severity
- name: ShortDescription
  property_count: 0
  slug: amazon-codeguru-reviewer-short-description
- name: SourceCodeArtifactsObjectKey
  property_count: 0
  slug: amazon-codeguru-reviewer-source-code-artifacts-object-key
- name: SourceCodeType
  property_count: 5
  slug: amazon-codeguru-reviewer-source-code-type
- name: StateReason
  property_count: 0
  slug: amazon-codeguru-reviewer-state-reason
- name: TagKeyList
  property_count: 0
  slug: amazon-codeguru-reviewer-tag-key-list
- name: TagKey
  property_count: 0
  slug: amazon-codeguru-reviewer-tag-key
- name: TagMap
  property_count: 0
  slug: amazon-codeguru-reviewer-tag-map
- name: TagResourceRequest
  property_count: 1
  slug: amazon-codeguru-reviewer-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: amazon-codeguru-reviewer-tag-resource-response
- name: TagValue
  property_count: 0
  slug: amazon-codeguru-reviewer-tag-value
- name: Text
  property_count: 0
  slug: amazon-codeguru-reviewer-text
- name: ThirdPartySourceRepository
  property_count: 3
  slug: amazon-codeguru-reviewer-third-party-source-repository
- name: TimeStamp
  property_count: 0
  slug: amazon-codeguru-reviewer-time-stamp
- name: Type
  property_count: 0
  slug: amazon-codeguru-reviewer-type
- name: UntagResourceRequest
  property_count: 0
  slug: amazon-codeguru-reviewer-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: amazon-codeguru-reviewer-untag-resource-response
- name: UserId
  property_count: 0
  slug: amazon-codeguru-reviewer-user-id
- name: UserIds
  property_count: 0
  slug: amazon-codeguru-reviewer-user-ids
- name: VendorName
  property_count: 0
  slug: amazon-codeguru-reviewer-vendor-name
json_structures:
- name: Amazon Codeguru Reviewer Analysis Type Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-analysis-type-structure
- name: Amazon Codeguru Reviewer Analysis Types Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-analysis-types-structure
- name: Amazon Codeguru Reviewer Arn Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-arn-structure
- name: Amazon Codeguru Reviewer Associate Repository Request Structure
  property_count: 4
  slug: amazon-codeguru-reviewer-associate-repository-request-structure
- name: Amazon Codeguru Reviewer Associate Repository Response Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-associate-repository-response-structure
- name: Amazon Codeguru Reviewer Association Arn Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-association-arn-structure
- name: Amazon Codeguru Reviewer Association Id Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-association-id-structure
- name: Amazon Codeguru Reviewer Branch Diff Source Code Type Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-branch-diff-source-code-type-structure
- name: Amazon Codeguru Reviewer Branch Name Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-branch-name-structure
- name: Amazon Codeguru Reviewer Build Artifacts Object Key Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-build-artifacts-object-key-structure
- name: Amazon Codeguru Reviewer Client Request Token Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-client-request-token-structure
- name: Amazon Codeguru Reviewer Code Artifacts Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-code-artifacts-structure
- name: Amazon Codeguru Reviewer Code Commit Repository Structure
  property_count: 1
  slug: amazon-codeguru-reviewer-code-commit-repository-structure
- name: Amazon Codeguru Reviewer Code Review Name Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-code-review-name-structure
- name: Amazon Codeguru Reviewer Code Review Structure
  property_count: 16
  slug: amazon-codeguru-reviewer-code-review-structure
- name: Amazon Codeguru Reviewer Code Review Summaries Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-code-review-summaries-structure
- name: Amazon Codeguru Reviewer Code Review Summary Structure
  property_count: 12
  slug: amazon-codeguru-reviewer-code-review-summary-structure
- name: Amazon Codeguru Reviewer Code Review Type Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-code-review-type-structure
- name: Amazon Codeguru Reviewer Commit Diff Source Code Type Structure
  property_count: 3
  slug: amazon-codeguru-reviewer-commit-diff-source-code-type-structure
- name: Amazon Codeguru Reviewer Commit Id Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-commit-id-structure
- name: Amazon Codeguru Reviewer Config File State Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-config-file-state-structure
- name: Amazon Codeguru Reviewer Connection Arn Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-connection-arn-structure
- name: Amazon Codeguru Reviewer Create Code Review Request Structure
  property_count: 4
  slug: amazon-codeguru-reviewer-create-code-review-request-structure
- name: Amazon Codeguru Reviewer Create Code Review Response Structure
  property_count: 1
  slug: amazon-codeguru-reviewer-create-code-review-response-structure
- name: Amazon Codeguru Reviewer Describe Code Review Request Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-describe-code-review-request-structure
- name: Amazon Codeguru Reviewer Describe Code Review Response Structure
  property_count: 1
  slug: amazon-codeguru-reviewer-describe-code-review-response-structure
- name: Amazon Codeguru Reviewer Describe Recommendation Feedback Request Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-describe-recommendation-feedback-request-structure
- name: Amazon Codeguru Reviewer Describe Recommendation Feedback Response Structure
  property_count: 1
  slug: amazon-codeguru-reviewer-describe-recommendation-feedback-response-structure
- name: Amazon Codeguru Reviewer Describe Repository Association Request Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-describe-repository-association-request-structure
- name: Amazon Codeguru Reviewer Describe Repository Association Response Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-describe-repository-association-response-structure
- name: Amazon Codeguru Reviewer Disassociate Repository Request Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-disassociate-repository-request-structure
- name: Amazon Codeguru Reviewer Disassociate Repository Response Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-disassociate-repository-response-structure
- name: Amazon Codeguru Reviewer Encryption Option Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-encryption-option-structure
- name: Amazon Codeguru Reviewer Event Info Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-event-info-structure
- name: Amazon Codeguru Reviewer Event Name Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-event-name-structure
- name: Amazon Codeguru Reviewer Event State Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-event-state-structure
- name: Amazon Codeguru Reviewer File Path Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-file-path-structure
- name: Amazon Codeguru Reviewer Findings Count Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-findings-count-structure
- name: Amazon Codeguru Reviewer Job State Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-job-state-structure
- name: Amazon Codeguru Reviewer Job States Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-job-states-structure
- name: Amazon Codeguru Reviewer Kms Key Details Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-kms-key-details-structure
- name: Amazon Codeguru Reviewer Kms Key Id Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-kms-key-id-structure
- name: Amazon Codeguru Reviewer Line Number Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-line-number-structure
- name: Amazon Codeguru Reviewer Lines Of Code Count Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-lines-of-code-count-structure
- name: Amazon Codeguru Reviewer List Code Reviews Max Results Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-list-code-reviews-max-results-structure
- name: Amazon Codeguru Reviewer List Code Reviews Request Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-list-code-reviews-request-structure
- name: Amazon Codeguru Reviewer List Code Reviews Response Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-list-code-reviews-response-structure
- name: Amazon Codeguru Reviewer List Recommendation Feedback Request Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-list-recommendation-feedback-request-structure
- name: Amazon Codeguru Reviewer List Recommendation Feedback Response Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-list-recommendation-feedback-response-structure
- name: Amazon Codeguru Reviewer List Recommendations Max Results Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-list-recommendations-max-results-structure
- name: Amazon Codeguru Reviewer List Recommendations Request Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-list-recommendations-request-structure
- name: Amazon Codeguru Reviewer List Recommendations Response Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-list-recommendations-response-structure
- name: Amazon Codeguru Reviewer List Repository Associations Request Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-list-repository-associations-request-structure
- name: Amazon Codeguru Reviewer List Repository Associations Response Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-list-repository-associations-response-structure
- name: Amazon Codeguru Reviewer List Tags For Resource Request Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-list-tags-for-resource-request-structure
- name: Amazon Codeguru Reviewer List Tags For Resource Response Structure
  property_count: 1
  slug: amazon-codeguru-reviewer-list-tags-for-resource-response-structure
- name: Amazon Codeguru Reviewer Long Description Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-long-description-structure
- name: Amazon Codeguru Reviewer Max Results Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-max-results-structure
- name: Amazon Codeguru Reviewer Metrics Structure
  property_count: 3
  slug: amazon-codeguru-reviewer-metrics-structure
- name: Amazon Codeguru Reviewer Metrics Summary Structure
  property_count: 3
  slug: amazon-codeguru-reviewer-metrics-summary-structure
- name: Amazon Codeguru Reviewer Name Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-name-structure
- name: Amazon Codeguru Reviewer Names Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-names-structure
- name: Amazon Codeguru Reviewer Next Token Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-next-token-structure
- name: Amazon Codeguru Reviewer Not Found Exception Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-not-found-exception-structure
- name: Amazon Codeguru Reviewer Owner Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-owner-structure
- name: Amazon Codeguru Reviewer Owners Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-owners-structure
- name: Amazon Codeguru Reviewer Provider Type Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-provider-type-structure
- name: Amazon Codeguru Reviewer Provider Types Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-provider-types-structure
- name: Amazon Codeguru Reviewer Pull Request Id Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-pull-request-id-structure
- name: Amazon Codeguru Reviewer Put Recommendation Feedback Request Structure
  property_count: 3
  slug: amazon-codeguru-reviewer-put-recommendation-feedback-request-structure
- name: Amazon Codeguru Reviewer Put Recommendation Feedback Response Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-put-recommendation-feedback-response-structure
- name: Amazon Codeguru Reviewer Reaction Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-reaction-structure
- name: Amazon Codeguru Reviewer Reactions Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-reactions-structure
- name: Amazon Codeguru Reviewer Recommendation Category Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-recommendation-category-structure
- name: Amazon Codeguru Reviewer Recommendation Feedback Structure
  property_count: 6
  slug: amazon-codeguru-reviewer-recommendation-feedback-structure
- name: Amazon Codeguru Reviewer Recommendation Feedback Summaries Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-recommendation-feedback-summaries-structure
- name: Amazon Codeguru Reviewer Recommendation Feedback Summary Structure
  property_count: 3
  slug: amazon-codeguru-reviewer-recommendation-feedback-summary-structure
- name: Amazon Codeguru Reviewer Recommendation Id Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-recommendation-id-structure
- name: Amazon Codeguru Reviewer Recommendation Ids Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-recommendation-ids-structure
- name: Amazon Codeguru Reviewer Recommendation Summaries Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-recommendation-summaries-structure
- name: Amazon Codeguru Reviewer Recommendation Summary Structure
  property_count: 8
  slug: amazon-codeguru-reviewer-recommendation-summary-structure
- name: Amazon Codeguru Reviewer Repository Analysis Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-repository-analysis-structure
- name: Amazon Codeguru Reviewer Repository Association State Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-repository-association-state-structure
- name: Amazon Codeguru Reviewer Repository Association States Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-repository-association-states-structure
- name: Amazon Codeguru Reviewer Repository Association Structure
  property_count: 12
  slug: amazon-codeguru-reviewer-repository-association-structure
- name: Amazon Codeguru Reviewer Repository Association Summaries Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-repository-association-summaries-structure
- name: Amazon Codeguru Reviewer Repository Association Summary Structure
  property_count: 8
  slug: amazon-codeguru-reviewer-repository-association-summary-structure
- name: Amazon Codeguru Reviewer Repository Head Source Code Type Structure
  property_count: 1
  slug: amazon-codeguru-reviewer-repository-head-source-code-type-structure
- name: Amazon Codeguru Reviewer Repository Names Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-repository-names-structure
- name: Amazon Codeguru Reviewer Repository Structure
  property_count: 4
  slug: amazon-codeguru-reviewer-repository-structure
- name: Amazon Codeguru Reviewer Request Id Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-request-id-structure
- name: Amazon Codeguru Reviewer Request Metadata Structure
  property_count: 4
  slug: amazon-codeguru-reviewer-request-metadata-structure
- name: Amazon Codeguru Reviewer Requester Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-requester-structure
- name: Amazon Codeguru Reviewer Rule Id Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-rule-id-structure
- name: Amazon Codeguru Reviewer Rule Metadata Structure
  property_count: 5
  slug: amazon-codeguru-reviewer-rule-metadata-structure
- name: Amazon Codeguru Reviewer Rule Name Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-rule-name-structure
- name: Amazon Codeguru Reviewer Rule Tag Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-rule-tag-structure
- name: Amazon Codeguru Reviewer Rule Tags Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-rule-tags-structure
- name: Amazon Codeguru Reviewer S3 Bucket Name Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-s3-bucket-name-structure
- name: Amazon Codeguru Reviewer S3 Bucket Repository Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-s3-bucket-repository-structure
- name: Amazon Codeguru Reviewer S3 Repository Details Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-s3-repository-details-structure
- name: Amazon Codeguru Reviewer S3 Repository Structure
  property_count: 2
  slug: amazon-codeguru-reviewer-s3-repository-structure
- name: Amazon Codeguru Reviewer Severity Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-severity-structure
- name: Amazon Codeguru Reviewer Short Description Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-short-description-structure
- name: Amazon Codeguru Reviewer Source Code Artifacts Object Key Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-source-code-artifacts-object-key-structure
- name: Amazon Codeguru Reviewer Source Code Type Structure
  property_count: 5
  slug: amazon-codeguru-reviewer-source-code-type-structure
- name: Amazon Codeguru Reviewer State Reason Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-state-reason-structure
- name: Amazon Codeguru Reviewer Tag Key List Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-tag-key-list-structure
- name: Amazon Codeguru Reviewer Tag Key Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-tag-key-structure
- name: Amazon Codeguru Reviewer Tag Map Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-tag-map-structure
- name: Amazon Codeguru Reviewer Tag Resource Request Structure
  property_count: 1
  slug: amazon-codeguru-reviewer-tag-resource-request-structure
- name: Amazon Codeguru Reviewer Tag Resource Response Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-tag-resource-response-structure
- name: Amazon Codeguru Reviewer Tag Value Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-tag-value-structure
- name: Amazon Codeguru Reviewer Text Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-text-structure
- name: Amazon Codeguru Reviewer Third Party Source Repository Structure
  property_count: 3
  slug: amazon-codeguru-reviewer-third-party-source-repository-structure
- name: Amazon Codeguru Reviewer Time Stamp Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-time-stamp-structure
- name: Amazon Codeguru Reviewer Type Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-type-structure
- name: Amazon Codeguru Reviewer Untag Resource Request Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-untag-resource-request-structure
- name: Amazon Codeguru Reviewer Untag Resource Response Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-untag-resource-response-structure
- name: Amazon Codeguru Reviewer User Id Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-user-id-structure
- name: Amazon Codeguru Reviewer User Ids Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-user-ids-structure
- name: Amazon Codeguru Reviewer Vendor Name Structure
  property_count: 0
  slug: amazon-codeguru-reviewer-vendor-name-structure
jsonld:
- class_count: 40
  name: Amazon Codeguru Reviewer Context
  property_count: 78
  slug: amazon-codeguru-reviewer-context
layout: provider
modified: '2026-06-20'
name: Amazon CodeGuru Reviewer
nav: Providers
network: true
overview: 'Amazon CodeGuru Reviewer publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Associations API, Codereviews API, Codereviews#Type API, and 2 more. Tagged areas include Amazon, Code Review, Security, DevOps, and Machine Learning.


  The Amazon CodeGuru Reviewer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon CodeGuru Reviewer''s developer surface includes authentication, getting-started guide, pricing, developer console, developer portal, documentation, engineering blog, and 18 more developer resources.'
random_paper: 35
rules:
- name: Amazon CodeGuru Reviewer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-codeguru-reviewer-jsonschema-spectral-rules
- name: Amazon CodeGuru Reviewer API Rules
  rule_count: 16
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 10
  slug: amazon-codeguru-reviewer-spectral-rules
score:
  band: strong
  composite: 61.4
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 75.2
    developer_ergonomics: 52.2
    discoverability: 92.6
    governance: 80.2
    operational_transparency: 21.1
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-codeguru-reviewer/refs/heads/main/screenshots/amazon-codeguru-reviewer-2026-07-25T200004.png
security:
- kind: authentication
  name: Amazon Codeguru Reviewer Authentication
  slug: amazon-codeguru-reviewer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Codeguru Reviewer Domain Security
  slug: amazon-codeguru-reviewer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Codeguru Reviewer Vulnerability Disclosure
  slug: amazon-codeguru-reviewer-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Codeguru Reviewer Trust Center
  slug: amazon-codeguru-reviewer-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-codeguru-reviewer
tags:
- Amazon
- Code Review
- Security
- DevOps
- Machine Learning
- Developer Tools
use_cases:
- description: Automatically detect security issues in code changes before they reach production, reducing security review burden on developers.
  name: Security Vulnerability Detection
- description: Enforce code quality standards across the organization with consistent, automated review feedback on every pull request.
  name: Automated Code Quality Enforcement
- description: Help developers identify and fix common coding errors and anti-patterns earlier in the development cycle.
  name: Developer Productivity
website: https://aws.amazon.com/codegurureviewer/
---
