---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Sentinel Agentic Access
  operation_count: 11
  slug: microsoft-sentinel-agentic-access
  summary_line: 11 operations · 4 acting
api_count: 5
apis:
- description: The AlertRules API from Microsoft Sentinel — 2 operation(s) for alertrules.
  name: Microsoft Sentinel AlertRules API
  slug: microsoft-sentinel-alertrules-api
- description: The Bookmarks API from Microsoft Sentinel — 1 operation(s) for bookmarks.
  name: Microsoft Sentinel Bookmarks API
  slug: microsoft-sentinel-bookmarks-api
- description: The DataConnectors API from Microsoft Sentinel — 1 operation(s) for dataconnectors.
  name: Microsoft Sentinel DataConnectors API
  slug: microsoft-sentinel-dataconnectors-api
- description: The Incidents API from Microsoft Sentinel — 2 operation(s) for incidents.
  name: Microsoft Sentinel Incidents API
  slug: microsoft-sentinel-incidents-api
- description: The ThreatIntelligence API from Microsoft Sentinel — 1 operation(s) for threatintelligence.
  name: Microsoft Sentinel ThreatIntelligence API
  slug: microsoft-sentinel-threatintelligence-api
artifact_total: 12
collections:
- collection_type: open
  name: Microsoft Sentinel REST API
  slug: open-microsoft-sentinel
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-sentinel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-sentinel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-sentinel-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/microsoft-sentinel/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/sentinel/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/microsoft-sentinel/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=MicrosoftSentinelBlog
created: '2024-01-01'
description: Microsoft Sentinel is a cloud-native security information and event management (SIEM) and security orchestration, automation, and response (SOAR) solution. It provides REST APIs for managing incidents, analytics rules, threat intelligence, and automation playbooks.
finops:
- name: Microsoft Sentinel Finops
  service_category: API
  slug: microsoft-sentinel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-sentinel.png
layout: provider
modified: '2026-05-19'
name: Microsoft Sentinel
nav: Providers
network: true
overview: 'Microsoft Sentinel publishes 5 APIs on the [APIs.io](https://apis.io/) network, including AlertRules API, Bookmarks API, DataConnectors API, and 2 more. Tagged areas include Microsoft, Security, SIEM, SOAR, and Threat Detection.


  Microsoft Sentinel''s developer surface includes authentication, developer portal, documentation, pricing, getting-started guide, support, engineering blog, and 8 more developer resources.'
plans:
- name: Microsoft Sentinel Plans Pricing
  plan_count: 3
  slug: microsoft-sentinel-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Microsoft Sentinel Rate Limits
  slug: microsoft-sentinel-rate-limits
score:
  band: developing
  composite: 50.1
  delta: -2.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 50.0
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-sentinel/refs/heads/main/screenshots/microsoft-sentinel-2026-06-20T185532.png
security:
- kind: authentication
  name: Microsoft Sentinel Authentication
  slug: microsoft-sentinel-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Sentinel Domain Security
  slug: microsoft-sentinel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-sentinel
tags:
- Microsoft
- Security
- SIEM
- SOAR
- Threat Detection
website: https://azure.microsoft.com/en-us/products/microsoft-sentinel/
---
