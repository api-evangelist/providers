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
  href: https://raw.githubusercontent.com/api-evangelist/coherentbiopharma/refs/heads/main/hosts/coherentbiopharma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coherentbiopharma-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.coherentbio.com/media
- group: other
  title: ''
  type: Leadership
  url: https://www.coherentbio.com/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coherentbiopharma/refs/heads/main/security/coherentbiopharma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coherentbiopharma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coherentbio.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.coherentbio.com/about
- group: docs
  title: ''
  type: Documentation
  url: https://www.coherentbio.com/pipeline
- group: docs
  title: ''
  type: Documentation
  url: https://www.coherentbio.com/science
- group: docs
  title: ''
  type: Documentation
  url: https://www.coherentbio.com/publications
- group: docs
  title: ''
  type: Documentation
  url: https://www.coherentbio.com/patient-safety
- group: docs
  title: ''
  type: Documentation
  url: https://www.coherentbio.com/clinical-sites
- group: docs
  title: ''
  type: Documentation
  url: https://www.coherentbio.com/expanded-access-policy
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI or other machine‑readable contract found after probing common spec locations.
  evidence:
  - status: 404
    url: https://www.coherentbio.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Coherentbiopharma (CBP) is a biopharma company focused on pioneering bi‑targeting XDC technology to develop novel cancer therapies. The company’s website presents its mission, pipeline, scientific approach, clinical trials, publications, and patient safety information, offering insight into its drug discovery platform and corporate culture.
layout: provider
modified: '2026-10-09'
name: Coherentbiopharma
nav: Providers
network: true
overview: 'Coherentbiopharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Cancer, XDC Technology, and Innovation.


  Coherentbiopharma''s developer surface includes documentation and 11 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 5.3
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
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
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
  name: Coherentbiopharma Domain Security
  slug: coherentbiopharma-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coherentbiopharma
tags:
- Company
- Biopharma
- Cancer
- XDC Technology
- Innovation
website: https://www.coherentbio.com
---
