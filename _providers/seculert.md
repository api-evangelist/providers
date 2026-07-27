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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seculert-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seculert.com
created: '2026-07-17'
description: 'Seculert was an Israeli cybersecurity company that provided cloud-based automated threat and attack detection, analytics, and breach-detection services, correlating outbound traffic and threat intelligence to identify compromised devices. Backed by Norwest Venture Partners, it was acquired by Radware in January 2017 and folded into Radware''s cloud security portfolio; the independent seculert.com brand is now defunct. This enrichment pass found no live independent API surface: the apex domain no longer serves TLS, www.seculert.com redirects to a dead HubSpot landing page, and no /.well-known, llms.txt, or developer/API documentation is published. Retained as a network profile of an acquired, now-inactive provider; DNS records (DMARC ruf to dmarc@radware.com) corroborate the Radware ownership.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seculert.png
layout: provider
modified: '2026-07-21'
name: Seculert
nav: Providers
network: true
overview: Seculert is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Threat Detection, Security, and Analytics.
random_paper: 55
score:
  band: minimal
  composite: 6.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Seculert Domain Security
  slug: seculert-domain-security
  summary_line: DMARC
slug: seculert
tags:
- Company
- Cybersecurity
- Threat Detection
- Security
- Analytics
- Acquired
- Defunct
website: https://seculert.com
---
