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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
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
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/lexisnexis-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lexisnexis-vulnerability-disclosure.yml
- group: auth
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
- name: Lexisnexis Finops
  service_category: API
  slug: lexisnexis-finops
graphqls:
- description: LexisNexis provides legal research, news, and business intelligence data. The API covers legal case search, statute retrieval, news aggregation, company profiles, and Accurint identity data for law fi
  name: LexisNexis GraphQL API
  slug: lexisnexis-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lexisnexis.png
layout: provider
modified: '2026-04-28'
name: LexisNexis
nav: Providers
network: true
overview: 'LexisNexis publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Risk, Identity Verification, Fraud Detection, and Compliance.


  LexisNexis'' developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Lexisnexis Plans Pricing
  plan_count: 3
  slug: lexisnexis-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Lexisnexis Rate Limits
  slug: lexisnexis-rate-limits
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 11.9
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 25.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lexisnexis/refs/heads/main/screenshots/lexisnexis-2026-06-20T184446.png
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
- Risk
- Identity Verification
- Fraud Detection
- Compliance
- Analytics
- Data
website: https://www.lexisnexis.com/
---
