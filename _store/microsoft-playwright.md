---
aid: microsoft-playwright
name: Microsoft Playwright
description: Playwright is an open-source browser automation framework by Microsoft for reliable end-to-end testing of web applications. It supports Chromium, Firefox, and WebKit with a single API across multiple programming languages.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Browser Automation
  - End-To-End Testing
  - Microsoft
  - Testing
url: https://raw.githubusercontent.com/api-evangelist/microsoft-playwright/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-playwright:playwright-api
    name: Playwright API
    tags:
      - Browser Automation
      - End-To-End Testing
      - Testing
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://playwright.dev/docs/api/class-playwright
    properties:
      - url: https://playwright.dev/docs/api/class-playwright
        type: Documentation
      - url: https://playwright.dev/docs/intro
        type: Getting Started
    description: Playwright provides a cross-browser automation API for end-to-end testing of web applications. It supports Chromium, Firefox, and WebKit with a single API, enabling reliable testing with auto-wait, network interception, mobile emulation, and parallel execution across Node.js, Python, Java, and .NET.
  - aid: microsoft-playwright:testing-service-api
    name: Azure Playwright Testing Service API
    tags:
      - Azure
      - Cloud Testing
      - Testing
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/azure/playwright-testing/
    baseURL: https://eastus.api.playwright.microsoft.com/
    properties:
      - url: https://learn.microsoft.com/en-us/azure/playwright-testing/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/azure/playwright-testing/quickstart-run-end-to-end-tests
        type: Getting Started
    description: Azure Playwright Testing is a managed cloud service for running Playwright tests at scale. It provides browser infrastructure for parallel test execution, reducing test suite run times and enabling CI/CD integration with Azure DevOps and GitHub Actions.
common:
  - type: Portal
    url: https://playwright.dev/
  - type: Website
    url: https://playwright.dev/
  - type: Documentation
    url: https://playwright.dev/docs/intro
  - type: GitHub Organization
    url: https://github.com/microsoft/playwright
  - type: Getting Started
    url: https://playwright.dev/docs/intro
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://playwright.dev/docs/support
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
