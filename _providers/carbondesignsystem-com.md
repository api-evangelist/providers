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
- description: The Carbon Design System provides UI components and design guidelines. Documentation is available at the API reference page.
  name: Carbon Design System API
  slug: carbon-design-system-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/carbondesignsystem-com/llms/carbondesignsystem-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carbondesignsystem-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/carbondesignsystem-com/well-known/carbondesignsystem-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carbondesignsystem-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/carbondesignsystem-com/hosts/carbondesignsystem-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbondesignsystem-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/carbondesignsystem-com/vendors/carbondesignsystem-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbondesignsystem-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.carbondesignsystem.com/support/faqs
- group: start
  title: ''
  type: Login
  url: https://www.carbondesignsystem.com/building-blocks/core/patterns/login
- group: auth
  href: https://artifacts.apis.io/carbondesignsystem-com/security/carbondesignsystem-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbondesignsystem-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carbondesignsystem.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.carbondesignsystem.com/getting-started/designing/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.carbondesignsystem.com/getting-started/developing/overview
coverage:
  checked: '2026-11-03'
  detail: The provider's documentation site contains no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.carbondesignsystem.com/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Carbon is IBM’s open source design system for products and digital experiences. It provides a comprehensive set of UI components, design guidelines, and resources to help teams build consistent, accessible, and performant digital products. The system is built on the IBM Design Language and is maintained by a vibrant community of contributors, offering extensive documentation, tooling, and support for developers and designers alike.
image: https://www.carbondesignsystem.com/ogimage.png
layout: provider
modified: '2026-11-03'
name: Carbon Design System
nav: Providers
network: true
overview: 'Carbon Design System is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Design Systems, Open Source, UI Components, Accessibility, and Digital Experience.


  Carbon Design System''s developer surface includes support, documentation, getting-started guide, and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
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
  name: Carbondesignsystem Com Domain Security
  slug: carbondesignsystem-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: carbondesignsystem-com
tags:
- Design Systems
- Open Source
- UI Components
- Accessibility
- Digital Experience
- IBM
website: https://www.carbondesignsystem.com/
---
