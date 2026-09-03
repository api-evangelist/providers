---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Electra.Aero Agentic Access
  operation_count: 2
  slug: electra.aero-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://electra.aero/api
  baseurl_source: declared
  description: Electra newsroom and in-the-news entries.
  name: Electra.aero News API
  slug: electra.aero-news-api
artifact_total: 7
collections:
- collection_type: open
  name: Electra.aero Content API (news)
  slug: open-electra
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/electra.aero-content-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/electra.aero-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://electra.aero/
- group: company
  title: ''
  type: Blog
  url: https://electra.aero/news
- group: operate
  title: ''
  type: Support
  url: https://electra.aero/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/electra-aero/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ElectraAero
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Electraaero
- group: company
  title: ''
  type: Careers
  url: https://electra.aero/careers
- group: auth
  title: ''
  type: Authentication
  url: authentication/electra.aero-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/electra.aero-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/electra.aero-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/electra.aero-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/electra.aero-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/electra.aero-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/electra.aero-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/electra.aero-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/electra.aero-domain-security.yml
created: '2026-08-12'
description: Electra is an American aerospace manufacturer developing hybrid-electric "Ultra Short" aircraft that combine blown lift with hybrid-electric propulsion to take off and land in roughly 150 feet, removing the runway from regional air travel. Founded in 2020 by Dr. John Langford, the founder of Aurora Flight Sciences, with MIT professors John Hansman and Mark Drela as technical advisors, Electra flew its EL2 Goldfinch technology demonstrator in November 2023 and submitted an FAA Part 23 type-certification application for the nine-passenger EL9 Ultra Short in December 2025. The company reports more than 2,200 pre-orders from over 60 operators, and works both a commercial regional air-mobility market and a defense last-tactical-leg airlift market backed by U.S. Air Force SBIR Phase III and STTR contracts. It is headquartered in Manassas, Virginia, with operations in Cambridge, Massachusetts and Switzerland and a production facility under development at AirPark Ohio adjacent to Springfield-Beckley
  Municipal Airport. Strategic investors include Lockheed Martin Ventures, Honeywell and Safran. Electra publishes no developer program, API reference or machine-readable specification; the one public, anonymous JSON API it serves is the Statamic CMS content surface behind its newsroom, discovered and documented here by probe.
image: https://electra-aero.s3.us-east-1.amazonaws.com/electra-logo.svg
layout: provider
modified: '2026-08-12'
name: Electra.aero
nav: Providers
network: true
overview: 'Electra.aero publishes 1 API on the [APIs.io](https://apis.io/) network: News API. Tagged areas include Aerospace, Aviation, Aircraft Manufacturing, Advanced Air Mobility, and Electric Aviation.


  Electra.aero''s developer surface includes engineering blog, support, YouTube channel, authentication, and 15 more developer resources.'
plans:
- name: Electra.Aero Plans Pricing
  plan_count: 0
  slug: electra.aero-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Electra.Aero Rate Limits
  slug: electra.aero-rate-limits
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 57.1
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 26.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/electra.aero/refs/heads/main/screenshots/electra.aero-2026-09-02T145333.png
security:
- kind: authentication
  name: Electra.Aero Authentication
  slug: electra.aero-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Electra.Aero Domain Security
  slug: electra.aero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: electra.aero
tags:
- Aerospace
- Aviation
- Aircraft Manufacturing
- Advanced Air Mobility
- Electric Aviation
- Hybrid-Electric Propulsion
- Regional Air Mobility
- Defense
- Transportation
- Content
- Company
website: https://electra.aero/
---
