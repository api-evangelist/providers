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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Amazon Well Architected Tool Agentic Access
  operation_count: 56
  slug: amazon-well-architected-tool-agentic-access
  summary_line: 56 operations · 34 acting
api_count: 13
apis:
- description: The ConsolidatedReport#Format API from Amazon Well-Architected Tool — 1 operation(s) for consolidatedreport#format.
  name: Amazon Well-Architected Tool ConsolidatedReport#Format API
  slug: amazon-well-architected-tool-consolidatedreport-format-api
- description: The Global Settings API from Amazon Well-Architected Tool — 1 operation(s) for global settings.
  name: Amazon Well-Architected Tool Global Settings API
  slug: amazon-well-architected-tool-global-settings-api
- description: The ImportLens API from Amazon Well-Architected Tool — 1 operation(s) for importlens.
  name: Amazon Well-Architected Tool ImportLens API
  slug: amazon-well-architected-tool-importlens-api
- description: The Lenses API from Amazon Well-Architected Tool — 8 operation(s) for lenses.
  name: Amazon Well-Architected Tool Lenses API
  slug: amazon-well-architected-tool-lenses-api
- description: The Notifications API from Amazon Well-Architected Tool — 1 operation(s) for notifications.
  name: Amazon Well-Architected Tool Notifications API
  slug: amazon-well-architected-tool-notifications-api
- description: The ProfileNotifications API from Amazon Well-Architected Tool — 1 operation(s) for profilenotifications.
  name: Amazon Well-Architected Tool ProfileNotifications API
  slug: amazon-well-architected-tool-profilenotifications-api
- description: The Profiles API from Amazon Well-Architected Tool — 5 operation(s) for profiles.
  name: Amazon Well-Architected Tool Profiles API
  slug: amazon-well-architected-tool-profiles-api
- description: The ProfileSummaries API from Amazon Well-Architected Tool — 1 operation(s) for profilesummaries.
  name: Amazon Well-Architected Tool ProfileSummaries API
  slug: amazon-well-architected-tool-profilesummaries-api
- description: The ProfileTemplate API from Amazon Well-Architected Tool — 1 operation(s) for profiletemplate.
  name: Amazon Well-Architected Tool ProfileTemplate API
  slug: amazon-well-architected-tool-profiletemplate-api
- description: The ShareInvitations API from Amazon Well-Architected Tool — 2 operation(s) for shareinvitations.
  name: Amazon Well-Architected Tool ShareInvitations API
  slug: amazon-well-architected-tool-shareinvitations-api
- description: The Tags API from Amazon Well-Architected Tool — 2 operation(s) for tags.
  name: Amazon Well-Architected Tool Tags API
  slug: amazon-well-architected-tool-tags-api
- description: The Workloads API from Amazon Well-Architected Tool — 23 operation(s) for workloads.
  name: Amazon Well-Architected Tool Workloads API
  slug: amazon-well-architected-tool-workloads-api
- description: The WorkloadsSummaries API from Amazon Well-Architected Tool — 1 operation(s) for workloadssummaries.
  name: Amazon Well-Architected Tool WorkloadsSummaries API
  slug: amazon-well-architected-tool-workloadssummaries-api
arazzos:
- description: Read a lens review and record lens-level and pillar-level notes on it.
  name: Amazon Well-Architected Tool Annotate Lens Review
  slug: amazon-well-architected-tool-annotate-lens-review-workflow
- description: Update a best-practice answer and snapshot the result as a milestone.
  name: Amazon Well-Architected Tool Answer then Milestone
  slug: amazon-well-architected-tool-answer-then-milestone-workflow
- description: Create a workload, attach additional lenses, and list the lens reviews.
  name: Amazon Well-Architected Tool Associate Lens to Workload
  slug: amazon-well-architected-tool-associate-lens-workflow
- description: Record a milestone for a workload and read it back to confirm.
  name: Amazon Well-Architected Tool Capture Milestone
  slug: amazon-well-architected-tool-capture-milestone-workflow
- description: List your workloads and generate a consolidated report across them.
  name: Amazon Well-Architected Tool Consolidated Report
  slug: amazon-well-architected-tool-consolidated-report-workflow
- description: Create a workload, confirm it, and list the lens reviews it generated.
  name: Amazon Well-Architected Tool Create Workload
  slug: amazon-well-architected-tool-create-workload-workflow
- description: Open a lens review and list its prioritized improvement items.
  name: Amazon Well-Architected Tool Improvement Plan
  slug: amazon-well-architected-tool-improvement-plan-workflow
- description: Find a lens review on a workload and generate its review report.
  name: Amazon Well-Architected Tool Lens Review Report
  slug: amazon-well-architected-tool-lens-review-report-workflow
- description: List a workload's milestones and read the most recent one in detail.
  name: Amazon Well-Architected Tool List Milestone Snapshots
  slug: amazon-well-architected-tool-list-milestone-snapshots-workflow
- description: Open a lens review, list its answers, read one question, and update it.
  name: Amazon Well-Architected Tool Review and Update a Lens Answer
  slug: amazon-well-architected-tool-review-lens-answer-workflow
- description: Share a custom lens with a principal and list its lens shares.
  name: Amazon Well-Architected Tool Share Custom Lens
  slug: amazon-well-architected-tool-share-lens-workflow
- description: Create a workload, share it with an account, and list its shares.
  name: Amazon Well-Architected Tool Share Workload
  slug: amazon-well-architected-tool-share-workload-workflow
- description: Read a workload and update its descriptive metadata and pillar priorities.
  name: Amazon Well-Architected Tool Update Workload Metadata
  slug: amazon-well-architected-tool-update-workload-metadata-workflow
artifact_total: 813
collections:
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format API
  slug: postman-amazon-well-architected-tool-consolidatedreport-format-api
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format Global Settings API
  slug: postman-amazon-well-architected-tool-global-settings-api
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format ImportLens API
  slug: postman-amazon-well-architected-tool-importlens-api
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format Lenses API
  slug: postman-amazon-well-architected-tool-lenses-api
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format Notifications API
  slug: postman-amazon-well-architected-tool-notifications-api
- collection_type: postman
  name: AWS Well-Architected Tool
  slug: postman-amazon-well-architected-tool-openapi-original
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format ProfileNotifications API
  slug: postman-amazon-well-architected-tool-profilenotifications-api
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format Profiles API
  slug: postman-amazon-well-architected-tool-profiles-api
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format ProfileSummaries API
  slug: postman-amazon-well-architected-tool-profilesummaries-api
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format ProfileTemplate API
  slug: postman-amazon-well-architected-tool-profiletemplate-api
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format ShareInvitations API
  slug: postman-amazon-well-architected-tool-shareinvitations-api
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format Tags API
  slug: postman-amazon-well-architected-tool-tags-api
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format Workloads API
  slug: postman-amazon-well-architected-tool-workloads-api
- collection_type: postman
  name: AWS Well-Architected Tool ConsolidatedReport#Format WorkloadsSummaries API
  slug: postman-amazon-well-architected-tool-workloadssummaries-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/aws-samples/custom-lens-wa-hub/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/aws-samples/custom-lens-wa-hub/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/aws-samples/custom-lens-wa-hub/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/aws-samples/custom-lens-wa-hub/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-well-architected-tool-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-well-architected-tool-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-well-architected-tool-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-well-architected-tool-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-well-architected-tool-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-well-architected-tool/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-annotate-lens-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-answer-then-milestone-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-associate-lens-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-capture-milestone-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-consolidated-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-create-workload-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-improvement-plan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-lens-review-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-list-milestone-snapshots-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-review-lens-answer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-share-lens-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-share-workload-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-well-architected-tool-update-workload-metadata-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/well-architected-tool/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/wellarchitected/latest/userguide/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/wellarchitected/
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
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/aws-samples/custom-lens-wa-hub
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-well-architected-tool-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-well-architected-tool-vocabulary.yaml
created: '2026-03-16'
description: 'The AWS Well-Architected Tool helps you review your workloads and compare them to the latest AWS architectural best practices. It provides a consistent process for evaluating architectures and implementing designs that scale over time across five pillars: operational excellence, security, reliability, performance efficiency, and cost optimization. The tool offers lens catalogs, custom lenses, profiles, review templates, and API-driven extensibility for integration into governance workflows.'
examples:
- key_count: 2
  name: Well Architected Tool Additional Resources Example
  slug: well-architected-tool-additional-resources-example
- key_count: 14
  name: Well Architected Tool Answer Example
  slug: well-architected-tool-answer-example
- key_count: 10
  name: Well Architected Tool Answer Summary Example
  slug: well-architected-tool-answer-summary-example
- key_count: 1
  name: Well Architected Tool Associate Lenses Input Example
  slug: well-architected-tool-associate-lenses-input-example
- key_count: 1
  name: Well Architected Tool Associate Profiles Input Example
  slug: well-architected-tool-associate-profiles-input-example
- key_count: 2
  name: Well Architected Tool Best Practice Example
  slug: well-architected-tool-best-practice-example
- key_count: 13
  name: Well Architected Tool Check Detail Example
  slug: well-architected-tool-check-detail-example
- key_count: 11
  name: Well Architected Tool Check Summary Example
  slug: well-architected-tool-check-summary-example
- key_count: 4
  name: Well Architected Tool Choice Answer Example
  slug: well-architected-tool-choice-answer-example
- key_count: 3
  name: Well Architected Tool Choice Answer Summary Example
  slug: well-architected-tool-choice-answer-summary-example
- key_count: 2
  name: Well Architected Tool Choice Content Example
  slug: well-architected-tool-choice-content-example
- key_count: 6
  name: Well Architected Tool Choice Example
  slug: well-architected-tool-choice-example
- key_count: 3
  name: Well Architected Tool Choice Improvement Plan Example
  slug: well-architected-tool-choice-improvement-plan-example
- key_count: 3
  name: Well Architected Tool Choice Update Example
  slug: well-architected-tool-choice-update-example
- key_count: 8
  name: Well Architected Tool Consolidated Report Metric Example
  slug: well-architected-tool-consolidated-report-metric-example
- key_count: 2
  name: Well Architected Tool Create Lens Share Input Example
  slug: well-architected-tool-create-lens-share-input-example
- key_count: 1
  name: Well Architected Tool Create Lens Share Output Example
  slug: well-architected-tool-create-lens-share-output-example
- key_count: 3
  name: Well Architected Tool Create Lens Version Input Example
  slug: well-architected-tool-create-lens-version-input-example
- key_count: 2
  name: Well Architected Tool Create Lens Version Output Example
  slug: well-architected-tool-create-lens-version-output-example
- key_count: 2
  name: Well Architected Tool Create Milestone Input Example
  slug: well-architected-tool-create-milestone-input-example
- key_count: 2
  name: Well Architected Tool Create Milestone Output Example
  slug: well-architected-tool-create-milestone-output-example
- key_count: 5
  name: Well Architected Tool Create Profile Input Example
  slug: well-architected-tool-create-profile-input-example
- key_count: 2
  name: Well Architected Tool Create Profile Output Example
  slug: well-architected-tool-create-profile-output-example
- key_count: 2
  name: Well Architected Tool Create Profile Share Input Example
  slug: well-architected-tool-create-profile-share-input-example
- key_count: 2
  name: Well Architected Tool Create Profile Share Output Example
  slug: well-architected-tool-create-profile-share-output-example
- key_count: 18
  name: Well Architected Tool Create Workload Input Example
  slug: well-architected-tool-create-workload-input-example
- key_count: 2
  name: Well Architected Tool Create Workload Output Example
  slug: well-architected-tool-create-workload-output-example
- key_count: 3
  name: Well Architected Tool Create Workload Share Input Example
  slug: well-architected-tool-create-workload-share-input-example
- key_count: 2
  name: Well Architected Tool Create Workload Share Output Example
  slug: well-architected-tool-create-workload-share-output-example
- key_count: 1
  name: Well Architected Tool Disassociate Lenses Input Example
  slug: well-architected-tool-disassociate-lenses-input-example
- key_count: 1
  name: Well Architected Tool Disassociate Profiles Input Example
  slug: well-architected-tool-disassociate-profiles-input-example
- key_count: 1
  name: Well Architected Tool Export Lens Output Example
  slug: well-architected-tool-export-lens-output-example
- key_count: 5
  name: Well Architected Tool Get Answer Output Example
  slug: well-architected-tool-get-answer-output-example
- key_count: 3
  name: Well Architected Tool Get Consolidated Report Output Example
  slug: well-architected-tool-get-consolidated-report-output-example
