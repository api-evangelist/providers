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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pretty-litter/refs/heads/main/hosts/pretty-litter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pretty-litter-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pretty-litter/refs/heads/main/vendors/pretty-litter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pretty-litter-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.prettylitter.com/hc/en-us
- group: company
  title: ''
  type: Newsroom
  url: https://www.prettylitter.com/press
- group: start
  title: ''
  type: GettingStarted
  url: https://www.prettylitter.com/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.prettylitter.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pretty-litter/refs/heads/main/security/pretty-litter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pretty-litter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prettylitter.com
coverage:
  checked: '2026-10-12'
  detail: Developer portal pages render via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://dev.prettylitter.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Pretty Litter provides health‑monitoring cat litter that changes color to indicate potential health issues in cats. The subscription‑based product offers owners insights into urinary health, kidney function, and stress levels while reducing odor. Backed by Starting Line VC, the company operates under the Mars Petcare umbrella and serves a growing community of pet parents seeking proactive wellness solutions.
image: https://cdn.shopify.com/s/files/1/0997/4496/t/22/assets/pl_logo_new.png?v=9762398793934081268
layout: provider
modified: '2026-10-12'
name: Pretty Litter
nav: Providers
network: true
overview: 'Pretty Litter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pet Care, Health Monitoring, Subscription, Cat Litter, and Veterinary.


  Pretty Litter''s developer surface includes support, getting-started guide, documentation, and 5 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pretty Litter Domain Security
  slug: pretty-litter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pretty-litter
tags:
- Pet Care
- Health Monitoring
- Subscription
- Cat Litter
- Veterinary
website: https://prettylitter.com
---
