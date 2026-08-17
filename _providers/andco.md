---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/andco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.useandco.com
- group: start
  title: ''
  type: Login
  url: https://app.useandco.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/andco-llms.txt
created: '2026-07-17'
description: Andco is a Y Combinator (Spring 2026) startup building an AI-agent platform that automates the pre-litigation case workup process for personal injury law firms. Its agents retrieve and synthesize case documents across fax, phone, email, mail, web portal, and SMS channels, including police and accident reports, insurance coverage verification, medical records, and medical bills, then draft demand letters and calculate damages. Andco covers auto accident, premises liability, medical malpractice, workplace injury, and mass tort practice areas, offering same-day go-live and a free trial on the first case. This profile was surfaced from Andco's Y Combinator portfolio listing and enriched by the API Evangelist pipeline; Andco publishes no public API, developer portal, or machine-readable specification at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/andco.png
layout: provider
modified: '2026-07-17'
name: Andco
nav: Providers
network: true
overview: Andco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal Tech, Personal Injury, Legal, and AI Agents.
random_paper: 70
score:
  band: minimal
  composite: 8.4
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/andco/refs/heads/main/screenshots/andco-2026-07-25T200218.png
security:
- kind: domain-security
  name: Andco Domain Security
  slug: andco-domain-security
  summary_line: TLSv1.3 · DMARC
slug: andco
tags:
- Company
- Legal Tech
- Personal Injury
- Legal
- AI Agents
- Document Automation
- Y Combinator
website: https://www.useandco.com
---
