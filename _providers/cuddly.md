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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuddly/refs/heads/main/security/cuddly-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cuddly-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cuddly/refs/heads/main/llms/cuddly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cuddly-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cuddly/refs/heads/main/well-known/cuddly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cuddly-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cuddly/refs/heads/main/hosts/cuddly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cuddly-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cuddly/refs/heads/main/vendors/cuddly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cuddly-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://cuddly.com/press
- group: start
  title: ''
  type: Login
  url: https://cuddly.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuddly/refs/heads/main/security/cuddly-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cuddly-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cuddly/refs/heads/main/security/cuddly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cuddly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cuddly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cuddly.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://cuddly.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://cuddly.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cuddly.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cuddly.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://cuddly.com/contact-us
coverage:
  checked: '2026-10-12'
  detail: The provider's site returns a JSON at /openapi.json but it contains non‑OpenAPI data, not a machine‑readable contract.
  evidence:
  - status: 200
    url: https://cuddly.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: CUDDLY is a crowdfunding platform dedicated to animal welfare, enabling shelters and rescues to raise funds for supplies, medical care, and adoption support. The site offers wish‑list donations, a shop for pet products, and a community hub for donors, while providing transparent tracking of contributions and impact.
image: https://cuddly.com/img/cuddly.webp?t=1791777838
layout: provider
modified: '2026-10-11'
name: CUDDLY
nav: Providers
network: true
overview: 'CUDDLY is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crowdfunding, Animal Welfare, Non-Profit, and E-Commerce.


  CUDDLY''s developer surface includes documentation, engineering blog, pricing, support, and 12 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cuddly Domain Security
  slug: cuddly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cuddly Vulnerability Disclosure
  slug: cuddly-vulnerability-disclosure
  summary_line: no policy recorded
slug: cuddly
tags:
- Company
- Crowdfunding
- Animal Welfare
- Non-Profit
- E-Commerce
website: https://cuddly.com/
---
