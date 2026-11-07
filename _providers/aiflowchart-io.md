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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/aiflowchart-io/llms/aiflowchart-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiflowchart-io-llms.txt
- group: other
  href: https://artifacts.apis.io/aiflowchart-io/hosts/aiflowchart-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiflowchart-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiflowchart-io/vendors/aiflowchart-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiflowchart-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiflowchart.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiflowchart.io/privacy
- group: auth
  href: https://artifacts.apis.io/aiflowchart-io/security/aiflowchart-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiflowchart-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiflowchart.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://aiflowchart.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://aiflowchart.io/blog
coverage:
  checked: '2026-11-01'
  detail: The provider offers AI diagram generation but provides no public API documentation or machine‑readable contract.
  evidence:
  - status: 200
    url: https://aiflowchart.io/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: AI Flowchart provides a free AI-powered diagram and flowchart generator. Users can input ideas, code snippets, sketches, or PDFs, and the platform automatically creates flowcharts, mind maps, ER diagrams, sequence diagrams, system designs, swimlanes, and org charts. It offers a range of templates, animated explainer creation, and integration with VS Code. Plans include a free tier with limited AI credits and a Pro subscription for unlimited AI usage across web and VS Code extensions.
image: https://aiflowchart.io/og-image.png
layout: provider
modified: '2026-11-01'
name: AI Flowchart
nav: Providers
network: true
overview: 'AI Flowchart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Diagram, Flowchart, Generator, and Free.


  AI Flowchart''s developer surface includes pricing, engineering blog, and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 11.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiflowchart Io Domain Security
  slug: aiflowchart-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aiflowchart-io
tags:
- Artificial Intelligence
- Diagram
- Flowchart
- Generator
- Free
website: https://aiflowchart.io/
---
