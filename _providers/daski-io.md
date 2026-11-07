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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Daski platform providing service outcomes
  name: Daski API
  slug: daski-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/daski-io/conformance/daski-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/daski-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/daski-io/llms/daski-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/daski-io-llms.txt
- group: other
  href: https://artifacts.apis.io/daski-io/hosts/daski-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daski-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/daski-io/vendors/daski-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daski-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://daski.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daski.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/daski-io
- group: auth
  href: https://artifacts.apis.io/daski-io/security/daski-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daski-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daski.io/
created: '2026-11-04'
description: Daski is a curated procurement marketplace for AI agents, offering services to discover, evaluate, buy, and manage domains, mailboxes, and company formation. It connects AI agents with essential digital infrastructure, providing a seamless platform for acquiring and managing online assets.
image: https://daski.io/assets/social/daski-card.png
layout: provider
modified: '2026-11-04'
name: Daski
nav: Providers
network: true
overview: Daski is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, AI Agents, Mailbox Services, and Business Formation.
random_paper: 17
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Daski Io Domain Security
  slug: daski-io-domain-security
  summary_line: TLSv1.3
slug: daski-io
tags:
- Marketplace
- AI Agents
- Mailbox Services
- Business Formation
website: https://daski.io/
---
