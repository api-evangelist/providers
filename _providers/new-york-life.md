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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/new-york-life-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/newyorklife
- group: company
  title: ''
  type: Website
  url: https://www.newyorklife.com/
- group: other
  title: ''
  type: Investments
  url: https://www.nylim.com/
created: '2026-05-05'
description: New York Life Insurance Company is the largest mutual life insurance company in the United States, headquartered in Manhattan, New York. The company provides life insurance, fixed and variable annuities, long-term care, and investment management (through subsidiaries such as New York Life Investments / NYLIM). New York Life has maintained the highest financial-strength ratings from major rating agencies for more than a century. No public developer portal or external APIs have been identified; agent, partner, and reinsurer integrations occur through private B2B channels.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/new-york-life.png
layout: provider
modified: '2026-05-16'
name: New York Life
nav: Providers
network: true
overview: New York Life is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Financial-Services, Life Insurance, Wealth Management, and Fortune 100.
random_paper: 8
score:
  band: minimal
  composite: 2.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/new-york-life/refs/heads/main/screenshots/new-york-life-2026-06-20T190227.png
security:
- kind: domain-security
  name: New York Life Domain Security
  slug: new-york-life-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: new-york-life
tags:
- Insurance
- Financial-Services
- Life Insurance
- Wealth Management
- Fortune 100
website: https://www.newyorklife.com/
---
