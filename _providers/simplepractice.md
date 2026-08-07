---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Partner-only integration announced by SimplePractice Enterprise (September 2022) that connects to overlapping SimplePractice provider accounts so that Employee Assistance Programs (EAPs), Managed Care
  name: SimplePractice Enterprise Scheduling API
  slug: simplepractice-enterprise-scheduling-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/simplepractice-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simplepractice-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simplepractice
- group: company
  title: ''
  type: Website
  url: https://www.simplepractice.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/simplepractice
- group: docs
  title: ''
  type: Documentation
  url: https://www.simplepractice.com/press/simplepractice-enterprise-launches-api/
- group: commercial
  title: ''
  type: Plans
  url: plans/simplepractice-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/simplepractice-finops.yml
created: '2026-07-10'
description: SimplePractice is a cloud-based practice management platform and EHR for behavioral and mental health, therapy, and wellness practices, covering scheduling, client management, telehealth, intake and clinical documentation, insurance and superbill billing, and a secure client portal (Client Secure Messaging). As of this cataloging, SimplePractice does NOT publish a public, self-serve developer API - there is no developer portal, no documented REST endpoints, no OpenAPI, and no webhooks for third parties. The only programmatic surface is the partner-only SimplePractice Enterprise scheduling integration, which lets EAPs and Managed Care Organizations view in-network provider availability and request appointments; it is delivered through customized partnerships rather than as public developer documentation. Third-party pages that advertise a "stable SimplePractice REST API" for clients, appointments, notes, or billing are unofficial and not backed by any SimplePractice developer
  program.
finops:
- name: Simplepractice Finops
  service_category: Practice Management and EHR
  slug: simplepractice-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simplepractice.png
layout: provider
modified: '2026-07-25'
name: SimplePractice
nav: Providers
network: true
overview: 'SimplePractice publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Behavioral Health, Mental Health, EHR, Practice Management, and Healthcare.


  SimplePractice''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Simplepractice Plans Pricing
  plan_count: 5
  slug: simplepractice-plans-pricing
random_paper: 24
score:
  band: emerging
  composite: 16.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 16.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Simplepractice Domain Security
  slug: simplepractice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Simplepractice Vulnerability Disclosure
  slug: simplepractice-vulnerability-disclosure
  summary_line: disclosure policy published
slug: simplepractice
tags:
- Behavioral Health
- Mental Health
- EHR
- Practice Management
- Healthcare
- Scheduling
- Telehealth
- HIPAA
- Partner API
- No Public API
website: https://www.simplepractice.com
---
