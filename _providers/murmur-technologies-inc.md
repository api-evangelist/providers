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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://murmurcars.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/murmur-technologies-inc-domain-security.yml
coverage:
  checked: '2026-08-12'
  detail: Both Murmur marketing domains resolve to Route 53 nameservers with no A record whatsoever, and the private REST backend the advertiser portal calls (backendapp.murmurcars.com) still resolves but has TCP 443 and 80 dead — the only surface left standing is a static React portal shell on S3/CloudFront whose last build shipped 2024-12-26 and which can no longer reach its own API.
  evidence:
  - status: 0
    url: https://murmurcars.com
  - status: 0
    url: https://murmurads.com
  - status: 0
    url: https://backendapp.murmurcars.com/api/v1/zipcode/get-us-information
  - status: 200
    url: https://portal.murmurads.com/
  - status: 404
    url: https://portal.murmurads.com/.well-known/security.txt
  - status: 404
    url: https://portal.murmurads.com/llms.txt
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Murmur Technologies INC (Murmur) is a Chicago, Illinois out-of-home advertising technology company operating a mobile digital billboard platform. It mounts smart LCD screens on car-tops and pedestrian backpacks to display geo-targeted ads on city streets, using sensors, computer vision, and location data to segment audiences by demographics, location, and behavior, measure ad performance in real time, and retarget viewers across other channels such as Facebook and Google. The company was surfaced as a portfolio company of 500 Global and added to the API Evangelist network as a lead for enrichment. As of the 2026-08-12 enrichment pass the operation appears dormant: both marketing domains (murmurcars.com and murmurads.com) carry Route 53 nameservers but no A record at all, and the blog host times out. The one surviving surface is portal.murmurads.com, the advertiser portal, a static React single-page app served from Amazon S3 behind CloudFront whose last build shipped 2024-12-26.
  Its JavaScript bundle calls a private REST backend at backendapp.murmurcars.com/api/v1/ (campaigns, venues, zipcode demographics, GPS, air quality and user endpoints), but that host — while it still resolves — has TCP 443 and 80 dead, so the portal front-end can no longer reach its own API. Murmur publishes no public API, developer portal, documentation, SDK, or machine-readable specification of any kind, and no package exists for it in any public registry.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/murmur-technologies-inc.png
layout: provider
modified: '2026-08-12'
name: Murmur Technologies INC
nav: Providers
network: true
overview: Murmur Technologies INC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Out-of-Home Advertising, and Digital Billboards.
random_paper: 16
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Murmur Technologies Inc Domain Security
  slug: murmur-technologies-inc-domain-security
  summary_line: DMARC
slug: murmur-technologies-inc
tags:
- Company
- Advertising
- AdTech
- Out-of-Home Advertising
- Digital Billboards
- Mobile Advertising
- Marketing
website: https://murmurcars.com
---
