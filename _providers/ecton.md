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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ecton-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ecton.io
- group: company
  title: ''
  type: About
  url: https://www.ecton.io/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.ecton.io/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.ecton.io/patient-sign-up-login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ecton.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ecton.io/terms-of-use
- group: operate
  title: ''
  type: ChangeLog
  url: https://guttural-scribe-930.notion.site/Monthly-release-notes-1985a709258f80fa921beccd12ca4dce
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.ecton.io/vulnerability-disclosure
- group: auth
  title: ''
  type: Security
  url: https://www.ecton.io/vulnerability-disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://www.ecton.io/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ecton-io
created: '2026-07-17'
description: Ecton, Inc. is an AI-powered patient payments platform focused on reducing the financial stress and financial toxicity that surround healthcare costs. Its flagship product, Toni, is an AI financial counselor that gives patients personalized guidance on medical bills, insurance, and payment options, paired with a Health Savings and Spending Wallet for managing and paying healthcare expenses. Ecton helps healthcare providers strengthen patient relationships, improve treatment adherence, and increase revenue collection. The company is HIPAA-aligned and backed by General Catalyst. Ecton does not currently publish a public developer API or documentation surface; this profile captures its identity and public security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ecton.png
layout: provider
modified: '2026-07-19'
name: Ecton
nav: Providers
network: true
overview: 'Ecton is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Patient Payments, Payments, and Fintech.


  Ecton''s developer surface includes engineering blog, signup flow, changelog, and 9 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 21.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ecton/refs/heads/main/screenshots/ecton-2026-07-25T212815.png
security:
- kind: domain-security
  name: Ecton Domain Security
  slug: ecton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ecton Vulnerability Disclosure
  slug: ecton-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: ecton
tags:
- Company
- Healthcare
- Patient Payments
- Payments
- Fintech
- Financial Wellness
- Health Savings
- Revenue Cycle Management
- Artificial Intelligence
website: https://www.ecton.io
---
