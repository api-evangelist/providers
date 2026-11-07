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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/chatsimple-ai/changelog/chatsimple-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/chatsimple-ai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.expertise.ai/security
- group: agent
  href: https://artifacts.apis.io/chatsimple-ai/llms/chatsimple-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chatsimple-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/chatsimple-ai/well-known/chatsimple-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chatsimple-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/chatsimple-ai/hosts/chatsimple-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chatsimple-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/chatsimple-ai/vendors/chatsimple-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chatsimple-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.expertise.ai/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.expertise.ai
- group: auth
  title: ''
  type: Security
  url: https://www.expertise.ai/security
- group: operate
  title: ''
  type: Roadmap
  url: https://www.expertise.ai/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.expertise.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.expertise.ai/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.expertise.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.expertise.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.expertise.ai/skills/client-onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chatsimple.ai/
- group: auth
  href: https://artifacts.apis.io/chatsimple-ai/security/chatsimple-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/chatsimple-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/chatsimple-ai/security/chatsimple-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chatsimple-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chatsimple.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://chatsimple.ai
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Expertise AI provides enterprise AI agents that automate sales and customer‑support conversations. The agents use a company’s knowledge, systems and workflows to answer buyers, book meetings and resolve support requests across chat, voice, video and phone. The service is targeted at enterprises that need high‑volume, multi‑channel conversational automation.
image: https://www.expertise.ai/images/og-image-homepage-agents.jpg
layout: provider
modified: '2026-10-25'
name: Chatsimple
nav: Providers
network: true
overview: 'Chatsimple is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise AI, Customer Service, Multi-Channel, and AI Deployment.


  Chatsimple''s developer surface includes changelog, pricing, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 46.4
    operational_transparency: 26.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chatsimple-ai/chatsimple-ai-2026-11-03T123930.png
security:
- kind: domain-security
  name: Chatsimple Ai Domain Security
  slug: chatsimple-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Chatsimple Ai Trust Center
  slug: chatsimple-ai-trust-center
  summary_line: SOC 2, HIPAA
slug: chatsimple-ai
tags:
- Enterprise AI
- Customer Service
- Multi-Channel
- AI Deployment
website: https://chatsimple.ai
---
