---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 90
  human_in_the_loop: 3
  name: Ispring Agentic Access
  operation_count: 141
  slug: ispring-agentic-access
  summary_line: 141 operations · 90 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: Assignment operations
  name: iSpring Learn assignments API
  slug: ispring-assignments-api
- description: Certificate operations
  name: iSpring Learn certificate API
  slug: ispring-certificate-api
- description: Content operations
  name: iSpring Learn content API
  slug: ispring-content-api
- description: Department operations
  name: iSpring Learn department API
  slug: ispring-department-api
- description: The departments API from iSpring Learn — 1 operation(s) for departments.
  name: iSpring Learn departments API
  slug: ispring-departments-api
- description: Enrollment operations
  name: iSpring Learn enrollment API
  slug: ispring-enrollment-api
- description: Gamification operations
  name: iSpring Learn gamification API
  slug: ispring-gamification-api
- description: Group operations
  name: iSpring Learn group API
  slug: ispring-group-api
- description: The jobtraining API from iSpring Learn — 4 operation(s) for jobtraining.
  name: iSpring Learn jobtraining API
  slug: ispring-jobtraining-api
- description: Learning track operations
  name: iSpring Learn learning_track API
  slug: ispring-learning-track-api
- description: The performance-management API from iSpring Learn — 37 operation(s) for performance-management.
  name: iSpring Learn performance-management API
  slug: ispring-performance-management-api
- description: The quizzes API from iSpring Learn — 2 operation(s) for quizzes.
  name: iSpring Learn quizzes API
  slug: ispring-quizzes-api
- description: The report API from iSpring Learn — 2 operation(s) for report.
  name: iSpring Learn report API
  slug: ispring-report-api
- description: User result data operations
  name: iSpring Learn results API
  slug: ispring-results-api
- description: The statistics API from iSpring Learn — 2 operation(s) for statistics.
  name: iSpring Learn statistics API
  slug: ispring-statistics-api
- description: Async method operations
  name: iSpring Learn task API
  slug: ispring-task-api
- description: Retrieve access tokens
  name: iSpring Learn token API
  slug: ispring-token-api
- description: Training operations
  name: iSpring Learn training API
  slug: ispring-training-api
- description: User operations
  name: iSpring Learn user API
  slug: ispring-user-api
- description: The webhook API from iSpring Learn — 11 operation(s) for webhook.
  name: iSpring Learn webhook API
  slug: ispring-webhook-api
artifact_total: 242
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Learn Rest Api assignments API
  slug: open-ispring-assignments-api
- collection_type: open
  name: Learn Rest Api assignments certificate API
  slug: open-ispring-certificate-api
- collection_type: open
  name: Learn Rest Api assignments content API
  slug: open-ispring-content-api
- collection_type: open
  name: Learn Rest Api assignments department API
  slug: open-ispring-department-api
- collection_type: open
  name: Learn Rest Api assignments departments API
  slug: open-ispring-departments-api
- collection_type: open
  name: Learn Rest Api assignments enrollment API
  slug: open-ispring-enrollment-api
- collection_type: open
  name: Learn Rest Api assignments gamification API
  slug: open-ispring-gamification-api
- collection_type: open
  name: Learn Rest Api assignments group API
  slug: open-ispring-group-api
- collection_type: open
  name: Learn Rest Api assignments jobtraining API
  slug: open-ispring-jobtraining-api
- collection_type: open
  name: Learn Rest Api assignments learning_track API
  slug: open-ispring-learning-track-api
- collection_type: open
  name: Learn Rest Api assignments performance-management API
  slug: open-ispring-performance-management-api
- collection_type: open
  name: Learn Rest Api assignments quizzes API
  slug: open-ispring-quizzes-api
- collection_type: open
  name: Learn Rest Api assignments report API
  slug: open-ispring-report-api
- collection_type: open
  name: Learn Rest Api assignments results API
  slug: open-ispring-results-api
- collection_type: open
  name: Learn Rest Api assignments statistics API
  slug: open-ispring-statistics-api
- collection_type: open
  name: Learn Rest Api assignments task API
  slug: open-ispring-task-api
- collection_type: open
  name: Learn Rest Api assignments token API
  slug: open-ispring-token-api
- collection_type: open
  name: Learn Rest Api assignments training API
  slug: open-ispring-training-api
