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
- description: Oasdiff is an open-source tool for detecting breaking changes and generating changelogs from OpenAPI specifications.
  name: Oasdiff
  slug: oasdiff
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oasdiff-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oasdiff
- group: company
  title: ''
  type: Website
  url: https://www.oasdiff.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tufin/oasdiff
- group: agent
  title: ''
  type: LlmsText
  url: https://www.oasdiff.com/llms.txt
created: '2026-03-29'
description: Oasdiff is an open-source tool for detecting breaking changes and generating changelogs from OpenAPI specifications.
finops:
- name: Oasdiff Finops
  service_category: API
  slug: oasdiff-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oasdiff.png
layout: provider
modified: '2026-03-29'
name: Oasdiff
nav: Providers
network: true
overview: Oasdiff publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Breaking Changes, Changelogs, Deprecation, and OpenAPI.
plans:
- name: Oasdiff Plans Pricing
  plan_count: 3
  slug: oasdiff-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Oasdiff Rate Limits
  slug: oasdiff-rate-limits
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 84.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oasdiff/refs/heads/main/screenshots/oasdiff-2026-06-20T190549.png
security:
- kind: domain-security
  name: Oasdiff Domain Security
  slug: oasdiff-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: oasdiff
tags:
- Breaking Changes
- Changelogs
- Deprecation
- OpenAPI
website: https://www.oasdiff.com/
---
