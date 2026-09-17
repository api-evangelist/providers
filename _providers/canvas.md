---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 566
  human_in_the_loop: 29
  name: Canvas Agentic Access
  operation_count: 1148
  slug: canvas-agentic-access
  summary_line: 1148 operations · 566 acting · 29 human-in-the-loop
api_count: 146
apis:
- description: The Canvas LMS GraphQL API is an alternative to the REST API that lets clients request exactly the fields they need across Canvas resources in a single request. It is well suited for dashboards and ag
  name: Canvas LMS GraphQL API
  slug: canvas-lms-graphql-api
- description: Canvas supports Learning Tools Interoperability (LTI 1.1 and LTI 1.3 / Advantage) for embedding external tools, assignments, and content into courses with deep linking, grade passback, and names-and-r
  name: Canvas LTI Integrations
  slug: canvas-lti-integrations
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Courses resource of the Canvas LMS REST API — 31 operations covering course creation, settings, users and enrollment counts, course copy, blueprint associations, effective due dates, bulk course u
  name: Canvas Courses API
  slug: canvas-courses-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Access Tokens API from Canvas — 3 operation(s) for access tokens.
  name: Canvas Access Tokens API
  slug: canvas-access-tokens-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Accessibility Course Scans API from Canvas — 1 operation(s) for accessibility course scans.
  name: Canvas Accessibility Course Scans API
  slug: canvas-accessibility-course-scans-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Accessibility Course Statistics API from Canvas — 2 operation(s) for accessibility course statistics.
  name: Canvas Accessibility Course Statistics API
  slug: canvas-accessibility-course-statistics-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Account Calendars API from Canvas — 4 operation(s) for account calendars.
  name: Canvas Account Calendars API
  slug: canvas-account-calendars-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Account Domain Lookups API from Canvas — 1 operation(s) for account domain lookups.
  name: Canvas Account Domain Lookups API
  slug: canvas-account-domain-lookups-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Account Notifications API from Canvas — 2 operation(s) for account notifications.
  name: Canvas Account Notifications API
  slug: canvas-account-notifications-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Account Reports API from Canvas — 4 operation(s) for account reports.
  name: Canvas Account Reports API
  slug: canvas-account-reports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Accounts API from Canvas — 19 operation(s) for accounts.
  name: Canvas Accounts API
  slug: canvas-accounts-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Accounts (Lti) API from Canvas — 1 operation(s) for accounts (lti).
  name: Canvas Accounts (Lti) API
  slug: canvas-accounts-lti-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Admins API from Canvas — 3 operation(s) for admins.
  name: Canvas Admins API
  slug: canvas-admins-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Ai Conversations API from Canvas — 6 operation(s) for ai conversations.
  name: Canvas Ai Conversations API
  slug: canvas-ai-conversations-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Ai Experiences API from Canvas — 6 operation(s) for ai experiences.
  name: Canvas Ai Experiences API
  slug: canvas-ai-experiences-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Analytics API from Canvas — 18 operation(s) for analytics.
  name: Canvas Analytics API
  slug: canvas-analytics-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Announcement External Feeds API from Canvas — 4 operation(s) for announcement external feeds.
  name: Canvas Announcement External Feeds API
  slug: canvas-announcement-external-feeds-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Announcements API from Canvas — 1 operation(s) for announcements.
  name: Canvas Announcements API
  slug: canvas-announcements-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Api Token Scopes API from Canvas — 1 operation(s) for api token scopes.
  name: Canvas Api Token Scopes API
  slug: canvas-api-token-scopes-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Appointment Groups API from Canvas — 5 operation(s) for appointment groups.
  name: Canvas Appointment Groups API
  slug: canvas-appointment-groups-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Assessment Question Banks API from Canvas — 3 operation(s) for assessment question banks.
  name: Canvas Assessment Question Banks API
  slug: canvas-assessment-question-banks-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Asset Processor API from Canvas — 3 operation(s) for asset processor.
  name: Canvas Asset Processor API
  slug: canvas-asset-processor-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Assignment Extensions API from Canvas — 1 operation(s) for assignment extensions.
  name: Canvas Assignment Extensions API
  slug: canvas-assignment-extensions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Assignment Groups API from Canvas — 2 operation(s) for assignment groups.
  name: Canvas Assignment Groups API
  slug: canvas-assignment-groups-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Assignments API from Canvas — 12 operation(s) for assignments.
  name: Canvas Assignments API
  slug: canvas-assignments-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Authentication Providers API from Canvas — 5 operation(s) for authentication providers.
  name: Canvas Authentication Providers API
  slug: canvas-authentication-providers-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Authentications Log API from Canvas — 3 operation(s) for authentications log.
  name: Canvas Authentications Log API
  slug: canvas-authentications-log-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Blackout Dates API from Canvas — 6 operation(s) for blackout dates.
  name: Canvas Blackout Dates API
  slug: canvas-blackout-dates-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Block Editor Template API from Canvas — 1 operation(s) for block editor template.
  name: Canvas Block Editor Template API
  slug: canvas-block-editor-template-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Blueprint Courses API from Canvas — 12 operation(s) for blueprint courses.
  name: Canvas Blueprint Courses API
  slug: canvas-blueprint-courses-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Bookmarks API from Canvas — 2 operation(s) for bookmarks.
  name: Canvas Bookmarks API
  slug: canvas-bookmarks-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Brand Configs API from Canvas — 3 operation(s) for brand configs.
  name: Canvas Brand Configs API
  slug: canvas-brand-configs-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Calendar Events API from Canvas — 8 operation(s) for calendar events.
  name: Canvas Calendar Events API
  slug: canvas-calendar-events-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Canvas Career Experiences API from Canvas — 4 operation(s) for canvas career experiences.
  name: Canvas Canvas Career Experiences API
  slug: canvas-canvas-career-experiences-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Canvas Career User Context API from Canvas — 1 operation(s) for canvas career user context.
  name: Canvas Canvas Career User Context API
  slug: canvas-canvas-career-user-context-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Collaborations API from Canvas — 5 operation(s) for collaborations.
  name: Canvas Collaborations API
  slug: canvas-collaborations-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Comm Messages API from Canvas — 1 operation(s) for comm messages.
  name: Canvas Comm Messages API
  slug: canvas-comm-messages-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Communication Channels API from Canvas — 4 operation(s) for communication channels.
  name: Canvas Communication Channels API
  slug: canvas-communication-channels-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Conferences API from Canvas — 3 operation(s) for conferences.
  name: Canvas Conferences API
  slug: canvas-conferences-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Content Exports API from Canvas — 6 operation(s) for content exports.
  name: Canvas Content Exports API
  slug: canvas-content-exports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Content Migrations API from Canvas — 25 operation(s) for content migrations.
  name: Canvas Content Migrations API
  slug: canvas-content-migrations-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Content Security Policy Settings API from Canvas — 5 operation(s) for content security policy settings.
  name: Canvas Content Security Policy Settings API
  slug: canvas-content-security-policy-settings-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Content Shares API from Canvas — 6 operation(s) for content shares.
  name: Canvas Content Shares API
  slug: canvas-content-shares-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Conversations API from Canvas — 8 operation(s) for conversations.
  name: Canvas Conversations API
  slug: canvas-conversations-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Course Audit Log API from Canvas — 2 operation(s) for course audit log.
  name: Canvas Course Audit Log API
  slug: canvas-course-audit-log-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Course Pace API from Canvas — 2 operation(s) for course pace.
  name: Canvas Course Pace API
  slug: canvas-course-pace-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Course Quiz Extensions API from Canvas — 1 operation(s) for course quiz extensions.
  name: Canvas Course Quiz Extensions API
  slug: canvas-course-quiz-extensions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Course Reports API from Canvas — 2 operation(s) for course reports.
  name: Canvas Course Reports API
  slug: canvas-course-reports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Custom Gradebook Columns API from Canvas — 6 operation(s) for custom gradebook columns.
  name: Canvas Custom Gradebook Columns API
  slug: canvas-custom-gradebook-columns-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Developer Key Account Bindings API from Canvas — 1 operation(s) for developer key account bindings.
  name: Canvas Developer Key Account Bindings API
  slug: canvas-developer-key-account-bindings-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Developer Keys API from Canvas — 3 operation(s) for developer keys.
  name: Canvas Developer Keys API
  slug: canvas-developer-keys-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Discovery Pages API from Canvas — 2 operation(s) for discovery pages.
  name: Canvas Discovery Pages API
  slug: canvas-discovery-pages-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Discussion Topics API from Canvas — 36 operation(s) for discussion topics.
  name: Canvas Discussion Topics API
  slug: canvas-discussion-topics-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The E Portfolios API from Canvas — 5 operation(s) for e portfolios.
  name: Canvas E Portfolios API
  slug: canvas-e-portfolios-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The E Pub Exports API from Canvas — 3 operation(s) for e pub exports.
  name: Canvas E Pub Exports API
  slug: canvas-e-pub-exports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Enrollment Terms API from Canvas — 2 operation(s) for enrollment terms.
  name: Canvas Enrollment Terms API
  slug: canvas-enrollment-terms-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Enrollments API from Canvas — 12 operation(s) for enrollments.
  name: Canvas Enrollments API
  slug: canvas-enrollments-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Error Reports API from Canvas — 1 operation(s) for error reports.
  name: Canvas Error Reports API
  slug: canvas-error-reports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The External Tools API from Canvas — 11 operation(s) for external tools.
  name: Canvas External Tools API
  slug: canvas-external-tools-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Favorites API from Canvas — 4 operation(s) for favorites.
  name: Canvas Favorites API
  slug: canvas-favorites-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Feature Flags API from Canvas — 10 operation(s) for feature flags.
  name: Canvas Feature Flags API
  slug: canvas-feature-flags-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Files API from Canvas — 43 operation(s) for files.
  name: Canvas Files API
  slug: canvas-files-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Grade Change Log API from Canvas — 5 operation(s) for grade change log.
  name: Canvas Grade Change Log API
  slug: canvas-grade-change-log-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Gradebook History API from Canvas — 4 operation(s) for gradebook history.
  name: Canvas Gradebook History API
  slug: canvas-gradebook-history-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Grading Period Sets API from Canvas — 2 operation(s) for grading period sets.
  name: Canvas Grading Period Sets API
  slug: canvas-grading-period-sets-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Grading Periods API from Canvas — 6 operation(s) for grading periods.
  name: Canvas Grading Periods API
  slug: canvas-grading-periods-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Grading Standards API from Canvas — 4 operation(s) for grading standards.
  name: Canvas Grading Standards API
  slug: canvas-grading-standards-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Group Categories API from Canvas — 12 operation(s) for group categories.
  name: Canvas Group Categories API
  slug: canvas-group-categories-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Groups API from Canvas — 17 operation(s) for groups.
  name: Canvas Groups API
  slug: canvas-groups-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The History API from Canvas — 1 operation(s) for history.
  name: Canvas History API
  slug: canvas-history-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Inst Access Tokens API from Canvas — 1 operation(s) for inst access tokens.
  name: Canvas Inst Access Tokens API
  slug: canvas-inst-access-tokens-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Late Policy API from Canvas — 1 operation(s) for late policy.
  name: Canvas Late Policy API
  slug: canvas-late-policy-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Learning Object Dates API from Canvas — 6 operation(s) for learning object dates.
  name: Canvas Learning Object Dates API
  slug: canvas-learning-object-dates-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Line Items API from Canvas — 2 operation(s) for line items.
  name: Canvas Line Items API
  slug: canvas-line-items-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Live Assessments API from Canvas — 2 operation(s) for live assessments.
  name: Canvas Live Assessments API
  slug: canvas-live-assessments-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Logins API from Canvas — 5 operation(s) for logins.
  name: Canvas Logins API
  slug: canvas-logins-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Lti Context Controls API from Canvas — 4 operation(s) for lti context controls.
  name: Canvas Lti Context Controls API
  slug: canvas-lti-context-controls-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Lti Launch Definitions API from Canvas — 2 operation(s) for lti launch definitions.
  name: Canvas Lti Launch Definitions API
  slug: canvas-lti-launch-definitions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Lti Registrations API from Canvas — 28 operation(s) for lti registrations.
  name: Canvas Lti Registrations API
  slug: canvas-lti-registrations-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Lti Resource Links API from Canvas — 3 operation(s) for lti resource links.
  name: Canvas Lti Resource Links API
  slug: canvas-lti-resource-links-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Media Objects API from Canvas — 10 operation(s) for media objects.
  name: Canvas Media Objects API
  slug: canvas-media-objects-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Moderated Grading API from Canvas — 7 operation(s) for moderated grading.
  name: Canvas Moderated Grading API
  slug: canvas-moderated-grading-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Modules API from Canvas — 10 operation(s) for modules.
  name: Canvas Modules API
  slug: canvas-modules-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Names And Role API from Canvas — 2 operation(s) for names and role.
  name: Canvas Names And Role API
  slug: canvas-names-and-role-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The New Quiz Items API from Canvas — 3 operation(s) for new quiz items.
  name: Canvas New Quiz Items API
  slug: canvas-new-quiz-items-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The New Quizzes Accommodations API from Canvas — 2 operation(s) for new quizzes accommodations.
  name: Canvas New Quizzes Accommodations API
  slug: canvas-new-quizzes-accommodations-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The New Quizzes API from Canvas — 2 operation(s) for new quizzes.
  name: Canvas New Quizzes API
  slug: canvas-new-quizzes-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The New Quizzes Reports API from Canvas — 1 operation(s) for new quizzes reports.
  name: Canvas New Quizzes Reports API
  slug: canvas-new-quizzes-reports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Notice Handlers API from Canvas — 1 operation(s) for notice handlers.
  name: Canvas Notice Handlers API
  slug: canvas-notice-handlers-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Notification Preferences API from Canvas — 10 operation(s) for notification preferences.
  name: Canvas Notification Preferences API
  slug: canvas-notification-preferences-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Originality Reports API from Canvas — 3 operation(s) for originality reports.
  name: Canvas Originality Reports API
  slug: canvas-originality-reports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Outcome Groups API from Canvas — 22 operation(s) for outcome groups.
  name: Canvas Outcome Groups API
  slug: canvas-outcome-groups-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Outcome Imports API from Canvas — 6 operation(s) for outcome imports.
  name: Canvas Outcome Imports API
  slug: canvas-outcome-imports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Outcome Results API from Canvas — 6 operation(s) for outcome results.
  name: Canvas Outcome Results API
  slug: canvas-outcome-results-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Outcomes API from Canvas — 2 operation(s) for outcomes.
  name: Canvas Outcomes API
  slug: canvas-outcomes-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Pages API from Canvas — 13 operation(s) for pages.
  name: Canvas Pages API
  slug: canvas-pages-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Peer Reviews API from Canvas — 5 operation(s) for peer reviews.
  name: Canvas Peer Reviews API
  slug: canvas-peer-reviews-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Plagiarism Detection Platform Assignments API from Canvas — 1 operation(s) for plagiarism detection platform assignments.
  name: Canvas Plagiarism Detection Platform Assignments API
  slug: canvas-plagiarism-detection-platform-assignments-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Plagiarism Detection Platform Users API from Canvas — 2 operation(s) for plagiarism detection platform users.
  name: Canvas Plagiarism Detection Platform Users API
  slug: canvas-plagiarism-detection-platform-users-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Plagiarism Detection Submissions API from Canvas — 2 operation(s) for plagiarism detection submissions.
  name: Canvas Plagiarism Detection Submissions API
  slug: canvas-plagiarism-detection-submissions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Planner API from Canvas — 6 operation(s) for planner.
  name: Canvas Planner API
  slug: canvas-planner-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Poll Choices API from Canvas — 2 operation(s) for poll choices.
  name: Canvas Poll Choices API
  slug: canvas-poll-choices-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Poll Sessions API from Canvas — 6 operation(s) for poll sessions.
  name: Canvas Poll Sessions API
  slug: canvas-poll-sessions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Poll Submissions API from Canvas — 2 operation(s) for poll submissions.
  name: Canvas Poll Submissions API
  slug: canvas-poll-submissions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Polls API from Canvas — 2 operation(s) for polls.
  name: Canvas Polls API
  slug: canvas-polls-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Portfolio Notifications API from Canvas — 1 operation(s) for portfolio notifications.
  name: Canvas Portfolio Notifications API
  slug: canvas-portfolio-notifications-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Proficiency Ratings API from Canvas — 2 operation(s) for proficiency ratings.
  name: Canvas Proficiency Ratings API
  slug: canvas-proficiency-ratings-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Progress API from Canvas — 3 operation(s) for progress.
  name: Canvas Progress API
  slug: canvas-progress-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Public Jwk API from Canvas — 1 operation(s) for public jwk.
  name: Canvas Public Jwk API
  slug: canvas-public-jwk-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Assignment Overrides API from Canvas — 2 operation(s) for quiz assignment overrides.
  name: Canvas Quiz Assignment Overrides API
  slug: canvas-quiz-assignment-overrides-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Extensions API from Canvas — 1 operation(s) for quiz extensions.
  name: Canvas Quiz Extensions API
  slug: canvas-quiz-extensions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Ip Filters API from Canvas — 1 operation(s) for quiz ip filters.
  name: Canvas Quiz Ip Filters API
  slug: canvas-quiz-ip-filters-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Question Groups API from Canvas — 3 operation(s) for quiz question groups.
  name: Canvas Quiz Question Groups API
  slug: canvas-quiz-question-groups-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Questions API from Canvas — 2 operation(s) for quiz questions.
  name: Canvas Quiz Questions API
  slug: canvas-quiz-questions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Reports API from Canvas — 2 operation(s) for quiz reports.
  name: Canvas Quiz Reports API
  slug: canvas-quiz-reports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Statistics API from Canvas — 1 operation(s) for quiz statistics.
  name: Canvas Quiz Statistics API
  slug: canvas-quiz-statistics-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Submission Events API from Canvas — 1 operation(s) for quiz submission events.
  name: Canvas Quiz Submission Events API
  slug: canvas-quiz-submission-events-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Submission Files API from Canvas — 1 operation(s) for quiz submission files.
  name: Canvas Quiz Submission Files API
  slug: canvas-quiz-submission-files-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Submission Questions API from Canvas — 4 operation(s) for quiz submission questions.
  name: Canvas Quiz Submission Questions API
  slug: canvas-quiz-submission-questions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Submission User List API from Canvas — 1 operation(s) for quiz submission user list.
  name: Canvas Quiz Submission User List API
  slug: canvas-quiz-submission-user-list-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Submissions API from Canvas — 5 operation(s) for quiz submissions.
  name: Canvas Quiz Submissions API
  slug: canvas-quiz-submissions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quizzes API from Canvas — 4 operation(s) for quizzes.
  name: Canvas Quizzes API
  slug: canvas-quizzes-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Result API from Canvas — 2 operation(s) for result.
  name: Canvas Result API
  slug: canvas-result-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Roles API from Canvas — 6 operation(s) for roles.
  name: Canvas Roles API
  slug: canvas-roles-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Rubrics API from Canvas — 15 operation(s) for rubrics.
  name: Canvas Rubrics API
  slug: canvas-rubrics-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Sandboxes API from Canvas — 1 operation(s) for sandboxes.
  name: Canvas Sandboxes API
  slug: canvas-sandboxes-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Score API from Canvas — 1 operation(s) for score.
  name: Canvas Score API
  slug: canvas-score-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Search API from Canvas — 3 operation(s) for search.
  name: Canvas Search API
  slug: canvas-search-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Sections API from Canvas — 6 operation(s) for sections.
  name: Canvas Sections API
  slug: canvas-sections-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Services API from Canvas — 2 operation(s) for services.
  name: Canvas Services API
  slug: canvas-services-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Shared Brand Configs API from Canvas — 3 operation(s) for shared brand configs.
  name: Canvas Shared Brand Configs API
  slug: canvas-shared-brand-configs-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Sis Import Errors API from Canvas — 2 operation(s) for sis import errors.
  name: Canvas Sis Import Errors API
  slug: canvas-sis-import-errors-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Sis Imports API from Canvas — 6 operation(s) for sis imports.
  name: Canvas Sis Imports API
  slug: canvas-sis-imports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Sis Integration API from Canvas — 3 operation(s) for sis integration.
  name: Canvas Sis Integration API
  slug: canvas-sis-integration-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Smart Search API from Canvas — 1 operation(s) for smart search.
  name: Canvas Smart Search API
  slug: canvas-smart-search-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Study Assist API from Canvas — 1 operation(s) for study assist.
  name: Canvas Study Assist API
  slug: canvas-study-assist-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Submission Comments API from Canvas — 3 operation(s) for submission comments.
  name: Canvas Submission Comments API
  slug: canvas-submission-comments-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Submissions API from Canvas — 32 operation(s) for submissions.
  name: Canvas Submissions API
  slug: canvas-submissions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Tabs API from Canvas — 5 operation(s) for tabs.
  name: Canvas Tabs API
  slug: canvas-tabs-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Temporary Enrollment Pairings API from Canvas — 3 operation(s) for temporary enrollment pairings.
  name: Canvas Temporary Enrollment Pairings API
  slug: canvas-temporary-enrollment-pairings-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The User Observees API from Canvas — 5 operation(s) for user observees.
  name: Canvas User Observees API
  slug: canvas-user-observees-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Users API from Canvas — 38 operation(s) for users.
  name: Canvas Users API
  slug: canvas-users-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Webhooks Subscriptions For Plagiarism Platform API from Canvas — 2 operation(s) for webhooks subscriptions for plagiarism platform.
  name: Canvas Webhooks Subscriptions For Plagiarism Platform API
  slug: canvas-webhooks-subscriptions-for-plagiarism-platform-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The What If Grades API from Canvas — 2 operation(s) for what if grades.
  name: Canvas What If Grades API
  slug: canvas-what-if-grades-api
