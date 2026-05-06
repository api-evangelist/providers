---
aid: httpie
name: HTTPie
description: HTTPie is a user-friendly command-line and web-based HTTP client designed for testing, debugging, and interacting with APIs and HTTP services. It provides expressive syntax that mirrors actual HTTP requests, formatted and syntax-highlighted output, native JSON support, file uploads, form submissions, persistent sessions, multiple authentication schemes (basic, digest, bearer, .netrc, and an extensible plugin system covering OAuth, AWS, NTLM, and more), download mode similar to wget, HTTPS and proxy support, and cross-platform installation across Linux, macOS, Windows, and FreeBSD. The companion HTTPie web app and Desktop client layer a graphical interface over the same request and response model that the CLI exposes.
url: https://raw.githubusercontent.com/api-evangelist/httpie/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Client
  - API Testing
  - CLI
  - Client
  - Command Line
  - Developer Tools
  - HTTP
  - Open Source
  - Sessions
created: '2025-01-08'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: httpie:httpie
    name: HTTPie
    description: HTTPie is a user-friendly command-line and web-based HTTP client designed for interacting with APIs. It provides an intuitive interface for crafting HTTP requests, inspecting responses, and managing sessions with persistent headers, authentication, and cookies.
    humanURL: https://httpie.io/
    tags:
      - API Client
      - Command Line
      - HTTP
    properties:
      - type: Documentation
        url: https://httpie.io/docs/
      - type: OpenAPI
        url: openapi/httpie-httpie-openapi.yml
      - type: JSON Schema
        url: json-schema/request.json
      - type: JSON-LD Context
        url: json-ld/httpie-context.jsonld
      - type: Getting Started
        url: https://httpie.io/docs/cli/installation
      - type: GitHub
        url: https://github.com/httpie/cli
common:
  - type: Website
    url: https://httpie.io/
  - type: Documentation
    url: https://httpie.io/docs/
  - type: GitHub Organization
    url: https://github.com/httpie
  - type: Sign Up
    url: https://httpie.io/app
  - type: Blog
    url: https://httpie.io/blog
  - type: Pricing
    url: https://httpie.io/pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
