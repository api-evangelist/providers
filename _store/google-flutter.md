---
aid: google-flutter
url: https://raw.githubusercontent.com/api-evangelist/google-flutter/refs/heads/main/apis.yml
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
name: Google Flutter
tags:
- Cross-Platform
- Dart
- Google
- Mobile Development
- Open Source
- UI Framework
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Flutter is an open-source UI toolkit for building natively compiled applications for mobile, web, and desktop from a single codebase, with developer tools including the Pub.dev package API and Dart analysis APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

