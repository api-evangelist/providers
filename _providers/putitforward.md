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
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.putitforward.com/
- group: auth
  href: https://artifacts.apis.io/putitforward/security/putitforward-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/putitforward-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/putitforward/hosts/putitforward-hosts.yml
  title: ''
  type: Hosts
  url: hosts/putitforward-hosts.yml
- group: auth
  href: https://artifacts.apis.io/putitforward/security/putitforward-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/putitforward-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/putitforward/security/putitforward-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/putitforward-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/putitforward/security/putitforward-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/putitforward-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://putitforward.com/
- group: company
  title: ''
  type: Blog
  url: https://www.putitforward.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.putitforward.com/platform/about
- group: commercial
  title: ''
  type: Pricing
  url: https://www.putitforward.com/platform/about/pricing
coverage:
  checked: '2026-10-21'
  detail: The documentation site renders pages via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.putitforward.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Put it Forward provides governed decision execution and enterprise automation solutions. Their platform enables organizations to integrate data, automate processes, and apply predictive analytics across functions such as marketing, sales, finance, and IT. By offering a suite of components—including data integration, process automation, process mining, and AI‑driven analytics—Put it Forward helps enterprises streamline operations, improve decision‑making, and accelerate digital transformation. The company focuses on compliance, AI governance, and delivering measurable business outcomes through a unified automation ecosystem.
image: https://www.putitforward.com/images/home-images/Put-It-Forward-Intelligent-Automation-Platform-Main-Image.webp
layout: provider
modified: '2026-10-21'
name: Put it Forward
nav: Providers
network: true
overview: 'Put it Forward is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, Artificial Intelligence, Enterprise, and Integration.


  Put it Forward''s developer surface includes engineering blog, documentation, pricing, and 7 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/putitforward/putitforward-2026-11-03T141732.png
security:
- kind: domain-security
  name: Putitforward Domain Security
  slug: putitforward-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Putitforward Vulnerability Disclosure
  slug: putitforward-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Putitforward Trust Center
  slug: putitforward-trust-center
  summary_line: SOC 2, ISO 27001
slug: putitforward
tags:
- Company
- Automation
- Artificial Intelligence
- Enterprise
- Integration
website: https://putitforward.com/
---
