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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-18'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agrimwholesale/refs/heads/main/security/agrimwholesale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agrimwholesale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agrim.app/
- group: company
  title: ''
  type: About
  url: https://agrim.app/about-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agrim.app/policy/tnc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agrim.app/policy/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agrimindia/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agrimwholesale/refs/heads/main/llms/agrimwholesale-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agrimwholesale-llms.txt
coverage:
  checked: '2026-09-13'
  detail: Agrim ships its marketplace only as Android retailer and seller apps plus a Next.js marketing site; agrim.app has no developer, API or integration section anywhere in its navigation, and the company's own backend host api.agrim.app answers a bare "Hello, Welcome to AGRIM" HTML page on / while returning 404 for every OpenAPI, Swagger, GraphQL, MCP and /.well-known/ discovery path probed.
  evidence:
  - status: 200
    url: https://api.agrim.app/
  - status: 404
    url: https://api.agrim.app/openapi.json
  - status: 404
    url: https://api.agrim.app/graphql
  - status: 404
    url: https://agrim.app/llms.txt
  - status: 404
    url: https://agrim.app/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: Agrim Wholesale Private Limited (branded AGRIM) is a Gurugram, India based business-to-business e-commerce marketplace for agricultural inputs, connecting agri-input manufacturers and wholesale suppliers with small rural retailers. Founded in 2020 by Avi Jain and Mukul Garg, the company lists more than 30,000 seed, crop-protection, fertiliser and farm-equipment products from over 1,200 manufacturers and fulfils orders across a pan-India network. The platform is delivered to retailers and sellers as Android applications and a marketing website at agrim.app; as of this profile the company publishes no public developer program, API reference, or machine-readable API contract.
image: https://agrim.app/favicon.png
layout: provider
modified: '2026-09-13'
name: Agrim Wholesale
nav: Providers
network: true
overview: Agrim Wholesale is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgriTech, Wholesale, and B2B.
random_paper: 18
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
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
  previous_composite: 9.2
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agrimwholesale Domain Security
  slug: agrimwholesale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agrimwholesale
tags:
- Company
- Agriculture
- AgriTech
- Wholesale
- B2B
- Marketplace
- E-Commerce
- Supply Chain
- India
website: https://agrim.app/
---
