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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-06'
  detail: Moody's acquired Able in March 2024 and decommissioned able.ai — https://www.able.ai/ now aborts every TLS handshake with alert 40 and presents no certificate, the apex able.ai and the ableai.com pair only redirect into that dead host, and the plain-HTTP listener 301-redirects to Moody's Commercial Lending Solutions page, so not one of the 64 probed well-known and contract paths returned a document.
  evidence:
  - status: 0
    url: https://www.able.ai/.well-known/security.txt
  - status: 301
    url: https://able.ai/.well-known/security.txt
  - status: 301
    url: http://www.able.ai/.well-known/security.txt
  - status: 308
    url: https://ableai.com/.well-known/agent-card.json
  - status: 200
    url: https://www.moodys.com/web/en/us/solutions/lending.html
  - status: 404
    url: https://api.github.com/orgs/able-ai
  - status: 200
    url: https://equityzen.com/company/able42c5/
  reason: defunct
  state: none
created: '2026-09-06'
description: 'Able was a San Francisco artificial-intelligence company for commercial lending, founded in 2020 by Diego Represas and Andrew Hurst and operating at able.ai. Its platform used computer vision, robotic process automation and machine learning to collect, read and categorize borrower documentation for high-value commercial loan transactions, generating transaction-aware document checklists, sending automated follow-up reminders to the borrowing team, and giving lenders, borrowers and third parties such as appraisers, guarantors and insurers a single collaborative workspace with per-document access controls. It sold to banks and lenders rather than to borrowers, exited stealth in June 2022 with a $20M Series A led by Canapi Ventures with participation from Human Capital, demonstrated at FinovateFall 2022, and advertised SOC 2 compliance. Moody''s acquired Able in March 2024 and absorbed it into its lending technology portfolio alongside Numerated Growth Technologies. The able.ai
  and ableai.com domains are still registered to Moody''s registrant entity MIS Quality Management Corp. through CSC Corporate Domains, but the web surface is decommissioned: https://www.able.ai/ presents no TLS certificate and fails every handshake, while the plain-HTTP listener on that host 301-redirects to Moody''s Commercial Lending Solutions page. Able never published a developer portal, public API, SDK, webhook catalog or machine-readable specification; the archived site, whose last HTTP 200 homepage snapshot is 2024-03-28, carried only marketing, company, security, careers and legal pages. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-09-06'
name: Able
nav: Providers
network: true
overview: Able is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Acquired, Defunct, Financial Services, and Fintech.
random_paper: 7
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 4.6
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: able42c5
tags:
- Company
- Acquired
- Defunct
- Financial Services
- Fintech
- Lending
- Commercial Lending
- Loan Origination
- Document Automation
- Artificial Intelligence
---
