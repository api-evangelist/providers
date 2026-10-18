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
  href: https://raw.githubusercontent.com/api-evangelist/cellmicrosystems/refs/heads/main/hosts/cellmicrosystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cellmicrosystems-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cellmicrosystems.com/clonechallenge/termsandconditions/
- group: operate
  title: ''
  type: Support
  url: https://cellmicrosystems.com/contact-us/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cellmicrosystems.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://cellmicrosystems.com/about-us/news
- group: other
  title: ''
  type: Leadership
  url: https://cellmicrosystems.com/about-us/leadership
- group: company
  title: ''
  type: Blog
  url: https://cellmicrosystems.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cellmicrosystems
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cellmicrosystems/refs/heads/main/security/cellmicrosystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cellmicrosystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cellmicrosystems.com
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 200
    url: https://cellmicrosystems.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cellmicrosystems develops innovative tools for single‑cell biology, offering platforms for imaging, sorting, and isolating individual cells and colonies. Their products support CRISPR gene editing, cancer research, stem‑cell studies, immunology and neurobiology, serving academic and biotech labs worldwide. The company provides detailed product information, application notes, and a blog with scientific content.
image: https://cellmicrosystems.com/wp-content/uploads/2016/10/Array-close-up-e1476822107719.jpg
layout: provider
modified: '2026-10-07'
name: Cellmicrosystems
nav: Providers
network: true
overview: 'Cellmicrosystems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Single Cell, Research, and Instruments.


  Cellmicrosystems'' developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 5
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
    discoverability: 51.8
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Cellmicrosystems Domain Security
  slug: cellmicrosystems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cellmicrosystems
tags:
- Company
- Biotechnology
- Single Cell
- Research
- Instruments
website: https://cellmicrosystems.com
---
