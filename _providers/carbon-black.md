---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 9.6
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: REST APIs for the Carbon Black Cloud platform — Endpoint Standard, Enterprise EDR, Audit and Remediation (live query), and Workload/Container protection. Authentication uses an API Id/Secret pair in a
  name: Carbon Black Cloud Platform API
  slug: carbon-black-cloud-platform-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carbon-black-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.carbonblack.com/
- group: company
  title: ''
  type: Website
  url: https://developer.carbonblack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.carbonblack.com/reference/carbon-black-cloud/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.carbonblack.com/reference/carbon-black-cloud/platform-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.carbonblack.com/reference/carbon-black-cloud/authentication/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carbonblack
- group: operate
  title: ''
  type: Roadmap
  url: https://trello.com/b/URJZ5Pn5
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/carbon-black
- group: operate
  title: ''
  type: Support
  url: https://community.broadcom.com/symantecenterprise
- group: build
  title: ''
  type: SDKs
  url: packages/carbon-black-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/carbon-black-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carbon-black-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carbon-black-llms.txt
created: '2026-07-17'
description: Carbon Black is an endpoint security company, now part of Broadcom (formerly VMware Carbon Black), whose cloud-native platform delivers next-generation antivirus, endpoint detection and response (EDR), threat hunting, live query, and application control. The Carbon Black Cloud platform spans Endpoint Standard, Enterprise EDR, Audit and Remediation, and Workload/Container protection, alongside the on-premises Carbon Black EDR and App Control products. Its developer network at developer.carbonblack.com publishes REST APIs, a Python SDK, and integration guides for security operations, threat intelligence, and automated remediation. APIs authenticate with an API Id/Secret pair passed in an X-Auth-Token header against region-specific Carbon Black Cloud hostnames.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carbon-black.png
layout: provider
modified: '2026-07-18'
name: Carbon Black
nav: Providers
network: true
overview: 'Carbon Black publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Endpoint Security, EDR, and Threat Detection.


  Carbon Black''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 9 more developer resources.'
random_paper: 27
score:
  band: emerging
  composite: 22.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 22.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carbon-black/refs/heads/main/screenshots/carbon-black-2026-07-25T204503.png
security:
- kind: authentication
  name: Carbon Black Authentication
  slug: carbon-black-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Carbon Black Domain Security
  slug: carbon-black-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbon-black
tags:
- Company
- Security
- Endpoint Security
- EDR
- Threat Detection
- Cybersecurity
- Cloud Security
website: https://developer.carbonblack.com/
---
