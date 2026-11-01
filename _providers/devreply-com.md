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
    dynamic_client_registration: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: DevReply provides a native in‑app chat solution that lets users message developers directly from iOS, Android, or web apps.
  name: DevReply API
  slug: devreply-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/devreply-com/llms/devreply-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/devreply-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/devreply-com/well-known/devreply-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/devreply-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/devreply-com/hosts/devreply-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/devreply-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/devreply-com/vendors/devreply-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/devreply-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/devreply-com/security/devreply-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/devreply-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://devreply.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://devreply.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://devreply.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devreply.com/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://devreply.com/support-chat-swiftui.html
coverage:
  checked: '2026-10-30'
  detail: MCP endpoint https://api.devreply.com/mcp returns 401 Unauthorized, indicating the API is behind authentication.
  evidence:
  - status: 401
    url: https://api.devreply.com/mcp
  reason: auth-required
  state: gated
created: '2026-10-30'
description: DevReply provides a native in‑app chat solution that lets users message developers directly from iOS, Android, or web apps. Messages are delivered to a developer inbox with device and version metadata, enabling rapid response to user feedback and preventing negative reviews. The service is free for manual handling and offers a paid agent‑assist tier. The company’s API enables integration of the chat widget into applications via a simple JavaScript snippet or native SDKs, and the MCP endpoint https://api.devreply.com/mcp allows tool integration. DevReply aims to improve developer‑user communication and app reputation.
image: https://devreply.com/assets/og.png?v=3
layout: provider
modified: '2026-10-30'
name: devreply-com
nav: Providers
network: true
overview: 'devreply-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chat, Customer Support, Mobile, and Web.


  devreply-com''s developer surface includes pricing, support, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Devreply Com Domain Security
  slug: devreply-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: devreply-com
tags:
- Company
- Chat
- Customer Support
- Mobile
- Web
- Developer Tools
website: https://devreply.com/
---
