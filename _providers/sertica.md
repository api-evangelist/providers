---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - https://www.sertica.com/modules/maintenance-api/
  trial: false
  try_now: false
agentic_access:
- acting_count: 1656
  human_in_the_loop: 26
  name: Sertica Agentic Access
  operation_count: 3340
  slug: sertica-agentic-access
  summary_line: 3340 operations · 1656 acting · 26 human-in-the-loop
api_count: 1
apis:
- baseURL: https://{sitename}.sertica.com/api
  baseurl_source: declared
  description: The SERTICA Web API - the single REST/JSON contract behind every SERTICA module. 3,340 operations across 254 resource families cover maintenance (components, jobs, job histories, counters, procedures)
  name: SERTICA Web API
  slug: sertica
artifact_total: 8
asyncapis:
- description: ''
  name: Sertica Webhooks
  slug: sertica-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.sertica.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sertica-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sertica-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sertica-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sertica-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sertica-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sertica-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sertica-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sertica-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sertica-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sertica-web-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/sertica-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sertica-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sertica-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sertica-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sertica-webhooks.yml
- group: docs
  title: ''
  type: Documentation
  url: https://support.sertica.com/hc/en-us/articles/28558470734109-SERTICA-Application-Programming-Interface
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sertica.com/api/swagger/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://support.sertica.com/hc/en-us/articles/28558504030365-Example-Get-component-data
- group: operate
  title: ''
  type: Support
  url: https://support.sertica.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sertica.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/sertica
- group: agent
  title: ''
  type: LlmsText
  url: https://www.sertica.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.sertica.com/blog/
created: '2025-02-12'
description: 'SERTICA is a maritime fleet and ship management system from RINA (originally built by Logimatic in Denmark, first code written in 1989), used to run planned maintenance, procurement, HSQE, crewing, performance, logbooks and vessel reporting across a fleet. It is deployed as a per-customer site rather than a shared multi-tenant service, and it publishes a genuinely large machine-readable contract: the SERTICA Web API is an OpenAPI 3.0.4 document with 2,743 paths, 3,340 operations and 1,104 schemas, served publicly at https://docs.sertica.com/api/swagger/v1/swagger.json and browsable in a live Swagger UI. It is a REST/JSON API authenticated with a 24-hour JWT obtained by posting a SERTICA user login to /Auth, with authorization expressed as per-user SERTICA user rights rather than OAuth scopes. Beyond CRUD it carries the statutory maritime surface - MARPOL Oil, Garbage and Ballast Water electronic record books with signing and printout operations, SFI-coded components, ISM management-system
  documents, and PunchOut/ShipServ procurement integration.'
finops:
- name: Sertica Finops
  service_category: API
  slug: sertica-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sertica.png
layout: provider
modified: '2026-08-27'
name: SERTICA
nav: Providers
network: true
overview: 'SERTICA publishes 1 API on the [APIs.io](https://apis.io/) network: Web API. Tagged areas include Maritime, Shipping, Fleet Management, Maintenance, and Procurement.


  The SERTICA catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SERTICA''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 18 more developer resources.'
plans:
- name: Sertica Plans Pricing
  plan_count: 0
  slug: sertica-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Sertica Rate Limits
  slug: sertica-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/sertica/refs/heads/main/screenshots/sertica-2026-06-20T193727.png
security:
- kind: authentication
  name: Sertica Authentication
  slug: sertica-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sertica Domain Security
  slug: sertica-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: sertica
tags:
- Maritime
- Shipping
- Fleet Management
- Maintenance
- Procurement
- Asset Management
- Compliance
- Enterprise Software
website: https://www.sertica.com/
---
