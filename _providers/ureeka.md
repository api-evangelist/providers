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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ureeka-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ureeka.biz
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ureeka-llms.txt
created: '2026-07-17'
description: Ureeka was a community and mentorship platform for small businesses, surfaced as a Bullpen Capital portfolio company. The company no longer operates a standalone product - the ureeka.biz domain (www and apex) now permanently redirects (HTTP 301) to zenbusiness.com, and no developer, documentation, or API surface remains. Probed 2026-07-21 by the API Evangelist enrichment pipeline; no API artifacts exist to harvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ureeka.png
layout: provider
modified: '2026-07-21'
name: Ureeka
nav: Providers
network: true
overview: Ureeka is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Small Business, Mentorship, Community, and Entrepreneurship.
random_paper: 7
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ureeka/refs/heads/main/screenshots/ureeka-2026-09-02T165214.png
security:
- kind: domain-security
  name: Ureeka Domain Security
  slug: ureeka-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ureeka
tags:
- Company
- Small Business
- Mentorship
- Community
- Entrepreneurship
- Defunct
website: https://www.ureeka.biz
---
