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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: API for accessing SPDX open standard resources for software bill of materials, license compliance, and software supply chain transparency information.
  name: SPDX API
  slug: spdx-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spdx-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://spdx.dev/learn/overview/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/spdx
- group: company
  title: ''
  type: Blog
  url: https://spdx.dev/feed/
created: '2026-03-16'
description: The Software Package Data Exchange (SPDX) is an open standard under the Linux Foundation for communicating software bill of materials information including components, licenses, copyrights, and security references. It is an ISO/IEC standard (ISO/IEC 5962) used for software supply chain transparency.
finops:
- name: Spdx Finops
  service_category: API
  slug: spdx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spdx.png
layout: provider
modified: '2026-03-16'
name: SPDX
nav: Providers
network: true
overview: 'SPDX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Licensing, Linux Foundation, SBOM, and Standards.


  SPDX''s developer surface includes documentation, engineering blog, and 2 more developer resources.'
plans:
- name: Spdx Plans Pricing
  plan_count: 3
  slug: spdx-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 5
  name: Spdx Rate Limits
  slug: spdx-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spdx/refs/heads/main/screenshots/spdx-2026-06-20T194248.png
security:
- kind: domain-security
  name: Spdx Domain Security
  slug: spdx-domain-security
  summary_line: TLSv1.3 · HSTS
slug: spdx
tags:
- Licensing
- Linux Foundation
- SBOM
- Standards
---
