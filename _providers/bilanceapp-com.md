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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.bilanceapp.com/security
- group: design
  href: https://artifacts.apis.io/bilanceapp-com/conformance/bilanceapp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bilanceapp-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/bilanceapp-com/hosts/bilanceapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bilanceapp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bilanceapp-com/vendors/bilanceapp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bilanceapp-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.bilanceapp.com/help
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bilanceapp.com/help/getting-started
- group: auth
  href: https://artifacts.apis.io/bilanceapp-com/security/bilanceapp-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bilanceapp-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bilanceapp-com/security/bilanceapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bilanceapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bilanceapp.com/
- group: company
  title: ''
  type: About
  url: https://www.bilanceapp.com/about
- group: auth
  title: ''
  type: Security
  url: https://www.bilanceapp.com/security
- group: company
  title: ''
  type: Blog
  url: https://www.bilanceapp.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bilanceapp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bilanceapp.com/privacy
coverage:
  checked: '2026-11-02'
  detail: The Bilance website provides help pages but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://www.bilanceapp.com/help/getting-started
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bilance is a budgeting app that connects to over 2,300 European banks, automatically syncing transactions and organizing them into budgets. Available on iOS and Android, it helps users track spending, set financial goals, and gain insights into their money habits across multiple currencies and banks.
image: https://www.bilanceapp.com/og-image.png
layout: provider
modified: '2026-11-02'
name: Bilance
nav: Providers
network: true
overview: 'Bilance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Budgeting, Banking, Personal Finance, and Mobile App.


  Bilance''s developer surface includes support, getting-started guide, engineering blog, and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 13.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bilanceapp Com Domain Security
  slug: bilanceapp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bilanceapp Com Trust Center
  slug: bilanceapp-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: bilanceapp-com
tags:
- Finance
- Budgeting
- Banking
- Personal Finance
- Mobile App
website: https://www.bilanceapp.com/
---
