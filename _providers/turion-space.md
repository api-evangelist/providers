---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: First-party REST API gateway behind the STARFIRE customer dashboard. Route prefixes observed in the provider's own published dashboard bundle include /api/v1/tasking-orders, /api/v1/images/, /api/v1/t
  name: Turion Space STARFIRE API
  slug: turion-space-starfire-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turion-space-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/turion-space-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/turion-space-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://www.turionspace.com/
- group: company
  title: ''
  type: About
  url: https://turionspace.com/about
- group: company
  title: ''
  type: Blog
  url: https://turionspace.com/news
- group: operate
  title: ''
  type: Contact
  url: https://turionspace.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Turion-Space
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/turion-space
- group: start
  title: ''
  type: Login
  url: https://app.turionspace.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://turionspace.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://turionspace.com/terms-conditions
coverage:
  checked: '2026-09-01'
  detail: Turion Space runs a real first-party REST API — its own runtime config at app.turionspace.com/config.js names URL_API_GATEWAY as https://api.app.turionspace.com, and the gateway answers live — but there is no /developers, /docs or /pricing page anywhere in the turionspace.com sitemap, and the only entry point is the STARFIRE dashboard SPA, which serves a login shell and holds the entire reference behind an authenticated customer session.
  evidence:
  - status: 200
    url: https://starfire.turionspace.com/
  - status: 404
    url: https://turionspace.com/developers
  - status: 404
    url: https://api.app.turionspace.com/openapi.json
  - status: 404
    url: https://www.turionspace.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-09-01'
description: Turion Space is an Irvine, California aerospace company founded in 2021 (Y Combinator S21) that designs, builds and operates DROID maneuverable spacecraft for space domain awareness, non-earth imaging and in-orbit servicing, alongside the STARFIRE software platform for mission planning, autonomous tasking and command-and-control across Turion and third-party constellations. Its customer-facing surface is the STARFIRE dashboard at starfire.turionspace.com, backed by a first-party REST API gateway at api.app.turionspace.com that issues per-user API keys and meters imagery tasking and Starfire NEXUS jobs against a Stripe-billed credit balance. The company publishes no public developer portal, API reference, or machine-readable specification; the entire contract sits behind the STARFIRE customer login.
image: https://www.turionspace.com/images/turion-favicon.svg
layout: provider
modified: '2026-09-01'
name: Turion Space
nav: Providers
network: true
overview: 'Turion Space publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Satellites, Space Domain Awareness, and Non-Earth Imaging.


  Turion Space''s developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Turion Space Plans Pricing
  plan_count: 0
  slug: turion-space-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Turion Space Rate Limits
  slug: turion-space-rate-limits
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/turion-space/refs/heads/main/screenshots/turion-space-2026-09-02T164540.png
security:
- kind: authentication
  name: Turion Space Authentication
  slug: turion-space-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Turion Space Domain Security
  slug: turion-space-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: turion-space
tags:
- Company
- Space
- Satellites
- Space Domain Awareness
- Non-Earth Imaging
- Earth Observation
- Aerospace
- Defense
- Geospatial
- Imagery
website: https://www.turionspace.com/
---
