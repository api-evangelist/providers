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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arca-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://arcawealth.ai/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arca-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arca-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/arca-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arca-llms.txt
- group: company
  title: ''
  type: Website
  url: https://arcawealth.ai
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/arca
created: '2026-07-17'
description: 'Arca (Arca Financial, Inc.) is an AI-native wealth management company founded by former Plaid product leader Rron Rexha and headquartered in New York. It pairs human financial advisors with a fully integrated, agentic platform in which AI agents are the primary operational users: monitoring emails, calls, documents, market data, and news, coordinating with one another, generating dynamic user interfaces, and executing multi-step advisory workflows so advisors can focus on client relationships. Arca is an SEC-registered investment adviser managing over $1 billion in client assets, and raised $64M across a seed round (led by Venrock) and a Series A (led by General Catalyst, with Index Ventures and Venrock). It has no public developer API surface at this time; this profile captures its public identity and security posture.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arca.png
layout: provider
modified: '2026-07-18'
name: Arca
nav: Providers
network: true
overview: Arca is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Fintech, Financial Services, and Wealth Management.
random_paper: 7
score:
  band: minimal
  composite: 8.2
  delta: 0.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arca/refs/heads/main/screenshots/arca-2026-07-25T201009.png
security:
- kind: domain-security
  name: Arca Domain Security
  slug: arca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arca Vulnerability Disclosure
  slug: arca-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arca
tags:
- Company
- Ai Ml
- Fintech
- Financial Services
- Wealth Management
- Wealth Advisory
- AI Agents
- Agentic Platform
website: https://arcawealth.ai
---