- key_count: 1
  name: Well Architected Tool Get Lens Output Example
  slug: well-architected-tool-get-lens-output-example
- key_count: 3
  name: Well Architected Tool Get Lens Review Output Example
  slug: well-architected-tool-get-lens-review-output-example
- key_count: 3
  name: Well Architected Tool Get Lens Review Report Output Example
  slug: well-architected-tool-get-lens-review-report-output-example
- key_count: 6
  name: Well Architected Tool Get Lens Version Difference Output Example
  slug: well-architected-tool-get-lens-version-difference-output-example
- key_count: 2
  name: Well Architected Tool Get Milestone Output Example
  slug: well-architected-tool-get-milestone-output-example
- key_count: 1
  name: Well Architected Tool Get Profile Output Example
  slug: well-architected-tool-get-profile-output-example
- key_count: 1
  name: Well Architected Tool Get Profile Template Output Example
  slug: well-architected-tool-get-profile-template-output-example
- key_count: 1
  name: Well Architected Tool Get Workload Output Example
  slug: well-architected-tool-get-workload-output-example
- key_count: 4
  name: Well Architected Tool Import Lens Input Example
  slug: well-architected-tool-import-lens-input-example
- key_count: 2
  name: Well Architected Tool Import Lens Output Example
  slug: well-architected-tool-import-lens-output-example
- key_count: 6
  name: Well Architected Tool Improvement Summary Example
  slug: well-architected-tool-improvement-summary-example
- key_count: 7
  name: Well Architected Tool Lens Example
  slug: well-architected-tool-lens-example
- key_count: 3
  name: Well Architected Tool Lens Metric Example
  slug: well-architected-tool-lens-metric-example
- key_count: 12
  name: Well Architected Tool Lens Review Example
  slug: well-architected-tool-lens-review-example
- key_count: 3
  name: Well Architected Tool Lens Review Report Example
  slug: well-architected-tool-lens-review-report-example
- key_count: 9
  name: Well Architected Tool Lens Review Summary Example
  slug: well-architected-tool-lens-review-summary-example
- key_count: 4
  name: Well Architected Tool Lens Share Summary Example
  slug: well-architected-tool-lens-share-summary-example
- key_count: 10
  name: Well Architected Tool Lens Summary Example
  slug: well-architected-tool-lens-summary-example
- key_count: 6
  name: Well Architected Tool Lens Upgrade Summary Example
  slug: well-architected-tool-lens-upgrade-summary-example
- key_count: 6
  name: Well Architected Tool List Answers Output Example
  slug: well-architected-tool-list-answers-output-example
- key_count: 6
  name: Well Architected Tool List Check Details Input Example
  slug: well-architected-tool-list-check-details-input-example
- key_count: 2
  name: Well Architected Tool List Check Details Output Example
  slug: well-architected-tool-list-check-details-output-example
- key_count: 6
  name: Well Architected Tool List Check Summaries Input Example
  slug: well-architected-tool-list-check-summaries-input-example
- key_count: 2
  name: Well Architected Tool List Check Summaries Output Example
  slug: well-architected-tool-list-check-summaries-output-example
- key_count: 6
  name: Well Architected Tool List Lens Review Improvements Output Example
  slug: well-architected-tool-list-lens-review-improvements-output-example
- key_count: 4
  name: Well Architected Tool List Lens Reviews Output Example
  slug: well-architected-tool-list-lens-reviews-output-example
- key_count: 2
  name: Well Architected Tool List Lens Shares Output Example
  slug: well-architected-tool-list-lens-shares-output-example
- key_count: 2
  name: Well Architected Tool List Lenses Output Example
  slug: well-architected-tool-list-lenses-output-example
- key_count: 2
  name: Well Architected Tool List Milestones Input Example
  slug: well-architected-tool-list-milestones-input-example
- key_count: 3
  name: Well Architected Tool List Milestones Output Example
  slug: well-architected-tool-list-milestones-output-example
- key_count: 3
  name: Well Architected Tool List Notifications Input Example
  slug: well-architected-tool-list-notifications-input-example
- key_count: 2
  name: Well Architected Tool List Notifications Output Example
  slug: well-architected-tool-list-notifications-output-example
- key_count: 2
  name: Well Architected Tool List Profile Notifications Output Example
  slug: well-architected-tool-list-profile-notifications-output-example
- key_count: 2
  name: Well Architected Tool List Profile Shares Output Example
  slug: well-architected-tool-list-profile-shares-output-example
- key_count: 2
  name: Well Architected Tool List Profiles Output Example
  slug: well-architected-tool-list-profiles-output-example
- key_count: 2
  name: Well Architected Tool List Share Invitations Output Example
  slug: well-architected-tool-list-share-invitations-output-example
- key_count: 1
  name: Well Architected Tool List Tags For Resource Output Example
  slug: well-architected-tool-list-tags-for-resource-output-example
- key_count: 3
  name: Well Architected Tool List Workload Shares Output Example
  slug: well-architected-tool-list-workload-shares-output-example
- key_count: 3
  name: Well Architected Tool List Workloads Input Example
  slug: well-architected-tool-list-workloads-input-example
- key_count: 2
  name: Well Architected Tool List Workloads Output Example
  slug: well-architected-tool-list-workloads-output-example
- key_count: 4
  name: Well Architected Tool Milestone Example
  slug: well-architected-tool-milestone-example
- key_count: 4
  name: Well Architected Tool Milestone Summary Example
  slug: well-architected-tool-milestone-summary-example
- key_count: 2
  name: Well Architected Tool Notification Summary Example
  slug: well-architected-tool-notification-summary-example
- key_count: 4
  name: Well Architected Tool Pillar Difference Example
  slug: well-architected-tool-pillar-difference-example
- key_count: 3
  name: Well Architected Tool Pillar Metric Example
  slug: well-architected-tool-pillar-metric-example
- key_count: 5
  name: Well Architected Tool Pillar Review Summary Example
  slug: well-architected-tool-pillar-review-summary-example
- key_count: 3
  name: Well Architected Tool Profile Choice Example
  slug: well-architected-tool-profile-choice-example
- key_count: 10
  name: Well Architected Tool Profile Example
  slug: well-architected-tool-profile-example
- key_count: 7
  name: Well Architected Tool Profile Notification Summary Example
  slug: well-architected-tool-profile-notification-summary-example
- key_count: 7
  name: Well Architected Tool Profile Question Example
  slug: well-architected-tool-profile-question-example
- key_count: 2
  name: Well Architected Tool Profile Question Update Example
  slug: well-architected-tool-profile-question-update-example
- key_count: 4
  name: Well Architected Tool Profile Share Summary Example
  slug: well-architected-tool-profile-share-summary-example
- key_count: 7
  name: Well Architected Tool Profile Summary Example
  slug: well-architected-tool-profile-summary-example
- key_count: 3
  name: Well Architected Tool Profile Template Choice Example
  slug: well-architected-tool-profile-template-choice-example
- key_count: 4
  name: Well Architected Tool Profile Template Example
  slug: well-architected-tool-profile-template-example
- key_count: 6
  name: Well Architected Tool Profile Template Question Example
  slug: well-architected-tool-profile-template-question-example
- key_count: 3
  name: Well Architected Tool Question Difference Example
  slug: well-architected-tool-question-difference-example
- key_count: 3
  name: Well Architected Tool Question Metric Example
  slug: well-architected-tool-question-metric-example
- key_count: 6
  name: Well Architected Tool Share Invitation Example
  slug: well-architected-tool-share-invitation-example
- key_count: 11
  name: Well Architected Tool Share Invitation Summary Example
  slug: well-architected-tool-share-invitation-summary-example
- key_count: 1
  name: Well Architected Tool Tag Resource Input Example
  slug: well-architected-tool-tag-resource-input-example
- key_count: 5
  name: Well Architected Tool Update Answer Input Example
  slug: well-architected-tool-update-answer-input-example
- key_count: 4
  name: Well Architected Tool Update Answer Output Example
  slug: well-architected-tool-update-answer-output-example
- key_count: 2
  name: Well Architected Tool Update Global Settings Input Example
  slug: well-architected-tool-update-global-settings-input-example
- key_count: 2
  name: Well Architected Tool Update Lens Review Input Example
  slug: well-architected-tool-update-lens-review-input-example
- key_count: 2
  name: Well Architected Tool Update Lens Review Output Example
  slug: well-architected-tool-update-lens-review-output-example
- key_count: 2
  name: Well Architected Tool Update Profile Input Example
  slug: well-architected-tool-update-profile-input-example
- key_count: 1
  name: Well Architected Tool Update Profile Output Example
  slug: well-architected-tool-update-profile-output-example
- key_count: 1
  name: Well Architected Tool Update Share Invitation Input Example
  slug: well-architected-tool-update-share-invitation-input-example
- key_count: 1
  name: Well Architected Tool Update Share Invitation Output Example
  slug: well-architected-tool-update-share-invitation-output-example
- key_count: 16
  name: Well Architected Tool Update Workload Input Example
  slug: well-architected-tool-update-workload-input-example
- key_count: 1
  name: Well Architected Tool Update Workload Output Example
  slug: well-architected-tool-update-workload-output-example
- key_count: 1
  name: Well Architected Tool Update Workload Share Input Example
  slug: well-architected-tool-update-workload-share-input-example
- key_count: 2
  name: Well Architected Tool Update Workload Share Output Example
  slug: well-architected-tool-update-workload-share-output-example
- key_count: 2
  name: Well Architected Tool Upgrade Lens Review Input Example
  slug: well-architected-tool-upgrade-lens-review-input-example
- key_count: 2
  name: Well Architected Tool Upgrade Profile Version Input Example
  slug: well-architected-tool-upgrade-profile-version-input-example
- key_count: 1
  name: Well Architected Tool Version Differences Example
  slug: well-architected-tool-version-differences-example
- key_count: 2
  name: Well Architected Tool Workload Discovery Config Example
  slug: well-architected-tool-workload-discovery-config-example
- key_count: 27
  name: Well Architected Tool Workload Example
  slug: well-architected-tool-workload-example
- key_count: 2
  name: Well Architected Tool Workload Profile Example
  slug: well-architected-tool-workload-profile-example
- key_count: 7
  name: Well Architected Tool Workload Share Example
  slug: well-architected-tool-workload-share-example
- key_count: 5
  name: Well Architected Tool Workload Share Summary Example
  slug: well-architected-tool-workload-share-summary-example
- key_count: 10
  name: Well Architected Tool Workload Summary Example
  slug: well-architected-tool-workload-summary-example
features:
- description: Expert-authored review lenses from AWS covering diverse technology and industry-specific pillars, continuously refreshed with latest best practices.
  name: Lens Catalog
- description: Create organization-specific lenses that combine internal best practices with AWS guidance, shareable with up to 300 IAM users or across AWS Organizations.
  name: Custom Lenses
- description: Pre-define business goals to auto-generate prioritized review questions tailored to your workload context.
  name: Profiles
- description: Standardize answers across multiple workloads to ensure consistent architectural reviews at scale.
  name: Review Templates
- description: Share workloads and custom lenses with IAM users or integrate with AWS Organizations for organization-wide access and visibility.
  name: Enhanced Collaboration
- description: Native integration with AWS Trusted Advisor and AWS Service Catalog AppRegistry to reduce manual review effort.
  name: Service Integration
- description: Robust APIs allow extending Well-Architected functionality into existing architecture governance processes, applications, and workflows.
  name: API-Driven Extensibility
- description: Save milestones, implement improvements, and measure progress over time with point-in-time snapshots of workload review state.
  name: Milestone Tracking
- description: Available in GovCloud (US) with FedRAMP compliance for organizations with stringent regulatory requirements.
  name: Compliance and Regulatory Support
- description: Generate consolidated reports across workloads for governance and executive visibility into architectural risk posture.
  name: Consolidated Reporting
finops:
- name: Amazon Well Architected Tool Finops
  service_category: API
  slug: amazon-well-architected-tool-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-well-architected-tool.png
json_schemas:
- name: AccessDeniedException
  property_count: 0
  slug: well-architected-tool-access-denied-exception
- name: AccountSummary
  property_count: 0
  slug: well-architected-tool-account-summary
- name: AdditionalResourceType
  property_count: 0
  slug: well-architected-tool-additional-resource-type
- name: AdditionalResourcesList
  property_count: 0
  slug: well-architected-tool-additional-resources-list
