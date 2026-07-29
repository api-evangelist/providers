---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for enriching CRM records with contact and company data, including verified emails, phone numbers, job titles, and firmographics. Available to enterprise Cognism customers; endpoints and quot
  name: Cognism Enrichment API
  slug: enrichment
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cognism-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognism-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cognism-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cognism
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cognism
- group: company
  title: ''
  type: Website
  url: https://www.cognism.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cognism.com/api
- group: commercial
  title: ''
  type: Plans
  url: plans/cognism-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cognism-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cognism-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cognism.com/blog/rss.xml
created: '2026-05-08'
description: Cognism is a B2B sales intelligence platform providing verified emails, mobile numbers (Diamond Data), firmographic data, intent signals, and enrichment. Cognism exposes APIs for enrichment and integration but they are gated and not publicly self-serve; access is granted to enterprise customers via partnerships and integrations.
finops:
- name: Cognism Finops
  service_category: Sales Intelligence
  slug: cognism-finops
graphqls:
- description: This conceptual GraphQL schema models the Cognism B2B sales intelligence platform, covering contact enrichment, company data, firmographics, phone and email verification, list management, CRM integrat
  name: Cognism GraphQL Schema
  slug: cognism-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cognism.png
layout: provider
modified: '2026-05-08'
name: Cognism
nav: Providers
network: true
overview: 'Cognism publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Intelligence, B2B, Enrichment, Contact Data, and GDPR.


  Cognism''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Cognism Plans Pricing
  plan_count: 1
  slug: cognism-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 1
  name: Cognism Rate Limits
  slug: cognism-rate-limits
score:
  band: thin
  composite: 31.8
  delta: 9.6
  facets:
    commercial_clarity: 36.8
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cognism/refs/heads/main/screenshots/cognism-2026-06-20T174713.png
security:
- kind: domain-security
  name: Cognism Domain Security
  slug: cognism-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cognism Vulnerability Disclosure
  slug: cognism-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cognism Trust Center
  slug: cognism-trust-center
  summary_line: SOC 2, ISO 27001
slug: cognism
tags:
- Sales Intelligence
- B2B
- Enrichment
- Contact Data
- GDPR
- Intent Data
website: https://www.cognism.com/
---
