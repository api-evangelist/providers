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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Chrome Agentic Access
  operation_count: 18
  slug: google-chrome-agentic-access
  summary_line: 18 operations · 2 acting
api_count: 15
apis:
- description: APIs for building Chrome browser extensions.
  name: Chrome Extensions API
  slug: chrome-extensions-api
- description: Instrument, inspect, debug and profile Chromium, Chrome and other Blink-based browsers.
  name: Chrome DevTools Protocol
  slug: chrome-devtools-protocol
- description: API for publishing and managing extensions in the Chrome Web Store.
  name: Chrome Web Store API
  slug: chrome-web-store-api
- description: Access real-world user experience data for popular websites.
  name: Chrome User Experience Report API
  slug: chrome-user-experience-report-api
- description: API for programmatically viewing and managing Chrome policies assigned to Organizational Units.
  name: Chrome Policy API
  slug: chrome-policy-api
- description: API to cryptographically verify that ChromeOS clients are genuine and conform to corporate policy.
  name: Chrome Verified Access API
  slug: chrome-verified-access-api
- description: API to check URLs against Google lists of unsafe web resources including phishing and malware sites.
  name: Google Safe Browsing API
  slug: google-safe-browsing-api
- description: API to measure web page performance and receive optimization suggestions using Lighthouse and CrUX data.
  name: PageSpeed Insights API
  slug: pagespeed-insights-api
- description: On-device AI APIs powered by Gemini Nano built into Chrome for text generation, summarization, translation, and more.
  name: Chrome Built-in AI APIs
  slug: chrome-built-in-ai-apis
- description: Operations for retrieving information about Chrome apps, extensions, and Android apps available to managed devices.
  name: Google Chrome App Details API
  slug: google-chrome-app-details-api
- description: Operations for generating reports about browsers, devices, installed apps, extensions, and app usage within the enterprise.
  name: Google Chrome Reports API
  slug: google-chrome-reports-api
- description: Operations for retrieving telemetry data from managed ChromeOS devices including hardware specs, OS version, CPU, memory, storage, and network information.
  name: Google Chrome Telemetry Devices API
  slug: google-chrome-telemetry-devices-api
- description: Operations for listing telemetry events from managed ChromeOS devices such as USB peripherals, audio, network state changes, and hardware status events.
  name: Google Chrome Telemetry Events API
  slug: google-chrome-telemetry-events-api
- description: Operations for managing telemetry notification configurations that enable push notifications for telemetry events.
  name: Google Chrome Telemetry Notification Configs API
  slug: google-chrome-telemetry-notification-configs-api
- description: Operations for retrieving telemetry information associated with managed users on ChromeOS devices.
  name: Google Chrome Telemetry Users API
  slug: google-chrome-telemetry-users-api
artifact_total: 88
collections:
- collection_type: open
  name: Google Chrome Management API
  slug: open-google-chrome-management-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-chrome-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-chrome-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-chrome-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-chrome-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-chrome
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.chrome.com/
- group: company
  title: ''
  type: Blog
  url: https://developer.chrome.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleChrome
- group: other
  title: ''
  type: X
  url: https://twitter.com/ChromiumDev
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/GoogleChromeDevelopers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.chrome.com/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.chrome.com/new
- group: operate
  title: ''
  type: StatusPage
  url: https://chromestatus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.chrome.com/origintrials/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.chrome.com/docs/web-platform/origin-trials
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/google-chrome-extension
- group: start
  title: ''
  type: Portal
  url: https://chromeenterprise.google/
- group: other
  title: ''
  type: Resources
  url: https://source.chromium.org/chromium
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/google-chrome-extension-manifest-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-chrome-context.jsonld
created: '2024'
description: Collection of APIs and resources for the Google Chrome browser and Chrome platform.
features:
- Chrome Extensions Manifest V3 platform
- Chrome DevTools Protocol for browser automation
- Chrome Web Store publishing and management APIs
- Enterprise device and policy management
- Real user experience metrics (CrUX)
- Safe Browsing URL threat detection
- PageSpeed Insights performance analysis
- Built-in AI APIs (Gemini Nano)
- Verified Access for ChromeOS device attestation
finops:
- name: Google Chrome Finops
  service_category: Browser / Developer Tools
  slug: google-chrome-finops
image: https://www.google.com/chrome/static/images/chrome-logo.svg
integrations:
- Google Workspace Admin
- Google Cloud
- Puppeteer
- Playwright
- Selenium
- BigQuery
- Lighthouse
- Google Search Console
json_schemas:
- name: AndroidAppInfo
  property_count: 3
  slug: google-chrome-androidappinfo
- name: AudioStatusReport
  property_count: 7
  slug: google-chrome-audiostatusreport
- name: BatteryInfo
  property_count: 6
  slug: google-chrome-batteryinfo
- name: BatteryStatusReport
  property_count: 8
  slug: google-chrome-batterystatusreport
- name: BootPerformanceReport
  property_count: 6
  slug: google-chrome-bootperformancereport
- name: ChromeAppInfo
  property_count: 21
  slug: google-chrome-chromeappinfo
- name: CountChromeBrowsersNeedingAttentionResponse
  property_count: 4
  slug: google-chrome-countchromebrowsersneedingattentionresponse
