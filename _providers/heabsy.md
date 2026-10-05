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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/heabsy/refs/heads/main/plans/heabsy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/heabsy-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://heabsy.com/compliance
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/heabsy/refs/heads/main/overlays/heabsy-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/heabsy-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/heabsy/refs/heads/main/llms/heabsy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/heabsy-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/heabsy/refs/heads/main/well-known/heabsy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/heabsy-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/heabsy/refs/heads/main/hosts/heabsy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/heabsy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/heabsy/refs/heads/main/vendors/heabsy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/heabsy-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://heabsy.com/products/security
- group: company
  title: ''
  type: Blog
  url: https://heabsy.com/de/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/heabsy/refs/heads/main/security/heabsy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/heabsy-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/heabsy/refs/heads/main/security/heabsy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heabsy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://heabsy.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.heabsy.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://heabsy.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://heabsy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://heabsy.com/privacy
created: '2026-10-02'
description: Heabsy provides an OpenAI‑compatible inference API hosted in the European Economic Area, targeting regulated industries such as finance, insurance, and manufacturing. The platform offers sovereign AI models with zero data retention, compliance with EU AI regulations, and detailed security certifications. It includes a developer console for key management, pricing tiers, and extensive documentation for integration.
image: https://heabsy.com/og/index.png
layout: provider
modified: '2026-10-02'
name: Heabsy
nav: Providers
network: true
overview: 'Heabsy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Inference, OpenAI-Compatible, EU-regulated, and Software-as-a-Service.


  Heabsy''s developer surface includes engineering blog, documentation, pricing, and 13 more developer resources.'
plans:
- name: Heabsy Plans Pricing
  plan_count: 3
  slug: heabsy-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Heabsy Domain Security
  slug: heabsy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Heabsy Trust Center
  slug: heabsy-trust-center
  summary_line: SOC 2, ISO 27001
slug: heabsy
tags:
- Artificial Intelligence
- Inference
- OpenAI-Compatible
- EU-regulated
- Software-as-a-Service
website: https://heabsy.com
---
