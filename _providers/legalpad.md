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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.deel.com/immigration/
- group: other
  title: ''
  type: Archive
  url: https://web.archive.org/web/20241123115209/https://legalpad.io/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/legalpad-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/legalpad-llms.txt
created: '2026-07-17'
description: Legalpad (Legalpad Inc, Seattle) was a startup-focused US work-visa and immigration company founded by Todd Heine and Sara Itucas, who first began processing visas together at Teleborder (Y Combinator 2013) and reunited in Techstars Seattle in 2017. Legalpad paired software with staff immigration attorneys to file O-1, H-1B, L-1, TN, E-1/E-2, E-3 and B-1 work visas plus EB-1A, EB-1B, EB-1C, EB-2 and EB-2 NIW employment-based green cards, and said it had helped 500+ companies at roughly one-third the typical processing time. It raised a $2M seed in 2018 and a $10M Series A in 2020 before being acquired by Deel in 2022, after which it operated as "Legalpad by Deel" inside Deel Immigration. The legalpad.io web presence was retired after 2024 and the business now lives on as Deel Immigration. Legalpad never published a public API, developer portal, documentation, SDK or other developer surface, so there is no API artifact to enrich.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/legalpad.png
layout: provider
modified: '2026-07-19'
name: LegalPad
nav: Providers
network: true
overview: LegalPad is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal, Immigration, Work Visas, and Legal Services.
random_paper: 81
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/legalpad/refs/heads/main/screenshots/legalpad-2026-07-25T224830.png
security:
- kind: domain-security
  name: Legalpad Domain Security
  slug: legalpad-domain-security
  summary_line: no transport/DNS hardening detected
slug: legalpad
tags:
- Company
- Legal
- Immigration
- Work Visas
- Legal Services
- Human Resources
- Employment
- Global Mobility
- Professional Services
website: https://www.deel.com/immigration/
---
