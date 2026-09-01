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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/assurely-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/assurely-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/assurely-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/assurely-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.assurely.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/assurely
created: '2026-07-25'
description: Assurely is a United States insurtech and managing general agent (MGA) founded by David Carpentier and Ty Sagalow that builds and distributes commercial property-and-casualty insurance for companies with unconventional funding models, most notably TigerMark, a directors-and-officers (D&O) product written for Regulation CF / Regulation A crowdfunding issuers and early-stage startups that incumbent carriers decline. Assurely positioned itself as an "Insurance-as-a-Service" (IaaS) provider embedding industry-specific products plus a multi-carrier marketplace into vertical SaaS operating systems in fintech and capital raising, proptech and construction, property management, blockchain and digital assets, and SMB marketplaces (named partners include Wefunder, Silicon Prairie, Fairmint, Dalmore Group, Buildertrend and CoConstruct), and stated licensing in all 50 states and Bermuda. Its API posture is the honest floor of this sector — no public, self-serve developer portal, no API
  reference, and no downloadable OpenAPI was ever published. "Embedded" here meant a commercial partnership with white-labeled quote-and-bind web flows on client.assurely.com and tigermark.assurely.com plus human advisory and administration, not a documented partner API. Assurely was acquired by Equal Parts on 2025-06-26, and as of the 2026-07-25 review its entire public surface is offline — www.assurely.com returns HTTP 404 as an expired Squarespace site, and api./client./tigermark.assurely.com are dangling CNAMEs to a deleted AWS load balancer. Home market is the United States.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Assurely
nav: Providers
network: true
overview: Assurely is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United States, Insurtech, Embedded Insurance, and Managing General Agent.
random_paper: 6
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 5
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
  previous_composite: 4.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Assurely Domain Security
  slug: assurely-domain-security
  summary_line: TLSv1.3 · DMARC
slug: assurely
tags:
- Insurance
- United States
- Insurtech
- Embedded Insurance
- Managing General Agent
- Property and Casualty
- Directors and Officers
- Brokers
- Crowdfunding
website: https://www.assurely.com/
---
