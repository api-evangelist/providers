---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for BoomerangAI platform providing referral agent capabilities
  name: BoomerangAI API
  slug: boomerangai-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/boomerangai/refs/heads/main/plans/boomerangai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boomerangai-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.getboomerang.ai/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boomerangai/refs/heads/main/llms/boomerangai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boomerangai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boomerangai/refs/heads/main/hosts/boomerangai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boomerangai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boomerangai/refs/heads/main/vendors/boomerangai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boomerangai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getboomerang.ai/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://www.getboomerang.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getboomerang.ai/privacy-notice
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getboomerang.ai/pricing
- group: other
  title: ''
  type: Leadership
  url: https://www.getboomerang.ai/scaling-pipeline-for-hypergrowth/team
- group: company
  title: ''
  type: Blog
  url: https://www.getboomerang.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getboomerang.ai/salesforce/mZnVrwP3Sdhcx3Vm83YXHz/step-6-setup-boomerang---contacts-details-to-contact-layout/1VeasJGzoB3t8fc53fAhom
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getboomerang.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boomerangai/refs/heads/main/security/boomerangai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/boomerangai-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boomerangai/refs/heads/main/security/boomerangai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boomerangai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getboomerang.ai/
coverage:
  checked: '2026-10-02'
  detail: Docs are served as a JavaScript-rendered single-page app, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.getboomerang.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: BoomerangAI provides an AI‑powered referral agent that helps sales teams get warm introductions. By leveraging conversational AI, it surfaces relevant contacts, tracks champion relationships, and automates pipeline leak assessments, turning cold outreach into data‑driven engagements. The platform offers use‑cases like Path to Power, Champion Tracking, and Buying‑Group Intelligence, delivering measurable revenue impact for B2B sellers.
image: https://cdn.prod.website-files.com/64901216dea3f5805b4f783b/6aac648c0fc0e97d67a7f03e_og-home.png
layout: provider
modified: '2026-10-02'
name: BoomerangAI
nav: Providers
network: true
overview: 'BoomerangAI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Sales, B2B, Referrals, and Automation.


  BoomerangAI''s developer surface includes pricing, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
plans:
- name: Boomerangai Plans Pricing
  plan_count: 4
  slug: boomerangai-plans-pricing
random_paper: 12
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boomerangai Domain Security
  slug: boomerangai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Boomerangai Trust Center
  slug: boomerangai-trust-center
  summary_line: SOC 2, GDPR
slug: boomerangai
tags:
- Artificial Intelligence
- Sales
- B2B
- Referrals
- Automation
website: https://www.getboomerang.ai/
---
