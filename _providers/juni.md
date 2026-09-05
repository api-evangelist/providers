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
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/juni-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/juni-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.juni.co/
- group: operate
  title: ''
  type: Support
  url: https://help.juni.co/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.juni.co/price-plans
- group: start
  title: ''
  type: SignUp
  url: https://app.juni.co/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.juni.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.juni.co/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.juni.co/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/juni-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/juni-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.juni.co/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/juni-llms.txt
created: '2026-07-17'
description: 'Juni is a Swedish fintech (headquartered in Göteborg, founded 2020) that provides a financial platform for ecommerce and digital businesses: business banking with multi-currency accounts, corporate and virtual cards, local and global payments, spend management, working-capital financing, and AI-driven accounting with integrations such as Fortnox. Juni is a licensed payment institution under the oversight of the Swedish Financial Supervisory Authority (SFSA) and is backed by EQT Ventures. It exposes a regulatory PSD2 / Open Banking (ASPSP) API surface for third-party providers, but publishes no public product API, SDKs, or developer portal. This profile was added to the API Evangelist network as a portfolio lead and enriched by the pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/juni.png
layout: provider
modified: '2026-07-19'
name: Juni
nav: Providers
network: true
overview: 'Juni is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking, Spend Management, and Payments.


  Juni''s developer surface includes support, pricing, signup flow, and 10 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 17.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 25.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Juni Domain Security
  slug: juni-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Juni Trust Center
  slug: juni-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: juni
tags:
- Company
- Fintech
- Banking
- Spend Management
- Payments
- E-Commerce
- Corporate Cards
- Open Banking
- Sweden
website: https://www.juni.co/
---
