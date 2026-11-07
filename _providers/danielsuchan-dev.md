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
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/danielsuchan-dev/changelog/danielsuchan-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/danielsuchan-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/danielsuchan-dev/security/danielsuchan-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/danielsuchan-dev-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/danielsuchan-dev/llms/danielsuchan-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/danielsuchan-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/danielsuchan-dev/well-known/danielsuchan-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/danielsuchan-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/danielsuchan-dev/well-known/danielsuchan-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/danielsuchan-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/danielsuchan-dev/hosts/danielsuchan-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/danielsuchan-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/danielsuchan-dev/vendors/danielsuchan-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/danielsuchan-dev-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://danielsuchan.dev/changelog
- group: auth
  href: https://artifacts.apis.io/danielsuchan-dev/security/danielsuchan-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/danielsuchan-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/danielsuchan-dev/security/danielsuchan-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/danielsuchan-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://danielsuchan.dev/
coverage:
  checked: '2026-11-04'
  detail: The provider's site returns HTML shells for expected spec URLs (e.g., /openapi.json) with no machine‑readable contract.
  evidence:
  - status: 200
    url: https://danielsuchan.dev/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Software engineer based in Brno, Czech Republic. Building Dzarvis, a multi‑agent AI assistant on Claude, and shipping production AI infrastructure. Co‑founder of Blaze (CTO 2023–2026) with 8+ years of coding experience, founder of JarvisCheck and Syncoli, and creator of various AI‑driven tools and services.
layout: provider
modified: '2026-11-04'
name: Daniel Suchan
nav: Providers
network: true
overview: 'Daniel Suchan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Engineering, Open Source, and Czech.


  Daniel Suchan''s developer surface includes changelog and 10 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Danielsuchan Dev Domain Security
  slug: danielsuchan-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Danielsuchan Dev Vulnerability Disclosure
  slug: danielsuchan-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: danielsuchan-dev
tags:
- Company
- Artificial Intelligence
- Engineering
- Open Source
- Czech
website: https://danielsuchan.dev/
---
