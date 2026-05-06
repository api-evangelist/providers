---
aid: owasp-zap
name: OWASP ZAP
description: OWASP ZAP (Zed Attack Proxy) is an open source web application security scanner for finding vulnerabilities in APIs and web applications during development and testing. ZAP exposes a comprehensive HTTP API for controlling and automating scans, spidering, authentication, alerts, reporting, and more.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Security Testing
  - Application Security
  - Vulnerability Scanning
  - Testing
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/owasp-zap/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: owasp-zap:owasp-zap
    name: OWASP ZAP API
    description: The HTTP API for controlling and accessing ZAP. Supports automation of access control scans, active and passive scanning, spidering, authentication, alerts, contexts, reports, scripts, and many more ZAP components.
    humanURL: https://www.zaproxy.org
    baseURL: http://zap
    tags:
      - Security Testing
      - Application Security
      - Vulnerability Scanning
      - Testing
    properties:
      - type: Documentation
        url: https://www.zaproxy.org/docs/
      - type: API Documentation
        url: https://www.zaproxy.org/docs/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/owasp-zap/refs/heads/main/openapi/owasp-zap-openapi.yml
      - type: GitHub Repository
        url: https://github.com/zaproxy/zaproxy
      - type: GitHub API Docs
        url: https://github.com/zaproxy/zap-api-docs
common:
  - type: Website
    url: https://www.zaproxy.org
  - type: Documentation
    url: https://www.zaproxy.org/docs/
  - type: API Documentation
    url: https://www.zaproxy.org/docs/api/
  - type: GitHub Organization
    url: https://github.com/zaproxy
  - type: Download
    url: https://www.zaproxy.org/download/
  - type: Community
    url: https://groups.google.com/group/zaproxy-users
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
