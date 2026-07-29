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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: The OTX DirectConnect API provides programmatic access to the LevelBlue Open Threat Exchange, an open community threat-intelligence platform. It exposes indicators (IPs, domains, hostnames, file hashe
  name: LevelBlue Open Threat Exchange (OTX) DirectConnect API
  slug: levelblue-open-threat-exchange-otx-directconnect-api
- description: Endpoints for managing and searching alarm messages.
  name: LevelBlue Alarms API
  slug: levelblue-alarms-api
- description: Endpoints for managing and searching events.
  name: LevelBlue Events API
  slug: levelblue-events-api
- description: Endpoint for OAuth 2.0 functionality.
  name: LevelBlue OAuth API
  slug: levelblue-oauth-api
artifact_total: 9
asyncapis:
- description: ''
  name: Levelblue Usm Anywhere Webhooks
  slug: levelblue-usm-anywhere-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.levelblue.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.levelblue.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.levelblue.com/api-reference/oauth/get-oauth-token
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.levelblue.com/documentation/usm-anywhere/user-guide/user-management/api-clients
- group: operate
  title: ''
  type: Support
  url: https://www.levelblue.com/company/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://success.levelblue.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.levelblue.com/blogs/levelblue-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlienVault-OTX
- group: commercial
  title: ''
  type: Pricing
  url: https://www.levelblue.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.levelblue.com/legal/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.levelblue.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alienvault.cloud/
- group: auth
  title: ''
  type: Security
  url: https://docs.levelblue.com/documentation/how-to-submit-a-security-issue
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/levelblue-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/levelblue-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/levelblue-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/levelblue-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/levelblue-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/levelblue-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/levelblue-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/levelblue-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/levelblue-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/levelblue-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/levelblue-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/levelblue-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/levelblue-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/levelblue-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/levelblue-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/levelblue-usm-anywhere-webhooks.yml
created: '2026-07-17'
description: LevelBlue is a pure-play managed security service provider (MSSP), formed from AT&T Cybersecurity and the AlienVault platform it acquired, delivering managed detection and response, managed cloud and network security, incident readiness and response, cyber advisory, exposure management and email security, backed by SpiderLabs threat intelligence. Its developer surface is the USM Anywhere v2.0 REST API — a per-tenant, OAuth 2.0 client-credentials API over alarms and normalized security events, with HAL pagination and a webhook connector for pushing third-party events into the platform — alongside the LevelBlue Open Threat Exchange (OTX) DirectConnect API for community threat intelligence.
image: https://www.levelblue.com/hubfs/lb-web/social/metadata.jpg
layout: provider
modified: '2026-07-19'
name: LevelBlue
nav: Providers
network: true
overview: 'LevelBlue publishes 3 APIs on the [APIs.io](https://apis.io/) network: Alarms API, Events API, and OAuth API. Tagged areas include Company, Enterprise, Cybersecurity, Security, and Threat Intelligence.


  The LevelBlue catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LevelBlue''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 23 more developer resources.'
random_paper: 69
scopes:
- name: Levelblue Scopes
  scope_count: 3
  slug: levelblue-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 52.8
  delta: -0.1
  facets:
    commercial_clarity: 31.6
    contract_quality: 66.5
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 52.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/levelblue/refs/heads/main/screenshots/levelblue-2026-07-25T224945.png
security:
- kind: authentication
  name: Levelblue Authentication
  slug: levelblue-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Levelblue Domain Security
  slug: levelblue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Levelblue Vulnerability Disclosure
  slug: levelblue-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: levelblue
tags:
- Company
- Enterprise
- Cybersecurity
- Security
- Threat Intelligence
- Managed Security
- SIEM
- Threat Detection
- Incident Response
- Compliance
website: https://docs.levelblue.com/documentation
---
