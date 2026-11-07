---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  score: 21.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation for Dreambooth Studio platform, covering photobooth features, hardware integration, and platform setup.
  name: Dreambooth API
  slug: dreambooth-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/dreamboothstudio-com/security/dreamboothstudio-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dreamboothstudio-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/dreamboothstudio-com/llms/dreamboothstudio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dreamboothstudio-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dreamboothstudio-com/well-known/dreamboothstudio-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dreamboothstudio-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dreamboothstudio-com/hosts/dreamboothstudio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dreamboothstudio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dreamboothstudio-com/vendors/dreamboothstudio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dreamboothstudio-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://dreamboothstudio.com/api/support/whatsapp
- group: auth
  href: https://artifacts.apis.io/dreamboothstudio-com/security/dreamboothstudio-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dreamboothstudio-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dreamboothstudio-com/security/dreamboothstudio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dreamboothstudio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dreamboothstudio.com/
created: '2026-11-05'
description: Dreambooth is a self‑service photobooth software platform offering integrated cashless payments, custom branding, and photobooth templates. It supports Windows, Web browsers, and Android (beta), with tiered pricing and free trials. The company, PT Mimpi Teknologi Nusantara, provides analytics dashboards, cloud storage, and multi‑format output for photo strips, GIFs, and videos, serving businesses worldwide.
image: https://dreamboothstudio.com/assets/images/thumbnail-en.png
layout: provider
modified: '2026-11-05'
name: Dreambooth
nav: Providers
network: true
overview: 'Dreambooth is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Photobooth, Software-as-a-Service, Payments, Branding, and Analytics.


  Dreambooth''s developer surface includes support and 8 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 16.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dreamboothstudio Com Domain Security
  slug: dreamboothstudio-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dreamboothstudio Com Vulnerability Disclosure
  slug: dreamboothstudio-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: dreamboothstudio-com
tags:
- Photobooth
- Software-as-a-Service
- Payments
- Branding
- Analytics
website: https://dreamboothstudio.com/
---
