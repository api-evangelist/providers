---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Utilityhouse Xyz Agentic Access
  operation_count: 7
  slug: utilityhouse-xyz-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.utilityhouse.xyz
  baseurl_source: declared
  description: The Grants API from utilityhouse-xyz — 3 operation(s) for grants.
  name: utilityhouse-xyz Grants API
  slug: utilityhouse-xyz-grants-api
- baseURL: https://api.utilityhouse.xyz
  baseurl_source: declared
  description: The Woo API from utilityhouse-xyz — 2 operation(s) for woo.
  name: utilityhouse-xyz Woo API
  slug: utilityhouse-xyz-woo-api
- baseURL: https://api.utilityhouse.xyz
  baseurl_source: declared
  description: The Wp Updates API from utilityhouse-xyz — 2 operation(s) for wp updates.
  name: utilityhouse-xyz Wp Updates API
  slug: utilityhouse-xyz-wp-updates-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/utilityhouse-xyz/agentic-access/utilityhouse-xyz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/utilityhouse-xyz-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/utilityhouse-xyz/rules/utilityhouse-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/utilityhouse-xyz-rules.yml
- group: agent
  href: https://artifacts.apis.io/utilityhouse-xyz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/utilityhouse-xyz/errors/utilityhouse-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/utilityhouse-xyz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/utilityhouse-xyz/conformance/utilityhouse-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/utilityhouse-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/utilityhouse-xyz/llms/utilityhouse-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/utilityhouse-xyz-llms.txt
- group: auth
  href: https://artifacts.apis.io/utilityhouse-xyz/well-known/utilityhouse-xyz-updates-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/utilityhouse-xyz-updates-security.txt
- group: agent
  href: https://artifacts.apis.io/utilityhouse-xyz/well-known/utilityhouse-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/utilityhouse-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/utilityhouse-xyz/hosts/utilityhouse-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/utilityhouse-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/utilityhouse-xyz/vendors/utilityhouse-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/utilityhouse-xyz-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://app.utilityhouse.xyz/support
- group: start
  title: ''
  type: SignUp
  url: https://app.utilityhouse.xyz/signup
- group: auth
  title: ''
  type: Security
  url: https://app.utilityhouse.xyz/security
- group: auth
  href: https://artifacts.apis.io/utilityhouse-xyz/security/utilityhouse-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/utilityhouse-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://utilityhouse.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://utilityhouse.xyz/company/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://utilityhouse.xyz/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://utilityhouse.xyz/company/terms
- group: operate
  title: ''
  type: Contact
  url: https://utilityhouse.xyz/company/contact
created: '2026-10-29'
description: UtilityHouse is an independent personal software project founded by Jeonguk Shin in Seoul, South Korea, on July 1, 2026. It builds focused tools for grant research, WordPress operations, and WooCommerce release readiness, providing clear evidence and bounded decision support. The project emphasizes transparency, evidence‑based workflows, and leaving final decisions to users.
layout: provider
modified: '2026-10-29'
name: utilityhouse-xyz
nav: Providers
network: true
overview: 'utilityhouse-xyz publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Grants API, Woo API, and Wp Updates API. Tagged areas include Company, Software, Grants, WordPress, and WooCommerce.


  The utilityhouse-xyz catalog on APIs.io includes 1 Spectral governance ruleset.


  utilityhouse-xyz''s developer surface includes support, signup flow, documentation, and 16 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: utilityhouse-xyz API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: utilityhouse-xyz-rules
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 39.8
    developer_ergonomics: 8.9
    discoverability: 69.6
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/utilityhouse-xyz/utilityhouse-xyz-2026-11-03T145549.png
security:
- kind: domain-security
  name: Utilityhouse Xyz Domain Security
  slug: utilityhouse-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: utilityhouse-xyz-federal-grant-research
  slug: utilityhouse-xyz-federal-grant-research
slug: utilityhouse-xyz
tags:
- Company
- Software
- Grants
- WordPress
- WooCommerce
website: https://utilityhouse.xyz/
---
