---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/oxipital-ai/llms/oxipital-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oxipital-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/oxipital-ai/well-known/oxipital-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/oxipital-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/oxipital-ai/hosts/oxipital-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oxipital-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/oxipital-ai/vendors/oxipital-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oxipital-ai-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.oxipitalai.com/sandbox/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oxipitalai.com/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://www.oxipitalai.com/leadership/
- group: auth
  href: https://artifacts.apis.io/oxipital-ai/security/oxipital-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oxipital-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oxipitalai.com/
coverage:
  checked: '2026-10-23'
  detail: No public developer documentation or API specifications were found on the provider's website.
  evidence:
  - status: 200
    url: https://www.oxipitalai.com/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Oxipital AI provides AI-powered computer vision solutions that enable developers to integrate advanced image and video analysis into their applications. Their platform offers APIs for object detection, scene understanding, and visual search, targeting industries such as retail, security, and autonomous systems. Founded in 2022, Oxipital AI leverages deep learning models to deliver scalable, real-time visual insights, with a focus on privacy and on-device processing where possible. The company is backed by Scale Venture Partners and aims to democratize access to cutting‑edge visual AI technology for developers worldwide.
layout: provider
modified: '2026-10-23'
name: Oxipital AI
nav: Providers
network: true
overview: 'Oxipital AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Computer Vision, APIs, and Developer Tools.


  Oxipital AI''s developer surface includes sandbox and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Oxipital Ai Domain Security
  slug: oxipital-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: oxipital-ai
tags:
- Company
- AI
- Computer Vision
- APIs
- Developer Tools
website: https://www.oxipitalai.com/
---
