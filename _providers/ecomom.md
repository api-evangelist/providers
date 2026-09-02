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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: DomainForSale
  url: https://www.afternic.com/forsale/ecomom.com
created: '2026-07-17'
description: EcoMom was surfaced as a portfolio company of 500 Global and added to the API Evangelist network as a stub lead for enrichment. Enrichment probing on 2026-07-20 found no operating company surface behind the ecomom.com domain. The domain's nameservers are ns1/ns2.afternic.com and every request to ecomom.com issues a 307 redirect to an Afternic listing headlined "The domain name ecomom.com is for sale!" with no published price. The host serves a wildcard soft-200 parking page - arbitrary paths, including a deliberately nonsense control path, all return HTTP 200 with text/html that redirects to /lander - so the 200 status codes returned for /.well-known/security.txt, /.well-known/openid-configuration, /.well-known/oauth-authorization-server, /.well-known/api-catalog, /.well-known/ai-plugin.json, /llms.txt and /openapi.json are parking artifacts and not real documents. The api, developer, docs and www subdomains resolve to the same two parking IPs. There is no developer portal,
  no documentation, no specification and no API surface to catalog, so no enrichment artifacts were written for this company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ecomom.png
layout: provider
modified: '2026-07-20'
name: EcoMom
nav: Providers
network: true
overview: EcoMom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Venture Backed, 500 Global, Portfolio Lead, and Defunct.
random_paper: 10
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ecomom/refs/heads/main/screenshots/ecomom-2026-07-25T212804.png
slug: ecomom
tags:
- Company
- Venture Backed
- 500 Global
- Portfolio Lead
- Defunct
- No API Surface
- Domain For Sale
- E-Commerce
---