- name: AdditionalResources
  property_count: 2
  slug: well-architected-tool-additional-resources
- name: AnswerReason
  property_count: 0
  slug: well-architected-tool-answer-reason
- name: Answer
  property_count: 14
  slug: well-architected-tool-answer
- name: AnswerSummaries
  property_count: 0
  slug: well-architected-tool-answer-summaries
- name: AnswerSummary
  property_count: 10
  slug: well-architected-tool-answer-summary
- name: ApplicationArn
  property_count: 0
  slug: well-architected-tool-application-arn
- name: AssociateLensesInput
  property_count: 1
  slug: well-architected-tool-associate-lenses-input
- name: AssociateProfilesInput
  property_count: 1
  slug: well-architected-tool-associate-profiles-input
- name: AwsAccountId
  property_count: 0
  slug: well-architected-tool-aws-account-id
- name: AwsRegion
  property_count: 0
  slug: well-architected-tool-aws-region
- name: Base64String
  property_count: 0
  slug: well-architected-tool-base64-string
- name: BestPractice
  property_count: 2
  slug: well-architected-tool-best-practice
- name: BestPractices
  property_count: 0
  slug: well-architected-tool-best-practices
- name: CheckDescription
  property_count: 0
  slug: well-architected-tool-check-description
- name: CheckDetail
  property_count: 13
  slug: well-architected-tool-check-detail
- name: CheckDetails
  property_count: 0
  slug: well-architected-tool-check-details
- name: CheckFailureReason
  property_count: 0
  slug: well-architected-tool-check-failure-reason
- name: CheckId
  property_count: 0
  slug: well-architected-tool-check-id
- name: CheckName
  property_count: 0
  slug: well-architected-tool-check-name
- name: CheckProvider
  property_count: 0
  slug: well-architected-tool-check-provider
- name: CheckStatusCount
  property_count: 0
  slug: well-architected-tool-check-status-count
- name: CheckStatus
  property_count: 0
  slug: well-architected-tool-check-status
- name: CheckSummaries
  property_count: 0
  slug: well-architected-tool-check-summaries
- name: CheckSummary
  property_count: 11
  slug: well-architected-tool-check-summary
- name: ChoiceAnswer
  property_count: 4
  slug: well-architected-tool-choice-answer
- name: ChoiceAnswerSummaries
  property_count: 0
  slug: well-architected-tool-choice-answer-summaries
- name: ChoiceAnswerSummary
  property_count: 3
  slug: well-architected-tool-choice-answer-summary
- name: ChoiceAnswers
  property_count: 0
  slug: well-architected-tool-choice-answers
- name: ChoiceContentDisplayText
  property_count: 0
  slug: well-architected-tool-choice-content-display-text
- name: ChoiceContent
  property_count: 2
  slug: well-architected-tool-choice-content
- name: ChoiceContentUrl
  property_count: 0
  slug: well-architected-tool-choice-content-url
- name: ChoiceDescription
  property_count: 0
  slug: well-architected-tool-choice-description
- name: ChoiceId
  property_count: 0
  slug: well-architected-tool-choice-id
- name: ChoiceImprovementPlan
  property_count: 3
  slug: well-architected-tool-choice-improvement-plan
- name: ChoiceImprovementPlans
  property_count: 0
  slug: well-architected-tool-choice-improvement-plans
- name: ChoiceNotes
  property_count: 0
  slug: well-architected-tool-choice-notes
- name: ChoiceReason
  property_count: 0
  slug: well-architected-tool-choice-reason
- name: Choice
  property_count: 6
  slug: well-architected-tool-choice
- name: ChoiceStatus
  property_count: 0
  slug: well-architected-tool-choice-status
- name: ChoiceTitle
  property_count: 0
  slug: well-architected-tool-choice-title
- name: ChoiceUpdate
  property_count: 3
  slug: well-architected-tool-choice-update
- name: ChoiceUpdates
  property_count: 0
  slug: well-architected-tool-choice-updates
- name: Choices
  property_count: 0
  slug: well-architected-tool-choices
- name: ClientRequestToken
  property_count: 0
  slug: well-architected-tool-client-request-token
- name: ConflictException
  property_count: 0
  slug: well-architected-tool-conflict-exception
- name: ConsolidatedReportMetric
  property_count: 8
  slug: well-architected-tool-consolidated-report-metric
- name: ConsolidatedReportMetrics
  property_count: 0
  slug: well-architected-tool-consolidated-report-metrics
- name: Count
  property_count: 0
  slug: well-architected-tool-count
- name: CreateLensShareInput
  property_count: 2
  slug: well-architected-tool-create-lens-share-input
- name: CreateLensShareOutput
  property_count: 1
  slug: well-architected-tool-create-lens-share-output
- name: CreateLensVersionInput
  property_count: 3
  slug: well-architected-tool-create-lens-version-input
- name: CreateLensVersionOutput
  property_count: 2
  slug: well-architected-tool-create-lens-version-output
- name: CreateMilestoneInput
  property_count: 2
  slug: well-architected-tool-create-milestone-input
- name: CreateMilestoneOutput
  property_count: 2
  slug: well-architected-tool-create-milestone-output
- name: CreateProfileInput
  property_count: 5
  slug: well-architected-tool-create-profile-input
- name: CreateProfileOutput
  property_count: 2
  slug: well-architected-tool-create-profile-output
- name: CreateProfileShareInput
  property_count: 2
  slug: well-architected-tool-create-profile-share-input
- name: CreateProfileShareOutput
  property_count: 2
  slug: well-architected-tool-create-profile-share-output
- name: CreateWorkloadInput
  property_count: 18
  slug: well-architected-tool-create-workload-input
- name: CreateWorkloadOutput
  property_count: 2
  slug: well-architected-tool-create-workload-output
- name: CreateWorkloadShareInput
  property_count: 3
  slug: well-architected-tool-create-workload-share-input
- name: CreateWorkloadShareOutput
  property_count: 2
  slug: well-architected-tool-create-workload-share-output
- name: DefinitionType
  property_count: 0
  slug: well-architected-tool-definition-type
- name: DeleteLensInput
  property_count: 0
  slug: well-architected-tool-delete-lens-input
- name: DeleteLensShareInput
  property_count: 0
  slug: well-architected-tool-delete-lens-share-input
- name: DeleteProfileInput
  property_count: 0
  slug: well-architected-tool-delete-profile-input
- name: DeleteProfileShareInput
  property_count: 0
  slug: well-architected-tool-delete-profile-share-input
- name: DeleteWorkloadInput
  property_count: 0
  slug: well-architected-tool-delete-workload-input
- name: DeleteWorkloadShareInput
  property_count: 0
  slug: well-architected-tool-delete-workload-share-input
- name: DifferenceStatus
  property_count: 0
  slug: well-architected-tool-difference-status
- name: DisassociateLensesInput
  property_count: 1
  slug: well-architected-tool-disassociate-lenses-input
- name: DisassociateProfilesInput
  property_count: 1
  slug: well-architected-tool-disassociate-profiles-input
- name: DiscoveryIntegrationStatus
  property_count: 0
  slug: well-architected-tool-discovery-integration-status
- name: DisplayText
  property_count: 0
  slug: well-architected-tool-display-text
- name: ExportLensInput
  property_count: 0
  slug: well-architected-tool-export-lens-input
- name: ExportLensOutput
  property_count: 1
  slug: well-architected-tool-export-lens-output
- name: FlaggedResources
  property_count: 0
  slug: well-architected-tool-flagged-resources
- name: GetAnswerInput
  property_count: 0
  slug: well-architected-tool-get-answer-input
- name: GetAnswerOutput
  property_count: 5
  slug: well-architected-tool-get-answer-output
- name: GetConsolidatedReportInput
  property_count: 0
  slug: well-architected-tool-get-consolidated-report-input
- name: GetConsolidatedReportMaxResults
  property_count: 0
  slug: well-architected-tool-get-consolidated-report-max-results
- name: GetConsolidatedReportOutput
  property_count: 3
  slug: well-architected-tool-get-consolidated-report-output
- name: GetLensInput
  property_count: 0
  slug: well-architected-tool-get-lens-input
- name: GetLensOutput
  property_count: 1
  slug: well-architected-tool-get-lens-output
- name: GetLensReviewInput
  property_count: 0
  slug: well-architected-tool-get-lens-review-input
- name: GetLensReviewOutput
  property_count: 3
  slug: well-architected-tool-get-lens-review-output
- name: GetLensReviewReportInput
  property_count: 0
  slug: well-architected-tool-get-lens-review-report-input
- name: GetLensReviewReportOutput
  property_count: 3
  slug: well-architected-tool-get-lens-review-report-output
- name: GetLensVersionDifferenceInput
  property_count: 0
  slug: well-architected-tool-get-lens-version-difference-input
- name: GetLensVersionDifferenceOutput
  property_count: 6
  slug: well-architected-tool-get-lens-version-difference-output
- name: GetMilestoneInput
  property_count: 0
  slug: well-architected-tool-get-milestone-input
- name: GetMilestoneOutput
  property_count: 2
  slug: well-architected-tool-get-milestone-output
- name: GetProfileInput
  property_count: 0
  slug: well-architected-tool-get-profile-input
- name: GetProfileOutput
  property_count: 1
  slug: well-architected-tool-get-profile-output
- name: GetProfileTemplateInput
  property_count: 0
  slug: well-architected-tool-get-profile-template-input
- name: GetProfileTemplateOutput
  property_count: 1
  slug: well-architected-tool-get-profile-template-output
- name: GetWorkloadInput
  property_count: 0
  slug: well-architected-tool-get-workload-input
- name: GetWorkloadOutput
  property_count: 1
  slug: well-architected-tool-get-workload-output
- name: HelpfulResourceUrl
  property_count: 0
  slug: well-architected-tool-helpful-resource-url
- name: ImportLensInput
  property_count: 4
  slug: well-architected-tool-import-lens-input
- name: ImportLensOutput
  property_count: 2
  slug: well-architected-tool-import-lens-output
- name: ImportLensStatus
  property_count: 0
  slug: well-architected-tool-import-lens-status
- name: ImprovementPlanUrl
  property_count: 0
  slug: well-architected-tool-improvement-plan-url
- name: ImprovementSummaries
  property_count: 0
  slug: well-architected-tool-improvement-summaries
- name: ImprovementSummary
  property_count: 6
  slug: well-architected-tool-improvement-summary
- name: IncludeSharedResources
  property_count: 0
  slug: well-architected-tool-include-shared-resources
- name: InternalServerException
  property_count: 0
  slug: well-architected-tool-internal-server-exception
- name: IsApplicable
  property_count: 0
  slug: well-architected-tool-is-applicable
- name: IsMajorVersion
  property_count: 0
  slug: well-architected-tool-is-major-version
- name: IsReviewOwnerUpdateAcknowledged
  property_count: 0
  slug: well-architected-tool-is-review-owner-update-acknowledged
- name: LensAlias
  property_count: 0
  slug: well-architected-tool-lens-alias
- name: LensAliases
  property_count: 0
  slug: well-architected-tool-lens-aliases
- name: LensArn
  property_count: 0
  slug: well-architected-tool-lens-arn
- name: LensDescription
  property_count: 0
  slug: well-architected-tool-lens-description
- name: LensJSON
  property_count: 0
  slug: well-architected-tool-lens-json
- name: LensMetric
  property_count: 3
  slug: well-architected-tool-lens-metric
- name: LensMetrics
  property_count: 0
  slug: well-architected-tool-lens-metrics
- name: LensNamePrefix
  property_count: 0
  slug: well-architected-tool-lens-name-prefix
- name: LensName
  property_count: 0
  slug: well-architected-tool-lens-name
- name: LensOwner
  property_count: 0
  slug: well-architected-tool-lens-owner
- name: LensReviewReport
  property_count: 3
  slug: well-architected-tool-lens-review-report
- name: LensReview
  property_count: 12
  slug: well-architected-tool-lens-review
- name: LensReviewSummaries
  property_count: 0
  slug: well-architected-tool-lens-review-summaries
- name: LensReviewSummary
  property_count: 9
  slug: well-architected-tool-lens-review-summary
- name: Lens
  property_count: 7
  slug: well-architected-tool-lens
- name: LensShareSummaries
  property_count: 0
  slug: well-architected-tool-lens-share-summaries
- name: LensShareSummary
  property_count: 4
  slug: well-architected-tool-lens-share-summary
- name: LensStatus
  property_count: 0
  slug: well-architected-tool-lens-status