- collection_type: open
  name: Learn Rest Api assignments user API
  slug: open-ispring-user-api
- collection_type: open
  name: Learn Rest Api assignments webhook API
  slug: open-ispring-webhook-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ispring-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ispring-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ispring-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ispring-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://ispringhelpdocs.com/ispring-learn/api-documentation-10685383.html
- group: docs
  title: ''
  type: Reference
  url: https://ispringhelpdocs.com/ispring-learn/rest-api-10684924.html
- group: docs
  title: ''
  type: OpenAPI
  url: https://api-learn.ispringlearn.com/docs/rest-api
- group: design
  title: ''
  type: Webhooks
  url: https://ispringhelpdocs.com/ispring-learn/webhook-62863671.html
- group: auth
  title: ''
  type: Authentication
  url: https://ispringhelpdocs.com/ispring-learn/rest-api-10684924.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ispringsolutions.com/articles/integration-of-ispring-learn-with-your-system
- group: company
  title: ''
  type: Blog
  url: https://www.ispringsolutions.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.ispring.com/whats-new
- group: operate
  title: ''
  type: Support
  url: https://www.ispringsolutions.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ispringsolutions.com/company/policy/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ispringsolutions.com/services-subscription-agreement
- group: commercial
  title: ''
  type: Plans
  url: plans/ispring-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ispring-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ispring-finops.yml
created: '2026-06-13'
description: iSpring Learn is an eLearning platform and LMS that provides a REST API for managing courses, users, groups, departments, enrollments, learning paths, and accessing detailed learner progress reports. The API supports content management, assignment grading, 360-degree performance reviews, on-the-job training, and event-driven webhooks. API access requires a Business subscription.
finops:
- name: Ispring Finops
  service_category: ''
  slug: ispring-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ispring.png
json_schemas:
- name: ActiveUsersByPeriod
  property_count: 3
  slug: ActiveUsersByPeriod
- name: AddAppraisalQuestionRequest
  property_count: 3
  slug: AddAppraisalQuestionRequest
- name: AddAppraisalSessionEmployeeCardsRequest
  property_count: 1
  slug: AddAppraisalSessionEmployeeCardsRequest
- name: AddAppraisalSessionPermissionsRequest
  property_count: 1
  slug: AddAppraisalSessionPermissionsRequest
- name: AndSmartGroupRuleNode
  property_count: 1
  slug: AndSmartGroupRuleNode
- name: AnswerBreakdownResult
  property_count: 17
  slug: AnswerBreakdownResult
- name: AnswerBreakdownResultsPage
  property_count: 2
  slug: AnswerBreakdownResultsPage
- name: AppraisalQuestion
  property_count: 4
  slug: AppraisalQuestion
- name: AppraisalSession
  property_count: 8
  slug: AppraisalSession
- name: AppraisalSessionContentCommentsRequirementLevel
  property_count: 0
  slug: AppraisalSessionContentCommentsRequirementLevel
- name: AppraisalSessionContentCompetencies
  property_count: 2
  slug: AppraisalSessionContentCompetencies
- name: AppraisalSessionContentCompetency
  property_count: 8
  slug: AppraisalSessionContentCompetency
- name: AppraisalSessionContentCompetencyReviewMethod
  property_count: 0
  slug: AppraisalSessionContentCompetencyReviewMethod
- name: AppraisalSessionContentIndicatorData
  property_count: 3
  slug: AppraisalSessionContentIndicatorData
- name: AppraisalSessionContentRequiredLevelData
  property_count: 2
  slug: AppraisalSessionContentRequiredLevelData
- name: AppraisalSessionContentScale
  property_count: 2
  slug: AppraisalSessionContentScale
- name: AppraisalSessionContentScaleLevelData
  property_count: 2
  slug: AppraisalSessionContentScaleLevelData
- name: AppraisalSessionEmployeeCard
  property_count: 2
  slug: AppraisalSessionEmployeeCard
- name: AppraisalSessionEmployeeCompetencyResults
  property_count: 2
  slug: AppraisalSessionEmployeeCompetencyResults
- name: AppraisalSessionEmployeeDetailedCard
  property_count: 2
  slug: AppraisalSessionEmployeeDetailedCard
