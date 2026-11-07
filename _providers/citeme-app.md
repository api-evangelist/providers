---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
- description: Citation generation API as documented on the CiteMe site.
  name: CiteMe API
  slug: citeme-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/citeme-app/plans/citeme-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/citeme-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/citeme-app/conformance/citeme-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/citeme-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/citeme-app/llms/citeme-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citeme-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/citeme-app/well-known/citeme-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citeme-app-security.txt
- group: agent
  href: https://artifacts.apis.io/citeme-app/well-known/citeme-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citeme-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/citeme-app/hosts/citeme-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citeme-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/citeme-app/vendors/citeme-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citeme-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/citeme-app/packages/citeme-app-packages.yml
  title: ''
  type: SDKs
  url: packages/citeme-app-packages.yml
- group: build
  href: https://artifacts.apis.io/citeme-app/packages/citeme-app-packages.yml
  title: ''
  type: Packages
  url: packages/citeme-app-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citeme.app/terms
- group: operate
  title: ''
  type: Support
  url: https://citeme.app/support
- group: start
  title: ''
  type: SignUp
  url: https://citeme.app/signup
- group: auth
  title: ''
  type: Security
  url: https://citeme.app/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citeme.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://citeme.app/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://citeme.app/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/danielnichiata96
- group: docs
  title: ''
  type: Documentation
  url: https://citeme.app/guides
- group: docs
  title: ''
  type: APIReference
  url: https://citeme.app/llms.txt
- group: auth
  href: https://artifacts.apis.io/citeme-app/security/citeme-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/citeme-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/citeme-app/security/citeme-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citeme-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citeme.app/
created: '2026-11-03'
description: CiteMe (citeme.app) offers a free online citation generator that helps students, researchers, and professionals create accurate references in APA, MLA, Chicago, Harvard, and over 60 other styles. Users can paste a DOI, ISBN, URL, or title, and the tool formats the citation instantly without requiring signup, making academic writing faster and more reliable.
image: https://citeme.app/en/opengraph-image-ds8rmm?3949d840ca5d2e7c
layout: provider
modified: '2026-11-03'
name: CiteMe
nav: Providers
network: true
overview: 'CiteMe is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Citations, Academic, Tool, Free, and Web App.


  CiteMe''s developer surface includes support, signup flow, pricing, documentation, API reference, and 17 more developer resources.'
plans:
- name: Citeme App Plans Pricing
  plan_count: 4
  slug: citeme-app-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 67.0
    operational_transparency: 7.9
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Citeme App Domain Security
  slug: citeme-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Citeme App Vulnerability Disclosure
  slug: citeme-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: citeme-app
tags:
- Citations
- Academic
- Tool
- Free
- Web App
website: https://citeme.app/
---
