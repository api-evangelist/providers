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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/flowers-software/llms/flowers-software-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flowers-software-llms.txt
- group: other
  href: https://artifacts.apis.io/flowers-software/hosts/flowers-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flowers-software-hosts.yml
- group: other
  href: https://artifacts.apis.io/flowers-software/vendors/flowers-software-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flowers-software-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flowers-software
- group: auth
  href: https://artifacts.apis.io/flowers-software/security/flowers-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flowers-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flowers-software.de/
- group: company
  title: ''
  type: Blog
  url: https://www.flowers-software.de/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flowers-software.de/en/prices
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flowers-software.de/de/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flowers-software.de/de/datenschutz
- group: operate
  title: ''
  type: Support
  url: https://www.flowers-software.de/en/contact
coverage:
  checked: '2026-10-26'
  detail: The provider's website returns a JavaScript shell and cannot be read without a browser.
  evidence:
  - status: 200
    url: https://www.flowers-software.de/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Flowers Software automates finance and approval processes for the German Mittelstand, offering solutions for invoice approval, invoice capture, contract and document workflows, and integration with bookkeeping and ERP systems such as DATEV and SAP. The company provides a platform to streamline financial operations for small and medium-sized enterprises in Germany.
layout: provider
modified: '2026-10-26'
name: Flowers Software
nav: Providers
network: true
overview: 'Flowers Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Automation, ERP, and Germany.


  Flowers Software''s developer surface includes engineering blog, pricing, support, and 8 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 51.8
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 13.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/flowers-software/flowers-software-2026-11-03T132158.png
security:
- kind: domain-security
  name: Flowers Software Domain Security
  slug: flowers-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flowers-software
tags:
- Company
- Finance
- Automation
- ERP
- Germany
website: https://flowers-software.de/
---
