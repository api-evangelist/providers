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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/bonsai-health/hosts/bonsai-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonsai-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/bonsai-health/vendors/bonsai-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bonsai-health-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bonsai-health/security/bonsai-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonsai-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bonsaihealth.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.bonsaihealth.com/about
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bonsaihealth.com/demo
- group: start
  title: ''
  type: Demo
  url: https://www.bonsaihealth.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bonsaihealth.com/terms-of-use
- group: start
  title: ''
  type: SignUp
  url: https://www.bonsaihealth.com/demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bonsaihealth.com/privacy-policy
coverage:
  checked: '2026-10-25'
  detail: The provider's website returns HTML with no discoverable OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.bonsaihealth.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Bonsai Health is an AI‑powered platform that helps medical practices improve patient outcomes by automating outreach, scheduling, and follow‑up care. Founded after a personal loss to melanoma, the company aims to ensure no patient is overlooked and to reduce staff burnout. Now part of ModMed, Bonsai Health delivers agentic AI tools for automated patient engagement, appointment filling, and revenue growth across thousands of practices.
image: https://cdn.bonsaihealth.com/assets/bonsai-OG.png
layout: provider
modified: '2026-10-25'
name: Bonsai Health
nav: Providers
network: true
overview: 'Bonsai Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Patient Engagement, and Automation.


  Bonsai Health''s developer surface includes documentation, getting-started guide, signup flow, and 7 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bonsai-health/bonsai-health-2026-11-03T122216.png
security:
- kind: domain-security
  name: Bonsai Health Domain Security
  slug: bonsai-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bonsai-health
tags:
- Company
- Healthcare
- Artificial Intelligence
- Patient Engagement
- Automation
website: https://www.bonsaihealth.com
---
