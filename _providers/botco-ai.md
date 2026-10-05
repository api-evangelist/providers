---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Botco.ai provides generative AI chatbot solutions with an API documented on their website.
  name: Botco.ai API
  slug: botco-ai-api
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/botco-ai/refs/heads/main/changelog/botco-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/botco-ai-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/botco-ai/refs/heads/main/well-known/botco-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botco-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/botco-ai/refs/heads/main/hosts/botco-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botco-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/botco-ai/refs/heads/main/vendors/botco-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botco-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://botco.ai/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://help.botco.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botco.ai/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://botco.ai/press/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.botco.ai/release-notes
- group: company
  title: ''
  type: Blog
  url: https://botco.ai/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.botco.ai/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.botco.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/botco-ai/refs/heads/main/security/botco-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botco-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botco.ai/
coverage:
  checked: '2026-10-03'
  detail: API endpoints return 401 Unauthorized, indicating authentication gating.
  evidence:
  - status: 401
    url: https://api.botco.ai
  reason: sales-gate
  state: gated
created: '2026-10-03'
description: Botco.ai provides generative AI chatbot solutions that augment workforce productivity across industries such as healthcare, city services, and pharmaceuticals. Their platform enables organizations to automate compliance, streamline navigation, and scale operations with AI agents, offering customizable chat experiences, integrations, and analytics. Founded to empower teams with conversational AI, Botco.ai delivers enterprise-grade chatbot technology and consulting services to drive efficiency and innovation.
image: https://7f819ccc.delivery.rocketcdn.me/wp-content/uploads/botco_hero_phone_hand_desktop_2x-scaled.jpg
layout: provider
modified: '2026-10-03'
name: Botco.ai
nav: Providers
network: true
overview: 'Botco.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Chatbots, Healthcare, Pharmaceuticals, and Government.


  Botco.ai''s developer surface includes changelog, support, engineering blog, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Botco Ai Domain Security
  slug: botco-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: botco-ai
tags:
- AI Agents
- Chatbots
- Healthcare
- Pharmaceuticals
- Government
- Compliance
- Software-as-a-Service
website: https://botco.ai/
---
