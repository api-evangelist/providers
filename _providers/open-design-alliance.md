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
    dynamic_client_registration: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/open-design-alliance/vendors/open-design-alliance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/open-design-alliance-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/open-design-alliance/plans/open-design-alliance-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/open-design-alliance-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/open-design-alliance/llms/open-design-alliance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/open-design-alliance-llms.txt
- group: agent
  href: https://artifacts.apis.io/open-design-alliance/well-known/open-design-alliance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/open-design-alliance-well-known.yml
- group: other
  href: https://artifacts.apis.io/open-design-alliance/hosts/open-design-alliance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/open-design-alliance-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://www.opendesign.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opendesign.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.opendesign.com/user/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.opendesign.com/releases
- group: docs
  title: ''
  type: APIReference
  url: https://opendesign.com/guestfiles/oda_drawings_explorer/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.opendesign.com/getting_started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opendesign.com/
- group: auth
  href: https://artifacts.apis.io/open-design-alliance/security/open-design-alliance-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-design-alliance-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/open-design-alliance/security/open-design-alliance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/open-design-alliance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opendesign.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opendesign.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.opendesign.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.opendesign.com/blog
coverage:
  checked: '2026-10-23'
  detail: The provider's website does not expose any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.opendesign.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Open Design Alliance (ODA) is a non‑profit consortium that provides developers with tools and libraries to create, view, and edit CAD (Computer‑Aided Design) files across multiple platforms. Founded in 1998, ODA offers the Teigha platform, which supports a wide range of DWG, DGN, and other industry‑standard formats, enabling interoperability among CAD applications. The organization focuses on fostering collaboration among its member companies, delivering high‑quality SDKs, documentation, and support for building robust engineering and design software solutions. Through its open‑source initiatives and extensive developer resources, ODA empowers engineers, architects, and software developers to integrate advanced CAD capabilities into their products, accelerating innovation in the design and manufacturing sectors.
image: https://www.opendesign.com/themes/oda/img/oda_sign_black_orange.png
layout: provider
modified: '2026-10-23'
name: Open Design Alliance
nav: Providers
network: true
overview: 'Open Design Alliance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CAD, SDK, OpenSource, and Consortium.


  Open Design Alliance''s developer surface includes changelog, API reference, getting-started guide, documentation, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Open Design Alliance Plans Pricing
  plan_count: 6
  slug: open-design-alliance-plans-pricing
random_paper: 15
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Open Design Alliance Domain Security
  slug: open-design-alliance-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Open Design Alliance Vulnerability Disclosure
  slug: open-design-alliance-vulnerability-disclosure
  summary_line: no policy recorded
slug: open-design-alliance
tags:
- Company
- CAD
- SDK
- OpenSource
- Consortium
website: https://www.opendesign.com/
---
