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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bizay/refs/heads/main/hosts/bizay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bizay-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bizay/refs/heads/main/vendors/bizay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bizay-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://us.bizay.com/en-us/Home/TermsAndConditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://us.bizay.com/en-us/Home/PrivacyPolicy
- group: start
  title: ''
  type: Login
  url: https://us.bizay.com/en-us/Account/Login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bizay/refs/heads/main/security/bizay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bizay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://us.bizay.com/en-us
coverage:
  checked: '2026-09-29'
  detail: The Bizay website provides no machine‑readable API specification despite having a public site.
  evidence:
  - status: 200
    url: https://us.bizay.com/en-us
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: Bizay is an online platform offering personalized promotional products and marketing materials. Customers can design and order custom business cards, flyers, stickers, apparel, and packaging through an intuitive web interface. The service targets businesses seeking branded merchandise, providing templates, design tools, and bulk ordering options. Bizay operates primarily in the United States, supporting English language customers and offering worldwide shipping. The company emphasizes fast turnaround, quality printing, and a wide range of product categories for marketing and corporate branding needs.
image: https://us.bizay.com/cdn-cgi/image/format=webp,quality=80/Images/OpenGraph/bizay/bizay_1080x1080.png?version=52d25674183fc6d54714d5a1c3ada578
layout: provider
modified: '2026-09-29'
name: Bizay
nav: Providers
network: true
overview: Bizay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Print on Demand, Marketing, and Customization.
random_paper: 15
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Bizay Domain Security
  slug: bizay-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bizay
tags:
- Company
- E-Commerce
- Print on Demand
- Marketing
- Customization
website: https://us.bizay.com/en-us
---
