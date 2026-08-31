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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Adobe Captivate Agentic Access
  operation_count: 28
  slug: adobe-captivate-agentic-access
  summary_line: 28 operations · 4 acting
api_count: 1
apis:
- description: API for SCORM-compliant content delivery and tracking.
  name: Adobe Captivate SCORM API
  slug: adobe-captivate-scorm-api
- description: Experience API for tracking learning experiences.
  name: Adobe Captivate xAPI (Tin Can API)
  slug: adobe-captivate-xapi-tin-can-api
- description: API for collaborative review and commenting on eLearning projects.
  name: Adobe Captivate Review API
  slug: adobe-captivate-review-api
- description: Webhooks API for Adobe Learning Manager that enables real-time event notifications for learner activities, course completions, enrollments, and other learning management events.
  name: Adobe Learning Manager Webhooks API
  slug: adobe-learning-manager-webhooks-api
- description: Retrieve and manage account-level settings
  name: Adobe Captivate Account API
  slug: adobe-captivate-account-api
- description: Manage badges awarded to learners for achievements
  name: Adobe Captivate Badges API
  slug: adobe-captivate-badges-api
- description: Manage content catalogs that organize learning objects
  name: Adobe Captivate Catalogs API
  slug: adobe-captivate-catalogs-api
- description: Manage certification programs and compliance tracking
  name: Adobe Captivate Certifications API
  slug: adobe-captivate-certifications-api
- description: Manage learner enrollments in courses and learning programs
  name: Adobe Captivate Enrollments API
  slug: adobe-captivate-enrollments-api
- description: Manage gamification points and leaderboard features
  name: Adobe Captivate Gamification API
  slug: adobe-captivate-gamification-api
- description: Manage bulk import/export jobs for data operations
  name: Adobe Captivate Jobs API
  slug: adobe-captivate-jobs-api
- description: Manage learning objects including courses, learning programs, certifications, and job aids
  name: Adobe Captivate Learning Objects API
  slug: adobe-captivate-learning-objects-api
- description: Manage user notifications and announcements
  name: Adobe Captivate Notifications API
  slug: adobe-captivate-notifications-api
- description: Manage skills and skill levels associated with learning content
  name: Adobe Captivate Skills API
  slug: adobe-captivate-skills-api
- description: Manage groups of users for targeted content delivery
  name: Adobe Captivate User Groups API
  slug: adobe-captivate-user-groups-api
- description: Manage learner, manager, author, and admin user accounts
  name: Adobe Captivate Users API
  slug: adobe-captivate-users-api
arazzos:
- description: Read a user, activate them if not already ACTIVE, then enroll them into a course instance.
  name: Adobe Learning Manager Activate and Enroll a User
  slug: adobe-captivate-activate-and-enroll-user-workflow
- description: Resolve a course, pick an available instance, enroll a learner, and confirm the enrollment.
  name: Adobe Learning Manager Enroll a Learner in a Course
  slug: adobe-captivate-enroll-learner-in-course-workflow
- description: Assemble a learner profile from their account, enrollments, skills, and gamification points.
  name: Adobe Learning Manager Learner Progress Report
  slug: adobe-captivate-learner-progress-report-workflow
- description: Submit a bulk import/export job, poll until it finishes, and branch on success or failure.
  name: Adobe Learning Manager Run and Poll a Bulk Job
  slug: adobe-captivate-run-bulk-job-workflow
- description: Search the catalog by text, pick the top course, choose an instance, and enroll a learner.
  name: Adobe Learning Manager Search and Enroll
  slug: adobe-captivate-search-and-enroll-workflow
- description: Find a learner's enrollment in a course, confirm it, and remove it if present.
  name: Adobe Learning Manager Unenroll a Learner from a Course
  slug: adobe-captivate-unenroll-learner-workflow
artifact_total: 241
asyncapis:
- description: The Adobe Learning Manager Webhooks API enables real-time event notifications for learning management activities. When configured, Adobe Learning Manager sends HTTP POST requests to registered webhook
  name: Adobe Learning Manager Webhooks API
  slug: adobe-captivate-learning-manager-webhooks-asyncapi
