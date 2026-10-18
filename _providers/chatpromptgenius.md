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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chatpromptgenius/refs/heads/main/well-known/chatpromptgenius-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chatpromptgenius-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chatpromptgenius/refs/heads/main/hosts/chatpromptgenius-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chatpromptgenius-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chatpromptgenius/refs/heads/main/vendors/chatpromptgenius-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chatpromptgenius-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chatpromptgenius/refs/heads/main/security/chatpromptgenius-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chatpromptgenius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chatpromptgenius.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://chatpromptgenius.com/how-it-works/
- group: operate
  title: ''
  type: Support
  url: https://chatpromptgenius.com/support/
- group: company
  title: ''
  type: Blog
  url: https://chatpromptgenius.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chatpromptgenius.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chatpromptgenius.com/privacy-policy/
coverage:
  checked: '2026-10-16'
  detail: The site provides no machine‑readable API specification despite having a public website.
  evidence:
  - status: 200
    url: https://chatpromptgenius.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Chat Prompt Genius provides ready‑made AI prompt packs and custom GPTs tailored for local businesses, marketers, and e‑commerce operators. Their marketplace offers one‑time‑purchase prompt collections covering SEO, social media, advertising, content creation, and industry‑specific use cases. Users can instantly download and paste prompts into ChatGPT or other AI chat tools without a subscription, enabling fast deployment of AI‑powered workflows for marketing campaigns, online business growth, and client communication.
layout: provider
modified: '2026-10-16'
name: Chat Prompt Genius
nav: Providers
network: true
overview: 'Chat Prompt Genius is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, PromptMarketplace, Marketing, and E-Commerce.


  Chat Prompt Genius'' developer surface includes getting-started guide, support, engineering blog, and 7 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chatpromptgenius Domain Security
  slug: chatpromptgenius-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chatpromptgenius
tags:
- Company
- Artificial Intelligence
- PromptMarketplace
- Marketing
- E-Commerce
website: https://chatpromptgenius.com/
---
