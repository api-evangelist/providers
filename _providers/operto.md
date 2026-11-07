---
access_model:
  confidence: low
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/operto/well-known/operto-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/operto-well-known.yml
- group: other
  href: https://artifacts.apis.io/operto/hosts/operto-hosts.yml
  title: ''
  type: Hosts
  url: hosts/operto-hosts.yml
- group: other
  href: https://artifacts.apis.io/operto/vendors/operto-vendors.yml
  title: ''
  type: Vendors
  url: vendors/operto-vendors.yml
- group: build
  href: https://artifacts.apis.io/operto/packages/operto-packages.yml
  title: ''
  type: SDKs
  url: packages/operto-packages.yml
- group: build
  href: https://artifacts.apis.io/operto/packages/operto-packages.yml
  title: ''
  type: Packages
  url: packages/operto-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://operto.com/media/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/operto
- group: auth
  href: https://artifacts.apis.io/operto/security/operto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/operto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://operto.com/
- group: company
  title: ''
  type: Blog
  url: https://operto.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://operto.com/demo-operto/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://operto.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://operto.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://operto.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://auth.operto.com
coverage:
  checked: '2026-10-28'
  detail: Operto's API contracts are behind authentication; the MCP endpoint https://auth.operto.com/mcp returns 403, indicating a partner login is required.
  evidence:
  - status: 403
    url: https://auth.operto.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Operto provides industry-leading hospitality management software that streamlines operations, enhances guest experiences, and drives growth for hotels, vacation rentals, student housing, and multi‑family properties. Its platform includes modules for guest access, mobile keys, contactless check‑in, housekeeping, scheduling, inventory, preventative maintenance, payroll, and digital guidebooks, helping property owners automate tasks and increase revenue.
image: https://operto.com/wp-content/uploads/2022/11/Connectdashmockup6-04-2.png
layout: provider
modified: '2026-10-28'
name: Operto
nav: Providers
network: true
overview: 'Operto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Property Management, Guest Experience, and Automation.


  Operto''s developer surface includes engineering blog, pricing, support, signup flow, and 11 more developer resources.'
plans:
- name: Operto Plans Pricing
  plan_count: 0
  slug: operto-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Operto Rate Limits
  slug: operto-rate-limits
scopes:
- name: Operto Scopes
  scope_count: 0
  slug: operto-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 49.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.6
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/operto/operto-2026-11-03T140704.png
security:
- kind: authentication
  name: Operto Authentication
  slug: operto-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Operto Domain Security
  slug: operto-domain-security
  summary_line: TLSv1.3 · DMARC
slug: operto
tags:
- Company
- Hospitality
- Property Management
- Guest Experience
- Automation
website: https://operto.com/
---
