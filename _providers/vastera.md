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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vastera-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vastera-llms.txt
- group: other
  title: ''
  type: CorporateFilings
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001075056&type=&dateb=&owner=include&count=40
created: '2026-07-17'
description: Vastera, Inc. was a global trade management (GTM) software and managed-services company headquartered in Dulles, Virginia. Its solutions automated the trade-management processes tied to the physical movement of goods across international borders — import/export documentation, licensing and classification, compliance and tax requirements, inventory management, and payment tracking. A Battery Ventures portfolio company, Vastera went public on Nasdaq in 2000 and was acquired by JPMorgan Chase Bank, N.A. for $3.00 per share (approximately $129 million), effective April 1, 2005, becoming JPMorgan Chase Vastera. It no longer operates independently and publishes no public website or APIs; the vastera.com domain remains registered but is configured for email only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vastera.png
layout: provider
modified: '2026-07-21'
name: Vastera
nav: Providers
network: true
overview: Vastera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Global Trade Management, Supply Chain, Trade Compliance, and Logistics.
random_paper: 2
score:
  band: minimal
  composite: 5.7
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
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vastera/refs/heads/main/screenshots/vastera-2026-09-02T165456.png
security:
- kind: domain-security
  name: Vastera Domain Security
  slug: vastera-domain-security
  summary_line: DMARC
slug: vastera
tags:
- Company
- Global Trade Management
- Supply Chain
- Trade Compliance
- Logistics
- Acquired
---