- name: AppraisalSessionEmployeeIndicatorResults
  property_count: 2
  slug: AppraisalSessionEmployeeIndicatorResults
- name: AppraisalSessionEmployeeResults
  property_count: 4
  slug: AppraisalSessionEmployeeResults
- name: AppraisalSessionInfo
  property_count: 14
  slug: AppraisalSessionInfo
- name: AppraisalSessionNotificationSettings
  property_count: 2
  slug: AppraisalSessionNotificationSettings
- name: AppraisalSessionReview
  property_count: 6
  slug: AppraisalSessionReview
- name: AppraisalSessionReviewStatus
  property_count: 0
  slug: AppraisalSessionReviewStatus
- name: AppraisalSessionReviewer
  property_count: 2
  slug: AppraisalSessionReviewer
- name: AppraisalSessionReviewerRole
  property_count: 0
  slug: AppraisalSessionReviewerRole
- name: AppraisalSessionStatus
  property_count: 0
  slug: AppraisalSessionStatus
- name: AppraisalSessionUserAttribute
  property_count: 3
  slug: AppraisalSessionUserAttribute
- name: AppraisalSessionUserAttributes
  property_count: 8
  slug: AppraisalSessionUserAttributes
- name: AppraisalSessionUserStatus
  property_count: 0
  slug: AppraisalSessionUserStatus
- name: ArrayOfIds
  property_count: 0
  slug: ArrayOfIds
- name: Assignment
  property_count: 4
  slug: Assignment
- name: AssignmentAttempt
  property_count: 5
  slug: AssignmentAttempt
- name: AssignmentAttemptAttachment
  property_count: 3
  slug: AssignmentAttemptAttachment
- name: AssignmentAttemptGrade
  property_count: 3
  slug: AssignmentAttemptGrade
- name: AssignmentAttemptGrades
  property_count: 1
  slug: AssignmentAttemptGrades
- name: AssignmentsPage
  property_count: 2
  slug: AssignmentsPage
- name: AwardGamificationPoints
  property_count: 3
  slug: AwardGamificationPoints
- name: ChangeAppraisalQuestionOrdersRequest
  property_count: 1
  slug: ChangeAppraisalQuestionOrdersRequest
- name: ChangeAppraisalSessionNotificationSettingsRequest
  property_count: 2
  slug: ChangeAppraisalSessionNotificationSettingsRequest
- name: ChangeCompetencyData
  property_count: 6
  slug: ChangeCompetencyData
- name: ChangeCompetencyScaleRequest
  property_count: 2
  slug: ChangeCompetencyScaleRequest
- name: ChangeDepartmentSubordination
  property_count: 2
  slug: ChangeDepartmentSubordination
- name: ChangeUserSubordination
  property_count: 2
  slug: ChangeUserSubordination
- name: ChecklistSessionsData
  property_count: 4
  slug: ChecklistSessionsData
- name: ChecklistStatus
  property_count: 0
  slug: ChecklistStatus
- name: ClientCredentialsGrantTypeRequest
  property_count: 3
  slug: ClientCredentialsGrantTypeRequest
- name: Competency
  property_count: 8
  slug: Competency
- name: CompetencyCommentsRequirementLevel
  property_count: 0
  slug: CompetencyCommentsRequirementLevel
- name: CompetencyGroup
  property_count: 4
  slug: CompetencyGroup
- name: CompetencyIndicator
  property_count: 3
  slug: CompetencyIndicator
- name: CompetencyIndicatorData
  property_count: 2
  slug: CompetencyIndicatorData
- name: CompetencyIndicatorLevel
  property_count: 2
  slug: CompetencyIndicatorLevel
- name: CompetencyProfile
  property_count: 5
  slug: CompetencyProfile
- name: CompetencyReviewMethod
  property_count: 0
  slug: CompetencyReviewMethod
- name: CompetencyScale
  property_count: 3
  slug: CompetencyScale
- name: CompetencyScaleLevel
  property_count: 3
  slug: CompetencyScaleLevel
- name: CompletionStatus
  property_count: 0
  slug: CompletionStatus
- name: ConfirmRequest
  property_count: 2
  slug: ConfirmRequest
- name: ContentItemFinalStatus
  property_count: 5
  slug: ContentItemFinalStatus
- name: ContentItemInformation
  property_count: 10
  slug: ContentItemInformation
