---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Seon Agentic Access
  operation_count: 6
  slug: seon-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 6
apis:
- description: Sanctions, watchlist, PEP, and adverse-media screening.
  name: SEON AML API
  slug: seon-aml-api
- description: Email address digital footprint and risk scoring.
  name: SEON Email API
  slug: seon-email-api
- description: Combined transaction fraud scoring.
  name: SEON Fraud API
  slug: seon-fraud-api
- description: IP address proxy/VPN/Tor detection and risk scoring.
  name: SEON IP API
  slug: seon-ip-api
- description: Transaction outcome labeling for machine-learning feedback.
  name: SEON Labels API
  slug: seon-labels-api
- description: Phone number digital footprint and risk scoring.
  name: SEON Phone API
  slug: seon-phone-api
artifact_total: 14
collections:
- collection_type: open
  name: SEON REST API
  slug: open-seon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/seon-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/seon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seon-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seontechnologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/seon-tech
- group: company
  title: ''
  type: Website
  url: https://seon.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.seon.io
- group: commercial
  title: ''
  type: Plans
  url: plans/seon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/seon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/seon-finops.yml
created: '2026-06-25'
description: SEON provides fraud prevention and anti-money-laundering APIs that combine digital-footprint analysis, device fingerprinting, and machine-learning risk scoring. The SEON REST API returns real-time fraud scores and enriched intelligence from an email address, phone number, or IP address, plus a combined transaction Fraud API and AML screening, accessed over HTTPS with an X-API-KEY header.
finops:
- name: Seon Finops
  service_category: Security and Identity
  slug: seon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seon.png
layout: provider
modified: '2026-06-25'
name: SEON
nav: Providers
network: true
overview: 'SEON publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AML API, Email API, Fraud API, and 3 more. Tagged areas include Fraud Prevention, Risk Scoring, Digital Footprint, AML, and Identity.


  SEON''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Seon Plans Pricing
  plan_count: 3
  slug: seon-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 7
  name: Seon Rate Limits
  slug: seon-rate-limits
score:
  band: thin
  composite: 41.5
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Seon Authentication
  slug: seon-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Seon Domain Security
  slug: seon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Seon Trust Center
  slug: seon-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: seon
tags:
- Fraud Prevention
- Risk Scoring
- Digital Footprint
- AML
- Identity
website: https://seon.io/
---
