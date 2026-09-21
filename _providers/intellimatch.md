---
access_model:
  confidence: medium
  label: Enterprise contact-sales only; no published pricing and no self-service signup
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.fisglobal.com/products/fis-data-integrity-manager
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.fisglobal.com/products/fis-data-integrity-manager
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/intellimatch/refs/heads/main/security/intellimatch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intellimatch-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/intellimatch/refs/heads/main/well-known/intellimatch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/intellimatch-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/intellimatch/refs/heads/main/well-known/intellimatch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/intellimatch-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/intellimatch/refs/heads/main/security/intellimatch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/intellimatch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fisglobal.com/en/responsible-disclosure
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intellimatch/refs/heads/main/conformance/intellimatch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/intellimatch-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/intellimatch/refs/heads/main/lifecycle/intellimatch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/intellimatch-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/intellimatch/refs/heads/main/plans/intellimatch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/intellimatch-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/intellimatch/refs/heads/main/rate-limits/intellimatch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/intellimatch-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/intellimatch/refs/heads/main/packages/intellimatch-packages.yml
  title: ''
  type: Packages
  url: packages/intellimatch-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/intellimatch/refs/heads/main/llms/intellimatch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/intellimatch-llms.txt
coverage:
  checked: '2026-09-13'
  detail: 'FIS ships IntelliMatch — renamed FIS Data Integrity Manager — as an end-user enterprise reconciliation application with no developer program of its own: the live product page offers brochures and "Connect with sales" and links to no reference, spec or portal, while the URL this record previously carried as its Website is now a hard 404 after the rename.'
  evidence:
  - status: 200
    url: https://www.fisglobal.com/products/fis-data-integrity-manager
  - status: 404
    url: https://www.fisglobal.com/en/products/intellimatch-reconciliation-software
  - status: 403
    url: https://codeconnect.fisglobal.com/fisccp/apisbytag
  - status: 200
    url: https://fisglobal.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2024-01-01'
description: IntelliMatch is a transaction and account reconciliation platform originally developed by SunGard, now offered by FIS, and since renamed FIS Data Integrity Manager. It performs account-level balance and transaction proofing at high volume and drives review, approval, exception management and escalation through an integrated workflow engine, so financial institutions and corporates can reconcile cash, securities and intercompany activity and track data integrity centrally. The product is SWIFT-accredited, embeds machine learning through an AI Virtual Reconciler, and is sold either customer-hosted or as the FIS Optimized Reconciliation Service (formerly Managed Reconciliation Service). FIS publishes no developer program, documentation, OpenAPI or any other machine-readable contract for it; integration is arranged commercially. FIS's public API marketplace, Code Connect, carries a different product line and is profiled separately.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intellimatch.png
layout: provider
modified: '2026-09-13'
name: IntelliMatch
nav: Providers
network: true
overview: IntelliMatch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Reconciliation, Financial-Services, Matching, Exception Management, and Banking.
plans:
- name: Intellimatch Plans Pricing
  plan_count: 0
  slug: intellimatch-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Intellimatch Rate Limits
  slug: intellimatch-rate-limits
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 10.5
  previous_composite: 7.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Intellimatch Domain Security
  slug: intellimatch-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Intellimatch Vulnerability Disclosure
  slug: intellimatch-vulnerability-disclosure
  summary_line: Bugcrowd
slug: intellimatch
tags:
- Reconciliation
- Financial-Services
- Matching
- Exception Management
- Banking
- Treasury
- Swift
- Data Integrity
website: https://www.fisglobal.com/products/fis-data-integrity-manager
---
