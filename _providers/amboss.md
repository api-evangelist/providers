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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.amboss.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.amboss.com/us/pricing
- group: start
  title: ''
  type: SignUp
  url: https://next.amboss.com/us/registration
- group: start
  title: ''
  type: Login
  url: https://next.amboss.com/us/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amboss.com/us/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amboss.com/us/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.amboss.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amboss-mededu
- group: auth
  title: ''
  type: Security
  url: https://www.amboss.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amboss-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amboss-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amboss-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amboss-domain-security.yml
created: '2026-07-17'
description: AMBOSS is a Berlin-based (AMBOSS SE) digital medical knowledge platform used by medical students, physicians, educators, and healthcare institutions worldwide. It combines a physician-authored medical library, exam-style Qbanks with AI-powered analytics, and a point-of-care clinical reference tool, plus AI features (LiSA) for evidence-based clinical decision support. AMBOSS sells consumer memberships and institutional licenses to medical schools, residency programs, and hospitals. It is a Partech portfolio company. This profile was enriched from AMBOSS' public web and security surface; the medical platform publishes no public developer API (its amboss-mededu GitHub org hosts internal tooling), so this repo carries identity and security artifacts rather than API specifications.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amboss.png
layout: provider
modified: '2026-07-17'
name: AMBOSS
nav: Providers
network: true
overview: 'AMBOSS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Education, Medical Knowledge, and Clinical Reference.


  AMBOSS''s developer surface includes pricing, signup flow, support, and 10 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 19.0
  delta: -3.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 22.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amboss/refs/heads/main/screenshots/amboss-2026-07-25T200032.png
security:
- kind: domain-security
  name: Amboss Domain Security
  slug: amboss-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amboss Vulnerability Disclosure
  slug: amboss-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amboss
tags:
- Company
- Healthcare
- Medical Education
- Medical Knowledge
- Clinical Reference
- Physicians
- EdTech
website: https://www.amboss.com/
---
