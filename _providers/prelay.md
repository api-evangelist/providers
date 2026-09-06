---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prelay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prelay.com
coverage:
  checked: '2026-08-14'
  detail: 'Prelay has shut down — Y Combinator lists the W20 company as Inactive and Crunchbase records it as permanently closed — and the shutdown is visible in the infrastructure: prelay.com and www.prelay.com still point at the Webflow edge but the TLS certificate has been deprovisioned so no HTTPS request completes a handshake, app.prelay.com answers Google''s "Page not found" 404 for every path, and the github.com/prelay organization was archived on 2025-10-16 holding zero public repositories.'
  evidence:
  - status: 0
    url: https://www.prelay.com/
  - status: 0
    url: https://prelay.com/.well-known/agent-card.json
  - status: 404
    url: https://app.prelay.com/openapi.json
  - status: 403
    url: https://help.prelay.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/prelay
  - status: 200
    url: https://www.ycombinator.com/companies/prelay
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Prelay was a deal collaboration ("team selling") platform that helped B2B revenue teams coordinate the internal stakeholders behind complex enterprise deals — sales engineers, legal, deal desk, finance, and leadership — inside a shared workspace that plugged into the CRM. Founded 2019 in San Francisco (Y Combinator W20), it was a SaaS application aimed at sales and revenue operations, not a developer/API product. The company has since ceased operations: Y Combinator lists Prelay as Inactive, Crunchbase records it as permanently closed, the github.com/prelay organization was archived on 2025-10-16 with zero public repositories, and as of 2026-08-14 prelay.com and www.prelay.com no longer complete a TLS handshake (the Webflow certificate has been deprovisioned) while app.prelay.com answers 404 for every path. No public developer portal, API reference, OpenAPI/AsyncAPI specification, SDK, MCP server or agent card ever existed, and no api./docs./developers. subdomain resolves.
  Prelay was surfaced as a portfolio company of General Catalyst and added to the API Evangelist network.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prelay.png
layout: provider
modified: '2026-08-14'
name: Prelay
nav: Providers
network: true
overview: Prelay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Revenue Operations, Deal Collaboration, and Team Selling.
random_paper: 2
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Prelay Domain Security
  slug: prelay-domain-security
  summary_line: DNSSEC · DMARC
slug: prelay
tags:
- Company
- Sales
- Revenue Operations
- Deal Collaboration
- Team Selling
- Software-as-a-Service
website: https://www.prelay.com
---
