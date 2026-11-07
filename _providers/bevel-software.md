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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: System One inference hosted in Germany.
  name: eu/jev API
  slug: eu-jev-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/bevel-software/conformance/bevel-software-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bevel-software-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bevel-software/llms/bevel-software-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bevel-software-llms.txt
- group: auth
  href: https://artifacts.apis.io/bevel-software/well-known/bevel-software-jev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bevel-software-jev-security.txt
- group: agent
  href: https://artifacts.apis.io/bevel-software/well-known/bevel-software-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bevel-software-well-known.yml
- group: other
  href: https://artifacts.apis.io/bevel-software/hosts/bevel-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bevel-software-hosts.yml
- group: other
  href: https://artifacts.apis.io/bevel-software/vendors/bevel-software-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bevel-software-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bevel-software/security/bevel-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bevel-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bevel.software/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bevel.software/platform
- group: docs
  title: ''
  type: APIReference
  url: https://www.bevel.software/platform
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bevel.software/platform
- group: operate
  title: ''
  type: Support
  url: https://www.bevel.software/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bevel.software/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bevel.software/impressum
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bevel-Software
created: '2026-11-02'
description: Bevel builds applied AI tools for German enterprises, offering the Bevel OS platform and the open‑source Hexis framework. The team, originating from TU Munich, MIT and Cambridge, created the Universal Tool Calling Protocol (UTCP) and the CodeMode library, enabling agents to execute code and call tools natively. Backed by CDTM and UnternehmerTUM, Bevel focuses on low‑level AI stack integration and open‑source tooling for enterprise AI deployments.
layout: provider
modified: '2026-11-02'
name: Bevel
nav: Providers
network: true
overview: 'Bevel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Enterprise, Open Source, Tool Calling, and German.


  Bevel''s developer surface includes documentation, API reference, getting-started guide, support, and 11 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 62.5
    operational_transparency: 13.2
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bevel Software Domain Security
  slug: bevel-software-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bevel-software
tags:
- Artificial Intelligence
- Enterprise
- Open Source
- Tool Calling
- German
website: https://www.bevel.software/
---
