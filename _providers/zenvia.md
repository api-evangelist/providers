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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zenvia/refs/heads/main/llms/zenvia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zenvia-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zenvia/refs/heads/main/hosts/zenvia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zenvia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zenvia/refs/heads/main/vendors/zenvia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zenvia-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zenvia/refs/heads/main/packages/zenvia-packages.yml
  title: ''
  type: SDKs
  url: packages/zenvia-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zenvia/refs/heads/main/packages/zenvia-packages.yml
  title: ''
  type: Packages
  url: packages/zenvia-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.zenvia.com/
- group: operate
  title: ''
  type: Support
  url: https://support.zenvia.com/Account/Login?ReturnUrl=%2f
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zenvia.com/
- group: company
  title: ''
  type: Blog
  url: https://zenvia.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenvia
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zenvia/refs/heads/main/security/zenvia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zenvia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zenvia.com
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine-readable contract was found on the API host.
  evidence:
  - status: 404
    url: https://api.zenvia.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Zenvia provides a cloud communications platform that enables businesses to engage customers through messaging, voice, and chatbot solutions powered by AI. Their suite includes WhatsApp, SMS, voice calls, and omnichannel automation, offering APIs for CX, marketing, and support. Founded in Brazil, Zenvia serves global enterprises with scalable, secure, and programmable communication services.
image: https://zenvia.com/wp-content/uploads/2022/12/zenvia.jpg
layout: provider
modified: '2026-10-14'
name: Zenvia
nav: Providers
network: true
overview: 'Zenvia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Cloud, WhatsApp, and Customer experience.


  Zenvia''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 46.4
    operational_transparency: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zenvia Domain Security
  slug: zenvia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: zenvia
tags:
- Customer Cloud
- WhatsApp
- Customer experience
website: https://www.zenvia.com
---
