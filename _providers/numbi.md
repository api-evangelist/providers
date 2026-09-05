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
  url: security/numbi-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/numbi-llms.txt
- group: company
  title: ''
  type: Website
  url: https://numbi.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://numbi.ai/terminos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://numbi.ai/privacidad
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/numbiai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/numbi_ai
created: '2026-07-17'
description: 'Numbi is a tech-enabled accounting and payroll firm for Colombian companies — especially SAS entities, SMBs, and startups. It pairs expert accountants with automation and AI to run monthly bookkeeping, taxes, payroll, and DIAN electronic-invoicing compliance. Numbi is a service rather than software or an ERP: it operates on top of a company''s existing accounting systems (Siigo and Alegra) instead of replacing them, ingesting documents (PDFs, XMLs, images) and keeping tax calendars and filings current. Founded in Bogotá and backed by Homebrew and Newtopia VC. No public developer API surface is published as of this pass.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/numbi.png
layout: provider
modified: '2026-07-20'
name: Numbi
nav: Providers
network: true
overview: Numbi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Accounting, Payroll, and Tax Compliance.
random_paper: 14
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/numbi/refs/heads/main/screenshots/numbi-2026-08-07T185727.png
security:
- kind: domain-security
  name: Numbi Domain Security
  slug: numbi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: numbi
tags:
- Company
- Fintech
- Accounting
- Payroll
- Tax Compliance
- Bookkeeping
- Colombia
website: https://numbi.ai
---
