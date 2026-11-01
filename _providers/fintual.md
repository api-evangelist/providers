---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/fintual/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://fintual.com/security-policy.txt
- group: agent
  href: https://artifacts.apis.io/fintual/llms/fintual-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fintual-llms.txt
- group: auth
  href: https://artifacts.apis.io/fintual/well-known/fintual-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fintual-security.txt
- group: auth
  href: https://artifacts.apis.io/fintual/well-known/fintual-fintual-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fintual-fintual-security.txt
- group: auth
  href: https://artifacts.apis.io/fintual/well-known/fintual-ayuda-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fintual-ayuda-security.txt
- group: agent
  href: https://artifacts.apis.io/fintual/well-known/fintual-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fintual-well-known.yml
- group: other
  href: https://artifacts.apis.io/fintual/hosts/fintual-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fintual-hosts.yml
- group: other
  href: https://artifacts.apis.io/fintual/vendors/fintual-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fintual-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://fintual.cl/f/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://fintual.cl/docs
- group: auth
  href: https://artifacts.apis.io/fintual/security/fintual-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fintual-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fintual/security/fintual-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fintual-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fintual.cl/
coverage:
  checked: '2026-10-29'
  detail: The provider's documentation at https://fintual.cl/docs contains no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://fintual.cl/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Fintual is a Chilean fintech and robo‑advisor that provides a regulated investment platform allowing anyone to invest in mutual funds, APV retirement accounts, stocks and ETFs with no minimums. Over 200,000 users across Latin America use the app to manage diversified portfolios backed by data‑driven strategies. The company is backed by Sequoia Capital and focuses on transparent, low‑cost investing.
image: https://fintual.cl/f/og-image.png
layout: provider
modified: '2026-10-28'
name: Fintual
nav: Providers
network: true
overview: 'Fintual is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, Investment, Chile, and Robo-Advisor.


  Fintual''s developer surface includes documentation and 13 more developer resources.'
random_paper: 11
scopes:
- name: Fintual Scopes
  scope_count: 0
  slug: fintual-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.0
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
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
- kind: authentication
  name: Fintual Authentication
  slug: fintual-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Fintual Domain Security
  slug: fintual-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fintual Vulnerability Disclosure
  slug: fintual-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fintual
tags:
- Company
- FinTech
- Investment
- Chile
- Robo-Advisor
website: https://fintual.cl/
---
