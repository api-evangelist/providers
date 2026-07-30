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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'HTTP Reports API for accredited registrars: retrieves weekly domain and billing report files (CSV, gzip-compressed) from the Identity Digital registry. Authenticated with registrar login credentials o'
  name: Identity Digital Reports API
  slug: identity-digital-reports-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/donuts-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://donuts.domains
- group: docs
  title: ''
  type: Documentation
  url: https://www.identity.digital/help-categories/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.identity.digital/help-articles/reports-api
- group: operate
  title: ''
  type: Support
  url: https://www.identity.digital/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.identity.digital/newsroom
- group: start
  title: ''
  type: Login
  url: https://registrar.identitydigital.services/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.identity.digital/policies/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.identity.digital/policies/privacy-policy
created: '2026-07-17'
description: 'Donuts (now operating as Identity Digital, following the 2022 merger of Donuts Inc. and Afilias) runs the world''s largest portfolio of new generic top-level domains (gTLDs) — more than 280 extensions such as .email, .guru, .social, .live, and .restaurant. As a wholesale domain registry it provides DNS infrastructure, domain-name security, premium-domain services, and rights-protection tooling to the accredited registrars and resellers who sell domains to end customers. Its programmatic surface is registry-oriented and partner-facing: an EPP (Extensible Provisioning Protocol) interface for domain provisioning, a HTTP Reports API that delivers weekly domain and billing report files (CSV.gz over HTTP basic auth), and a Registrar Portal. There is no public REST/OpenAPI developer surface.'
image: https://cdn.prod.website-files.com/643d4b3fc3e02d37e33dd7d5/64931155928ec2e64df108cf_img_opengraph.jpg
layout: provider
modified: '2026-07-18'
name: Donuts
nav: Providers
network: true
overview: 'Donuts publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Domains, DNS, and Domain Registry.


  Donuts'' developer surface includes documentation, API reference, support, engineering blog, and 5 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 18.0
  delta: -2.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/donuts/refs/heads/main/screenshots/donuts-2026-07-25T212257.png
security:
- kind: domain-security
  name: Donuts Domain Security
  slug: donuts-domain-security
  summary_line: TLSv1.3 · DMARC
slug: donuts
tags:
- Company
- Infrastructure
- Domains
- DNS
- Domain Registry
- gTLD
- Registrar
- EPP
website: https://donuts.domains
---
