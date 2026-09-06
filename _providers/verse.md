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
api_count: 1
apis:
- description: Authenticated backend API for Verse, served at api.verse.inc over the Connect RPC protocol (gRPC-compatible; advertises Connect-Protocol-Version and Authorization headers, and OPTIONS/GET/POST/PATCH/D
  name: Verse API
  slug: verse-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://verse.inc/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/verse-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/verse-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/verse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/verse-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verse-domain-security.yml
created: '2026-07-17'
description: 'Verse (verse.inc) is a private company backed by Bessemer Venture Partners, surfaced into the API Evangelist network from Bessemer''s portfolio. Its public marketing site is served entirely behind a Cloudflare bot challenge, so the product and sector could not be independently characterized from the site itself during enrichment. What is verifiable: Verse operates a live, authenticated backend API at api.verse.inc built on the Connect RPC protocol (a gRPC-compatible framework — the host advertises the Connect-Protocol-Version header and OPTIONS/GET/POST/PATCH/DELETE methods), fronted by Google infrastructure, and it publishes an RFC 9116 security.txt naming a security contact. No public OpenAPI, developer docs, SDKs, or MCP server were discoverable. Sector remains undetermined pending further research.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verse.png
layout: provider
modified: '2026-07-21'
name: Verse
nav: Providers
network: true
overview: Verse publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Connect RPC, gRPC, Bessemer Portfolio, and Cloudflare.
random_paper: 3
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/verse/refs/heads/main/screenshots/verse-2026-09-02T165815.png
security:
- kind: domain-security
  name: Verse Domain Security
  slug: verse-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Verse Vulnerability Disclosure
  slug: verse-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: verse
tags:
- Company
- Connect RPC
- gRPC
- Bessemer Portfolio
- Cloudflare
website: https://verse.inc/
---
