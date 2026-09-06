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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RapidSilicon
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/os-fpga/Raptor
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rapid-silicon-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rapid-silicon-llms.txt
coverage:
  checked: '2026-08-26'
  detail: 'Rapid Silicon sells eFPGA IP cores and a GPL3 desktop RTL-to-bitstream tool-chain (Raptor), never a hosted service, and ships no developer program of any kind — and its corporate site is now gone on top of that: since 2026-05-25 rapidsilicon.com 301s to realdha.com, a domain-brokerage listing, and returns 404 for /openapi.json, /llms.txt, every former product and documentation path, and all seven /.well-known/ paths, while a GitHub code search across both the RapidSilicon and os-fpga organizations returns zero OpenAPI or Swagger documents.'
  evidence:
  - status: 301
    url: https://rapidsilicon.com/
  - status: 404
    url: https://rapidsilicon.com/openapi.json
  - status: 404
    url: https://rapidsilicon.com/llms.txt
  - status: 404
    url: https://rapidsilicon.com/.well-known/agent-card.json
  - status: 404
    url: https://rapidsilicon.com/documentation
  - status: 200
    url: https://github.com/RapidSilicon
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Rapid Silicon is a fabless semiconductor company founded in 2019 and headquartered in Los Gatos, California, building AI- and intelligent-edge-focused FPGAs and embedded FPGA (eFPGA) IP on an open-source technology base. Its product line covers the Gemini FPGA family, the Vega eFPGA IP core (a customizable, scalable embeddable FPGA fabric from roughly 1.5K to 100K+ logic cells with configurable BRAM and DSP MAC tiles), and the Rapid eFPGA Configurator for self-service eFPGA resource sizing. Design work is done in the Raptor Design Suite, the company's RTL-to-bitstream EDA tool-chain covering simulation, synthesis, placement, routing, bitstream generation and device configuration, released under GPL3 as what the company describes as the first complete commercially available open-source FPGA tool-chain. Rapid Silicon raised a $15M seed round in 2021 and a $30M Series A in January 2023 from Cambium Capital Partners and Chengwei Capital, and is led by chairman and CEO Naveed Sherwani.
  The company's products are silicon IP and locally installed design software rather than a hosted service, so it publishes no public web API, developer portal or machine-readable API contract; as of 2026-05-25 its rapidsilicon.com website no longer serves company content and redirects to a domain-brokerage page.
layout: provider
modified: '2026-08-26'
name: Rapid Silicon
nav: Providers
network: true
overview: Rapid Silicon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, FPGA, eFPGA, and Electronic Design Automation.
random_paper: 3
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 6.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Rapid Silicon Domain Security
  slug: rapid-silicon-domain-security
  summary_line: HSTS
slug: rapid-silicon
tags:
- Company
- Semiconductors
- FPGA
- eFPGA
- Electronic Design Automation
- Chip Design
- Open-Source
- Hardware
- Edge AI
- Silicon IP
---
