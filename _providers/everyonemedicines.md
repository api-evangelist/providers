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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everyonemedicines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.everyonemedicines.com/
created: '2026-07-17'
description: Everyone Medicines is a therapeutics company listed in the Khosla Ventures portfolio under the Therapeutics category, where it is described as "individualized precision therapeutics." The company has no public developer or API surface as of July 2026. Its original web address, everyonemedicines.com, now issues a 301 redirect to www.eomeds.com, a domain registered through GoDaddy on 2024-05-11 that currently resolves to no DNS A record, so the site is dark and no page, documentation, or .well-known document can be retrieved. Probes of the package registries (npm, PyPI), GitHub organizations (everyonemedicines, eomeds), and the .well-known discovery surface all returned nothing. This profile is retained in the API Evangelist network as a venture-backed life-sciences lead; it carries probed domain-security data only and should be re-run once the company publishes a live site.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/everyonemedicines.png
layout: provider
modified: '2026-07-20'
name: Everyone Medicines
nav: Providers
network: true
overview: Everyone Medicines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Therapeutics, Precision Medicine, Biotechnology, and Life Sciences.
random_paper: 16
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Everyonemedicines Domain Security
  slug: everyonemedicines-domain-security
  summary_line: TLSv1.3
slug: everyonemedicines
tags:
- Company
- Therapeutics
- Precision Medicine
- Biotechnology
- Life Sciences
- Health
- Venture Backed
website: https://www.everyonemedicines.com/
---
