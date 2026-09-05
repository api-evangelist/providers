---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://stalkbuylove.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.styched.in/ — a different registrable domain (stalkbuylove.com -> styched.in), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stalkbuylove-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stalkbuylove.com
created: '2026-07-17'
description: StalkBuyLove was an India-based online women's fashion e-commerce retailer, surfaced as a portfolio company of 500 Global and added to the API Evangelist network as a stub for enrichment. As of this enrichment pass the brand appears defunct as an independent property, since the stalkbuylove.com domain now returns a 301 permanent redirect to styched.in (Styched, an unrelated Shopify-powered Indian youth-fashion retailer). No public developer portal, API, SDK, MCP server, changelog, or other machine-readable API surface could be found for StalkBuyLove on any registry or well-known path. The only honest signal available is the domain, DNS, and TLS security posture of the redirecting host, captured in the domain-security artifact.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stalkbuylove.png
layout: provider
modified: '2026-07-21'
name: StalkBuyLove
nav: Providers
network: true
overview: StalkBuyLove is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, E-Commerce, Retail, and Apparel.
random_paper: 15
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
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stalkbuylove/refs/heads/main/screenshots/stalkbuylove-2026-09-02T160725.png
security:
- kind: domain-security
  name: Stalkbuylove Domain Security
  slug: stalkbuylove-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stalkbuylove
tags:
- Company
- Fashion
- E-Commerce
- Retail
- Apparel
- India
- Consumer
website: https://stalkbuylove.com
---