collections:
- collection_type: postman
  name: Adobe Captivate Prime API (Learning Manager)
  slug: postman-adobe-captivate-prime-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager) Account API
  slug: open-adobe-captivate-account-api
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager) Account Badges API
  slug: open-adobe-captivate-badges-api
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager) Account Catalogs API
  slug: open-adobe-captivate-catalogs-api
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager) Account Certifications API
  slug: open-adobe-captivate-certifications-api
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager) Account Enrollments API
  slug: open-adobe-captivate-enrollments-api
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager) Account Gamification API
  slug: open-adobe-captivate-gamification-api
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager) Account Jobs API
  slug: open-adobe-captivate-jobs-api
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager) Account Learning Objects API
  slug: open-adobe-captivate-learning-objects-api
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager) Account Notifications API
  slug: open-adobe-captivate-notifications-api
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager)
  slug: open-adobe-captivate-prime-api
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager) Account Skills API
  slug: open-adobe-captivate-skills-api
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager) Account User Groups API
  slug: open-adobe-captivate-user-groups-api
- collection_type: open
  name: Adobe Captivate Prime API (Learning Manager) Account Users API
  slug: open-adobe-captivate-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/adobe-captivate-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-captivate-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-captivate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adobe-captivate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adobe-captivate-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adobe-captivate-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adobe-captivate/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-captivate-activate-and-enroll-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-captivate-enroll-learner-in-course-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-captivate-learner-progress-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-captivate-run-bulk-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-captivate-search-and-enroll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-captivate-unenroll-learner-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adobe-captivate
- group: operate
  title: ''
  type: Support
  url: https://helpx.adobe.com/support/captivate.html
- group: operate
  title: ''
  type: Community
  url: https://community.adobe.com/t5/adobe-captivate/ct-p/ct-captivate
- group: company
  title: ''
  type: Blog
  url: https://elearning.adobe.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy.html
- group: operate
  title: ''
  type: Contact
  url: https://www.adobe.com/products/captivate/contact.html
- group: start
  title: ''
  type: Portal
  url: https://experienceleague.adobe.com/docs/learning-manager/using/introduction.html
- group: start
  title: ''
  type: GettingStarted
  url: https://experienceleague.adobe.com/docs/learning-manager/using/getting-started/getting-started.html
- group: docs
  title: ''
  type: Documentation
  url: https://experienceleague.adobe.com/docs/learning-manager/using/home.html
- group: start
  title: ''
  type: Console
  url: https://developer.adobe.com/console/
- group: operate
  title: ''
  type: ChangeLog
  url: https://experienceleague.adobe.com/docs/learning-manager/using/whats-new.html
- group: company
  title: ''
  type: Website
  url: https://business.adobe.com/products/learning-manager/adobe-learning-manager.html
- group: start
  title: ''
  type: Login
  url: https://learningmanager.adobe.com/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AdobeELearning
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adobe
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/adobe-captivate-learning-object-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-captivate-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/adobe-captivate-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/adobe-captivate-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-captivate-learning-manager-webhooks-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-captivate-prime-api-context.jsonld
created: '2024-01-20'
description: Adobe Captivate is an eLearning authoring tool used to create responsive eLearning content, software demonstrations, and interactive training modules.
examples:
- key_count: 2
  name: Adobe Captivate Learning Object Example
  slug: adobe-captivate-learning-object-example
- key_count: 3
  name: Learning Manager Webhooks Learner Reference Example
  slug: learning-manager-webhooks-learner-reference-example
- key_count: 4
  name: Learning Manager Webhooks Learning Object Reference Example
  slug: learning-manager-webhooks-learning-object-reference-example
- key_count: 5
  name: Learning Manager Webhooks Webhook Event Base Example
  slug: learning-manager-webhooks-webhook-event-base-example
- key_count: 3
  name: Prime Api Account Example
  slug: prime-api-account-example
- key_count: 1
  name: Prime Api Account Response Example
  slug: prime-api-account-response-example
- key_count: 3
  name: Prime Api Badge Example
  slug: prime-api-badge-example
- key_count: 2
  name: Prime Api Badge List Response Example
  slug: prime-api-badge-list-response-example
- key_count: 1
  name: Prime Api Badge Response Example
  slug: prime-api-badge-response-example
- key_count: 4
  name: Prime Api Catalog Example
  slug: prime-api-catalog-example
