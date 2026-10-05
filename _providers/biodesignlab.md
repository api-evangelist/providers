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
  href: https://raw.githubusercontent.com/api-evangelist/biodesignlab/refs/heads/main/hosts/biodesignlab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biodesignlab-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://biodesignlab.net/team/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/biodesignlab
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biodesignlab/refs/heads/main/security/biodesignlab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biodesignlab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biodesignlab.net
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at the API host.
  evidence:
  - status: 0
    url: https://api.biodesignlab.net
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bio Design Lab is a biotechnology and bioengineering company based in Seoul, South Korea. It creates and develops highly potent biopharmaceuticals using synthetic biology and systems-level genetic and genomic designs. The firm focuses on advancing retroviral and lentiviral vector platforms for cell and gene therapies, offering vector packaging services and innovative platform solutions. Its mission is to design and construct gene and cell therapy drugs and immunotherapies, delivering novel therapeutic technologies.
image: https://biodesignlab.net/wp-content/uploads/2023/12/BDL-url-preview-image-1200x625-1.png
layout: provider
modified: '2026-09-28'
name: Biodesignlab
nav: Providers
network: true
overview: Biodesignlab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Bioengineering, Gene Therapy, and Synthetic Biology.
random_paper: 19
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 5
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
    discoverability: 50.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
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
  name: Biodesignlab Domain Security
  slug: biodesignlab-domain-security
  summary_line: TLSv1.2 · DMARC
slug: biodesignlab
tags:
- Company
- Biotechnology
- Bioengineering
- Gene Therapy
- Synthetic Biology
website: https://biodesignlab.net
---
