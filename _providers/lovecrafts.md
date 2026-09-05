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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.lovecrafts.com/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/lovecrafts-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lovecrafts-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lovecrafts-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lovecrafts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lovecrafts.com/security.html
created: '2026-07-17'
description: LoveCrafts (LoveCrafts Group Limited) is a UK-based crafting commerce and community platform — "your home to shop, share and dream in crafts" — selling yarns and fibers, knitting, crochet, sewing, quilting and embroidery patterns, supplies, tools, kits and fabrics, alongside free and paid patterns, tutorials and inspiration content. It operates localized storefronts for North America, the UK, Germany, Australia and France on a Nuxt-based e-commerce stack. LoveCrafts was surfaced as a portfolio company of Balderton Capital and added to the API Evangelist network. It exposes no public developer portal or API surface; the only machine-discoverable public artifact is an RFC 9116 security.txt with a responsible- disclosure policy (no bug bounty programme).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lovecrafts.png
layout: provider
modified: '2026-07-20'
name: lovecrafts
nav: Providers
network: true
overview: lovecrafts is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crafts, E-Commerce, Retail, and Marketplace.
random_paper: 10
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
security:
- kind: domain-security
  name: Lovecrafts Domain Security
  slug: lovecrafts-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Lovecrafts Vulnerability Disclosure
  slug: lovecrafts-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lovecrafts
tags:
- Company
- Crafts
- E-Commerce
- Retail
- Marketplace
- Community
- Patterns
- Consumer
website: https://www.lovecrafts.com/
---
