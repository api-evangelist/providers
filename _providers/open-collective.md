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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Get Open Collective data
  name: Open Collective
  slug: open-collective
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-collective-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-collective-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.opencollective.com/help/developers/api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://blog.opencollective.com/rss/
created: '2026-05-28'
description: Get Open Collective data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-collective.png
layout: provider
modified: '2026-05-28'
name: Open Collective
nav: Providers
network: true
overview: 'Open Collective publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social and Public APIs.


  Open Collective''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-collective/refs/heads/main/screenshots/open-collective-2026-06-20T190736.png
security:
- kind: domain-security
  name: Open Collective Domain Security
  slug: open-collective-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Open Collective Vulnerability Disclosure
  slug: open-collective-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: open-collective
tags:
- Social
- Public APIs
website: https://docs.opencollective.com/help/developers/api
---
