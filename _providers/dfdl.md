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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dfdl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dfdl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daffodil.apache.org/
- group: docs
  title: ''
  type: Specification
  url: https://www.ogf.org/ogf/doku.php/standards/dfdl/dfdl
- group: other
  title: ''
  type: ISO Standard
  url: https://www.iso.org/standard/87444.html
- group: docs
  title: ''
  type: Documentation
  url: https://daffodil.apache.org/docs/
created: '2025-01-01'
description: Data Format Description Language (DFDL) is an open standard for describing data formats used in binary and text files and data streams. DFDL is used to describe the format of existing data so that it can be parsed or unparsed (generated) using a DFDL processor, enabling integration with legacy and modern data systems. DFDL was developed by the Open Grid Forum (OGF) and is also published as ISO/IEC 23415:2004. Apache Daffodil is the reference open-source implementation, with the latest release being version 4.1.0.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dfdl.png
layout: provider
modified: '2026-04-28'
name: DFDL
nav: Providers
network: true
overview: 'DFDL is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Apache Daffodil, Binary Data, Data Description, Data Formats, and DFDL.


  DFDL''s developer surface includes documentation and 5 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 7.2
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
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dfdl/refs/heads/main/screenshots/dfdl-2026-06-20T175955.png
security:
- kind: domain-security
  name: Dfdl Domain Security
  slug: dfdl-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Dfdl Vulnerability Disclosure
  slug: dfdl-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dfdl
tags:
- Apache Daffodil
- Binary Data
- Data Description
- Data Formats
- DFDL
- ISO Standard
- Open Grid Forum
- Parsing
- Schema
- Standards
- XML Schema
website: https://daffodil.apache.org/
---
