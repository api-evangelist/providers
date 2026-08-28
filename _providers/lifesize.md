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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: The automation and control interface built into Lifesize Icon video systems (models 300, 400, 450, 500, 600, 700, 800). It exposes a REST method for accessing a set of resources through a fixed set of
  name: Lifesize Icon Automation API
  slug: icon-automation-api
- description: The hosted service API behind the Lifesize Cloud meeting service, the Lifesize Admin Console, and the web/desktop/mobile applications. The host is live and serves JSON from an AWS API Gateway edge, re
  name: Lifesize Cloud API
  slug: cloud-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lifesize-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lifesize.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.lifesize.com/product/lifesize-icon-400-450-600-800/advanced-topics/api-overview/
- group: docs
  title: ''
  type: Documentation
  url: https://support.lifesize.com/
- group: docs
  title: ''
  type: APIReference
  url: https://support.lifesize.com/product/lifesize-icon-400-450-600-800/advanced-topics/api-overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.lifesize.com/product/lifesize-icon-400-450-600-800/lets-get-started/
- group: operate
  title: ''
  type: Support
  url: https://support.lifesize.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://customer.support.enghouse.com/servicedesk/customer/portal/19
- group: start
  title: ''
  type: SignUp
  url: https://call.lifesizecloud.com/
- group: start
  title: ''
  type: Login
  url: https://admin.lifesizecloud.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enghousevideo.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enghousevideo.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lifesizecloud.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.lifesize.com/product/release-notes/
- group: other
  title: ''
  type: Downloads
  url: https://support.lifesize.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/lifesize-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lifesize-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/lifesize-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lifesize-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lifesize-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lifesize-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lifesize-llms.txt
created: '2026-07-17'
description: 'Lifesize is a video conferencing and meeting-room platform — cloud meeting service (Lifesize Cloud), Icon conference-room systems, the Lifesize Share wireless presentation appliance, Phone HD, and the web/desktop/mobile apps — originally founded in Austin, Texas. Lifesize merged with contact-center provider Serenova (CxEngage) in 2020 and was acquired by Enghouse Systems in 2023; the video business now operates as Enghouse Video (Vidyo Inc.) and the Lifesize brand and product line continue under enghousevideo.com/lifesize. The developer surface is an on-device automation API on the Lifesize Icon series: a REST interface and a Lifesize Automation Command Line Interface (CLI) reachable over HTTPS or SSH with administrator credentials, both self-documenting on the device itself, used to read configuration, change system preferences, report call status and statistics, and control calls. Lifesize also runs a hosted cloud service API host and publishes chat (Slack, Microsoft Teams)
  and calendar (Google Workspace, Microsoft 365) integrations, dated release notes, and an Atlassian-hosted status page.'
image: https://www.enghousevideo.com/wp-content/uploads/2024/04/Enghouse-lifesize-icon-white.png
layout: provider
modified: '2026-07-19'
name: Lifesize
nav: Providers
network: true
overview: 'Lifesize publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video Conferencing, Communications, Collaboration, and Meetings.


  Lifesize''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, changelog, authentication, and 15 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 31.0
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 31.0
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lifesize/refs/heads/main/screenshots/lifesize-2026-07-25T225048.png
security:
- kind: authentication
  name: Lifesize Authentication
  slug: lifesize-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lifesize Domain Security
  slug: lifesize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lifesize
tags:
- Company
- Video Conferencing
- Communications
- Collaboration
- Meetings
- Unified Communications
- Video
- Contact Center
- Conference Room Systems
- Streaming
website: https://lifesize.com
---
