---
aid: dexcom
url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/apis.yml
name: Dexcom
tags:
  - Continuous Glucose Monitoring
  - Diabetes
  - Digital Health
  - Glucose
  - Healthcare
  - Medical Devices
  - Wearables
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: company
created: '2026-05-04'
modified: '2026-05-05'
description: Dexcom is a leading medical device company that develops, manufactures, and distributes continuous glucose monitoring (CGM) systems for people with diabetes. The company's wearable sensors stream real-time glucose data to mobile apps, dedicated receivers, and connected health platforms. Dexcom exposes a public developer program that lets approved third parties retrieve CGM data (estimated glucose values, events, calibrations, alerts, devices, and data range) through an OAuth 2.0 secured REST API, with a sandbox for development and a production environment for live patient data.
apis:
  - aid: dexcom:dexcom-api
    name: Dexcom Developer API
    humanURL: https://developer.dexcom.com/
    baseURL: https://api.dexcom.com
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - CGM
      - Glucose
      - Healthcare
      - REST
    properties:
      - type: Documentation
        url: https://developer.dexcom.com/
      - type: GettingStarted
        url: https://developer.dexcom.com/get-started
      - type: APIReference
        url: https://developer.dexcom.com/docs/dexcomv3/endpoint-overview
      - type: Authentication
        url: https://developer.dexcom.com/docs/dexcom/authentication/
      - type: Sandbox
        url: https://sandbox-api.dexcom.com
      - type: TermsOfService
        url: https://developer.dexcom.com/terms-of-use
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/openapi/dexcom-dexcom-api.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-egv-record-schema.json
        title: EGV Record Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-egvs-response-schema.json
        title: EGVs Response Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-event-record-schema.json
        title: Event Record Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-events-response-schema.json
        title: Events Response Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-calibration-record-schema.json
        title: Calibration Record Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-calibrations-response-schema.json
        title: Calibrations Response Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-alert-record-schema.json
        title: Alert Record Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-alerts-response-schema.json
        title: Alerts Response Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-alert-schedule-schema.json
        title: Alert Schedule Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-alert-setting-schema.json
        title: Alert Setting Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-device-record-schema.json
        title: Device Record Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-devices-response-schema.json
        title: Devices Response Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-data-range-moment-schema.json
        title: Data Range Moment Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-data-range-window-schema.json
        title: Data Range Window Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-data-range-response-schema.json
        title: Data Range Response Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-token-request-schema.json
        title: Token Request Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-token-response-schema.json
        title: Token Response Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-glucose-unit-schema.json
        title: Glucose Unit Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-rate-unit-schema.json
        title: Rate Unit Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-trend-type-schema.json
        title: Trend Type Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-egv-status-schema.json
        title: EGV Status Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-event-type-schema.json
        title: Event Type Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-event-status-schema.json
        title: Event Status Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-alert-name-schema.json
        title: Alert Name Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-alert-state-schema.json
        title: Alert State Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-transmitter-generation-schema.json
        title: Transmitter Generation Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-schema/dexcom-api-date-time-schema.json
        title: Date Time Schema
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-egv-record-structure.json
        title: EGV Record Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-egvs-response-structure.json
        title: EGVs Response Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-event-record-structure.json
        title: Event Record Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-events-response-structure.json
        title: Events Response Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-calibration-record-structure.json
        title: Calibration Record Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-calibrations-response-structure.json
        title: Calibrations Response Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-alert-record-structure.json
        title: Alert Record Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-alerts-response-structure.json
        title: Alerts Response Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-alert-schedule-structure.json
        title: Alert Schedule Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-alert-setting-structure.json
        title: Alert Setting Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-device-record-structure.json
        title: Device Record Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-devices-response-structure.json
        title: Devices Response Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-data-range-moment-structure.json
        title: Data Range Moment Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-data-range-window-structure.json
        title: Data Range Window Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-data-range-response-structure.json
        title: Data Range Response Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-token-request-structure.json
        title: Token Request Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-token-response-structure.json
        title: Token Response Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-glucose-unit-structure.json
        title: Glucose Unit Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-rate-unit-structure.json
        title: Rate Unit Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-trend-type-structure.json
        title: Trend Type Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-egv-status-structure.json
        title: EGV Status Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-event-type-structure.json
        title: Event Type Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-event-status-structure.json
        title: Event Status Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-alert-name-structure.json
        title: Alert Name Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-alert-state-structure.json
        title: Alert State Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-transmitter-generation-structure.json
        title: Transmitter Generation Structure
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-structure/dexcom-api-date-time-structure.json
        title: Date Time Structure
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-egv-record-example.json
        title: EGV Record Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-egvs-response-example.json
        title: EGVs Response Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-event-record-example.json
        title: Event Record Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-events-response-example.json
        title: Events Response Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-calibration-record-example.json
        title: Calibration Record Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-calibrations-response-example.json
        title: Calibrations Response Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-alert-record-example.json
        title: Alert Record Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-alerts-response-example.json
        title: Alerts Response Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-alert-schedule-example.json
        title: Alert Schedule Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-alert-setting-example.json
        title: Alert Setting Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-device-record-example.json
        title: Device Record Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-devices-response-example.json
        title: Devices Response Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-data-range-moment-example.json
        title: Data Range Moment Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-data-range-window-example.json
        title: Data Range Window Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-data-range-response-example.json
        title: Data Range Response Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-token-request-example.json
        title: Token Request Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-token-response-example.json
        title: Token Response Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-glucose-unit-example.json
        title: Glucose Unit Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-rate-unit-example.json
        title: Rate Unit Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-trend-type-example.json
        title: Trend Type Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-egv-status-example.json
        title: EGV Status Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-event-type-example.json
        title: Event Type Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-event-status-example.json
        title: Event Status Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-alert-name-example.json
        title: Alert Name Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-alert-state-example.json
        title: Alert State Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-transmitter-generation-example.json
        title: Transmitter Generation Example
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/examples/dexcom-api-date-time-example.json
        title: Date Time Example
    description: REST API for retrieving Dexcom continuous glucose monitoring data on behalf of authorized end users. Authentication is OAuth 2.0 authorization code flow; sandbox and production hosts are separate. Resources include estimated glucose values (EGVs), events, calibrations, alerts, devices, and data range. Intended for research, clinical, and consumer applications that integrate Dexcom CGM data with other digital health experiences.
