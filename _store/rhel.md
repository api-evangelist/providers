---
aid: rhel
url: https://raw.githubusercontent.com/api-evangelist/rhel/refs/heads/main/apis.yml
apis:
- aid: rhel:subscription-management-api
  name: Red Hat Subscription Management API
  description: API for managing RHEL subscriptions, entitlements, and system registrations.
  humanURL: https://access.redhat.com/management/api
  tags:
  - Entitlements
  - Subscriptions
  - Systems Management
  properties:
  - type: Documentation
    url: https://access.redhat.com/management/api/docs
  - type: OpenAPI
    url: https://api.access.redhat.com/management/v1/openapi.json
  - type: Authentication
    url: https://access.redhat.com/articles/3626371
- aid: rhel:insights-api
  name: Red Hat Insights API
  description: Predictive analytics and remediation service for RHEL systems.
  humanURL: https://console.redhat.com/docs/api/insights
  tags:
  - Analytics
  - Monitoring
  - Remediation
  properties:
  - type: Documentation
    url: https://console.redhat.com/docs/api/insights
  - type: OpenAPI
    url: https://cloud.redhat.com/api/insights/v1/openapi.json
- aid: rhel:security-data-api
  name: Red Hat Security Data API
  description: API for accessing security advisories, bug fixes, and enhancement updates.
  humanURL: https://access.redhat.com/documentation/en-us/red_hat_security_data_api/
  tags:
  - Advisories
  - CVE
  - Errata
  - Security
  properties:
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_security_data_api/1.0/
name: Red Hat Enterprise Linux
tags:
- Automation
- Enterprise
- Linux
- Operating System
- Red Hat
- RHEL
- Security
- Subscription Management
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs and services for Red Hat Enterprise Linux including subscription management, insights analytics, content delivery, satellite management, security advisories, and automation platform APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

