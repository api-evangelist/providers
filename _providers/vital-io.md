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
  band: agent-native
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
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 147
  human_in_the_loop: 0
  name: Vital Io Agentic Access
  operation_count: 591
  slug: vital-io-agentic-access
  summary_line: 591 operations · 147 acting
api_count: 9
apis:
- description: Programmatically manage all Junction regional and global resources for your organization. Authenticated with a separate x-vital-management-api-key, this API governs organizations, teams (create, updat
  name: Vital Management API
  slug: vital-management-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The Aggregate API from Vital — 3 operation(s) for aggregate.
  name: Vital Aggregate API
  slug: vital-io-aggregate-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The compendium API from Vital — 2 operation(s) for compendium.
  name: Vital compendium API
  slug: vital-io-compendium-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The insurance API from Vital — 3 operation(s) for insurance.
  name: Vital insurance API
  slug: vital-io-insurance-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The introspect API from Vital — 2 operation(s) for introspect.
  name: Vital introspect API
  slug: vital-io-introspect-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The lab_account API from Vital — 1 operation(s) for lab_account.
  name: Vital lab_account API
  slug: vital-io-lab-account-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The lab_report API from Vital — 2 operation(s) for lab_report.
  name: Vital lab_report API
  slug: vital-io-lab-report-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The lab_tests API from Vital — 9 operation(s) for lab_tests.
  name: Vital lab_tests API
  slug: vital-io-lab-tests-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The link API from Vital — 13 operation(s) for link.
  name: Vital link API
  slug: vital-io-link-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The order API from Vital — 32 operation(s) for order.
  name: Vital order API
  slug: vital-io-order-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The order_transaction API from Vital — 3 operation(s) for order_transaction.
  name: Vital order_transaction API
  slug: vital-io-order-transaction-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The orders API from Vital — 1 operation(s) for orders.
  name: Vital orders API
  slug: vital-io-orders-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The payor API from Vital — 1 operation(s) for payor.
  name: Vital payor API
  slug: vital-io-payor-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The providers API from Vital — 1 operation(s) for providers.
  name: Vital providers API
  slug: vital-io-providers-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The summary API from Vital — 15 operation(s) for summary.
  name: Vital summary API
  slug: vital-io-summary-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The team API from Vital — 5 operation(s) for team.
  name: Vital team API
  slug: vital-io-team-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The timeseries API from Vital — 80 operation(s) for timeseries.
  name: Vital timeseries API
  slug: vital-io-timeseries-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The user API from Vital — 16 operation(s) for user.
  name: Vital user API
  slug: vital-io-user-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The aggregation API from Vital — 0 operation(s) for aggregation.
  name: Vital Aggregation API
  slug: vital-io-aggregation-api
- baseURL: https://api.us.junction.com
  baseurl_source: declared
  description: The lab-testing API from Vital — 0 operation(s) for lab-testing.
  name: Vital Lab Testing API
  slug: vital-io-lab-testing-api
arazzos:
- description: Confirm phlebotomy coverage for an address, place an at-home order, find a slot, and book it.
  name: Vital Schedule an At-Home Phlebotomy Draw
  slug: vital-io-at-home-phlebotomy-booking-workflow
- description: Poll an existing order until it completes, then pull its result metadata and raw results.
  name: Vital Await Lab Order Completion and Retrieve Results
  slug: vital-io-await-order-results-workflow
- description: List your team's lab tests, fetch one in detail, and enumerate its biomarkers.
  name: Vital Browse Lab Tests and Inspect Markers
  slug: vital-io-browse-lab-tests-markers-workflow
- description: Cancel an order, confirm the cancellation, then mint a communications portal URL deeplinked to it.
  name: Vital Cancel a Lab Order and Send the User a Portal Link
  slug: vital-io-cancel-order-notify-portal-workflow
- description: Place an order set lab order for a user and poll its lifecycle status until it completes, cancels, or fails.
  name: Vital Create a Lab Order and Poll Until Resolved
  slug: vital-io-create-order-poll-status-workflow
- description: Create a user, attach a demo provider, then confirm the connection landed on the user record.
  name: Vital Connect a Demo Provider and Verify Connected Sources
  slug: vital-io-demo-connection-verify-sources-workflow
- description: Create a Vital user, mint a mobile sign-in token, and read back the user's connected providers.
  name: Vital Provision a User and Hand Off a Mobile Sign-In Token
  slug: vital-io-mobile-signin-token-handoff-workflow
- description: Create a Vital user, mint a Link token, and surface the available providers to connect.
  name: Vital Onboard a User and Connect a Wearable
  slug: vital-io-onboard-user-connect-wearable-workflow
- description: Create an unregistered testkit order, register it against a sample, then read the order back.
  name: Vital Create and Register a Lab Testkit Order
  slug: vital-io-testkit-order-register-workflow
- description: Resolve a user by client_user_id, list their devices, and fetch the first device in detail.
  name: Vital Inventory a User's Connected Devices
  slug: vital-io-user-device-inventory-workflow
artifact_total: 125
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
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vital Lab Report Parser Aggregate API
  slug: open-vital-io-aggregate-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate compendium API
  slug: open-vital-io-compendium-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate insurance API
  slug: open-vital-io-insurance-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate introspect API
  slug: open-vital-io-introspect-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate lab_account API
  slug: open-vital-io-lab-account-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate lab_report API
  slug: open-vital-io-lab-report-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate lab_tests API
  slug: open-vital-io-lab-tests-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate link API
  slug: open-vital-io-link-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate order API
  slug: open-vital-io-order-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate order_transaction API
  slug: open-vital-io-order-transaction-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate orders API
  slug: open-vital-io-orders-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate payor API
  slug: open-vital-io-payor-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate providers API
  slug: open-vital-io-providers-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate summary API
  slug: open-vital-io-summary-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate team API
  slug: open-vital-io-team-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate timeseries API
  slug: open-vital-io-timeseries-api
- collection_type: open
  name: Vital Lab Report Parser Aggregate user API
  slug: open-vital-io-user-api
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vital-io-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vital-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vital-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vital-io-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vital/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vital-io-at-home-phlebotomy-booking-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vital-io-await-order-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vital-io-browse-lab-tests-markers-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vital-io-cancel-order-notify-portal-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vital-io-create-order-poll-status-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vital-io-demo-connection-verify-sources-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vital-io-mobile-signin-token-handoff-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vital-io-onboard-user-connect-wearable-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vital-io-testkit-order-register-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vital-io-user-device-inventory-workflow.yml
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
  title: ''
  type: OpenAPI
  url: openapi/_original/vital-openapi-original.json
- group: docs
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
  title: ''
  type: SpectralRules
  url: rules/vital-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vital-io-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vital-io-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/vital-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vital-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vital-io-finops.yml
- group: company
  title: ''
  type: Website
  url: https://vital.io/
- group: docs
  title: ''
  type: Documentation
  url: https://vital.io/help/en/collections/19470958-integration-guide
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
  title: ''
  type: Lifecycle
  url: lifecycle/vital-io-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vital-io-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/vital-io-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vital-io-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vital-io-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vital-io-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vital-io-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/vital-io-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vital-io-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vital-io-domain-security.yml
created: '2026-05-25'
description: Vital (now operating as Junction, formerly tryVital) is a health-data API platform that gives digital-health, virtual-care, diagnostics, wellness, and EHR/EMR builders a single integration to wearable-device data and nationwide lab testing. Connect 300+ wearables and health devices — Apple HealthKit, Android Health Connect, Oura, Whoop, Garmin, Fitbit, Withings, Dexcom, Freestyle Libre, Withings, Polar, and the rest — through the Vital Link Widget; ingest normalized daily summaries and per-sample timeseries for sleep, activity, body, workouts, heart rate, HRV, glucose, blood pressure, SpO2, ECG, and menstrual cycle; order at-home testkits, at-home phlebotomy, walk-in / Patient Service Center lab collection, and on-site collection across all 50 U.S. states; retrieve structured biomarker results; and run Junction Sense continuous queries to turn raw data into clinically actionable insights. Backed by SOC 2 Type 2, ISO 27001, GDPR-ready, and HIPAA-compliant infrastructure with
  both US and EU regional deployments.
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
  name: Vital Link Widget and Connect app
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
- name: Vital Io Finops
  service_category: ''
  slug: vital-io-finops
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
  name: Vital Io Context
  property_count: 9
  slug: vital-io-context
layout: provider
modified: '2026-05-25'
name: Vital
nav: Providers
network: true
overview: 'Vital publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Aggregate API, compendium API, insurance API, and 16 more. Tagged areas include Health Data, Wearables, Lab Testing, Digital Health, and Health Tech.


  The Vital catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vital''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, developer console, signup flow, and 70 more developer resources.'
plans:
- name: Vital Io Plans Pricing
  plan_count: 4
  slug: vital-io-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Vital Io Rate Limits
  slug: vital-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Vital API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vital-io-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Vital API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: vital-rules
score:
  band: exemplar
  composite: 70.8
  coverage:
    artifact_dirs: 22
    catalog_gap: 55.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 47.0
    contract_quality: 60.2
    developer_ergonomics: 85.7
    discoverability: 50.0
    governance: 47.0
    operational_transparency: 39.5
  previous_composite: 70.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vital-io/refs/heads/main/screenshots/vital-io-2026-06-20T201103.png
security:
- kind: authentication
  name: Vital Io Authentication
  slug: vital-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vital Io Domain Security
  slug: vital-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vital Io Trust Center
  slug: vital-io-trust-center
  summary_line: SOC 2, HITRUST CSF, HIPAA, NIST CSF
slug: vital-io
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
- EHR
- EMR
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
website: https://vital.io/
---
