---
aid: apple-keynote
url: https://raw.githubusercontent.com/api-evangelist/apple-keynote/refs/heads/main/apis.yml
apis:
- name: Keynote iCloud API
  description: Cloud-based API for accessing and manipulating Keynote presentations through iCloud.
  image: https://www.apple.com/v/keynote/o/images/overview/keynote_icon__e6u8i7ju7e2e_large.jpg
  humanURL: https://www.icloud.com/keynote
  baseURL: https://p00-keynote.icloud.com
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/keynotekit
  - type: OpenAPI
    url: https://api.example.com/keynote/openapi.json
  tags:
  - Cloud Storage
  - Collaboration
  - Presentations
  - Slides
  contact:
  - FN: Apple Developer Support
    email: developer@apple.com
    url: https://developer.apple.com/contact/
- name: Keynote AppleScript API
  description: Local automation API for Keynote using AppleScript.
  humanURL: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/
  properties:
  - type: Documentation
    url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/KeynoteScriptingGuide/
  - type: Dictionary
    url: file:///Applications/Keynote.app/Contents/Resources/Keynote.sdef
  tags:
  - Automation
  - Local API
  - macOS
  - Scripting
- name: Keynote JavaScript for Automation API
  description: JavaScript-based automation interface for controlling Keynote on macOS. Provides the same automation capabilities as AppleScript using JavaScript syntax through the Open Scripting Architecture.
  image: https://www.apple.com/v/keynote/o/images/overview/keynote_icon__e6u8i7ju7e2e_large.jpg
  humanURL: https://developer.apple.com/library/archive/releasenotes/InterapplicationCommunication/RN-JavaScriptForAutomation/
  tags:
  - Automation
  - JavaScript
  - macOS
  - Scripting
  properties:
  - type: Documentation
    url: https://developer.apple.com/library/archive/releasenotes/InterapplicationCommunication/RN-JavaScriptForAutomation/
- name: Keynote Shortcuts Actions
  description: Shortcuts app actions for Keynote on iOS, iPadOS, and macOS, enabling users to open, create, and export presentations as part of automated workflows including format conversion and template generation.
  image: https://www.apple.com/v/keynote/o/images/overview/keynote_icon__e6u8i7ju7e2e_large.jpg
  humanURL: https://developer.apple.com/shortcuts/
  tags:
  - Automation
  - iOS
  - Shortcuts
  - Workflows
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/appintents/app-shortcuts
name: Apple Keynote
tags:
- Apple
- Design
- iWork
- Presentations
- Productivity
- Slides
type: Contract
image: https://www.apple.com/v/keynote/o/images/overview/keynote_icon__e6u8i7ju7e2e_large.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: API for Apple Keynote presentation software, enabling programmatic access to create, edit, and manage presentations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

