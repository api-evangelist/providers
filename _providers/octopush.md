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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/octopush/llms/octopush-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/octopush-llms.txt
- group: other
  href: https://artifacts.apis.io/octopush/hosts/octopush-hosts.yml
  title: ''
  type: Hosts
  url: hosts/octopush-hosts.yml
- group: other
  href: https://artifacts.apis.io/octopush/vendors/octopush-vendors.yml
  title: ''
  type: Vendors
  url: vendors/octopush-vendors.yml
- group: build
  href: https://artifacts.apis.io/octopush/packages/octopush-packages.yml
  title: ''
  type: SDKs
  url: packages/octopush-packages.yml
- group: build
  href: https://artifacts.apis.io/octopush/packages/octopush-packages.yml
  title: ''
  type: Packages
  url: packages/octopush-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.octopush.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/octopush
- group: auth
  href: https://artifacts.apis.io/octopush/security/octopush-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/octopush-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.octopush.com/
- group: docs
  title: ''
  type: Documentation
  url: https://octopush-api.readme.io/
- group: company
  title: ''
  type: Blog
  url: https://www.octopush.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.octopush.com/tarifs/tarifs-sms-france
coverage:
  checked: '2026-10-27'
  detail: The provider's documentation at https://octopush-api.readme.io/ does not expose a machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contract.
  evidence:
  - status: 200
    url: https://octopush-api.readme.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Octopush is a French multichannel communication platform offering SMS, Email, RCS, and voice services. It provides tools for campaign management, transactional messaging, contact verification, virtual numbers, and real‑time analytics. The service targets businesses seeking high‑delivery rates and compliance across multiple channels, with integrations for Zapier, WooCommerce, and custom APIs.
image: https://cdn.prod.website-files.com/6a91acc85d4f92dde457d018/6aa96add4f375ce05817a606_Open%20Graph%20-%20FR.png
layout: provider
modified: '2026-10-26'
name: Octopush
nav: Providers
network: true
overview: 'Octopush is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Communication, Marketing, SMS, Email, and Multichannel.


  Octopush''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 5.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Octopush Domain Security
  slug: octopush-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: octopush
tags:
- Communication
- Marketing
- SMS
- Email
- Multichannel
website: https://www.octopush.com/
---
