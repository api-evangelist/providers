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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/txn-solutions-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/txn-solutions-llms.txt
created: '2026-07-17'
description: TXN Solutions (TXN) was a fintech startup founded in 2014 that offered a web application for consumer spending analytics, competitive intelligence, and surveys - capturing spending directly from the credit and debit cards of consumers who joined its research panel to give brands, investors, and researchers insight into consumer spending, merchant performance, and market positioning, including CPG and SKU-level data. It raised seed funding (announced November 2016) from a16z, Homebrew, Bloomberg Beta, and Social Starts. The company appears defunct as of July 2026 - its historical domain txn.com has been relinquished and is parked on the eName domain marketplace - and no public API surface is known.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/txn-solutions.png
layout: provider
modified: '2026-07-21'
name: TXN Solutions
nav: Providers
network: true
overview: TXN Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Transaction Data, Consumer Spending, and Market Research.
random_paper: 13
score:
  band: minimal
  composite: 5.7
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Txn Solutions Domain Security
  slug: txn-solutions-domain-security
  summary_line: no transport/DNS hardening detected
slug: txn-solutions
tags:
- Company
- Fintech
- Transaction Data
- Consumer Spending
- Market Research
- Analytics
---