- key_count: 2
  name: Prime Api Catalog List Response Example
  slug: prime-api-catalog-list-response-example
- key_count: 1
  name: Prime Api Catalog Response Example
  slug: prime-api-catalog-response-example
- key_count: 2
  name: Prime Api Certification List Response Example
  slug: prime-api-certification-list-response-example
- key_count: 1
  name: Prime Api Enrollment Create Request Example
  slug: prime-api-enrollment-create-request-example
- key_count: 4
  name: Prime Api Enrollment Example
  slug: prime-api-enrollment-example
- key_count: 2
  name: Prime Api Enrollment List Response Example
  slug: prime-api-enrollment-list-response-example
- key_count: 1
  name: Prime Api Enrollment Response Example
  slug: prime-api-enrollment-response-example
- key_count: 3
  name: Prime Api Gamification Points Example
  slug: prime-api-gamification-points-example
- key_count: 1
  name: Prime Api Gamification Points Response Example
  slug: prime-api-gamification-points-response-example
- key_count: 1
  name: Prime Api Job Create Request Example
  slug: prime-api-job-create-request-example
- key_count: 3
  name: Prime Api Job Example
  slug: prime-api-job-example
- key_count: 2
  name: Prime Api Job List Response Example
  slug: prime-api-job-list-response-example
- key_count: 1
  name: Prime Api Job Response Example
  slug: prime-api-job-response-example
- key_count: 4
  name: Prime Api Learning Object Example
  slug: prime-api-learning-object-example
- key_count: 3
  name: Prime Api Learning Object Instance Example
  slug: prime-api-learning-object-instance-example
- key_count: 2
  name: Prime Api Learning Object Instance List Response Example
  slug: prime-api-learning-object-instance-list-response-example
- key_count: 3
  name: Prime Api Learning Object List Response Example
  slug: prime-api-learning-object-list-response-example
- key_count: 2
  name: Prime Api Learning Object Response Example
  slug: prime-api-learning-object-response-example
- key_count: 5
  name: Prime Api Localized Metadata Example
  slug: prime-api-localized-metadata-example
- key_count: 3
  name: Prime Api Notification Example
  slug: prime-api-notification-example
- key_count: 2
  name: Prime Api Notification List Response Example
  slug: prime-api-notification-list-response-example
- key_count: 3
  name: Prime Api Pagination Links Example
  slug: prime-api-pagination-links-example
- key_count: 2
  name: Prime Api Relationship Example
  slug: prime-api-relationship-example
- key_count: 2
  name: Prime Api Resource Identifier Example
  slug: prime-api-resource-identifier-example
- key_count: 4
  name: Prime Api Skill Example
  slug: prime-api-skill-example
- key_count: 2
  name: Prime Api Skill List Response Example
  slug: prime-api-skill-list-response-example
- key_count: 1
  name: Prime Api Skill Response Example
  slug: prime-api-skill-response-example
- key_count: 2
  name: Prime Api User Badge List Response Example
  slug: prime-api-user-badge-list-response-example
- key_count: 4
  name: Prime Api User Example
  slug: prime-api-user-example
- key_count: 3
  name: Prime Api User Group Example
  slug: prime-api-user-group-example
- key_count: 2
  name: Prime Api User Group List Response Example
  slug: prime-api-user-group-list-response-example
- key_count: 1
  name: Prime Api User Group Response Example
  slug: prime-api-user-group-response-example
- key_count: 2
  name: Prime Api User List Response Example
  slug: prime-api-user-list-response-example
- key_count: 1
  name: Prime Api User Response Example
  slug: prime-api-user-response-example
- key_count: 2
  name: Prime Api User Skill List Response Example
  slug: prime-api-user-skill-list-response-example
- key_count: 1
  name: Prime Api User Update Request Example
  slug: prime-api-user-update-request-example
features:
- description: Create and manage courses, learning programs, certifications, and job aids with full CRUD operations via REST API.
  name: Learning Object Management
- description: Programmatically enroll learners, track progress, and retrieve completion status across all learning objects.
  name: Learner Enrollment and Tracking
- description: Receive real-time HTTP POST notifications for enrollment, completion, badge, and certification events.
  name: Webhook Event Notifications
