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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/legion-co/well-known/legion-co-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/legion-co-status-security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://trust.legion.co/
- group: agent
  href: https://artifacts.apis.io/legion-co/well-known/legion-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/legion-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/legion-co/hosts/legion-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/legion-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/legion-co/vendors/legion-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/legion-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legion.co/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.legion.co/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legion.co/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://legion.co/news/
- group: auth
  href: https://artifacts.apis.io/legion-co/security/legion-co-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/legion-co-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/legion-co/security/legion-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/legion-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://legion.co
- group: docs
  title: ''
  type: Documentation
  url: https://legion.co/resources/
- group: company
  title: ''
  type: Blog
  url: https://legion.co/blog/
- group: operate
  title: ''
  type: Support
  url: https://legion.co/support-services/
coverage:
  checked: '2026-10-26'
  detail: No public developer documentation or API specifications were found on legion.co.
  evidence:
  - status: 200
    url: https://legion.co
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Legion provides an intelligent workforce management platform that automates labor planning, schedule optimization, time‑and‑attendance, and employee engagement. The solution leverages AI to forecast demand, reduce attrition, and improve compliance for enterprises across retail, hospitality, healthcare, and other industries. Founded with backing from Norwest Venture Partners, Legion serves thousands of locations worldwide, delivering measurable cost savings and productivity gains.
image: https://legion.co/wp-content/uploads/2025/12/hero-home-scaled.png
layout: provider
modified: '2026-10-26'
name: Legion
nav: Providers
network: true
overview: 'Legion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workforce, Automation, Artificial Intelligence, and Software-as-a-Service.


  Legion''s developer surface includes documentation, engineering blog, support, and 12 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 49.1
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/legion-co/legion-co-2026-11-03T134800.png
security:
- kind: domain-security
  name: Legion Co Domain Security
  slug: legion-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Legion Co Trust Center
  slug: legion-co-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: legion-co
tags:
- Company
- Workforce
- Automation
- Artificial Intelligence
- Software-as-a-Service
website: https://legion.co
---
