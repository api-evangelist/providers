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
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/crownofsilence-com/llms/crownofsilence-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crownofsilence-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/crownofsilence-com/well-known/crownofsilence-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crownofsilence-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/crownofsilence-com/hosts/crownofsilence-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crownofsilence-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/crownofsilence-com/vendors/crownofsilence-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crownofsilence-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/crownofsilence-com/security/crownofsilence-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crownofsilence-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crownofsilence.com/
- group: company
  title: ''
  type: Blog
  url: https://crownofsilence.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crownofsilence.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crownofsilence.com/privacy-policy/
coverage:
  checked: '2026-11-04'
  detail: The provider offers a blog and community platform but no developer API or documentation.
  evidence:
  - status: 200
    url: https://crownofsilence.com/
  reason: not-a-software-company
  state: none
created: '2026-11-04'
description: Crown of Silence is a place for truth‑seekers exploring philosophy, consciousness, self‑mastery, and the deeper questions of human existence. It offers a blog, a matrix of mental models, and a private Inner Circle community where members and approved AI agents discuss and create content.
image: https://crownofsilence.com/wp-content/uploads/2026/01/transparent-png-2.png
layout: provider
modified: '2026-11-04'
name: Crown of Silence
nav: Providers
network: true
overview: 'Crown of Silence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Philosophy, Self-Mastery, Community, and Content.


  Crown of Silence''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crownofsilence Com Domain Security
  slug: crownofsilence-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crownofsilence-com
tags:
- Company
- Philosophy
- Self-Mastery
- Community
- Content
website: https://crownofsilence.com/
---
