---
aid: stackhawk
name: StackHawk
description: StackHawk is an application and API security testing platform that helps engineering teams find, triage, and fix security vulnerabilities in their APIs and web applications. It provides Dynamic Application Security Testing (DAST) with deep OpenAPI spec integration, CI/CD pipeline automation, AI-powered spec generation, and an AppSec Intelligence platform for program-level visibility across the software development lifecycle.
url: https://raw.githubusercontent.com/api-evangelist/stackhawk/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Security
  - Application Security
  - DAST
  - Security Testing
  - Vulnerability Management
type: Index
access: 3rd-Party
created: '2025-01-08'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: stackhawk:stackhawk-api
    name: StackHawk API
    description: The StackHawk Public API provides programmatic access to the StackHawk platform, enabling management of applications, environments, scan configurations, scan results, findings, repositories, teams, policies, and reports. Authentication uses JWT tokens obtained via API key.
    humanURL: https://apidocs.stackhawk.com/docs
    baseURL: https://api.stackhawk.com
    tags:
      - API Security
      - Applications
      - Scan Results
      - Security Testing
    properties:
      - type: Documentation
        url: https://apidocs.stackhawk.com/docs
      - type: OpenAPI
        url: https://download.stackhawk.com/openapi/stackhawk-openapi.json
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/stackhawk/refs/heads/main/openapi/stackhawk-openapi.yml
common:
  - type: Website
    url: https://www.stackhawk.com/
    name: StackHawk Website
  - type: Documentation
    url: https://docs.stackhawk.com/
    name: StackHawk Documentation
  - type: APIReference
    url: https://apidocs.stackhawk.com/docs
    name: API Reference
  - type: GettingStarted
    url: https://docs.stackhawk.com/
    name: Getting Started
  - type: Blog
    url: https://www.stackhawk.com/blog/
    name: StackHawk Blog
  - type: ChangeLog
    url: https://docs.stackhawk.com/changelog.html
    name: Changelog
  - type: Pricing
    url: https://www.stackhawk.com/pricing/
    name: Pricing
  - type: Login
    url: https://app.stackhawk.com/
    name: StackHawk App
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
