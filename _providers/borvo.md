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
  href: https://raw.githubusercontent.com/api-evangelist/borvo/refs/heads/main/hosts/borvo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/borvo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/borvo/refs/heads/main/vendors/borvo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/borvo-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/borvo/refs/heads/main/security/borvo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/borvo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://borvo.co/
- group: operate
  title: ''
  type: Contact
  url: https://borvo.co/#!/contacts
coverage:
  checked: '2026-10-02'
  detail: Site renders a JavaScript shell and no machine‑readable spec was found despite probing common spec URLs and rendering the homepage.
  evidence:
  - status: 200
    url: https://borvo.co/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: Borvo is an outsourcing IT company offering custom software development, big data analytics, research & development, and QA testing services. Based on its website, Borvo positions itself as a technology partner for web hosting companies, providing end‑to‑end solutions from specification to delivery. The firm showcases case studies, career opportunities, and a contact portal, indicating an active service‑focused business.
layout: provider
modified: '2026-10-02'
name: Borvo
nav: Providers
network: true
overview: Borvo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Software Development, Web Hosting, Big Data, QA Testing, and Research and Development.
random_paper: 2
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
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
  name: Borvo Domain Security
  slug: borvo-domain-security
  summary_line: TLSv1.3
slug: borvo
tags:
- Software Development
- Web Hosting
- Big Data
- QA Testing
- Research and Development
- Applications Development
website: https://borvo.co/
---
