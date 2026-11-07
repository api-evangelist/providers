---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dwellsy Agentic Access
  operation_count: 4
  slug: dwellsy-agentic-access
  summary_line: 4 operations
api_count: 1
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/dwellsy/llms/dwellsy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dwellsy-llms.txt
- group: agent
  href: https://artifacts.apis.io/dwellsy/well-known/dwellsy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dwellsy-well-known.yml
- group: other
  href: https://artifacts.apis.io/dwellsy/hosts/dwellsy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dwellsy-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dwellsy.com/pages/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dwellsy.com/pages/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://blog.iq.dwellsy.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dwellsy
- group: auth
  href: https://artifacts.apis.io/dwellsy/security/dwellsy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dwellsy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dwellsy.com/
coverage:
  checked: '2026-10-28'
  detail: Provider's main site returns a JavaScript shell with no machine‑readable API spec.
  evidence:
  - status: 202
    url: https://dwellsy.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: 'Dwellsy is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: BalanceEntry
  property_count: 3
  slug: dwellsy-balance-entry
- name: CompsPackage
  property_count: 3
  slug: dwellsy-comps-package
jsonld:
- class_count: 3
  name: Dwellsy Context
  property_count: 7
  slug: dwellsy-context
layout: provider
modified: '2026-10-28'
name: Dwellsy
nav: Providers
network: true
overview: 'Dwellsy publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Dwellsy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dwellsy''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Dwellsy Plans Pricing
  plan_count: 4
  slug: dwellsy-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Dwellsy Rate Limits
  slug: dwellsy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Dwellsy API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: dwellsy-rules
scopes:
- name: Dwellsy Scopes
  scope_count: 0
  slug: dwellsy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 33
    catalog_earned: 44.5
    catalog_earned_first_party: 20.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 1.2
    discoverability: 33.9
    operational_transparency: 23.7
  previous_composite: 23.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Dwellsy Authentication
  slug: dwellsy-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Dwellsy Domain Security
  slug: dwellsy-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
skill_count: 1
skills:
- name: dwellsy-dashboard-api
  slug: dwellsy-dashboard-api
slug: dwellsy
tags:
- Company
website: https://dwellsy.com/
---
