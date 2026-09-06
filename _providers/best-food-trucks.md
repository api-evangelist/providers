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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/best-food-trucks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/best-food-trucks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/best-food-trucks-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/best-food-trucks-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/best-food-trucks-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://bestfoodtrucks.com/
created: '2026-07-17'
description: Best Food Trucks (BFT) operates a food truck booking, scheduling, and mobile ordering platform that connects food truck vendors with property managers, office buildings, event organizers, and hungry customers. The platform lets locations schedule rotating food trucks, lets customers browse menus and place mobile orders ahead of time, and gives trucks a point-of-sale and payments surface for on-site service. Backed by Techstars, the company was surfaced as a portfolio-company lead and enriched into the API Evangelist network. This profile currently carries only public infrastructure and security artifacts; no public API, developer portal, or OpenAPI surface was discoverable during enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/best-food-trucks.png
layout: provider
modified: '2026-07-18'
name: Best Food Trucks
nav: Providers
network: true
overview: Best Food Trucks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Trucks, Food and Beverage, Mobile Ordering, and Event.
random_paper: 16
score:
  band: minimal
  composite: 6.4
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
    operational_transparency: 10.5
  previous_composite: 6.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Best Food Trucks Domain Security
  slug: best-food-trucks-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Best Food Trucks Vulnerability Disclosure
  slug: best-food-trucks-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: best-food-trucks
tags:
- Company
- Food Trucks
- Food and Beverage
- Mobile Ordering
- Event
- Catering
- Point-of-Sale
website: https://bestfoodtrucks.com/
---
