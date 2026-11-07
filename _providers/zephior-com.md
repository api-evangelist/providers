---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: derived
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Read Zephior service information and search published resources. Public read‑only API.
  name: Zephior Public Discovery API
  slug: zephior-public-discovery-api
- description: Read‑only public assurance data.
  name: Zephior Trust Center API
  slug: zephior-trust-center-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/zephior-com/plans/zephior-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zephior-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/zephior-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/zephior-com/sandbox/zephior-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/zephior-com-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.zephior.com/
- group: design
  href: https://artifacts.apis.io/zephior-com/conformance/zephior-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zephior-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zephior-com/llms/zephior-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zephior-com-llms.txt
- group: other
  href: https://artifacts.apis.io/zephior-com/a2a/zephior-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/zephior-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/zephior-com/well-known/zephior-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zephior-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/zephior-com/hosts/zephior-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zephior-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/zephior-com/vendors/zephior-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zephior-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://zephior.com/security
- group: start
  title: ''
  type: Sandbox
  url: https://zephior.com/sandbox
- group: auth
  href: https://artifacts.apis.io/zephior-com/security/zephior-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zephior-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/zephior-com/security/zephior-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zephior-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zephior.com/
- group: docs
  title: ''
  type: Documentation
  url: https://zephior.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://zephior.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://zephior.com/developers
- group: operate
  title: ''
  type: Support
  url: https://zephior.com/contact
- group: company
  title: ''
  type: Blog
  url: https://zephior.com/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Zephior
- group: commercial
  title: ''
  type: Pricing
  url: https://zephior.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zephior.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zephior.com/privacy
created: '2026-10-31'
description: Zephior provides a global tender API that democratizes access to public procurement opportunities. Their platform aggregates data from over 10,000 procurement portals, offering searchable tender listings, pricing insights, and end‑to‑end bid execution tools. The service targets businesses seeking to discover and win public contracts worldwide, delivering read‑only APIs and agent tools without exposing customer data.
image: https://zephior.com/og-image.png?v=20261011
layout: provider
modified: '2026-10-31'
name: zephior-com
nav: Providers
network: true
overview: 'zephior-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Procurement, Tender, and Marketplace.


  zephior-com''s developer surface includes sandbox, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Zephior Com Plans Pricing
  plan_count: 8
  slug: zephior-com-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.1
  facets:
    access_clarity: 59.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 35.2
  provenance:
    conformance: derived
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zephior Com Domain Security
  slug: zephior-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zephior Com Trust Center
  slug: zephior-com-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 1
skills:
- name: search-public-tenders
  slug: zephior-com-search-public-tenders
slug: zephior-com
tags:
- Company
- Procurement
- Tender
- Marketplace
website: https://zephior.com/
---
