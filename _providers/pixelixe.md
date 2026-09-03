---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Pixelixe Agentic Access
  operation_count: 4
  slug: pixelixe-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://studio.pixelixe.com/api
  baseurl_source: declared
  description: The Authentication API from Pixelixe — 1 operation(s) for authentication.
  name: Pixelixe Authentication API
  slug: pixelixe-authentication-api
- baseURL: https://studio.pixelixe.com/api
  baseurl_source: declared
  description: The Document API from Pixelixe — 2 operation(s) for document.
  name: Pixelixe Document API
  slug: pixelixe-document-api
- baseURL: https://studio.pixelixe.com/api
  baseurl_source: declared
  description: The Graphic API from Pixelixe — 1 operation(s) for graphic.
  name: Pixelixe Graphic API
  slug: pixelixe-graphic-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pixelixe Authentication API
  slug: open-pixelixe-authentication-api
- collection_type: open
  name: Pixelixe Authentication Document API
  slug: open-pixelixe-document-api
- collection_type: open
  name: Pixelixe Authentication Graphic API
  slug: open-pixelixe-graphic-api
- collection_type: open
  name: Pixelixe
  slug: open-pixelixe
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pixelixe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixelixe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pixelixe-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pixelixe
- group: agent
  title: ''
  type: LlmsText
  url: https://pixelixe.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://pixelixe.com/blog
created: '2024-11-13'
description: Pixelixe is a comprehensive online design tool that allows users to create professional-quality graphics quickly and easily. With a user-friendly interface and a wide range of templates, images, and fonts to choose from, Pixelixe is perfect for individuals and businesses looking to enhance their online presence. Whether you need to design social media graphics, blog images, or marketing materials, Pixelixe offers the tools and resources needed to bring your vision to life.
finops:
- name: Pixelixe Finops
  service_category: API
  slug: pixelixe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pixelixe.png
layout: provider
modified: '2026-05-19'
name: Pixelixe
nav: Providers
network: true
overview: 'Pixelixe publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Document API, and Graphic API. Tagged areas include Graphics and Image.


  Pixelixe''s developer surface includes authentication, engineering blog, and 4 more developer resources.'
plans:
- name: Pixelixe Plans Pricing
  plan_count: 3
  slug: pixelixe-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Pixelixe Rate Limits
  slug: pixelixe-rate-limits
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pixelixe/refs/heads/main/screenshots/pixelixe-2026-06-20T191739.png
security:
- kind: authentication
  name: Pixelixe Authentication
  slug: pixelixe-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pixelixe Domain Security
  slug: pixelixe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pixelixe
tags:
- Graphics
- Image
---
