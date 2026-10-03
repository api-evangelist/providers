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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/awolvision/refs/heads/main/llms/awolvision-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/awolvision-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/awolvision/refs/heads/main/well-known/awolvision-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/awolvision-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/awolvision/refs/heads/main/hosts/awolvision-hosts.yml
  title: ''
  type: Hosts
  url: hosts/awolvision-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/awolvision/refs/heads/main/vendors/awolvision-vendors.yml
  title: ''
  type: Vendors
  url: vendors/awolvision-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://awolvision.com/pages/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.awolvision.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://awolvision.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://awolvision.com/blogs/news
- group: company
  title: ''
  type: Blog
  url: https://awolvision.com/blogs/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/awolvision/refs/heads/main/security/awolvision-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/awolvision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://awolvision.com
coverage:
  checked: 2026-09-27
  detail: The GraphQL endpoint appears to be a generic Shopify storefront API, not owned by Awolvision.
  evidence:
  - status: 200
    url: https://awolvision.com/api/graphql
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Awolvision designs and sells premium home theater projectors and accessories, offering 4K laser UST projectors, high‑gain screens, and related solutions for cinematic home entertainment. The company operates an e‑commerce site showcasing product lines like Aetherion, LuxVision, and Valerion, providing detailed specs, purchase options, and support resources for consumers and dealers.
image: http://awolvision.com/cdn/shop/files/AWOL_LOGO-150x150.png?v=1780293093
layout: provider
modified: '2026-09-27'
name: Awolvision
nav: Providers
network: true
overview: 'Awolvision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HomeTheater, Projectors, E-Commerce, and Consumer Electronics.


  Awolvision''s developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
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
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Awolvision Domain Security
  slug: awolvision-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: awolvision
tags:
- Company
- HomeTheater
- Projectors
- E-Commerce
- Consumer Electronics
website: https://awolvision.com
---
