---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.agranilabs.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agrani-labs
- group: company
  title: ''
  type: Careers
  url: https://jobs.agranilabs.com
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/agrani-labs_stock/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agrani-labs/refs/heads/main/security/agrani-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agrani-labs-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agrani-labs/refs/heads/main/llms/agrani-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agrani-labs-llms.txt
coverage:
  checked: '2026-09-12'
  detail: Agrani Labs is a pre-product AI-GPU startup eleven months out of stealth whose entire web presence is one static Apache-served page at agranilabs.com plus a Notion careers site — api., docs. and developer.agranilabs.com do not resolve in DNS, and every OpenAPI, GraphQL and /.well-known/ path on the live hosts returns 404.
  evidence:
  - status: 200
    url: https://www.agranilabs.com/
  - status: 404
    url: https://www.agranilabs.com/openapi.json
  - status: 404
    url: https://www.agranilabs.com/graphql
  - status: 404
    url: https://www.agranilabs.com/.well-known/api-catalog
  - status: 404
    url: https://www.agranilabs.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: 'Agrani Labs is a Bengaluru, India semiconductor and systems-software company founded in December 2024 by Dheemanth Nagaraj (CEO), Ashok Jagannathan (chief architect), Srikanth Nimmagadda (CTO) and Rajesh Vivekanandham (chief performance architect), all former AMD and Intel engineers, with Pentium architect Vinod Dham as founding advisor. The company is building indigenous AI GPUs together with the full software stack around them — compilers, kernel and math libraries, system software and AI frameworks — for enterprise and datacenter compute in North America and Asia, and emerged from stealth in January 2026 with an $8M seed round led by Peak XV Partners. Agrani Labs is a pre-product silicon company: agranilabs.com is a single static marketing page with a team section, a Notion-hosted careers site and a contact form, and it publishes no developer portal, documentation, API reference, SDK, CLI, changelog, status page or pricing. Enrichment probing on 2026-09-12 found no OpenAPI,
  Swagger, GraphQL, AsyncAPI, WSDL, gRPC, MCP or A2A agent-card surface on any host, no /.well-known/ documents, no public GitHub organization and no first-party packages in npm, PyPI, Maven Central, NuGet, RubyGems, crates.io or pkg.go.dev.'
image: https://agranilabs.com/Logos/agrani-logo.png
layout: provider
modified: '2026-09-12'
name: Agrani Labs
nav: Providers
network: true
overview: Agrani Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, AI Chips, GPU, and Artificial Intelligence.
plans:
- name: Agrani Labs Plans Pricing
  plan_count: 0
  slug: agrani-labs-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Agrani Labs Rate Limits
  slug: agrani-labs-rate-limits
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 6
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 5.0
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agrani Labs Domain Security
  slug: agrani-labs-domain-security
  summary_line: TLSv1.2
slug: agrani-labs
tags:
- Company
- Semiconductors
- AI Chips
- GPU
- Artificial Intelligence
- Data Center
- Compute Infrastructure
- Hardware
- Deep Tech
- India
website: https://www.agranilabs.com/
---
