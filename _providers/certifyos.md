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
- description: 'RESTful v2 API for healthcare provider data management. Endpoints create, retrieve, and manage provider and facility profiles, run real-time primary source verification (PSV), retrieve CAQH data, and '
  name: CertifyOS Provider Data API
  slug: certifyos-provider-data-api
artifact_total: 3
asyncapis:
- description: ''
  name: Certifyos Webhooks
  slug: certifyos-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/certifyos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.certifyos.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://provider.certifyos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://knowledgebase.certifyos.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.certifyos.com/resources/blog/api-future-of-provider-data
- group: operate
  title: ''
  type: Support
  url: https://certifyos.atlassian.net/servicedesk/customer/portal/53
- group: company
  title: ''
  type: Blog
  url: https://www.certifyos.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/certifyos
- group: operate
  title: ''
  type: StatusPage
  url: https://status.certifyos.com/
- group: start
  title: ''
  type: SignUp
  url: https://ng.certifyos.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.certifyos.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.certifyos.com/privacy
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/certifyos-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/certifyos-lifecycle.yml
created: '2026-07-17'
description: 'CertifyOS is a healthcare provider data platform that delivers a single, AI-enabled source of truth for provider information. Founded in 2021 by former Oscar Health employees and led by CEO Anshul Rathi, the New York-based company offers an API-first platform that automates every stage of provider network management: credentialing, licensing, payer enrollment, compliance monitoring, roster management, and provider data management. CertifyOS connects directly to 600+ primary sources (including CAQH and NPPES) for real-time primary source verification (PSV), and exposes verified provider data to downstream systems through a RESTful v2 API, webhooks, and bulk exports. It serves payers, health systems, multi-state provider groups, and rapidly scaling digital-health companies. Backed by General Catalyst (Series A) and Transformation Capital (Series B).'
image: https://www.certifyos.com/certifyos-favicon.png
layout: provider
modified: '2026-07-18'
name: Certifyos
nav: Providers
network: true
overview: 'Certifyos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Provider Data, Credentialing, and Licensing.


  The Certifyos catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Certifyos'' developer surface includes documentation, API reference, support, engineering blog, signup flow, and 9 more developer resources.'
random_paper: 60
score:
  band: thin
  composite: 33.6
  delta: 2.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 31.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/certifyos/refs/heads/main/screenshots/certifyos-2026-07-25T205001.png
security:
- kind: domain-security
  name: Certifyos Domain Security
  slug: certifyos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: certifyos
tags:
- Company
- Healthcare
- Provider Data
- Credentialing
- Licensing
- Payer Enrollment
- Compliance Monitoring
- Primary Source Verification
- Provider Network Management
- Roster Management
- Healthcare API
website: https://www.certifyos.com/
---
