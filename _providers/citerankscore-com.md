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
- group: auth
  title: ''
  type: Security
  url: https://citerankscore.com/security-policy.html
- group: commercial
  href: https://artifacts.apis.io/citerankscore-com/plans/citerankscore-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/citerankscore-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/citerankscore-com/changelog/citerankscore-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/citerankscore-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/citerankscore-com/llms/citerankscore-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citerankscore-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/citerankscore-com/well-known/citerankscore-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citerankscore-com-security.txt
- group: agent
  href: https://artifacts.apis.io/citerankscore-com/well-known/citerankscore-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citerankscore-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/citerankscore-com/hosts/citerankscore-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citerankscore-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/citerankscore-com/vendors/citerankscore-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citerankscore-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citerankscore.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citerankscore.com/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://citerankscore.com/blog/
- group: auth
  href: https://artifacts.apis.io/citerankscore-com/security/citerankscore-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/citerankscore-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/citerankscore-com/security/citerankscore-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citerankscore-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citerankscore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://citerankscore.com/mcp-docs.html
- group: commercial
  title: ''
  type: Pricing
  url: https://citerankscore.com/pricing.html
- group: start
  title: ''
  type: GettingStarted
  url: https://citerankscore.com/mcp-docs.html
coverage:
  checked: '2026-11-04'
  detail: Developer portal pages provide HTML docs but no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract files.
  evidence:
  - status: 200
    url: https://citerankscore.com/mcp-docs.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Citerank provides an AI Search Visibility Platform that identifies why AI engines skip your site, highlighting entity gaps, schema issues, crawler blocks, passage structure, and machine E‑E‑A‑T. It ranks impacts and generates ready‑to‑deploy fixes, helping improve visibility across AI search engines.
image: https://citerankscore.com/api/og
layout: provider
modified: '2026-11-03'
name: Citerank
nav: Providers
network: true
overview: 'Citerank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Search, Visibility, Platform, and SEO.


  Citerank''s developer surface includes changelog, engineering blog, documentation, pricing, getting-started guide, and 12 more developer resources.'
plans:
- name: Citerankscore Com Plans Pricing
  plan_count: 4
  slug: citerankscore-com-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Citerankscore Com Domain Security
  slug: citerankscore-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Citerankscore Com Vulnerability Disclosure
  slug: citerankscore-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: citerankscore-com
tags:
- Artificial Intelligence
- Search
- Visibility
- Platform
- SEO
- Company
website: https://citerankscore.com/
---
