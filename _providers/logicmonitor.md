---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: LogicMonitor is an AI-powered infrastructure monitoring and observability platform for hybrid IT environments.
  name: LogicMonitor
  slug: logicmonitor
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/logicmonitor-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logicmonitor-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/logicmonitor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/logicmonitor
- group: company
  title: ''
  type: Website
  url: https://www.logicmonitor.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.logicmonitor.com/support
created: '2026-03-27'
description: LogicMonitor is an AI-powered infrastructure monitoring and observability platform for hybrid IT environments.
finops:
- name: Logicmonitor Finops
  service_category: API
  slug: logicmonitor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logicmonitor.png
layout: provider
modified: '2026-03-27'
name: LogicMonitor
nav: Providers
network: true
overview: 'LogicMonitor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps and Monitoring.


  LogicMonitor''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Logicmonitor Plans Pricing
  plan_count: 3
  slug: logicmonitor-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 5
  name: Logicmonitor Rate Limits
  slug: logicmonitor-rate-limits
score:
  band: emerging
  composite: 12.1
  delta: -0.2
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/logicmonitor/refs/heads/main/screenshots/logicmonitor-2026-06-20T184653.png
security:
- kind: domain-security
  name: Logicmonitor Domain Security
  slug: logicmonitor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Logicmonitor Trust Center
  slug: logicmonitor-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: logicmonitor
tags:
- AIOps
- Monitoring
website: https://www.logicmonitor.com
---
