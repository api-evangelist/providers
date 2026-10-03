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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ateamventures/refs/heads/main/hosts/ateamventures-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ateamventures-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ateamventures/refs/heads/main/vendors/ateamventures-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ateamventures-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ateamventures/refs/heads/main/security/ateamventures-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ateamventures-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/ateamventures
coverage:
  checked: 2026-09-26
  detail: The company website renders only via JavaScript, preventing machine‑readable extraction of API specifications.
  evidence:
  - status: 200
    url: https://ateamventures.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Ateamventures is a venture that focuses on personalized manufacturing, offering a platform that combines on‑demand 3D modeling with a network of local 3D printers. By providing a one‑stop‑shop for designers and inventors, it aims to reshape how hardware and software products are created, enabling rapid prototyping and small‑batch production. The company leverages AI and data analytics to streamline design workflows and connect customers with manufacturing resources, positioning itself at the intersection of advanced manufacturing and digital innovation.
image: https://dioguwdgf472v.cloudfront.net/media/logos/equityinvest/Company/ateamventures_logo-a43f4e7ba88603f8.jpg
layout: provider
modified: '2026-09-26'
name: Ateamventures
nav: Providers
network: true
overview: Ateamventures is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, 3D Printing, Artificial Intelligence, Platform, and Venture.
random_paper: 4
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ateamventures Domain Security
  slug: ateamventures-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ateamventures
tags:
- Manufacturing
- 3D Printing
- Artificial Intelligence
- Platform
- Venture
website: https://equityzen.com/company/ateamventures
---