- description: Manage gamification points, leaderboards, and badge awards to motivate learners.
  name: Gamification and Badges
- description: Organize and expose learning content through catalogs with filtering and tagging capabilities.
  name: Catalog Management
- description: Associate skills with learning content and track learner skill attainment through the API.
  name: Skill Tracking
- description: Secure API access using OAuth 2.0 with role-based scopes for admin, learner, manager, and author roles.
  name: OAuth 2.0 Authentication
- description: Deliver and track SCORM-compliant and xAPI (Tin Can) learning content for LMS interoperability.
  name: SCORM and xAPI Support
- description: Use the Jobs API to import and export users, enrollments, and completion data in bulk.
  name: Bulk Data Import/Export
- description: Manage announcements and notifications sent to learners, managers, and administrators.
  name: Notification Management
finops:
- name: Adobe Captivate Finops
  service_category: eLearning Authoring
  slug: adobe-captivate-finops
image: /assets/icons/adobe-captivate.png
integrations:
- description: Sync learner data and completion status between Adobe Learning Manager and Salesforce CRM.
  name: Salesforce
- description: Surface learning content and notifications directly within Microsoft Teams via connector.
  name: Microsoft Teams
- description: Import organizational user data from Workday HCM to manage learner accounts automatically.
  name: Workday
- description: Bi-directional sync with SAP SuccessFactors for user provisioning and learning record exchange.
  name: SAP SuccessFactors
- description: Embed learning content and catalogs within Adobe Experience Manager sites.
  name: Adobe Experience Manager
- description: Schedule and launch virtual classroom sessions directly from Adobe Learning Manager.
  name: Zoom
- description: Import LinkedIn Learning content into Adobe Learning Manager catalogs for blended learning.
  name: LinkedIn Learning
- description: Host and launch SCORM content packages through SCORM Cloud integration.
  name: SCORM Cloud
json_schemas:
- name: Adobe Learning Manager Learning Object
  property_count: 2
  slug: adobe-captivate-learning-object
- name: BadgeAwardedPayload
  property_count: 0
  slug: learning-manager-webhooks-badge-awarded-payload
- name: CertificationCompletedPayload
  property_count: 0
  slug: learning-manager-webhooks-certification-completed-payload
- name: CourseCreatedPayload
  property_count: 0
  slug: learning-manager-webhooks-course-created-payload
- name: CourseUpdatedPayload
  property_count: 0
  slug: learning-manager-webhooks-course-updated-payload
- name: JobCompletedPayload
  property_count: 0
  slug: learning-manager-webhooks-job-completed-payload
- name: LearnerCompletionPayload
  property_count: 0
  slug: learning-manager-webhooks-learner-completion-payload
- name: LearnerEnrollmentPayload
  property_count: 0
  slug: learning-manager-webhooks-learner-enrollment-payload
- name: LearnerProgressPayload
  property_count: 0
  slug: learning-manager-webhooks-learner-progress-payload
- name: LearnerReference
  property_count: 3
  slug: learning-manager-webhooks-learner-reference
- name: LearnerUnenrollmentPayload
  property_count: 0
  slug: learning-manager-webhooks-learner-unenrollment-payload
- name: LearningObjectReference
  property_count: 4
  slug: learning-manager-webhooks-learning-object-reference
- name: SkillAchievedPayload
  property_count: 0
  slug: learning-manager-webhooks-skill-achieved-payload
- name: UserCreatedPayload
  property_count: 0
  slug: learning-manager-webhooks-user-created-payload
- name: UserDeletedPayload
  property_count: 0
  slug: learning-manager-webhooks-user-deleted-payload
- name: UserUpdatedPayload
  property_count: 0
  slug: learning-manager-webhooks-user-updated-payload
- name: WebhookEventBase
  property_count: 5
  slug: learning-manager-webhooks-webhook-event-base
- name: AccountResponse
  property_count: 1
  slug: prime-api-account-response
- name: Account
  property_count: 3
  slug: prime-api-account
- name: BadgeListResponse
  property_count: 2
  slug: prime-api-badge-list-response
- name: BadgeResponse
  property_count: 1
  slug: prime-api-badge-response
- name: Badge
  property_count: 3
  slug: prime-api-badge
- name: CatalogListResponse
  property_count: 2
  slug: prime-api-catalog-list-response
