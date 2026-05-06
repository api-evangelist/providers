---
aid: whistle
name: Whistle
description: Whistle is a cross-platform HTTP, HTTPS, HTTP/2, WebSocket, and TCP debugging proxy built on Node.js. It enables developers to inspect, intercept, modify, and replay network traffic through a rule-based configuration system with a built-in web UI.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Debugging Proxy
  - Proxy
  - Network Debugging
  - HTTP
  - HTTPS
  - WebSocket
  - Developer Tools
url: https://raw.githubusercontent.com/api-evangelist/whistle/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: whistle:whistle
    name: Whistle
    description: Whistle is a cross-platform HTTP, HTTPS, HTTP/2, WebSocket, and TCP debugging proxy tool. It lets developers intercept, inspect, and modify network traffic using a rule-based configuration system. Features include request/response modification, local file mapping, API mocking, remote debugging with Weinre, request replay via a built-in Composer, plugin support, and a web-based UI.
    humanURL: https://wproxy.org/whistle/
    baseURL: http://localhost:8899
    tags:
      - Debugging Proxy
      - Proxy
      - Network Debugging
      - HTTP
      - HTTPS
      - WebSocket
      - Developer Tools
      - API Mocking
      - Request Replay
    properties:
      - type: Documentation
        url: https://wproxy.org/en/docs/
      - type: Getting Started
        url: https://wproxy.org/en/docs/getting-started.html
      - type: GitHub
        url: https://github.com/avwo/whistle
      - type: NPM
        url: https://www.npmjs.com/package/whistle
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/whistle/main/json-schema/whistle-rule-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/whistle/main/json-schema/whistle-plugin-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/whistle/main/json-structure/whistle-rule-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/whistle/main/json-ld/whistle-context.jsonld
      - type: Examples
        url: https://raw.githubusercontent.com/api-evangelist/whistle/main/examples/whistle-rule-example.json
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/whistle/main/vocabulary/whistle-vocabulary.yml
    contact:
      - FN: Whistle Team
        url: https://github.com/avwo/whistle
    features:
      - Request and response interception and modification
      - HTTP, HTTPS, HTTP/2, WebSocket, TCP support
      - Rule-based traffic modification
      - Local file mapping and API mocking
      - Built-in Weinre for remote DOM inspection
      - Request Composer for replay and editing
      - Plugin extensibility system
      - Multiple proxy modes: HTTP, HTTPS, Socks, reverse proxy
      - Cross-platform: macOS, Windows, Linux
      - Web-based management UI at localhost:8899
    use-cases:
      - Frontend development API proxying
      - Mobile app network debugging
      - CORS configuration testing
      - Request/response modification during development
      - API mocking with local JSON files
      - Remote debugging of web pages on devices
      - Traffic inspection and analysis
    integrations:
      - Chrome Extension ZeroOmega for proxy switching
      - Weinre for remote DOM inspection
      - Node.js NPM module integration
      - Desktop client via whistle-client
common:
  - type: Website
    url: https://wproxy.org/whistle/
  - type: Documentation
    url: https://wproxy.org/en/docs/
  - type: Getting Started
    url: https://wproxy.org/en/docs/getting-started.html
  - type: GitHub Organization
    url: https://github.com/avwo
  - type: GitHub
    url: https://github.com/avwo/whistle
  - type: NPM
    url: https://www.npmjs.com/package/whistle
  - type: DesktopClient
    url: https://github.com/avwo/whistle-client
  - type: ChromeExtension
    url: https://github.com/avwo/whistle-for-chrome
  - type: PluginScaffolding
    url: https://github.com/avwo/lack
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
