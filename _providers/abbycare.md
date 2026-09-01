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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abbycare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.abbycare.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abbycare.org/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abbycare.org/privacy
created: '2026-07-17'
description: Abby Care (Wellspring Care Inc.) is a family caregiving platform that helps families deliver professional care at home and get paid for it. It provides no-cost caregiver certification and CNA training, employment, payroll and Medicaid enrollment support, and an AI-assisted care-management platform (AbbyOS / AbbyAid) for real-time care documentation and insights. Backed by Khosla Ventures. The company operates a public marketing website but publishes no public developer API, developer portal, or API documentation; this profile captures the identity and domain-security posture that could be verified from public sources.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abbycare.png
layout: provider
modified: '2026-07-17T12:00:00Z'
name: Abbycare
nav: Providers
network: true
overview: Abbycare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Caregiving, Home Care, and Medicaid.
random_paper: 6
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abbycare/refs/heads/main/screenshots/abbycare-2026-07-25T181404.png
security:
- kind: domain-security
  name: Abbycare Domain Security
  slug: abbycare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: abbycare
tags:
- Company
- Healthcare
- Caregiving
- Home Care
- Medicaid
- Health Tech
- Artificial Intelligence
website: https://www.abbycare.org/
---