- name: LensStatusType
  property_count: 0
  slug: well-architected-tool-lens-status-type
- name: LensSummaries
  property_count: 0
  slug: well-architected-tool-lens-summaries
- name: LensSummary
  property_count: 10
  slug: well-architected-tool-lens-summary
- name: LensType
  property_count: 0
  slug: well-architected-tool-lens-type
- name: LensUpgradeSummary
  property_count: 6
  slug: well-architected-tool-lens-upgrade-summary
- name: LensVersion
  property_count: 0
  slug: well-architected-tool-lens-version
- name: LensesAppliedCount
  property_count: 0
  slug: well-architected-tool-lenses-applied-count
- name: ListAnswersInput
  property_count: 0
  slug: well-architected-tool-list-answers-input
- name: ListAnswersMaxResults
  property_count: 0
  slug: well-architected-tool-list-answers-max-results
- name: ListAnswersOutput
  property_count: 6
  slug: well-architected-tool-list-answers-output
- name: ListCheckDetailsInput
  property_count: 6
  slug: well-architected-tool-list-check-details-input
- name: ListCheckDetailsOutput
  property_count: 2
  slug: well-architected-tool-list-check-details-output
- name: ListCheckSummariesInput
  property_count: 6
  slug: well-architected-tool-list-check-summaries-input
- name: ListCheckSummariesOutput
  property_count: 2
  slug: well-architected-tool-list-check-summaries-output
- name: ListLensReviewImprovementsInput
  property_count: 0
  slug: well-architected-tool-list-lens-review-improvements-input
- name: ListLensReviewImprovementsMaxResults
  property_count: 0
  slug: well-architected-tool-list-lens-review-improvements-max-results
- name: ListLensReviewImprovementsOutput
  property_count: 6
  slug: well-architected-tool-list-lens-review-improvements-output
- name: ListLensReviewsInput
  property_count: 0
  slug: well-architected-tool-list-lens-reviews-input
- name: ListLensReviewsOutput
  property_count: 4
  slug: well-architected-tool-list-lens-reviews-output
- name: ListLensSharesInput
  property_count: 0
  slug: well-architected-tool-list-lens-shares-input
- name: ListLensSharesOutput
  property_count: 2
  slug: well-architected-tool-list-lens-shares-output
- name: ListLensesInput
  property_count: 0
  slug: well-architected-tool-list-lenses-input
- name: ListLensesOutput
  property_count: 2
  slug: well-architected-tool-list-lenses-output
- name: ListMilestonesInput
  property_count: 2
  slug: well-architected-tool-list-milestones-input
- name: ListMilestonesOutput
  property_count: 3
  slug: well-architected-tool-list-milestones-output
- name: ListNotificationsInput
  property_count: 3
  slug: well-architected-tool-list-notifications-input
- name: ListNotificationsMaxResults
  property_count: 0
  slug: well-architected-tool-list-notifications-max-results
- name: ListNotificationsOutput
  property_count: 2
  slug: well-architected-tool-list-notifications-output
- name: ListProfileNotificationsInput
  property_count: 0
  slug: well-architected-tool-list-profile-notifications-input
- name: ListProfileNotificationsOutput
  property_count: 2
  slug: well-architected-tool-list-profile-notifications-output
- name: ListProfileSharesInput
  property_count: 0
  slug: well-architected-tool-list-profile-shares-input
- name: ListProfileSharesMaxResults
  property_count: 0
  slug: well-architected-tool-list-profile-shares-max-results
- name: ListProfileSharesOutput
  property_count: 2
  slug: well-architected-tool-list-profile-shares-output
- name: ListProfilesInput
  property_count: 0
  slug: well-architected-tool-list-profiles-input
- name: ListProfilesOutput
  property_count: 2
  slug: well-architected-tool-list-profiles-output
- name: ListShareInvitationsInput
  property_count: 0
  slug: well-architected-tool-list-share-invitations-input
- name: ListShareInvitationsMaxResults
  property_count: 0
  slug: well-architected-tool-list-share-invitations-max-results
- name: ListShareInvitationsOutput
  property_count: 2
  slug: well-architected-tool-list-share-invitations-output
- name: ListTagsForResourceInput
  property_count: 0
  slug: well-architected-tool-list-tags-for-resource-input
- name: ListTagsForResourceOutput
  property_count: 1
  slug: well-architected-tool-list-tags-for-resource-output
- name: ListWorkloadSharesInput
  property_count: 0
  slug: well-architected-tool-list-workload-shares-input
- name: ListWorkloadSharesMaxResults
  property_count: 0
  slug: well-architected-tool-list-workload-shares-max-results
- name: ListWorkloadSharesOutput
  property_count: 3
  slug: well-architected-tool-list-workload-shares-output
- name: ListWorkloadsInput
  property_count: 3
  slug: well-architected-tool-list-workloads-input
- name: ListWorkloadsMaxResults
  property_count: 0
  slug: well-architected-tool-list-workloads-max-results
- name: ListWorkloadsOutput
  property_count: 2
  slug: well-architected-tool-list-workloads-output
- name: MaxResults
  property_count: 0
  slug: well-architected-tool-max-results
- name: MaxSelectedProfileChoices
  property_count: 0
  slug: well-architected-tool-max-selected-profile-choices
- name: MetricType
  property_count: 0
  slug: well-architected-tool-metric-type
- name: MilestoneName
  property_count: 0
  slug: well-architected-tool-milestone-name
- name: MilestoneNumber
  property_count: 0
  slug: well-architected-tool-milestone-number
- name: Milestone
  property_count: 4
  slug: well-architected-tool-milestone
- name: MilestoneSummaries
  property_count: 0
  slug: well-architected-tool-milestone-summaries
- name: MilestoneSummary
  property_count: 4
  slug: well-architected-tool-milestone-summary
- name: MinSelectedProfileChoices
  property_count: 0
  slug: well-architected-tool-min-selected-profile-choices
- name: NextToken
  property_count: 0
  slug: well-architected-tool-next-token
- name: Notes
  property_count: 0
  slug: well-architected-tool-notes
- name: NotificationSummaries
  property_count: 0
  slug: well-architected-tool-notification-summaries
- name: NotificationSummary
  property_count: 2
  slug: well-architected-tool-notification-summary
- name: NotificationType
  property_count: 0
  slug: well-architected-tool-notification-type
- name: OrganizationSharingStatus
  property_count: 0
  slug: well-architected-tool-organization-sharing-status
- name: PermissionType
  property_count: 0
  slug: well-architected-tool-permission-type
- name: PillarDifference
  property_count: 4
  slug: well-architected-tool-pillar-difference
- name: PillarDifferences
  property_count: 0
  slug: well-architected-tool-pillar-differences
- name: PillarId
  property_count: 0
  slug: well-architected-tool-pillar-id
- name: PillarMetric
  property_count: 3
  slug: well-architected-tool-pillar-metric
- name: PillarMetrics
  property_count: 0
  slug: well-architected-tool-pillar-metrics
- name: PillarName
  property_count: 0
  slug: well-architected-tool-pillar-name
- name: PillarNotes
  property_count: 0
  slug: well-architected-tool-pillar-notes
- name: PillarReviewSummaries
  property_count: 0
  slug: well-architected-tool-pillar-review-summaries
- name: PillarReviewSummary
  property_count: 5
  slug: well-architected-tool-pillar-review-summary
- name: ProfileArn
  property_count: 0
  slug: well-architected-tool-profile-arn
- name: ProfileArns
  property_count: 0
  slug: well-architected-tool-profile-arns
- name: ProfileChoice
  property_count: 3
  slug: well-architected-tool-profile-choice
- name: ProfileDescription
  property_count: 0
  slug: well-architected-tool-profile-description
- name: ProfileNamePrefix
  property_count: 0
  slug: well-architected-tool-profile-name-prefix
- name: ProfileName
  property_count: 0
  slug: well-architected-tool-profile-name
- name: ProfileNotificationSummaries
  property_count: 0
  slug: well-architected-tool-profile-notification-summaries
- name: ProfileNotificationSummary
  property_count: 7
  slug: well-architected-tool-profile-notification-summary
- name: ProfileNotificationType
  property_count: 0
  slug: well-architected-tool-profile-notification-type
- name: ProfileOwnerType
  property_count: 0
  slug: well-architected-tool-profile-owner-type
- name: ProfileQuestionChoices
  property_count: 0
  slug: well-architected-tool-profile-question-choices
- name: ProfileQuestion
  property_count: 7
  slug: well-architected-tool-profile-question
- name: ProfileQuestionUpdate
  property_count: 2
  slug: well-architected-tool-profile-question-update
- name: ProfileQuestionUpdates
  property_count: 0
  slug: well-architected-tool-profile-question-updates
- name: ProfileQuestions
  property_count: 0
  slug: well-architected-tool-profile-questions
- name: Profile
  property_count: 10
  slug: well-architected-tool-profile
- name: ProfileShareSummaries
  property_count: 0
  slug: well-architected-tool-profile-share-summaries
- name: ProfileShareSummary
  property_count: 4
  slug: well-architected-tool-profile-share-summary
- name: ProfileSummaries
  property_count: 0
  slug: well-architected-tool-profile-summaries
- name: ProfileSummary
  property_count: 7
  slug: well-architected-tool-profile-summary
- name: ProfileTemplateChoice
  property_count: 3
  slug: well-architected-tool-profile-template-choice
- name: ProfileTemplateQuestionChoices
  property_count: 0
  slug: well-architected-tool-profile-template-question-choices
- name: ProfileTemplateQuestion
  property_count: 6
  slug: well-architected-tool-profile-template-question
- name: ProfileTemplate
  property_count: 4
  slug: well-architected-tool-profile-template
- name: ProfileVersion
  property_count: 0
  slug: well-architected-tool-profile-version
- name: QuestionDescription
  property_count: 0
  slug: well-architected-tool-question-description
- name: QuestionDifference
  property_count: 3
  slug: well-architected-tool-question-difference
- name: QuestionDifferences
  property_count: 0
  slug: well-architected-tool-question-differences
- name: QuestionId
  property_count: 0
  slug: well-architected-tool-question-id
- name: QuestionMetric
  property_count: 3
  slug: well-architected-tool-question-metric
- name: QuestionMetrics
  property_count: 0
  slug: well-architected-tool-question-metrics
- name: QuestionPriority
  property_count: 0
  slug: well-architected-tool-question-priority
- name: QuestionTitle
  property_count: 0
  slug: well-architected-tool-question-title
- name: QuestionType
  property_count: 0
  slug: well-architected-tool-question-type
- name: ReportFormat
  property_count: 0
  slug: well-architected-tool-report-format
- name: ResourceNotFoundException
  property_count: 0
  slug: well-architected-tool-resource-not-found-exception
- name: RiskCounts
  property_count: 0
  slug: well-architected-tool-risk-counts
- name: Risk
  property_count: 0
  slug: well-architected-tool-risk
- name: SelectedChoiceIds
  property_count: 0
  slug: well-architected-tool-selected-choice-ids
- name: SelectedChoices
  property_count: 0
  slug: well-architected-tool-selected-choices
- name: SelectedProfileChoiceIds
  property_count: 0
  slug: well-architected-tool-selected-profile-choice-ids
- name: ServiceQuotaExceededException
  property_count: 0
  slug: well-architected-tool-service-quota-exceeded-exception
- name: ShareId
  property_count: 0
  slug: well-architected-tool-share-id
- name: ShareInvitationAction
  property_count: 0
  slug: well-architected-tool-share-invitation-action
- name: ShareInvitationId
  property_count: 0
  slug: well-architected-tool-share-invitation-id
- name: ShareInvitation
  property_count: 6
  slug: well-architected-tool-share-invitation
- name: ShareInvitationSummaries
  property_count: 0
  slug: well-architected-tool-share-invitation-summaries
- name: ShareInvitationSummary
  property_count: 11
  slug: well-architected-tool-share-invitation-summary
- name: ShareResourceType
  property_count: 0
  slug: well-architected-tool-share-resource-type
- name: ShareStatus
  property_count: 0
  slug: well-architected-tool-share-status
- name: SharedWithPrefix
  property_count: 0
  slug: well-architected-tool-shared-with-prefix
- name: SharedWith
  property_count: 0
  slug: well-architected-tool-shared-with
- name: StatusMessage
  property_count: 0
  slug: well-architected-tool-status-message
- name: TagKeyList
  property_count: 0
  slug: well-architected-tool-tag-key-list
