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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 11.5
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dehaze-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dehaze-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dehaze-domain-security.yml
- group: company
  title: ''
  type: About
  url: https://www.dehaze.de/about
- group: company
  title: ''
  type: Careers
  url: https://www.dehaze.de/careers
- group: company
  title: ''
  type: Press
  url: https://www.dehaze.de/press
- group: company
  title: ''
  type: Website
  url: https://dehaze.de/
created: '2026-07-17'
description: dehaze is a Munich-area (Fürstenfeldbruck, Germany) healthtech company, part of the Techstars Berlin cohort, building proprietary causal AI infrastructure that detects chronic and autoimmune disease earlier by identifying overlooked diagnoses, health risks, and inappropriate treatments. Its platform unifies and harmonizes diverse health data (lab results, medical imaging, genomics, clinical notes) into doctor-validated patient journeys, risk-profiles individuals against millions of health journeys and medical guidelines, and runs targeted AI follow-ups to improve treatment adherence for patients, payers, and providers. dehaze has analyzed over 250,000 patient lives across 300 million health events and 200+ AI algorithms, and raised €3.2M in 2026. dehaze publishes no first-party developer API; it exposes a Wix Site MCP endpoint and an llms.txt for agentic AI access to public site content.
image: https://static.wixstatic.com/media/2f3c0d_42767967d90a40f58e3c1dc8c413b9a4~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: dehaze-mcp.yml
  slug: dehaze-mcpyml
modified: '2026-07-18'
name: dehaze
nav: Providers
network: true
overview: dehaze is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthtech, Artificial Intelligence, Machine Learning, and Digital Health.
random_paper: 13
score:
  band: minimal
  composite: 8.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dehaze/refs/heads/main/screenshots/dehaze-2026-07-25T211635.png
security:
- kind: domain-security
  name: Dehaze Domain Security
  slug: dehaze-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dehaze
tags:
- Company
- Healthtech
- Artificial Intelligence
- Machine Learning
- Digital Health
- Chronic Disease
- Diagnostics
- Data Harmonization
- Techstars
- Germany
website: https://dehaze.de/
---
