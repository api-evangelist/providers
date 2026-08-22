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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Administrator-facing API for integrating NetBeez network-performance telemetry with external tools. v2 is a JSON API (read-write: create targets, run ad-hoc tests) documented on Postman at api.netbeez'
  name: NetBeez API
  slug: netbeez-api
artifact_total: 4
asyncapis:
- description: ''
  name: Netbeez Alerts Webhooks
  slug: netbeez-alerts-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://netbeez.net/
- group: docs
  title: ''
  type: Documentation
  url: https://help.netbeez.net/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.netbeez.net/en/
- group: docs
  title: ''
  type: APIReference
  url: https://help.netbeez.net/en/collections/11391846-integrations-and-api
- group: operate
  title: ''
  type: Support
  url: https://community.netbeez.net/
- group: company
  title: ''
  type: Blog
  url: https://netbeez.net/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://netbeez.net/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://netbeez.net/pricing#request-form
- group: commercial
  title: ''
  type: TermsOfService
  url: https://netbeez.net/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://netbeez.net/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.netbeez.net/en/collections/11391847-version-release-notes
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netbeez-domain-security.yml
created: '2026-07-17'
description: 'NetBeez is a network performance monitoring platform that measures the end-user experience across distributed enterprise, remote-worker, and Wi-Fi networks. Hardware and software agents (including Raspberry Pi, Docker, and network-device-hosted agents on Cisco, Extreme, Cumulus, and Nutanix gear) run continuous and ad-hoc tests — ping, HTTP, DNS, traceroute, path analysis, Wi-Fi, and cellular — and report granular one-second-interval metrics to a central dashboard for real-time alerting and historical troubleshooting. The NetBeez API lets dashboard administrators integrate this telemetry with external tools, reporting, and analytics: a JSON-based v2 API documented on Postman at api.netbeez.net supports read and write operations (create targets, run ad-hoc tests), while a deprecated read-only v1 Swagger API is served per-instance. Alerting integrates outbound via webhooks and pre-built connectors for PagerDuty, Slack, Splunk, Microsoft Teams, ServiceNow, SNMP, syslog, and email.
  NetBeez was surfaced as a portfolio company of Partech.'
image: https://netbeez.net/wp-content/uploads/2021/03/netbeez-logo.png
layout: provider
modified: '2026-07-20'
name: Netbeez
nav: Providers
network: true
overview: 'Netbeez publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure SaaS, Network Monitoring, Network Performance Monitoring, and Observability.


  The Netbeez catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Netbeez''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, changelog, and 5 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 33.9
  delta: -1.2
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 45.1
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 35.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netbeez/refs/heads/main/screenshots/netbeez-2026-08-07T184928.png
security:
- kind: authentication
  name: Netbeez Authentication
  slug: netbeez-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Netbeez Domain Security
  slug: netbeez-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: netbeez
tags:
- Company
- Infrastructure SaaS
- Network Monitoring
- Network Performance Monitoring
- Observability
- Wi-Fi Monitoring
- Digital Experience Monitoring
- API
website: https://netbeez.net/
---
