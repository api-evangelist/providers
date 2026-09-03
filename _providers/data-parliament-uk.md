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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Contains live datasets including information about petitions, bills, MP votes, attendance and more
  name: Data.parliament.uk
  slug: dataparliamentuk
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/data-parliament-uk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-parliament-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://explore.data.parliament.uk/?learnmore=Members
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Contains live datasets including information about petitions, bills, MP votes, attendance and more
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-parliament-uk.png
layout: provider
modified: '2026-05-28'
name: Data.parliament.uk
nav: Providers
network: true
overview: Data.parliament.uk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 8
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-parliament-uk/refs/heads/main/screenshots/data-parliament-uk-2026-06-20T175607.png
security:
- kind: domain-security
  name: Data Parliament Uk Domain Security
  slug: data-parliament-uk-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Data Parliament Uk Vulnerability Disclosure
  slug: data-parliament-uk-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: data-parliament-uk
tags:
- Government
- Public APIs
website: https://explore.data.parliament.uk/?learnmore=Members
---
