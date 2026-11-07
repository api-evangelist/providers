---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-11-06'
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
  phrasing_intents:
  - id: create_new_course
    intent: Create a new course in an account
    question: How do I create a new course in a Canvas sub-account?
  - id: update_courses
    intent: Bulk offer, conclude or delete courses
    question: Can I conclude a whole batch of courses in an account at once?
  - id: list_your_courses
    intent: List my active courses
    question: Which courses am I currently enrolled in?
  - id: list_courses_for_user
    intent: List courses for a specific user
    question: What courses is a particular student taking?
  - id: get_user_progress
    intent: Get one user's progress in a course
    question: How far along is a single student in completing a course's requirements?
  - id: upload_file
    intent: Start a file upload to a course
    question: How do I upload a file into a course's files area?
  - id: list_students
    intent: List students via the deprecated endpoint
    question: Is there an older endpoint that just returns the students of a course?
  - id: list_users_in_course_users
    intent: List users in a course
    question: Who is enrolled in a course, including teachers and TAs?
  phrasing_ops: 31
  slug: canvas-courses-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Access Tokens API from Canvas — 3 operation(s) for access tokens.
  name: Canvas Access Tokens API
  phrasing_intents:
  - id: list_access_tokens_for_user
    intent: List a user's manually generated access tokens
    question: Which personal access tokens has a Canvas user generated?
  - id: show_access_token
    intent: Show an access token
    question: How do I look up one access token using its token hint?
  - id: update_access_token
    intent: Update or regenerate an access token
    question: Can I extend an access token's expiration date?
  - id: delete_access_token
    intent: Delete an access token
    question: How do I revoke a personal access token?
  - id: create_access_token
    intent: Create an access token for a user
    question: How do I generate a new API access token for a user?
  phrasing_ops: 5
  slug: canvas-access-tokens-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Accessibility Course Scans API from Canvas — 1 operation(s) for accessibility course scans.
  name: Canvas Accessibility Course Scans API
  phrasing_intents:
  - id: trigger_accessibility_course_scan
    intent: Scan my courses for accessibility issues
    question: How do I run an accessibility check across all the courses I teach?
  phrasing_ops: 1
  slug: canvas-accessibility-course-scans-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Accessibility Course Statistics API from Canvas — 2 operation(s) for accessibility course statistics.
  name: Canvas Accessibility Course Statistics API
  phrasing_intents:
  - id: list_accessibility_course_statistics
    intent: List accessibility issue counts per course I teach
    question: How many accessibility issues does each of my Canvas courses have?
  - id: list_accessibility_course_statistic_terms
    intent: List terms for the accessibility statistics filter
    question: Which enrollment terms can I filter my accessibility course statistics by?
  phrasing_ops: 2
  slug: canvas-accessibility-course-statistics-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Account Calendars API from Canvas — 4 operation(s) for account calendars.
  name: Canvas Account Calendars API
  phrasing_intents:
  - id: list_available_account_calendars
    intent: List account calendars I can subscribe to
    question: Which institution-wide calendars can I add to my Canvas calendar?
  - id: get_single_account_calendar
    intent: Get one account calendar
    question: Is a particular department's calendar visible and auto-subscribed?
  - id: update_calendar
    intent: Set an account calendar's visibility
    question: Can I hide one account calendar or make users auto-subscribe to it?
  - id: update_several_calendars
    intent: Change visibility on many account calendars
    question: Can I show or hide a batch of sub-account calendars at once?
  - id: list_all_account_calendars
    intent: List calendars for an account and sub-accounts
    question: Can an admin see every account calendar, including hidden ones, under an account?
  - id: count_of_all_visible_account_calendars
    intent: Count visible account calendars
    question: How many account calendars are currently visible to users?
  phrasing_ops: 6
  slug: canvas-account-calendars-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Account Domain Lookups API from Canvas — 1 operation(s) for account domain lookups.
  name: Canvas Account Domain Lookups API
  phrasing_intents:
  - id: search_account_domains
    intent: Find a school's Canvas domain
    question: How can I find my school's Canvas login domain by its name?
  phrasing_ops: 1
  slug: canvas-account-domain-lookups-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Account Notifications API from Canvas — 2 operation(s) for account notifications.
  name: Canvas Account Notifications API
  phrasing_intents:
  - id: index_of_active_global_notification_for_user
    intent: List my active account announcements
    question: What global announcements are showing for me in this account?
  - id: create_global_notification
    intent: Post a global account announcement
    question: How do I put a banner announcement in front of everyone in an account?
  - id: show_global_notification
    intent: Get a global account announcement
    question: What does a particular account announcement say?
  - id: update_global_notification
    intent: Edit a global account announcement
    question: Can I change the message or end date of an account announcement?
  - id: close_notification_for_user_destroy_notification_for_admin
    intent: Close or delete an account announcement
    question: How do I dismiss an account announcement so I stop seeing it?
  phrasing_ops: 5
  slug: canvas-account-notifications-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Account Reports API from Canvas — 4 operation(s) for account reports.
  name: Canvas Account Reports API
  phrasing_intents:
  - id: list_available_reports
    intent: List report types an account can run
    question: Which reports can I run on my Canvas account?
  - id: start_report
    intent: Run an account report
    question: How do I generate a provisioning or SIS export report for my account?
  - id: index_of_reports
    intent: List past runs of one report type
    question: How many times has a specific report been run on my account?
  - id: status_of_report
    intent: Check an account report's status
    question: Is my account report finished, and where can I download it?
  - id: delete_report
    intent: Delete a generated account report
    question: How do I delete an old report file from my account?
  - id: abort_report
    intent: Abort a running account report
    question: How do I stop a report that's still running?
  phrasing_ops: 6
  slug: canvas-account-reports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Accounts API from Canvas — 19 operation(s) for accounts.
  name: Canvas Accounts API
  phrasing_intents:
  - id: list_accounts
    intent: List accounts I can view or manage
    question: Which Canvas accounts am I an admin of?
  - id: list_horizon_accounts
    intent: List accounts with Horizon enabled
    question: Which of my accounts have the Horizon setting turned on?
  - id: get_accounts_that_admins_can_manage
    intent: List accounts where I can manage courses
    question: In which accounts do I have permission to create or manage courses as an admin?
  - id: get_accounts_that_users_can_create_courses_in
    intent: List accounts where I can create courses
    question: Where am I allowed to create a new course?
  - id: list_accounts_for_course_admins
    intent: List accounts visible through my teaching roles
    question: As a teacher or TA, which accounts can I see through my course enrollments?
  - id: get_single_account
    intent: Get details of an account
    question: What are the details of a specific account, by ID or SIS ID?
  - id: update_account
    intent: Update an account's name and settings
    question: How do I rename an account or change its default time zone?
  - id: settings
    intent: Get an account's settings
    question: What settings are configured on my account?
  phrasing_ops: 21
  slug: canvas-accounts-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Accounts (Lti) API from Canvas — 1 operation(s) for accounts (lti).
  name: Canvas Accounts (Lti) API
  phrasing_intents:
  - id: get_account
    intent: Get account details for an LTI tool
    question: How can an LTI tool look up the account it's installed in?
  phrasing_ops: 1
  slug: canvas-accounts-lti-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Admins API from Canvas — 3 operation(s) for admins.
  name: Canvas Admins API
  phrasing_intents:
  - id: list_account_admins
    intent: List an account's admins
    question: Who are the admins on my Canvas account?
  - id: make_account_admin
    intent: Make a user an account admin
    question: How do I give an existing user admin rights on an account?
  - id: remove_account_admin
    intent: Remove a user's account admin role
    question: How do I revoke someone's admin rights on an account?
  - id: list_my_admin_roles
    intent: List my own admin roles in an account
    question: What admin roles do I have on an account?
  phrasing_ops: 4
  slug: canvas-admins-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Ai Conversations API from Canvas — 6 operation(s) for ai conversations.
  name: Canvas Ai Conversations API
  phrasing_intents:
  - id: show_conversation
    intent: View a student's AI conversation
    question: As a teacher, can I read a specific student's conversation with an AI experience?
  - id: delete_ai_conversation
    intent: End an AI conversation session
    question: How do I end the current AI conversation session?
  - id: get_active_conversation
    intent: Get my active AI conversation
    question: Do I already have an ongoing conversation with this AI experience?
  - id: create_ai_conversation
    intent: Start a new AI conversation
    question: How do I start a fresh conversation with a course's AI experience?
  - id: post_message_to_conversation
    intent: Send a message to an AI conversation
    question: How do I send a message and get the AI's reply in a conversation?
  - id: get_conversation_evaluation
    intent: Read a conversation's stored evaluation
    question: Can I see the latest saved evaluation of an AI conversation without rerunning it?
  - id: generate_conversation_evaluation
    intent: Generate or reset a conversation's evaluation
    question: How do I have the LLM re-evaluate a student's AI conversation?
  - id: create_feedback_on_conversation_message
    intent: Like or dislike an AI reply
    question: Can I give a thumbs up or down on an AI-generated message?
  phrasing_ops: 9
  slug: canvas-ai-conversations-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Ai Experiences API from Canvas — 6 operation(s) for ai experiences.
  name: Canvas Ai Experiences API
  phrasing_intents:
  - id: list_ai_experiences
    intent: List a course's AI experiences
    question: What AI experiences are set up in my course?
  - id: create_ai_experience
    intent: Create an AI experience for a course
    question: How do I set up a new AI learning experience with a learning objective in my course?
  - id: show_ai_experience
    intent: Get an AI experience
    question: What are the learning objective and guidance of one AI experience?
  - id: update_ai_experience
    intent: Update an AI experience
    question: How do I change the learning objective of an existing AI experience?
  - id: delete_ai_experience
    intent: Delete an AI experience
    question: Is deleting an AI experience permanent or a soft delete?
  - id: show_new_ai_experience_form
    intent: Open the form for a new AI experience
    question: Where is the form for starting a new AI experience in a course?
  - id: show_edit_ai_experience_form
    intent: Open the edit form for an AI experience
    question: Where is the edit form for an existing AI experience?
  - id: list_student_ai_conversations
    intent: List students' latest AI conversations for an experience
    question: How have my students been chatting with an AI experience?
  phrasing_ops: 9
  slug: canvas-ai-experiences-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Analytics API from Canvas — 18 operation(s) for analytics.
  name: Canvas Analytics API
  phrasing_intents:
  - id: get_department_level_participation_data_terms
    intent: Get department page views for a term
    question: How much page-view activity did a department see during a specific term?
  - id: get_department_level_participation_data_current
    intent: Get department page views for current courses
    question: How active are students in a department's currently running courses?
  - id: get_department_level_participation_data_completed
    intent: Get department page views for completed courses
    question: How much activity did a department's concluded courses get?
  - id: get_department_level_grade_data_terms
    intent: Get a department's grade distribution for a term
    question: What did the grade distribution look like across a department for one term?
  - id: get_department_level_grade_data_current
    intent: Get a department's grade distribution for current courses
    question: What is the current grade distribution across a department's active courses?
  - id: get_department_level_grade_data_completed
    intent: Get a department's grade distribution for completed courses
    question: What were the final grade distributions for a department's concluded courses?
  - id: get_department_level_statistics_terms
    intent: Get department statistics for a term
    question: How many courses, teachers and students did a department have in a term?
  - id: get_department_level_statistics_current
    intent: Get department statistics for current courses
    question: What are the headline numbers for a department's active courses?
  phrasing_ops: 18
  slug: canvas-analytics-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Announcement External Feeds API from Canvas — 4 operation(s) for announcement external feeds.
  name: Canvas Announcement External Feeds API
  phrasing_intents:
  - id: list_external_feeds_courses
    intent: List a course's external announcement feeds
    question: Which RSS feeds are posting announcements into my course?
  - id: create_external_feed_courses
    intent: Add an external feed to a course
    question: How do I pipe an RSS feed into a course's announcements?
  - id: list_external_feeds_groups
    intent: List a group's external announcement feeds
    question: Which external feeds post into a student group's announcements?
  - id: create_external_feed_groups
    intent: Add an external feed to a group
    question: Can a student group pull announcements from an outside RSS feed?
  - id: delete_external_feed_courses
    intent: Remove an external feed from a course
    question: Can I disconnect an RSS feed from a course?
  - id: delete_external_feed_groups
    intent: Remove an external feed from a group
    question: Can I remove an RSS feed from a student group?
  phrasing_ops: 6
  slug: canvas-announcement-external-feeds-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Announcements API from Canvas — 1 operation(s) for announcements.
  name: Canvas Announcements API
  phrasing_intents:
  - id: list_announcements
    intent: List announcements across courses
    question: Is there a way to pull announcements from several courses at once?
  phrasing_ops: 1
  slug: canvas-announcements-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Api Token Scopes API from Canvas — 1 operation(s) for api token scopes.
  name: Canvas Api Token Scopes API
  phrasing_intents:
  - id: list_scopes
    intent: List API scopes for developer keys and tokens
    question: Which API scopes can I apply to a Canvas developer key or access token?
  phrasing_ops: 1
  slug: canvas-api-token-scopes-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Appointment Groups API from Canvas — 5 operation(s) for appointment groups.
  name: Canvas Appointment Groups API
  phrasing_intents:
  - id: list_appointment_groups
    intent: List appointment groups
    question: Which office-hours sign-up groups can I reserve or manage?
  - id: create_appointment_group
    intent: Create an appointment group
    question: How do I set up sign-up slots for office hours in a course?
  - id: get_single_appointment_group
    intent: Get an appointment group
    question: How do I see the details and slots of one appointment group?
  - id: update_appointment_group
    intent: Update an appointment group
    question: Can I change the title or location of an existing sign-up group?
  - id: delete_appointment_group
    intent: Delete an appointment group
    question: What happens to existing reservations when I delete an appointment group?
  - id: list_user_participants
    intent: List users in an appointment group
    question: Which students have signed up for an appointment group?
  - id: list_student_group_participants
    intent: List student groups in an appointment group
    question: Which student groups have booked a group-based appointment slot?
  - id: get_next_appointment
    intent: Find the next open appointment
    question: What's the next appointment slot I could sign up for?
  phrasing_ops: 8
  slug: canvas-appointment-groups-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Assessment Question Banks API from Canvas — 3 operation(s) for assessment question banks.
  name: Canvas Assessment Question Banks API
  phrasing_intents:
  - id: list_question_banks
    intent: List question banks in a context
    question: What question banks exist in a course?
  - id: get_single_question_bank
    intent: Get a single question bank
    question: What are the details of one question bank?
  - id: list_assessment_questions_for_question_bank
    intent: List questions in a question bank
    question: Which questions are inside a particular question bank?
  phrasing_ops: 3
  slug: canvas-assessment-question-banks-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Asset Processor API from Canvas — 3 operation(s) for asset processor.
  name: Canvas Asset Processor API
  phrasing_intents:
  - id: create_asset_report
    intent: Submit an asset processor report for a submission file
    question: How does an LTI asset processor tool post its result back for a student's submission attachment?
  - id: update_eula_deployment_configuration
    intent: Turn the EULA requirement on or off for a deployment
    question: Can a tool require every user in a deployment to accept a EULA?
  - id: create_eula_acceptance
    intent: Record whether a user accepted the tool EULA
    question: How does a tool tell Canvas that a user accepted its EULA?
  - id: delete_eula_acceptances_for_deployment
    intent: Reset EULA acceptances for all users in a deployment
    question: After our EULA changes, how do I force every user to accept it again?
  phrasing_ops: 4
  slug: canvas-asset-processor-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Assignment Extensions API from Canvas — 1 operation(s) for assignment extensions.
  name: Canvas Assignment Extensions API
  phrasing_intents:
  - id: set_extensions_for_student_assignment_submissions
    intent: Give students extra attempts on an assignment
    question: How do I give a student extra attempts on an assignment?
  phrasing_ops: 1
  slug: canvas-assignment-extensions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Assignment Groups API from Canvas — 2 operation(s) for assignment groups.
  name: Canvas Assignment Groups API
  phrasing_intents:
  - id: list_assignment_groups
    intent: List a course's assignment groups
    question: What assignment groups does a course have, in order?
  - id: create_assignment_group
    intent: Create an assignment group
    question: How do I add a weighted category like Homework to a course?
  - id: get_assignment_group
    intent: Get an assignment group
    question: How do I look up a single assignment group and its assignments?
  - id: edit_assignment_group
    intent: Update an assignment group
    question: Can I change an existing group's weight or its grading rules?
  - id: destroy_assignment_group
    intent: Delete an assignment group
    question: What happens to assignments when I delete their group?
  phrasing_ops: 5
  slug: canvas-assignment-groups-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Assignments API from Canvas — 12 operation(s) for assignments.
  name: Canvas Assignments API
  phrasing_intents:
  - id: delete_assignment
    intent: Delete an assignment
    question: Can I permanently remove an assignment from a course?
  - id: get_single_assignment
    intent: Get one assignment in a course
    question: How can I look up the details of a single Canvas assignment?
  - id: edit_assignment
    intent: Edit an assignment
    question: Can I change the due date or point value of an existing assignment?
  - id: list_assignments_assignments
    intent: List a course's assignments
    question: Which assignments in my course are overdue or still upcoming?
  - id: create_assignment
    intent: Create an assignment
    question: How do I add a new assignment to a course?
  - id: list_assignments_assignment_groups
    intent: List assignments in an assignment group
    question: Which assignments belong to one assignment group, like Homework or Exams?
  - id: list_assignments_for_user
    intent: List a student's assignments in a course
    question: How can a parent or advisor see the assignments for one particular student?
  - id: duplicate_assignment
    intent: Duplicate an assignment
    question: Can I make a copy of an existing assignment?
  phrasing_ops: 20
  slug: canvas-assignments-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Authentication Providers API from Canvas — 5 operation(s) for authentication providers.
  name: Canvas Authentication Providers API
  phrasing_intents:
  - id: list_authentication_providers
    intent: List an account's login providers
    question: Which login methods are configured for a Canvas account?
  - id: add_authentication_provider
    intent: Add a login provider to an account
    question: How do I add SAML single sign-on to an account?
  - id: get_authentication_provider
    intent: Get one login provider's configuration
    question: How do I view the settings of one specific authentication provider?
  - id: update_authentication_provider
    intent: Update a login provider's settings
    question: How do I change the settings of an existing SSO provider?
  - id: delete_authentication_provider
    intent: Delete a login provider
    question: How do I remove an SSO provider from an account?
  - id: restore_deleted_authentication_provider
    intent: Restore a deleted login provider
    question: How do I undo the deletion of an authentication provider?
  - id: show_account_auth_settings
    intent: View an account's SSO settings
    question: What account-level single sign-on settings are currently in effect?
  - id: update_account_auth_settings
    intent: Change an account's SSO settings
    question: How do I change account-level settings for a mixed SSO setup?
  phrasing_ops: 9
  slug: canvas-authentication-providers-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Authentications Log API from Canvas — 3 operation(s) for authentications log.
  name: Canvas Authentications Log API
  phrasing_intents:
  - id: query_by_login
    intent: Get sign-in history for a login
    question: When did a specific Canvas login last sign in or out?
  - id: query_by_account
    intent: Get sign-in history across an account
    question: Who has been logging in to our Canvas account this week?
  - id: query_by_user
    intent: Get sign-in history for a user
    question: Has a particular user signed in recently?
  phrasing_ops: 3
  slug: canvas-authentications-log-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Blackout Dates API from Canvas — 6 operation(s) for blackout dates.
  name: Canvas Blackout Dates API
  phrasing_intents:
  - id: list_blackout_dates_courses
    intent: List a course's blackout dates
    question: Which days are blocked out from scheduling in my Canvas course?
  - id: create_blackout_date_courses
    intent: Add a blackout date to a course
    question: How do I block out spring break in one course's schedule?
  - id: update_list_of_blackout_dates
    intent: Sync a course's full list of blackout dates
    question: Can I replace all of a course's blackout dates in one call?
  - id: list_blackout_dates_accounts
    intent: List an account's blackout dates
    question: What blackout dates are set at the account level for my institution?
  - id: create_blackout_date_accounts
    intent: Add a blackout date to an account
    question: How do I add a blackout date that applies to a whole account?
  - id: get_single_blackout_date_courses
    intent: Get one blackout date in a course
    question: How do I look up a single course blackout date by its id?
  - id: update_blackout_date_courses
    intent: Update a course blackout date
    question: Can I change the end date of an existing course blackout?
  - id: delete_blackout_date_courses
    intent: Delete a course blackout date
    question: How do I remove a blackout date from a course?
  phrasing_ops: 13
  slug: canvas-blackout-dates-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Block Editor Template API from Canvas — 1 operation(s) for block editor template.
  name: Canvas Block Editor Template API
  phrasing_intents:
  - id: list_block_templates
    intent: List block editor templates for a course
    question: What page templates can I use in the Canvas block editor for my course?
  phrasing_ops: 1
  slug: canvas-block-editor-template-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Blueprint Courses API from Canvas — 12 operation(s) for blueprint courses.
  name: Canvas Blueprint Courses API
  phrasing_intents:
  - id: get_blueprint_information
    intent: Get a blueprint course template
    question: Is this course set up as a blueprint, and what does its template look like?
  - id: get_associated_course_information
    intent: List courses that receive a blueprint's updates
    question: Which courses get updates pushed from my blueprint course?
  - id: update_associated_courses
    intent: Add or remove courses linked to a blueprint
    question: How do I add courses so they inherit content from a blueprint?
  - id: begin_migration_to_push_to_associated_courses
    intent: Push blueprint changes to associated courses
    question: How do I sync my latest blueprint edits out to all associated courses?
  - id: list_blueprint_migrations
    intent: List sync migrations pushed from a blueprint
    question: What syncs has my blueprint course pushed out, most recent first?
  - id: set_or_remove_restrictions_on_blueprint_course_object
    intent: Lock or unlock a blueprint item in child courses
    question: How do I stop teachers in associated courses from editing a blueprint assignment?
  - id: get_unsynced_changes
    intent: List blueprint changes not yet synced
    question: What has changed in my blueprint since the last sync?
  - id: show_blueprint_migration
    intent: Get the status of a blueprint sync
    question: Has the blueprint sync I started finished yet?
  phrasing_ops: 13
  slug: canvas-blueprint-courses-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Bookmarks API from Canvas — 2 operation(s) for bookmarks.
  name: Canvas Bookmarks API
  phrasing_intents:
  - id: list_bookmarks
    intent: List my bookmarks
    question: What bookmarks have I saved in Canvas?
  - id: create_bookmark
    intent: Create a bookmark
    question: How do I save a bookmark to a page or course?
  - id: get_bookmark
    intent: Get a bookmark
    question: What URL does one of my bookmarks point to?
  - id: update_bookmark
    intent: Update a bookmark
    question: How do I rename one of my bookmarks?
  - id: delete_bookmark
    intent: Delete a bookmark
    question: How do I remove a bookmark I no longer need?
  phrasing_ops: 5
  slug: canvas-bookmarks-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Brand Configs API from Canvas — 3 operation(s) for brand configs.
  name: Canvas Brand Configs API
  phrasing_intents:
  - id: get_brand_config_variables_that_should_be_used_for_this_domain
    intent: Get the theme variables for this domain
    question: What brand colors and logos does this Canvas domain use?
  - id: get_brand_config_variables_for_sub_account_or_course_accounts
    intent: Get the theme variables for a sub-account
    question: Which brand colors does a particular sub-account use?
  - id: get_brand_config_variables_for_sub_account_or_course_courses
    intent: Get the theme variables applied to a course
    question: What branding is applied to a specific course?
  phrasing_ops: 3
  slug: canvas-brand-configs-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Calendar Events API from Canvas — 8 operation(s) for calendar events.
  name: Canvas Calendar Events API
  phrasing_intents:
  - id: list_calendar_events
    intent: List my calendar events
    question: What's on my Canvas calendar between two dates?
  - id: create_calendar_event
    intent: Create a calendar event
    question: How do I add an event to a course calendar?
  - id: list_calendar_events_for_user
    intent: List another user's calendar events
    question: As a parent observer, can I see my student's calendar?
  - id: get_single_calendar_event_or_assignment
    intent: Get one calendar event or assignment
    question: How do I see the full details of a single calendar entry?
  - id: update_calendar_event
    intent: Update a calendar event
    question: Can I move an existing event to a new time or location?
  - id: delete_calendar_event
    intent: Delete a calendar event
    question: How do I cancel an event and tell attendees why?
  - id: reserve_time_slot
    intent: Reserve an appointment time slot
    question: How do I book an open office-hours slot?
  - id: reserve_time_slot_participant_id
    intent: Reserve a time slot for a specific participant
    question: Can an instructor book an appointment slot on behalf of a particular student?
  phrasing_ops: 12
  slug: canvas-calendar-events-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Canvas Career Experiences API from Canvas — 4 operation(s) for canvas career experiences.
  name: Canvas Canvas Career Experiences API
  phrasing_intents:
  - id: check_if_canvas_career_is_enabled
    intent: Check if Canvas Career is enabled
    question: Is Canvas Career turned on anywhere in our root account?
  - id: get_current_and_available_experiences
    intent: Show my current and available experiences
    question: Which experience am I in right now, and which others can I switch to?
  - id: switch_experience
    intent: Switch my active experience
    question: How do I switch from the academic experience to Canvas Career?
  - id: switch_role
    intent: Switch my role in the current experience
    question: Can I switch between learner and admin roles in my current experience?
  phrasing_ops: 4
  slug: canvas-canvas-career-experiences-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Canvas Career User Context API from Canvas — 1 operation(s) for canvas career user context.
  name: Canvas Canvas Career User Context API
  phrasing_intents:
  - id: get_career_user_context
    intent: Get my Career user context
    question: What permissions, enrollment types and admin roles does my user have for Journey?
  phrasing_ops: 1
  slug: canvas-canvas-career-user-context-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Collaborations API from Canvas — 5 operation(s) for collaborations.
  name: Canvas Collaborations API
  phrasing_intents:
  - id: list_collaborations_courses
    intent: List a course's collaborations
    question: What collaborative documents exist in my Canvas course?
  - id: list_collaborations_groups
    intent: List a group's collaborations
    question: Which collaborations has a student group created?
  - id: list_members_of_collaboration
    intent: List members of a collaboration
    question: Who is part of a given collaboration?
  - id: list_potential_members_courses
    intent: List users who could join a course collaboration
    question: Who can I add to a collaboration in my course?
  - id: list_potential_members_groups
    intent: List users who could join a group collaboration
    question: Who is eligible to be added to a group collaboration?
  phrasing_ops: 5
  slug: canvas-collaborations-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Comm Messages API from Canvas — 1 operation(s) for comm messages.
  name: Canvas Comm Messages API
  phrasing_intents:
  - id: list_of_commmessages_for_user
    intent: List notification messages sent to a user
    question: What emails and notifications has Canvas sent to a user?
  phrasing_ops: 1
  slug: canvas-comm-messages-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Communication Channels API from Canvas — 4 operation(s) for communication channels.
  name: Canvas Communication Channels API
  phrasing_intents:
  - id: list_user_communication_channels
    intent: List a user's communication channels
    question: What email addresses and phone numbers can a user be notified at?
  - id: create_communication_channel
    intent: Add a communication channel for a user
    question: How do I add a new email address for a user's notifications?
  - id: delete_communication_channel_id
    intent: Delete a communication channel by ID
    question: How do I remove a user's notification channel when I know its ID?
  - id: delete_communication_channel_type
    intent: Delete a channel by type and address
    question: Can I remove a user's email channel by the address itself?
  - id: delete_push_notification_endpoint
    intent: Remove my push notification endpoint
    question: How do I stop push notifications going to my device?
  phrasing_ops: 5
  slug: canvas-communication-channels-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Conferences API from Canvas — 3 operation(s) for conferences.
  name: Canvas Conferences API
  phrasing_intents:
  - id: list_conferences_courses
    intent: List a course's web conferences
    question: What web conferences are scheduled in my course?
  - id: list_conferences_groups
    intent: List a group's web conferences
    question: What conferences does my student group have?
  - id: list_conferences_for_current_user
    intent: List conferences across all my courses and groups
    question: Which conferences am I part of across every course and group?
  phrasing_ops: 3
  slug: canvas-conferences-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Content Exports API from Canvas — 6 operation(s) for content exports.
  name: Canvas Content Exports API
  phrasing_intents:
  - id: list_content_exports_courses
    intent: List a course's content exports
    question: What content exports have been run for a course?
  - id: export_content_courses
    intent: Export a course's content
    question: How do I export a whole course as a Common Cartridge file?
  - id: list_content_exports_groups
    intent: List a group's content exports
    question: What exports have been run for a group?
  - id: export_content_groups
    intent: Export a group's content
    question: How do I export the files and pages of a group?
  - id: list_content_exports_users
    intent: List a user's content exports
    question: What exports have been made of a user's personal files?
  - id: export_content_users
    intent: Export a user's personal content
    question: How do I export all of a user's personal files as a zip?
  - id: show_content_export_courses
    intent: Get a course export and its download link
    question: Is my course export finished, and where do I download it?
  - id: show_content_export_groups
    intent: Get a group export and its download link
    question: Has my group export completed yet?
  phrasing_ops: 9
  slug: canvas-content-exports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Content Migrations API from Canvas — 25 operation(s) for content migrations.
  name: Canvas Content Migrations API
  phrasing_intents:
  - id: list_migration_issues_accounts
    intent: List issues raised by an account content migration
    question: What problems came up during an import into my Canvas account?
  - id: list_migration_issues_courses
    intent: List issues raised by a course content migration
    question: What went wrong when I imported content into my course?
  - id: list_migration_issues_groups
    intent: List issues raised by a group content migration
    question: Which errors did a content import into a student group produce?
  - id: list_migration_issues_users
    intent: List issues raised by a user content migration
    question: What problems came up importing files into a user's personal space?
  - id: get_migration_issue_accounts
    intent: Get one issue from an account content migration
    question: What are the details of a single issue from an account-level import?
  - id: update_migration_issue_accounts
    intent: Resolve or reopen an account migration issue
    question: How do I mark an issue from an account-level import as resolved?
  - id: get_migration_issue_courses
    intent: Get one issue from a course content migration
    question: What exactly does one error from my course import say?
  - id: update_migration_issue_courses
    intent: Resolve or reopen a course migration issue
    question: How do I mark a course import problem as resolved once I've fixed it?
  phrasing_ops: 37
  slug: canvas-content-migrations-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Content Security Policy Settings API from Canvas — 5 operation(s) for content security policy settings.
  name: Canvas Content Security Policy Settings API
  phrasing_intents:
  - id: get_current_settings_for_account_or_course_courses
    intent: Get a course's content security policy settings
    question: Is the content security policy enabled for my course?
  - id: enable_disable_or_clear_explicit_csp_setting_courses
    intent: Turn a course's CSP on, off or back to inherited
    question: How do I turn off the content security policy for one course?
  - id: get_current_settings_for_account_or_course_accounts
    intent: Get an account's content security policy settings
    question: What CSP settings and allowed domains does my account have?
  - id: enable_disable_or_clear_explicit_csp_setting_accounts
    intent: Turn an account's CSP on, off or back to inherited
    question: How do I enable the content security policy for an account and its sub-accounts?
  - id: lock_or_unlock_current_csp_settings_for_sub_accounts_and_courses
    intent: Lock CSP settings for sub-accounts and courses
    question: Can I stop sub-accounts and courses from changing the CSP setting I chose?
  - id: add_allowed_domain_to_account
    intent: Allow a domain in an account's CSP
    question: How do I whitelist a domain so it can load under the account content security policy?
  - id: remove_domain_from_account
    intent: Remove an allowed domain from an account's CSP
    question: How do I take a domain off my account's CSP allow list?
  - id: add_multiple_allowed_domains_to_account
    intent: Allow several domains in an account's CSP at once
    question: Can I add a whole list of domains to the CSP allow list in one request?
  phrasing_ops: 8
  slug: canvas-content-security-policy-settings-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Content Shares API from Canvas — 6 operation(s) for content shares.
  name: Canvas Content Shares API
  phrasing_intents:
  - id: create_content_share
    intent: Share content directly with other users
    question: How do I share a quiz or page directly with another teacher?
  - id: list_content_shares_sent
    intent: List content shares a user has sent
    question: What content have I shared with other people?
  - id: list_content_shares_received
    intent: List content shares a user has received
    question: What content have other people shared with me?
  - id: get_unread_shares_count
    intent: Count unread received content shares
    question: How many shared items haven't I opened yet?
  - id: get_content_share
    intent: Get a single content share
    question: How do I see the details of one content share?
  - id: remove_content_share
    intent: Remove a content share from my list
    question: How do I remove a shared item from my list?
  - id: update_content_share
    intent: Mark a content share read or unread
    question: How do I mark a shared item as read?
  - id: add_users_to_content_share
    intent: Send an existing content share to more users
    question: How do I send something I already shared to additional people?
  phrasing_ops: 8
  slug: canvas-content-shares-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Conversations API from Canvas — 8 operation(s) for conversations.
  name: Canvas Conversations API
  phrasing_intents:
  - id: list_conversations
    intent: List my inbox conversations
    question: How do I see my Canvas inbox conversations, newest first?
  - id: create_conversation
    intent: Send a new inbox message
    question: How do I send a private message to a student in Canvas?
  - id: batch_update_conversations
    intent: Apply one change to many conversations
    question: How do I mark a bunch of conversations as read at once?
  - id: get_running_batches
    intent: Check my bulk message batches in progress
    question: Is my bulk private message still being sent?
  - id: get_single_conversation
    intent: Read a single conversation
    question: How do I open one conversation with all its messages?
  - id: edit_conversation
    intent: Star, archive or mute a conversation
    question: How do I star or archive one conversation?
  - id: delete_conversation
    intent: Delete a conversation from my inbox
    question: How do I delete a whole conversation from my inbox?
  - id: mark_all_as_read
    intent: Mark all my conversations as read
    question: Can I clear every unread conversation in my inbox at once?
  phrasing_ops: 12
  slug: canvas-conversations-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Course Audit Log API from Canvas — 2 operation(s) for course audit log.
  name: Canvas Course Audit Log API
  phrasing_intents:
  - id: query_by_course
    intent: List change events for a course
    question: Who changed a course's settings, and when?
  - id: query_by_account_course_audit_log
    intent: List course change events across an account
    question: How do I audit course changes across a whole account?
  phrasing_ops: 2
  slug: canvas-course-audit-log-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Course Pace API from Canvas — 2 operation(s) for course pace.
  name: Canvas Course Pace API
  phrasing_intents:
  - id: show_course_pace
    intent: Get a course pace
    question: Can I see the pacing schedule set for a Canvas course?
  - id: update_course_pace
    intent: Update a course pace
    question: Can I move the end date of an existing course pace?
  - id: delete_course_pace
    intent: Delete a course pace
    question: Can I remove a pacing plan from my course?
  - id: create_course_pace
    intent: Create a course pace
    question: How do I set up a pacing schedule for a self-paced course?
  phrasing_ops: 4
  slug: canvas-course-pace-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Course Quiz Extensions API from Canvas — 1 operation(s) for course quiz extensions.
  name: Canvas Course Quiz Extensions API
  phrasing_intents:
  - id: set_extensions_for_student_quiz_submissions
    intent: Give students extra quiz time or attempts
    question: How do I give a student extra time on quizzes in my course?
  phrasing_ops: 1
  slug: canvas-course-quiz-extensions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Course Reports API from Canvas — 2 operation(s) for course reports.
  name: Canvas Course Reports API
  phrasing_intents:
  - id: status_of_report_course_reports
    intent: Check a specific course report's status
    question: Is a particular course report I started ready yet?
  - id: start_report_course_reports
    intent: Run a course report
    question: How do I generate a report for my course?
  - id: status_of_last_report
    intent: Check my most recent course report
    question: What happened to the last course report I ran?
  phrasing_ops: 3
  slug: canvas-course-reports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Custom Gradebook Columns API from Canvas — 6 operation(s) for custom gradebook columns.
  name: Canvas Custom Gradebook Columns API
  phrasing_intents:
  - id: list_custom_gradebook_columns
    intent: List custom gradebook columns
    question: What custom columns have been added to a course gradebook?
  - id: create_custom_gradebook_column
    intent: Add a custom gradebook column
    question: How do I add a notes column to the gradebook?
  - id: update_custom_gradebook_column
    intent: Update a custom gradebook column
    question: Can I rename or hide an existing custom gradebook column?
  - id: delete_custom_gradebook_column
    intent: Delete a custom gradebook column
    question: Does deleting a custom gradebook column also delete the data in it?
  - id: reorder_custom_columns
    intent: Reorder custom gradebook columns
    question: Can I change the order custom columns appear in the gradebook?
  - id: list_entries_for_column
    intent: List entries in a custom column
    question: What has been entered for each student in a custom gradebook column?
  - id: update_column_data
    intent: Set one student's custom column entry
    question: How do I set a note for a single student in a custom column?
  - id: bulk_update_column_data
    intent: Bulk set custom column entries
    question: Can I fill in custom column values for many students in one request?
  phrasing_ops: 8
  slug: canvas-custom-gradebook-columns-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Developer Key Account Bindings API from Canvas — 1 operation(s) for developer key account bindings.
  name: Canvas Developer Key Account Bindings API
  phrasing_intents:
  - id: create_developer_key_account_binding
    intent: Turn a developer key on or off for an account
    question: How do I enable a developer key for a sub-account?
  phrasing_ops: 1
  slug: canvas-developer-key-account-bindings-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Developer Keys API from Canvas — 3 operation(s) for developer keys.
  name: Canvas Developer Keys API
  phrasing_intents:
  - id: list_developer_keys
    intent: List an account's developer keys
    question: What Canvas API developer keys exist in my account?
  - id: create_developer_key
    intent: Create a developer key
    question: How do I create a new API developer key for an integration?
  - id: update_developer_key
    intent: Update a developer key
    question: Can I change the redirect URIs or contact email on an existing developer key?
  - id: delete_developer_key
    intent: Delete a developer key
    question: Can I permanently remove an API developer key we no longer use?
  - id: regenerate_developer_key_secret
    intent: Rotate a developer key's secret
    question: Can I rotate the client secret on a developer key if it leaked?
  phrasing_ops: 5
  slug: canvas-developer-keys-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Discovery Pages API from Canvas — 2 operation(s) for discovery pages.
  name: Canvas Discovery Pages API
  phrasing_intents:
  - id: get_discovery_page
    intent: Get the login discovery page settings
    question: What sign-in buttons does our login discovery page show?
  - id: update_discovery_page
    intent: Replace the login discovery page settings
    question: How do I change which identity providers appear on the login discovery page?
  - id: generate_discovery_page_preview_token
    intent: Get a discovery page preview token
    question: Can I preview a discovery page layout before saving it?
  phrasing_ops: 3
  slug: canvas-discovery-pages-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Discussion Topics API from Canvas — 36 operation(s) for discussion topics.
  name: Canvas Discussion Topics API
  phrasing_intents:
  - id: list_discussion_topics_courses
    intent: List a course's discussion topics
    question: What discussion topics are open in my Canvas course right now?
  - id: create_new_discussion_topic_courses
    intent: Start a new discussion in a course
    question: How do I post a new discussion prompt for my whole class?
  - id: list_discussion_topics_groups
    intent: List a group's discussion topics
    question: Which discussions exist inside my student group's space?
  - id: create_new_discussion_topic_groups
    intent: Start a new discussion in a group
    question: Can students open a new thread just for their project group?
  - id: update_topic_courses
    intent: Edit a course discussion topic
    question: Can I rename or re-lock a class discussion after it's already posted?
  - id: delete_topic_courses
    intent: Delete a course discussion topic
    question: Does deleting a graded class discussion also remove its assignment?
  - id: get_single_topic_courses
    intent: Get one course discussion topic
    question: How can I pull the settings and details of a single course discussion?
  - id: update_topic_groups
    intent: Edit a group discussion topic
    question: Can a group discussion's title or message be changed after posting?
  phrasing_ops: 58
  slug: canvas-discussion-topics-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The E Portfolios API from Canvas — 5 operation(s) for e portfolios.
  name: Canvas E Portfolios API
  phrasing_intents:
  - id: get_all_eportfolios_for_user
    intent: List a user's ePortfolios
    question: What ePortfolios has a student created?
  - id: moderate_all_eportfolios_for_user
    intent: Set spam status on all of a user's ePortfolios
    question: As an admin, can I flag every ePortfolio a user owns as spam in one go?
  - id: get_eportfolio
    intent: Get an ePortfolio
    question: How do I see the details of one ePortfolio?
  - id: delete_eportfolio
    intent: Delete an ePortfolio
    question: How do I delete an ePortfolio?
  - id: get_eportfolio_pages
    intent: List an ePortfolio's pages
    question: What pages does an ePortfolio contain?
  - id: moderate_eportfolio
    intent: Set spam status on one ePortfolio
    question: How do I flag a single ePortfolio as spam?
  - id: restore_deleted_eportfolio
    intent: Restore a deleted ePortfolio
    question: Can an admin undelete an ePortfolio?
  phrasing_ops: 7
  slug: canvas-e-portfolios-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The E Pub Exports API from Canvas — 3 operation(s) for e pub exports.
  name: Canvas E Pub Exports API
  phrasing_intents:
  - id: list_courses_with_their_latest_epub_export
    intent: List my courses with their latest ePub export
    question: Which of my courses already have an ePub export?
  - id: create_epub_export
    intent: Export a course as an ePub
    question: How do I turn a course into an ePub book for offline reading?
  - id: show_epub_export
    intent: Get an ePub export
    question: Is my course's ePub export finished and ready to download?
  phrasing_ops: 3
  slug: canvas-e-pub-exports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Enrollment Terms API from Canvas — 2 operation(s) for enrollment terms.
  name: Canvas Enrollment Terms API
  phrasing_intents:
  - id: create_enrollment_term
    intent: Create an enrollment term
    question: How do I add a new semester as an enrollment term?
  - id: list_enrollment_terms
    intent: List an account's enrollment terms
    question: What terms are set up for my institution in Canvas?
  - id: update_enrollment_term
    intent: Update an enrollment term
    question: How do I change the end date of an existing term?
  - id: delete_enrollment_term
    intent: Delete an enrollment term
    question: How do I delete a term I no longer need?
  - id: retrieve_enrollment_term
    intent: Get one enrollment term
    question: How do I see the dates and overrides for one term?
  phrasing_ops: 5
  slug: canvas-enrollment-terms-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Enrollments API from Canvas — 12 operation(s) for enrollments.
  name: Canvas Enrollments API
  phrasing_intents:
  - id: list_enrollments_courses
    intent: List enrollments in a course
    question: Who is enrolled in my course, students and teachers alike?
  - id: enroll_user_courses
    intent: Enroll a user in a course
    question: How do I add a student to a course?
  - id: list_enrollments_sections
    intent: List enrollments in a section
    question: Who is enrolled in a particular course section?
  - id: enroll_user_sections
    intent: Enroll a user in a section
    question: How do I put a student into a specific section?
  - id: list_enrollments_users
    intent: List a user's enrollments
    question: Which courses is a particular user enrolled in?
  - id: enrollment_by_id
    intent: Get an enrollment by ID
    question: What are the details of one enrollment record?
  - id: enroll_multiple_users_to_one_or_more_courses
    intent: Bulk enroll users across courses
    question: How do I enroll a list of users into several courses at once?
  - id: conclude_deactivate_or_delete_enrollment
    intent: Conclude, deactivate or delete an enrollment
    question: How do I remove a student from a course?
  phrasing_ops: 14
  slug: canvas-enrollments-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Error Reports API from Canvas — 1 operation(s) for error reports.
  name: Canvas Error Reports API
  phrasing_intents:
  - id: create_error_report
    intent: Report a problem
    question: How can a user report a problem the same way as the help menu does?
  phrasing_ops: 1
  slug: canvas-error-reports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The External Tools API from Canvas — 11 operation(s) for external tools.
  name: Canvas External Tools API
  phrasing_intents:
  - id: list_external_tools_courses
    intent: List a course's external tools
    question: Which LTI tools are installed in a particular course?
  - id: create_external_tool_courses
    intent: Install an external tool in a course
    question: How do I add an LTI tool to just one course?
  - id: list_external_tools_accounts
    intent: List an account's external tools
    question: What LTI tools are configured at the account level?
  - id: create_external_tool_accounts
    intent: Install an external tool across an account
    question: How do I make an LTI tool available to every course under an account?
  - id: list_external_tools_groups
    intent: List a group's external tools
    question: Which external tools can a student group use?
  - id: get_sessionless_launch_url_for_external_tool_courses
    intent: Get a sessionless launch link for a course tool
    question: How can I launch an LTI tool in a course without a browser session?
  - id: get_sessionless_launch_url_for_external_tool_accounts
    intent: Get a sessionless launch link for an account tool
    question: Can I get a session-free launch URL for a tool installed on an account?
  - id: get_single_external_tool_courses
    intent: Get one external tool in a course
    question: How do I see the settings of a specific tool installed in a course?
  phrasing_ops: 19
  slug: canvas-external-tools-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Favorites API from Canvas — 4 operation(s) for favorites.
  name: Canvas Favorites API
  phrasing_intents:
  - id: list_favorite_courses
    intent: List my favorite courses
    question: Which courses are starred on my Canvas dashboard?
  - id: reset_course_favorites
    intent: Reset my favorite courses to the default
    question: Can I wipe my course favorites and go back to the automatic enrolled list?
  - id: list_favorite_groups
    intent: List my favorite groups
    question: Which groups have I marked as favorites?
  - id: reset_group_favorites
    intent: Reset my favorite groups to the default
    question: Can I undo all my group favorites in one go?
  - id: add_course_to_favorites
    intent: Add a course to my favorites
    question: How do I pin a course to my dashboard?
  - id: remove_course_from_favorites
    intent: Remove a course from my favorites
    question: Can I unstar an old course so it leaves my dashboard?
  - id: add_group_to_favorites
    intent: Add a group to my favorites
    question: Can I favorite a group so it's easy to find?
  - id: remove_group_from_favorites
    intent: Remove a group from my favorites
    question: How do I unfavorite a group I'm no longer active in?
  phrasing_ops: 8
  slug: canvas-favorites-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Feature Flags API from Canvas — 10 operation(s) for feature flags.
  name: Canvas Feature Flags API
  phrasing_intents:
  - id: list_features_courses
    intent: List features for a course
    question: Which feature options can be toggled for a course?
  - id: list_features_accounts
    intent: List features for an account
    question: What features can an admin enable or disable for an account?
  - id: list_features_users
    intent: List features for a user
    question: Which user-level feature previews can a person opt into?
  - id: list_enabled_features_courses
    intent: List features turned on for a course
    question: Which features are currently switched on in my course?
  - id: list_enabled_features_accounts
    intent: List features turned on for an account
    question: What features are enabled on our account right now?
  - id: list_enabled_features_users
    intent: List features turned on for a user
    question: Which feature previews has a user already enabled?
  - id: list_environment_features
    intent: Get global UI feature settings
    question: What global feature options shape the Canvas user interface?
  - id: get_feature_flag_courses
    intent: Check a feature flag on a course
    question: Is a feature on or off for a course, and is that inherited from the account?
  phrasing_ops: 16
  slug: canvas-feature-flags-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Files API from Canvas — 43 operation(s) for files.
  name: Canvas Files API
  phrasing_intents:
  - id: list_files_courses
    intent: List the files in a course
    question: How do I see every file uploaded to a Canvas course?
  - id: get_quota_information_courses
    intent: Check a course's file storage quota
    question: How much file storage has a course used out of its quota?
  - id: get_quota_information_groups
    intent: Check a group's file storage quota
    question: How much file storage is a student group using?
  - id: get_quota_information_users
    intent: Check a user's personal file storage quota
    question: How much of a user's personal file quota is used?
  - id: list_files_users
    intent: List a user's personal files
    question: How do I list the files in a user's personal files area?
  - id: list_files_groups
    intent: List the files in a group
    question: What files has a student group uploaded?
  - id: list_files_folders
    intent: List the files inside a folder
    question: How do I see just the files inside one specific folder?
  - id: get_public_inline_preview_url
    intent: Get a file's inline preview URL
    question: How do I get the URL used to preview a file inline?
  phrasing_ops: 53
  slug: canvas-files-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Grade Change Log API from Canvas — 5 operation(s) for grade change log.
  name: Canvas Grade Change Log API
  phrasing_intents:
  - id: query_by_assignment
    intent: List grade changes on an assignment
    question: Who changed grades on this assignment, and when?
  - id: query_by_course_grade_change_log
    intent: List grade changes in a course
    question: What grade changes were made across my whole course?
  - id: query_by_student
    intent: List grade changes for a student
    question: Have any of this student's grades been changed?
  - id: query_by_grader
    intent: List grade changes made by a grader
    question: Which grades has a particular teacher or TA changed?
  - id: advanced_query
    intent: Search grade changes by combined filters
    question: Can I find grade changes one grader made for one student in a specific course?
  phrasing_ops: 5
  slug: canvas-grade-change-log-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Gradebook History API from Canvas — 4 operation(s) for gradebook history.
  name: Canvas Gradebook History API
  phrasing_intents:
  - id: days_in_gradebook_history_for_this_course
    intent: List the days grading happened in a course
    question: On which days did anyone change grades in a course?
  - id: details_for_given_date_in_gradebook_history_for_this_course
    intent: See who graded what on a given date
    question: Who graded which assignments on a particular day?
  - id: lists_submissions
    intent: List grade changes by a grader on an assignment
    question: What submission versions did one grader change for an assignment on a specific day?
  - id: list_uncollated_submission_versions
    intent: Get a feed of all submission grade versions
    question: How do I get a flat feed of every graded submission version in a course?
  phrasing_ops: 4
  slug: canvas-gradebook-history-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Grading Period Sets API from Canvas — 2 operation(s) for grading period sets.
  name: Canvas Grading Period Sets API
  phrasing_intents:
  - id: list_grading_period_sets
    intent: List an account's grading period sets
    question: What grading period sets are defined for my account?
  - id: create_grading_period_set
    intent: Create a grading period set
    question: How do I set up a new grading period set for some enrollment terms?
  - id: update_grading_period_set
    intent: Update a grading period set
    question: Can I change which enrollment terms an existing grading period set applies to?
  - id: delete_grading_period_set
    intent: Delete a grading period set
    question: How do I remove a grading period set from an account?
  phrasing_ops: 4
  slug: canvas-grading-period-sets-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Grading Periods API from Canvas — 6 operation(s) for grading periods.
  name: Canvas Grading Periods API
  phrasing_intents:
  - id: list_grading_periods_accounts
    intent: List an account's grading periods
    question: What grading periods are defined at the account level?
  - id: list_grading_periods_courses
    intent: List a course's grading periods
    question: What grading periods apply to my course?
  - id: get_single_grading_period
    intent: Get one grading period in a course
    question: When does a specific grading period start and end?
  - id: update_single_grading_period
    intent: Change one grading period's dates
    question: How do I move the end date of a single grading period?
  - id: delete_grading_period_courses
    intent: Delete a course grading period
    question: How do I remove a grading period from my course?
  - id: delete_grading_period_accounts
    intent: Delete an account grading period
    question: How do I delete a grading period defined for the whole account?
  - id: batch_update_grading_periods_courses
    intent: Update several grading periods in a course
    question: How do I set up all my course's grading periods in one request?
  - id: batch_update_grading_periods_grading_period_sets
    intent: Update several grading periods in a set
    question: How do I edit every period in a grading period set together?
  phrasing_ops: 8
  slug: canvas-grading-periods-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Grading Standards API from Canvas — 4 operation(s) for grading standards.
  name: Canvas Grading Standards API
  phrasing_intents:
  - id: create_new_grading_standard_accounts
    intent: Create an account-wide grading standard
    question: How do I create a letter-grade scheme every course in an account can use?
  - id: list_grading_standards_available_in_context_accounts
    intent: List an account's grading standards
    question: Which grading schemes are available across an account?
  - id: create_new_grading_standard_courses
    intent: Create a course grading standard
    question: How do I make a custom grading scheme just for my course?
  - id: list_grading_standards_available_in_context_courses
    intent: List a course's grading standards
    question: What grading schemes can I pick from in my course?
  - id: get_single_grading_standard_in_context_courses
    intent: Get a grading standard in a course
    question: What are the grade cutoffs in one of my course's grading schemes?
  - id: update_grading_standard_courses
    intent: Update a course grading standard
    question: Can I change the cutoffs of a course grading scheme after it's been used?
  - id: delete_grading_standard_courses
    intent: Delete a course grading standard
    question: How do I remove a grading scheme I created in my course?
  - id: get_single_grading_standard_in_context_accounts
    intent: Get a grading standard in an account
    question: What does an account-level grading scheme look like?
  phrasing_ops: 10
  slug: canvas-grading-standards-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Group Categories API from Canvas — 12 operation(s) for group categories.
  name: Canvas Group Categories API
  phrasing_intents:
  - id: list_group_categories_for_context_accounts
    intent: List group sets in an account
    question: What group categories exist at the account level in Canvas?
  - id: create_group_category_accounts
    intent: Create a group set in an account
    question: How do I set up a new group category across an entire account?
  - id: list_group_categories_for_context_courses
    intent: List group sets in a course
    question: Which group sets has my instructor created in this course?
  - id: create_group_category_courses
    intent: Create a group set in a course
    question: Can I create project groups for my class and have students split automatically?
  - id: get_single_group_category
    intent: Get one group set
    question: Can I look up the settings of a specific group category?
  - id: update_group_category
    intent: Edit a group set's settings
    question: Can I rename a group category or change its member limit later?
  - id: delete_group_category
    intent: Delete a group set and its groups
    question: Does deleting a group category also delete every group inside it?
  - id: bulk_manage_differentiation_tags
    intent: Bulk create, rename or delete differentiation tags
    question: Can I create, rename and delete several differentiation tags in one request?
  phrasing_ops: 16
  slug: canvas-group-categories-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Groups API from Canvas — 17 operation(s) for groups.
  name: Canvas Groups API
  phrasing_intents:
  - id: upload_file_groups
    intent: Start a file upload to a group
    question: How do I upload a file into a student group's files?
  - id: create_group_group_categories
    intent: Create a group inside a group set
    question: How do I add a new group to an existing group set in a course?
  - id: list_your_groups
    intent: List groups I belong to
    question: Which groups am I a member of?
  - id: list_groups_available_in_context_accounts
    intent: List groups in an account
    question: What groups exist across a whole Canvas account?
  - id: list_groups_available_in_context_courses
    intent: List groups in a course
    question: Which student groups have been set up in my course?
  - id: bulk_fetch_user_tags_for_multiple_users_in_course
    intent: Get differentiation tags for many users
    question: Which differentiation tags are assigned to each student in a course?
  - id: get_single_group
    intent: Get a single group
    question: How do I look up one group's details by ID?
  - id: edit_group
    intent: Edit a group's name, settings or members
    question: Can I rename a group or change its description?
  phrasing_ops: 25
  slug: canvas-groups-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The History API from Canvas — 1 operation(s) for history.
  name: Canvas History API
  phrasing_intents:
  - id: list_recent_history_for_user
    intent: List a user's recently viewed items
    question: What pages and assignments did a student visit most recently in Canvas?
  phrasing_ops: 1
  slug: canvas-history-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Inst Access Tokens API from Canvas — 1 operation(s) for inst access tokens.
  name: Canvas Inst Access Tokens API
  phrasing_intents:
  - id: deprecated_create_instaccess_token
    intent: Create a short-lived InstAccess token
    question: How do I get an InstAccess token for calling Instructure services?
  phrasing_ops: 1
  slug: canvas-inst-access-tokens-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Late Policy API from Canvas — 1 operation(s) for late policy.
  name: Canvas Late Policy API
  phrasing_intents:
  - id: get_late_policy
    intent: Get a course's late policy
    question: What late penalty does my course apply?
  - id: create_late_policy
    intent: Create a course late policy
    question: How do I set up an automatic late penalty for a course that has none?
  - id: patch_late_policy
    intent: Change an existing late policy
    question: Can I change the late deduction on a course that already has a policy?
  phrasing_ops: 3
  slug: canvas-late-policy-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Learning Object Dates API from Canvas — 6 operation(s) for learning object dates.
  name: Canvas Learning Object Dates API
  phrasing_intents:
  - id: get_learning_object_s_date_information_modules
    intent: Get date details for a module
    question: What availability dates and overrides apply to a course module?
  - id: get_learning_object_s_date_information_assignments
    intent: Get date details for an assignment
    question: Where can I see an assignment's base dates together with every override?
  - id: update_learning_object_s_date_information_assignments
    intent: Update date details for an assignment
    question: Can I reset an assignment's dates and its overrides together in one request?
  - id: get_learning_object_s_date_information_quizzes
    intent: Get date details for a quiz
    question: When does a quiz open, close and come due, including any exceptions?
  - id: update_learning_object_s_date_information_quizzes
    intent: Update date details for a quiz
    question: Can I move a quiz's open and close times in a single update?
  - id: get_learning_object_s_date_information_discussion_topics
    intent: Get date details for a discussion
    question: What are the due and lock dates on a graded discussion?
  - id: update_learning_object_s_date_information_discussion_topics
    intent: Update date details for a discussion
    question: Can I change when a discussion closes for replies?
  - id: get_learning_object_s_date_information_pages
    intent: Get date details for a wiki page
    question: When does a course page become available to students?
  phrasing_ops: 11
  slug: canvas-learning-object-dates-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Line Items API from Canvas — 2 operation(s) for line items.
  name: Canvas Line Items API
  phrasing_intents:
  - id: create_line_item
    intent: Create an LTI line item
    question: How does an LTI tool add a new gradebook column?
  - id: list_line_items
    intent: List LTI line items in a course
    question: What gradebook columns has my LTI tool created in a course?
  - id: update_line_item
    intent: Update an LTI line item
    question: Can I change the maximum score of an existing line item?
  - id: show_line_item
    intent: Get one LTI line item
    question: How can a tool read back a single line item it created?
  - id: delete_line_item
    intent: Delete an LTI line item
    question: Can an LTI tool remove a gradebook column it created?
  phrasing_ops: 5
  slug: canvas-line-items-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Live Assessments API from Canvas — 2 operation(s) for live assessments.
  name: Canvas Live Assessments API
  phrasing_intents:
  - id: create_live_assessment_results
    intent: Record results for a live assessment
    question: How do I record students' scores from a live, in-class assessment?
  - id: list_live_assessment_results
    intent: List results recorded for a live assessment
    question: What results have been recorded for an in-class live assessment?
  - id: create_or_find_live_assessment
    intent: Create or find a live assessment by key
    question: How do I set up a live assessment aligned to a learning outcome?
  - id: list_live_assessments
    intent: List a course's live assessments
    question: Which live assessments exist in my course?
  phrasing_ops: 4
  slug: canvas-live-assessments-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Logins API from Canvas — 5 operation(s) for logins.
  name: Canvas Logins API
  phrasing_intents:
  - id: list_user_logins_accounts
    intent: List logins in an account
    question: How do I list the login records for an account in Canvas?
  - id: create_user_login
    intent: Create a login for an existing user
    question: How do I add a second login to an existing user in an account?
  - id: list_user_logins_users
    intent: List a user's logins
    question: What usernames does a specific user have?
  - id: kickoff_password_recovery_flow
    intent: Start a password recovery email
    question: How do I send a password reset email to a user?
  - id: edit_user_login
    intent: Edit a user login
    question: Can I change a user's username or password?
  - id: delete_user_login
    intent: Delete a user login
    question: How do I delete one of a user's logins?
  phrasing_ops: 6
  slug: canvas-logins-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Lti Context Controls API from Canvas — 4 operation(s) for lti context controls.
  name: Canvas Lti Context Controls API
  phrasing_intents:
  - id: list_all_context_controls
    intent: List an LTI registration's context controls
    question: Which courses and accounts is an LTI registration turned on or off for?
  - id: show_lti_context_control
    intent: Get one LTI context control
    question: How do I look at a single context control for an LTI registration?
  - id: modify_context_control
    intent: Turn an LTI tool on or off for a context
    question: How do I make an LTI tool unavailable in one course without uninstalling it?
  - id: delete_context_control
    intent: Delete an LTI context control
    question: What happens if I delete the primary context control for a deployment?
  - id: create_lti_context_control
    intent: Create an LTI context control
    question: How do I enable an LTI registration for one specific course?
  - id: bulk_create_lti_context_controls
    intent: Bulk create LTI context controls
    question: Can I create context controls for many courses at once?
  phrasing_ops: 6
  slug: canvas-lti-context-controls-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Lti Launch Definitions API from Canvas — 2 operation(s) for lti launch definitions.
  name: Canvas Lti Launch Definitions API
  phrasing_intents:
  - id: list_lti_launch_definitions_courses
    intent: List LTI launch definitions in a course
    question: Which LTI tools can be launched from a course's navigation?
  - id: list_lti_launch_definitions_accounts
    intent: List LTI launch definitions in an account
    question: What LTI tools are available for launch at the account level?
  phrasing_ops: 2
  slug: canvas-lti-launch-definitions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Lti Registrations API from Canvas — 28 operation(s) for lti registrations.
  name: Canvas Lti Registrations API
  phrasing_intents:
  - id: list_lti_registrations_in_account_lti_registrations
    intent: List LTI registrations in an account
    question: Which LTI registrations are available in my Canvas account, including ones inherited from Site Admin?
  - id: create_lti_registration_lti_registrations
    intent: Create an LTI registration
    question: How do I manually register a new LTI 1.3 tool with its configuration and developer key?
  - id: list_lti_registrations_in_account_apps
    intent: List LTI apps in an account via the apps alias
    question: What LTI apps are installed in an account when I call the apps endpoint instead of lti_registrations?
  - id: create_lti_registration_apps
    intent: Create an LTI app via the apps alias
    question: Can I add a new LTI app to an account through the apps endpoint?
  - id: show_lti_registration_lti_registrations
    intent: Show an LTI registration
    question: How do I see the configuration and account binding of one LTI registration?
  - id: update_lti_registration_lti_registrations
    intent: Update an LTI registration
    question: Can I rename an LTI registration or change its admin nickname?
  - id: delete_lti_registration_lti_registrations
    intent: Delete an LTI registration
    question: How do I remove an LTI registration I created from my account?
  - id: show_lti_registration_apps
    intent: Show an LTI app via the apps alias
    question: Can I look up a single app's configuration through the apps endpoint?
  phrasing_ops: 36
  slug: canvas-lti-registrations-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Lti Resource Links API from Canvas — 3 operation(s) for lti resource links.
  name: Canvas Lti Resource Links API
  phrasing_intents:
  - id: list_lti_resource_links
    intent: List a course's LTI resource links
    question: Which LTI tool links exist in my course, including ones embedded in pages?
  - id: create_lti_resource_link
    intent: Create an LTI resource link in a course
    question: Can I create an LTI resource link manually instead of through deep linking?
  - id: show_lti_resource_link
    intent: Get an LTI resource link
    question: Can I look up an LTI resource link by its resource_link_uuid instead of its id?
  - id: update_lti_resource_link
    intent: Update an LTI resource link
    question: Can changing an LTI resource link's URL break tool launches?
  - id: delete_lti_resource_link
    intent: Delete an LTI resource link
    question: How do I remove an LTI resource link from a course?
  - id: bulk_create_lti_resource_links
    intent: Create up to 100 LTI resource links at once
    question: Can I create many LTI resource links in a course with one request?
  phrasing_ops: 6
  slug: canvas-lti-resource-links-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Media Objects API from Canvas — 10 operation(s) for media objects.
  name: Canvas Media Objects API
  phrasing_intents:
  - id: list_media_tracks_for_media_object_or_attachment_media_objects
    intent: List captions on a media object
    question: What caption or subtitle tracks does a media object have?
  - id: update_media_tracks_media_objects
    intent: Replace caption tracks on a media object
    question: How do I replace all the subtitles on a media object?
  - id: list_media_tracks_for_media_object_or_attachment_media_attachments
    intent: List captions on a media attachment
    question: What caption tracks are attached to an uploaded media file?
  - id: update_media_tracks_media_attachments
    intent: Replace caption tracks on a media attachment
    question: How do I swap out the subtitles on a media attachment?
  - id: list_media_objects_media_objects
    intent: List media objects I created
    question: Which videos and audio recordings have I uploaded?
  - id: list_media_objects_courses_media_objects
    intent: List media objects in a course
    question: What recordings are associated with my course?
  - id: list_media_objects_groups_media_objects
    intent: List media objects in a group
    question: What videos have been added to a student group?
  - id: list_media_objects_media_attachments
    intent: List my media attachments
    question: Which media files have I uploaded as attachments?
  phrasing_ops: 12
  slug: canvas-media-objects-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Moderated Grading API from Canvas — 7 operation(s) for moderated grading.
  name: Canvas Moderated Grading API
  phrasing_intents:
  - id: list_students_selected_for_moderation
    intent: List students picked for moderation
    question: Which students' work has been selected for moderated grading on an assignment?
  - id: select_students_for_moderation
    intent: Add students to the moderation set
    question: How do I choose which students get a second grader on a moderated assignment?
  - id: bulk_select_provisional_grades
    intent: Choose many provisional grades at once
    question: As final grader, can I pick the provisional grades for many students in one go?
  - id: show_provisional_grade_status_for_student
    intent: Check if a student needs provisional grades
    question: Does a student's submission still need provisional grades?
  - id: select_provisional_grade
    intent: Select a provisional grade for a submission
    question: How does the final grader choose which provisional grade a student receives?
  - id: publish_provisional_grades_for_assignment
    intent: Publish selected provisional grades
    question: How do I release moderated grades to students once they are chosen?
  - id: publish_provisional_grades_for_assignment_asynchronous
    intent: Publish provisional grades in the background
    question: For a large class, can moderated grades be published as a background job?
  - id: show_provisional_grade_status_for_student_moderated_grading
    intent: Check provisional status for an anonymous student
    question: With anonymous grading on, can I check if a submission needs provisional grades?
  phrasing_ops: 8
  slug: canvas-moderated-grading-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Modules API from Canvas — 10 operation(s) for modules.
  name: Canvas Modules API
  phrasing_intents:
  - id: list_modules
    intent: List modules in a course
    question: What modules does a course have?
  - id: create_module
    intent: Create a module in a course
    question: How do I add a new module to a course?
  - id: show_module
    intent: Get a single module
    question: What's in one specific module, and is it published?
  - id: update_module
    intent: Update or publish a module
    question: Can I rename a module or change its position?
  - id: delete_module
    intent: Delete a module
    question: Can I delete an entire module from a course?
  - id: re_lock_module_progressions
    intent: Re-lock module progressions
    question: After adding requirements, how do I re-lock students out of a module until they meet them?
  - id: list_module_items
    intent: List items in a module
    question: What pages, assignments and files are inside a module?
  - id: create_module_item
    intent: Add an item to a module
    question: How do I add an assignment or page to a module?
  phrasing_ops: 17
  slug: canvas-modules-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Names And Role API from Canvas — 2 operation(s) for names and role.
  name: Canvas Names And Role API
  phrasing_intents:
  - id: list_course_memberships
    intent: List a course roster for an LTI tool
    question: How does an LTI tool get the names and roles of everyone in a Canvas course?
  - id: list_group_memberships_names_and_role
    intent: List a group roster for an LTI tool
    question: Can my LTI tool pull the active members of a Canvas group?
  phrasing_ops: 2
  slug: canvas-names-and-role-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The New Quiz Items API from Canvas — 3 operation(s) for new quiz items.
  name: Canvas New Quiz Items API
  phrasing_intents:
  - id: get_quiz_item
    intent: Get one question item in a New Quiz
    question: Can I pull the full content and scoring of a single item in a Canvas New Quiz?
  - id: update_quiz_item
    intent: Edit a question item in a New Quiz
    question: Can I change the points or wording of an existing New Quiz question?
  - id: delete_quiz_item
    intent: Delete a question item from a New Quiz
    question: Can I remove one question from a New Quiz without rebuilding it?
  - id: list_quiz_items
    intent: List the question items in a New Quiz
    question: What questions are in my New Quiz right now?
  - id: create_quiz_item
    intent: Add a question item to a New Quiz
    question: How do I add a multiple choice question to a New Quiz through the API?
  - id: get_items_media_upload_url
    intent: Get an upload URL for hot-spot question media
    question: Where do I upload the image for a hot-spot question in a New Quiz?
  phrasing_ops: 6
  slug: canvas-new-quiz-items-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The New Quizzes Accommodations API from Canvas — 2 operation(s) for new quizzes accommodations.
  name: Canvas New Quizzes Accommodations API
  phrasing_intents:
  - id: set_quiz_level_accommodations
    intent: Give a student accommodations on one quiz
    question: How do I give a student extra time on just one New Quiz?
  - id: set_course_level_accommodations
    intent: Give a student accommodations across a course
    question: How do I give a student extra time on every quiz in a course?
  phrasing_ops: 2
  slug: canvas-new-quizzes-accommodations-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The New Quizzes API from Canvas — 2 operation(s) for new quizzes.
  name: Canvas New Quizzes API
  phrasing_intents:
  - id: get_new_quiz
    intent: Get a New Quiz
    question: How do I get the settings of a single New Quiz?
  - id: update_single_quiz
    intent: Update a New Quiz
    question: Can I change a New Quiz's due date or time limit?
  - id: delete_new_quiz
    intent: Delete a New Quiz
    question: How do I delete a quiz built in New Quizzes?
  - id: list_new_quizzes
    intent: List a course's New Quizzes
    question: Which New Quizzes exist in a course?
  - id: create_new_quiz
    intent: Create a New Quiz
    question: How do I create a quiz in New Quizzes for a course?
  phrasing_ops: 5
  slug: canvas-new-quizzes-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The New Quizzes Reports API from Canvas — 1 operation(s) for new quizzes reports.
  name: Canvas New Quizzes Reports API
  phrasing_intents:
  - id: create_quiz_report
    intent: Generate a New Quiz report
    question: Can I export student analysis or item analysis for a New Quiz?
  phrasing_ops: 1
  slug: canvas-new-quizzes-reports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Notice Handlers API from Canvas — 1 operation(s) for notice handlers.
  name: Canvas Notice Handlers API
  phrasing_intents:
  - id: show_notice_handlers
    intent: List an LTI tool's notice handlers
    question: Which platform notices is an LTI tool subscribed to?
  - id: set_notice_handler
    intent: Subscribe or unsubscribe a tool notice handler
    question: How does an LTI tool subscribe to a platform notice type?
  phrasing_ops: 2
  slug: canvas-notice-handlers-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Notification Preferences API from Canvas — 10 operation(s) for notification preferences.
  name: Canvas Notification Preferences API
  phrasing_intents:
  - id: list_preferences_communication_channel_id
    intent: List notification settings for a channel by id
    question: What notification frequencies are set on a user's Canvas email channel?
  - id: list_preferences_type
    intent: List notification settings for a channel by address
    question: Can I look up notification preferences using an email address instead of a channel id?
  - id: list_of_preference_categories
    intent: List notification categories for a channel
    question: What notification categories exist for a user's communication channel?
  - id: get_preference_communication_channel_id
    intent: Get one notification setting by channel id
    question: How often does a user get a specific notification on a given channel id?
  - id: get_preference_type
    intent: Get one notification setting by channel address
    question: Can I check a single notification setting using the channel's email or phone address?
  - id: update_preference_communication_channel_id
    intent: Change one notification setting by channel id
    question: Can I make one notification arrive as a daily digest on my email channel?
  - id: update_preference_type
    intent: Change one notification setting by channel address
    question: Can I update a single notification for my channel using its address rather than id?
  - id: update_preferences_by_category
    intent: Change all notifications in a category
    question: Can I change a whole category of alerts, like all grading notices, at once?
  phrasing_ops: 10
  slug: canvas-notification-preferences-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Originality Reports API from Canvas — 3 operation(s) for originality reports.
  name: Canvas Originality Reports API
  phrasing_intents:
  - id: create_originality_report
    intent: Create an originality report for a submission
    question: How does a plagiarism tool post an originality score back on a student's submission?
  - id: edit_originality_report_submissions
    intent: Update a submission's originality report
    question: How do I change the score on an originality report once scanning finishes?
  - id: show_originality_report_submissions
    intent: Get an originality report for a submission
    question: What originality score did a submission get?
  - id: edit_originality_report_files
    intent: Update the originality report for a file
    question: Can I update an originality report addressed by its file id?
  - id: show_originality_report_files
    intent: Get the originality report for an attached file
    question: What's the originality report for one specific uploaded file?
  phrasing_ops: 5
  slug: canvas-originality-reports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Outcome Groups API from Canvas — 22 operation(s) for outcome groups.
  name: Canvas Outcome Groups API
  phrasing_intents:
  - id: redirect_to_root_outcome_group_for_context_global
    intent: Find the global root outcome group
    question: Where does the global outcome hierarchy start in Canvas?
  - id: redirect_to_root_outcome_group_for_context_accounts
    intent: Find an account's root outcome group
    question: Which outcome group sits at the top of my account's outcome tree?
  - id: redirect_to_root_outcome_group_for_context_courses
    intent: Find a course's root outcome group
    question: What is the top-level outcome group for my course?
  - id: get_all_outcome_groups_for_context_accounts
    intent: List every outcome group in an account
    question: How can I see all outcome groups defined at the account level?
  - id: get_all_outcome_groups_for_context_courses
    intent: List every outcome group in a course
    question: How can I see all outcome groups a course uses?
  - id: get_all_outcome_links_for_context_accounts
    intent: List all outcome links in an account
    question: How do I find every outcome linked anywhere in an account?
  - id: get_all_outcome_links_for_context_courses
    intent: List all outcome links in a course
    question: Which outcomes are linked into my course, across all its groups?
  - id: show_outcome_group_global
    intent: Get a global outcome group
    question: What details are stored on a global outcome group?
  phrasing_ops: 37
  slug: canvas-outcome-groups-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Outcome Imports API from Canvas — 6 operation(s) for outcome imports.
  name: Canvas Outcome Imports API
  phrasing_intents:
  - id: import_outcomes_accounts
    intent: Import outcomes into an account
    question: How do I bulk-import learning outcomes into an account from a CSV?
  - id: import_outcomes_courses
    intent: Import outcomes into a course
    question: How do I import learning outcomes into a single course from a CSV?
  - id: get_outcome_import_status_accounts
    intent: Check an account outcome import's status
    question: Has my account-level outcomes import finished?
  - id: get_outcome_import_status_courses
    intent: Check a course outcome import's status
    question: Has the outcomes import into my course finished or failed?
  - id: get_ids_of_outcome_groups_created_after_successful_import_accounts
    intent: List outcome groups an account import created
    question: Which outcome groups were created by an account's outcome import?
  - id: get_ids_of_outcome_groups_created_after_successful_import_courses
    intent: List outcome groups a course import created
    question: Which outcome groups did my course's outcome import create?
  phrasing_ops: 6
  slug: canvas-outcome-imports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Outcome Results API from Canvas — 6 operation(s) for outcome results.
  name: Canvas Outcome Results API
  phrasing_intents:
  - id: get_outcome_results
    intent: Get learning outcome results for students
    question: How did each student score against the learning outcomes in my course?
  - id: set_outcome_ordering_for_lmgb
    intent: Save outcome column order in the mastery gradebook
    question: How do I save the order of outcome columns in the Learning Mastery Gradebook?
  - id: get_outcome_result_rollups
    intent: Get rolled-up outcome scores per student
    question: What's each student's overall mastery score per outcome in my course?
  - id: get_contributing_scores
    intent: Get the scores behind one outcome result
    question: Which assignment and quiz scores fed into a student's outcome score?
  - id: get_mastery_distribution
    intent: Get the distribution of students across mastery levels
    question: How many students fall into each mastery level for every outcome?
  - id: enqueue_delayed_outcome_rollup_calculation_job
    intent: Queue a recalculation of outcome rollups
    question: How do I trigger a recalculation of outcome rollups for a course?
  phrasing_ops: 6
  slug: canvas-outcome-results-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Outcomes API from Canvas — 2 operation(s) for outcomes.
  name: Canvas Outcomes API
  phrasing_intents:
  - id: show_outcome
    intent: Get a learning outcome
    question: What are the mastery points and rating scale for a Canvas learning outcome?
  - id: update_outcome
    intent: Update a learning outcome
    question: Can I change the mastery threshold or calculation method of an outcome?
  - id: get_outcome_alignments_for_student_or_assignment
    intent: Get outcome alignments for a student or assignment
    question: Which outcomes is a given assignment aligned to in my course?
  phrasing_ops: 3
  slug: canvas-outcomes-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Pages API from Canvas — 13 operation(s) for pages.
  name: Canvas Pages API
  phrasing_intents:
  - id: show_front_page_courses
    intent: Show a course's front page
    question: How do I get the content of a Canvas course's front page?
  - id: update_create_front_page_courses
    intent: Update or create a course's front page
    question: Can I change the title or body of my course's front page?
  - id: show_front_page_groups
    intent: Show a group's front page
    question: How do I read the front page of a student group?
  - id: update_create_front_page_groups
    intent: Update or create a group's front page
    question: Can I edit the front page of a group's wiki?
  - id: duplicate_page
    intent: Duplicate a course wiki page
    question: How do I make a copy of an existing wiki page in a course?
  - id: list_pages_courses
    intent: List a course's wiki pages
    question: How do I list all the wiki pages in a course?
  - id: create_page_courses
    intent: Create a wiki page in a course
    question: How do I add a new content page to my course?
  - id: list_pages_groups
    intent: List a group's wiki pages
    question: What wiki pages exist in a student group?
  phrasing_ops: 23
  slug: canvas-pages-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Peer Reviews API from Canvas — 5 operation(s) for peer reviews.
  name: Canvas Peer Reviews API
  phrasing_intents:
  - id: get_all_peer_reviews_courses_peer_reviews
    intent: List peer reviews for a course assignment
    question: Who is reviewing whom on an assignment in my Canvas course?
  - id: get_all_peer_reviews_sections_peer_reviews
    intent: List peer reviews for an assignment in a section
    question: Can I see peer review pairings for just one section of my class?
  - id: get_all_peer_reviews_courses_submissions
    intent: List peer reviews of one submission in a course
    question: Who has been assigned to review a particular student's submission?
  - id: create_peer_review_courses
    intent: Assign a peer reviewer to a course submission
    question: Can I manually assign a classmate to peer review a specific submission?
  - id: delete_peer_review_courses
    intent: Remove a peer reviewer from a course submission
    question: Can I take a reviewer off a student's submission in my course?
  - id: get_all_peer_reviews_sections_submissions
    intent: List peer reviews of one submission in a section
    question: Within a section, who is reviewing a given student's submission?
  - id: create_peer_review_sections
    intent: Assign a peer reviewer to a submission in a section
    question: Can I pair reviewers through a section rather than the whole course?
  - id: delete_peer_review_sections
    intent: Remove a peer reviewer from a submission in a section
    question: Can I unassign a reviewer through the section endpoint?
  phrasing_ops: 9
  slug: canvas-peer-reviews-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Plagiarism Detection Platform Assignments API from Canvas — 1 operation(s) for plagiarism detection platform assignments.
  name: Canvas Plagiarism Detection Platform Assignments API
  phrasing_intents:
  - id: get_single_assignment_lti
    intent: Get an assignment as a plagiarism tool
    question: How does a plagiarism detection tool fetch an assignment it's attached to?
  phrasing_ops: 1
  slug: canvas-plagiarism-detection-platform-assignments-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Plagiarism Detection Platform Users API from Canvas — 2 operation(s) for plagiarism detection platform users.
  name: Canvas Plagiarism Detection Platform Users API
  phrasing_intents:
  - id: get_single_user_lti
    intent: Get a user as a plagiarism detection tool
    question: Can a plagiarism tool look up a student by their LTI id?
  - id: get_all_users_in_group_lti
    intent: List a group's users as an LTI tool
    question: Can my LTI tool list everyone in a student group?
  phrasing_ops: 2
  slug: canvas-plagiarism-detection-platform-users-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Plagiarism Detection Submissions API from Canvas — 2 operation(s) for plagiarism detection submissions.
  name: Canvas Plagiarism Detection Submissions API
  phrasing_intents:
  - id: get_single_submission
    intent: Get a submission for plagiarism review
    question: How does a plagiarism tool fetch a student's submission for checking?
  - id: get_history_of_single_submission
    intent: Get every attempt of a submission
    question: Can a plagiarism tool see every attempt a student made on a submission?
  phrasing_ops: 2
  slug: canvas-plagiarism-detection-submissions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Planner API from Canvas — 6 operation(s) for planner.
  name: Canvas Planner API
  phrasing_intents:
  - id: list_planner_items_planner
    intent: List my planner items
    question: What assignments and to-dos are on my Canvas planner this week?
  - id: list_planner_items_users
    intent: List a specific user's planner items
    question: As an observer, how do I see a student's planner items?
  - id: list_planner_notes
    intent: List my planner notes
    question: Which personal to-do notes have I added to my planner?
  - id: create_planner_note
    intent: Create a planner note
    question: How do I add a personal to-do to my planner?
  - id: show_planner_note
    intent: Show a planner note
    question: How do I read one of my planner notes by its id?
  - id: update_planner_note
    intent: Update a planner note
    question: Can I move a planner note to a different day?
  - id: delete_planner_note
    intent: Delete a planner note
    question: How do I delete a to-do note from my planner?
  - id: list_planner_overrides
    intent: List my planner overrides
    question: Which planner items have I marked complete or dismissed?
  phrasing_ops: 12
  slug: canvas-planner-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Poll Choices API from Canvas — 2 operation(s) for poll choices.
  name: Canvas Poll Choices API
  phrasing_intents:
  - id: list_poll_choices_in_poll
    intent: List the choices in a poll
    question: What answer options does a Canvas poll have?
  - id: create_single_poll_choice
    intent: Add a choice to a poll
    question: How do I add an answer option to a poll?
  - id: get_single_poll_choice
    intent: Get one poll choice
    question: How do I fetch a single choice from a poll?
  - id: update_single_poll_choice
    intent: Update a poll choice
    question: Can I change the wording of an existing poll choice?
  - id: delete_poll_choice
    intent: Delete a poll choice
    question: How do I remove an answer option from a poll?
  phrasing_ops: 5
  slug: canvas-poll-choices-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Poll Sessions API from Canvas — 6 operation(s) for poll sessions.
  name: Canvas Poll Sessions API
  phrasing_intents:
  - id: list_poll_sessions_for_poll
    intent: List sessions of a poll
    question: How many times has this poll been run in class?
  - id: create_single_poll_session
    intent: Start a new session of a poll for a course
    question: How do I run a poll for a specific course or section?
  - id: get_results_for_single_poll_session
    intent: Get results of a poll session
    question: What did students answer in a particular poll session?
  - id: update_single_poll_session
    intent: Update a poll session
    question: How do I change which section a poll session is for?
  - id: delete_poll_session
    intent: Delete a poll session
    question: How do I delete a poll session I ran by mistake?
  - id: open_poll_session
    intent: Open a poll session for responses
    question: How do I start accepting answers in a poll session?
  - id: close_opened_poll_session
    intent: Close an open poll session
    question: How do I stop students from answering a poll that's still open?
  - id: list_opened_poll_sessions
    intent: List poll sessions that are open
    question: Which polls are open for me to answer right now?
  phrasing_ops: 9
  slug: canvas-poll-sessions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Poll Submissions API from Canvas — 2 operation(s) for poll submissions.
  name: Canvas Poll Submissions API
  phrasing_intents:
  - id: get_single_poll_submission
    intent: Get one poll submission
    question: How do I see which choice a student picked in a poll session?
  - id: create_single_poll_submission
    intent: Submit a poll response
    question: How does a student answer a live poll?
  phrasing_ops: 2
  slug: canvas-poll-submissions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Polls API from Canvas — 2 operation(s) for polls.
  name: Canvas Polls API
  phrasing_intents:
  - id: list_polls
    intent: List my polls
    question: What polls have I created?
  - id: create_single_poll
    intent: Create a poll
    question: How do I create a new poll with a question?
  - id: get_single_poll
    intent: Get a single poll
    question: What does one of my polls ask?
  - id: update_single_poll
    intent: Update a poll's question
    question: Can I change the question of a poll I already made?
  - id: delete_poll
    intent: Delete a poll
    question: Is there a way to delete a poll I no longer need?
  phrasing_ops: 5
  slug: canvas-polls-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Portfolio Notifications API from Canvas — 1 operation(s) for portfolio notifications.
  name: Canvas Portfolio Notifications API
  phrasing_intents:
  - id: create_portfolio_notification
    intent: Send a portfolio notification to a user
    question: How do I notify a user about a portfolio event?
  phrasing_ops: 1
  slug: canvas-portfolio-notifications-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Proficiency Ratings API from Canvas — 2 operation(s) for proficiency ratings.
  name: Canvas Proficiency Ratings API
  phrasing_intents:
  - id: create_update_proficiency_ratings_accounts
    intent: Set an account's mastery scale
    question: How do I define the proficiency levels used for outcomes across an account?
  - id: get_proficiency_ratings_accounts
    intent: Get an account's mastery scale
    question: What proficiency ratings does my account use for outcomes?
  - id: create_update_proficiency_ratings_courses
    intent: Set a course's mastery scale
    question: Can a course have its own proficiency ratings separate from the account?
  - id: get_proficiency_ratings_courses
    intent: Get a course's mastery scale
    question: Which proficiency ratings apply to outcomes in my course?
  phrasing_ops: 4
  slug: canvas-proficiency-ratings-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Progress API from Canvas — 3 operation(s) for progress.
  name: Canvas Progress API
  phrasing_intents:
  - id: query_progress
    intent: Check a background job's progress
    question: How do I check whether an asynchronous Canvas job has finished?
  - id: cancel_progress
    intent: Cancel a background job
    question: How do I cancel a long-running asynchronous job?
  - id: query_progress_progress
    intent: Check an LTI job's progress in a course
    question: How does an LTI tool check the progress of a job it started in a course?
  phrasing_ops: 3
  slug: canvas-progress-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Public Jwk API from Canvas — 1 operation(s) for public jwk.
  name: Canvas Public Jwk API
  phrasing_intents:
  - id: update_public_jwk
    intent: Rotate an LTI developer key's public JWK
    question: How do I rotate the public key my LTI tool uses for services?
  phrasing_ops: 1
  slug: canvas-public-jwk-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Assignment Overrides API from Canvas — 2 operation(s) for quiz assignment overrides.
  name: Canvas Quiz Assignment Overrides API
  phrasing_intents:
  - id: retrieve_assignment_overridden_dates_for_classic_quizzes
    intent: Get overridden due dates for Classic Quizzes
    question: What are my actual due and unlock dates for Classic Quizzes after overrides apply?
  - id: retrieve_assignment_overridden_dates_for_new_quizzes
    intent: Get overridden due dates for New Quizzes
    question: What due, unlock and available dates apply to me for New Quizzes after overrides?
  phrasing_ops: 2
  slug: canvas-quiz-assignment-overrides-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Extensions API from Canvas — 1 operation(s) for quiz extensions.
  name: Canvas Quiz Extensions API
  phrasing_intents:
  - id: set_extensions_for_student_quiz_submissions_quiz_extensions
    intent: Give a student extra quiz time or attempts
    question: How do I give a student extra time on a quiz?
  phrasing_ops: 1
  slug: canvas-quiz-extensions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Ip Filters API from Canvas — 1 operation(s) for quiz ip filters.
  name: Canvas Quiz Ip Filters API
  phrasing_intents:
  - id: get_available_quiz_ip_filters
    intent: List IP filters available to a quiz
    question: Which IP address filters can I apply to restrict where a quiz is taken?
  phrasing_ops: 1
  slug: canvas-quiz-ip-filters-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Question Groups API from Canvas — 3 operation(s) for quiz question groups.
  name: Canvas Quiz Question Groups API
  phrasing_intents:
  - id: list_question_groups_in_quiz
    intent: List a quiz's question groups
    question: Which question groups make up a quiz?
  - id: create_question_group
    intent: Create a quiz question group
    question: How do I make a quiz pick a random number of questions from a group?
  - id: get_single_quiz_group
    intent: Get one quiz question group
    question: How many questions does a particular quiz group pick, and for how many points?
  - id: update_question_group
    intent: Update a quiz question group
    question: Can I change how many questions a quiz group picks?
  - id: delete_question_group
    intent: Delete a quiz question group
    question: Can I remove a question group from a quiz?
  - id: reorder_question_groups
    intent: Reorder questions within a quiz group
    question: How do I change the order of questions inside a question group?
  phrasing_ops: 6
  slug: canvas-quiz-question-groups-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Questions API from Canvas — 2 operation(s) for quiz questions.
  name: Canvas Quiz Questions API
  phrasing_intents:
  - id: list_questions_in_quiz_or_submission
    intent: List the questions in a classic quiz
    question: What questions are in a classic Canvas quiz?
  - id: create_single_quiz_question
    intent: Add a question to a classic quiz
    question: How do I add a new question to an existing classic quiz?
  - id: get_single_quiz_question
    intent: Get one classic quiz question
    question: Can I fetch a single quiz question with its answers?
  - id: update_existing_quiz_question
    intent: Edit a classic quiz question
    question: Can I fix a typo in a quiz question that's already published?
  - id: delete_quiz_question
    intent: Delete a classic quiz question
    question: Can I remove a question from a classic quiz?
  phrasing_ops: 5
  slug: canvas-quiz-questions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Reports API from Canvas — 2 operation(s) for quiz reports.
  name: Canvas Quiz Reports API
  phrasing_intents:
  - id: retrieve_all_quiz_reports
    intent: List a quiz's reports
    question: What reports are available for a classic quiz?
  - id: create_quiz_report_quiz_reports
    intent: Generate a quiz report
    question: How do I generate a new statistics report for a classic quiz?
  - id: get_quiz_report
    intent: Get one quiz report
    question: How do I fetch the data of a quiz report I already generated?
  - id: abort_generation_of_report_or_remove_previously_generated_one
    intent: Cancel or remove a quiz report
    question: Can I stop a quiz report that's still generating?
  phrasing_ops: 4
  slug: canvas-quiz-reports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Statistics API from Canvas — 1 operation(s) for quiz statistics.
  name: Canvas Quiz Statistics API
  phrasing_intents:
  - id: fetching_latest_quiz_statistics
    intent: Get statistics for a quiz
    question: How did my students do on a quiz overall and per question?
  phrasing_ops: 1
  slug: canvas-quiz-statistics-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Submission Events API from Canvas — 1 operation(s) for quiz submission events.
  name: Canvas Quiz Submission Events API
  phrasing_intents:
  - id: submit_captured_events
    intent: Record events from a quiz session
    question: How do I send the events captured during a quiz-taking session?
  - id: retrieve_captured_events
    intent: Get events captured during a quiz attempt
    question: What did a student do while taking a quiz, like page blurs or answer changes?
  phrasing_ops: 2
  slug: canvas-quiz-submission-events-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Submission Files API from Canvas — 1 operation(s) for quiz submission files.
  name: Canvas Quiz Submission Files API
  phrasing_intents:
  - id: upload_file_quiz_submission_files
    intent: Upload a file for my quiz submission
    question: How do I attach a file to my answer on a quiz file-upload question?
  phrasing_ops: 1
  slug: canvas-quiz-submission-files-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Submission Questions API from Canvas — 4 operation(s) for quiz submission questions.
  name: Canvas Quiz Submission Questions API
  phrasing_intents:
  - id: get_all_quiz_submission_questions
    intent: List the questions in a quiz submission
    question: How do I see every question record in a student's quiz attempt?
  - id: answering_questions
    intent: Answer questions in a quiz submission
    question: How do I submit or change answers for questions in a quiz attempt?
  - id: get_formatted_student_numerical_answer
    intent: Format a student's numerical answer
    question: How will Canvas format a number a student types into a numerical question?
  - id: flagging_question
    intent: Flag a quiz question to revisit
    question: How do I flag a quiz question so I can come back to it later?
  - id: unflagging_question
    intent: Remove the flag from a quiz question
    question: How do I unflag a quiz question after returning to it?
  phrasing_ops: 5
  slug: canvas-quiz-submission-questions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Submission User List API from Canvas — 1 operation(s) for quiz submission user list.
  name: Canvas Quiz Submission User List API
  phrasing_intents:
  - id: send_message_to_unsubmitted_or_submitted_users_for_quiz
    intent: Message students who have or haven't taken a quiz
    question: Can I remind everyone who hasn't taken a quiz yet with one message?
  phrasing_ops: 1
  slug: canvas-quiz-submission-user-list-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quiz Submissions API from Canvas — 5 operation(s) for quiz submissions.
  name: Canvas Quiz Submissions API
  phrasing_intents:
  - id: get_all_quiz_submissions
    intent: List all submissions for a quiz
    question: Who has taken a particular quiz in my course?
  - id: create_quiz_submission_start_quiz_taking_session
    intent: Start taking a quiz
    question: How does a student start a quiz attempt through the API?
  - id: get_quiz_submission
    intent: Get my own submission for a quiz
    question: What's my current submission on a quiz I'm taking?
  - id: get_single_quiz_submission
    intent: Get a quiz submission by id
    question: How do I look up one specific quiz submission by its id?
  - id: update_student_question_scores_and_comments
    intent: Adjust question scores and comments on a quiz attempt
    question: How do I change the points a student got on individual quiz questions?
  - id: complete_quiz_submission_turn_it_in
    intent: Turn in a quiz attempt
    question: How do I submit a quiz attempt for grading when I'm done?
  - id: get_current_quiz_submission_times
    intent: Check time left on a quiz attempt
    question: How much time is left on a timed quiz attempt?
  phrasing_ops: 7
  slug: canvas-quiz-submissions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Quizzes API from Canvas — 4 operation(s) for quizzes.
  name: Canvas Quizzes API
  phrasing_intents:
  - id: list_quizzes_in_course
    intent: List the quizzes in a course
    question: How do I see every classic quiz in a course?
  - id: create_quiz
    intent: Create a quiz in a course
    question: How do I create a new quiz in a Canvas course?
  - id: get_single_quiz
    intent: Get a single quiz
    question: How do I see the settings of one quiz?
  - id: edit_quiz
    intent: Edit an existing quiz
    question: How do I change the settings of a quiz that already exists?
  - id: delete_quiz
    intent: Delete a quiz
    question: How do I delete a quiz from a course?
  - id: reorder_quiz_items
    intent: Reorder questions in a quiz
    question: How do I change the order of questions in a quiz?
  - id: validate_quiz_access_code
    intent: Check a quiz access code
    question: How do I check whether an access code for a quiz is correct?
  phrasing_ops: 7
  slug: canvas-quizzes-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Result API from Canvas — 2 operation(s) for result.
  name: Canvas Result API
  phrasing_intents:
  - id: show_collection_of_results
    intent: List scores recorded for an LTI line item
    question: How can an LTI tool read back all the scores recorded on a gradebook line item?
  - id: show_result
    intent: Get one result on an LTI line item
    question: Can I fetch a single result record by its id from a line item?
  phrasing_ops: 2
  slug: canvas-result-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Roles API from Canvas — 6 operation(s) for roles.
  name: Canvas Roles API
  phrasing_intents:
  - id: list_roles
    intent: List an account's roles
    question: Which custom and built-in roles exist in my account?
  - id: create_new_role
    intent: Create a custom role
    question: How do I create a custom course-level role like Grader?
  - id: get_single_role
    intent: Get one role and its permissions
    question: What permissions does a particular role have?
  - id: deactivate_role
    intent: Deactivate a custom role
    question: What happens to users who already hold a role I deactivate?
  - id: update_role
    intent: Update a role's permissions
    question: Can I change the permissions on the built-in Teacher role?
  - id: activate_role
    intent: Reactivate an inactive role
    question: Can I bring back a role I previously deactivated?
  - id: list_assignable_permissions
    intent: List permissions that roles can be granted
    question: Which permissions can I grant to roles in my account?
  - id: get_help_text_for_permissions
    intent: Explain what a permission does
    question: What does a specific Canvas permission actually allow?
  phrasing_ops: 9
  slug: canvas-roles-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Rubrics API from Canvas — 15 operation(s) for rubrics.
  name: Canvas Rubrics API
  phrasing_intents:
  - id: create_single_rubric
    intent: Create a rubric in a course
    question: How do I build a new grading rubric with criteria in a course?
  - id: list_rubrics_courses
    intent: List a course's active rubrics
    question: What rubrics are active in my Canvas course?
  - id: update_single_rubric
    intent: Update a course rubric
    question: How do I rename a rubric or change its criteria in a course?
  - id: delete_single
    intent: Delete a rubric and its associations
    question: What happens to assignments using a rubric when I delete it?
  - id: get_single_rubric_courses
    intent: Get a rubric from a course
    question: How can I view one rubric's criteria and ratings in a course?
  - id: list_rubrics_accounts
    intent: List an account's active rubrics
    question: Which rubrics are shared at the account level for reuse across courses?
  - id: get_single_rubric_accounts
    intent: Get a rubric from an account
    question: How do I view one account-level rubric's details?
  - id: get_courses_and_assignments_for_rubric_courses
    intent: See where a course rubric is used
    question: Which assignments are using a particular rubric from my course?
  phrasing_ops: 20
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
  phrasing_intents:
  - id: create_score
    intent: Post an LTI score for a student
    question: How does an LTI tool send a student's score back to the Canvas gradebook?
  phrasing_ops: 1
  slug: canvas-score-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Search API from Canvas — 3 operation(s) for search.
  name: Canvas Search API
  phrasing_intents:
  - id: find_recipients_conversations
    intent: Find message recipients (deprecated conversations path)
    question: Is the old conversations find_recipients endpoint still usable for looking up who I can message?
  - id: find_recipients_search
    intent: Find people, courses and groups I can message
    question: Who can I send a message to whose name starts with a few letters?
  - id: list_all_courses
    intent: Browse courses in the public course index
    question: Which courses are listed in the public course index?
  phrasing_ops: 3
  slug: canvas-search-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Sections API from Canvas — 6 operation(s) for sections.
  name: Canvas Sections API
  phrasing_intents:
  - id: list_course_sections
    intent: List a course's sections
    question: What sections does my Canvas course have?
  - id: create_course_section
    intent: Create a section in a course
    question: How do I add a new section to a course?
  - id: cross_list_section
    intent: Cross-list a section into another course
    question: How do I move a section into a different course?
  - id: de_cross_list_section
    intent: Undo cross-listing of a section
    question: How do I send a cross-listed section back to its original course?
  - id: edit_section
    intent: Edit a section
    question: Can I rename a section or change its dates?
  - id: get_section_information_sections
    intent: Get a section by its id
    question: How do I look up a section when I only know its section id?
  - id: delete_section
    intent: Delete a section
    question: How do I delete a section from a course?
  - id: get_section_information_courses
    intent: Get a section within a specific course
    question: How do I get one section's details scoped to its course?
  phrasing_ops: 9
  slug: canvas-sections-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Services API from Canvas — 2 operation(s) for services.
  name: Canvas Services API
  phrasing_intents:
  - id: get_kaltura_config
    intent: Get the Kaltura plugin configuration
    question: Is Kaltura media enabled on this Canvas instance?
  - id: start_kaltura_session
    intent: Start a Kaltura upload session
    question: How do I start a Kaltura session so I can record and upload media?
  phrasing_ops: 2
  slug: canvas-services-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Shared Brand Configs API from Canvas — 3 operation(s) for shared brand configs.
  name: Canvas Shared Brand Configs API
  phrasing_intents:
  - id: share_brandconfig_theme
    intent: Share a theme with the account
    question: How do I save a custom theme so other admins in my account can use it?
  - id: update_shared_theme
    intent: Rename or repoint a shared theme
    question: How do I rename a theme that's already shared?
  - id: un_share_brandconfig_theme
    intent: Stop sharing a theme
    question: How do I remove a shared theme so nobody can pick it anymore?
  phrasing_ops: 3
  slug: canvas-shared-brand-configs-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Sis Import Errors API from Canvas — 2 operation(s) for sis import errors.
  name: Canvas Sis Import Errors API
  phrasing_intents:
  - id: get_sis_import_error_list_sis_imports
    intent: List errors from one SIS import
    question: What went wrong in a specific SIS import?
  - id: get_sis_import_error_list_sis_import_errors
    intent: List all recent SIS import errors for an account
    question: How do I see every SIS import error on an account from the last 30 days?
  phrasing_ops: 2
  slug: canvas-sis-import-errors-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Sis Imports API from Canvas — 6 operation(s) for sis imports.
  name: Canvas Sis Imports API
  phrasing_intents:
  - id: get_sis_import_list
    intent: List SIS imports for an account
    question: Which SIS imports have run on my root account?
  - id: import_sis_data
    intent: Import SIS data into Canvas
    question: How do I upload a SIS CSV file to sync users and enrollments?
  - id: get_current_importing_sis_import
    intent: Show SIS imports currently running
    question: Is a SIS import running on my account right now?
  - id: get_sis_import_status
    intent: Get a SIS import's status
    question: Did my SIS import finish, and were there errors?
  - id: restore_workflow_states_of_sis_imported_items
    intent: Roll back states changed by a SIS import
    question: Can I undo the deletions a bad SIS import made?
  - id: abort_sis_import
    intent: Abort a SIS import
    question: How do I stop a SIS import that's still running?
  - id: abort_all_pending_sis_imports
    intent: Abort all pending SIS imports
    question: Can I cancel every queued SIS import at once?
  phrasing_ops: 7
  slug: canvas-sis-imports-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Sis Integration API from Canvas — 3 operation(s) for sis integration.
  name: Canvas Sis Integration API
  phrasing_intents:
  - id: retrieve_assignments_enabled_for_grade_export_to_sis_accounts
    intent: List an account's SIS-export assignments
    question: Which published assignments across an account are flagged to send grades to the SIS?
  - id: retrieve_assignments_enabled_for_grade_export_to_sis_courses
    intent: List a course's SIS-export assignments
    question: Which assignments in a single course will post grades to the SIS?
  - id: disable_assignments_currently_enabled_for_grade_export_to_sis
    intent: Turn off SIS grade export for a course
    question: How do I stop every assignment in a course from posting grades to the SIS?
  phrasing_ops: 3
  slug: canvas-sis-integration-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Smart Search API from Canvas — 1 operation(s) for smart search.
  name: Canvas Smart Search API
  phrasing_intents:
  - id: search_course_content
    intent: Search course content by meaning
    question: Where in my course is a topic covered, even if the exact words differ?
  phrasing_ops: 1
  slug: canvas-smart-search-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Study Assist API from Canvas — 1 operation(s) for study assist.
  name: Canvas Study Assist API
  phrasing_intents:
  - id: request_study_assist_response
    intent: Ask the course study assistant a question
    question: Can I ask an AI study helper a question about my course material?
  phrasing_ops: 1
  slug: canvas-study-assist-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Submission Comments API from Canvas — 3 operation(s) for submission comments.
  name: Canvas Submission Comments API
  phrasing_intents:
  - id: edit_submission_comment
    intent: Edit a comment on a submission
    question: Can I fix a typo in feedback I left on a student's submission?
  - id: delete_submission_comment
    intent: Delete a comment on a submission
    question: How do I remove a comment I posted on a student's submission?
  - id: upload_file_submission_comments
    intent: Upload a file to attach to a submission comment
    question: How do I attach a marked-up file to my feedback on a submission?
  - id: send_annotation_notification
    intent: Notify users about a new submission annotation
    question: How do I notify a student and their observers that someone annotated their submission?
  phrasing_ops: 4
  slug: canvas-submission-comments-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Submissions API from Canvas — 32 operation(s) for submissions.
  name: Canvas Submissions API
  phrasing_intents:
  - id: submit_assignment_courses
    intent: Submit a course assignment as a student
    question: How do I turn in homework for a course assignment through the API?
  - id: list_assignment_submissions_courses
    intent: List all submissions for a course assignment
    question: Which students have turned in a given assignment in my Canvas course?
  - id: submit_assignment_sections
    intent: Submit an assignment through a course section
    question: Can a student submit an assignment through their section rather than the course?
  - id: list_assignment_submissions_sections
    intent: List a section's submissions for an assignment
    question: Which students in one section have turned in a particular assignment?
  - id: list_submissions_for_multiple_assignments_courses
    intent: List course submissions across students and assignments
    question: Can I fetch submissions for several students and several assignments at once in a course?
  - id: list_submissions_for_multiple_assignments_sections
    intent: List section submissions across students and assignments
    question: Can I pull submissions for many students and assignments within just one section?
  - id: get_single_submission_courses
    intent: Get one student's submission for a course assignment
    question: How can I see a specific student's submission on a course assignment?
  - id: grade_or_comment_on_submission_courses
    intent: Grade or comment on a student's course submission
    question: How do I post a grade for one student's submission in a course?
  phrasing_ops: 46
  slug: canvas-submissions-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Tabs API from Canvas — 5 operation(s) for tabs.
  name: Canvas Tabs API
  phrasing_intents:
  - id: list_available_tabs_for_course_or_group_accounts
    intent: List navigation tabs for an account
    question: Which navigation links appear in an account's admin menu?
  - id: list_available_tabs_for_course_or_group_courses
    intent: List navigation tabs for a course
    question: Which items are in my course's left-hand navigation menu?
  - id: list_available_tabs_for_course_or_group_groups
    intent: List navigation tabs for a group
    question: What navigation tabs does a student group have?
  - id: list_available_tabs_for_course_or_group_users
    intent: List navigation tabs for a user
    question: What tabs show up in a user's profile navigation?
  - id: update_tab_for_course
    intent: Hide or reorder a course navigation tab
    question: How do I hide a tab like Discussions from my course navigation?
  phrasing_ops: 5
  slug: canvas-tabs-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Temporary Enrollment Pairings API from Canvas — 3 operation(s) for temporary enrollment pairings.
  name: Canvas Temporary Enrollment Pairings API
  phrasing_intents:
  - id: list_temporary_enrollment_pairings
    intent: List temporary enrollment pairings
    question: Which temporary enrollment pairings exist in our root account?
  - id: create_temporary_enrollment_pairing
    intent: Create a temporary enrollment pairing
    question: How do I set up a temporary enrollment pairing, for example for a substitute teacher?
  - id: get_single_temporary_enrollment_pairing
    intent: Get one temporary enrollment pairing
    question: How do I look up a specific temporary enrollment pairing?
  - id: delete_temporary_enrollment_pairing
    intent: Delete a temporary enrollment pairing
    question: Can I remove a temporary enrollment pairing once it's no longer needed?
  - id: new_temporaryenrollmentpairing
    intent: Start a blank temporary enrollment pairing
    question: Can I get an unsaved template of a temporary enrollment pairing before creating one?
  phrasing_ops: 5
  slug: canvas-temporary-enrollment-pairings-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The User Observees API from Canvas — 5 operation(s) for user observees.
  name: Canvas User Observees API
  phrasing_intents:
  - id: list_linked_observees
    intent: List the students a user observes
    question: Which students is a parent account linked to observe in Canvas?
  - id: add_observee_with_credentials
    intent: Link an observee using their credentials or pairing code
    question: How does a parent link to their child's account with a pairing code?
  - id: list_linked_observers
    intent: List the observers linked to a user
    question: Which parents or guardians are observing a student?
  - id: show_observee
    intent: Show one observed user
    question: How do I get details on a single student I observe?
  - id: add_observee
    intent: Register a user as an observee by id
    question: As an admin, how do I link an observer to a student by user id without credentials?
  - id: remove_observee
    intent: Unlink an observee from an observer
    question: How do I stop a parent from observing a student?
  - id: show_observer
    intent: Show one observer of a user
    question: How do I see details about a specific parent observing my account?
  - id: create_observer_pairing_code
    intent: Generate an observer pairing code for a student
    question: How does a student generate a code so a parent can link to them?
  phrasing_ops: 8
  slug: canvas-user-observees-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Users API from Canvas — 38 operation(s) for users.
  name: Canvas Users API
  phrasing_intents:
  - id: list_users_in_account
    intent: List users in an account
    question: How can I see every user that belongs to a Canvas account?
  - id: create_user
    intent: Create a user with a login in an account
    question: How do I add a new person with a login to a Canvas account as an admin?
  - id: upload_file_users
    intent: Upload a file to a user's personal files
    question: How do I upload a file into a user's personal files area?
  - id: list_activity_stream_self
    intent: List my activity stream
    question: How can I pull my own recent activity stream from the self endpoint?
  - id: hide_all_stream_items
    intent: Hide every item in my activity stream
    question: Can I clear out my whole activity stream at once?
  - id: list_activity_stream_activity_stream
    intent: List my activity stream (alternate route)
    question: Is there an alternate route without self to fetch the current user's activity stream?
  - id: activity_stream_summary
    intent: Summarize my activity stream
    question: How do I get counts of what's in my activity stream by type?
  - id: list_todo_items
    intent: List my to-do items
    question: What's on my Canvas to-do list right now?
  phrasing_ops: 48
  slug: canvas-users-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The Webhooks Subscriptions For Plagiarism Platform API from Canvas — 2 operation(s) for webhooks subscriptions for plagiarism platform.
  name: Canvas Webhooks Subscriptions For Plagiarism Platform API
  phrasing_intents:
  - id: create_webhook_subscription
    intent: Subscribe a tool to Canvas events
    question: How does a plagiarism platform subscribe to submission events in Canvas?
  - id: list_all_webhook_subscription_for_tool_proxy
    intent: List my tool's webhook subscriptions
    question: What webhook subscriptions does my plagiarism-detection tool have?
  - id: delete_webhook_subscription
    intent: Delete a webhook subscription
    question: How do I stop receiving events from a webhook subscription?
  - id: show_single_webhook_subscription
    intent: Get a webhook subscription
    question: How do I check the details of one webhook subscription?
  - id: update_webhook_subscription
    intent: Update a webhook subscription
    question: Can I change the events or transport on an existing webhook subscription?
  phrasing_ops: 5
  slug: canvas-webhooks-subscriptions-for-plagiarism-platform-api
