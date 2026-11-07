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
- group: agent
  href: https://artifacts.apis.io/thankview/llms/thankview-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thankview-llms.txt
- group: other
  href: https://artifacts.apis.io/thankview/hosts/thankview-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thankview-hosts.yml
- group: other
  href: https://artifacts.apis.io/thankview/vendors/thankview-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thankview-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.evertrue.com/sign-in/
- group: auth
  href: https://artifacts.apis.io/thankview/security/thankview-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thankview-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thankview.com/
- group: company
  title: ''
  type: Blog
  url: https://www.evertrue.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evertrue.com/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://www.evertrue.com/thankview/
- group: operate
  title: ''
  type: Support
  url: https://www.evertrue.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evertrue.com/terms-of-service/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/evertrue/workspace/thankview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evertrue
coverage:
  checked: '2026-10-27'
  detail: Provider docs are rendered as HTML with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.evertrue.com/thankview/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: ThankView, now part of EverTrue, provides video fundraising software for nonprofits, enabling organizations to engage donors through personalized video messages and track supporter relationships at scale. The platform integrates with donor management systems and offers APIs for video creation, distribution, and analytics, helping nonprofits increase fundraising effectiveness and donor retention.
image: https://www.evertrue.com/wp-content/uploads/2026/10/Logo_ThankView_Wordmark-Icon.svg
layout: provider
modified: '2026-10-27'
name: ThankView
nav: Providers
network: true
overview: 'ThankView is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Video, Fundraising, Non-Profit, and Marketing.


  ThankView''s developer surface includes engineering blog, documentation, support, and 10 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 46.4
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/thankview/thankview-2026-11-03T144529.png
security:
- kind: domain-security
  name: Thankview Domain Security
  slug: thankview-domain-security
  summary_line: TLSv1.2 · DMARC
slug: thankview
tags:
- Video
- Fundraising
- Non-Profit
- Marketing
website: https://thankview.com/
---
