---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Lean theorem prover and programming language for formal verification of mathematics and software.
  name: Lean
  slug: lean
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lean-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lean-lang.org/
- group: docs
  title: ''
  type: Documentation
  url: https://lean-lang.org/documentation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leanprover/lean4
created: '2025-01-01'
description: Lean is an open-source theorem prover and programming language based on dependent type theory, designed for formal verification of mathematics and software. It supports interactive proof development and is used by mathematicians and computer scientists.
finops:
- name: Lean Finops
  service_category: API
  slug: lean-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lean.png
layout: provider
modified: '2026-04-28'
name: Lean
nav: Providers
network: true
overview: 'Lean publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Dependent Types, Formal Verification, Programming Language, and Theorem Prover.


  Lean''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Lean Plans Pricing
  plan_count: 3
  slug: lean-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Lean Rate Limits
  slug: lean-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lean/refs/heads/main/screenshots/lean-2026-06-20T184354.png
security:
- kind: domain-security
  name: Lean Domain Security
  slug: lean-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: lean
tags:
- Dependent Types
- Formal Verification
- Programming Language
- Theorem Prover
website: https://lean-lang.org/
---
