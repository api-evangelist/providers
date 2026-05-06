---
aid: google-flutter
name: Google Flutter
description: Google Flutter is an open-source UI toolkit for building natively compiled applications for mobile, web, and desktop from a single codebase, with developer tools including the Pub.dev package API and Dart analysis APIs.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-flutter/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Cross-Platform
  - Dart
  - Google
  - Mobile Development
  - Open Source
  - UI Framework
apis:
  - name: Pub.dev API
    description: The Pub.dev API provides programmatic access to the official package repository for Dart and Flutter. Developers can search for packages, retrieve package metadata and version details, fetch package scores and metrics, and access documentation links.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://pub.dev/help/api
    baseURL: https://pub.dev/api
    tags:
      - Dependencies
      - Packages
      - Registry
    properties:
      - type: Documentation
        url: https://pub.dev/help/api
      - type: OpenAPI
        url: openapi/flutter-pub-dev-openapi.yml
      - type: Authentication
        url: https://pub.dev/help/api#authentication
      - type: Getting Started
        url: https://docs.flutter.dev/get-started
      - type: JSONSchema
        url: json-schema/google-flutter-pub-package-schema.json
  - name: Dart Analysis Server Protocol
    description: The Dart Analysis Server provides a JSON-based protocol for IDE integration, enabling code analysis, completion, navigation, refactoring, and diagnostics for Dart and Flutter projects.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://htmlpreview.github.io/?https://github.com/dart-lang/sdk/blob/main/pkg/analysis_server/doc/api.html
    baseURL: https://localhost
    tags:
      - Code Analysis
      - IDE
      - Language Server
    properties:
      - type: Documentation
        url: https://github.com/dart-lang/sdk/blob/main/pkg/analysis_server/doc/api.html
common:
  - type: Portal
    url: https://flutter.dev
  - type: Getting Started
    url: https://docs.flutter.dev/get-started
  - type: Documentation
    url: https://docs.flutter.dev
  - type: Authentication
    url: https://pub.dev/help/api#authentication
  - type: SDKs
    url: https://docs.flutter.dev/get-started/install
  - type: Terms of Service
    url: https://policies.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://github.com/flutter/flutter/wiki
  - type: Support
    url: https://flutter.dev/community
  - type: JSON-LD
    url: json-ld/google-flutter-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