common:
  - type: Website
    url: https://www.dexcom.com/
  - type: DeveloperPortal
    url: https://developer.dexcom.com/
  - type: Documentation
    url: https://developer.dexcom.com/
  - type: GettingStarted
    url: https://developer.dexcom.com/get-started
  - type: Authentication
    url: https://developer.dexcom.com/docs/dexcom/authentication/
  - type: Sandbox
    url: https://sandbox-api.dexcom.com
  - type: TermsOfService
    url: https://www.dexcom.com/terms-of-use
  - type: PrivacyPolicy
    url: https://www.dexcom.com/privacy-policy
  - type: Support
    url: https://www.dexcom.com/contact
  - type: GitHubOrganization
    url: https://github.com/dexcom
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/rules/dexcom-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/vocabulary/dexcom-vocabulary.yml
  - type: JSON-LD
    url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/json-ld/dexcom-context.jsonld
    title: Dexcom JSON-LD Context
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/capabilities/cgm-data-access.yaml
    title: CGM Data Access Workflow
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/dexcom/refs/heads/main/capabilities/shared/dexcom-api.yaml
    title: Dexcom Developer API (Shared)
  - type: Features
    data:
      - name: Continuous Glucose Monitoring Data
        description: Retrieve estimated glucose values (EGVs) at 5-minute intervals across G6, G7, Dexcom ONE, and ONE+ systems.
      - name: User-Entered Events
        description: Access user-logged carbs, insulin, exercise, and health events alongside CGM data.
      - name: Calibrations
        description: Read fingerstick BG meter calibration entries for transmitters that require them.
      - name: Alerts
        description: Read CGM display device alerts (high, low, urgent low, rise, fall, no readings, out-of-range).
      - name: Device Inventory
        description: List the user's transmitters and display devices, including alert schedules and settings.
      - name: Data Range
        description: Discover earliest and latest record times for efficient incremental sync.
      - name: Multi-Region Hosts
        description: Production hosts in the US (api.dexcom.com), EU (api.dexcom.eu), and Japan (api.dexcom.jp).
      - name: Sandbox Environment
        description: Test against simulated CGM data without real Dexcom credentials at sandbox-api.dexcom.com.
      - name: OAuth 2.0 Authorization Code
        description: Standards-based user consent and token issuance with offline_access (refresh) support.
  - type: UseCases
    data:
      - name: Diabetes Self-Management Apps
        description: Consumer apps that visualize glucose trends alongside insulin, food, and activity logs.
      - name: Clinical Decision Support
        description: Provider tools that aggregate CGM data into time-in-range and ambulatory glucose profile (AGP) views.
      - name: Clinical Research
        description: Studies analyzing glycemic patterns, intervention response, or device performance across cohorts.
      - name: Coaching and Behavior Change
        description: Health-coaching platforms correlating CGM signals with meals, workouts, and sleep.
      - name: AI-Assisted Glucose Management
        description: LLM and agentic systems that reason over CGM history via MCP tools to recommend actions.
      - name: Connected Health Platforms
        description: Aggregators (Apple Health, Validic, Tidepool, etc.) that ingest Dexcom data alongside other wearables.
  - type: Integrations
    data:
      - name: Apple Health
        description: Dexcom apps publish CGM data into Apple Health on iOS.
      - name: Tidepool
        description: Open diabetes data platform that ingests Dexcom data for clinical and research use.
      - name: Validic
        description: Healthcare data aggregator with documented Dexcom API integration.
      - name: Nightscout
        description: Community-maintained DIY CGM dashboard supporting Dexcom data flows.
      - name: Garmin / Fitbit / Wearables
        description: Companion apps and watch faces display Dexcom values streamed via Dexcom's apps.
  - type: Solutions
    data:
      - name: Dexcom G7
        description: Latest-generation 10-day all-in-one disposable CGM with the smallest, thinnest sensor and direct-to-watch streaming.
      - name: Dexcom G6
        description: 10-day CGM with separate transmitter and sensor; widely supported across partner integrations.
      - name: Dexcom ONE / ONE+
        description: Simplified CGM tier targeted at intermittent CGM users in select markets.
      - name: Dexcom Stelo
        description: Over-the-counter glucose biosensor for non-insulin users (US).
      - name: Clarity
        description: Cloud reporting for patients and clinicians with AGP, time-in-range, and pattern recognition.
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
specificationVersion: '0.19'
---
