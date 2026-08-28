---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: The FTC Developer Portal is the central hub for developer documentation, data dictionaries, and access program details for FTC-managed datasets and services.
  name: FTC Developer Portal
  slug: developer-portal
- description: The National Do Not Call Registry program lets telemarketers and sellers download phone-number data they must scrub against before placing calls. Access is provisioned through telemarketer.donotcall.g
  name: National Do Not Call Registry
  slug: do-not-call-registry
- description: Consumer Sentinel is the FTC's secure online database of consumer reports of fraud, identity theft, and other complaints, made available to participating federal, state, local, and international law e
  name: Consumer Sentinel Network
  slug: consumer-sentinel
- description: The Hart-Scott-Rodino (HSR) Premerger Notification Program coordinates premerger filings reviewed by the FTC and DOJ. Filings are submitted electronically through the dedicated HSR e-filing system.
  name: HSR Premerger Notification
  slug: hsr-premerger
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-trade-commission-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FederalTradeCommission
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-trade-commission
- group: company
  title: ''
  type: Website
  url: https://www.ftc.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ftc.gov/developer
- group: company
  title: ''
  type: News
  url: https://www.ftc.gov/news-events
- group: other
  title: ''
  type: Open Data
  url: https://www.ftc.gov/policy/research
- group: other
  title: ''
  type: Consumer Resources
  url: https://consumer.ftc.gov
- group: company
  title: ''
  type: Blog
  url: https://www.ftc.gov/feeds/press-release.xml
created: '2024-12-03'
description: The Federal Trade Commission (FTC) is a U.S. federal agency that enforces antitrust and consumer protection laws affecting virtually every area of commerce. The FTC publishes developer-facing data products and APIs through ftc.gov/developer and partner platforms, including the National Do Not Call Registry telemarketer access program and the Consumer Sentinel Network of consumer complaint data shared with law enforcement.
finops:
- name: Federal Trade Commission Finops
  service_category: API
  slug: federal-trade-commission-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-trade-commission.png
layout: provider
modified: '2026-04-28'
name: Federal Trade Commission
nav: Providers
network: true
overview: 'Federal Trade Commission publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Antitrust, Consumer Protection, Do Not Call, Federal-Government, and Law Enforcement.


  Federal Trade Commission''s developer surface includes documentation, product news, engineering blog, and 6 more developer resources.'
plans:
- name: Federal Trade Commission Plans Pricing
  plan_count: 3
  slug: federal-trade-commission-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Federal Trade Commission Rate Limits
  slug: federal-trade-commission-rate-limits
score:
  band: emerging
  composite: 11.8
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-trade-commission/refs/heads/main/screenshots/federal-trade-commission-2026-06-20T181129.png
security:
- kind: domain-security
  name: Federal Trade Commission Domain Security
  slug: federal-trade-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-trade-commission
tags:
- Antitrust
- Consumer Protection
- Do Not Call
- Federal-Government
- Law Enforcement
- Open Data
website: https://www.ftc.gov/
---
