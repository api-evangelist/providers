---
aid: vessel
url: https://raw.githubusercontent.com/api-evangelist/vessel/refs/heads/main/apis.yml
apis:
- aid: vessel:actions-api
  name: Vessel Actions API
  description: The Vessel Actions API provides pre-built actions for common integration operations, with validated API responses and request inputs. It offers well-documented APIs so developers don't need to refer to downstream provider documentation, and handles authentication, rate limits, and data normalization automatically.
  humanURL: https://www.vessel.dev/
  tags:
  - Actions
  - Automation
  - Integrations
  properties:
  - type: Documentation
    url: https://www.vessel.dev/
  - type: GitHubRepository
    url: https://github.com/vesselapi/integrations
- aid: vessel:unified-api
  name: Vessel Unified API
  description: The Vessel Unified API provides a standardized interface across integrations, abstracting away the differences between third-party APIs to provide a consistent developer experience when connecting to multiple services.
  humanURL: https://www.vessel.dev/
  tags:
  - Integrations
  - Normalization
  - Unified API
  properties:
  - type: Documentation
    url: https://www.vessel.dev/
name: Vessel
tags:
- Embedded Integrations
- Integrations
- iPaaS
- Unified API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Vessel is a developer-first embedded integrations platform that enables product teams to add native integrations to their applications. It provides unified API abstractions, actions APIs, and passthrough APIs to connect with CRM, marketing, HR, and productivity tools while managing authentication, rate limits, and data normalization.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

