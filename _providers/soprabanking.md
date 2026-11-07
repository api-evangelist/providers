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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation for SBS banking and financing software solutions.
  name: SBS API
  slug: sbs-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/soprabanking/llms/soprabanking-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/soprabanking-llms.txt
- group: agent
  href: https://artifacts.apis.io/soprabanking/well-known/soprabanking-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/soprabanking-well-known.yml
- group: other
  href: https://artifacts.apis.io/soprabanking/hosts/soprabanking-hosts.yml
  title: ''
  type: Hosts
  url: hosts/soprabanking-hosts.yml
- group: other
  href: https://artifacts.apis.io/soprabanking/vendors/soprabanking-vendors.yml
  title: ''
  type: Vendors
  url: vendors/soprabanking-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sbs-software.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://sbs-software.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sbs-software.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://sbs-software.com/news
- group: auth
  href: https://artifacts.apis.io/soprabanking/security/soprabanking-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/soprabanking-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sbs-software.com/
coverage:
  checked: '2026-10-21'
  detail: No machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract was found on the provider’s website.
  evidence:
  - status: 200
    url: https://sbs-software.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: SBS provides banking and financing software solutions, offering a suite of products for financial institutions to manage accounts, payments, and lending. The company focuses on modern, scalable platforms that integrate with existing banking infrastructure, delivering secure, compliant, and customizable services for banks and fintechs.
image: https://sbs-software.com/wp-content/uploads/2025/10/Thumbnail-SBS.png
layout: provider
modified: '2026-10-21'
name: SBS
nav: Providers
network: true
overview: 'SBS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Software, and Fintech.


  SBS''s developer surface includes support and 9 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 56.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/soprabanking/soprabanking-2026-11-03T143538.png
security:
- kind: domain-security
  name: Soprabanking Domain Security
  slug: soprabanking-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soprabanking
tags:
- Company
- Banking
- Software
- Fintech
website: https://sbs-software.com/
---
