---
aid: nudge-security
name: Nudge Security
description: Nudge Security is a SaaS and AI security management platform that discovers all SaaS and cloud applications used across an organization, helps security teams manage OAuth grants, enforce security policies, monitor app-to-app integrations, and reduce SaaS risk without blocking productivity. The platform provides automated SaaS discovery, shadow IT detection, and security posture management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Access Management
  - AI Security
  - Compliance
  - Governance
  - OAuth
  - SaaS Management
  - SaaS Security
  - Security
  - Shadow IT
  - SSPM
url: https://raw.githubusercontent.com/api-evangelist/nudge-security/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: nudge-security:rest-api
    name: Nudge Security API
    description: The Nudge Security REST API enables programmatic access to retrieve data about apps, accounts, OAuth grants, security events, fields, users, user groups, labels, notifications, findings, app-to-app integrations, app instances, AI sessions and prompts, and the browser extension. It supports integration with SIEM, SOAR, and ticketing systems, and allows management of custom fields and classifications. The API is rate limited to 1200 requests per 5-minute period.
    humanURL: https://help.nudgesecurity.com/en/articles/8890697-getting-started-with-the-nudge-security-api
    baseURL: https://api.nudgesecurity.io/api/1.0
    tags:
      - Discovery
      - Governance
      - OAuth
      - SaaS Security
      - Apps
      - Accounts
      - Events
    properties:
      - type: Documentation
        url: https://help.nudgesecurity.com/en/articles/8890697-getting-started-with-the-nudge-security-api
      - type: Reference
        url: https://nudgesecurity.readme.io/reference
      - type: GettingStarted
        url: https://help.nudgesecurity.com/en/collections/10835744-integrations-and-api-configuration
      - type: OpenAPI
        url: openapi/nudge-security-openapi.yml
common:
  - type: Website
    url: https://www.nudgesecurity.com/
  - type: Documentation
    url: https://help.nudgesecurity.com/
  - type: Blog
    url: https://www.nudgesecurity.com/blog
  - type: Pricing
    url: https://www.nudgesecurity.com/pricing
  - type: SignUp
    url: https://www.nudgesecurity.com/getting-started
  - type: Integrations
    url: https://www.nudgesecurity.com/integrations
  - type: ChangeLog
    url: https://www.nudgesecurity.com/changelog
  - type: FAQ
    url: https://www.nudgesecurity.com/faqs
  - type: Product
    url: https://www.nudgesecurity.com/product
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