- name: ContentItemsInformationPage
  property_count: 2
  slug: ContentItemsInformationPage
- name: ContentType
  property_count: 0
  slug: ContentType
- name: CourseCompletionStatus
  property_count: 0
  slug: CourseCompletionStatus
- name: CourseField
  property_count: 4
  slug: CourseField
- name: CourseFieldType
  property_count: 0
  slug: CourseFieldType
- name: CourseFieldValue
  property_count: 2
  slug: CourseFieldValue
- name: CourseFields
  property_count: 1
  slug: CourseFields
- name: CourseModule
  property_count: 11
  slug: CourseModule
- name: CourseModulesPage
  property_count: 2
  slug: CourseModulesPage
- name: CourseTreeItem
  property_count: 8
  slug: CourseTreeItem
- name: CoursesModule
  property_count: 8
  slug: CoursesModule
- name: CoursesModulesPage
  property_count: 2
  slug: CoursesModulesPage
- name: CreateAppraisalSessionRequest
  property_count: 3
  slug: CreateAppraisalSessionRequest
- name: CreateCompetencyData
  property_count: 7
  slug: CreateCompetencyData
- name: CreateCompetencyGroupData
  property_count: 2
  slug: CreateCompetencyGroupData
- name: CreateCompetencyScaleData
  property_count: 2
  slug: CreateCompetencyScaleData
- name: CreateCompetencyScaleLevelData
  property_count: 2
  slug: CreateCompetencyScaleLevelData
- name: CreateCourseRequest
  property_count: 2
  slug: CreateCourseRequest
- name: CriterionGroupResultData
  property_count: 9
  slug: CriterionGroupResultData
- name: CriterionResultData
  property_count: 10
  slug: CriterionResultData
- name: DateRange
  property_count: 2
  slug: DateRange
- name: Day
  property_count: 7
  slug: Day
- name: DeleteEnrollments
  property_count: 1
  slug: DeleteEnrollments
- name: Department
  property_count: 6
  slug: Department
- name: DepartmentsPage
  property_count: 2
  slug: DepartmentsPage
- name: DetailedGroup
  property_count: 5
  slug: DetailedGroup
- name: DueDateType
  property_count: 0
  slug: DueDateType
- name: Enrollment
  property_count: 9
  slug: Enrollment
- name: EnrollmentTypeGroup
  property_count: 0
  slug: EnrollmentTypeGroup
- name: EnrollmentsPage
  property_count: 2
  slug: EnrollmentsPage
- name: ErrorResponse
  property_count: 2
  slug: ErrorResponse
- name: GetPagedUsersListRequest
  property_count: 6
  slug: GetPagedUsersListRequest
- name: GetPagedUsersListResponse
  property_count: 3
  slug: GetPagedUsersListResponse
- name: GetSubscriberInfoResponse
  property_count: 3
  slug: GetSubscriberInfoResponse
- name: Group
  property_count: 3
  slug: Group
- name: GroupsPage
  property_count: 2
  slug: GroupsPage
- name: IssuedCertificate
  property_count: 1
  slug: IssuedCertificate
- name: IssuedCertificateInformation
  property_count: 3
  slug: IssuedCertificateInformation
- name: JobTrainingSessionResultData
  property_count: 12
  slug: JobTrainingSessionResultData
- name: LearnerModuleResult
  property_count: 17
  slug: LearnerModuleResult
- name: LearnerResult
  property_count: 16
  slug: LearnerResult
- name: LearnersModulesResultsResponse
  property_count: 2
  slug: LearnersModulesResultsResponse
- name: LearnersResultsResponse
  property_count: 2
  slug: LearnersResultsResponse
- name: LearningTrackCourse
  property_count: 2
  slug: LearningTrackCourse
- name: ListAppraisalSessionUserAttributesRequest
  property_count: 1
  slug: ListAppraisalSessionUserAttributesRequest
- name: ListAppraisalSessionsRequest
  property_count: 1
  slug: ListAppraisalSessionsRequest
- name: ListChecklistsSessionsRequest
  property_count: 2
  slug: ListChecklistsSessionsRequest
- name: ListCompetenciesRequest
  property_count: 1
  slug: ListCompetenciesRequest
- name: ListCompetencyProfilesRequest
  property_count: 1
  slug: ListCompetencyProfilesRequest
