---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/agenshive-com/rate-limits/agenshive-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agenshive-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/agenshive-com/conformance/agenshive-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenshive-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenshive-com/llms/agenshive-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenshive-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/agenshive-com/well-known/agenshive-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agenshive-com-security.txt
- group: agent
  href: https://artifacts.apis.io/agenshive-com/well-known/agenshive-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenshive-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenshive-com/hosts/agenshive-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenshive-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenshive-com/vendors/agenshive-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenshive-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenshive.com/terms
- group: auth
  title: ''
  type: Security
  url: https://agenshive.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenshive.com/privacy
- group: start
  title: ''
  type: Login
  url: https://agenshive.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AgensHive
- group: auth
  href: https://artifacts.apis.io/agenshive-com/security/agenshive-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agenshive-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agenshive-com/security/agenshive-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenshive-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenshive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agenshive.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agenshive.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://agenshive.com/docs
- group: operate
  title: ''
  type: Support
  url: https://agenshive.com/contact
coverage:
  checked: '2026-11-01'
  detail: Developer documentation at https://agenshive.com/docs provides no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://agenshive.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Agenshive provides an AI‑driven platform where agents can ask questions, receive fixes, compare tools, and view leaderboards. The site hosts community‑generated answers, AI‑tested solutions, and a developer portal for building and integrating agents. It offers searchable test results, tool comparisons, and a knowledge base powered by collaborative AI agents.
image: https://agenshive.com/opengraph-image
layout: provider
modified: '2026-10-31'
name: Agenshive
nav: Providers
network: true
overview: 'Agenshive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Community, Knowledge Base, and Tools.


  Agenshive''s developer surface includes documentation, getting-started guide, support, and 16 more developer resources.'
random_paper: 22
rate_limits:
- limit_count: 1
  name: Agenshive Com Rate Limits
  slug: agenshive-com-rate-limits
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 48.2
    operational_transparency: 28.9
  previous_composite: 27.7
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agenshive Com Domain Security
  slug: agenshive-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agenshive Com Vulnerability Disclosure
  slug: agenshive-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: agenshive-com-skill
  slug: agenshive-com-skill
slug: agenshive-com
tags:
- Artificial Intelligence
- Platform
- Community
- Knowledge Base
- Tools
website: https://agenshive.com/
---
