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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Kivra provides a digital mailbox API documented at the developer portal.
  name: Kivra API
  slug: kivra-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/kivra/well-known/kivra-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kivra-well-known.yml
- group: other
  href: https://artifacts.apis.io/kivra/hosts/kivra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kivra-hosts.yml
- group: build
  href: https://artifacts.apis.io/kivra/packages/kivra-packages.yml
  title: ''
  type: SDKs
  url: packages/kivra-packages.yml
- group: build
  href: https://artifacts.apis.io/kivra/packages/kivra-packages.yml
  title: ''
  type: Packages
  url: packages/kivra-packages.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.kivra.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kivra
- group: auth
  href: https://artifacts.apis.io/kivra/security/kivra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kivra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kivra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kivra.se/sv/om-kivra
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kivra.se/sv/om-kivra
- group: start
  title: ''
  type: GettingStarted
  url: https://kivra.se/sv/privat/registrera
- group: operate
  title: ''
  type: Support
  url: https://kivra.se/sv/om-kivra/hjalpcenter
- group: company
  title: ''
  type: Blog
  url: https://kivra.se/sv/om-kivra/press
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kivra.se/sv/om-kivra/villkor
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kivra.se/sv/om-kivra/dataskydd
coverage:
  checked: '2026-10-15'
  detail: Developer portal returns HTML with no machine‑readable OpenAPI spec, only JavaScript‑rendered pages.
  evidence:
  - status: 200
    url: https://developer.kivra.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Kivra provides a digital mailbox service for individuals and businesses in Sweden, allowing users to receive, store, and manage electronic mail, invoices, and official documents securely. The platform aims to reduce paper usage and streamline communication between citizens, companies, and public authorities, offering features such as digital receipts, payment handling, and identity verification through Kivra ID.
image: https://images.ctfassets.net/7jy2i7elrvww/1mJ4a8ridMWS0MspiIkS8O/9068246f91db7929d82cabd5f6bbaad4/dog-hero-background__1_.webp?w=1000
layout: provider
modified: '2026-10-15'
name: Kivra
nav: Providers
network: true
overview: 'Kivra is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Mailbox, Sweden, Fintech, and Secure Communications.


  Kivra''s developer surface includes API reference, documentation, getting-started guide, support, engineering blog, and 10 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 29.8
    discoverability: 57.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 28.8
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kivra/kivra-2026-11-03T134434.png
security:
- kind: domain-security
  name: Kivra Domain Security
  slug: kivra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kivra
tags:
- Company
- Digital Mailbox
- Sweden
- Fintech
- Secure Communications
website: https://kivra.com/
---
