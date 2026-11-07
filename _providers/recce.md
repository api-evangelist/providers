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
- description: Recce provides a data review agent platform with documentation at https://docs.reccehq.com. No machine‑readable OpenAPI or other contract was found despite probing known locations, indicating the docs
  name: Recce API
  slug: recce-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/recce/plans/recce-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/recce-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/recce/changelog/recce-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/recce-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://reccehq.com/security/
- group: design
  href: https://artifacts.apis.io/recce/conformance/recce-conformance.yml
  title: ''
  type: Conformance
  url: conformance/recce-conformance.yml
- group: agent
  href: https://artifacts.apis.io/recce/llms/recce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/recce-llms.txt
- group: agent
  href: https://artifacts.apis.io/recce/well-known/recce-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/recce-well-known.yml
- group: other
  href: https://artifacts.apis.io/recce/hosts/recce-hosts.yml
  title: ''
  type: Hosts
  url: hosts/recce-hosts.yml
- group: other
  href: https://artifacts.apis.io/recce/vendors/recce-vendors.yml
  title: ''
  type: Vendors
  url: vendors/recce-vendors.yml
- group: build
  href: https://artifacts.apis.io/recce/packages/recce-packages.yml
  title: ''
  type: SDKs
  url: packages/recce-packages.yml
- group: build
  href: https://artifacts.apis.io/recce/packages/recce-packages.yml
  title: ''
  type: Packages
  url: packages/recce-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reccehq.com/statements/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://reccehq.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reccehq.com/statements/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://reccehq.com/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://reccehq.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://blog.reccehq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datarecce.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.reccehq.com/
- group: auth
  href: https://artifacts.apis.io/recce/security/recce-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/recce-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/recce/security/recce-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/recce-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/recce/security/recce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/recce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reccehq.com
coverage:
  checked: '2026-10-29'
  detail: Docs are rendered as a JavaScript SPA, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.reccehq.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Recce is your AI Data Review Agent that validates how every pull request impacts your data. It helps engineering teams understand data changes before merging code, providing confidence and preventing blind trust in automated updates. The platform offers automated data review, impact analysis, and approval workflows for data pipelines.
image: https://reccehq.com/assets/images/recce-og-image.avif
layout: provider
modified: '2026-10-29'
name: Recce
nav: Providers
network: true
overview: 'Recce is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, DataReview, Engineering, and Software-as-a-Service.


  Recce''s developer surface includes changelog, pricing, engineering blog, documentation, and 18 more developer resources.'
plans:
- name: Recce Plans Pricing
  plan_count: 3
  slug: recce-plans-pricing
random_paper: 10
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 18.4
  previous_composite: 35.4
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/recce/recce-2026-11-03T142042.png
security:
- kind: domain-security
  name: Recce Domain Security
  slug: recce-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Recce Vulnerability Disclosure
  slug: recce-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Recce Trust Center
  slug: recce-trust-center
  summary_line: SOC 2
slug: recce
tags:
- Company
- Artificial Intelligence
- DataReview
- Engineering
- Software-as-a-Service
website: https://reccehq.com
---
