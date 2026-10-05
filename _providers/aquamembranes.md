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
api_count: 1
apis:
- description: API information referenced from the company's About page, though no machine-readable contract is available.
  name: Aquamembranes API
  slug: aquamembranes-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquamembranes/refs/heads/main/hosts/aquamembranes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aquamembranes-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aquamembranes/refs/heads/main/security/aquamembranes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aquamembranes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aquamembranes.com
- group: company
  title: ''
  type: Blog
  url: https://aquamembranes.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://aquamembranes.com/about/
coverage:
  checked: 2026-09-25
  detail: No OpenAPI or other machine-readable contract found on the site.
  evidence:
  - status: 200
    url: https://aquamembranes.com/about/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Aquamembranes provides optimized reverse osmosis technology with patented, precision printed elements that improve industrial RO systems. Their solutions lower energy costs, reduce cleaning cycles, and boost water recovery without retrofits. The company serves global leaders in water treatment, offering products, resources, and design software to enhance system performance.
image: https://821.29a.mytemp.website/wp-content/uploads/2026/04/Logo.svg
layout: provider
modified: '2026-09-25'
name: Aquamembranes
nav: Providers
network: true
overview: 'Aquamembranes publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Water Treatment, Reverse Osmosis, Clean Technology, Industrial Solutions, and Sustainability.


  Aquamembranes'' developer surface includes engineering blog, getting-started guide, and 3 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 7.1
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
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aquamembranes Domain Security
  slug: aquamembranes-domain-security
  summary_line: TLSv1.2 · DMARC
slug: aquamembranes
tags:
- Water Treatment
- Reverse Osmosis
- Clean Technology
- Industrial Solutions
- Sustainability
website: https://aquamembranes.com
---
