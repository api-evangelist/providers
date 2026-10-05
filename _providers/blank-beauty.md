---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blank-beauty/refs/heads/main/llms/blank-beauty-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blank-beauty-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blank-beauty/refs/heads/main/well-known/blank-beauty-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blank-beauty-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blank-beauty/refs/heads/main/hosts/blank-beauty-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blank-beauty-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blank-beauty/refs/heads/main/vendors/blank-beauty-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blank-beauty-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blank-beauty/refs/heads/main/security/blank-beauty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blank-beauty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blankbeauty.com/
- group: company
  title: ''
  type: Blog
  url: https://blankbeauty.com/blogs/articles/about-us-blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blankbeauty.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blankbeauty.com/policies/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://blankbeauty.com/pages/contact
- group: company
  title: ''
  type: AboutUs
  url: https://blankbeauty.com/pages/about-us
coverage:
  checked: '2026-09-29'
  detail: The provider's site serves only JavaScript‑rendered pages with no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://blankbeauty.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: Blank Beauty is a direct-to-consumer nail polish brand offering cruelty‑free, vegan, and customizable nail products. Founded to provide high‑quality, affordable polish with a focus on sustainability, the company operates an online storefront, a custom‑color creation tool, and a subscription service. It serves a global customer base through its e‑commerce site and social media channels, emphasizing community engagement and innovative product launches.
image: http://blankbeauty.com/cdn/shop/files/Logo.png?v=1663750874
layout: provider
modified: '2026-09-29'
name: Blank Beauty
nav: Providers
network: true
overview: 'Blank Beauty is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beauty, NailPolish, E-Commerce, and Vegan.


  Blank Beauty''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blank Beauty Domain Security
  slug: blank-beauty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blank-beauty
tags:
- Company
- Beauty
- NailPolish
- E-Commerce
- Vegan
website: https://blankbeauty.com/
---
