---
name: Appium
description: Appium is an open-source test automation framework governed by the OpenJS Foundation, designed to facilitate UI automation of many app platforms including mobile (iOS, Android), browser (Chrome, Firefox, Safari), desktop (macOS, Windows), and TV (Roku, tvOS, Android TV). It implements the W3C WebDriver protocol and provides an extensible ecosystem of drivers, clients, and plugins.
image: https://appium.io/docs/en/latest/assets/images/appium-logo.png
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.18'
url: https://appium.io/apis.json
apis:
  - name: Appium Server API
    description: The main Appium server API that implements the W3C WebDriver protocol for mobile, web, desktop, and TV app automation. Supports session management, element interaction, actions, screenshots, and Appium-specific device commands.
    image: https://appium.io/docs/en/latest/assets/images/appium-logo.png
    humanURL: https://appium.io/
    baseURL: http://localhost:4723
    tags:
      - Android
      - Automation
      - iOS
      - Mobile Testing
      - WebDriver
    properties:
      - type: Documentation
        url: https://appium.io/docs/en/latest/
      - type: OpenAPI
        url: openapi/appium-server-openapi.yaml
      - type: GitHubRepository
        url: https://github.com/appium/appium
      - type: APIReference
        url: https://appium.io/docs/en/latest/reference/
      - type: JSONSchema
        url: json-schema/appium-server-session-info-schema.json
        title: Session Info Schema
      - type: JSONSchema
        url: json-schema/appium-server-find-element-request-schema.json
        title: Find Element Request Schema
      - type: JSONSchema
        url: json-schema/appium-server-app-id-request-schema.json
        title: App ID Request Schema
      - type: JSONSchema
        url: json-schema/appium-server-action-sequence-schema.json
        title: Action Sequence Schema
      - type: JSONSchema
        url: json-schema/appium-server-cookie-schema.json
        title: Cookie Schema
      - type: JSONSchema
        url: json-schema/appium-server-error-response-schema.json
        title: Error Response Schema
  - name: Appium Inspector
    description: Standalone GUI inspector for mobile apps that communicates with an Appium server, enabling visual element inspection and XPath generation for test authoring.
    humanURL: https://github.com/appium/appium-inspector
    baseURL: https://github.com/appium/appium-inspector/releases
    tags:
      - Debugging
      - GUI
      - Inspector
      - Mobile Testing
    properties:
      - type: GitHubRepository
        url: https://github.com/appium/appium-inspector
      - type: SDK
        url: https://github.com/appium/appium-inspector/releases
        title: Desktop App Downloads
  - name: Appium UiAutomator2 Driver
    description: The primary Appium driver for Android automation, backed by Google's UiAutomator2 framework. Supports Android 5.0+ devices and emulators.
    humanURL: https://github.com/appium/appium-uiautomator2-driver
    baseURL: http://localhost:4723
    tags:
      - Android
      - Automation
      - Driver
      - Mobile Testing
    properties:
      - type: GitHubRepository
        url: https://github.com/appium/appium-uiautomator2-driver
      - type: Documentation
        url: https://github.com/appium/appium-uiautomator2-driver#readme
  - name: Appium XCUITest Driver
    description: The primary Appium driver for iOS and tvOS automation, backed by Apple's XCTest framework. Supports iOS 12+ and macOS Sequoia.
    humanURL: https://github.com/appium/appium-xcuitest-driver
    baseURL: http://localhost:4723
    tags:
      - Automation
      - Driver
      - iOS
      - Mobile Testing
      - tvOS
    properties:
      - type: GitHubRepository
        url: https://github.com/appium/appium-xcuitest-driver
      - type: Documentation
        url: https://github.com/appium/appium-xcuitest-driver#readme
maintainers:
  - FN: Appium Contributors
    email: appium@googlegroups.com
    url: https://github.com/appium/appium/graphs/contributors
tags:
  - Android
  - Cross-Platform
  - iOS
  - Mobile Testing
  - Open Source
  - OpenJS Foundation
  - Test Automation
  - WebDriver
common:
  - type: GettingStarted
    url: https://appium.io/docs/en/latest/quickstart/
  - type: GitHubOrganization
    url: https://github.com/appium
  - type: Documentation
    url: https://appium.io/docs/en/latest/
  - type: Support
    url: https://discuss.appium.io/
  - type: Slack
    url: http://appium.slack.com
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/appium
  - type: YouTube
    url: https://www.youtube.com/c/AppiumConf
  - type: ChangeLog
    url: https://github.com/appium/appium/blob/master/CHANGELOG.md
  - type: SDK
    url: https://github.com/appium/python-client
    title: Python Client
  - type: SDK
    url: https://github.com/appium/java-client
    title: Java Client
  - type: SDK
    url: https://github.com/appium/ruby_lib_core
    title: Ruby Client
  - type: SDK
    url: https://github.com/appium/dotnet-client
    title: .NET Client
  - type: Tools
    url: https://github.com/appium/appium-mcp
    title: MCP Server
  - type: SpectralRules
    url: rules/appium-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/appium-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/appium-server.yaml
    title: Appium Server Shared Capability
  - type: NaftikoCapability
    url: capabilities/mobile-test-automation.yaml
    title: Mobile Test Automation Workflow
  - type: Features
    data:
      - name: Multi-Platform Support
        description: Automate iOS, Android, Windows, macOS, web browsers, and TV platforms from a single framework
      - name: WebDriver Protocol
        description: Implements the W3C WebDriver protocol for standard, cross-platform automation
      - name: Extensible Driver Architecture
        description: Plugin-based driver system supports any platform through community and official drivers
      - name: Multiple Language Clients
        description: Official client libraries for Python, Java, JavaScript, Ruby, .NET, and more
      - name: WebDriver BiDi Support
        description: Supports the next-generation WebDriver BiDi bidirectional protocol
      - name: MCP Server
        description: Model Context Protocol server for AI-assisted test automation
      - name: Inspector GUI
        description: Visual app inspector for element discovery and XPath/accessibility ID generation
  - type: UseCases
    data:
      - name: Mobile App Testing
        description: Automated functional and regression testing of iOS and Android native apps
      - name: Cross-Platform Test Suites
        description: Single test codebase targeting multiple platforms and devices
      - name: CI/CD Integration
        description: Running automated mobile tests in continuous integration pipelines
      - name: Web Automation
        description: Browser automation on mobile and desktop via WebDriver
      - name: AI-Assisted Testing
        description: Using the MCP server to enable AI agents to drive test execution
  - type: Integrations
    data:
      - name: BrowserStack
        description: Cloud device farm integration for running Appium tests on real devices
      - name: Sauce Labs
        description: Cloud testing platform with Appium support for real and virtual devices
      - name: LambdaTest
        description: Cloud test execution platform with Appium integration
      - name: TestNG
        description: Java testing framework commonly used with Appium Java client
      - name: pytest
        description: Python testing framework used with the Appium Python client
      - name: WebdriverIO
        description: JavaScript test automation framework with built-in Appium support
      - name: Selenium Grid
        description: Distributed test execution grid compatible with Appium sessions
---
