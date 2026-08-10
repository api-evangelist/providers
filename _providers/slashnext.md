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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: RESTful phishing threat intelligence API. Look up URL/host reputation, run real-time SEER-engine URL scans (async url/scan and blocking url/scansync), pull forensic downloads (screenshot/html/text) by
  name: SlashNext On-demand Threat Intelligence (OTI) API
  slug: slashnext-on-demand-threat-intelligence-oti-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://slashnext.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.varonis.com/platform/email-security
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/slashnext-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/slashnext-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/slashnext-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/slashnext-error-codes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slashnext-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/slashnext-llms.txt
created: '2026-07-17'
description: SlashNext is an AI-native phishing and social-engineering threat detection company founded by Atif Mushtaq (an architect of FireEye's core malware sandbox). Its Real-Time Phishing Threat Intelligence is delivered through the SlashNext On-demand Threat Intelligence (OTI) REST API at oti.slashnext.cloud, which offers URL and host reputation lookups, real-time cloud SEER-engine URL scanning in both asynchronous and blocking modes, and forensic downloads (screenshot, HTML, and rendered text) keyed by scan id, plus per-tenant API quota status. Responses are available as JSON, CSV, or plaintext and every request authenticates with a per-tenant API key passed as the authkey parameter. SlashNext was acquired by Varonis Systems in August 2025 and its detection capabilities are being integrated into the Varonis Email Security and MDDR platform.
image: https://slashnext.com/wp-content/uploads/2021/03/SlashNext-Logo.png
layout: provider
modified: '2026-07-21'
name: SlashNext
nav: Providers
network: true
overview: 'SlashNext publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Phishing, and Threat Intelligence.


  SlashNext''s developer surface includes documentation, authentication, and 6 more developer resources.'
random_paper: 58
score:
  band: minimal
  composite: 11.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Slashnext Authentication
  slug: slashnext-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Slashnext Domain Security
  slug: slashnext-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: slashnext
tags:
- Company
- Security
- Cybersecurity
- Phishing
- Threat Intelligence
- Email Security
- Anti-Phishing
- API
website: https://slashnext.com
---