- name: TagKey
  property_count: 0
  slug: well-architected-tool-tag-key
- name: TagMap
  property_count: 0
  slug: well-architected-tool-tag-map
- name: TagResourceInput
  property_count: 1
  slug: well-architected-tool-tag-resource-input
- name: TagResourceOutput
  property_count: 0
  slug: well-architected-tool-tag-resource-output
- name: TagValue
  property_count: 0
  slug: well-architected-tool-tag-value
- name: TemplateQuestions
  property_count: 0
  slug: well-architected-tool-template-questions
- name: ThrottlingException
  property_count: 0
  slug: well-architected-tool-throttling-exception
- name: Timestamp
  property_count: 0
  slug: well-architected-tool-timestamp
- name: TrustedAdvisorIntegrationStatus
  property_count: 0
  slug: well-architected-tool-trusted-advisor-integration-status
- name: UntagResourceInput
  property_count: 0
  slug: well-architected-tool-untag-resource-input
- name: UntagResourceOutput
  property_count: 0
  slug: well-architected-tool-untag-resource-output
- name: UpdateAnswerInput
  property_count: 5
  slug: well-architected-tool-update-answer-input
- name: UpdateAnswerOutput
  property_count: 4
  slug: well-architected-tool-update-answer-output
- name: UpdateGlobalSettingsInput
  property_count: 2
  slug: well-architected-tool-update-global-settings-input
- name: UpdateLensReviewInput
  property_count: 2
  slug: well-architected-tool-update-lens-review-input
- name: UpdateLensReviewOutput
  property_count: 2
  slug: well-architected-tool-update-lens-review-output
- name: UpdateProfileInput
  property_count: 2
  slug: well-architected-tool-update-profile-input
- name: UpdateProfileOutput
  property_count: 1
  slug: well-architected-tool-update-profile-output
- name: UpdateShareInvitationInput
  property_count: 1
  slug: well-architected-tool-update-share-invitation-input
- name: UpdateShareInvitationOutput
  property_count: 1
  slug: well-architected-tool-update-share-invitation-output
- name: UpdateWorkloadInput
  property_count: 16
  slug: well-architected-tool-update-workload-input
- name: UpdateWorkloadOutput
  property_count: 1
  slug: well-architected-tool-update-workload-output
- name: UpdateWorkloadShareInput
  property_count: 1
  slug: well-architected-tool-update-workload-share-input
- name: UpdateWorkloadShareOutput
  property_count: 2
  slug: well-architected-tool-update-workload-share-output
- name: UpgradeLensReviewInput
  property_count: 2
  slug: well-architected-tool-upgrade-lens-review-input
- name: UpgradeProfileVersionInput
  property_count: 2
  slug: well-architected-tool-upgrade-profile-version-input
- name: Urls
  property_count: 0
  slug: well-architected-tool-urls
- name: VersionDifferences
  property_count: 1
  slug: well-architected-tool-version-differences
- name: WorkloadAccountIds
  property_count: 0
  slug: well-architected-tool-workload-account-ids
- name: WorkloadApplications
  property_count: 0
  slug: well-architected-tool-workload-applications
- name: WorkloadArchitecturalDesign
  property_count: 0
  slug: well-architected-tool-workload-architectural-design
- name: WorkloadArn
  property_count: 0
  slug: well-architected-tool-workload-arn
- name: WorkloadAwsRegions
  property_count: 0
  slug: well-architected-tool-workload-aws-regions
- name: WorkloadDescription
  property_count: 0
  slug: well-architected-tool-workload-description
- name: WorkloadDiscoveryConfig
  property_count: 2
  slug: well-architected-tool-workload-discovery-config
- name: WorkloadEnvironment
  property_count: 0
  slug: well-architected-tool-workload-environment
- name: WorkloadId
  property_count: 0
  slug: well-architected-tool-workload-id
- name: WorkloadImprovementStatus
  property_count: 0
  slug: well-architected-tool-workload-improvement-status
- name: WorkloadIndustry
  property_count: 0
  slug: well-architected-tool-workload-industry
- name: WorkloadIndustryType
  property_count: 0
  slug: well-architected-tool-workload-industry-type
- name: WorkloadLenses
  property_count: 0
  slug: well-architected-tool-workload-lenses
- name: WorkloadNamePrefix
  property_count: 0
  slug: well-architected-tool-workload-name-prefix
- name: WorkloadName
  property_count: 0
  slug: well-architected-tool-workload-name
- name: WorkloadNonAwsRegion
  property_count: 0
  slug: well-architected-tool-workload-non-aws-region
- name: WorkloadNonAwsRegions
  property_count: 0
  slug: well-architected-tool-workload-non-aws-regions
- name: WorkloadPillarPriorities
  property_count: 0
  slug: well-architected-tool-workload-pillar-priorities
- name: WorkloadProfileArns
  property_count: 0
  slug: well-architected-tool-workload-profile-arns
- name: WorkloadProfile
  property_count: 2
  slug: well-architected-tool-workload-profile
- name: WorkloadProfiles
  property_count: 0
  slug: well-architected-tool-workload-profiles
- name: WorkloadResourceDefinition
  property_count: 0
  slug: well-architected-tool-workload-resource-definition
- name: WorkloadReviewOwner
  property_count: 0
  slug: well-architected-tool-workload-review-owner
- name: Workload
  property_count: 27
  slug: well-architected-tool-workload
- name: WorkloadShare
  property_count: 7
  slug: well-architected-tool-workload-share
- name: WorkloadShareSummaries
  property_count: 0
  slug: well-architected-tool-workload-share-summaries
- name: WorkloadShareSummary
  property_count: 5
  slug: well-architected-tool-workload-share-summary
- name: WorkloadSummaries
  property_count: 0
  slug: well-architected-tool-workload-summaries
- name: WorkloadSummary
  property_count: 10
  slug: well-architected-tool-workload-summary
json_structures:
- name: Well Architected Tool Access Denied Exception Structure
  property_count: 0
  slug: well-architected-tool-access-denied-exception-structure
- name: Well Architected Tool Account Summary Structure
  property_count: 0
  slug: well-architected-tool-account-summary-structure
- name: Well Architected Tool Additional Resource Type Structure
  property_count: 0
  slug: well-architected-tool-additional-resource-type-structure
- name: Well Architected Tool Additional Resources List Structure
  property_count: 0
  slug: well-architected-tool-additional-resources-list-structure
- name: Well Architected Tool Additional Resources Structure
  property_count: 2
  slug: well-architected-tool-additional-resources-structure
- name: Well Architected Tool Answer Reason Structure
  property_count: 0
  slug: well-architected-tool-answer-reason-structure
- name: Well Architected Tool Answer Structure
  property_count: 14
  slug: well-architected-tool-answer-structure
- name: Well Architected Tool Answer Summaries Structure
  property_count: 0
  slug: well-architected-tool-answer-summaries-structure
- name: Well Architected Tool Answer Summary Structure
  property_count: 10
  slug: well-architected-tool-answer-summary-structure
- name: Well Architected Tool Application Arn Structure
  property_count: 0
  slug: well-architected-tool-application-arn-structure
- name: Well Architected Tool Associate Lenses Input Structure
  property_count: 1
  slug: well-architected-tool-associate-lenses-input-structure
- name: Well Architected Tool Associate Profiles Input Structure
  property_count: 1
  slug: well-architected-tool-associate-profiles-input-structure
- name: Well Architected Tool Aws Account Id Structure
  property_count: 0
  slug: well-architected-tool-aws-account-id-structure
- name: Well Architected Tool Aws Region Structure
  property_count: 0
  slug: well-architected-tool-aws-region-structure
- name: Well Architected Tool Base64 String Structure
  property_count: 0
  slug: well-architected-tool-base64-string-structure
- name: Well Architected Tool Best Practice Structure
  property_count: 2
  slug: well-architected-tool-best-practice-structure
- name: Well Architected Tool Best Practices Structure
  property_count: 0
  slug: well-architected-tool-best-practices-structure
- name: Well Architected Tool Check Description Structure
  property_count: 0
  slug: well-architected-tool-check-description-structure
- name: Well Architected Tool Check Detail Structure
  property_count: 13
  slug: well-architected-tool-check-detail-structure
- name: Well Architected Tool Check Details Structure
  property_count: 0
  slug: well-architected-tool-check-details-structure
- name: Well Architected Tool Check Failure Reason Structure
  property_count: 0
  slug: well-architected-tool-check-failure-reason-structure
- name: Well Architected Tool Check Id Structure
  property_count: 0
  slug: well-architected-tool-check-id-structure
- name: Well Architected Tool Check Name Structure
  property_count: 0
  slug: well-architected-tool-check-name-structure
- name: Well Architected Tool Check Provider Structure
  property_count: 0
  slug: well-architected-tool-check-provider-structure
- name: Well Architected Tool Check Status Count Structure
  property_count: 0
  slug: well-architected-tool-check-status-count-structure
- name: Well Architected Tool Check Status Structure
  property_count: 0
  slug: well-architected-tool-check-status-structure
- name: Well Architected Tool Check Summaries Structure
  property_count: 0
  slug: well-architected-tool-check-summaries-structure
- name: Well Architected Tool Check Summary Structure
  property_count: 11
  slug: well-architected-tool-check-summary-structure
- name: Well Architected Tool Choice Answer Structure
  property_count: 4
  slug: well-architected-tool-choice-answer-structure
- name: Well Architected Tool Choice Answer Summaries Structure
  property_count: 0
  slug: well-architected-tool-choice-answer-summaries-structure
- name: Well Architected Tool Choice Answer Summary Structure
  property_count: 3
  slug: well-architected-tool-choice-answer-summary-structure
- name: Well Architected Tool Choice Answers Structure
  property_count: 0
  slug: well-architected-tool-choice-answers-structure
- name: Well Architected Tool Choice Content Display Text Structure
  property_count: 0
  slug: well-architected-tool-choice-content-display-text-structure
- name: Well Architected Tool Choice Content Structure
  property_count: 2
  slug: well-architected-tool-choice-content-structure
- name: Well Architected Tool Choice Content Url Structure
  property_count: 0
  slug: well-architected-tool-choice-content-url-structure
- name: Well Architected Tool Choice Description Structure
  property_count: 0
  slug: well-architected-tool-choice-description-structure
- name: Well Architected Tool Choice Id Structure
  property_count: 0
  slug: well-architected-tool-choice-id-structure
- name: Well Architected Tool Choice Improvement Plan Structure
  property_count: 3
  slug: well-architected-tool-choice-improvement-plan-structure
- name: Well Architected Tool Choice Improvement Plans Structure
  property_count: 0
  slug: well-architected-tool-choice-improvement-plans-structure
- name: Well Architected Tool Choice Notes Structure
  property_count: 0
  slug: well-architected-tool-choice-notes-structure
- name: Well Architected Tool Choice Reason Structure
  property_count: 0
  slug: well-architected-tool-choice-reason-structure
- name: Well Architected Tool Choice Status Structure
  property_count: 0
  slug: well-architected-tool-choice-status-structure
- name: Well Architected Tool Choice Structure
  property_count: 6
  slug: well-architected-tool-choice-structure
- name: Well Architected Tool Choice Title Structure
  property_count: 0
  slug: well-architected-tool-choice-title-structure
- name: Well Architected Tool Choice Update Structure
  property_count: 3
  slug: well-architected-tool-choice-update-structure
- name: Well Architected Tool Choice Updates Structure
  property_count: 0
  slug: well-architected-tool-choice-updates-structure
- name: Well Architected Tool Choices Structure
  property_count: 0
  slug: well-architected-tool-choices-structure
- name: Well Architected Tool Client Request Token Structure
  property_count: 0
  slug: well-architected-tool-client-request-token-structure
- name: Well Architected Tool Conflict Exception Structure
  property_count: 0
  slug: well-architected-tool-conflict-exception-structure
- name: Well Architected Tool Consolidated Report Metric Structure
  property_count: 8
  slug: well-architected-tool-consolidated-report-metric-structure
- name: Well Architected Tool Consolidated Report Metrics Structure
  property_count: 0
  slug: well-architected-tool-consolidated-report-metrics-structure
- name: Well Architected Tool Count Structure
  property_count: 0
  slug: well-architected-tool-count-structure
- name: Well Architected Tool Create Lens Share Input Structure
  property_count: 2
  slug: well-architected-tool-create-lens-share-input-structure
