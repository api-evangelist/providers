---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API under development; not publicly available yet.
  name: Atmita Developer API
  slug: atmita-developer-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/atmita-com/plans/atmita-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atmita-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/atmita-com/changelog/atmita-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/atmita-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/atmita-com/llms/atmita-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atmita-com-llms.txt
- group: other
  href: https://artifacts.apis.io/atmita-com/hosts/atmita-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atmita-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/atmita-com/vendors/atmita-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atmita-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.atmita.com/changelog
- group: auth
  href: https://artifacts.apis.io/atmita-com/security/atmita-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atmita-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atmita.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atmita.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atmita.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atmita.com/legal/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.atmita.com/legal/security
coverage:
  checked: '2026-11-02'
  detail: Developer API page states the API is not public yet and no machine-readable spec is provided.
  evidence:
  - status: 200
    url: https://www.atmita.com/products/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Atmita is an AI‑powered autonomous agent platform that automates tasks across apps, browsers, and APIs. It operates on a schedule, remembers context, and integrates with over a thousand tools, enabling solopreneurs and small businesses to streamline workflows, generate content, and manage leads without manual effort.
image: https://www.atmita.com/marketing/atmita-logo-current.png
layout: provider
modified: '2026-11-01'
name: Atmita
nav: Providers
network: true
overview: 'Atmita is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Productivity, Software-as-a-Service, and Agents.


  Atmita''s developer surface includes changelog, pricing, and 10 more developer resources.'
plans:
- name: Atmita Com Plans Pricing
  plan_count: 6
  slug: atmita-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Atmita Com Rate Limits
  slug: atmita-com-rate-limits
scopes:
- name: Atmita Com Scopes
  scope_count: 0
  slug: atmita-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 22.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atmita Com Authentication
  slug: atmita-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atmita Com Domain Security
  slug: atmita-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: atmita-com
tags:
- Artificial Intelligence
- Automation
- Productivity
- Software-as-a-Service
- Agents
website: https://www.atmita.com/
---
