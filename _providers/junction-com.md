---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
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
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 45
  human_in_the_loop: 0
  name: Junction Com Agentic Access
  operation_count: 197
  slug: junction-com-agentic-access
  summary_line: 197 operations · 45 acting
api_count: 9
apis:
- description: Programmatically manage all Junction regional and global resources for your organization. Authenticated with a separate x-vital-management-api-key, this API governs organizations, teams (create, updat
  name: Junction Management API
  slug: junction-management-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The Aggregate API from Vital — 3 operation(s) for aggregate.
  name: Junction Aggregate API
  phrasing_intents:
  - id: query_one_aggregate_v1_user__user_id__query_post
    intent: Run an aggregate query over a user's data
    question: Can I run a custom aggregation over one user's health data for a set timeframe?
  - id: get_result_table_for_query_aggregate_v1_user__user_id__continuous_query__query_id_or_slug__result_table_get
    intent: Get a continuous query's result table
    question: Where can I read the latest output table of a continuous query set up for a user?
  - id: get_task_history_for_query_aggregate_v1_user__user_id__continuous_query__query_id_or_slug__task_history_get
    intent: List a continuous query's past runs
    question: Can I see when a user's continuous query last ran and whether it succeeded?
  phrasing_ops: 3
  slug: junction-com-aggregate-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The compendium API from Vital — 2 operation(s) for compendium.
  name: Junction Compendium API
  phrasing_intents:
  - id: search_compendium_v3_compendium_search_post
    intent: Search the lab test compendium
    question: Can I find orderable lab tests in the compendium by CPT code?
  - id: convert_compendium_v3_compendium_convert_post
    intent: Convert a lab test to another lab's equivalent
    question: Can I map a lab test to the equivalent orderable tests at a different lab?
  phrasing_ops: 2
  slug: junction-com-compendium-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The insurance API from Vital — 3 operation(s) for insurance.
  name: Junction Insurance API
  phrasing_intents:
  - id: post_insurance_payor_information_v3_insurance_search_payor_post
    intent: Search payors with a POST request body
    question: Can I submit a payor lookup as a JSON body instead of query parameters?
  - id: search_insurance_payor_information_v3_insurance_search_payor_get
    intent: Search insurance payors by name
    question: How do I find the payor code for a patient's insurance company?
  - id: search_diagnosis_v3_insurance_search_diagnosis_get
    intent: Search diagnoses by keyword
    question: What diagnosis code matches a condition like type 2 diabetes?
  - id: validate_icd_codes_v3_insurance_validate_icd_codes_post
    intent: Validate a list of ICD codes
    question: Can I check whether a list of ICD codes is valid before placing an order?
  phrasing_ops: 4
  slug: junction-com-insurance-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The introspect API from Vital — 2 operation(s) for introspect.
  name: Junction Introspect API
  phrasing_intents:
  - id: introspect_resources_v2_introspect_resources_get
    intent: Inspect synced data resources per user
    question: Can I see which data resources each user has synced from a provider?
  - id: introspect_historical_pulls_v2_introspect_historical_pull_get
    intent: Inspect historical data pulls per user
    question: Has the historical backfill finished for a user's newly connected provider?
  phrasing_ops: 2
  slug: junction-com-introspect-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The lab_account API from Vital — 1 operation(s) for lab_account.
  name: Junction Lab Account API
  phrasing_intents:
  - id: get_team_lab_accounts_v3_lab_test_lab_account_get
    intent: List my team's lab accounts
    question: Which lab accounts does my team have access to?
  phrasing_ops: 1
  slug: junction-com-lab-account-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The lab_report API from Vital — 2 operation(s) for lab_report.
  name: Junction Lab Report API
  phrasing_intents:
  - id: CreateLabReportParserJob
    intent: Parse an uploaded lab report
    question: Can I upload a lab report file and have the results extracted?
  - id: get_lab_report_parser_job_lab_report_v1_parser_job__job_id__get
    intent: Check a lab report parse job
    question: Has my lab report parse job finished, and what did it extract?
  phrasing_ops: 2
  slug: junction-com-lab-report-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The lab_tests API from Vital — 9 operation(s) for lab_tests.
  name: Junction Lab Tests API
  phrasing_intents:
  - id: get_lab_tests_for_team_v3_lab_tests_get
    intent: List all lab tests my team can order
    question: What lab tests can my team order?
  - id: create_lab_test_for_team_v3_lab_tests_post
    intent: Create a custom lab test
    question: Can I build my own lab test panel from a set of markers?
  - id: update_lab_test_for_team_v3_lab_tests__lab_test_id__patch
    intent: Rename or deactivate a lab test
    question: Can I rename a lab test after creating it?
  - id: get_lab_test_for_team_v3_lab_tests__lab_test_id__get
    intent: Get one lab test
    question: What's included in one specific lab test my team has?
  - id: get_markers_v3_lab_tests_markers_get
    intent: List orderable markers at a lab
    question: Which biomarkers can I order from a particular lab?
  - id: get_markers_for_order_set_v3_lab_tests_list_order_set_markers_post
    intent: List markers for an order set
    question: What markers would an order set of several lab tests plus add-ons include?
  - id: get_markers_for_test_v3_lab_tests__lab_test_id__markers_get
    intent: List a lab test's markers and reflexes
    question: Which markers, including reflex markers, does a lab test cover?
  - id: get_markers_by_provider_id_v3_lab_tests__lab_id__markers__provider_id__get
    intent: Look up a marker by a lab's provider ID
    question: Can I look up a marker using the lab's own test code?
  phrasing_ops: 11
  slug: junction-com-lab-tests-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The link API from Vital — 13 operation(s) for link.
  name: Junction Link API
  phrasing_intents:
  - id: list_bulk_ops_v2_link_bulk_op_get
    intent: List bulk connection operations
    question: Can I see the status of my bulk import, export and pause jobs?
  - id: bulk_import_connections_v2_link_bulk_import_post
    intent: Bulk import existing provider connections
    question: Can I import existing device connections for many users at once?
  - id: bulk_trigger_historical_pull_v2_link_bulk_trigger_historical_pull_post
    intent: Trigger historical pulls for many users
    question: Can I trigger a historical backfill for a batch of users at once?
  - id: bulk_export_connections_v2_link_bulk_export_post
    intent: Export users' provider connections
    question: Can I export my users' connections for a provider?
  - id: bulk_pause_connections_v2_link_bulk_pause_post
    intent: Pause provider connections in bulk
    question: Can I pause data syncing for many users' connections at once?
  - id: generate_vital_link_token_v2_link_token_post
    intent: Generate a Link token to connect a user
    question: How do I start the Vital Link connection flow for one of my users?
  - id: create_token_v2_link_code_create_post
    intent: Invite a mobile app user to my team
    question: Can I invite someone using the Vital mobile app to join my team?
  - id: generate_oauth_link
    intent: Get an OAuth authorization link for a provider
    question: How do I get the OAuth URL a user visits to authorize a provider?
  phrasing_ops: 13
  slug: junction-com-link-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The order API from Vital — 32 operation(s) for order.
  name: Junction Order API
  phrasing_intents:
  - id: register_testkit_v3_order_testkit_register_post
    intent: Register a received test kit
    question: How does a patient register a test kit they received?
  - id: create_testkit_order_v3_order_testkit_post
    intent: Order an unregistered test kit
    question: Can I ship an at-home test kit to a user before it's registered?
  - id: get_order_appointment_availability_v3_order_phlebotomy_appointment_availability_post
    intent: Find at-home blood draw time slots
    question: What at-home blood draw time slots are open near a patient's address?
  - id: book_phlebotomy_appointment_v3_order__order_id__phlebotomy_appointment_book_post
    intent: Book an at-home blood draw
    question: How do I book an at-home blood draw for an order?
  - id: request_phlebotomy_appointment_v3_order__order_id__phlebotomy_appointment_request_post
    intent: Request an at-home blood draw
    question: Can I request an at-home draw without picking a specific time slot?
  - id: reschedule_phlebotomy_appointment_v3_order__order_id__phlebotomy_appointment_reschedule_patch
    intent: Reschedule an at-home blood draw
    question: Can I move a booked at-home blood draw to another time?
  - id: cancel_phlebotomy_appointment_v3_order__order_id__phlebotomy_appointment_cancel_patch
    intent: Cancel an at-home blood draw
    question: How do I cancel an at-home phlebotomy appointment?
  - id: get_phlebotomy_appointment_cancellation_reasons_v3_order_phlebotomy_appointment_cancellation_reasons_get
    intent: List reasons for cancelling a home draw
    question: What reasons are accepted for cancelling an at-home blood draw?
  phrasing_ops: 33
  slug: junction-com-order-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The order_transaction API from Vital — 3 operation(s) for order_transaction.
  name: Junction Order Transaction API
  phrasing_intents:
  - id: get_order_transaction_v3_order_transaction__transaction_id__get
    intent: Get an order transaction
    question: What orders belong to an order transaction?
  - id: get_order_transaction_result_v3_order_transaction__transaction_id__result_get
    intent: Get an order transaction's results
    question: Can I get combined results for every order in a transaction?
  - id: get_order_transaction_result_pdf_v3_order_transaction__transaction_id__result_pdf_get
    intent: Download an order transaction's results PDF
    question: Can I download a PDF of an order transaction's results?
  phrasing_ops: 3
  slug: junction-com-order-transaction-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The orders API from Vital — 1 operation(s) for orders.
  name: Junction Orders API
  phrasing_intents:
  - id: get_orders_v3_orders_get
    intent: List and filter lab orders
    question: Can I list lab orders filtered by status and date range?
  phrasing_ops: 1
  slug: junction-com-orders-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The payor API from Vital — 1 operation(s) for payor.
  name: Junction Payor API
  phrasing_intents:
  - id: create_payor_v3_payor_post
    intent: Create an insurance payor
    question: Can I add an insurance payor that isn't already listed?
  phrasing_ops: 1
  slug: junction-com-payor-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The providers API from Vital — 1 operation(s) for providers.
  name: Junction Providers API
  phrasing_intents:
  - id: get_list_of_providers_v2_providers_get
    intent: List supported data providers
    question: Which data providers does Vital support?
  phrasing_ops: 1
  slug: junction-com-providers-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The summary API from Vital — 15 operation(s) for summary.
  name: Junction Summary API
  phrasing_intents:
  - id: get_user_electrocardiogram_v2_summary_electrocardiogram__user_id__get
    intent: Get a user's electrocardiogram summaries
    question: Can I get a user's electrocardiogram readings for a date range?
  - id: get_user_sleep_cycle_v2_summary_sleep_cycle__user_id__get
    intent: Get a user's sleep cycles
    question: Can I see a user's sleep cycle data for a period?
  - id: get_user_profile_v2_summary_profile__user_id__get
    intent: Get a user's normalized profile
    question: What profile information has a user's connected device shared?
  - id: get_user_profile_raw_v2_summary_profile__user_id__raw_get
    intent: Get a user's raw provider profile
    question: Can I see the raw profile payload exactly as a provider sent it?
  - id: get_user_devices_raw_v2_summary_devices__user_id__raw_get
    intent: Get a user's raw device data
    question: Which devices has a user connected, in the provider's raw format?
  - id: get_user_activity_v2_summary_activity__user_id__get
    intent: Get a user's daily activity summaries
    question: How active was a user each day over a date range?
  - id: get_user_activity_raw_v2_summary_activity__user_id__raw_get
    intent: Get a user's raw activity data
    question: Can I see raw activity data exactly as the provider reported it?
  - id: get_user_workouts_v2_summary_workouts__user_id__get
    intent: Get a user's workout summaries
    question: What workouts did a user log in a date range?
  phrasing_ops: 15
  slug: junction-com-summary-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The team API from Vital — 5 operation(s) for team.
  name: Junction Team API
  phrasing_intents:
  - id: get_team_v2_team__team_id__get
    intent: Get a team's details
    question: What configuration and details are stored for my team?
  - id: search_team_users_by_uuid_or_client_user_id_v2_team_users_search_get
    intent: Find a team user by either ID
    question: Can I find a team user by their Vital user ID or my own client user ID?
  - id: get_svix_webhook_url_v2_team_svix_url_get
    intent: Get my team's webhook portal URL
    question: Where do I manage my team's webhook endpoints?
  - id: get_source_priorities_v2_team_source_priorities_get
    intent: Get data source priorities
    question: Which data source takes precedence when several providers report the same data?
  - id: update_source_priorities_v2_team_source_priorities_patch
    intent: Update data source priorities
    question: Can I change which provider wins when data sources overlap?
  - id: get_team_physicians_v2_team__team_id__physicians_get
    intent: List a team's physicians
    question: Which physicians are set up for my team?
  phrasing_ops: 6
  slug: junction-com-team-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The user API from Vital — 16 operation(s) for user.
  name: Junction User API
  phrasing_intents:
  - id: get_teams_users_v2_user_get
    intent: List my team's users
    question: Can I list every user on my team?
  - id: create_user_v2_user_post
    intent: Create a user
    question: How do I create a Vital user for someone in my app?
  - id: get_teams_metrics_v2_user_metrics_get
    intent: Get my team's metrics
    question: What usage metrics are available for my team?
  - id: get_connected_providers_v2_user_providers__user_id__get
    intent: List a user's connected providers
    question: Which providers has a user connected?
  - id: get_user_demographcis_v2_user__user_id__info_latest_get
    intent: Get a user's latest demographics
    question: What demographic info is on file for a user?
  - id: create_insurance_v2_user__user_id__insurance_post
    intent: Add health insurance to a user
    question: How do I add health insurance to a user?
  - id: get_latest_insurance_v2_user__user_id__insurance_latest_get
    intent: Get a user's latest insurance
    question: What insurance is currently on file for a user?
  - id: create_user_demographics_v2_user__user_id__info_patch
    intent: Save a user's demographic details
    question: How do I save a user's name, contact details and address?
  phrasing_ops: 19
  slug: junction-com-user-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The aggregation API from Vital — 0 operation(s) for aggregation.
  name: Junction Aggregation API
  slug: junction-com-aggregation-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The lab-testing API from Vital — 0 operation(s) for lab-testing.
  name: Junction Lab Testing API
  slug: junction-com-lab-testing-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The checkout API from Vital — 6 operation(s) for checkout.
  name: Junction Checkout API
  slug: junction-com-checkout-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The unmatched API from Vital — 8 operation(s) for unmatched.
  name: Junction Unmatched API
  slug: junction-com-unmatched-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The Time Series API from Vital — 80 operation(s) for time series.
  name: Junction Time Series API
  phrasing_intents:
  - id: get_user_sleep_stream_v2_timeseries_sleep__sleep_id__stream_get
    intent: Get the sample stream for one sleep session
    question: Can I get second-by-second data like heart rate during a single night's sleep?
  - id: get_user_workouts_v2_timeseries_workouts__workout_id__stream_get
    intent: Get the sample stream for one workout
    question: Can I see the detailed data stream captured during one workout?
  - id: get_workout_swimming_stroke_grouped
    intent: Get swimming stroke counts grouped by source
    question: Can I pull a swimmer's stroke counts from their workouts?
  - id: get_workout_distance_grouped
    intent: Get workout distance samples grouped by source
    question: How far did a user go during workouts over a date range?
  - id: get_heart_rate_recovery_one_minute_grouped
    intent: Get one-minute heart rate recovery by source
    question: Can I track how quickly a user's heart rate drops one minute after exercise?
  - id: get_waist_circumference_grouped
    intent: Get waist circumference readings by source
    question: Can I pull a user's waist measurements over time?
  - id: get_lean_body_mass_grouped
    intent: Get lean body mass readings by source
    question: How has a user's lean body mass changed over a period?
  - id: get_body_mass_index_grouped
    intent: Get BMI readings grouped by source
    question: Can I get a user's BMI history?
  phrasing_ops: 80
  slug: junction-com-time-series-api
arazzos:
- description: Confirm phlebotomy coverage for an address, place an at-home order, find a slot, and book it.
  name: Vital Schedule an At-Home Phlebotomy Draw
  slug: junction-com-at-home-phlebotomy-booking-workflow
- description: Poll an existing order until it completes, then pull its result metadata and raw results.
  name: Vital Await Lab Order Completion and Retrieve Results
  slug: junction-com-await-order-results-workflow
- description: List your team's lab tests, fetch one in detail, and enumerate its biomarkers.
  name: Vital Browse Lab Tests and Inspect Markers
  slug: junction-com-browse-lab-tests-markers-workflow
- description: Cancel an order, confirm the cancellation, then mint a communications portal URL deeplinked to it.
  name: Vital Cancel a Lab Order and Send the User a Portal Link
  slug: junction-com-cancel-order-notify-portal-workflow
- description: Place an order set lab order for a user and poll its lifecycle status until it completes, cancels, or fails.
  name: Vital Create a Lab Order and Poll Until Resolved
  slug: junction-com-create-order-poll-status-workflow
- description: Create a user, attach a demo provider, then confirm the connection landed on the user record.
  name: Vital Connect a Demo Provider and Verify Connected Sources
  slug: junction-com-demo-connection-verify-sources-workflow
- description: Create a Vital user, mint a mobile sign-in token, and read back the user's connected providers.
  name: Vital Provision a User and Hand Off a Mobile Sign-In Token
  slug: junction-com-mobile-signin-token-handoff-workflow
- description: Create a Vital user, mint a Link token, and surface the available providers to connect.
  name: Vital Onboard a User and Connect a Wearable
  slug: junction-com-onboard-user-connect-wearable-workflow
- description: Create an unregistered testkit order, register it against a sample, then read the order back.
  name: Vital Create and Register a Lab Testkit Order
  slug: junction-com-testkit-order-register-workflow
- description: Resolve a user by client_user_id, list their devices, and fetch the first device in detail.
  name: Vital Inventory a User's Connected Devices
  slug: junction-com-user-device-inventory-workflow
artifact_total: 129
asyncapis:
- description: ''
  name: Junction Com Webhooks
  slug: junction-com-webhooks
collections:
- collection_type: postman
  name: Vital Lab Report Parser API
  slug: postman-vital-lab-report-parser-api
- collection_type: postman
  name: Vital Lab Testing API
  slug: postman-vital-lab-testing-api
- collection_type: postman
  name: Vital Link API
  slug: postman-vital-link-api
- collection_type: postman
  name: Vital Sense API
  slug: postman-vital-sense-api
- collection_type: postman
  name: Vital Team API
  slug: postman-vital-team-api
- collection_type: postman
  name: Vital Users API
  slug: postman-vital-users-api
- collection_type: postman
  name: Vital Wearables Data API
  slug: postman-vital-wearables-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate API
  slug: open-junction-com-aggregate-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate compendium API
  slug: open-junction-com-compendium-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate insurance API
  slug: open-junction-com-insurance-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate introspect API
  slug: open-junction-com-introspect-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate lab_account API
  slug: open-junction-com-lab-account-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate lab_report API
  slug: open-junction-com-lab-report-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate lab_tests API
  slug: open-junction-com-lab-tests-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate link API
  slug: open-junction-com-link-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate order API
  slug: open-junction-com-order-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate order_transaction API
  slug: open-junction-com-order-transaction-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate orders API
  slug: open-junction-com-orders-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate payor API
  slug: open-junction-com-payor-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate providers API
  slug: open-junction-com-providers-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate summary API
  slug: open-junction-com-summary-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate team API
  slug: open-junction-com-team-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate timeseries API
  slug: open-junction-com-timeseries-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate user API
  slug: open-junction-com-user-api
- collection_type: open
  name: Vital Lab Report Parser API
  slug: open-vital-lab-report-parser-api
- collection_type: open
  name: Vital Lab Testing API
  slug: open-vital-lab-testing-api
- collection_type: open
  name: Vital Link API
  slug: open-vital-link-api
- collection_type: open
  name: Junction API
  slug: open-vital-openapi-original
- collection_type: open
  name: Vital Sense API
  slug: open-vital-sense-api
- collection_type: open
  name: Vital Team API
  slug: open-vital-team-api
- collection_type: open
  name: Vital Users API
  slug: open-vital-users-api
- collection_type: open
  name: Vital Wearables Data API
  slug: open-vital-wearables-api
common:
- group: design
  href: https://artifacts.apis.io/junction-com/rules/vital-rules.yml
  title: ''
  type: Spectral
  url: rules/vital-rules.yml
- group: design
  href: https://artifacts.apis.io/junction-com/rules/junction-com-rules.yml
  title: ''
  type: Spectral
  url: rules/junction-com-rules.yml
- group: design
  href: https://artifacts.apis.io/junction-com/rules/junction-com-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/junction-com-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/junction-com/asyncapi/junction-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/junction-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/junction-com/data-model/junction-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/junction-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/junction-com/changelog/junction-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/junction-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/junction-com/conventions/junction-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/junction-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/junction-com/conventions/junction-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/junction-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/junction-com/errors/junction-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/junction-com-problem-types.yml
- group: other
  href: https://artifacts.apis.io/junction-com/overlays/junction-com-aggregate-api-phrasing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/junction-com-aggregate-api-phrasing-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/junction-com/llms/junction-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/junction-com-llms.txt
- group: other
  href: https://artifacts.apis.io/junction-com/a2a/junction-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/junction-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/junction-com/mcp/junction-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/junction-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/junction-com/mcp/junction-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/junction-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/junction-com/hosts/junction-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/junction-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/junction-com/vendors/junction-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/junction-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/junction-com/packages/junction-com-packages.yml
  title: ''
  type: Packages
  url: packages/junction-com-packages.yml
- group: other
  href: https://artifacts.apis.io/junction-com/capabilities/junction-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/junction-com-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/junction-com/agentic-access/junction-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/junction-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/junction-com/security/junction-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/junction-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/junction-com/authentication/junction-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/junction-com-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vital/overview
- group: design
  href: https://artifacts.apis.io/junction-com/arazzo/junction-com-at-home-phlebotomy-booking-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/junction-com-at-home-phlebotomy-booking-workflow.yml
- group: design
  href: https://artifacts.apis.io/junction-com/arazzo/junction-com-await-order-results-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/junction-com-await-order-results-workflow.yml
- group: design
  href: https://artifacts.apis.io/junction-com/arazzo/junction-com-browse-lab-tests-markers-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/junction-com-browse-lab-tests-markers-workflow.yml
- group: design
  href: https://artifacts.apis.io/junction-com/arazzo/junction-com-cancel-order-notify-portal-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/junction-com-cancel-order-notify-portal-workflow.yml
- group: design
  href: https://artifacts.apis.io/junction-com/arazzo/junction-com-create-order-poll-status-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/junction-com-create-order-poll-status-workflow.yml
- group: design
  href: https://artifacts.apis.io/junction-com/arazzo/junction-com-demo-connection-verify-sources-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/junction-com-demo-connection-verify-sources-workflow.yml
- group: design
  href: https://artifacts.apis.io/junction-com/arazzo/junction-com-mobile-signin-token-handoff-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/junction-com-mobile-signin-token-handoff-workflow.yml
- group: design
  href: https://artifacts.apis.io/junction-com/arazzo/junction-com-onboard-user-connect-wearable-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/junction-com-onboard-user-connect-wearable-workflow.yml
- group: design
  href: https://artifacts.apis.io/junction-com/arazzo/junction-com-testkit-order-register-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/junction-com-testkit-order-register-workflow.yml
- group: design
  href: https://artifacts.apis.io/junction-com/arazzo/junction-com-user-device-inventory-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/junction-com-user-device-inventory-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.junction.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.junction.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.junction.com/api-details/junction-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.junction.com/home/quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.junction.com/home/welcome
- group: start
  title: ''
  type: Console
  url: https://app.junction.com
- group: start
  title: ''
  type: Signup
  url: https://app.junction.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.junction.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tryvital.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tryvital.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.junction.com/home/api/changelog
- group: operate
  title: ''
  type: RateLimiting
  url: https://docs.junction.com/home/rate-limiting
- group: docs
  title: ''
  type: Documentation
  url: https://docs.junction.com/home/regions
- group: auth
  title: ''
  type: Authentication
  url: https://docs.junction.com/home/authentication
- group: design
  title: ''
  type: Webhooks
  url: https://docs.junction.com/webhooks/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.junction.com/wearables/providers/introduction
- group: auth
  title: ''
  type: Security
  url: https://docs.junction.com/home/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tryVital
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tryVital/vital-fern-api
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tryVital/docs
- group: build
  title: ''
  type: SampleApp
  url: https://github.com/tryVital/quickstart
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/tryVital/vital-fern-api/main/fern/openapi/openapi.json
- group: docs
  href: https://artifacts.apis.io/junction-com/openapi/_original/vital-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/vital-openapi-original.json
- group: docs
  href: https://artifacts.apis.io/junction-com/openapi/_original/vital-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/vital-openapi-original.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tryvital/vital-node
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tryvital/vital-link
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tryvital/vital-core-react-native
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tryvital/vital-devices-react-native
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@tryvital/vital-health-react-native
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/vital/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tryVital/vital-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tryVital/vital-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tryVital/vital-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tryVital/vital-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tryVital/vital-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tryVital/vital-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tryVital/vital-flutter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tryVital/vital-react-native
- group: build
  title: ''
  type: SampleApp
  url: https://github.com/tryVital/vital-connect-rn
- group: design
  href: https://artifacts.apis.io/junction-com/rules/vital-rules.yml
  title: ''
  type: SpectralRules
  url: rules/vital-rules.yml
- group: design
  href: https://artifacts.apis.io/junction-com/vocabulary/junction-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/junction-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/junction-com/json-ld/junction-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/junction-com-context.jsonld
- group: commercial
  href: https://artifacts.apis.io/junction-com/plans/junction-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/junction-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/junction-com/rate-limits/junction-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/junction-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/junction-com/finops/junction-com-finops.yml
  title: ''
  type: FinOps
  url: finops/junction-com-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.junction.com/
- group: operate
  title: ''
  type: Support
  url: https://vital.io/help
- group: company
  title: ''
  type: Blog
  url: https://vital.io/newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vital.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vital.io/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vital.io/
- group: design
  href: https://artifacts.apis.io/junction-com/lifecycle/junction-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/junction-com-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/junction-com/security/junction-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/junction-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/junction-com/security/junction-com-trust-center.yml
  title: ''
  type: Compliance
  url: security/junction-com-trust-center.yml
- group: design
  href: https://artifacts.apis.io/junction-com/conformance/junction-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/junction-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/junction-com/security/junction-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/junction-com-domain-security.yml
- group: design
  href: https://artifacts.apis.io/junction-com/lifecycle/junction-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/junction-com-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/junction-com/security/junction-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/junction-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/junction-com/security/junction-com-trust-center.yml
  title: ''
  type: Compliance
  url: security/junction-com-trust-center.yml
- group: design
  href: https://artifacts.apis.io/junction-com/conformance/junction-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/junction-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/junction-com/security/junction-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/junction-com-domain-security.yml
created: '2026-05-25'
description: Junction (formerly Vital, and tryVital before that) is a health-data API platform that gives digital-health, virtual-care, diagnostics, wellness, and EHR/EMR builders a single integration to wearable-device data and nationwide lab testing. Connect 300+ wearables and health devices — Apple HealthKit, Android Health Connect, Oura, Whoop, Garmin, Fitbit, Withings, Dexcom, Freestyle Libre, Withings, Polar, and the rest — through the Vital Link Widget; ingest normalized daily summaries and per-sample timeseries for sleep, activity, body, workouts, heart rate, HRV, glucose, blood pressure, SpO2, ECG, and menstrual cycle; order at-home testkits, at-home phlebotomy, walk-in / Patient Service Center lab collection, and on-site collection across all 50 U.S. states; retrieve structured biomarker results; and run Junction Sense continuous queries to turn raw data into clinically actionable insights. Backed by SOC 2 Type 2, ISO 27001, GDPR-ready, and HIPAA-compliant infrastructure with both
  US and EU regional deployments.
examples:
- key_count: 2
  name: Vital Create Order Example
  slug: vital-create-order-example
- key_count: 2
  name: Vital Create User Example
  slug: vital-create-user-example
- key_count: 2
  name: Vital Heart Rate Timeseries Example
  slug: vital-heart-rate-timeseries-example
- key_count: 2
  name: Vital Lab Result Example
  slug: vital-lab-result-example
- key_count: 2
  name: Vital Link Token Example
  slug: vital-link-token-example
- key_count: 2
  name: Vital Sleep Summary Example
  slug: vital-sleep-summary-example
features:
- description: Apple HealthKit, Android Health Connect, Samsung Health, Oura, Whoop, Garmin, Fitbit, Withings, Polar, Strava, Wahoo, Cronometer, Ultrahuman, Peloton, Zwift, Hammerhead, Dexcom (G6 and G7), Freestyle Libre (cloud + BLE), Abbott LibreView, 8Sleep, Beurer, Kardia, Accu-Chek, Contour, Omron — all behind a single, normalized schema.
  name: 300+ wearable and health-device integrations
- description: Drop-in user-facing UI that handles OAuth, email/password, and mobile-SDK connection flows. Generate a one-time Link token, hand it to the widget or Connect app, and the widget runs the full consent-and-connect handshake for any supported provider.
  name: Junction Link Widget and Connect app
- description: A single API to order at-home testkits, at-home phlebotomy, walk-in / Patient Service Center collection, and on-site collection across all 50 US states including NY, NJ, and RI — with no test upcharges and built-in operational support (result tracking, reminders, exception handling, 6-day support).
  name: Nationwide lab-testing network
- description: Every supported device, lab, and provider is mapped onto Vital's normalized schema so your app sees one Sleep, one Activity, one Heart Rate, one Glucose, one Biomarker — regardless of which Fitbit / Garmin / Quest / Labcorp source it came from.
  name: Normalized biomarker and timeseries schema
- description: Define a continuous aggregate query once (e.g. "weekly HRV baseline", "monthly glucose time-in-range") and Junction recomputes it as new data lands. Read the materialized result table per user or run an ad-hoc query.
  name: Junction Sense — continuous queries
- description: Daily-data created/updated events for every wearable resource, historical-pull completion, lab-test orders + appointments + critical results, lab-report parser status, provider connection events, and continuous-query result changes. Backed by Svix for retry, signing, and a per-team management portal.
  name: Webhooks with Svix-backed delivery
- description: Pipe ingested data directly into your own infrastructure — Azure Event Hubs, Google Cloud Pub/Sub, or RabbitMQ — instead of (or in addition to) webhooks. Configurable per team.
  name: ETL pipelines (BYO destination)
- description: Pick your data residency — production and sandbox base URLs are split into api.us.junction.com and api.eu.junction.com. Regional API key prefixes (pk_us, pk_eu, sk_us, sk_eu) prevent cross-region key reuse.
  name: US and EU regional deployments
- description: First-party Swift, Kotlin, Flutter, and React Native SDKs that wrap Apple HealthKit and Android Health Connect, plus Bluetooth Devices SDKs for direct device pairing (Accu-Chek, Beurer BLE, Contour, Freestyle Libre BLE, Omron BLE).
  name: Mobile SDKs for HealthKit and Health Connect
- description: Python, TypeScript/Node, Go, and Java SDKs are generated from a single Fern API spec — keeping the SDK surface in lockstep with the underlying OpenAPI 3.1 definition.
  name: Typed server SDKs (Fern-generated)
- description: BAA-eligible HIPAA infrastructure, SOC 2 Type 2 and ISO 27001 attestations, plus EU-region GDPR-aligned deployment. Suitable for regulated digital-health, virtual-care, and diagnostics workloads.
  name: HIPAA, SOC 2 Type 2, ISO 27001, GDPR-ready
- description: Dedicated sandbox environment (api.sandbox.us.junction.com / .eu.) with sk_* API keys, demo providers, and synthetic user lifecycle simulation so you can build and test without touching real PHI.
  name: Sandbox with synthetic data
- description: Submit existing lab-result PDFs (from other labs, historical patient records) and Vital normalizes them into the same biomarker schema as Junction-fulfilled orders.
  name: Lab report parser
finops:
- has_sources: false
  method: generated
  name: Junction Com Finops
  primary_unit: ''
  service_category: ''
  slug: junction-com-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vital-io.png
integrations:
- description: First-class iOS Swift SDK plus Flutter / React Native bindings stream HealthKit categories (sleep, activity, HR, HRV, workouts, ECG, glucose, blood pressure, body) into the Vital normalized schema.
  name: Apple HealthKit
- description: Kotlin / Flutter / React Native SDKs read from Android Health Connect — Samsung Health, Google Fit successor, Fitbit Android, and other Health Connect publishers — through one bridge.
  name: Android Health Connect
- description: Read Samsung-Health data on Android via the Health SDK without writing Samsung-Health-specific code.
  name: Samsung Health
- description: OAuth-based cloud providers, all behind one Link Widget flow and one normalized data schema.
  name: Oura, Whoop, Garmin, Fitbit, Withings, Polar
- description: Continuous-glucose monitoring via Dexcom cloud (v3), Freestyle Libre cloud, Abbott LibreView, and direct Bluetooth Low Energy for newer Libre models. Normalized into the glucose timeseries resource.
  name: Dexcom and Freestyle Libre (cloud + BLE)
- description: Non-OAuth cloud providers covering connected mattresses and indoor-training platforms.
  name: 8Sleep, Peloton, Zwift, Hammerhead
- description: Additional OAuth providers covering endurance training, nutrition logging, and metabolic wearables.
  name: Strava, Wahoo, Cronometer, Ultrahuman
- description: Accu-Chek, Beurer BLE, Contour, Freestyle Libre BLE, Omron BLE — paired directly to the user's phone through the Vital Devices SDK and reported back through the same API.
  name: Bluetooth devices via Devices SDK
- description: Forward ingested data to Azure Event Hubs, Google Cloud Pub/Sub, or RabbitMQ for in-house analytics pipelines.
  name: ETL destinations (Azure / GCP / RabbitMQ)
- description: Junction's normalized health-data API is a natural fit as a tool surface for Anthropic Claude agents — pair the Vital OpenAPI specs in this repo with Claude tool calling (or Naftiko capabilities / MCP servers) to let Claude reason over a patient's sleep, HRV, glucose, lab biomarkers, and order new lab panels under appropriate medical oversight.
  name: Anthropic Claude
- description: Vital's webhook delivery is Svix-backed — your team can be issued a Svix management portal URL for managing webhook endpoints, signing secrets, and delivery history.
  name: Svix
- description: The Junction OpenAPI definition and the Python/TypeScript/Go/Java server SDKs are generated with Fern from a single source of truth (github.com/tryVital/vital-fern-api).
  name: Fern
json_schemas:
- name: VitalActivitySummary
  property_count: 15
  slug: vital-activity-summary
- name: VitalHeartRateTimeseries
  property_count: 7
  slug: vital-heart-rate-timeseries
- name: VitalLabOrder
  property_count: 12
  slug: vital-lab-order
- name: VitalLabResult
  property_count: 8
  slug: vital-lab-result
- name: VitalProvider
  property_count: 6
  slug: vital-provider
- name: VitalSleepSummary
  property_count: 19
  slug: vital-sleep-summary
- name: VitalUser
  property_count: 7
  slug: vital-user
json_structures:
- name: Vital Lab Order Structure
  property_count: 0
  slug: vital-lab-order-structure
- name: Vital User Structure
  property_count: 0
  slug: vital-user-structure
jsonld:
- class_count: 31
  name: Junction Com Context
  property_count: 9
  slug: junction-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.junction.com; 3 tools listed.
  name: Junction documentation MCP server
  slug: junction-documentation-mcp-server
modified: '2026-05-25'
name: Junction
nav: Providers
network: true
overview: 'Junction publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aggregate API, Compendium API, Insurance API, and 19 more. Tagged areas include Health Data, Wearables, Lab Testing, Digital Health, and Health Tech.


  The Junction catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Junction''s developer surface includes changelog, authentication, developer portal, documentation, API reference, getting-started guide, developer console, and 86 more developer resources.'
plans:
- name: Junction Com Plans Pricing
  plan_count: 2
  slug: junction-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Junction Com Rate Limits
  slug: junction-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Junction — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: junction-com-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Junction API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 2
  slug: junction-com-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Junction — vital rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: vital-rules
score:
  band: exemplar
  composite: 73.2
  coverage:
    artifact_dirs: 37
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 35.6
    contract_quality: 70.2
    developer_ergonomics: 82.1
    discoverability: 70.0
    operational_transparency: 76.3
  previous_composite: 73.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/junction-com/junction-com-2026-06-20T201103.png
security:
- kind: authentication
  name: Junction Com Authentication
  slug: junction-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Junction Com Domain Security
  slug: junction-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Junction Com Trust Center
  slug: junction-com-trust-center
  summary_line: SOC 2, HITRUST CSF, HIPAA, NIST CSF
slug: junction-com
solutions:
- description: One API for the two hardest health-data integrations — wearables and labs — so a small team can ship a clinical-grade product without negotiating individual vendor contracts.
  name: For digital-health builders
- description: Add a software layer (ordering, results, patient app) over a managed nationwide lab network without building lab-vendor integrations or running a fulfillment ops team in-house.
  name: For diagnostics companies
- description: Replace per-device SDKs and OAuth flows with one Link Widget and one normalized timeseries + summary schema covering 300+ devices.
  name: For platforms adding wearable data
- description: SOC 2 Type 2, ISO 27001, HIPAA, GDPR-ready, US/EU regional deployments, white-label app branding, uptime SLAs, prioritized integrations, ETL pipelines, and Analytics API access on the Scale plan.
  name: For enterprises
tags:
- Health Data
- Wearables
- Lab Testing
- Digital Health
- Health Tech
- Healthcare
- HIPAA
- HealthKit
- Health Connect
- Electronic Health Records
- Biomarkers
- Diagnostics
- Continuous Glucose Monitoring
- Sleep
- Activity
- Heart Rate
- Webhook
- Phlebotomy
- Lab Orders
use_cases:
- description: Add wearable monitoring and ordering of standard lab panels to telehealth visits without integrating dozens of device APIs and lab vendors.
  name: Virtual-first / digital-health clinics
- description: White-label at-home testkits, deliver results in-app, and pair them with continuous wearable context (sleep, HRV, glucose) to drive coaching and lifestyle programs.
  name: Consumer diagnostics and wellness platforms
- description: Embed Junction as a labs-and-devices module inside an EHR/EMR product so customers get ordering, results, and wearable data without leaving the chart.
  name: EHR / EMR and healthcare SaaS providers
- description: Pull continuous-glucose-monitor data from Dexcom, Freestyle Libre, and Abbott LibreView; pair with lab biomarkers (HbA1c, lipid panel, fasting insulin); compute glucose-variability metrics with Sense.
  name: Cardiometabolic and CGM programs
- description: Normalized sleep, sleep-cycle, HRV, workout, and recovery data from Oura, Whoop, Garmin, Fitbit, Apple Watch, and 25+ other devices in one schema.
  name: Sleep, recovery, and performance apps
- description: Menstrual-cycle, basal-body-temperature, and hormone-panel lab data combined for cycle tracking and fertility coaching.
  name: Women's-health and fertility platforms
- description: Backfill historical wearable + lab data across thousands of users via bulk-import, bulk-pull, and historical-pull endpoints. Push to ETL pipelines for in-house analytics.
  name: Population-health and research cohorts
- description: Expose normalized wearable + lab data to AI agents (via Naftiko capabilities or MCP) so agents can reason over a patient's biomarkers, sleep, and activity without bespoke per-source adapters.
  name: AI agents over patient health data
website: https://www.junction.com/
---