- name: Well Architected Tool Create Lens Share Output Structure
  property_count: 1
  slug: well-architected-tool-create-lens-share-output-structure
- name: Well Architected Tool Create Lens Version Input Structure
  property_count: 3
  slug: well-architected-tool-create-lens-version-input-structure
- name: Well Architected Tool Create Lens Version Output Structure
  property_count: 2
  slug: well-architected-tool-create-lens-version-output-structure
- name: Well Architected Tool Create Milestone Input Structure
  property_count: 2
  slug: well-architected-tool-create-milestone-input-structure
- name: Well Architected Tool Create Milestone Output Structure
  property_count: 2
  slug: well-architected-tool-create-milestone-output-structure
- name: Well Architected Tool Create Profile Input Structure
  property_count: 5
  slug: well-architected-tool-create-profile-input-structure
- name: Well Architected Tool Create Profile Output Structure
  property_count: 2
  slug: well-architected-tool-create-profile-output-structure
- name: Well Architected Tool Create Profile Share Input Structure
  property_count: 2
  slug: well-architected-tool-create-profile-share-input-structure
- name: Well Architected Tool Create Profile Share Output Structure
  property_count: 2
  slug: well-architected-tool-create-profile-share-output-structure
- name: Well Architected Tool Create Workload Input Structure
  property_count: 18
  slug: well-architected-tool-create-workload-input-structure
- name: Well Architected Tool Create Workload Output Structure
  property_count: 2
  slug: well-architected-tool-create-workload-output-structure
- name: Well Architected Tool Create Workload Share Input Structure
  property_count: 3
  slug: well-architected-tool-create-workload-share-input-structure
- name: Well Architected Tool Create Workload Share Output Structure
  property_count: 2
  slug: well-architected-tool-create-workload-share-output-structure
- name: Well Architected Tool Definition Type Structure
  property_count: 0
  slug: well-architected-tool-definition-type-structure
- name: Well Architected Tool Delete Lens Input Structure
  property_count: 0
  slug: well-architected-tool-delete-lens-input-structure
- name: Well Architected Tool Delete Lens Share Input Structure
  property_count: 0
  slug: well-architected-tool-delete-lens-share-input-structure
- name: Well Architected Tool Delete Profile Input Structure
  property_count: 0
  slug: well-architected-tool-delete-profile-input-structure
- name: Well Architected Tool Delete Profile Share Input Structure
  property_count: 0
  slug: well-architected-tool-delete-profile-share-input-structure
- name: Well Architected Tool Delete Workload Input Structure
  property_count: 0
  slug: well-architected-tool-delete-workload-input-structure
- name: Well Architected Tool Delete Workload Share Input Structure
  property_count: 0
  slug: well-architected-tool-delete-workload-share-input-structure
- name: Well Architected Tool Difference Status Structure
  property_count: 0
  slug: well-architected-tool-difference-status-structure
- name: Well Architected Tool Disassociate Lenses Input Structure
  property_count: 1
  slug: well-architected-tool-disassociate-lenses-input-structure
- name: Well Architected Tool Disassociate Profiles Input Structure
  property_count: 1
  slug: well-architected-tool-disassociate-profiles-input-structure
- name: Well Architected Tool Discovery Integration Status Structure
  property_count: 0
  slug: well-architected-tool-discovery-integration-status-structure
- name: Well Architected Tool Display Text Structure
  property_count: 0
  slug: well-architected-tool-display-text-structure
- name: Well Architected Tool Export Lens Input Structure
  property_count: 0
  slug: well-architected-tool-export-lens-input-structure
- name: Well Architected Tool Export Lens Output Structure
  property_count: 1
  slug: well-architected-tool-export-lens-output-structure
- name: Well Architected Tool Flagged Resources Structure
  property_count: 0
  slug: well-architected-tool-flagged-resources-structure
- name: Well Architected Tool Get Answer Input Structure
  property_count: 0
  slug: well-architected-tool-get-answer-input-structure
- name: Well Architected Tool Get Answer Output Structure
  property_count: 5
  slug: well-architected-tool-get-answer-output-structure
- name: Well Architected Tool Get Consolidated Report Input Structure
  property_count: 0
  slug: well-architected-tool-get-consolidated-report-input-structure
- name: Well Architected Tool Get Consolidated Report Max Results Structure
  property_count: 0
  slug: well-architected-tool-get-consolidated-report-max-results-structure
- name: Well Architected Tool Get Consolidated Report Output Structure
  property_count: 3
  slug: well-architected-tool-get-consolidated-report-output-structure
- name: Well Architected Tool Get Lens Input Structure
  property_count: 0
  slug: well-architected-tool-get-lens-input-structure
- name: Well Architected Tool Get Lens Output Structure
  property_count: 1
  slug: well-architected-tool-get-lens-output-structure
- name: Well Architected Tool Get Lens Review Input Structure
  property_count: 0
  slug: well-architected-tool-get-lens-review-input-structure
- name: Well Architected Tool Get Lens Review Output Structure
  property_count: 3
  slug: well-architected-tool-get-lens-review-output-structure
- name: Well Architected Tool Get Lens Review Report Input Structure
  property_count: 0
  slug: well-architected-tool-get-lens-review-report-input-structure
- name: Well Architected Tool Get Lens Review Report Output Structure
  property_count: 3
  slug: well-architected-tool-get-lens-review-report-output-structure
- name: Well Architected Tool Get Lens Version Difference Input Structure
  property_count: 0
  slug: well-architected-tool-get-lens-version-difference-input-structure
- name: Well Architected Tool Get Lens Version Difference Output Structure
  property_count: 6
  slug: well-architected-tool-get-lens-version-difference-output-structure
- name: Well Architected Tool Get Milestone Input Structure
  property_count: 0
  slug: well-architected-tool-get-milestone-input-structure
- name: Well Architected Tool Get Milestone Output Structure
  property_count: 2
  slug: well-architected-tool-get-milestone-output-structure
- name: Well Architected Tool Get Profile Input Structure
  property_count: 0
  slug: well-architected-tool-get-profile-input-structure
- name: Well Architected Tool Get Profile Output Structure
  property_count: 1
  slug: well-architected-tool-get-profile-output-structure
- name: Well Architected Tool Get Profile Template Input Structure
  property_count: 0
  slug: well-architected-tool-get-profile-template-input-structure
- name: Well Architected Tool Get Profile Template Output Structure
  property_count: 1
  slug: well-architected-tool-get-profile-template-output-structure
- name: Well Architected Tool Get Workload Input Structure
  property_count: 0
  slug: well-architected-tool-get-workload-input-structure
- name: Well Architected Tool Get Workload Output Structure
  property_count: 1
  slug: well-architected-tool-get-workload-output-structure
- name: Well Architected Tool Helpful Resource Url Structure
  property_count: 0
  slug: well-architected-tool-helpful-resource-url-structure
- name: Well Architected Tool Import Lens Input Structure
  property_count: 4
  slug: well-architected-tool-import-lens-input-structure
- name: Well Architected Tool Import Lens Output Structure
  property_count: 2
  slug: well-architected-tool-import-lens-output-structure
- name: Well Architected Tool Import Lens Status Structure
  property_count: 0
  slug: well-architected-tool-import-lens-status-structure
- name: Well Architected Tool Improvement Plan Url Structure
  property_count: 0
  slug: well-architected-tool-improvement-plan-url-structure
- name: Well Architected Tool Improvement Summaries Structure
  property_count: 0
  slug: well-architected-tool-improvement-summaries-structure
- name: Well Architected Tool Improvement Summary Structure
  property_count: 6
  slug: well-architected-tool-improvement-summary-structure
- name: Well Architected Tool Include Shared Resources Structure
  property_count: 0
  slug: well-architected-tool-include-shared-resources-structure
- name: Well Architected Tool Internal Server Exception Structure
  property_count: 0
  slug: well-architected-tool-internal-server-exception-structure
- name: Well Architected Tool Is Applicable Structure
  property_count: 0
  slug: well-architected-tool-is-applicable-structure
- name: Well Architected Tool Is Major Version Structure
  property_count: 0
  slug: well-architected-tool-is-major-version-structure
- name: Well Architected Tool Is Review Owner Update Acknowledged Structure
  property_count: 0
  slug: well-architected-tool-is-review-owner-update-acknowledged-structure
- name: Well Architected Tool Lens Alias Structure
  property_count: 0
  slug: well-architected-tool-lens-alias-structure
- name: Well Architected Tool Lens Aliases Structure
  property_count: 0
  slug: well-architected-tool-lens-aliases-structure
- name: Well Architected Tool Lens Arn Structure
  property_count: 0
  slug: well-architected-tool-lens-arn-structure
- name: Well Architected Tool Lens Description Structure
  property_count: 0
  slug: well-architected-tool-lens-description-structure
- name: Well Architected Tool Lens Json Structure
  property_count: 0
  slug: well-architected-tool-lens-json-structure
- name: Well Architected Tool Lens Metric Structure
  property_count: 3
  slug: well-architected-tool-lens-metric-structure
- name: Well Architected Tool Lens Metrics Structure
  property_count: 0
  slug: well-architected-tool-lens-metrics-structure
- name: Well Architected Tool Lens Name Prefix Structure
  property_count: 0
  slug: well-architected-tool-lens-name-prefix-structure
- name: Well Architected Tool Lens Name Structure
  property_count: 0
  slug: well-architected-tool-lens-name-structure
- name: Well Architected Tool Lens Owner Structure
  property_count: 0
  slug: well-architected-tool-lens-owner-structure
- name: Well Architected Tool Lens Review Report Structure
  property_count: 3
  slug: well-architected-tool-lens-review-report-structure
- name: Well Architected Tool Lens Review Structure
  property_count: 12
  slug: well-architected-tool-lens-review-structure
- name: Well Architected Tool Lens Review Summaries Structure
  property_count: 0
  slug: well-architected-tool-lens-review-summaries-structure
- name: Well Architected Tool Lens Review Summary Structure
  property_count: 9
  slug: well-architected-tool-lens-review-summary-structure
- name: Well Architected Tool Lens Share Summaries Structure
  property_count: 0
  slug: well-architected-tool-lens-share-summaries-structure
- name: Well Architected Tool Lens Share Summary Structure
  property_count: 4
  slug: well-architected-tool-lens-share-summary-structure
- name: Well Architected Tool Lens Status Structure
  property_count: 0
  slug: well-architected-tool-lens-status-structure
- name: Well Architected Tool Lens Status Type Structure
  property_count: 0
  slug: well-architected-tool-lens-status-type-structure
- name: Well Architected Tool Lens Structure
  property_count: 7
  slug: well-architected-tool-lens-structure
- name: Well Architected Tool Lens Summaries Structure
  property_count: 0
  slug: well-architected-tool-lens-summaries-structure
- name: Well Architected Tool Lens Summary Structure
  property_count: 10
  slug: well-architected-tool-lens-summary-structure
- name: Well Architected Tool Lens Type Structure
  property_count: 0
  slug: well-architected-tool-lens-type-structure
- name: Well Architected Tool Lens Upgrade Summary Structure
  property_count: 6
  slug: well-architected-tool-lens-upgrade-summary-structure
- name: Well Architected Tool Lens Version Structure
  property_count: 0
  slug: well-architected-tool-lens-version-structure
- name: Well Architected Tool Lenses Applied Count Structure
  property_count: 0
  slug: well-architected-tool-lenses-applied-count-structure
- name: Well Architected Tool List Answers Input Structure
  property_count: 0
  slug: well-architected-tool-list-answers-input-structure
- name: Well Architected Tool List Answers Max Results Structure
  property_count: 0
  slug: well-architected-tool-list-answers-max-results-structure
- name: Well Architected Tool List Answers Output Structure
  property_count: 6
  slug: well-architected-tool-list-answers-output-structure
- name: Well Architected Tool List Check Details Input Structure
  property_count: 6
  slug: well-architected-tool-list-check-details-input-structure
- name: Well Architected Tool List Check Details Output Structure
  property_count: 2
  slug: well-architected-tool-list-check-details-output-structure
- name: Well Architected Tool List Check Summaries Input Structure
  property_count: 6
  slug: well-architected-tool-list-check-summaries-input-structure
- name: Well Architected Tool List Check Summaries Output Structure
  property_count: 2
  slug: well-architected-tool-list-check-summaries-output-structure
- name: Well Architected Tool List Lens Review Improvements Input Structure
  property_count: 0
  slug: well-architected-tool-list-lens-review-improvements-input-structure
