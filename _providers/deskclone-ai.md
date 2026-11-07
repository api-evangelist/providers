---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Ask your DeskClone agent, manage its knowledge, read conversations and get notified when conversations start or are handed to a person.
  name: DeskClone API
  slug: deskclone-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/deskclone-ai/plans/deskclone-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deskclone-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/deskclone-ai/changelog/deskclone-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/deskclone-ai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://deskclone.ai/compliance
- group: design
  href: https://artifacts.apis.io/deskclone-ai/conformance/deskclone-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deskclone-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deskclone-ai/llms/deskclone-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deskclone-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/deskclone-ai/hosts/deskclone-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deskclone-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/deskclone-ai/vendors/deskclone-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deskclone-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deskclone.ai/terms
- group: auth
  title: ''
  type: Security
  url: https://deskclone.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deskclone.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://deskclone.ai/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.deskclone.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://deskclone.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.deskclone.ai/agent-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deskclone.ai/
- group: auth
  href: https://artifacts.apis.io/deskclone-ai/security/deskclone-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/deskclone-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/deskclone-ai/security/deskclone-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deskclone-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deskclone-ai/security/deskclone-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deskclone-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deskclone.ai/
created: '2026-11-05'
description: DeskClone AI is a SaaS platform that enables businesses to build AI-powered support agents that clone the expertise of their best employees. The agents learn from product documentation, internal knowledge bases, and past interactions to autonomously resolve customer issues, handle order lookups, refunds, and account fixes with flat monthly pricing and no per‑ticket fees. It offers a self‑learning, end‑to‑end solution for scalable customer support.
image: https://deskclone.ai/og-image.jpg
layout: provider
modified: '2026-11-05'
name: DeskClone AI
nav: Providers
network: true
overview: 'DeskClone AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Software-as-a-Service, Customer Service, Automation, and Platform.


  DeskClone AI''s developer surface includes changelog, pricing, engineering blog, getting-started guide, documentation, and 14 more developer resources.'
plans:
- name: Deskclone Ai Plans Pricing
  plan_count: 4
  slug: deskclone-ai-plans-pricing
random_paper: 23
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deskclone Ai Domain Security
  slug: deskclone-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deskclone Ai Vulnerability Disclosure
  slug: deskclone-ai-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Deskclone Ai Trust Center
  slug: deskclone-ai-trust-center
  summary_line: SOC 2, GDPR
slug: deskclone-ai
tags:
- Artificial Intelligence
- Software-as-a-Service
- Customer Service
- Automation
- Platform
website: https://deskclone.ai/
---