- name: ListCriterionGroupsResultRequest
  property_count: 3
  slug: ListCriterionGroupsResultRequest
- name: ListCriterionResultRequest
  property_count: 4
  slug: ListCriterionResultRequest
- name: ListEnrollmentsRequest
  property_count: 5
  slug: ListEnrollmentsRequest
- name: ListSessionsResultRequest
  property_count: 3
  slug: ListSessionsResultRequest
- name: ModuleItemType
  property_count: 0
  slug: ModuleItemType
- name: ModuleStatus
  property_count: 5
  slug: ModuleStatus
- name: MoveCompetenciesToGroup
  property_count: 2
  slug: MoveCompetenciesToGroup
- name: MoveCompetencyGroupsToParentGroup
  property_count: 2
  slug: MoveCompetencyGroupsToParentGroup
- name: MoveDepartments
  property_count: 1
  slug: MoveDepartments
- name: MoveUsersToDepartment
  property_count: 1
  slug: MoveUsersToDepartment
- name: NewDepartment
  property_count: 3
  slug: NewDepartment
- name: NewEnrollment
  property_count: 7
  slug: NewEnrollment
- name: NewGroup
  property_count: 2
  slug: NewGroup
- name: NewSmartGroup
  property_count: 2
  slug: NewSmartGroup
- name: NewUser
  property_count: 12
  slug: NewUser
- name: OrSmartGroupRuleNode
  property_count: 1
  slug: OrSmartGroupRuleNode
- name: ParticipantsPage
  property_count: 2
  slug: ParticipantsPage
- name: ProfileCompetencyData
  property_count: 2
  slug: ProfileCompetencyData
- name: ProfileFieldsDateRangeItem
  property_count: 3
  slug: ProfileFieldsDateRangeItem
- name: ProfileFieldsFilterItem
  property_count: 2
  slug: ProfileFieldsFilterItem
- name: ProfileIndicatorData
  property_count: 2
  slug: ProfileIndicatorData
- name: Quiz
  property_count: 4
  slug: Quiz
- name: QuizzesPage
  property_count: 2
  slug: QuizzesPage
- name: Reenroll
  property_count: 5
  slug: Reenroll
- name: RemoveAppraisalSessionEmployeeCardsRequest
  property_count: 1
  slug: RemoveAppraisalSessionEmployeeCardsRequest
- name: RemoveAppraisalSessionPermissionsRequest
  property_count: 1
  slug: RemoveAppraisalSessionPermissionsRequest
- name: RemoveAppraisalSessionReviewersRequest
  property_count: 1
  slug: RemoveAppraisalSessionReviewersRequest
- name: RemoveUserGroups
  property_count: 1
  slug: RemoveUserGroups
- name: ReplaceAppraisalSessionEmployeeReviewersRequest
  property_count: 1
  slug: ReplaceAppraisalSessionEmployeeReviewersRequest
- name: RestartAppraisalSessionStatusCode
  property_count: 0
  slug: RestartAppraisalSessionStatusCode
- name: Role
  property_count: 4
  slug: Role
- name: ScheduledUserDeactivation
  property_count: 1
  slug: ScheduledUserDeactivation
- name: ScheduledUserTermination
  property_count: 1
  slug: ScheduledUserTermination
- name: SessionStatus
  property_count: 0
  slug: SessionStatus
- name: SmartGroupRule
  property_count: 4
  slug: SmartGroupRule
- name: SmartGroupRuleNodes
  property_count: 1
  slug: SmartGroupRuleNodes
- name: SmartGroupRules
  property_count: 2
  slug: SmartGroupRules
- name: StartAppraisalSessionStatusCode
  property_count: 0
  slug: StartAppraisalSessionStatusCode
- name: Subordination
  property_count: 2
  slug: Subordination
- name: SubscribeRequest
  property_count: 2
  slug: SubscribeRequest
- name: SubscriberNameRequest
  property_count: 1
  slug: SubscriberNameRequest
- name: SubscriberRequest
  property_count: 3
  slug: SubscriberRequest
- name: Subscription
  property_count: 2
  slug: Subscription
- name: SubscriptionParameter
  property_count: 2
  slug: SubscriptionParameter
- name: TaskStatus
  property_count: 1
  slug: TaskStatus