- name: Well Architected Tool List Lens Review Improvements Max Results Structure
  property_count: 0
  slug: well-architected-tool-list-lens-review-improvements-max-results-structure
- name: Well Architected Tool List Lens Review Improvements Output Structure
  property_count: 6
  slug: well-architected-tool-list-lens-review-improvements-output-structure
- name: Well Architected Tool List Lens Reviews Input Structure
  property_count: 0
  slug: well-architected-tool-list-lens-reviews-input-structure
- name: Well Architected Tool List Lens Reviews Output Structure
  property_count: 4
  slug: well-architected-tool-list-lens-reviews-output-structure
- name: Well Architected Tool List Lens Shares Input Structure
  property_count: 0
  slug: well-architected-tool-list-lens-shares-input-structure
- name: Well Architected Tool List Lens Shares Output Structure
  property_count: 2
  slug: well-architected-tool-list-lens-shares-output-structure
- name: Well Architected Tool List Lenses Input Structure
  property_count: 0
  slug: well-architected-tool-list-lenses-input-structure
- name: Well Architected Tool List Lenses Output Structure
  property_count: 2
  slug: well-architected-tool-list-lenses-output-structure
- name: Well Architected Tool List Milestones Input Structure
  property_count: 2
  slug: well-architected-tool-list-milestones-input-structure
- name: Well Architected Tool List Milestones Output Structure
  property_count: 3
  slug: well-architected-tool-list-milestones-output-structure
- name: Well Architected Tool List Notifications Input Structure
  property_count: 3
  slug: well-architected-tool-list-notifications-input-structure
- name: Well Architected Tool List Notifications Max Results Structure
  property_count: 0
  slug: well-architected-tool-list-notifications-max-results-structure
- name: Well Architected Tool List Notifications Output Structure
  property_count: 2
  slug: well-architected-tool-list-notifications-output-structure
- name: Well Architected Tool List Profile Notifications Input Structure
  property_count: 0
  slug: well-architected-tool-list-profile-notifications-input-structure
- name: Well Architected Tool List Profile Notifications Output Structure
  property_count: 2
  slug: well-architected-tool-list-profile-notifications-output-structure
- name: Well Architected Tool List Profile Shares Input Structure
  property_count: 0
  slug: well-architected-tool-list-profile-shares-input-structure
- name: Well Architected Tool List Profile Shares Max Results Structure
  property_count: 0
  slug: well-architected-tool-list-profile-shares-max-results-structure
- name: Well Architected Tool List Profile Shares Output Structure
  property_count: 2
  slug: well-architected-tool-list-profile-shares-output-structure
- name: Well Architected Tool List Profiles Input Structure
  property_count: 0
  slug: well-architected-tool-list-profiles-input-structure
- name: Well Architected Tool List Profiles Output Structure
  property_count: 2
  slug: well-architected-tool-list-profiles-output-structure
- name: Well Architected Tool List Share Invitations Input Structure
  property_count: 0
  slug: well-architected-tool-list-share-invitations-input-structure
- name: Well Architected Tool List Share Invitations Max Results Structure
  property_count: 0
  slug: well-architected-tool-list-share-invitations-max-results-structure
- name: Well Architected Tool List Share Invitations Output Structure
  property_count: 2
  slug: well-architected-tool-list-share-invitations-output-structure
- name: Well Architected Tool List Tags For Resource Input Structure
  property_count: 0
  slug: well-architected-tool-list-tags-for-resource-input-structure
- name: Well Architected Tool List Tags For Resource Output Structure
  property_count: 1
  slug: well-architected-tool-list-tags-for-resource-output-structure
- name: Well Architected Tool List Workload Shares Input Structure
  property_count: 0
  slug: well-architected-tool-list-workload-shares-input-structure
- name: Well Architected Tool List Workload Shares Max Results Structure
  property_count: 0
  slug: well-architected-tool-list-workload-shares-max-results-structure
- name: Well Architected Tool List Workload Shares Output Structure
  property_count: 3
  slug: well-architected-tool-list-workload-shares-output-structure
- name: Well Architected Tool List Workloads Input Structure
  property_count: 3
  slug: well-architected-tool-list-workloads-input-structure
- name: Well Architected Tool List Workloads Max Results Structure
  property_count: 0
  slug: well-architected-tool-list-workloads-max-results-structure
- name: Well Architected Tool List Workloads Output Structure
  property_count: 2
  slug: well-architected-tool-list-workloads-output-structure
- name: Well Architected Tool Max Results Structure
  property_count: 0
  slug: well-architected-tool-max-results-structure
- name: Well Architected Tool Max Selected Profile Choices Structure
  property_count: 0
  slug: well-architected-tool-max-selected-profile-choices-structure
- name: Well Architected Tool Metric Type Structure
  property_count: 0
  slug: well-architected-tool-metric-type-structure
- name: Well Architected Tool Milestone Name Structure
  property_count: 0
  slug: well-architected-tool-milestone-name-structure
- name: Well Architected Tool Milestone Number Structure
  property_count: 0
  slug: well-architected-tool-milestone-number-structure
- name: Well Architected Tool Milestone Structure
  property_count: 4
  slug: well-architected-tool-milestone-structure
- name: Well Architected Tool Milestone Summaries Structure
  property_count: 0
  slug: well-architected-tool-milestone-summaries-structure
- name: Well Architected Tool Milestone Summary Structure
  property_count: 4
  slug: well-architected-tool-milestone-summary-structure
- name: Well Architected Tool Min Selected Profile Choices Structure
  property_count: 0
  slug: well-architected-tool-min-selected-profile-choices-structure
- name: Well Architected Tool Next Token Structure
  property_count: 0
  slug: well-architected-tool-next-token-structure
- name: Well Architected Tool Notes Structure
  property_count: 0
  slug: well-architected-tool-notes-structure
- name: Well Architected Tool Notification Summaries Structure
  property_count: 0
  slug: well-architected-tool-notification-summaries-structure
- name: Well Architected Tool Notification Summary Structure
  property_count: 2
  slug: well-architected-tool-notification-summary-structure
- name: Well Architected Tool Notification Type Structure
  property_count: 0
  slug: well-architected-tool-notification-type-structure
- name: Well Architected Tool Organization Sharing Status Structure
  property_count: 0
  slug: well-architected-tool-organization-sharing-status-structure
- name: Well Architected Tool Permission Type Structure
  property_count: 0
  slug: well-architected-tool-permission-type-structure
- name: Well Architected Tool Pillar Difference Structure
  property_count: 4
  slug: well-architected-tool-pillar-difference-structure
- name: Well Architected Tool Pillar Differences Structure
  property_count: 0
  slug: well-architected-tool-pillar-differences-structure
- name: Well Architected Tool Pillar Id Structure
  property_count: 0
  slug: well-architected-tool-pillar-id-structure
- name: Well Architected Tool Pillar Metric Structure
  property_count: 3
  slug: well-architected-tool-pillar-metric-structure
- name: Well Architected Tool Pillar Metrics Structure
  property_count: 0
  slug: well-architected-tool-pillar-metrics-structure
- name: Well Architected Tool Pillar Name Structure
  property_count: 0
  slug: well-architected-tool-pillar-name-structure
- name: Well Architected Tool Pillar Notes Structure
  property_count: 0
  slug: well-architected-tool-pillar-notes-structure
- name: Well Architected Tool Pillar Review Summaries Structure
  property_count: 0
  slug: well-architected-tool-pillar-review-summaries-structure
- name: Well Architected Tool Pillar Review Summary Structure
  property_count: 5
  slug: well-architected-tool-pillar-review-summary-structure
- name: Well Architected Tool Profile Arn Structure
  property_count: 0
  slug: well-architected-tool-profile-arn-structure
- name: Well Architected Tool Profile Arns Structure
  property_count: 0
  slug: well-architected-tool-profile-arns-structure
- name: Well Architected Tool Profile Choice Structure
  property_count: 3
  slug: well-architected-tool-profile-choice-structure
- name: Well Architected Tool Profile Description Structure
  property_count: 0
  slug: well-architected-tool-profile-description-structure
- name: Well Architected Tool Profile Name Prefix Structure
  property_count: 0
  slug: well-architected-tool-profile-name-prefix-structure
- name: Well Architected Tool Profile Name Structure
  property_count: 0
  slug: well-architected-tool-profile-name-structure
- name: Well Architected Tool Profile Notification Summaries Structure
  property_count: 0
  slug: well-architected-tool-profile-notification-summaries-structure
- name: Well Architected Tool Profile Notification Summary Structure
  property_count: 7
  slug: well-architected-tool-profile-notification-summary-structure
- name: Well Architected Tool Profile Notification Type Structure
  property_count: 0
  slug: well-architected-tool-profile-notification-type-structure
- name: Well Architected Tool Profile Owner Type Structure
  property_count: 0
  slug: well-architected-tool-profile-owner-type-structure
- name: Well Architected Tool Profile Question Choices Structure
  property_count: 0
  slug: well-architected-tool-profile-question-choices-structure
- name: Well Architected Tool Profile Question Structure
  property_count: 7
  slug: well-architected-tool-profile-question-structure
- name: Well Architected Tool Profile Question Update Structure
  property_count: 2
  slug: well-architected-tool-profile-question-update-structure
- name: Well Architected Tool Profile Question Updates Structure
  property_count: 0
  slug: well-architected-tool-profile-question-updates-structure
- name: Well Architected Tool Profile Questions Structure
  property_count: 0
  slug: well-architected-tool-profile-questions-structure
- name: Well Architected Tool Profile Share Summaries Structure
  property_count: 0
  slug: well-architected-tool-profile-share-summaries-structure
- name: Well Architected Tool Profile Share Summary Structure
  property_count: 4
  slug: well-architected-tool-profile-share-summary-structure
- name: Well Architected Tool Profile Structure
  property_count: 10
  slug: well-architected-tool-profile-structure
- name: Well Architected Tool Profile Summaries Structure
  property_count: 0
  slug: well-architected-tool-profile-summaries-structure
- name: Well Architected Tool Profile Summary Structure
  property_count: 7
  slug: well-architected-tool-profile-summary-structure
- name: Well Architected Tool Profile Template Choice Structure
  property_count: 3
  slug: well-architected-tool-profile-template-choice-structure
- name: Well Architected Tool Profile Template Question Choices Structure
  property_count: 0
  slug: well-architected-tool-profile-template-question-choices-structure
- name: Well Architected Tool Profile Template Question Structure
  property_count: 6
  slug: well-architected-tool-profile-template-question-structure
- name: Well Architected Tool Profile Template Structure
  property_count: 4
  slug: well-architected-tool-profile-template-structure
- name: Well Architected Tool Profile Version Structure
  property_count: 0
  slug: well-architected-tool-profile-version-structure
- name: Well Architected Tool Question Description Structure
  property_count: 0
  slug: well-architected-tool-question-description-structure
- name: Well Architected Tool Question Difference Structure
  property_count: 3
  slug: well-architected-tool-question-difference-structure
- name: Well Architected Tool Question Differences Structure
  property_count: 0
  slug: well-architected-tool-question-differences-structure
- name: Well Architected Tool Question Id Structure
  property_count: 0
  slug: well-architected-tool-question-id-structure
- name: Well Architected Tool Question Metric Structure
  property_count: 3
  slug: well-architected-tool-question-metric-structure
- name: Well Architected Tool Question Metrics Structure
  property_count: 0
  slug: well-architected-tool-question-metrics-structure
- name: Well Architected Tool Question Priority Structure
  property_count: 0
  slug: well-architected-tool-question-priority-structure
- name: Well Architected Tool Question Title Structure
  property_count: 0
  slug: well-architected-tool-question-title-structure
- name: Well Architected Tool Question Type Structure
  property_count: 0
  slug: well-architected-tool-question-type-structure
- name: Well Architected Tool Report Format Structure
  property_count: 0
  slug: well-architected-tool-report-format-structure
- name: Well Architected Tool Resource Not Found Exception Structure
  property_count: 0
  slug: well-architected-tool-resource-not-found-exception-structure
- name: Well Architected Tool Risk Counts Structure
  property_count: 0
  slug: well-architected-tool-risk-counts-structure
- name: Well Architected Tool Risk Structure
  property_count: 0
  slug: well-architected-tool-risk-structure
- name: Well Architected Tool Selected Choice Ids Structure
  property_count: 0
  slug: well-architected-tool-selected-choice-ids-structure