- name: CatalogResponse
  property_count: 1
  slug: prime-api-catalog-response
- name: Catalog
  property_count: 4
  slug: prime-api-catalog
- name: CertificationListResponse
  property_count: 2
  slug: prime-api-certification-list-response
- name: EnrollmentCreateRequest
  property_count: 1
  slug: prime-api-enrollment-create-request
- name: EnrollmentListResponse
  property_count: 2
  slug: prime-api-enrollment-list-response
- name: EnrollmentResponse
  property_count: 1
  slug: prime-api-enrollment-response
- name: Enrollment
  property_count: 4
  slug: prime-api-enrollment
- name: GamificationPointsResponse
  property_count: 1
  slug: prime-api-gamification-points-response
- name: GamificationPoints
  property_count: 3
  slug: prime-api-gamification-points
- name: JobCreateRequest
  property_count: 1
  slug: prime-api-job-create-request
- name: JobListResponse
  property_count: 2
  slug: prime-api-job-list-response
- name: JobResponse
  property_count: 1
  slug: prime-api-job-response
- name: Job
  property_count: 3
  slug: prime-api-job
- name: LearningObjectInstanceListResponse
  property_count: 2
  slug: prime-api-learning-object-instance-list-response
- name: LearningObjectInstance
  property_count: 3
  slug: prime-api-learning-object-instance
- name: LearningObjectListResponse
  property_count: 3
  slug: prime-api-learning-object-list-response
- name: LearningObjectResponse
  property_count: 2
  slug: prime-api-learning-object-response
- name: LearningObject
  property_count: 4
  slug: prime-api-learning-object
- name: LocalizedMetadata
  property_count: 5
  slug: prime-api-localized-metadata
- name: NotificationListResponse
  property_count: 2
  slug: prime-api-notification-list-response
- name: Notification
  property_count: 3
  slug: prime-api-notification
- name: PaginationLinks
  property_count: 3
  slug: prime-api-pagination-links
- name: Relationship
  property_count: 2
  slug: prime-api-relationship
- name: ResourceIdentifier
  property_count: 2
  slug: prime-api-resource-identifier
- name: SkillListResponse
  property_count: 2
  slug: prime-api-skill-list-response
- name: SkillResponse
  property_count: 1
  slug: prime-api-skill-response
- name: Skill
  property_count: 4
  slug: prime-api-skill
- name: UserBadgeListResponse
  property_count: 2
  slug: prime-api-user-badge-list-response
- name: UserGroupListResponse
  property_count: 2
  slug: prime-api-user-group-list-response
- name: UserGroupResponse
  property_count: 1
  slug: prime-api-user-group-response
- name: UserGroup
  property_count: 3
  slug: prime-api-user-group
- name: UserListResponse
  property_count: 2
  slug: prime-api-user-list-response
- name: UserResponse
  property_count: 1
  slug: prime-api-user-response
- name: User
  property_count: 4
  slug: prime-api-user
- name: UserSkillListResponse
  property_count: 2
  slug: prime-api-user-skill-list-response
- name: UserUpdateRequest
  property_count: 1
  slug: prime-api-user-update-request
json_structures:
- name: Adobe Captivate Learning Object Structure
  property_count: 2
  slug: adobe-captivate-learning-object-structure
- name: Learning Manager Webhooks Badge Awarded Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-badge-awarded-payload-structure
- name: Learning Manager Webhooks Certification Completed Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-certification-completed-payload-structure
- name: Learning Manager Webhooks Course Created Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-course-created-payload-structure
- name: Learning Manager Webhooks Course Updated Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-course-updated-payload-structure
- name: Learning Manager Webhooks Job Completed Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-job-completed-payload-structure
- name: Learning Manager Webhooks Learner Completion Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-learner-completion-payload-structure
- name: Learning Manager Webhooks Learner Enrollment Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-learner-enrollment-payload-structure
- name: Learning Manager Webhooks Learner Progress Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-learner-progress-payload-structure
- name: Learning Manager Webhooks Learner Reference Structure
  property_count: 3
  slug: learning-manager-webhooks-learner-reference-structure
- name: Learning Manager Webhooks Learner Unenrollment Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-learner-unenrollment-payload-structure
- name: Learning Manager Webhooks Learning Object Reference Structure
  property_count: 4
  slug: learning-manager-webhooks-learning-object-reference-structure
