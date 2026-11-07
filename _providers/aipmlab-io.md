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
  href: https://artifacts.apis.io/aipmlab-io/llms/aipmlab-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aipmlab-io-llms.txt
- group: other
  href: https://artifacts.apis.io/aipmlab-io/hosts/aipmlab-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aipmlab-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/aipmlab-io/vendors/aipmlab-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aipmlab-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aipmlab-io/security/aipmlab-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aipmlab-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aipmlab.io/
- group: docs
  title: ''
  type: APIReference
  url: https://aipmlab.io/api/mcp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aipmlab.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aipmlab.io/terms
coverage:
  checked: '2026-11-01'
  detail: MCP endpoint requires POST, blocking contract discovery
  evidence:
  - status: 405
    url: https://aipmlab.io/api/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: AI PM Lab provides interactive AI product management lessons and challenges, allowing users to explore models in 3D, run real‑world scenarios, and benchmark costs. The platform offers a suite of MCP‑enabled tools for prompt engineering, cost estimation, and evaluation, targeting developers and product teams building AI‑driven products.
image: https://aipmlab.io/opengraph-image?1ddc06e2261f1f27
layout: provider
modified: '2026-11-01'
name: AI PM Lab
nav: Providers
network: true
overview: 'AI PM Lab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Product Management, Education, Machine Learning, and Interactive.


  AI PM Lab''s developer surface includes API reference and 7 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 9.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
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
  name: Aipmlab Io Domain Security
  slug: aipmlab-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aipmlab-io
tags:
- Artificial Intelligence
- Product Management
- Education
- Machine Learning
- Interactive
website: https://aipmlab.io/
---
