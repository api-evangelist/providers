---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH 2.0) endpoint for DepositOnce, the institutional repository of TU Berlin. Allows harvesting metadata for open-access publications and
  name: DepositOnce OAI-PMH Interface
  slug: depositonce-oai
- description: DSpace 8.1 REST/HAL API for the DepositOnce repository, exposing communities, collections, items, bitstreams and discovery endpoints. The API root returns a HAL document with dspaceVersion "DSpace 8.1
  name: DepositOnce DSpace REST API
  slug: depositonce-rest
- description: Self-hosted GitLab Enterprise Edition instance for TU Berlin. The GitLab REST API (v4) is present but gated — unauthenticated requests to /api/v4/ return HTTP 401. Login and API access require a TUB a
  name: TU Berlin GitLab API
  slug: gitlab
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tu-berlin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tu.berlin/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TU-Berlin
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TUUB
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tu-berlin/
- group: auth
  title: ''
  type: Authentication
  url: https://www.tu.berlin/campusmanagement/angebot/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/tu-berlin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tu-berlin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tu-berlin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Technische Universität Berlin (TU Berlin) is a public research university in Berlin, Germany, ranked #66 in the QS World University Rankings 2025. Its public developer/API footprint is concentrated in research-data and library infrastructure rather than a unified developer portal. The institutional repository DepositOnce runs on DSpace 8.1 and exposes a public OAI-PMH interface and a public DSpace REST/HAL API for harvesting open-access publications and research data. TU Berlin also operates a self-hosted GitLab instance (git.tu-berlin.de) whose API is gated behind Shibboleth SSO, plus public GitHub organizations (TU-Berlin, TUUB). Authentication across services is provided via Shibboleth/SAML (DFN-AAI), operated by the ZECM.'
finops:
- name: Tu Berlin Finops
  service_category: Education
  slug: tu-berlin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tu-berlin.png
jsonld:
- class_count: 17
  name: Tu Berlin Context
  property_count: 3
  slug: tu-berlin-context
layout: provider
modified: '2026-06-03'
name: Technical University of Berlin
nav: Providers
network: true
overview: 'Technical University of Berlin publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research Data, and Open Access.


  The Technical University of Berlin catalog on APIs.io includes 1 JSON-LD context.


  Technical University of Berlin''s developer surface includes GitHub presence, authentication, and 8 more developer resources.'
plans:
- name: Tu Berlin Plans Pricing
  plan_count: 2
  slug: tu-berlin-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Tu Berlin Rate Limits
  slug: tu-berlin-rate-limits
score:
  band: emerging
  composite: 22.4
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tu-berlin/refs/heads/main/screenshots/tu-berlin-2026-06-20T195818.png
security:
- kind: domain-security
  name: Tu Berlin Domain Security
  slug: tu-berlin-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tu-berlin
tags:
- Education
- Higher Education
- University
- Research Data
- Open Access
- Repository
- Library
- Germany
website: https://www.tu.berlin/en
---
