---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.zo.computer
  baseurl_source: spec
  description: The AI API from Zocomputer — 3 operation(s) for ai.
  name: Zocomputer AI API
  slug: zocomputer-ai-api
- baseURL: https://api.zo.computer
  baseurl_source: spec
  description: The Personas API from Zocomputer — 1 operation(s) for personas.
  name: Zocomputer Personas API
  slug: zocomputer-personas-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zo AI API
  slug: open-zocomputer-ai-api
- collection_type: open
  name: Zo AI Personas API
  slug: open-zocomputer-personas-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zocomputer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zocomputer-domain-security.yml
created: '2026-07-17'
description: Zocomputer is a company surfaced as a portfolio company of lightspeed-venture-partners and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zocomputer.png
layout: provider
modified: '2026-07-17'
name: Zocomputer
nav: Providers
network: true
overview: 'Zocomputer publishes 2 APIs on the [APIs.io](https://apis.io/) network: AI API and Personas API. Tagged areas include Company.'
random_paper: 20
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 93.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 52.7
    developer_ergonomics: 0.0
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 18.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Zocomputer Domain Security
  slug: zocomputer-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Zocomputer Vulnerability Disclosure
  slug: zocomputer-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zocomputer
tags:
- Company
---