- name: Learning Manager Webhooks Skill Achieved Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-skill-achieved-payload-structure
- name: Learning Manager Webhooks User Created Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-user-created-payload-structure
- name: Learning Manager Webhooks User Deleted Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-user-deleted-payload-structure
- name: Learning Manager Webhooks User Updated Payload Structure
  property_count: 0
  slug: learning-manager-webhooks-user-updated-payload-structure
- name: Learning Manager Webhooks Webhook Event Base Structure
  property_count: 5
  slug: learning-manager-webhooks-webhook-event-base-structure
- name: Prime Api Account Response Structure
  property_count: 1
  slug: prime-api-account-response-structure
- name: Prime Api Account Structure
  property_count: 3
  slug: prime-api-account-structure
- name: Prime Api Badge List Response Structure
  property_count: 2
  slug: prime-api-badge-list-response-structure
- name: Prime Api Badge Response Structure
  property_count: 1
  slug: prime-api-badge-response-structure
- name: Prime Api Badge Structure
  property_count: 3
  slug: prime-api-badge-structure
- name: Prime Api Catalog List Response Structure
  property_count: 2
  slug: prime-api-catalog-list-response-structure
- name: Prime Api Catalog Response Structure
  property_count: 1
  slug: prime-api-catalog-response-structure
- name: Prime Api Catalog Structure
  property_count: 4
  slug: prime-api-catalog-structure
- name: Prime Api Certification List Response Structure
  property_count: 2
  slug: prime-api-certification-list-response-structure
- name: Prime Api Enrollment Create Request Structure
  property_count: 1
  slug: prime-api-enrollment-create-request-structure
- name: Prime Api Enrollment List Response Structure
  property_count: 2
  slug: prime-api-enrollment-list-response-structure
- name: Prime Api Enrollment Response Structure
  property_count: 1
  slug: prime-api-enrollment-response-structure
- name: Prime Api Enrollment Structure
  property_count: 4
  slug: prime-api-enrollment-structure
- name: Prime Api Gamification Points Response Structure
  property_count: 1
  slug: prime-api-gamification-points-response-structure
- name: Prime Api Gamification Points Structure
  property_count: 3
  slug: prime-api-gamification-points-structure
- name: Prime Api Job Create Request Structure
  property_count: 1
  slug: prime-api-job-create-request-structure
- name: Prime Api Job List Response Structure
  property_count: 2
  slug: prime-api-job-list-response-structure
- name: Prime Api Job Response Structure
  property_count: 1
  slug: prime-api-job-response-structure
- name: Prime Api Job Structure
  property_count: 3
  slug: prime-api-job-structure
- name: Prime Api Learning Object Instance List Response Structure
  property_count: 2
  slug: prime-api-learning-object-instance-list-response-structure
- name: Prime Api Learning Object Instance Structure
  property_count: 3
  slug: prime-api-learning-object-instance-structure
- name: Prime Api Learning Object List Response Structure
  property_count: 3
  slug: prime-api-learning-object-list-response-structure
- name: Prime Api Learning Object Response Structure
  property_count: 2
  slug: prime-api-learning-object-response-structure
- name: Prime Api Learning Object Structure
  property_count: 4
  slug: prime-api-learning-object-structure
- name: Prime Api Localized Metadata Structure
  property_count: 5
  slug: prime-api-localized-metadata-structure
- name: Prime Api Notification List Response Structure
  property_count: 2
  slug: prime-api-notification-list-response-structure
- name: Prime Api Notification Structure
  property_count: 3
  slug: prime-api-notification-structure
- name: Prime Api Pagination Links Structure
  property_count: 3
  slug: prime-api-pagination-links-structure
- name: Prime Api Relationship Structure
  property_count: 2
  slug: prime-api-relationship-structure
- name: Prime Api Resource Identifier Structure
  property_count: 2
  slug: prime-api-resource-identifier-structure
- name: Prime Api Skill List Response Structure
  property_count: 2
  slug: prime-api-skill-list-response-structure
- name: Prime Api Skill Response Structure
  property_count: 1
  slug: prime-api-skill-response-structure
