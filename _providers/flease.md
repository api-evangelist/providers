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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flease-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flease.fr/
- group: start
  title: ''
  type: Login
  url: https://webapp.flease.fr/
- group: company
  title: ''
  type: Blog
  url: https://www.flease.fr/blog
- group: operate
  title: ''
  type: Support
  url: https://www.flease.fr/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flease.fr/legal/politique-de-confidentialite
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flease.fr/legal/conditions-generales-dutilisation
created: '2026-07-17'
description: Flease is a French vehicle-leasing marketplace offering flexible long-term (LLD, 24-50 month) and medium-term (LMD, 1-12 month) car and utility-vehicle rental to SMEs and small businesses. It sources quasi-new vehicles (under two years old, fewer than 30,000 km), delivers within a week for LMD and a month for LLD, and bundles a fleet-management web application (webapp.flease.fr) for tracking mileage, drivers, maintenance, contracts, and invoices. Flease positions on transparent pricing and a roughly 20% lower total cost of ownership versus traditional leasing, with a circular-economy angle of redeploying used vehicles. Backed by Partech. No public developer API or documentation is published; the customer-facing webapp is a Vue single-page app authenticated with AWS Cognito.
image: https://www.flease.fr/img/icons/favicon.ico
layout: provider
modified: '2026-07-19'
name: Flease
nav: Providers
network: true
overview: 'Flease is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Automotive, Vehicle Leasing, and Fleet Management.


  Flease''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 54
score:
  band: emerging
  composite: 13.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flease/refs/heads/main/screenshots/flease-2026-07-25T214726.png
security:
- kind: domain-security
  name: Flease Domain Security
  slug: flease-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flease
tags:
- Company
- Marketplace
- Automotive
- Vehicle Leasing
- Fleet Management
- Mobility
- France
website: https://www.flease.fr/
---
