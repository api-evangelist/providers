---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Appium Agentic Access
  operation_count: 32
  slug: appium-agentic-access
  summary_line: 32 operations · 18 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Standalone GUI inspector for mobile apps that communicates with an Appium server, enabling visual element inspection and XPath generation for test authoring.
  name: Appium Inspector
  slug: appium-inspector
- description: The primary Appium driver for Android automation, backed by Google's UiAutomator2 framework. Supports Android 5.0+ devices and emulators.
  name: Appium UiAutomator2 Driver
  slug: appium-uiautomator2-driver
- description: The primary Appium driver for iOS and tvOS automation, backed by Apple's XCTest framework. Supports iOS 12+ and macOS Sequoia.
  name: Appium XCUITest Driver
  slug: appium-xcuitest-driver
- description: W3C Actions API for complex input sequences
  name: Appium Actions API
  slug: appium-actions-api
- description: Dialog and alert handling
  name: Appium Alerts API
  slug: appium-alerts-api
- description: Appium-specific device commands (app management, files, keyboard)
  name: Appium Appium Device API
  slug: appium-appium-device-api
- description: Appium session settings and capabilities
  name: Appium Appium Session API
  slug: appium-appium-session-api
- description: Cookie management
  name: Appium Cookies API
  slug: appium-cookies-api
- description: Element discovery and interaction
  name: Appium Elements API
  slug: appium-elements-api
- description: Browser and app navigation commands
  name: Appium Navigation API
  slug: appium-navigation-api
- description: Screenshot capture
  name: Appium Screenshots API
  slug: appium-screenshots-api
- description: Server status and session listing
  name: Appium Server API
  slug: appium-server-api
- description: WebDriver session lifecycle management
  name: Appium Sessions API
  slug: appium-sessions-api
artifact_total: 69
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appium-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appium-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appium
- group: start
  title: ''
  type: GettingStarted
  url: https://appium.io/docs/en/latest/quickstart/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appium
- group: docs
  title: ''
  type: Documentation
  url: https://appium.io/docs/en/latest/
- group: operate
  title: ''
  type: Support
  url: https://discuss.appium.io/
- group: operate
  title: ''
  type: Slack
  url: http://appium.slack.com
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/appium
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/AppiumConf
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/appium/appium/blob/master/CHANGELOG.md
- group: build
  title: Python Client
  type: SDKs
  url: https://github.com/appium/python-client
- group: build
  title: Java Client
  type: SDKs
  url: https://github.com/appium/java-client
- group: build
  title: Ruby Client
  type: SDKs
  url: https://github.com/appium/ruby_lib_core
- group: build
  title: .NET Client
  type: SDKs
  url: https://github.com/appium/dotnet-client
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/appium/appium-mcp
- group: design
  title: ''
  type: SpectralRules
  url: rules/appium-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/appium-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/appium/appium-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/appium/skills
created: '2024-01-15'
description: Appium is an open-source test automation framework governed by the OpenJS Foundation, designed to facilitate UI automation of many app platforms including mobile (iOS, Android), browser (Chrome, Firefox, Safari), desktop (macOS, Windows), and TV (Roku, tvOS, Android TV). It implements the W3C WebDriver protocol and provides an extensible ecosystem of drivers, clients, and plugins.
examples:
- key_count: 4
  name: Appium Server Action Sequence Example
  slug: appium-server-action-sequence-example
- key_count: 3
  name: Appium Server App Id Request Example
  slug: appium-server-app-id-request-example
- key_count: 7
  name: Appium Server Cookie Example
  slug: appium-server-cookie-example
- key_count: 1
  name: Appium Server Error Response Example
  slug: appium-server-error-response-example
- key_count: 2
  name: Appium Server Find Element Request Example
  slug: appium-server-find-element-request-example
- key_count: 2
  name: Appium Server Session Info Example
  slug: appium-server-session-info-example
features:
- description: Automate iOS, Android, Windows, macOS, web browsers, and TV platforms from a single framework
  name: Multi-Platform Support
- description: Implements the W3C WebDriver protocol for standard, cross-platform automation
  name: WebDriver Protocol
- description: Plugin-based driver system supports any platform through community and official drivers
  name: Extensible Driver Architecture
- description: Official client libraries for Python, Java, JavaScript, Ruby, .NET, and more
  name: Multiple Language Clients
- description: Supports the next-generation WebDriver BiDi bidirectional protocol
  name: WebDriver BiDi Support
- description: Model Context Protocol server for AI-assisted test automation
  name: MCP Server
