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
api_count: 1
apis:
- description: BitSpire provides a platform for managing devices and services, but no public machine‑readable contract was found.
  name: BitSpire API
  slug: bitspire-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/bitspire-ch/llms/bitspire-ch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitspire-ch-llms.txt
- group: other
  href: https://artifacts.apis.io/bitspire-ch/hosts/bitspire-ch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitspire-ch-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitspire-ch/vendors/bitspire-ch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitspire-ch-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linkdotnet
- group: company
  title: ''
  type: Blog
  url: https://bitspire.ch/blog
- group: auth
  href: https://artifacts.apis.io/bitspire-ch/security/bitspire-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitspire-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitspire.ch/
coverage:
  checked: '2026-11-02'
  detail: No public OpenAPI, AsyncAPI, GraphQL, or other contract was found despite documentation links.
  evidence:
  - status: 0
    url: https://api.bitspire.ch/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BitSpire GmbH is a Swiss .NET consultancy delivering professional software development, architecture, and UX/UI design. Founded by Microsoft MVPs, they specialize in .NET, C#, ASP.NET Core, Blazor, and enterprise solutions, serving Switzerland, Germany, and Austria.
image: https://bitspire.ch/assets/bitspire-logo.l75rzjsfo1.webp
layout: provider
modified: '2026-11-02'
name: BitSpire GmbH
nav: Providers
network: true
overview: 'BitSpire GmbH is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, .NET, Software Development, Architecture, and UX/UI Design.


  BitSpire GmbH''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitspire Ch Domain Security
  slug: bitspire-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitspire-ch
tags:
- Company
- .NET
- Software Development
- Architecture
- UX/UI Design
website: https://bitspire.ch/
---
