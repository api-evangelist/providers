---
aid: keyrunner
name: KeyRunner
description: KeyRunner is a local-first API platform combining a desktop API client, request monitor, mock server, and secret manager. It is delivered as desktop applications (Windows, macOS Intel, macOS Apple Silicon), a VS Code extension, and a CLI, with all requests and secrets kept inside the developer environment.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Client
  - API Testing
  - Developer Tools
  - Local-First
  - Mock Server
  - Secret Management
created: '2025-01-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/keyrunner/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: keyrunner:keyrunner-platform
    name: KeyRunner Platform
    description: The KeyRunner platform provides a local-first toolset for testing, monitoring, mocking, and running APIs with secrets kept on-device. Available as desktop apps, a VS Code extension, and a CLI distributed via npm. KeyRunner does not currently expose a public HTTP API.
    humanURL: https://keyrunner.app/
    tags:
      - API Client
      - Developer Tools
    properties:
      - type: Documentation
        url: https://keyrunner.app/
      - type: Website
        url: https://keyrunner.app/
common:
  - type: Website
    url: https://keyrunner.app/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
