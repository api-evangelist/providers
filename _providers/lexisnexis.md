---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: 'The LexisNexis Developer Portal provides access to legal research and content APIs, allowing partners to integrate LexisNexis legal data and services directly into customer workflows. Access requires '
  name: LexisNexis Developer Portal
  slug: lexisnexis-developer-portal
- description: LexisNexis Risk Solutions offers fraud detection, identity verification, and risk orchestration capabilities through partner-accessed APIs, including the Dynamic Decision Platform, ThreatMetrix, and I
  name: LexisNexis Risk Solutions
  slug: lexisnexis-risk-solutions
- description: ThreatMetrix delivers digital identity intelligence and behavioral analytics for fraud prevention across user interactions, accounts, and channels. Integration is partner-only.
  name: LexisNexis ThreatMetrix
  slug: lexisnexis-threatmetrix
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/lexisnexis/plans/lexisnexis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lexisnexis-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lexisnexis/rate-limits/lexisnexis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lexisnexis-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lexisnexis/finops/lexisnexis-finops.yml
  title: ''
  type: FinOps
  url: finops/lexisnexis-finops.yml
- group: auth
  href: https://artifacts.apis.io/lexisnexis/security/lexisnexis-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lexisnexis-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/lexisnexis/security/lexisnexis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lexisnexis-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lexisnexis/security/lexisnexis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lexisnexis-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LexisNexis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lexisnexis
- group: company
  title: ''
  type: Website
  url: https://www.lexisnexis.com/
- group: other
  title: ''
  type: Developer
  url: https://dev.lexisnexis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://risk.lexisnexis.com/products
- group: agent
  title: ''
  type: LlmsText
  url: https://dev.lexisnexis.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.lexisnexis.com/blogs/sg
created: '2025-02-09'
description: LexisNexis is a global provider of legal, regulatory, and business information and analytics. Through the LexisNexis Developer Portal and LexisNexis Risk Solutions, partners can integrate access to legal research, fraud detection, identity verification, and risk assessment capabilities into their applications. Most LexisNexis APIs are partner-access only and require contractual agreements before credentials and OpenAPI specifications are released.
finops:
- has_sources: false
  method: generated
  name: Lexisnexis Finops
  primary_unit: request
  service_category: API
  slug: lexisnexis-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lexisnexis.png
layout: provider
modified: '2026-04-28'
name: LexisNexis
nav: Providers
network: true
overview: 'LexisNexis is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Risk Management, Identity Verification, Fraud Prevention, and Compliance.


  LexisNexis'' developer surface includes documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Lexisnexis Plans Pricing
  plan_count: 3
  slug: lexisnexis-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Lexisnexis Rate Limits
  slug: lexisnexis-rate-limits
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 69.6
    operational_transparency: 21.1
  previous_composite: 15.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lexisnexis/lexisnexis-2026-06-20T184446.png
security:
- kind: domain-security
  name: Lexisnexis Domain Security
  slug: lexisnexis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lexisnexis Vulnerability Disclosure
  slug: lexisnexis-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Lexisnexis Trust Center
  slug: lexisnexis-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: lexisnexis
tags:
- Legal
- Risk Management
- Identity Verification
- Fraud Prevention
- Compliance
- Analytics
- Data
website: https://www.lexisnexis.com/
---
