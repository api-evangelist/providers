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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/withcoverage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://withcoverage.com
- group: start
  title: ''
  type: Login
  url: https://app.withcoverage.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.withcoverage.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withcoverage.com/legal/privacy
created: '2026-07-17'
description: WithCoverage is a technology-driven risk management and commercial insurance platform that aims to replace the traditional insurance broker for growing businesses. It pairs a team of insurance advisors, claims specialists, and attorneys with an AI-powered digital platform to analyze policies, reduce premiums, manage certificates of insurance, and handle claims proactively as companies scale. Headquartered in New York City and backed by venture investors including 8vc, WithCoverage operates in the insurtech sector. This API Evangelist profile was created as a portfolio lead and enriched by the pipeline; the company currently exposes no public developer API surface (client access is through the app.withcoverage.com web application).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/withcoverage.png
layout: provider
modified: '2026-07-21'
name: Withcoverage
nav: Providers
network: true
overview: Withcoverage is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurtech, Insurance, Risk Management, and Commercial Insurance.
random_paper: 7
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/withcoverage/refs/heads/main/screenshots/withcoverage-2026-09-02T170846.png
security:
- kind: domain-security
  name: Withcoverage Domain Security
  slug: withcoverage-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: withcoverage
tags:
- Company
- Insurtech
- Insurance
- Risk Management
- Commercial Insurance
- Brokerage
- Claims
- Fintech
website: https://withcoverage.com
---
