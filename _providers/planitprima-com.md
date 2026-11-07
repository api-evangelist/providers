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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Datenschutz‑Software // PRIMA offers a privacy‑management platform; API details not publicly documented.
  name: PlanitPrima API
  slug: planitprima-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/planitprima-com/vendors/planitprima-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/planitprima-com-vendors.yml
- group: agent
  href: https://artifacts.apis.io/planitprima-com/llms/planitprima-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/planitprima-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/planitprima-com/well-known/planitprima-com-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/planitprima-com-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/planitprima-com/well-known/planitprima-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/planitprima-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/planitprima-com/hosts/planitprima-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/planitprima-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/planitprima-com/security/planitprima-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/planitprima-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://planitprima.com/
- group: company
  title: ''
  type: Blog
  url: https://www.planitprima.com/en/prima-blog/
- group: operate
  title: ''
  type: Support
  url: https://www.planitprima.com/en/contact/
- group: docs
  title: ''
  type: Documentation
  url: https://www.planitprima.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://www.planitprima.com/de/anmeldung-testphase/
coverage:
  checked: '2026-10-30'
  detail: The provider's website does not publish any machine‑readable API contract or specification.
  evidence:
  - status: 200
    url: https://api.planitprima.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Planit Prima offers a web‑based data protection management platform that helps organisations maintain GDPR‑compliant documentation. The software keeps data protection management lean, transparent and always up to date with legal requirements. It provides templates, AI‑assisted checks, training courses, and a centralized portal for creating, storing and tracking data protection records. Developed with support from IT lawyers, it enables companies to start simple and scale their compliance efforts without needing specialized knowledge.
image: https://www.planitprima.com/wp-content/uploads/2024/04/planit-logo-test.svg
layout: provider
modified: '2026-10-30'
name: planitprima-com
nav: Providers
network: true
overview: 'planitprima-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Protection, GDPR, Software-as-a-Service, Privacy, and Compliance.


  planitprima-com''s developer surface includes engineering blog, support, documentation, signup flow, and 7 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 64.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/planitprima-com/planitprima-com-2026-11-03T141255.png
security:
- kind: domain-security
  name: Planitprima Com Domain Security
  slug: planitprima-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: planitprima-com
tags:
- Data Protection
- GDPR
- Software-as-a-Service
- Privacy
- Compliance
- Software
website: https://planitprima.com/
---
