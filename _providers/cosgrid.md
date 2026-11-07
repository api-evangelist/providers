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
api_count: 1
apis:
- description: COSGrid provides security and networking APIs for Zero Trust, SASE, and related services.
  name: COSGrid API
  slug: cosgrid-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/cosgrid/llms/cosgrid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cosgrid-llms.txt
- group: other
  href: https://artifacts.apis.io/cosgrid/hosts/cosgrid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cosgrid-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cosgrid.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cosgrid.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cosgrid.com/on-this-page/quick-start
- group: auth
  href: https://artifacts.apis.io/cosgrid/security/cosgrid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cosgrid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cosgrid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cosgrid.com/resources
- group: operate
  title: ''
  type: Support
  url: https://www.cosgrid.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.cosgrid.com/resources/blogs
coverage:
  checked: '2026-10-20'
  detail: API documentation page returns 404 and no OpenAPI/Swagger spec is available.
  evidence:
  - status: 200
    url: https://www.cosgrid.com/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: COSGrid Networks provides cyber resiliency solutions, offering secure access, zero trust networking, SD-WAN, and cloud security services. Their platform simplifies protection for enterprises by integrating secure web access, micro‑segmentation, and AI‑driven governance, helping organizations prevent data exposure and manage risk across distributed environments.
image: https://vcdn.cosgrid.com/website/assets/images/meta/COSGrid_Meta_Logo.png
layout: provider
modified: '2026-10-20'
name: COSGrid Networks
nav: Providers
network: true
overview: 'COSGrid Networks is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Zero Trust, SD-WAN, and Cloud Security.


  COSGrid Networks'' developer surface includes getting-started guide, documentation, support, engineering blog, and 6 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cosgrid/cosgrid-2026-11-03T125424.png
security:
- kind: domain-security
  name: Cosgrid Domain Security
  slug: cosgrid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cosgrid
tags:
- Company
- Cybersecurity
- Zero Trust
- SD-WAN
- Cloud Security
website: https://cosgrid.com/
---
