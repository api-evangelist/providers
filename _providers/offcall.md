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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.offcall.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.offcall.com/sign-up
- group: operate
  title: ''
  type: Support
  url: mailto:contact@offcall.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.offcall.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.offcall.com/legal/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/offcall-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/offcall-llms.txt
created: '2026-07-17'
description: Offcall is a career and practice platform for physicians, backed by Bloomberg Beta. It provides confidential, anonymous physician salary and compensation benchmarking, and a verified clinician-to-clinician patient referrals network with HIPAA-compliant messaging for care coordination, delivered through web and mobile (iOS and Android) applications. Offcall does not currently publish a public developer API, developer portal, or OpenAPI specification; this profile was surfaced through the Bloomberg Beta portfolio and enriched with the identity and domain-security signals that are publicly available.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/offcall.png
layout: provider
modified: '2026-07-20'
name: Offcall
nav: Providers
network: true
overview: 'Offcall is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Physicians, Compensation, and Referrals.


  Offcall''s developer surface includes signup flow, support, and 5 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/offcall/refs/heads/main/screenshots/offcall-2026-08-07T190017.png
security:
- kind: domain-security
  name: Offcall Domain Security
  slug: offcall-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: offcall
tags:
- Company
- Healthcare
- Physicians
- Compensation
- Referrals
- Clinical
- HIPAA
website: https://www.offcall.com/
---
