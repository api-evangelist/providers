---
name: Apple Keynote
description: Apple Keynote is a presentation software application developed by Apple Inc. as part of the iWork productivity suite, available on macOS, iOS, iPadOS, and the web via iCloud. It enables creating visually rich presentations with animations, transitions, charts, and real-time collaboration. Keynote supports automation via AppleScript, JavaScript for Automation (JXA), and Apple Shortcuts, and provides iCloud-based access for cross-device sync and sharing.
image: https://www.apple.com/v/keynote/o/images/overview/keynote_icon__e6u8i7ju7e2e_large.jpg
url: https://www.apple.com/keynote/
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.18'
apis:
  - name: Keynote iCloud API
    description: Cloud-based API for accessing and manipulating Keynote presentations through iCloud, enabling programmatic creation, management, slide operations, and multi-format export of presentations stored in iCloud.
    image: https://www.apple.com/v/keynote/o/images/overview/keynote_icon__e6u8i7ju7e2e_large.jpg
    humanURL: https://www.icloud.com/keynote
    baseURL: https://p00-keynote.icloud.com
    tags:
      - Cloud Storage
      - Collaboration
      - Presentations
      - Slides
      - iCloud
    properties:
      - type: Documentation
        url: https://developer.apple.com/documentation/
      - type: OpenAPI
        url: openapi/apple-keynote-icloud-openapi.yaml
      - type: JSONSchema
        url: json-schema/apple-keynote-presentation-schema.json
        title: Presentation Schema
      - type: JSONSchema
        url: json-schema/apple-keynote-slide-schema.json
        title: Slide Schema
      - type: JSONSchema
        url: json-schema/apple-keynote-theme-schema.json
        title: Theme Schema
      - type: JSONSchema
        url: json-schema/apple-keynote-export-request-schema.json
        title: Export Request Schema
    contact:
      - FN: Apple Developer Support
        email: developer@apple.com
        url: https://developer.apple.com/contact/
  - name: Keynote AppleScript API
    description: Local automation API for Keynote using AppleScript, enabling programmatic control of presentations, slides, and elements on macOS. Access via the Open Scripting Architecture dictionary.
    humanURL: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/
    tags:
      - Automation
      - Local API
      - macOS
      - Scripting
    properties:
      - type: Documentation
        url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/KeynoteScriptingGuide/
      - type: APIReference
        url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/KeynoteScriptingGuide/
  - name: Keynote JavaScript for Automation API
    description: JavaScript-based automation interface for controlling Keynote on macOS using the Open Scripting Architecture (OSA). Provides the same capabilities as AppleScript using JavaScript syntax via JXA.
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
    humanURL: https://developer.apple.com/shortcuts/
    tags:
      - Automation
      - iOS
      - Shortcuts
      - Workflows
    properties:
      - type: Documentation
        url: https://developer.apple.com/documentation/appintents/app-shortcuts
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Apple
  - Design
  - iWork
  - Presentations
  - Productivity
  - Slides
common:
  - type: Portal
    url: https://developer.apple.com/
  - type: Documentation
    url: https://support.apple.com/guide/keynote/
  - type: Support
    url: https://developer.apple.com/support/
  - type: TermsOfService
    url: https://developer.apple.com/support/terms/
  - type: PrivacyPolicy
    url: https://www.apple.com/privacy/
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/keynote
  - type: YouTube
    url: https://www.youtube.com/@AppleDeveloper
  - type: JSONLD
    url: json-ld/apple-keynote-context.jsonld
  - type: SpectralRules
    url: rules/apple-keynote-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apple-keynote-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/shared/apple-keynote-icloud.yaml
    title: Apple Keynote iCloud Shared Capability
  - type: NaftikoCapability
    url: capabilities/presentation-automation.yaml
    title: Presentation Automation Workflow
  - type: Features
    data:
      - name: Multi-Platform Availability
        description: Available on macOS, iOS, iPadOS, and web browsers via iCloud
      - name: Real-Time Collaboration
        description: Multiple users can edit presentations simultaneously via iCloud sharing
      - name: Magic Move Transitions
        description: Intelligent morph transitions that animate elements between slides
      - name: AppleScript Automation
        description: Full scripting support via AppleScript and JavaScript for Automation
      - name: Shortcuts Integration
        description: Apple Shortcuts actions for automated presentation workflows on iOS and macOS
      - name: Multi-Format Export
        description: Export to PDF, PowerPoint (.pptx), HTML, images, and native .key format
      - name: Live Video Presenter
        description: Present with live video overlays in video conferencing applications
      - name: Cinematic Animations
        description: Rich build-in and build-out animations for slide elements
      - name: Charts and Data Visualization
        description: Built-in chart types including bar, line, pie, scatter, and more with live data
  - type: UseCases
    data:
      - name: Business Presentations
        description: Creating professional pitch decks, board presentations, and quarterly reviews
      - name: Educational Content
        description: Designing lecture slides, course materials, and educational presentations
      - name: Marketing Materials
        description: Producing brand presentations, product launches, and sales decks
      - name: Automated Report Generation
        description: Using AppleScript or Shortcuts to programmatically generate recurring presentation reports
      - name: Conference Presentations
        description: Creating polished conference talks with animations and transitions
      - name: Training Materials
        description: Building step-by-step training and onboarding presentations
  - type: Integrations
    data:
      - name: iCloud Drive
        description: Automatic sync and storage of presentations across Apple devices
      - name: Apple Numbers
        description: Import live chart data from Numbers spreadsheets
      - name: Apple Pages
        description: Cross-link documents and share content between Pages and Keynote
      - name: Microsoft PowerPoint
        description: Import and export PPTX files for cross-platform compatibility
      - name: Zoom
        description: Present directly from Keynote in Zoom video calls
      - name: Apple Shortcuts
        description: Automate presentation creation and export workflows on iOS and macOS
      - name: Spotlight
        description: Index and search Keynote presentation content via macOS Spotlight
---
