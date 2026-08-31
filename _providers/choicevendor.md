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
artifact_total: 0
created: '2026-07-17'
description: ChoiceVendor is a company surfaced as a portfolio company of battery-ventures and added to the API Evangelist network as a stub for enrichment. An enrichment pass on 2026-07-20 found no live company surface to harvest - the choicevendor.com domain is still registered and delegated to Cloudflare name servers (autumn.ns.cloudflare.com, sevki.ns.cloudflare.com) but publishes no A record and no MX record, so no website, developer portal, documentation, or API host resolves. HTTPS requests to choicevendor.com and www.choicevendor.com fail to connect (curl exit 6, DNS resolution failure). Domain-security and security-program probes both returned no hosts and no vulnerability-disclosure or trust-center surface. There is no OpenAPI, no SDK, and no event surface to enrich, and no artifacts were fabricated. This profile remains a dormant portfolio lead and should be re-probed only if the domain is brought back online.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/choicevendor.png
layout: provider
modified: '2026-07-20'
name: ChoiceVendor
nav: Providers
network: true
overview: ChoiceVendor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Portfolio, Venture Backed, Battery Ventures, and Stub.
random_paper: 13
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 0
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: choicevendor
tags:
- Company
- Portfolio
- Venture Backed
- Battery Ventures
- Stub
- Dormant
- No API Surface
---