- baseURL: https://canvas.instructure.com/api/graphql
  baseurl_source: declared
  description: The JWTs API from Canvas — 2 operation(s) for jwts.
  name: Canvas JW Ts API
  slug: canvas-jwts-api
artifact_total: 159
asyncapis:
- description: ''
  name: Canvas Live Events Webhooks
  slug: canvas-live-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Canvas LMS REST API ( subset) Courses API
  slug: open-canvas-courses-api
- collection_type: open
  name: Canvas LMS REST API (Courses subset)
  slug: open-canvas
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/scopes/canvas-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/canvas-scopes.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/instructure/canvas-lms/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/instructure/canvas-lms/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/instructure/canvas-lms/blob/master/code_of_conduct.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/instructure/canvas-lms/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/instructure/canvas-lms/blob/master/LICENSE
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/agentic-access/canvas-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/canvas-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/security/canvas-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/canvas-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/security/canvas-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/canvas-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/security/canvas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canvas-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/authentication/canvas-authentication.yml
  title: ''
  type: Authentication
  url: authentication/canvas-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/canvaslms
- group: company
  title: ''
  type: Website
  url: https://www.instructure.com/canvas
- group: docs
  title: ''
  type: Documentation
  url: https://canvas.instructure.com/doc/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instructure
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/instructure/canvas-lms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.instructure.com/
- group: operate
  title: ''
  type: Community
  url: https://community.canvaslms.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instructure.com/policies/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.instructure.com/resources/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.instructure.com/policies/acceptable-use
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/packages/canvas-packages.yml
  title: ''
  type: Packages
  url: packages/canvas-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/packages/canvas-packages.yml
  title: ''
  type: SDKs
  url: packages/canvas-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/well-known/canvas-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canvas-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/well-known/canvas-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/canvas-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/llms/canvas-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canvas-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/mcp/canvas-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/canvas-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/conformance/canvas-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canvas-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.instructure.com/trust-center
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/errors/canvas-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canvas-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/lifecycle/canvas-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/canvas-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://community.canvaslms.com/t5/Change-Log/tkb-p/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/changelog/canvas-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/canvas-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/conventions/canvas-conventions.yml
  title: ''
  type: Conventions
  url: conventions/canvas-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/sandbox/canvas-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/canvas-sandbox.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/cli/canvas-cli.yml
  title: ''
  type: CLI
  url: cli/canvas-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/components/canvas-components.yml
  title: ''
  type: Components
  url: components/canvas-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/data-model/canvas-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canvas-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/asyncapi/canvas-live-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/canvas-live-events-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/rate-limits/canvas-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/canvas-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/plans/canvas-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canvas-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://www.instructure.com/trust-center/vulnerability-disclosure
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/overlays/canvas-canvas-lms-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canvas-canvas-lms-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/overlays/canvas-canvas-courses-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canvas-canvas-courses-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developerdocs.instructure.com/services/canvas
- group: docs
  title: ''
  type: APIReference
  url: https://canvas.instructure.com/doc/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developerdocs.instructure.com/services/canvas/oauth2/file.oauth
