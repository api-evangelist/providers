---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/3dfortify-com/hosts/3dfortify-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3dfortify-com-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/3DFortify
- group: auth
  href: https://artifacts.apis.io/3dfortify-com/security/3dfortify-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3dfortify-com-domain-security.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: http://www.3dfortify.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Fortify provides advanced 3D security scanning and vulnerability assessment services for software applications. Leveraging proprietary scanning engines, Fortify helps organizations identify, prioritize, and remediate security flaws across codebases, binaries, and container images. The platform integrates with CI/CD pipelines, offers detailed reporting, and supports compliance frameworks such as OWASP Top Ten, PCI DSS, and GDPR. Founded with backing from leading venture capital, Fortify aims to empower developers to build secure software by delivering actionable insights and automated remediation guidance.
layout: provider
modified: '2026-10-21'
name: Fortify
nav: Providers
network: true
overview: Fortify is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Application Security, DevOps, Vulnerability Management, and Cloud.
random_paper: 14
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 3.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 3Dfortify Com Domain Security
  slug: 3dfortify-com-domain-security
  summary_line: DMARC
slug: 3dfortify-com
tags:
- Security
- Application Security
- DevOps
- Vulnerability Management
- Cloud
---
