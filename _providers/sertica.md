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
    auth_clarity: false
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
  score: 3.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Build interfaces to SERTICA Maintenance without any involvement from SERTICA.
  name: SERTICA
  slug: sertica
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sertica-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/sertica
- group: agent
  title: ''
  type: LlmsText
  url: https://sertica.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.sertica.com/blog/
created: '2025-02-12'
description: Build interfaces to SERTICA Maintenance without any involvement from SERTICA.
finops:
- name: Sertica Finops
  service_category: API
  slug: sertica-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sertica.png
layout: provider
modified: '2026-03-16'
name: SERTICA
nav: Providers
network: true
overview: 'SERTICA publishes 1 API on the [APIs.io](https://apis.io/) network.


  SERTICA''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: Sertica Plans Pricing
  plan_count: 3
  slug: sertica-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Sertica Rate Limits
  slug: sertica-rate-limits
score:
  band: minimal
  composite: 9.5
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 9.5
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sertica/refs/heads/main/screenshots/sertica-2026-06-20T193727.png
security:
- kind: domain-security
  name: Sertica Domain Security
  slug: sertica-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: sertica
---
