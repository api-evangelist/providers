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
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.pave.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pave.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.pave.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.pave.com/insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pave.com/company/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pave.com/company/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.pave.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.pave.com/company/security-and-privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pave-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pave-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pave-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.pave.com/company/security-and-privacy
created: '2026-07-17'
description: Pave is an AI-native compensation management platform that helps organizations make data-driven pay decisions. It combines real-time market benchmarking (compensation data sourced from 9,000+ companies), automated market pricing and salary-range building, merit-cycle and compensation-planning workflows, an employee-facing total rewards portal, and visual offer letters into one system. Pave connects to HRIS, ATS, equity-management, and performance-management systems to create a single source of truth for an organization's compensation ecosystem. Pave does not currently publish a public developer API or developer portal; its integration surface is inbound connectors to systems of record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pave.png
layout: provider
modified: '2026-07-20'
name: Pave
nav: Providers
network: true
overview: 'Pave is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Compensation, Human Resources, Compensation Benchmarking, and Market Data.


  Pave''s developer surface includes pricing, support, engineering blog, and 9 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 18.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pave/refs/heads/main/screenshots/pave-2026-08-07T191625.png
security:
- kind: domain-security
  name: Pave Domain Security
  slug: pave-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Pave Vulnerability Disclosure
  slug: pave-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Pave Trust Center
  slug: pave-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: pave
tags:
- Company
- Compensation
- Human Resources
- Compensation Benchmarking
- Market Data
- People Analytics
- HR Tech
- Total Rewards
website: https://www.pave.com/
---
