---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.lattice-engines.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.dnb.com/en-us/products/dnb-rev-up-abx.html — a different registrable domain (lattice-engines.com -> dnb.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/dun-and-bradstreet/
- group: company
  title: ''
  type: Website
  url: https://www.lattice-engines.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lattice-engines-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lattice-engines-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lattice-engines-llms.txt
created: '2026-07-17'
description: 'Lattice Engines was a predictive marketing and AI-driven B2B customer data platform that applied machine learning to first-party CRM and marketing automation data combined with external firmographic, technographic, and intent signals in order to score accounts and leads, prioritize sales outreach, and power account-based marketing programs. The company was acquired by Dun & Bradstreet in 2019 and the product was rebranded D&B Lattice before being folded into the Dun & Bradstreet Rev.Up ABX go-to-market platform. Lattice Engines no longer operates as an independent brand and publishes no developer surface of its own: as of the 2026-07-19 enrichment probe, www.lattice-engines.com returns HTTP 301 to dnb.com, the apex domain returns HTTP 403, api.lattice-engines.com returns HTTP 404, and developer./docs. subdomains do not resolve. This profile is retained as a historical record; the live successor surface is documented in the api-evangelist dun-and-bradstreet repository.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lattice-engines.png
layout: provider
modified: '2026-07-19'
name: Lattice Engines
nav: Providers
network: true
overview: Lattice Engines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Acquired, Predictive Marketing, Account Based Marketing, and Sales Intelligence.
random_paper: 20
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lattice-engines/refs/heads/main/screenshots/lattice-engines-2026-07-25T224607.png
security:
- kind: domain-security
  name: Lattice Engines Domain Security
  slug: lattice-engines-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: lattice-engines
tags:
- Company
- Acquired
- Predictive Marketing
- Account Based Marketing
- Sales Intelligence
- Customer Data Platform
- Lead Scoring
- Machine-Learning
- B2B Marketing
- Historical
website: https://www.lattice-engines.com/
---
