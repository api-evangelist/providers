---
aid: browserstack
url: https://raw.githubusercontent.com/api-evangelist/browserstack/refs/heads/main/apis.yml
apis:
- aid: browserstack:browserstack
  name: BrowserStack
  tags: []
  humanURL: ' https://www.browserstack.com/'
  properties:
  - url: ' https://www.browserstack.com/'
    type: Documentation
  description: Give your users a seamless experience by testing on 20,000 real devices.Dont compromise with emulators and simulators.
- aid: browserstack:automate-api
  name: BrowserStack Automate API
  tags:
  - Automation
  - Cross-Browser Testing
  - Selenium
  - Testing
  humanURL: https://www.browserstack.com/docs/automate/api-reference/selenium/introduction
  properties:
  - url: https://www.browserstack.com/docs/automate/api-reference/selenium/introduction
    type: Documentation
  - url: https://www.browserstack.com/docs/automate/api-reference/selenium/introduction#authentication
    type: Authentication
  - url: https://www.browserstack.com/docs/automate/api-reference/selenium/automate-api
    type: Reference
  - url: https://www.browserstack.com/docs/automate/selenium
    type: Getting Started
  description: The BrowserStack Automate REST API provides access to plan, project, build, and session details for Selenium-based automated testing on real browsers and devices. It enables managing test sessions, retrieving logs, and integrating CI/CD pipelines with BrowserStack Automate.
- aid: browserstack:app-automate-api
  name: BrowserStack App Automate API
  tags:
  - Appium
  - Automation
  - Espresso
  - Mobile Testing
  - XCUITest
  humanURL: https://www.browserstack.com/docs/app-automate/api-reference/introduction
  properties:
  - url: https://www.browserstack.com/docs/app-automate/api-reference/introduction
    type: Documentation
  - url: https://www.browserstack.com/docs/app-automate/api-reference/authentication
    type: Authentication
  - url: https://www.browserstack.com/docs/app-automate/appium
    type: Getting Started
  description: The BrowserStack App Automate REST API enables running mobile automation tests and integrating CI/CD pipelines with BrowserStack. It supports Appium, Espresso, XCUITest, Flutter, Detox, and Maestro frameworks for testing native and hybrid apps on real devices.
- aid: browserstack:screenshots-api
  name: BrowserStack Screenshots API
  tags:
  - Cross-Browser Testing
  - Screenshots
  - Visual Testing
  humanURL: https://www.browserstack.com/screenshots/api
  properties:
  - url: https://www.browserstack.com/screenshots/api
    type: Documentation
  description: The BrowserStack Screenshots API enables headless screenshot creation for any URL across 3000+ real browser and OS combinations. It supports generating, managing, and retrieving screenshots via REST endpoints.
- aid: browserstack:app-live-api
  name: BrowserStack App Live API
  tags:
  - Applications
  - Mobile Testing
  humanURL: https://www.browserstack.com/app-live/rest-api
  properties:
  - url: https://www.browserstack.com/app-live/rest-api
    type: Documentation
  description: The BrowserStack App Live REST API supports uploading, viewing, and deleting mobile apps via command line or automation scripts. It enables managing .apk, .aab, and .ipa files for manual testing on real devices.
- aid: browserstack:local-testing-api
  name: BrowserStack Local Testing API
  tags:
  - Debugging
  - Local Testing
  - Networking
  humanURL: https://www.browserstack.com/docs/local-testing/api
  properties:
  - url: https://www.browserstack.com/docs/local-testing/api
    type: Documentation
  description: The BrowserStack Local Testing API helps manage and debug multiple Local Testing connections. It provides endpoints to list active binary instances, retrieve instance details, and disconnect running binaries.
- aid: browserstack:automate-turboscale-api
  name: BrowserStack Automate TurboScale API
  tags:
  - Automation
  - Scaling
  - Selenium
  humanURL: https://www.browserstack.com/docs/automate-turboscale/api-reference/introduction
  properties:
  - url: https://www.browserstack.com/docs/automate-turboscale/api-reference/introduction
    type: Documentation
  - url: https://www.browserstack.com/docs/automate-turboscale
    type: Getting Started
  description: The BrowserStack Automate TurboScale REST API provides access to projects, builds, sessions, grids, and browser information for tests run on BrowserStack TurboScale infrastructure, including self-hosted grid management.
- aid: browserstack:test-management-api
  name: BrowserStack Test Management API
  tags:
  - QA
  - Test Management
  - Testing
  humanURL: https://www.browserstack.com/docs/test-management/api-reference/introduction
  properties:
  - url: https://www.browserstack.com/docs/test-management/api-reference/introduction
    type: Documentation
  - url: https://www.browserstack.com/docs/test-management/api-reference/authentication
    type: Authentication
  - url: https://www.browserstack.com/docs/test-management/api-reference/rate-limit-for-api-calls
    type: Rate Limits
  description: The BrowserStack Test Management API provides REST access to manage test projects, folders, test cases, test runs, test plans, test results, attachments, configurations, and custom fields for organizing and executing quality assurance workflows.
- aid: browserstack:test-reporting-and-analytics-api
  name: BrowserStack Test Reporting and Analytics API
  tags:
  - Analytics
  - Observability
  - Reporting
  - Testing
  humanURL: https://www.browserstack.com/docs/test-reporting-and-analytics/api-reference
  properties:
  - url: https://www.browserstack.com/docs/test-reporting-and-analytics/api-reference
    type: Documentation
  - url: https://www.browserstack.com/docs/test-reporting-and-analytics/api
    type: Reference
  description: The BrowserStack Test Reporting and Analytics API provides programmatic access to upload JUnit XML and Allure reports, manage projects and builds, retrieve test executions, and check Quality Gate status for automated quality workflows.
