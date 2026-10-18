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
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mitek-systems/refs/heads/main/plans/mitek-systems-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mitek-systems-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mitek-systems/refs/heads/main/llms/mitek-systems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mitek-systems-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mitek-systems/refs/heads/main/hosts/mitek-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mitek-systems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mitek-systems/refs/heads/main/vendors/mitek-systems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mitek-systems-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.miteksystems.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.miteksystems.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.miteksystems.com/products/biometric-authentication/plans
- group: company
  title: ''
  type: Newsroom
  url: https://www.miteksystems.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mitek-systems/refs/heads/main/security/mitek-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mitek-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.miteksystems.com
- group: company
  title: ''
  type: Blog
  url: https://www.miteksystems.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.miteksystems.com/support
- group: docs
  title: ''
  type: Documentation
  url: https://www.miteksystems.com/support
coverage:
  checked: '2026-10-14'
  detail: Documentation site renders via JavaScript and provides no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.miteksystems.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Mitek Systems provides digital identity verification and fraud detection solutions, offering products such as mobile check deposit, biometric authentication, and AI‑driven fraud defense. The company serves financial institutions, enterprises, and developers with APIs for identity verification, document liveness, and compliance workflows, enabling secure onboarding and transaction security across channels.
image: https://www.miteksystems.com/files/styles/rectangle_xl/public/img/misc/mitek-social-sharing-image-2026-en.jpg?itok=9OSwz-1D
layout: provider
modified: '2026-10-14'
name: Mitek Systems
nav: Providers
network: true
overview: 'Mitek Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IdentityVerification, FraudDetection, and Financial Services.


  Mitek Systems'' developer surface includes pricing, engineering blog, support, documentation, and 9 more developer resources.'
plans:
- name: Mitek Systems Plans Pricing
  plan_count: 2
  slug: mitek-systems-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mitek Systems Domain Security
  slug: mitek-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mitek-systems
tags:
- Company
- IdentityVerification
- FraudDetection
- Financial Services
website: https://www.miteksystems.com
---