- description: Visual app inspector for element discovery and XPath/accessibility ID generation
  name: Inspector GUI
finops:
- name: Appium Finops
  service_category: Test Automation / WebDriver
  slug: appium-finops
image: https://appium.io/docs/en/latest/assets/images/appium-logo.png
integrations:
- description: Cloud device farm integration for running Appium tests on real devices
  name: BrowserStack
- description: Cloud testing platform with Appium support for real and virtual devices
  name: Sauce Labs
- description: Cloud test execution platform with Appium integration
  name: LambdaTest
- description: Java testing framework commonly used with Appium Java client
  name: TestNG
- description: Python testing framework used with the Appium Python client
  name: pytest
- description: JavaScript test automation framework with built-in Appium support
  name: WebdriverIO
- description: Distributed test execution grid compatible with Appium sessions
  name: Selenium Grid
json_schemas:
- name: ActionSequence
  property_count: 4
  slug: appium-server-action-sequence
- name: AppIdRequest
  property_count: 3
  slug: appium-server-app-id-request
- name: Cookie
  property_count: 7
  slug: appium-server-cookie
- name: ErrorResponse
  property_count: 1
  slug: appium-server-error-response
- name: FindElementRequest
  property_count: 2
  slug: appium-server-find-element-request
- name: SessionInfo
  property_count: 2
  slug: appium-server-session-info
json_structures:
- name: Appium Server Action Sequence Structure
  property_count: 4
  slug: appium-server-action-sequence-structure
- name: Appium Server App Id Request Structure
  property_count: 3
  slug: appium-server-app-id-request-structure
- name: Appium Server Cookie Structure
  property_count: 7
  slug: appium-server-cookie-structure
- name: Appium Server Error Response Structure
  property_count: 1
  slug: appium-server-error-response-structure
- name: Appium Server Find Element Request Structure
  property_count: 2
  slug: appium-server-find-element-request-structure
- name: Appium Server Session Info Structure
  property_count: 2
  slug: appium-server-session-info-structure
jsonld:
- class_count: 7
  name: Appium Server Context
  property_count: 15
  slug: appium-server-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Appium
nav: Providers
network: true
overview: 'Appium publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Alerts API, Appium Device API, and 7 more. Tagged areas include Android, Cross-Platform, iOS, Mobile Testing, and Open Source.


  The Appium catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Appium''s developer surface includes getting-started guide, documentation, support, Stack Overflow tag, YouTube channel, changelog, tooling, and 13 more developer resources.'
plans:
- name: Appium Plans Pricing
  plan_count: 1
  slug: appium-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Appium Rate Limits
  slug: appium-rate-limits
rules:
- name: Appium API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: appium-jsonschema-spectral-rules
- name: Appium API Rules
  rule_count: 30
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 18
  slug: appium-spectral-rules
score:
  band: developing
  composite: 49.4
  delta: -7.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 52.5
    developer_ergonomics: 47.8
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 57.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 10
      marker_coverage: 100.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/appium/refs/heads/main/screenshots/appium-2026-06-20T172316.png
security:
- kind: domain-security
  name: Appium Domain Security
  slug: appium-domain-security
  summary_line: TLSv1.2 · DMARC
skill_count: 10
skills:
- name: appium-troubleshooting
  slug: appium-troubleshooting
- name: environment-setup-android
  slug: environment-setup-android
- name: environment-setup-bundletool
  slug: environment-setup-bundletool
- name: environment-setup-chromium
  slug: environment-setup-chromium
- name: environment-setup-espresso
  slug: environment-setup-espresso
- name: environment-setup-ffmpeg
  slug: environment-setup-ffmpeg
- name: environment-setup-node
  slug: environment-setup-node
- name: environment-setup-uiautomator2
  slug: environment-setup-uiautomator2
- name: environment-setup-xcuitest
  slug: environment-setup-xcuitest
- name: xcuitest-real-device-config
  slug: xcuitest-real-device-config
slug: appium
tags:
- Android
- Cross-Platform
- iOS
- Mobile Testing
- Open Source
- OpenJS Foundation
- Test Automation
- WebDriver
use_cases:
- description: Automated functional and regression testing of iOS and Android native apps
  name: Mobile App Testing
- description: Single test codebase targeting multiple platforms and devices
  name: Cross-Platform Test Suites
- description: Running automated mobile tests in continuous integration pipelines
  name: CI/CD Integration
- description: Browser automation on mobile and desktop via WebDriver
  name: Web Automation
- description: Using the MCP server to enable AI agents to drive test execution
  name: AI-Assisted Testing
website: https://appium.io/apis.json
---
