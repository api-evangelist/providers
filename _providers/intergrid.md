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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/intergrid/llms/intergrid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/intergrid-llms.txt
- group: agent
  href: https://artifacts.apis.io/intergrid/well-known/intergrid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/intergrid-well-known.yml
- group: other
  href: https://artifacts.apis.io/intergrid/hosts/intergrid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intergrid-hosts.yml
- group: other
  href: https://artifacts.apis.io/intergrid/vendors/intergrid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/intergrid-vendors.yml
- group: auth
  href: https://artifacts.apis.io/intergrid/security/intergrid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intergrid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://intergridsystems.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://intergridsystems.com/privacy-policy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://intergridsystems.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Intergrid provides autonomous control solutions for industrial energy systems, enabling operators to optimize energy consumption, integrate renewable sources, and automate grid interactions. Trusted by over 100 sites across Europe, Intergrid’s platform offers real-time monitoring, predictive analytics, and seamless integration with existing infrastructure, helping businesses reduce costs and improve sustainability.
image: https://intergridsystems.com/hubfs/Web%20optimized%20photos/Vatajankoski/Intergrid-Vatajankoski_Still%202026-01-28%20140451_2.35.1_lowres.jpg
layout: provider
modified: '2026-10-24'
name: Intergrid
nav: Providers
network: true
overview: Intergrid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Automation, Industrial, and Sustainability.
random_paper: 8
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 6.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/intergrid/intergrid-2026-11-03T133946.png
security:
- kind: domain-security
  name: Intergrid Domain Security
  slug: intergrid-domain-security
  summary_line: TLSv1.3 · HSTS
slug: intergrid
tags:
- Company
- Energy
- Automation
- Industrial
- Sustainability
website: https://intergridsystems.com
---
