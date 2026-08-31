---
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: A REST API over Verify's near real-time quality-control data. Beaconcure documents it as resource-oriented, accepting form-encoded request bodies and returning JSON (or CSV on request) with standard H
  name: Beaconcure Verify API
  slug: beaconcure-verify-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://beaconcure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://beaconcure.com/api/
- group: company
  title: ''
  type: Blog
  url: https://beaconcure.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://beaconcure.com/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Beaconcure-Inc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beaconcure.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beaconcure.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/beaconcure-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/beaconcure-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beaconcure-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beaconcure-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beaconcure-llms.txt
coverage:
  checked: '2026-08-06'
  detail: The public Verify API page describes the REST surface in prose but issues no reference — each customer gets a unique API version and endpoint URL from Beaconcure's customer success team, reachable only from an IP allowlist supplied at onboarding.
  evidence:
  - status: 200
    url: https://beaconcure.com/api/
  - status: 404
    url: https://beaconcure.com/openapi.json
  - status: 404
    url: https://beaconcure.com/docs
  - status: 404
    url: https://beaconcure.com/llms.txt
  - status: 404
    url: https://beaconcure.com/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: Beaconcure is a clinical data technology company whose AI-enabled platform, Verify, automates the statistical analysis and reporting workflow for biometrics teams running clinical trials. Verify converts static Tables, Listings and Figures (TLFs) into machine-readable form and runs format, reference, within-table and cross-table validation checks, tracks quality-control progress in a shared review workspace, and captures every fix in an inspection-ready audit trail across its Essentials, Validate and Generate modules. Beaconcure also documents a customer-scoped Verify REST API that exposes near real-time QC data — deliverables, projects, protocols, users, files, suspected and verified outputs, and discrepancies — as JSON or CSV, though each customer receives a unique API version and endpoint behind an IP allowlist. Founded in Israel with US headquarters in Boston, the company works with top-10 pharmaceutical companies and contract research organizations.
image: https://beaconcure.com/wp-content/uploads/2025/06/Artboard-1-copy-e1749721689852.png
layout: provider
modified: '2026-08-06'
name: Beaconcure
nav: Providers
network: true
overview: 'Beaconcure publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Clinical Trials, Clinical Data, Life Sciences, and Pharmaceuticals.


  Beaconcure''s developer surface includes documentation, engineering blog, support, authentication, and 8 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 17.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beaconcure/refs/heads/main/screenshots/beaconcure-2026-08-07T162233.png
security:
- kind: authentication
  name: Beaconcure Authentication
  slug: beaconcure-authentication
  summary_line: apiKey/ipAllowlist · 2 schemes
- kind: domain-security
  name: Beaconcure Domain Security
  slug: beaconcure-domain-security
  summary_line: TLSv1.3 · DMARC
slug: beaconcure
tags:
- Company
- Clinical Trials
- Clinical Data
- Life Sciences
- Pharmaceuticals
- Data Validation
- Quality Control
- Artificial Intelligence
- Biometrics
- Healthcare
website: https://beaconcure.com/
---
