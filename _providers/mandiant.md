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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: The Mandiant Advantage Threat Intelligence (MATI) API v3 provides programmatic access to Mandiant's threat intelligence, including indicators of compromise, finished intelligence reports, threat actor
  name: Mandiant Threat Intelligence API v3
  slug: mandiant-threat-intelligence-api-v3
- description: The Digital Threat Monitoring API surfaces exposed credentials, leaked data and brand/deep-and-dark-web threats monitored by Mandiant Advantage. It is served from the Mandiant intelligence API host an
  name: Mandiant Digital Threat Monitoring API
  slug: mandiant-digital-threat-monitoring-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mandiant.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mandiant.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mandiant.com/home/mati-threat-intelligence-api-v3
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/topics/threat-intelligence
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mandiant
- group: start
  title: ''
  type: Login
  url: https://advantage.mandiant.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/mandiant-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mandiant-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mandiant-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mandiant-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mandiant-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mandiant-llms.txt
created: '2026-07-17'
description: Mandiant, now part of Google Cloud, is a threat intelligence and cyber defense company whose Mandiant Advantage platform exposes several authenticated REST APIs documented at docs.mandiant.com. The Threat Intelligence (MATI) API v3 serves indicators, finished intelligence reports, threat actors, malware families, vulnerabilities and campaigns; the Digital Threat Monitoring API surfaces exposed credentials and brand/deep-and-dark-web threats; the Attack Surface Management API inventories an organization's external assets; and the Security Validation (MSV) API drives automated testing of security controls. These APIs authenticate with an API key and secret that is exchanged for a short-lived bearer access token. Mandiant's frontline threat data now also powers Google Threat Intelligence alongside VirusTotal.
image: https://avatars.githubusercontent.com/mandiant
layout: provider
modified: '2026-07-20'
name: Mandiant
nav: Providers
network: true
overview: 'Mandiant publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Threat Intelligence, Cybersecurity, and Incident Response.


  Mandiant''s developer surface includes documentation, API reference, engineering blog, authentication, and 8 more developer resources.'
random_paper: 53
score:
  band: emerging
  composite: 19.4
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 19.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mandiant/refs/heads/main/screenshots/mandiant-2026-07-25T230027.png
security:
- kind: authentication
  name: Mandiant Authentication
  slug: mandiant-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Mandiant Domain Security
  slug: mandiant-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: mandiant
tags:
- Company
- Security
- Threat Intelligence
- Cybersecurity
- Incident Response
- Attack Surface Management
- Vulnerability Intelligence
- Malware
- Google Cloud
website: https://docs.mandiant.com
---
