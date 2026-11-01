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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/crowdcast/plans/crowdcast-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crowdcast-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/crowdcast/security/crowdcast-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/crowdcast-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/crowdcast/llms/crowdcast-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crowdcast-llms.txt
- group: auth
  href: https://artifacts.apis.io/crowdcast/well-known/crowdcast-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crowdcast-security.txt
- group: auth
  href: https://artifacts.apis.io/crowdcast/well-known/crowdcast-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crowdcast-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/crowdcast/well-known/crowdcast-crowdcast-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crowdcast-crowdcast-security.txt
- group: agent
  href: https://artifacts.apis.io/crowdcast/well-known/crowdcast-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crowdcast-well-known.yml
- group: other
  href: https://artifacts.apis.io/crowdcast/hosts/crowdcast-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowdcast-hosts.yml
- group: other
  href: https://artifacts.apis.io/crowdcast/vendors/crowdcast-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crowdcast-vendors.yml
- group: auth
  href: https://artifacts.apis.io/crowdcast/security/crowdcast-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crowdcast-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crowdcast/security/crowdcast-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowdcast-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crowdcast.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.crowdcast.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crowdcast.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.crowdcast.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.crowdcast.io/sign-up
- group: company
  title: ''
  type: Blog
  url: https://www.crowdcast.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crowdcast.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crowdcast.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crowdcast.io/privacy-policy
coverage:
  checked: '2026-10-27'
  detail: Docs site loads via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://docs.crowdcast.io/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Crowdcast is a live video platform that enables creators, businesses, and communities to host webinars, workshops, and virtual events. It offers integrated tools for audience interaction, ticketing, and analytics, supporting millions of attendees worldwide. The service provides a seamless experience for both presenters and participants, with features like live chat, Q&A, polls, and customizable branding.
image: https://crowdcast.io/og/home.png
layout: provider
modified: '2026-10-27'
name: Crowdcast
nav: Providers
network: true
overview: 'Crowdcast is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Video, Live-Streaming, Webinars, Community, and SaaS.


  Crowdcast''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Crowdcast Plans Pricing
  plan_count: 5
  slug: crowdcast-plans-pricing
random_paper: 10
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
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
  name: Crowdcast Domain Security
  slug: crowdcast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crowdcast Vulnerability Disclosure
  slug: crowdcast-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crowdcast
tags:
- Video
- Live-Streaming
- Webinars
- Community
- SaaS
website: https://www.crowdcast.io/
---
