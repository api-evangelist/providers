---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
  score: 5.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The fastest continuous integration and continuous delivery platform
  name: Buddy
  slug: buddy
artifact_total: 3
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/buddy-a2a.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/buddy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buddy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buddy.works/docs/api/getting-started/overview
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://buddy.works/blog
created: '2026-05-28'
description: The fastest continuous integration and continuous delivery platform
layout: provider
modified: '2026-05-28'
name: Buddy
nav: Providers
network: true
overview: 'Buddy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Continuous Integration and Public APIs.


  Buddy''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buddy/refs/heads/main/screenshots/buddy-2026-06-20T173742.png
security:
- kind: domain-security
  name: Buddy Domain Security
  slug: buddy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Buddy Trust Center
  slug: buddy-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: buddy
tags:
- Continuous Integration
- Public APIs
website: https://buddy.works/docs/api/getting-started/overview
---