- name: TaskStatusEnum
  property_count: 0
  slug: TaskStatusEnum
- name: TokenResponse
  property_count: 3
  slug: TokenResponse
- name: Training
  property_count: 4
  slug: Training
- name: TrainingParticipantAttendance
  property_count: 3
  slug: TrainingParticipantAttendance
- name: TrainingSession
  property_count: 6
  slug: TrainingSession
- name: TrainingType
  property_count: 2
  slug: TrainingType
- name: UnsubscribeRequest
  property_count: 2
  slug: UnsubscribeRequest
- name: UpdateAppraisalQuestionRequest
  property_count: 3
  slug: UpdateAppraisalQuestionRequest
- name: UpdateAppraisalSessionRequest
  property_count: 6
  slug: UpdateAppraisalSessionRequest
- name: UpdateCourseStatus
  property_count: 6
  slug: UpdateCourseStatus
- name: UpdateDay
  property_count: 1
  slug: UpdateDay
- name: UpdateDayParticipantsAttendanceRequest
  property_count: 1
  slug: UpdateDayParticipantsAttendanceRequest
- name: UpdateDepartment
  property_count: 3
  slug: UpdateDepartment
- name: UpdateEnrollment
  property_count: 5
  slug: UpdateEnrollment
- name: UpdateGroup
  property_count: 1
  slug: UpdateGroup
- name: UpdateGroupMembers
  property_count: 1
  slug: UpdateGroupMembers
- name: UpdateModulesStatuses
  property_count: 3
  slug: UpdateModulesStatuses
- name: UpdateSmartGroup
  property_count: 2
  slug: UpdateSmartGroup
- name: UpdateUser
  property_count: 7
  slug: UpdateUser
- name: UpdateUserPassword
  property_count: 1
  slug: UpdateUserPassword
- name: UpdateUserStatus
  property_count: 1
  slug: UpdateUserStatus
- name: UpdateWorkLeaveStatusesRequest
  property_count: 1
  slug: UpdateWorkLeaveStatusesRequest
- name: User
  property_count: 16
  slug: User
- name: UserFieldInfo
  property_count: 8
  slug: UserFieldInfo
- name: UserPointsInfo
  property_count: 2
  slug: UserPointsInfo
- name: UserProfileField
  property_count: 2
  slug: UserProfileField
- name: UserProfileFields
  property_count: 3
  slug: UserProfileFields
- name: UserRole
  property_count: 3
  slug: UserRole
- name: UserRoleEnum
  property_count: 0
  slug: UserRoleEnum
- name: UserStatus
  property_count: 0
  slug: UserStatus
- name: UserV2
  property_count: 16
  slug: UserV2
- name: UsersPage
  property_count: 2
  slug: UsersPage
- name: UsersPageV2
  property_count: 2
  slug: UsersPageV2
- name: WithdrawGamificationPoints
  property_count: 3
  slug: WithdrawGamificationPoints
- name: WorkLeaveReason
  property_count: 0
  slug: WorkLeaveReason
- name: WorkLeaveStatus
  property_count: 3
  slug: WorkLeaveStatus
- name: WorkLeaveStatusData
  property_count: 4
  slug: WorkLeaveStatusData
layout: provider
modified: '2026-06-13'
name: iSpring Learn
nav: Providers
network: true
overview: 'iSpring Learn publishes 20 APIs on the [APIs.io](https://apis.io/) network, including assignments API, certificate API, content API, and 17 more. Tagged areas include eLearning, LMS, Learning Management System, Training, and Courses.


  The iSpring Learn catalog on APIs.io includes 1 Spectral governance ruleset.


  iSpring Learn''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, support, and 12 more developer resources.'
plans:
- name: Ispring Plans Pricing
  plan_count: 3
  slug: ispring-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Ispring Rate Limits
  slug: ispring-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: iSpring Learn API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ispring-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 9.8
    contract_quality: 51.3
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 55.3
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 37.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ispring/refs/heads/main/screenshots/ispring-2026-06-20T183622.png
security:
- kind: authentication
  name: Ispring Authentication
  slug: ispring-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ispring Domain Security
  slug: ispring-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ispring
tags:
- eLearning
- LMS
- Learning Management System
- Training
- Courses
- Enrollments
- User
- Group
- Reporting
- Webhook
- SCORM
- Corporate Training
---
