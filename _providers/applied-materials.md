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
  href: https://artifacts.apis.io/applied-materials/llms/applied-materials-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/applied-materials-llms.txt
- group: company
  title: ''
  type: Website
  url: https://appliedsmartfactory.com
- group: company
  title: ''
  type: Blog
  url: https://appliedsmartfactory.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://appliedsmartfactory.com/support/
- group: auth
  href: https://artifacts.apis.io/applied-materials/security/applied-materials-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applied-materials-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/applied-materials
- group: company
  title: ''
  type: Website
  url: https://www.appliedmaterials.com
coverage:
  checked: '2026-09-04'
  detail: Applied Materials runs no developer program at all - api., developer., developers., docs., portal., customer., sso. and login..appliedmaterials.com every one returns NXDOMAIN, and the two OpenAPI files already in this repo describe an api.applied-materials.com host that is not an Applied Materials domain (the company's registrable domain is appliedmaterials.com, CAA iodef mailto:dnsadmin@amat.com), so they are API Evangelist scaffolds and are now stamped x-provenance as such.
  evidence:
  - status: 403
    url: https://www.appliedmaterials.com/
  - status: 403
    url: https://www.appliedmaterials.com/robots.txt
  - status: 200
    url: https://appliedsmartfactory.com/llms.txt
  - status: 404
    url: https://appliedsmartfactory.com/.well-known/api-catalog
  - status: 404
    url: https://appliedsmartfactory.com/.well-known/agent-card.json
  - status: 0
    url: https://api.applied-materials.com/
  reason: no-developer-program
  state: none
created: '2026-05-04'
description: 'Applied Materials, Inc. (NASDAQ: AMAT) is the global leader in materials engineering solutions used to produce virtually every new chip and advanced display in the world, supplying deposition, etch, chemical mechanical planarization, ion implantation, metrology and inspection equipment to semiconductor, display and adjacent markets. Its Applied SmartFactory business unit (appliedsmartfactory.com) ships the software side of that portfolio - PROMIS and 300works MES, SPC and process-quality, scheduling, dispatching and material-control products for fabs. Applied Materials publishes no public developer portal, API reference or machine-readable API contract; software is delivered under enterprise licence and support runs through customer portals.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/applied-materials.png
layout: provider
modified: '2026-09-04'
name: Applied Materials
nav: Providers
network: true
overview: 'Applied Materials is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Semiconductors, Manufacturing, Equipment, Fab Operations, and Materials Engineering.


  Applied Materials'' developer surface includes engineering blog, support, and 5 more developer resources.'
press:
- date: ''
  title: Applied Materials
  url: https://www.facebook.com/AppliedMaterialsInc/posts/today-applied-materials-announced-a-new-innovation-partnership-with-tsmc-to-acce/1407076051453212/
- date: ''
  title: Applied Materials and Micron Partner To Advance U.S. ...
  url: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-and-micron-partner-advance-us-innovation-next
- date: ''
  title: Applied Materials
  url: https://www.appliedmaterials.com/us/en.html
- date: ''
  title: Applied Materials and SK hynix Announce Long-Term R&D ...
  url: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-and-sk-hynix-announce-long-term-rd-partnership
- date: ''
  title: Applied Materials Debuts New Gear For Making AI Chips
  url: https://www.investors.com/news/technology/amat-stock-applied-materials-new-gear-ai-chips/
random_paper: 14
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 5.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/applied-materials/applied-materials-2026-10-11T100010.png
security:
- kind: domain-security
  name: Applied Materials Domain Security
  slug: applied-materials-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: applied-materials
tags:
- Semiconductors
- Manufacturing
- Equipment
- Fab Operations
- Materials Engineering
- Fortune 500
website: https://appliedsmartfactory.com
---
