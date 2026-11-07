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
api_count: 0
artifact_total: 3
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lm-kit.com/legal/legal-notice/
- group: commercial
  href: https://artifacts.apis.io/lm-kit/plans/lm-kit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lm-kit-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/lm-kit/llms/lm-kit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lm-kit-llms.txt
- group: auth
  href: https://artifacts.apis.io/lm-kit/well-known/lm-kit-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lm-kit-security.txt
- group: agent
  href: https://artifacts.apis.io/lm-kit/well-known/lm-kit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lm-kit-well-known.yml
- group: other
  href: https://artifacts.apis.io/lm-kit/hosts/lm-kit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lm-kit-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://lm-kit.com/trust/
- group: operate
  title: ''
  type: Support
  url: https://lm-kit.com/support/
- group: auth
  title: ''
  type: Security
  url: https://lm-kit.com/products/lm-kit-one/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LM-Kit
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lm-kit.com/lm-kit-one/changelog/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://lm-kit.com/quickstart/
- group: company
  title: ''
  type: Website
  url: https://lm-kit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lm-kit.com/
- group: company
  title: ''
  type: Blog
  url: https://lm-kit.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://lm-kit.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lm-kit.com/legal/privacy
- group: auth
  href: https://artifacts.apis.io/lm-kit/security/lm-kit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lm-kit-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lm-kit/security/lm-kit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lm-kit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lm-kit.com/
created: '2026-10-21'
description: LM-Kit provides private AI infrastructure for enterprises, offering LM-Kit One as a self‑hosted AI application server and LM-Kit.NET as an embedded runtime for .NET applications. It enables running models, agents, retrieval‑augmented generation, search, and document intelligence within your own infrastructure, ensuring data privacy and control. Part of the Calico IIM Group, LM‑Kit focuses on secure, on‑premise AI solutions for businesses.
image: https://lm-kit.com/img/brand/og-default.png
layout: provider
modified: '2026-10-21'
name: LM-Kit
nav: Providers
network: true
overview: 'LM-Kit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Private, Enterprise, and Infrastructure.


  LM-Kit''s developer surface includes support, changelog, getting-started guide, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Lm Kit Plans Pricing
  plan_count: 2
  slug: lm-kit-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 40.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lm-kit/lm-kit-2026-11-03T135014.png
security:
- kind: domain-security
  name: Lm Kit Domain Security
  slug: lm-kit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lm Kit Vulnerability Disclosure
  slug: lm-kit-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lm-kit
tags:
- Company
- Artificial Intelligence
- Private
- Enterprise
- Infrastructure
website: https://lm-kit.com/
---
