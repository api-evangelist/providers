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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API documentation hosted on Notion, but no machine-readable spec discovered.
  name: Backflip AI API
  slug: backflip-ai-api
artifact_total: 4
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/backflip-ai/refs/heads/main/well-known/backflip-ai-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/backflip-ai-clarity-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/backflip-ai/refs/heads/main/vendors/backflip-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backflip-ai-vendors.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/backflip-ai/refs/heads/main/plans/backflip-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/backflip-ai-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/backflip-ai/refs/heads/main/well-known/backflip-ai-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/backflip-ai-www-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/backflip-ai/refs/heads/main/well-known/backflip-ai-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/backflip-ai-docs-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/backflip-ai/refs/heads/main/well-known/backflip-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/backflip-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/backflip-ai/refs/heads/main/hosts/backflip-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backflip-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.backflip.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.backflip.ai/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.backflip.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.backflip.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.backflip.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/backflip-ai/refs/heads/main/security/backflip-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/backflip-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/backflip-ai/refs/heads/main/security/backflip-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backflip-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.backflip.ai/
coverage:
  checked: 2026-09-27
  detail: Documentation at https://docs.backflip.ai/ is a Notion page rendered via JavaScript, providing no machine-readable spec.
  evidence:
  - status: 200
    url: https://docs.backflip.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Backflip AI provides an AI copilot for 3D design, enabling users to create parametric CAD models with full feature trees directly in their favorite CAD packages. The platform aims to lower the steep learning curve of traditional CAD tools by offering a foundation model that generates editable designs, supporting rapid prototyping and engineering workflows for creators and professionals alike.
image: https://framerusercontent.com/images/KNEZi754kT1xbGEw12mNxFWRlU.png
layout: provider
modified: '2026-09-27'
name: Backflip Ai
nav: Providers
network: true
overview: 'Backflip Ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, CAD, 3D Design, Automation, and Platform.


  Backflip Ai''s developer surface includes pricing, engineering blog, documentation, and 13 more developer resources.'
plans:
- name: Backflip Ai Plans Pricing
  plan_count: 4
  slug: backflip-ai-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Backflip Ai Domain Security
  slug: backflip-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Backflip Ai Vulnerability Disclosure
  slug: backflip-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: backflip-ai
tags:
- Artificial Intelligence
- CAD
- 3D Design
- Automation
- Platform
website: https://www.backflip.ai/
---