- name: CountChromeDevicesReachingAutoExpirationDateResponse
  property_count: 1
  slug: google-chrome-countchromedevicesreachingautoexpirationdateresponse
- name: CountChromeDevicesThatNeedOsUpdateResponse
  property_count: 1
  slug: google-chrome-countchromedevicesthatneedosupdateresponse
- name: CountChromeHardwareFleetDevicesResponse
  property_count: 4
  slug: google-chrome-countchromehardwarefleetdevicesresponse
- name: CountChromeVersionsResponse
  property_count: 3
  slug: google-chrome-countchromeversionsresponse
- name: CountInstalledAppsResponse
  property_count: 3
  slug: google-chrome-countinstalledappsresponse
- name: CpuInfo
  property_count: 5
  slug: google-chrome-cpuinfo
- name: CpuStatusReport
  property_count: 4
  slug: google-chrome-cpustatusreport
- name: Chrome Extension Manifest (Manifest V3)
  property_count: 41
  slug: google-chrome-extension-manifest
- name: FindInstalledAppDevicesResponse
  property_count: 3
  slug: google-chrome-findinstalledappdevicesresponse
- name: GoogleRpcStatus
  property_count: 3
  slug: google-chrome-googlerpcstatus
- name: GraphicsInfo
  property_count: 2
  slug: google-chrome-graphicsinfo
- name: GraphicsStatusReport
  property_count: 2
  slug: google-chrome-graphicsstatusreport
- name: HeartbeatStatusReport
  property_count: 2
  slug: google-chrome-heartbeatstatusreport
- name: ListTelemetryDevicesResponse
  property_count: 2
  slug: google-chrome-listtelemetrydevicesresponse
- name: ListTelemetryEventsResponse
  property_count: 2
  slug: google-chrome-listtelemetryeventsresponse
- name: ListTelemetryNotificationConfigsResponse
  property_count: 2
  slug: google-chrome-listtelemetrynotificationconfigsresponse
- name: ListTelemetryUsersResponse
  property_count: 2
  slug: google-chrome-listtelemetryusersresponse
- name: MemoryInfo
  property_count: 3
  slug: google-chrome-memoryinfo
- name: MemoryStatusReport
  property_count: 4
  slug: google-chrome-memorystatusreport
- name: NetworkDiagnosticsReport
  property_count: 2
  slug: google-chrome-networkdiagnosticsreport
- name: NetworkInfo
  property_count: 1
  slug: google-chrome-networkinfo
- name: NetworkStatusReport
  property_count: 11
  slug: google-chrome-networkstatusreport
- name: OsUpdateStatus
  property_count: 6
  slug: google-chrome-osupdatestatus
- name: PeripheralsReport
  property_count: 2
  slug: google-chrome-peripheralsreport
- name: StorageInfo
  property_count: 3
  slug: google-chrome-storageinfo
- name: StorageStatusReport
  property_count: 2
  slug: google-chrome-storagestatusreport
- name: TelemetryDevice
  property_count: 23
  slug: google-chrome-telemetrydevice
- name: TelemetryEvent
  property_count: 9
  slug: google-chrome-telemetryevent
- name: TelemetryNotificationConfig
  property_count: 4
  slug: google-chrome-telemetrynotificationconfig
- name: TelemetryUser
  property_count: 6
  slug: google-chrome-telemetryuser
- name: WebAppInfo
  property_count: 2
  slug: google-chrome-webappinfo
json_structures:
- name: Google Chrome Structure
  property_count: 0
  slug: google-chrome-structure
jsonld:
- class_count: 7
  name: Google Chrome Context
  property_count: 19
  slug: google-chrome-context
layout: provider
modified: '2026-05-19'
name: Google Chrome
nav: Providers
network: true
overview: 'Google Chrome publishes 6 APIs on the [APIs.io](https://apis.io/) network, including App Details API, Reports API, Telemetry Devices API, and 3 more. Tagged areas include Browser, Chrome Extensions, Developer Tools, and Web Platform.


  The Google Chrome catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Chrome''s developer surface includes authentication, engineering blog, YouTube channel, release notes, changelog, documentation, Stack Overflow tag, and 15 more developer resources.'
plans:
- name: Google Chrome Plans Pricing
  plan_count: 4
  slug: google-chrome-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 7
  name: Google Chrome Rate Limits
  slug: google-chrome-rate-limits
rules:
- name: Google Chrome API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-chrome-jsonschema-spectral-rules
scopes:
- name: Google Chrome Scopes
  scope_count: 3
  slug: google-chrome-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 56.2
  delta: -2.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 70.6
    developer_ergonomics: 30.4
    discoverability: 44.4
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 58.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-chrome/refs/heads/main/screenshots/google-chrome-2026-06-20T182034.png
security:
- kind: authentication
  name: Google Chrome Authentication
  slug: google-chrome-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Chrome Domain Security
  slug: google-chrome-domain-security
  summary_line: TLSv1.3 · DMARC
slug: google-chrome
tags:
- Browser
- Chrome Extensions
- Developer Tools
- Web Platform
use_cases:
- Building and publishing Chrome browser extensions
- Automating browser testing and debugging
- Managing Chrome enterprise deployments at scale
- Monitoring web performance with real user metrics
- Protecting users from phishing and malware URLs
- Running on-device AI inference in the browser
- Enforcing Chrome policies across organizational units
website: https://developer.chrome.com/
---
