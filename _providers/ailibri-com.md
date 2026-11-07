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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/ailibri-com/llms/ailibri-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ailibri-com-llms.txt
- group: other
  href: https://artifacts.apis.io/ailibri-com/hosts/ailibri-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ailibri-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ailibri.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://ailibri.com/news/
- group: company
  title: ''
  type: Blog
  url: https://ailibri.com/blog/
- group: auth
  href: https://artifacts.apis.io/ailibri-com/security/ailibri-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ailibri-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ailibri.com/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found at the API host.
  evidence:
  - status: 0
    url: https://api.ailibri.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Ailibri operates a Russian-language catalog of AI tools and services, offering free and paid neural network applications for text, images, video, code, and more. The site lists over 3,000 AI models across 70 categories, providing descriptions, pricing, and usage instructions in Russian. It serves developers, creators, and businesses seeking AI solutions, with sections for productivity, content generation, translation, and specialized tools like deepfake generators and code assistants.
image: https://ailibri.com/apple-touch-icon.png
layout: provider
modified: '2026-11-01'
name: Ailibri
nav: Providers
network: true
overview: 'Ailibri is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Catalog, Russian, Tools, and Services.


  Ailibri''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 49.1
    operational_transparency: 0.0
  previous_composite: 6.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ailibri Com Domain Security
  slug: ailibri-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: ailibri-com
tags:
- Artificial Intelligence
- Catalog
- Russian
- Tools
- Services
website: https://ailibri.com/
---
