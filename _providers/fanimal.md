---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://fanimal.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.tickpick.com/?fanimal=y — a different registrable domain (fanimal.com -> tickpick.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fanimal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fanimal.com
created: '2026-07-17'
description: Fanimal was surfaced as a portfolio company of bullpen-capital and added to the API Evangelist network as a stub for enrichment. Re-verified on 2026-07-20, the primary domain fanimal.com remains a parked, Cloudflare-fronted redirect — every path probed (root, /llms.txt, /.well-known/security.txt, /.well-known/openid-configuration, /.well-known/api-catalog, and the api./developer./docs. subdomains) returns HTTP 301 to https://tickpick.com/?fanimal=y. The ?fanimal=y attribution marker on a redirect into a ticket-resale marketplace indicates the property is defunct or has been absorbed by TickPick. No package was found on npm, PyPI, RubyGems, or crates.io; the github.com/Fanimal organization exists but is empty (0 public repos, no profile metadata) and cannot be verified as the same company. No independent Fanimal API, developer portal, OpenAPI spec, MCP server, or reachable /.well-known/ surface exists to enrich; there is no spec-bearing developer surface to ground any artifact
  against. The registered domain is still administered (live TLS, HSTS, SES SPF, Google and Klaviyo site-verification TXT records), which is captured in the probed domain-security artifact.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fanimal.png
layout: provider
modified: '2026-07-20'
name: Fanimal
nav: Providers
network: true
overview: Fanimal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Event, Ticketing, and Marketplace.
random_paper: 14
score:
  band: minimal
  composite: 5.0
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
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fanimal/refs/heads/main/screenshots/fanimal-2026-07-25T214219.png
security:
- kind: domain-security
  name: Fanimal Domain Security
  slug: fanimal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fanimal
tags:
- Company
- Defunct
- Event
- Ticketing
- Marketplace
website: https://fanimal.com
---