- name: Prime Api Skill Structure
  property_count: 4
  slug: prime-api-skill-structure
- name: Prime Api User Badge List Response Structure
  property_count: 2
  slug: prime-api-user-badge-list-response-structure
- name: Prime Api User Group List Response Structure
  property_count: 2
  slug: prime-api-user-group-list-response-structure
- name: Prime Api User Group Response Structure
  property_count: 1
  slug: prime-api-user-group-response-structure
- name: Prime Api User Group Structure
  property_count: 3
  slug: prime-api-user-group-structure
- name: Prime Api User List Response Structure
  property_count: 2
  slug: prime-api-user-list-response-structure
- name: Prime Api User Response Structure
  property_count: 1
  slug: prime-api-user-response-structure
- name: Prime Api User Skill List Response Structure
  property_count: 2
  slug: prime-api-user-skill-list-response-structure
- name: Prime Api User Structure
  property_count: 4
  slug: prime-api-user-structure
- name: Prime Api User Update Request Structure
  property_count: 1
  slug: prime-api-user-update-request-structure
jsonld:
- class_count: 0
  name: Adobe Captivate Context
  property_count: 16
  slug: adobe-captivate-context
- class_count: 5
  name: Adobe Captivate Learning Manager Webhooks Context
  property_count: 9
  slug: adobe-captivate-learning-manager-webhooks-context
- class_count: 45
  name: Adobe Captivate Prime Api Context
  property_count: 80
  slug: adobe-captivate-prime-api-context
layout: provider
modified: '2026-04-19'
name: Adobe Captivate
nav: Providers
network: true
overview: 'Adobe Captivate publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Adobe Learning Manager Webhooks API, Account API, Badges API, and 10 more. Tagged areas include Authoring, Education, eLearning, LMS, and SCORM.


  The Adobe Captivate catalog on APIs.io includes 1 event-driven AsyncAPI specification, 3 JSON-LD contexts, and 3 Spectral governance rulesets.


  Adobe Captivate''s developer surface includes authentication, support, engineering blog, developer portal, getting-started guide, documentation, developer console, and 29 more developer resources.'
plans:
- name: Adobe Captivate Plans Pricing
  plan_count: 2
  slug: adobe-captivate-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Adobe Captivate Rate Limits
  slug: adobe-captivate-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Adobe Captivate API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: adobe-captivate-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Adobe Captivate API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: adobe-captivate-jsonschema-spectral-rules
- effective_rule_count: 34
  extends: []
  name: Adobe Captivate API Rules
  rule_count: 34
  severity_counts:
    error: 16
    hint: 0
    info: 4
    warn: 14
  slug: adobe-captivate-spectral-rules
scopes:
- name: Adobe Captivate Scopes
  scope_count: 4
  slug: adobe-captivate-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 21
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 28.8
    contract_quality: 81.5
    developer_ergonomics: 45.2
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 75.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-captivate/refs/heads/main/screenshots/adobe-captivate-2026-06-20T164834.png
security:
- kind: authentication
  name: Adobe Captivate Authentication
  slug: adobe-captivate-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Adobe Captivate Domain Security
  slug: adobe-captivate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Captivate Vulnerability Disclosure
  slug: adobe-captivate-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: adobe-captivate
tags:
- Authoring
- Education
- eLearning
- LMS
- SCORM
- Training
- xAPI
use_cases:
- description: Automatically provision users from HRIS systems like Workday or SAP SuccessFactors into Adobe Learning Manager.
  name: HR System Integration
- description: Build branded training portals that surface Adobe Learning Manager content through the REST API.
  name: Custom Learning Portal
- description: Auto-enroll new hires in mandatory compliance courses and track completion for regulatory reporting.
  name: Compliance Training Automation
- description: Extract learner progress and completion data to build custom analytics and reporting dashboards.
  name: Learning Analytics Dashboard
- description: Integrate course purchases with e-commerce platforms and auto-enroll paying customers.
  name: E-Commerce Integration
- description: Use webhooks to monitor learner activity in real time and trigger downstream workflows on completion.
  name: Real-Time Progress Monitoring
- description: Automate certification enrollment, renewal reminders, and expiry tracking using the REST API.
  name: Certification Management
website: https://business.adobe.com/products/learning-manager/adobe-learning-manager.html
---