- name: Well Architected Tool Selected Choices Structure
  property_count: 0
  slug: well-architected-tool-selected-choices-structure
- name: Well Architected Tool Selected Profile Choice Ids Structure
  property_count: 0
  slug: well-architected-tool-selected-profile-choice-ids-structure
- name: Well Architected Tool Service Quota Exceeded Exception Structure
  property_count: 0
  slug: well-architected-tool-service-quota-exceeded-exception-structure
- name: Well Architected Tool Share Id Structure
  property_count: 0
  slug: well-architected-tool-share-id-structure
- name: Well Architected Tool Share Invitation Action Structure
  property_count: 0
  slug: well-architected-tool-share-invitation-action-structure
- name: Well Architected Tool Share Invitation Id Structure
  property_count: 0
  slug: well-architected-tool-share-invitation-id-structure
- name: Well Architected Tool Share Invitation Structure
  property_count: 6
  slug: well-architected-tool-share-invitation-structure
- name: Well Architected Tool Share Invitation Summaries Structure
  property_count: 0
  slug: well-architected-tool-share-invitation-summaries-structure
- name: Well Architected Tool Share Invitation Summary Structure
  property_count: 11
  slug: well-architected-tool-share-invitation-summary-structure
- name: Well Architected Tool Share Resource Type Structure
  property_count: 0
  slug: well-architected-tool-share-resource-type-structure
- name: Well Architected Tool Share Status Structure
  property_count: 0
  slug: well-architected-tool-share-status-structure
- name: Well Architected Tool Shared With Prefix Structure
  property_count: 0
  slug: well-architected-tool-shared-with-prefix-structure
- name: Well Architected Tool Shared With Structure
  property_count: 0
  slug: well-architected-tool-shared-with-structure
- name: Well Architected Tool Status Message Structure
  property_count: 0
  slug: well-architected-tool-status-message-structure
- name: Well Architected Tool Tag Key List Structure
  property_count: 0
  slug: well-architected-tool-tag-key-list-structure
- name: Well Architected Tool Tag Key Structure
  property_count: 0
  slug: well-architected-tool-tag-key-structure
- name: Well Architected Tool Tag Map Structure
  property_count: 0
  slug: well-architected-tool-tag-map-structure
- name: Well Architected Tool Tag Resource Input Structure
  property_count: 1
  slug: well-architected-tool-tag-resource-input-structure
- name: Well Architected Tool Tag Resource Output Structure
  property_count: 0
  slug: well-architected-tool-tag-resource-output-structure
- name: Well Architected Tool Tag Value Structure
  property_count: 0
  slug: well-architected-tool-tag-value-structure
- name: Well Architected Tool Template Questions Structure
  property_count: 0
  slug: well-architected-tool-template-questions-structure
- name: Well Architected Tool Throttling Exception Structure
  property_count: 0
  slug: well-architected-tool-throttling-exception-structure
- name: Well Architected Tool Timestamp Structure
  property_count: 0
  slug: well-architected-tool-timestamp-structure
- name: Well Architected Tool Trusted Advisor Integration Status Structure
  property_count: 0
  slug: well-architected-tool-trusted-advisor-integration-status-structure
- name: Well Architected Tool Untag Resource Input Structure
  property_count: 0
  slug: well-architected-tool-untag-resource-input-structure
- name: Well Architected Tool Untag Resource Output Structure
  property_count: 0
  slug: well-architected-tool-untag-resource-output-structure
- name: Well Architected Tool Update Answer Input Structure
  property_count: 5
  slug: well-architected-tool-update-answer-input-structure
- name: Well Architected Tool Update Answer Output Structure
  property_count: 4
  slug: well-architected-tool-update-answer-output-structure
- name: Well Architected Tool Update Global Settings Input Structure
  property_count: 2
  slug: well-architected-tool-update-global-settings-input-structure
- name: Well Architected Tool Update Lens Review Input Structure
  property_count: 2
  slug: well-architected-tool-update-lens-review-input-structure
- name: Well Architected Tool Update Lens Review Output Structure
  property_count: 2
  slug: well-architected-tool-update-lens-review-output-structure
- name: Well Architected Tool Update Profile Input Structure
  property_count: 2
  slug: well-architected-tool-update-profile-input-structure
- name: Well Architected Tool Update Profile Output Structure
  property_count: 1
  slug: well-architected-tool-update-profile-output-structure
- name: Well Architected Tool Update Share Invitation Input Structure
  property_count: 1
  slug: well-architected-tool-update-share-invitation-input-structure
- name: Well Architected Tool Update Share Invitation Output Structure
  property_count: 1
  slug: well-architected-tool-update-share-invitation-output-structure
- name: Well Architected Tool Update Workload Input Structure
  property_count: 16
  slug: well-architected-tool-update-workload-input-structure
- name: Well Architected Tool Update Workload Output Structure
  property_count: 1
  slug: well-architected-tool-update-workload-output-structure
- name: Well Architected Tool Update Workload Share Input Structure
  property_count: 1
  slug: well-architected-tool-update-workload-share-input-structure
- name: Well Architected Tool Update Workload Share Output Structure
  property_count: 2
  slug: well-architected-tool-update-workload-share-output-structure
- name: Well Architected Tool Upgrade Lens Review Input Structure
  property_count: 2
  slug: well-architected-tool-upgrade-lens-review-input-structure
- name: Well Architected Tool Upgrade Profile Version Input Structure
  property_count: 2
  slug: well-architected-tool-upgrade-profile-version-input-structure
- name: Well Architected Tool Urls Structure
  property_count: 0
  slug: well-architected-tool-urls-structure
- name: Well Architected Tool Version Differences Structure
  property_count: 1
  slug: well-architected-tool-version-differences-structure
- name: Well Architected Tool Workload Account Ids Structure
  property_count: 0
  slug: well-architected-tool-workload-account-ids-structure
- name: Well Architected Tool Workload Applications Structure
  property_count: 0
  slug: well-architected-tool-workload-applications-structure
- name: Well Architected Tool Workload Architectural Design Structure
  property_count: 0
  slug: well-architected-tool-workload-architectural-design-structure
- name: Well Architected Tool Workload Arn Structure
  property_count: 0
  slug: well-architected-tool-workload-arn-structure
- name: Well Architected Tool Workload Aws Regions Structure
  property_count: 0
  slug: well-architected-tool-workload-aws-regions-structure
- name: Well Architected Tool Workload Description Structure
  property_count: 0
  slug: well-architected-tool-workload-description-structure
- name: Well Architected Tool Workload Discovery Config Structure
  property_count: 2
  slug: well-architected-tool-workload-discovery-config-structure
- name: Well Architected Tool Workload Environment Structure
  property_count: 0
  slug: well-architected-tool-workload-environment-structure
- name: Well Architected Tool Workload Id Structure
  property_count: 0
  slug: well-architected-tool-workload-id-structure
- name: Well Architected Tool Workload Improvement Status Structure
  property_count: 0
  slug: well-architected-tool-workload-improvement-status-structure
- name: Well Architected Tool Workload Industry Structure
  property_count: 0
  slug: well-architected-tool-workload-industry-structure
- name: Well Architected Tool Workload Industry Type Structure
  property_count: 0
  slug: well-architected-tool-workload-industry-type-structure
- name: Well Architected Tool Workload Lenses Structure
  property_count: 0
  slug: well-architected-tool-workload-lenses-structure
- name: Well Architected Tool Workload Name Prefix Structure
  property_count: 0
  slug: well-architected-tool-workload-name-prefix-structure
- name: Well Architected Tool Workload Name Structure
  property_count: 0
  slug: well-architected-tool-workload-name-structure
- name: Well Architected Tool Workload Non Aws Region Structure
  property_count: 0
  slug: well-architected-tool-workload-non-aws-region-structure
- name: Well Architected Tool Workload Non Aws Regions Structure
  property_count: 0
  slug: well-architected-tool-workload-non-aws-regions-structure
- name: Well Architected Tool Workload Pillar Priorities Structure
  property_count: 0
  slug: well-architected-tool-workload-pillar-priorities-structure
- name: Well Architected Tool Workload Profile Arns Structure
  property_count: 0
  slug: well-architected-tool-workload-profile-arns-structure
- name: Well Architected Tool Workload Profile Structure
  property_count: 2
  slug: well-architected-tool-workload-profile-structure
- name: Well Architected Tool Workload Profiles Structure
  property_count: 0
  slug: well-architected-tool-workload-profiles-structure
- name: Well Architected Tool Workload Resource Definition Structure
  property_count: 0
  slug: well-architected-tool-workload-resource-definition-structure
- name: Well Architected Tool Workload Review Owner Structure
  property_count: 0
  slug: well-architected-tool-workload-review-owner-structure
- name: Well Architected Tool Workload Share Structure
  property_count: 7
  slug: well-architected-tool-workload-share-structure
- name: Well Architected Tool Workload Share Summaries Structure
  property_count: 0
  slug: well-architected-tool-workload-share-summaries-structure
- name: Well Architected Tool Workload Share Summary Structure
  property_count: 5
  slug: well-architected-tool-workload-share-summary-structure
- name: Well Architected Tool Workload Structure
  property_count: 27
  slug: well-architected-tool-workload-structure
- name: Well Architected Tool Workload Summaries Structure
  property_count: 0
  slug: well-architected-tool-workload-summaries-structure
- name: Well Architected Tool Workload Summary Structure
  property_count: 10
  slug: well-architected-tool-workload-summary-structure
jsonld:
- class_count: 146
  name: Amazon Well Architected Tool Context
  property_count: 139
  slug: amazon-well-architected-tool-context
layout: provider
modified: '2026-05-19'
name: Amazon Well-Architected Tool
nav: Providers
network: true
overview: 'Amazon Well-Architected Tool publishes 13 APIs on the [APIs.io](https://apis.io/) network, including ConsolidatedReport#Format API, Global Settings API, ImportLens API, and 10 more. Tagged areas include Architecture, Best Practices, Cloud Governance, Well-Architected, and Workloads.


  The Amazon Well-Architected Tool catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Well-Architected Tool''s developer surface includes authentication, developer portal, documentation, developer console, support, signup flow, and 32 more developer resources.'
plans:
- name: Amazon Well Architected Tool Plans Pricing
  plan_count: 3
  slug: amazon-well-architected-tool-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 5
  name: Amazon Well Architected Tool Rate Limits
  slug: amazon-well-architected-tool-rate-limits
rules:
- name: Amazon Well-Architected Tool API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-well-architected-tool-jsonschema-spectral-rules
- name: Amazon Well-Architected Tool API Rules
  rule_count: 29
  severity_counts:
    error: 9
    hint: 0
    info: 5
    warn: 15
  slug: amazon-well-architected-tool-spectral-rules
score:
  band: strong
  composite: 59.8
  delta: 0.0
  facets:
    commercial_clarity: 65.8
    contract_quality: 73.9
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-well-architected-tool/refs/heads/main/screenshots/amazon-well-architected-tool-2026-07-25T200017.png
security:
- kind: authentication
  name: Amazon Well Architected Tool Authentication
  slug: amazon-well-architected-tool-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Well Architected Tool Domain Security
  slug: amazon-well-architected-tool-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Well Architected Tool Vulnerability Disclosure
  slug: amazon-well-architected-tool-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Well Architected Tool Trust Center
  slug: amazon-well-architected-tool-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-well-architected-tool
tags:
- Architecture
- Best Practices
- Cloud Governance
- Well-Architected
- Workloads
use_cases:
- description: Evaluate cloud workload architecture quality against AWS best practices across the five Well-Architected pillars.
  name: Architecture Reviews and Governance
- description: Use review templates to standardize architectural answers and enforce consistent governance across multiple workloads and teams.
  name: Multi-Workload Standardization
- description: Apply industry-specific and technology-specific lenses from the lens catalog to assess specialized workloads.
  name: Industry-Specific Best Practice Implementation
- description: Evaluate workloads for FedRAMP, GovCloud, and other regulatory compliance requirements through targeted lenses.
  name: Regulatory Compliance Assessment
- description: Integrate Well-Architected reviews into CI/CD workflows and automation pipelines for continuous architecture assessment.
  name: DevOps Pipeline Integration
- description: Share workloads with reviewers and stakeholders to facilitate collaborative architectural decision-making across teams.
  name: Cross-Team Architectural Alignment
- description: Use the sustainability pillar to minimize environmental impact and meet organizational sustainability commitments.
  name: Sustainability Goal Realization
website: https://aws.amazon.com/well-architected-tool/
---
