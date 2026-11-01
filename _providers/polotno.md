---
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/polotno/llms/polotno-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/polotno-llms.txt
- group: agent
  href: https://artifacts.apis.io/polotno/well-known/polotno-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/polotno-well-known.yml
- group: other
  href: https://artifacts.apis.io/polotno/hosts/polotno-hosts.yml
  title: ''
  type: Hosts
  url: hosts/polotno-hosts.yml
- group: other
  href: https://artifacts.apis.io/polotno/vendors/polotno-vendors.yml
  title: ''
  type: Vendors
  url: vendors/polotno-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://polotno.com/legal/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://polotno.com/legal/security
- group: build
  title: ''
  type: SDKs
  url: https://polotno.com/sdk/product/pdf
- group: operate
  title: ''
  type: Roadmap
  url: https://community.polotno.com/c/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://polotno.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://polotno.com/sdk/pricing
- group: start
  title: ''
  type: Login
  url: https://polotno.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://polotno.com/docs/overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://community.polotno.com/c/changelog/
- group: company
  title: ''
  type: Blog
  url: https://polotno.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://community.polotno.com/c/ask/issues-getting-polotno-sdk-working-out-of-the-box-following-quick-start
- group: auth
  href: https://artifacts.apis.io/polotno/security/polotno-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/polotno-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/polotno/security/polotno-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/polotno-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://polotno.com/
coverage:
  checked: '2026-10-27'
  detail: Polotno provides HTML documentation but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contracts were found.
  evidence:
  - status: 404
    url: https://polotno.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Polotno provides a powerful, open-source canvas library for building design tools and visual editors directly in the browser. It offers a flexible, component‑based architecture, extensive customization options, and a rich set of pre‑built UI elements, enabling developers to create sophisticated graphic applications without reinventing core drawing functionality. The library is actively maintained, supports modern web standards, and integrates seamlessly with React, Vue, and other frameworks, making it a versatile choice for both startups and enterprise projects seeking high‑performance, client‑side design capabilities.
image: https://polotno.com/og/default.png
layout: provider
modified: '2026-10-26'
name: Polotno
nav: Providers
network: true
overview: 'Polotno is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Canvas, DesignTools, OpenSource, and JavaScript.


  Polotno''s developer surface includes pricing, documentation, changelog, engineering blog, getting-started guide, and 13 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 48.2
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Polotno Domain Security
  slug: polotno-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Polotno Vulnerability Disclosure
  slug: polotno-vulnerability-disclosure
  summary_line: no policy recorded
slug: polotno
tags:
- Company
- Canvas
- DesignTools
- OpenSource
- JavaScript
website: https://polotno.com/
---
