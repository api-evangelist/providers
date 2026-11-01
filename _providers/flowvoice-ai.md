---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/flowvoice-ai/plans/flowvoice-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flowvoice-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/flowvoice-ai/llms/flowvoice-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flowvoice-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/flowvoice-ai/well-known/flowvoice-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flowvoice-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/flowvoice-ai/hosts/flowvoice-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flowvoice-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/flowvoice-ai/vendors/flowvoice-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flowvoice-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wisprflow.ai/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://wisprflow.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wisprflow.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://wisprflow.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://wisprflow.ai/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wisprflow.ai/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://wisprflow.ai/whats-new
- group: company
  title: ''
  type: Blog
  url: https://wisprflow.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wisprflow.ai/collections/2654500357-getting_started-1
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wisprflow.ai/
- group: auth
  href: https://artifacts.apis.io/flowvoice-ai/security/flowvoice-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flowvoice-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wisprflow.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://docs.wisprflow.ai/mcp
  - status: 200
    url: https://flowvoice.ai
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Wispr Ai, operating as Flow, provides a voice‑to‑text dictation platform that leverages AI to capture spoken words into editable text in real time. The service targets professionals, students, and developers needing fast, accurate transcription for notes, documentation, and communication. Features include multi‑language support, custom vocabularies, real‑time editing, and integration hooks for third‑party apps. Backed by 8vc, Wispr Ai aims to streamline workflow productivity through seamless voice interaction.
image: https://cdn.prod.website-files.com/682f84b3838c89f8ff7667db/6a724a4fff322698a57a7d97_dictation-og%20(1).jpg
layout: provider
modified: '2026-10-21'
name: Wispr Ai
nav: Providers
network: true
overview: 'Wispr Ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Voice-to-Text, AI, Productivity, and Transcription.


  Wispr Ai''s developer surface includes support, pricing, changelog, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
plans:
- name: Flowvoice Ai Plans Pricing
  plan_count: 7
  slug: flowvoice-ai-plans-pricing
random_paper: 21
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Flowvoice Ai Domain Security
  slug: flowvoice-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: flowvoice-ai
tags:
- Company
- Voice-to-Text
- AI
- Productivity
- Transcription
website: https://wisprflow.ai
---
