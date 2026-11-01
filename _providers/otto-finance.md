---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 16.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://ottofinance.io/security
- group: agent
  href: https://artifacts.apis.io/otto-finance/well-known/otto-finance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/otto-finance-well-known.yml
- group: other
  href: https://artifacts.apis.io/otto-finance/hosts/otto-finance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/otto-finance-hosts.yml
- group: other
  href: https://artifacts.apis.io/otto-finance/vendors/otto-finance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/otto-finance-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://ottofinance.io/security
- group: auth
  href: https://artifacts.apis.io/otto-finance/security/otto-finance-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/otto-finance-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/otto-finance/security/otto-finance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/otto-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ottofinance.io/
- group: docs
  title: ''
  type: Documentation
  url: https://ottofinance.io/platform
- group: docs
  title: ''
  type: APIReference
  url: https://ottofinance.io/platform
- group: start
  title: ''
  type: GettingStarted
  url: https://ottofinance.io/platform
- group: operate
  title: ''
  type: Support
  url: https://ottofinance.io/contact
- group: company
  title: ''
  type: Blog
  url: https://ottofinance.io/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ottofinance.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ottofinance.io/legal/privacy
coverage:
  checked: '2026-10-23'
  detail: No developer documentation or API specifications were found on ottofinance.io domains.
  evidence:
  - status: 200
    url: https://ottofinance.io/platform
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Otto Finance provides an AI‑driven automation and governance platform for regulated UK wealth management firms. It streamlines onboarding, annual reviews, compliance and client workflow automation, delivering a full audit trail and real‑time monitoring. The solution connects to existing systems, automates critical processes, and ensures security and data protection compliance, serving firms with billions in assets under management.
image: https://ottofinance.io/og-image.png
layout: provider
modified: '2026-10-23'
name: Otto Finance
nav: Providers
network: true
overview: 'Otto Finance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, Wealth Management, Automation, and AI.


  Otto Finance''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 10 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Otto Finance Domain Security
  slug: otto-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Otto Finance Trust Center
  slug: otto-finance-trust-center
  summary_line: ISO 27001, GDPR
slug: otto-finance
tags:
- Company
- FinTech
- Wealth Management
- Automation
- AI
website: https://www.ottofinance.io/
---
