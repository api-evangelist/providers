---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation is referenced at https://docs.processbolt.com/ but no machine‑readable contract was found.
  name: ProcessBolt API
  slug: processbolt-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/processbolt-com/well-known/processbolt-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/processbolt-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/processbolt-com/hosts/processbolt-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/processbolt-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/processbolt-com/vendors/processbolt-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/processbolt-com-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://perimeter.net/about/leadership/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.processbolt.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ProcessBolt
- group: auth
  href: https://artifacts.apis.io/processbolt-com/security/processbolt-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/processbolt-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://perimeter.net/
- group: company
  title: ''
  type: Blog
  url: https://perimeter.net/insights/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://perimeter.net/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://perimeter.net/terms-and-conditions/
coverage:
  checked: '2026-10-29'
  detail: Documentation at https://docs.processbolt.com/ provides no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.processbolt.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: ProcessBolt, now operating as Perimeter, provides a painless Vendor Risk Management (VRM) platform for regulated industries. The solution offers continuous monitoring, automated assessments, AI‑powered document extraction, and real‑time risk scoring to help organizations reduce manual effort, improve vendor oversight, and meet compliance requirements. Backed by Techstars, Perimeter serves healthcare, finance, and enterprise customers with a cloud‑native, scalable service.
image: https://perimeter.net/wp-content/uploads/2025/09/ProcessBolt-Perimeter.jpg
layout: provider
modified: '2026-10-29'
name: ProcessBolt
nav: Providers
network: true
overview: 'ProcessBolt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, VRM, Third-Party Risk Management, Software-as-a-Service, and Healthcare.


  ProcessBolt''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Processbolt Com Plans Pricing
  plan_count: 0
  slug: processbolt-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Processbolt Com Rate Limits
  slug: processbolt-com-rate-limits
scopes:
- name: Processbolt Com Scopes
  scope_count: 0
  slug: processbolt-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 58.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.7
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/processbolt-com/processbolt-com-2026-11-03T141519.png
security:
- kind: authentication
  name: Processbolt Com Authentication
  slug: processbolt-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Processbolt Com Domain Security
  slug: processbolt-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: processbolt-com
tags:
- Company
- VRM
- Third-Party Risk Management
- Software-as-a-Service
- Healthcare
- Finance
website: https://perimeter.net/
---
