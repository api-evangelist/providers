---
aid: cequence
url: https://raw.githubusercontent.com/api-evangelist/cequence/refs/heads/main/apis.yml
name: Cequence Security
tags:
  - AI Protection
  - API Discovery
  - API Security
  - Application Security
  - Attack Surface
  - Bot Management
  - Business Logic Abuse
  - CNAPP
  - Cybersecurity
  - Fraud
  - Unified API Protection
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: Cequence Security delivers the Unified API Protection (UAP) platform, combining external API attack-surface discovery, posture and compliance analysis, inline runtime protection, and testing into a single solution for defending web applications, APIs, and AI endpoints against business logic abuse, bot attacks, and fraud. The Cequence product family is organized into API Spyder (agentless external discovery), API Sentinel (API inventory, posture, and compliance), API Spartan (runtime bot and abuse defense), API Security Testing (shift-left OpenAPI conformance and vulnerability testing), and Cequence Defender (inline reverse-proxy enforcement of API policy).
apis:
  - aid: cequence:cequence-api-spyder
    name: Cequence API Spyder
    tags:
      - Attack Surface Management
      - Discovery
      - External Scanning
      - Shadow APIs
    humanURL: https://www.cequence.ai/products/api-spyder/
    properties:
      - url: https://www.cequence.ai/products/api-spyder/
        type: Website
      - url: https://www.cequence.ai/wp-content/uploads/2022/06/cequence-ds-apispyder.pdf
        type: Datasheet
      - url: https://www.cequence.ai/apispyder-demo/
        type: Demo
    description: API Spyder is a SaaS-based, agentless external discovery service that provides an attacker's view into an organization's public-facing API hosts, hosting providers, and API-specific exposures including weak TLS and shadow APIs. Crawls can be on-demand or scheduled for continuous external attack-surface monitoring.
  - aid: cequence:cequence-api-sentinel
    name: Cequence API Sentinel
    tags:
      - API Inventory
      - Compliance
      - Posture
      - Risk
      - Sensitive Data
    humanURL: https://www.cequence.ai/products/
    properties:
      - url: https://www.cequence.ai/products/
        type: Website
      - url: https://helpdesk.cequence.ai/
        type: HelpCenter
    description: API Sentinel is the Cequence API posture and compliance module that continuously inventories internal and external APIs, classifies sensitive data flows, scores API risk against governance policies, and generates remediation guidance for security and platform teams.
  - aid: cequence:cequence-api-spartan
    name: Cequence API Spartan
    tags:
      - ATO
      - Bot Management
      - Business Logic Abuse
      - Credential Stuffing
      - Fraud
      - Runtime
    humanURL: https://www.cequence.ai/products/
    properties:
      - url: https://www.cequence.ai/products/
        type: Website
      - url: https://helpdesk.cequence.ai/hc/en-us/articles/19223960381719-Cequence-Unified-API-Protection-overview
        type: Documentation
    description: API Spartan provides runtime protection against malicious and unwanted API traffic, including account takeover, credential stuffing, scraping, gift-card fraud, and other business logic abuse, with ML-driven detection and mitigation actions such as blocking, rate limiting, and deception.
  - aid: cequence:cequence-api-security-testing
    name: Cequence API Security Testing
    tags:
      - Conformance
      - DAST
      - OWASP API Top 10
      - Pre-Production
      - Testing
    humanURL: https://www.cequence.ai/blog/cequence-product-news/announcing-unified-api-protection-v2-0/
    properties:
      - url: https://www.cequence.ai/blog/cequence-product-news/announcing-unified-api-protection-v2-0/
        type: Announcement
      - url: https://www.cequence.ai/products/
        type: Website
    description: API Security Testing extends Cequence into shift-left, performing pre-production OpenAPI conformance and vulnerability testing against the OWASP API Security Top 10, feeding results back into Sentinel and Spartan for continuous lifecycle protection.
  - aid: cequence:cequence-defender
    name: Cequence Defender
    tags:
      - Enforcement
      - Inline
      - Policy
      - Reverse Proxy
      - Runtime
    humanURL: https://helpdesk.cequence.ai/hc/en-us/articles/19223960381719-Cequence-Unified-API-Protection-overview
    properties:
      - url: https://helpdesk.cequence.ai/hc/en-us/articles/19223960381719-Cequence-Unified-API-Protection-overview
        type: Documentation
      - url: https://www.cequence.ai/products/
        type: Website
    description: Cequence Defender is a reverse-proxy deployed inline with API traffic, enforcing API policies, filtering malicious traffic, and providing real-time detection and mitigation through active traffic inspection.
common:
  - type: Website
    url: https://www.cequence.ai/
  - type: Products
    url: https://www.cequence.ai/products/
  - type: HelpCenter
    url: https://helpdesk.cequence.ai/
  - type: Blog
    url: https://www.cequence.ai/blog/
  - type: News
    url: https://www.cequence.ai/news/
  - type: Privacy Policy
    url: https://www.cequence.ai/privacy-policy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
