---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/getabacus-com/hosts/getabacus-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getabacus-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getabacus-com/vendors/getabacus-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getabacus-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/getabacus-com/security/getabacus-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getabacus-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getabacus.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getabacus.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://www.getabacus.com/contact
coverage:
  checked: '2026-10-26'
  detail: No public API documentation or machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.getabacus.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Abacus is an AI‑powered accounting platform that automates tax preparation, audit tie‑outs, and advisory services for accounting firms. Backed by Menlo Ventures, it integrates document ingestion, AI agents, and secure SOC 2‑compliant hosting to streamline complex returns and improve firm productivity.
image: https://www.getabacus.com/opengraph-image?0f17cd1a40325ffa
layout: provider
modified: '2026-10-25'
name: Abacus
nav: Providers
network: true
overview: Abacus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Artificial Intelligence, Tax, and Automation.
random_paper: 11
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 6.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/getabacus-com/getabacus-com-2026-11-03T132648.png
security:
- kind: domain-security
  name: Getabacus Com Domain Security
  slug: getabacus-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: getabacus-com
tags:
- Company
- Accounting
- Artificial Intelligence
- Tax
- Automation
website: https://getabacus.com
---
