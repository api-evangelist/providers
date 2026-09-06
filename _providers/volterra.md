---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.volterra.io/'', ''status'': 301, ''note'': ''declared website redirects to https://www.f5.com/products/distributed-cloud-services — a different registrable domain (volterra.io -> f5.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/volterra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.volterra.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/volterraedge
- group: build
  title: ''
  type: Packages
  url: packages/volterra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/volterra-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/volterra-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/volterra-llms.txt
created: '2026-07-17'
description: Volterra was a Santa Clara-based distributed cloud company founded in 2017 by Ankur Singla, Harshad Nakil, and Ashish Ranjan, offering the VoltMesh (multi-cloud networking and security) and VoltStack (edge application deployment) SaaS platforms on a global application delivery network. Backed by roughly $50M from Khosla Ventures, Mayfield, M12, Samsung NEXT, and Itochu Technology Ventures, Volterra was acquired by F5 in January 2021 for approximately $500M and became the foundation of F5 Distributed Cloud Services. Its API surface (ves.io.schema, console.ves.volterra.io) is catalogued in the F5 Distributed Cloud Services profile, while the Volterra-branded Terraform provider and vesctl CLI remain published and maintained by F5.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/volterra.png
layout: provider
modified: '2026-07-21'
name: Volterra
nav: Providers
network: true
overview: 'Volterra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Edge Computing, Multi-Cloud, Distributed Cloud, and Networking.


  Volterra''s developer surface includes CLI and 6 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 8.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/volterra/refs/heads/main/screenshots/volterra-2026-09-02T170223.png
security:
- kind: domain-security
  name: Volterra Domain Security
  slug: volterra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: volterra
tags:
- Company
- Edge Computing
- Multi-Cloud
- Distributed Cloud
- Networking
- Application Security
- Kubernetes
- Acquired
website: https://www.volterra.io/
---
