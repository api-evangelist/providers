---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
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
  score: 6.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://www.jaikin.eu/politique-confidentialite
- group: auth
  href: https://artifacts.apis.io/jaikin-eu/authentication/jaikin-eu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jaikin-eu-authentication.yml
- group: agent
  href: https://artifacts.apis.io/jaikin-eu/llms/jaikin-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jaikin-eu-llms.txt
- group: auth
  href: https://artifacts.apis.io/jaikin-eu/well-known/jaikin-eu-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jaikin-eu-security.txt
- group: auth
  href: https://artifacts.apis.io/jaikin-eu/well-known/jaikin-eu-jaikin-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jaikin-eu-jaikin-security.txt
- group: agent
  href: https://artifacts.apis.io/jaikin-eu/well-known/jaikin-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jaikin-eu-well-known.yml
- group: other
  href: https://artifacts.apis.io/jaikin-eu/hosts/jaikin-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jaikin-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/jaikin-eu/vendors/jaikin-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jaikin-eu-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.jaikin.eu/glossaire/webhook
- group: auth
  href: https://artifacts.apis.io/jaikin-eu/security/jaikin-eu-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jaikin-eu-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jaikin-eu/security/jaikin-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jaikin-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jaikin.eu/
- group: company
  title: ''
  type: Blog
  url: https://www.jaikin.eu/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jaikin.eu/tarifs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jaikin.eu/conditions-generales
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jaikin.eu/politique-confidentialite
- group: operate
  title: ''
  type: Support
  url: https://www.jaikin.eu/contact
coverage:
  checked: '2026-10-30'
  detail: No machine‑readable API specification (OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL) was found on any discovered host.
  evidence:
  - status: 200
    url: https://www.jaikin.eu/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: JAIKIN is a French agency specializing in artificial intelligence, Odoo ERP integration, and custom software development for SMEs and mid‑size enterprises. Based in Alsace, it offers end‑to‑end solutions including Odoo integration, bespoke business applications, mobile apps for iOS and Android, and AI‑driven process automation. The company provides consulting, project scoping, migration, and ongoing support, delivering projects from €2,000 HT onward. Its services span industry, medical, legal, and other sectors, with a focus on rapid delivery and tailored technology stacks.
image: https://www.jaikin.eu/og-partage/jaikin-agence-ia-odoo-logiciels-sur-mesure-pme.jpg
layout: provider
modified: '2026-10-30'
name: jaikin-eu
nav: Providers
network: true
overview: 'jaikin-eu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Odoo, Custom Software, and Consulting.


  jaikin-eu''s developer surface includes authentication, engineering blog, pricing, support, and 13 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 55.4
    operational_transparency: 9.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/jaikin-eu/jaikin-eu-2026-11-03T134124.png
security:
- kind: authentication
  name: Jaikin Eu Authentication
  slug: jaikin-eu-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Jaikin Eu Domain Security
  slug: jaikin-eu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jaikin Eu Vulnerability Disclosure
  slug: jaikin-eu-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jaikin-eu
tags:
- Company
- Artificial Intelligence
- Odoo
- Custom Software
- Consulting
- France
website: https://jaikin.eu/
---
