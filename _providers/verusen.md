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
    dynamic_client_registration: true
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Verusen provides AI‑powered MRO inventory optimization platform; API documentation not publicly available.
  name: Verusen API
  slug: verusen-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/verusen/well-known/verusen-verusen-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/verusen-verusen-security.txt
- group: agent
  href: https://artifacts.apis.io/verusen/llms/verusen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/verusen-llms.txt
- group: agent
  href: https://artifacts.apis.io/verusen/well-known/verusen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/verusen-well-known.yml
- group: other
  href: https://artifacts.apis.io/verusen/hosts/verusen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/verusen-hosts.yml
- group: other
  href: https://artifacts.apis.io/verusen/vendors/verusen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/verusen-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://verusen.statuspage.io/
- group: auth
  title: ''
  type: Security
  url: https://verusen.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://verusen.com/news/
- group: docs
  title: ''
  type: Documentation
  url: https://help.verusen.com/
- group: auth
  href: https://artifacts.apis.io/verusen/security/verusen-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/verusen-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/verusen/security/verusen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/verusen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://verusen.com
- group: company
  title: ''
  type: Blog
  url: https://verusen.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://verusen.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://verusen.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://verusen.com/terms/
coverage:
  checked: '2026-10-24'
  detail: No OpenAPI or other machine‑readable contract found; attempts to fetch common spec URLs returned 404.
  evidence:
  - status: 404
    url: https://verusen.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Verusen provides an AI‑powered MRO inventory optimization platform that helps manufacturers overcome data challenges to make better maintenance, repair, and operations decisions. Their solution offers tools such as ROI calculators, whitepapers, and a blog to educate users on spare‑part criticality, SLOB management, and inventory best practices.
image: https://verusen.com/wp-content/uploads/2021/01/iso-logo-1.png
layout: provider
modified: '2026-10-23'
name: Verusen
nav: Providers
network: true
overview: 'Verusen is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, MRO, Inventory, and Optimization.


  Verusen''s developer surface includes documentation, engineering blog, support, and 13 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 65.2
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/verusen/verusen-2026-11-03T145741.png
security:
- kind: domain-security
  name: Verusen Domain Security
  slug: verusen-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Verusen Vulnerability Disclosure
  slug: verusen-vulnerability-disclosure
  summary_line: no policy recorded
slug: verusen
tags:
- Company
- Artificial Intelligence
- MRO
- Inventory
- Optimization
- Manufacturing
website: https://verusen.com
---