- aid: browserstack:accessibility-testing-api
  name: BrowserStack Accessibility Testing API
  tags:
  - Accessibility
  - Testing
  - WCAG
  humanURL: https://www.browserstack.com/docs/accessibility/api-reference
  properties:
  - url: https://www.browserstack.com/docs/accessibility/api-reference
    type: Documentation
  - url: https://www.browserstack.com/docs/accessibility/api/authentication
    type: Authentication
  - url: https://www.browserstack.com/docs/accessibility/api
    type: Reference
  - url: https://www.browserstack.com/docs/accessibility/overview/introduction
    type: Getting Started
  description: The BrowserStack Accessibility Testing API provides REST access to workflow analyzer, assisted tests, website scanner, and automated tests results for identifying and managing accessibility issues across web applications.
- aid: browserstack:percy-api
  name: BrowserStack Percy API
  tags:
  - Regression Testing
  - Screenshots
  - Visual Testing
  humanURL: https://www.browserstack.com/docs/percy/api-reference/percy-apis
  properties:
  - url: https://www.browserstack.com/docs/percy/api-reference/percy-apis
    type: Documentation
  - url: https://www.browserstack.com/docs/percy
    type: Getting Started
  description: The BrowserStack Percy API provides REST access for managing visual testing projects, builds, snapshots, Visual Git synchronization, and Visual Scanner capabilities to detect visual regressions across browsers and screen widths.
- aid: browserstack:app-percy-api
  name: BrowserStack App Percy API
  tags:
  - Mobile Testing
  - Regression Testing
  - Visual Testing
  humanURL: https://www.browserstack.com/docs/app-percy/api-reference/authentication
  properties:
  - url: https://www.browserstack.com/docs/app-percy/api-reference/authentication
    type: Documentation
  - url: https://www.browserstack.com/docs/app-percy/api-reference/authentication
    type: Authentication
  - url: https://www.browserstack.com/docs/app-percy/references/overview
    type: Reference
  - url: https://www.browserstack.com/docs/app-percy
    type: Getting Started
  description: The BrowserStack App Percy API provides automated visual testing for mobile applications across real iOS and Android devices, enabling teams to detect visual regressions and deploy with confidence.
- aid: browserstack:user-management-api
  name: BrowserStack User Management API
  tags:
  - Administration
  - Enterprise
  - User Management
  humanURL: https://www.browserstack.com/docs/enterprise/api-reference/introduction
  properties:
  - url: https://www.browserstack.com/docs/enterprise/api-reference/introduction
    type: Documentation
  description: The BrowserStack User Management REST API enables enterprise account management including creating and managing users, teams, service accounts, usage reports, and audit logs. It requires an Enterprise plan with Owner or Admin role access.
- aid: browserstack:javascript-testing-api
  name: BrowserStack JavaScript Testing API
  tags:
  - Cross-Browser Testing
  - JavaScript
  - Testing
  - Unit Testing
  humanURL: https://www.browserstack.com/docs/automate/javascript-testing/api
  properties:
  - url: https://www.browserstack.com/docs/automate/javascript-testing/api
    type: Documentation
  - url: https://www.browserstack.com/docs/automate/javascript-testing
    type: Getting Started
  - url: https://github.com/browserstack/api
    type: GitHubRepository
  description: The BrowserStack JavaScript Testing API provides HTTPS-based access to run JavaScript unit tests across 3000+ real desktop and mobile browsers in the cloud. It supports popular test frameworks including Jasmine, QUnit, Mocha, and Jest, with language bindings for Node.js, Ruby, and .NET.
- aid: browserstack:app-accessibility-testing-api
  name: BrowserStack App Accessibility Testing API
  tags:
  - Accessibility
  - Mobile Testing
  - Testing
  humanURL: https://www.browserstack.com/docs/app-accessibility/api-reference/introduction
  properties:
  - url: https://www.browserstack.com/docs/app-accessibility/api-reference/introduction
    type: Documentation
  - url: https://www.browserstack.com/docs/app-accessibility/overview/introduction
    type: Getting Started
  description: The BrowserStack App Accessibility REST API enables programmatic access to accessibility data for mobile app projects and builds. It provides endpoints for retrieving accessibility results from automated and manual tests, including project lists, build details, test cases, and issue-level analysis.
- aid: browserstack:low-code-automation-api
  name: BrowserStack Low Code Automation API
  tags:
  - Automation
  - CI/CD
  - Low Code
  - Testing
  humanURL: https://www.browserstack.com/docs/low-code-automation/cicd-integrations/rest-api
  properties:
  - url: https://www.browserstack.com/docs/low-code-automation/cicd-integrations/rest-api
    type: Documentation
  - url: https://www.browserstack.com/docs/low-code-automation/cicd-integrations/run-tests-api
    type: Reference
  - url: https://www.browserstack.com/docs/low-code-automation
    type: Getting Started
  description: The BrowserStack Low Code Automation REST API enables triggering test suite executions and retrieving build statuses for CI/CD pipeline integration. It also supports exporting low-code tests as code in .side and Nightwatch.js formats.
name: BrowserStack
tags:
- Accessibility
- Appium
- Applications
- Automation
- CI/CD
- Cross-Browser Testing
- Enterprise
- JavaScript
- Low Code
- Mobile Testing
- QA
- Regression Testing
- Selenium
- Testing
- Unit Testing
- Visual Testing
type: Contract
image: https://www.browserstack.com/images/browserstack-logo.svg
access: 3rd-Party
created: '2025-02-17'
modified: '2026-04-07'
position: Consuming
description: BrowserStack provides instant access to 3500+ real mobile devices and desktop browsers for testing web and mobile applications across different platforms and operating systems.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

