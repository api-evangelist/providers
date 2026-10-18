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
  href: https://raw.githubusercontent.com/api-evangelist/cloudframe/refs/heads/main/hosts/cloudframe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudframe-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloudframe/refs/heads/main/packages/cloudframe-packages.yml
  title: ''
  type: SDKs
  url: packages/cloudframe-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cloudframe/refs/heads/main/packages/cloudframe-packages.yml
  title: ''
  type: Packages
  url: packages/cloudframe-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://CloudFrame.com/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudframe
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudframe/refs/heads/main/security/cloudframe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudframe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudframe.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.cloudframe.com
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: CloudFrame provides mainframe modernization and COBOL transformation solutions, helping enterprises modernize legacy mainframe applications with confidence and velocity. Their platform offers tools like Continuum, CodeNavigator, and Atlas to analyze, transform, and migrate mainframe workloads to cloud-native environments, accelerating digital transformation and reducing operational risk.
image: https://CloudFrame.com/website/cf_og_image.png
layout: provider
modified: '2026-10-09'
name: CloudFrame
nav: Providers
network: true
overview: CloudFrame is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mainframe, Modernization, COBOL, and Cloud.
random_paper: 2
score:
  band: minimal
  composite: 5.7
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudframe Domain Security
  slug: cloudframe-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloudframe
tags:
- Company
- Mainframe
- Modernization
- COBOL
- Cloud
- Enterprise
website: https://www.cloudframe.com
---