- baseURL: https://canvas.instructure.com/api/v1
  baseurl_source: declared
  description: The What If Grades API from Canvas — 2 operation(s) for what if grades.
  name: Canvas What If Grades API
  phrasing_intents:
  - id: update_submission_s_what_if_score_and_calculate_grades
    intent: Try a what-if score on a submission
    question: What would my course grade be if I scored a certain number on this assignment?
  - id: reset_what_if_scores_for_current_user_for_entire_course_and_recalculate_grades
    intent: Clear all my what-if scores in a course
    question: How do I clear every hypothetical score I entered in a course?
  phrasing_ops: 2
  slug: canvas-what-if-grades-api
- description: Platform Notification Service (PNS) enables server-to-server communication by allowing Canvas to send Notices (webhook deliveries) to LTI tools outside the scope of an active user session. Tools regis
  name: Canvas Platform Notification Service
  slug: canvas-platform-notification-service
- description: Canvas Live Events stream lifecycle events emitted by Canvas (course, enrollment, assignment, submission, grade change, discussion, module, outcome, file/attachment, SIS batch, conversation, quiz, wik
  name: Canvas Live Events
  slug: canvas-live-events
- description: Data Access Platform (DAP) is the warehouse-scale data export API for Canvas Data 2 — the successor to Canvas Data 1 / Canvas Data CLI. DAP exposes Canvas tables and Caliper-derived event streams as s
  name: Canvas Data Access Platform
  slug: canvas-data-access-platform
- baseURL: https://canvas.instructure.com/api/graphql
  baseurl_source: declared
  description: The JWTs API from Canvas — 2 operation(s) for jwts.
  name: Canvas JWTs API
  phrasing_intents:
  - id: create_jwt
    intent: Create a JWT for other Canvas services
    question: How do I get a short-lived JWT to call other Canvas services?
  - id: refresh_jwt
    intent: Refresh an existing JWT
    question: Can I swap an expiring JWT for a fresh one?
  phrasing_ops: 2
  slug: canvas-jwts-api
artifact_total: 168
asyncapis:
- description: AsyncAPI description of the Canvas LMS Live Events surface. Live Events are emitted by Canvas when interesting actions occur (course/assignment/submission/enrollment/discussion/module/outcome/file/SIS
  name: Canvas LMS Live Events
  slug: canvas-live-events-asyncapi
- description: ''
  name: Canvas Live Events Webhooks
  slug: canvas-live-events-webhooks
collections:
- collection_type: open
  name: Canvas LMS REST API ( subset) Courses API
  slug: open-canvas-courses-api
- collection_type: open
  name: Canvas LMS REST API (Courses subset)
  slug: open-canvas
common:
- group: commercial
  href: https://artifacts.apis.io/canvas/finops/canvas-finops.yml
  title: ''
  type: FinOps
  url: finops/canvas-finops.yml
- group: auth
  href: https://artifacts.apis.io/canvas/scopes/canvas-scopes.yml
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
  href: https://artifacts.apis.io/canvas/agentic-access/canvas-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/canvas-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/canvas/security/canvas-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/canvas-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/canvas/security/canvas-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/canvas-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/canvas/security/canvas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canvas-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/canvas/authentication/canvas-authentication.yml
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
  href: https://artifacts.apis.io/canvas/packages/canvas-packages.yml
  title: ''
  type: Packages
  url: packages/canvas-packages.yml
- group: build
  href: https://artifacts.apis.io/canvas/packages/canvas-packages.yml
  title: ''
  type: SDKs
  url: packages/canvas-packages.yml
- group: agent
  href: https://artifacts.apis.io/canvas/well-known/canvas-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canvas-well-known.yml
- group: auth
  href: https://artifacts.apis.io/canvas/well-known/canvas-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/canvas-security.txt
- group: agent
  href: https://artifacts.apis.io/canvas/llms/canvas-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canvas-llms.txt
- group: build
  href: https://artifacts.apis.io/canvas/mcp/canvas-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/canvas-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/canvas/conformance/canvas-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canvas-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.instructure.com/trust-center
- group: design
  href: https://artifacts.apis.io/canvas/errors/canvas-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canvas-problem-types.yml
- group: design
  href: https://artifacts.apis.io/canvas/lifecycle/canvas-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/canvas-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://community.canvaslms.com/t5/Change-Log/tkb-p/changelog
- group: operate
  href: https://artifacts.apis.io/canvas/changelog/canvas-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/canvas-changelog.yml
- group: design
  href: https://artifacts.apis.io/canvas/conventions/canvas-conventions.yml
  title: ''
  type: Conventions
  url: conventions/canvas-conventions.yml
- group: start
  href: https://artifacts.apis.io/canvas/sandbox/canvas-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/canvas-sandbox.yml
- group: build
  href: https://artifacts.apis.io/canvas/cli/canvas-cli.yml
  title: ''
  type: CLI
  url: cli/canvas-cli.yml
- group: design
  href: https://artifacts.apis.io/canvas/components/canvas-components.yml
  title: ''
  type: Components
  url: components/canvas-components.yml
- group: design
  href: https://artifacts.apis.io/canvas/data-model/canvas-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canvas-data-model.yml
- group: design
  href: https://artifacts.apis.io/canvas/asyncapi/canvas-live-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/canvas-live-events-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/canvas/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/canvas/rate-limits/canvas-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/canvas-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/canvas/plans/canvas-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canvas-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://www.instructure.com/trust-center/vulnerability-disclosure
- group: other
  href: https://artifacts.apis.io/canvas/overlays/canvas-canvas-lms-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canvas-canvas-lms-overlay.yaml
- group: other
  href: https://artifacts.apis.io/canvas/overlays/canvas-canvas-courses-api-overlay.yaml
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
  href: https://artifacts.apis.io/canvas/mcp/canvas-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/canvas-mcp.yml
- group: docs
  title: ''
  type: Documentation
  url: https://canvas.instructure.com/doc/api/all_resources.html
- group: docs
  title: ''
  type: Documentation
  url: https://canvas.instructure.com/doc/api/file.graphql.html
- group: docs
  title: ''
  type: Documentation
  url: https://canvas.instructure.com/doc/api/file.tools_intro.html
- group: company
  title: ''
  type: Blog
  url: https://www.instructure.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/instructure/canvas-lms/wiki
created: '2025-01-14'
description: Canvas is Instructure's open-source learning management system (LMS) used by K-12, higher education, and corporate training organizations to deliver courses, assessments, and learner communication. Canvas exposes a comprehensive REST API and a GraphQL endpoint for reading and modifying courses, assignments, quizzes, grades, users, enrollments, content, and account administration, and it integrates with external tools through LTI, Caliper, and live event streams.
finops:
- has_sources: true
  method: derived
  name: Canvas Finops
  primary_unit: ''
  service_category: ''
  slug: canvas-finops
  template: true
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
overview: 'Canvas publishes 148 API contracts indexed on the [APIs.io](https://apis.io/) network, including Courses API, Access Tokens API, Accessibility Course Scans API, and 145 more. Tagged areas include Canvas, Education, EdTech, GraphQL, and LMS.


  The Canvas catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Canvas'' developer surface includes authentication, documentation, engineering blog, changelog, sandbox, CLI, API reference, and 51 more developer resources.'
plans:
- name: Canvas Plans Pricing
  plan_count: 1
  slug: canvas-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Canvas Rate Limits
  slug: canvas-rate-limits
rules:
- authorship: generated
  effective_rule_count: 115
  extends:
  - spectral:oas
  name: Canvas API Rules
  rule_count: 74
  severity_counts:
    error: 64
    hint: 0
    info: 1
    warn: 9
  slug: canvas-rules
scopes:
- name: Canvas Scopes
  scope_count: 1117
  slug: canvas-scopes
  summary_line: 1117 scopes · authorizationCode
score:
  band: exemplar
  composite: 70.3
  coverage:
    artifact_dirs: 34
    catalog_earned: 60.5
    catalog_earned_first_party: 16.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 31.1
    developer_ergonomics: 80.4
    discoverability: 78.6
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  open_source:
    applies: true
    score: 75.0
  previous_composite: 70.3
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
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/canvas/canvas-2026-06-20T173929.png
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
skill_count: 5
skills:
- name: Read submissions for an assignment and post grades and comments
  slug: canvas-grade-and-return-work
- name: Provision a Canvas course and enrol people into it
  slug: canvas-provision-course-and-enroll
- name: Read a course's structure and content without changing anything
  slug: canvas-read-course-content
- name: Register an LTI 1.3 tool in a Canvas account and deploy it
  slug: canvas-register-an-lti-tool
- name: Load or update rosters in bulk with a Canvas SIS import
  slug: canvas-sync-roster-via-sis-import
slug: canvas
tags:
- Canvas
- Education
- EdTech
- GraphQL
- LMS
- LTI
- Open Source
- REST
- Higher Education
- K-12
- AGPL
website: https://www.instructure.com/canvas
---
