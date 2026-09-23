---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-09-23'
api_count: 1
apis:
- baseURL: https://version-signal.inboxtzdjqv.workers.dev
  baseurl_source: declared
  description: Free, no-auth REST API returning the current stable version and publication date of npm and PyPI packages from the canonical registry.
  name: Version Signal API
  slug: version-signal-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://version-signal.inboxtzdjqv.workers.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://version-signal.inboxtzdjqv.workers.dev/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/version-signal-api/refs/heads/main/security/version-signal-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/version-signal-api-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/version-signal-api/refs/heads/main/authentication/version-signal-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/version-signal-api-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/version-signal-api/refs/heads/main/well-known/version-signal-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/version-signal-api-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/version-signal-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/version-signal-api/refs/heads/main/errors/version-signal-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/version-signal-api-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/version-signal-api/refs/heads/main/conventions/version-signal-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/version-signal-api-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/version-signal-api/refs/heads/main/lifecycle/version-signal-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/version-signal-api-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/version-signal-api/refs/heads/main/conformance/version-signal-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/version-signal-api-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/version-signal-api/refs/heads/main/plans/version-signal-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/version-signal-api-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/version-signal-api/refs/heads/main/rate-limits/version-signal-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/version-signal-api-rate-limits.yml
created: '2026-09-20'
description: Returns the current stable version and publication date of any npm or PyPI package, sourced from the canonical registry. A free, no-signup lookup tool with a browser UI and a machine-readable API, hosted on a Cloudflare Worker.
layout: provider
modified: '2026-09-20'
name: Version Signal
nav: Providers
network: true
overview: 'Version Signal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, Package Registry, npm, PyPI, and Versions.


  Version Signal''s developer surface includes documentation, authentication, and 10 more developer resources.'
plans:
- name: Version Signal Api Plans Pricing
  plan_count: 1
  slug: version-signal-api-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Version Signal Api Rate Limits
  slug: version-signal-api-rate-limits
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 29.9
    developer_ergonomics: 23.2
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 23.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Version Signal Api Authentication
  slug: version-signal-api-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Version Signal Api Domain Security
  slug: version-signal-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: version-signal-api
tags:
- Developer Tools
- Package Registry
- npm
- PyPI
- Versions
- Software Supply Chain
- Dependency Management
- open-source metadata
website: https://version-signal.inboxtzdjqv.workers.dev/
---
