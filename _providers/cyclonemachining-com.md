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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for machining titanium parts, describing material changes and shop setup.
  name: Machining Titanium API
  slug: machining-titanium-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/cyclonemachining-com/security/cyclonemachining-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cyclonemachining-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/cyclonemachining-com/llms/cyclonemachining-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cyclonemachining-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/cyclonemachining-com/well-known/cyclonemachining-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cyclonemachining-com-security.txt
- group: agent
  href: https://artifacts.apis.io/cyclonemachining-com/well-known/cyclonemachining-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cyclonemachining-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cyclonemachining-com/hosts/cyclonemachining-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cyclonemachining-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cyclonemachining-com/vendors/cyclonemachining-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cyclonemachining-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cyclonemachining.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cyclonemachining.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://cyclonemachining.com/reference/machining-titanium
- group: auth
  href: https://artifacts.apis.io/cyclonemachining-com/security/cyclonemachining-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cyclonemachining-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cyclonemachining-com/security/cyclonemachining-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cyclonemachining-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cyclonemachining.com/
coverage:
  checked: '2026-11-05'
  detail: Provider documentation is public HTML with no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract.
  evidence:
  - status: 200
    url: https://cyclonemachining.com/reference/machining-titanium
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Cyclone Machining Co. is a prototype and R&D machine shop located in Grand Rapids, Michigan. They offer five-axis CNC machining, precision finishing, TIG fabrication, and a range of manufacturing services for low‑quantity and custom parts, serving industries such as aerospace, automotive, and medical device development. The company emphasizes rapid prototyping, high‑quality engineering, and in‑house capabilities to turn designs into functional components.
image: https://cyclonemachining.com/opengraph-image?040b615184fcdb4c
layout: provider
modified: '2026-11-04'
name: Cyclone Machining Co.
nav: Providers
network: true
overview: 'Cyclone Machining Co. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, CNC, Prototyping, MachineShop, and Michigan.


  Cyclone Machining Co.''s developer surface includes API reference and 11 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cyclonemachining Com Domain Security
  slug: cyclonemachining-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cyclonemachining Com Vulnerability Disclosure
  slug: cyclonemachining-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cyclonemachining-com
tags:
- Manufacturing
- CNC
- Prototyping
- MachineShop
- Michigan
website: https://cyclonemachining.com/
---
