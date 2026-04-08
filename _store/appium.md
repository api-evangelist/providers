---
aid: appium
url: https://raw.githubusercontent.com/api-evangelist/appium/refs/heads/main/apis.yml
apis:
- name: Appium Server API
  description: The main Appium server API that implements the WebDriver protocol for mobile automation.
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
    url: https://raw.githubusercontent.com/appium/appium/master/packages/base-driver/lib/protocol/openapi.json
  - type: GitHub
    url: https://github.com/appium/appium
  - type: Commands
    url: https://appium.io/docs/en/latest/reference/commands/
  contact:
  - FN: Appium Community
    email: appium@googlegroups.com
    url: https://discuss.appium.io/
- name: Appium Inspector API
  description: Standalone GUI inspector for mobile apps that communicates with Appium server.
  humanURL: https://github.com/appium/appium-inspector
  baseURL: https://github.com/appium/appium-inspector/releases
  tags:
  - Debugging
  - GUI
  - Inspector
  - Mobile Testing
  properties:
  - type: GitHub
    url: https://github.com/appium/appium-inspector
  - type: Downloads
    url: https://github.com/appium/appium-inspector/releases
name: Appium
tags:
- Android
- Cross-Platform
- iOS
- Mobile Testing
- Open Source
- Test Automation
- WebDriver
type: Contract
image: https://appium.io/docs/en/latest/assets/images/appium-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Appium is an open-source test automation framework for use with native, hybrid and mobile web apps. It drives iOS, Android, and Windows apps using the WebDriver protocol.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