- group: operate
  title: ''
  type: Support
  url: https://community.canvaslms.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.instructure.com/canvas/free-for-teacher
- group: commercial
  title: ''
  type: Pricing
  url: https://www.instructure.com/canvas
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/mcp/canvas-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/canvas-mcp.yml
created: '2025-01-14'
description: Canvas is Instructure's open-source learning management system (LMS) used by K-12, higher education, and corporate training organizations to deliver courses, assessments, and learner communication. Canvas exposes a comprehensive REST API and a GraphQL endpoint for reading and modifying courses, assignments, quizzes, grades, users, enrollments, content, and account administration, and it integrates with external tools through LTI, Caliper, and live event streams.
finops:
- name: Canvas Finops
  service_category: API
  slug: canvas-finops
graphqls:
- description: The Canvas LMS GraphQL API is an alternative to the REST API that lets clients request exactly the fields they need across Canvas resources in a single request. It is well suited for dashboards and ag
  name: Canvas GraphQL API
  slug: canvas-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canvas.png
layout: provider
modified: '2026-09-05'
name: Canvas
nav: Providers
network: true
overview: 'Canvas publishes 143 APIs on the [APIs.io](https://apis.io/) network, including Courses API, Access Tokens API, Accessibility Course Scans API, and 140 more. Tagged areas include Education, EdTech, GraphQL, Learning Management System, and LMS.


  The Canvas catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Canvas'' developer surface includes authentication, documentation, engineering blog, changelog, sandbox, CLI, API reference, and 45 more developer resources.'
plans:
- name: Canvas Plans Pricing
  plan_count: 1
  slug: canvas-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Canvas Rate Limits
  slug: canvas-rate-limits
scopes:
- name: Canvas Scopes
  scope_count: 1117
  slug: canvas-scopes
  summary_line: 1117 scopes · authorizationCode
score:
  band: exemplar
  composite: 71.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 46.0
    catalog_earned_first_party: 16.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 24.2
    developer_ergonomics: 80.4
    discoverability: 57.4
    operational_transparency: 81.6
  open_source:
    applies: true
    score: 75.0
  previous_composite: 73.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 143
      marker_coverage: 100.0
      total: 143
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 85.2
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/canvas/refs/heads/main/screenshots/canvas-2026-06-20T173929.png
security:
- kind: authentication
  name: Canvas Authentication
  slug: canvas-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Canvas Domain Security
  slug: canvas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Canvas Vulnerability Disclosure
  slug: canvas-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Canvas Trust Center
  slug: canvas-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: canvas
tags:
- Education
- EdTech
- GraphQL
- Learning Management System
- LMS
- LTI
- Open-Source
- REST
website: https://www.instructure.com/canvas
---
