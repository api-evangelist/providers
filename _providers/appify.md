---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: The Appify platform's tenant-facing REST API. Appify's public pricing page lists "REST API access" among the standard capabilities included in a subscription. The API is served from the platform appli
  name: Appify Platform REST API
  slug: appify-platform-rest-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.appify.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appify.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appify.com/privacy
- group: start
  title: ''
  type: Login
  url: https://login.appify.com
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/appify_stock/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agentappify/
- group: other
  title: ''
  type: X
  url: https://x.com/agentappify
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appify-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Appify's pricing page sells "REST API access" as a standard subscription capability and the API route is live — https://login.appify.com/api/v1 answers 403 (Spring Security, empty body) while sibling paths answer 404 — but the reference is tenant-only, the site's Resources page renders "No resources yet", and the leftover Springfox Swagger UI at /swagger-ui.html has no reachable document (every /v2/api-docs, /v3/api-docs and /swagger-resources endpoint returns 404).
  evidence:
  - status: 403
    url: https://login.appify.com/api/v1
  - status: 200
    url: https://login.appify.com/swagger-ui.html
  - status: 404
    url: https://login.appify.com/v2/api-docs
  - status: 200
    url: https://www.appify.com/resources
  - status: 404
    url: https://www.appify.com/docs
  - status: 404
    url: https://www.appify.com/llms.txt
  - status: 404
    url: https://www.appify.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: Appify is an enterprise application platform that lets organizations build, extend, and migrate line-of-business software without traditional development. The company markets a model-driven, AI-native platform — apps are described in natural language and the platform generates the data model, UI, permissions, workflows, and analytics — plus an "Unshackle" AI agent that extends systems of record such as Salesforce, SAP, and Oracle, or replicates an existing SaaS application on Appify-owned infrastructure. Appify states 40+ enterprise integrations, 12+ industries in production, and 20M+ transactions processed, and its published pricing includes "REST API access" and "unlimited apps, objects, endpoints" as standard capabilities. No public developer portal, API reference, or machine-readable specification is published; the API surface sits behind the tenant login.
image: https://www.appify.com/favicon.ico
layout: provider
modified: '2026-08-06'
name: Appify
nav: Providers
network: true
overview: 'Appify publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Application Development, No-Code, Low-Code, and Enterprise Software.


  Appify''s developer surface includes pricing and 8 more developer resources.'
random_paper: 19
screenshot: https://raw.githubusercontent.com/api-evangelist/appify/refs/heads/main/screenshots/appify-2026-08-07T161502.png
security:
- kind: domain-security
  name: Appify Domain Security
  slug: appify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appify
tags:
- Company
- Application Development
- No-Code
- Low-Code
- Enterprise Software
- Workflow-Automation
- Artificial Intelligence
- Integration
- Field Service
website: https://www.appify.com/
---
