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
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: A service that provides solutions relating to marketing and/or transactional email and/or SMS
  name: Sendinblue
  slug: sendinblue
artifact_total: 4
asyncapis:
- description: AsyncAPI description of the outbound webhook surface for Brevo (formerly Sendinblue). Brevo delivers event notifications by issuing HTTP POST requests with a JSON body to a URL configured by the custo
  name: Brevo (Sendinblue) Webhooks
  slug: sendinblue-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendinblue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developers.sendinblue.com/docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: A service that provides solutions relating to marketing and/or transactional email and/or SMS
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sendinblue.png
layout: provider
modified: '2026-05-30'
name: Sendinblue
nav: Providers
network: true
overview: 'Sendinblue publishes 1 API on the [APIs.io](https://apis.io/) network: Sendinblue. Tagged areas include Email and Public APIs.


  The Sendinblue catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 64
rules:
- name: Sendinblue API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: sendinblue-asyncapi-spectral-rules
score:
  band: emerging
  composite: 24.3
  delta: 2.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 54.3
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 41.7
    operational_transparency: 0.0
  previous_composite: 21.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendinblue/refs/heads/main/screenshots/sendinblue-2026-06-20T193701.png
security:
- kind: domain-security
  name: Sendinblue Domain Security
  slug: sendinblue-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sendinblue
tags:
- Email
- Public APIs
website: https://developers.sendinblue.com/docs
---
