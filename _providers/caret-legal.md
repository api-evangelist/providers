---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/caret-legal/plans/caret-legal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/caret-legal-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/caret-legal/llms/caret-legal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caret-legal-llms.txt
- group: agent
  href: https://artifacts.apis.io/caret-legal/well-known/caret-legal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caret-legal-well-known.yml
- group: other
  href: https://artifacts.apis.io/caret-legal/hosts/caret-legal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caret-legal-hosts.yml
- group: other
  href: https://artifacts.apis.io/caret-legal/vendors/caret-legal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caret-legal-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://caretlegal.com/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://caretlegal.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caretlegal.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/caret-legal/security/caret-legal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caret-legal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caretlegal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.caretlegal.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://caretlegal.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://caretlegal.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://support.caretlegal.com/hc/en-us
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation site provides only HTML pages without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://caretlegal.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: CARET Legal provides cloud‑based legal practice management software designed to streamline case handling, automate workflows, and integrate billing, document management, and client communication. The platform serves law firms of all sizes, offering features such as case management, reporting and analytics, secure document storage, and mobile access, all hosted securely in the cloud.
image: https://caretlegal.com/wp-content/uploads/2023/06/CARET_Link_Share_Image_Option3.png
layout: provider
modified: '2026-10-28'
name: CARET Legal
nav: Providers
network: true
overview: 'CARET Legal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal Tech, Software-as-a-Service, Cloud, and Practice Management.


  CARET Legal''s developer surface includes engineering blog, pricing, support, and 11 more developer resources.'
plans:
- name: Caret Legal Plans Pricing
  plan_count: 3
  slug: caret-legal-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 55.4
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/caret-legal/caret-legal-2026-11-03T123334.png
security:
- kind: domain-security
  name: Caret Legal Domain Security
  slug: caret-legal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caret-legal
tags:
- Company
- Legal Tech
- Software-as-a-Service
- Cloud
- Practice Management
website: https://caretlegal.com/
---
