---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/shuttleai/security/shuttleai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/shuttleai-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/shuttleai/llms/shuttleai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shuttleai-llms.txt
- group: other
  href: https://artifacts.apis.io/shuttleai/a2a/shuttleai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/shuttleai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/shuttleai/well-known/shuttleai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shuttleai-security.txt
- group: auth
  href: https://artifacts.apis.io/shuttleai/well-known/shuttleai-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shuttleai-api-security.txt
- group: agent
  href: https://artifacts.apis.io/shuttleai/well-known/shuttleai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shuttleai-well-known.yml
- group: other
  href: https://artifacts.apis.io/shuttleai/hosts/shuttleai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shuttleai-hosts.yml
- group: other
  href: https://artifacts.apis.io/shuttleai/vendors/shuttleai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shuttleai-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.shuttleai.com/pricing/plans
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shuttleai.com/getting-started/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shuttleai.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shuttleai.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/shuttleai/security/shuttleai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/shuttleai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/shuttleai/security/shuttleai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shuttleai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shuttleai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shuttleai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shuttleai.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shuttleai
- group: other
  title: ''
  type: SocialMedia
  url: https://discord.gg/Vgk26KKuJv
- group: other
  title: ''
  type: SocialMedia
  url: https://www.linkedin.com/company/shuttleai
- group: other
  title: ''
  type: SocialMedia
  url: https://x.com/shuttleai_com
- group: other
  title: ''
  type: SocialMedia
  url: https://www.tiktok.com/@shuttleai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://docs.shuttleai.com/mcp
  - status: 401
    url: https://api.shuttleai.com/mcp
  - status: 200
    url: https://shuttleai.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: ShuttleAI is an artificial intelligence company advancing the systems and ideas that shape what comes next. It builds AI infrastructure, developer tools, and intelligent products that make advanced models easier to access, integrate, and use, helping developers and enterprises accelerate AI adoption.
layout: provider
modified: '2026-10-26'
name: ShuttleAI
nav: Providers
network: true
overview: 'ShuttleAI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Infrastructure, DeveloperTools, Products, and Company.


  ShuttleAI''s developer surface includes pricing, getting-started guide, documentation, API reference, and 18 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Shuttleai Domain Security
  slug: shuttleai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Shuttleai Vulnerability Disclosure
  slug: shuttleai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: shuttleai
tags:
- AI
- Infrastructure
- DeveloperTools
- Products
- Company
website: https://shuttleai.com/
---
