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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tacton/refs/heads/main/llms/tacton-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tacton-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tacton/refs/heads/main/hosts/tacton-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tacton-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tacton.com/legal-information/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://www.tacton.com/about-us/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tacton
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tacton/refs/heads/main/security/tacton-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tacton-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tacton.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tacton.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tacton.com/buyer-engagement-platform/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.tacton.com/cpq-blog/
- group: operate
  title: ''
  type: Support
  url: https://support.tacton.com/
- group: start
  title: ''
  type: Login
  url: https://www.tacton.com/login/
coverage:
  checked: '2026-10-15'
  detail: Tacton provides CPQ software but does not expose a public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.tacton.com/buyer-engagement-platform/pricing/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Tacton provides CPQ (Configure, Price, Quote) software that helps manufacturers and complex‑product sellers streamline their sales processes. Their platform enables engineering‑to‑order, AI‑driven configuration, and seamless integration with ERP and CRM systems, improving buyer experience across industries such as chemical, energy, medical, and industrial equipment. Tacton’s solutions focus on digital transformation, enabling faster quoting, accurate pricing, and better collaboration between commercial and technical teams.
image: https://www.tacton.com/wp-content/uploads/2025/09/tacton-website-video-thumb1.jpg
layout: provider
modified: '2026-10-15'
name: Tacton
nav: Providers
network: true
overview: 'Tacton is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CPQ, Manufacturing, Software-as-a-Service, B2B, and Engineering.


  Tacton''s developer surface includes documentation, pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Tacton Plans Pricing
  plan_count: 0
  slug: tacton-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tacton Domain Security
  slug: tacton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tacton
tags:
- CPQ
- Manufacturing
- Software-as-a-Service
- B2B
- Engineering
- Company
website: https://tacton.com/
---
