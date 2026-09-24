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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: 'Chatwik''s publicly consumable surfaces: an llms.txt / llms-full.txt agent-native discovery file and product help documentation. An embeddable JavaScript Widget SDK is loadable from app.chatwik.com (au'
  name: Chatwik
  slug: chatwik
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.chatwik.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chatwik/refs/heads/main/security/chatwik-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chatwik-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chatwik/refs/heads/main/security/chatwik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chatwik-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chatwik/refs/heads/main/security/chatwik-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/chatwik-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chatwik/refs/heads/main/well-known/chatwik-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chatwik-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chatwik/refs/heads/main/well-known/chatwik-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chatwik-security.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://chatwik.com/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://chatwik.com/help-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chatwik.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chatwik.com/privacy-policy
created: '2026-09-15'
description: Modern omnichannel customer communication platform (operated by ZeroFlux Technologies) combining live chat, social media messaging, a multi-agent shared inbox, CRM workspace, and the WikAI autonomous AI support assistant. Built on a Chatwoot-derived application stack, it consolidates Website chat, WhatsApp, Facebook, Instagram, Telegram, SMS, Voice, Email, LINE, TikTok and X into a single shared inbox. Currently exposes an llms.txt / llms-full.txt agent-native discovery file, a served security.txt, and an embeddable JavaScript Widget SDK; a REST/webhook developer API is advertised on the integrations page but is not yet documented (the /docs API Reference link 404s).
layout: provider
modified: '2026-09-15'
name: Chatwik
nav: Providers
network: true
overview: 'Chatwik publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, AI Agents, Chatbots, Live Chat, and Help Desk.


  Chatwik''s developer surface includes pricing and 9 more developer resources.'
plans:
- name: Chatwik Plans Pricing
  plan_count: 3
  slug: chatwik-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Chatwik Rate Limits
  slug: chatwik-rate-limits
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 66.7
    operational_transparency: 10.5
  previous_composite: 25.0
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chatwik Domain Security
  slug: chatwik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chatwik Vulnerability Disclosure
  slug: chatwik-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chatwik
tags:
- Artificial Intelligence
- AI Agents
- Chatbots
- Live Chat
- Help Desk
- Customer Support
- Omnichannel
- Shared Inbox
- CRM
- WhatsApp
- Messaging
website: https://www.chatwik.com
---
