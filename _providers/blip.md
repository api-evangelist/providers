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
api_count: 1
apis:
- description: Blip conversational AI platform API documentation
  name: Blip API
  slug: blip-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.blip.ai/en/trust-center/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blip/refs/heads/main/llms/blip-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blip-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blip/refs/heads/main/well-known/blip-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/blip-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blip/refs/heads/main/well-known/blip-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blip-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blip/refs/heads/main/hosts/blip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blip-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blip/refs/heads/main/vendors/blip-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blip-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.blip.ai/hc/pt-br
- group: operate
  title: ''
  type: StatusPage
  url: https://status.blip.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.blip.ai/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.whatsapp.com/send/?phone=553133496201&text=Ol%C3%A1%2C+Blip!&type=phone_number&app_absent=0
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blip/refs/heads/main/security/blip-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/blip-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blip/refs/heads/main/security/blip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blip.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.blip.ai/en/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blip.ai/en/pricing
- group: other
  title: ''
  type: Platform
  url: https://www.blip.ai/en/platform
- group: operate
  title: ''
  type: Contact
  url: https://www.blip.ai/en/contact-us
coverage:
  detail: Documentation pages return HTML shells and no OpenAPI spec is available at common endpoints.
  evidence:
  - status: 404
    url: https://api.blip.ai/openapi.json
  - status: 404
    url: https://docs.blip.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Blip provides conversational AI platforms that enable businesses to create intelligent, end‑to‑end conversational journeys. Their solutions turn interactions into measurable results across industries such as utilities, retail, banking, education, and automotive. Blip’s platform offers tools for contact, platform integration, demos, case studies, and a trust center, emphasizing data privacy and security. The company focuses on driving sales, customer retention, and business outcomes through AI‑powered conversations.
image: https://www.blip.ai/wp-content/uploads/2023/06/Blip_ThumbGeral_PT-1.png
layout: provider
modified: '2026-10-14'
name: Blip
nav: Providers
network: true
overview: 'Blip is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Conversational AI, Business Automation, Customer Engagement, Platform, and Company.


  Blip''s developer surface includes support, engineering blog, documentation, pricing, and 13 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blip Domain Security
  slug: blip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Blip Trust Center
  slug: blip-trust-center
  summary_line: ISO 27001
slug: blip
tags:
- Conversational AI
- Business Automation
- Customer Engagement
- Platform
- Company
website: https://www.blip.ai
---
