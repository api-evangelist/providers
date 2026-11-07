---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
  href: https://artifacts.apis.io/zugferd-validator-de/llms/zugferd-validator-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zugferd-validator-de-llms.txt
- group: other
  href: https://artifacts.apis.io/zugferd-validator-de/hosts/zugferd-validator-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zugferd-validator-de-hosts.yml
- group: build
  href: https://artifacts.apis.io/zugferd-validator-de/packages/zugferd-validator-de-packages.yml
  title: ''
  type: SDKs
  url: packages/zugferd-validator-de-packages.yml
- group: build
  href: https://artifacts.apis.io/zugferd-validator-de/packages/zugferd-validator-de-packages.yml
  title: ''
  type: Packages
  url: packages/zugferd-validator-de-packages.yml
- group: auth
  href: https://artifacts.apis.io/zugferd-validator-de/security/zugferd-validator-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zugferd-validator-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zugferd-validator.de/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zugferd-validator.de/
- group: commercial
  title: ''
  type: Pricing
  url: https://zugferd-validator.de/enterprise
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zugferd-validator.de/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zugferd-validator.de/datenschutz
- group: operate
  title: ''
  type: Support
  url: https://zugferd-validator.de/kontakt
coverage:
  checked: '2026-10-31'
  detail: Documentation is provided as static HTML with no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://docs.zugferd-validator.de/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: ZUGFeRD Validator provides an API and MCP client for validating electronic invoices (ZUGFeRD, Factur‑X, XRechnung). Users can upload PDF or XML invoices and receive structured JSON validation results with error codes and correction suggestions, all without registration for limited free use. The service offers tools for conversion, consistency checks, and rule queries, targeting developers and businesses handling e‑invoicing in Germany and EU.
image: https://zugferd-validator.de/og-image.png
layout: provider
modified: '2026-10-31'
name: zugferd-validator-de
nav: Providers
network: true
overview: 'zugferd-validator-de is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Validation, E-Invoicing, and Germany.


  zugferd-validator-de''s developer surface includes documentation, pricing, support, and 8 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 39.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 15.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zugferd Validator De Domain Security
  slug: zugferd-validator-de-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zugferd-validator-de
tags:
- Company
- Validation
- E-Invoicing
- Germany
website: https://zugferd-validator.de/
---
