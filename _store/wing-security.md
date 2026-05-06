---
aid: wing-security
name: Wing Security
description: Wing Security is an AI security platform providing automated discovery, risk assessment, and governance of AI agents, SaaS applications, and app-to-app integrations. The platform delivers SaaS Security Posture Management (SSPM), Identity Threat Detection and Response (ITDR), and continuous observability for AI tools across enterprise environments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Security
  - Identity Threat Detection
  - ITDR
  - SaaS Security
  - SSPM
  - Supply Chain Security
url: https://raw.githubusercontent.com/api-evangelist/wing-security/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: wing-security:wing-security-platform-api
    name: Wing Security Platform API
    description: The Wing Security platform API provides programmatic access to SaaS discovery, risk assessment, identity threat detection, and remediation capabilities. The platform supports webhook integrations and API-based connectivity for SIEM/SOAR automation workflows.
    humanURL: https://www.wing.security
    baseURL: https://www.wing.security
    tags:
      - AI Security
      - Identity Security
      - SaaS Discovery
      - SaaS Security
      - SSPM
    properties:
      - type: Documentation
        url: https://www.wing.security/resources
      - type: Website
        url: https://www.wing.security
      - type: Platform
        url: https://wing.security/platform/
common:
  - type: Website
    url: https://www.wing.security
    name: Wing Security
    description: Main website for Wing Security AI agent and SaaS security platform.
  - type: Documentation
    url: https://www.wing.security/resources
    name: Wing Security Resources
    description: Resources and documentation for Wing Security.
  - type: Platform
    url: https://wing.security/platform/
    name: Wing Security Platform
    description: Overview of the Wing Security SSPM and ITDR platform capabilities.
  - type: Blog
    url: https://wing.security/blog/
    name: Wing Security Blog
    description: Technical insights on AI security, SaaS security, and threat intelligence.
  - type: TrustCenter
    url: https://trust.wing.security/
    name: Wing Security Trust Center
    description: Security and compliance information for Wing Security.
  - url: https://raw.githubusercontent.com/api-evangelist/wing-security/refs/heads/main/json-ld/wing-security-context.jsonld
    name: Wing Security JSON-LD Context
    type: JSONLDContext
    description: JSON-LD context for Wing Security domain vocabulary.
  - url: https://raw.githubusercontent.com/api-evangelist/wing-security/refs/heads/main/vocabulary/wing-security-vocabulary.yml
    name: Wing Security Vocabulary
    type: Vocabulary
    description: Domain vocabulary for Wing Security platform concepts.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
