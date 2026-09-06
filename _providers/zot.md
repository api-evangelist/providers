---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Zot Agentic Access
  operation_count: 25
  slug: zot-agentic-access
  summary_line: 25 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Blobs API from Zot — 3 operation(s) for blobs.
  name: Zot Blobs API
  slug: zot-blobs-api
- description: The Catalog API from Zot — 1 operation(s) for catalog.
  name: Zot Catalog API
  slug: zot-catalog-api
- description: The Manifests API from Zot — 1 operation(s) for manifests.
  name: Zot Manifests API
  slug: zot-manifests-api
- description: The Oci API from Zot — 1 operation(s) for oci.
  name: Zot Oci API
  slug: zot-oci-api
- description: The Open Container Initiative Distribution Specification API from Zot — 1 operation(s) for open container initiative distribution specification.
  name: Zot Open Container Initiative Distribution Specification API
  slug: zot-open-container-initiative-distribution-specification-api
- description: The Referrers API from Zot — 1 operation(s) for referrers.
  name: Zot Referrers API
  slug: zot-referrers-api
- description: The Tags API from Zot — 1 operation(s) for tags.
  name: Zot Tags API
  slug: zot-tags-api
- description: The Zot API from Zot — 6 operation(s) for zot.
  name: Zot Zot API
  slug: zot-zot-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open Container Initiative Distribution Specification Blobs API
  slug: open-zot-blobs-api
- collection_type: open
  name: Open Container Initiative Distribution Specification Blobs Catalog API
  slug: open-zot-catalog-api
- collection_type: open
  name: Open Container Initiative Distribution Specification Blobs Manifests API
  slug: open-zot-manifests-api
- collection_type: open
  name: Open Container Initiative Distribution Specification Blobs Oci API
  slug: open-zot-oci-api
- collection_type: open
  name: Blobs Open Container Initiative Distribution Specification API
  slug: open-zot-open-container-initiative-distribution-specification-api
- collection_type: open
  name: Open Container Initiative Distribution Specification Blobs Referrers API
  slug: open-zot-referrers-api
- collection_type: open
  name: Open Container Initiative Distribution Specification Blobs Tags API
  slug: open-zot-tags-api
- collection_type: open
  name: Open Container Initiative Distribution Specification Blobs Zot API
  slug: open-zot-zot-api
- collection_type: open
  name: Open Container Initiative Distribution Specification
  slug: open-zot
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zot-agentic-access.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/project-zot
created: '2025'
description: A decentralized communication protocol and platform for federated social networking, enabling secure and private content sharing across distributed servers.
finops:
- name: Zot Finops
  service_category: API
  slug: zot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zot.png
layout: provider
modified: '2026-05-19'
name: Zot
nav: Providers
network: true
overview: Zot publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Blobs API, Catalog API, Manifests API, and 5 more. Tagged areas include Decentralized, Federation, Privacy, and Social Networking.
plans:
- name: Zot Plans Pricing
  plan_count: 1
  slug: zot-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Zot Rate Limits
  slug: zot-rate-limits
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 40.7
    developer_ergonomics: 0.0
    discoverability: 38.9
    governance: 0.0
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 22.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zot/refs/heads/main/screenshots/zot-2026-06-20T201959.png
slug: zot
tags:
- Decentralized
- Federation
- Privacy
- Social Networking
website: https://zotlabs.org
---
