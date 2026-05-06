---
aid: mockserver
name: MockServer
description: MockServer enables easy mocking of any system you integrate with via HTTP or HTTPS (e.g. services, web sites, etc) with clients in Java, JavaScript, and Ruby and a simple REST API. MockServer can be used to mock APIs that are not yet fully developed, isolate the system under test for reliable testing, simulate slow or faulty endpoints, and record/replay requests.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/mockserver/refs/heads/main/apis.yml
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-28'
position: Consumer
specificationVersion: '0.19'
tags:
  - Mocking
  - Mock Server
  - Testing
  - Service Virtualization
  - HTTP
  - REST API
  - Platform
apis:
  - aid: mockserver:mockserver
    name: MockServer
    description: MockServer is a flexible open-source tool for mocking and proxying HTTP and HTTPS requests. It exposes a simple REST control plane for creating expectations, verifying received requests, retrieving recorded traffic, and managing the running mock or proxy process.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.mock-server.com/
    baseURL: http://localhost:1080/
    tags:
      - Mocking
      - Mock Server
      - Testing
      - Proxy
      - HTTP
    properties:
      - type: Documentation
        url: https://www.mock-server.com/
      - type: Getting Started
        url: https://www.mock-server.com/mock_server/getting_started.html
      - type: GitHub Repository
        url: https://github.com/mock-server/mockserver
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/mockserver/refs/heads/main/openapi/mockserver-openapi-original.yml
common:
  - type: Website
    url: https://www.mock-server.com/
  - type: Documentation
    url: https://www.mock-server.com/
  - type: GitHub Organization
    url: https://github.com/mock-server
  - type: Getting Started
    url: https://www.mock-server.com/mock_server/getting_started.html
  - type: Issues
    url: https://github.com/mock-server/mockserver/issues
  - type: License
    url: https://github.com/mock-server/mockserver/blob/master/LICENSE.md
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
