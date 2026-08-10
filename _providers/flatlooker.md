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
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flatlooker-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flatlooker-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.flatlooker.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.manda.fr/tarifs
- group: company
  title: ''
  type: Blog
  url: https://www.manda.fr/ressources
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.manda.fr/hc/fr
- group: operate
  title: ''
  type: Support
  url: https://support.manda.fr/hc/fr
created: '2026-07-17'
description: Flatlooker (founded 2016) is a French digital real-estate agency for online rental search, tenant placement, and full rental property management (gestion locative). It now operates under the Manda brand (formerly Flatlooker and Hello Syndic); flatlooker.com redirects to manda.fr. Manda covers rental and property management, sales, condominium (syndic) management, and energy renovation for owners, tenants, investors, and co-ownerships across France, working primarily online — remote viewings, electronic dossiers and signatures, and mobile apps to track properties in real time — while relying on local agents in Paris, Lyon, and Marseille. Flatlooker was surfaced as a Partech portfolio company. It publishes no public developer API; this profile captures its live llms.txt and probed domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flatlooker.png
layout: provider
modified: '2026-07-19'
name: Flatlooker
nav: Providers
network: true
overview: 'Flatlooker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Real Estate, Property Management, and Rental.


  Flatlooker''s developer surface includes pricing, engineering blog, support, and 4 more developer resources.'
random_paper: 31
score:
  band: minimal
  composite: 9.1
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flatlooker/refs/heads/main/screenshots/flatlooker-2026-07-25T214724.png
security:
- kind: domain-security
  name: Flatlooker Domain Security
  slug: flatlooker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flatlooker
tags:
- Company
- Marketplace
- Real Estate
- Property Management
- Rental
- Proptech
- France
website: https://www.flatlooker.com/
---
