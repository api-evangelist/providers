---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
api_count: 3
apis:
- description: 'Discovery endpoint (GET api/service/v1/discovery) that a partner application calls on startup to resolve the current RESTful URI patterns for the Web-Intent resources it needs, rather than hardcoding '
  name: Mitchell 1 Intent Registry Discovery API
  slug: mitchell1-intent-registry-discovery-api
- description: Resolve endpoint (POST api/intent/v1/resolve) used to securely look up where a specific Web-Intent should be routed, as part of the TAPE (transfer application public extension) token flow that hands a
  name: Mitchell 1 Intent Resolve API
  slug: mitchell1-intent-resolve-api
- description: Two GET endpoints (api/script/v1/integrationclient and api/script/v1/integrationserver) listed in the sandbox Intent Registry index with no published documentation beyond their names; they appear to s
  name: Mitchell 1 Integration Script Services API
  slug: mitchell1-integration-script-services-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mitchell1-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mitchell-1/
- group: company
  title: ''
  type: Website
  url: https://mitchell1.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mitchell1.com/resources/api-request/
- group: commercial
  title: ''
  type: Plans
  url: plans/mitchell1-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://mitchell1.com/feed/
created: '2026-07-04'
description: Mitchell 1 is a division of Snap-on Incorporated providing repair information (ProDemand, TruckSeries) and shop management software (Manager SE, SocialCRM) to independent auto repair shops. Mitchell 1 is a legacy enterprise software provider, not an API-first company - it has no public, self-serve REST API reference. It does operate a gated Web-Intent / Data API integration program for approved third-party partners (shop management systems, CRM, parts and marketing platforms) to embed or link into ProDemand labor, parts, and maintenance data, fronted by a token-based (TAPE) auth flow and an Intent Registry discovery service. Access requires submitting an integration request, a Mitchell 1 review (roughly two weeks), and a signed partner agreement; no public API reference, OpenAPI document, or SDK is published. Note - Mitchell 1 (mitchell1.com, Snap-on) is a distinct company from Mitchell International (mitchell.com, part of Enlyte) - the two share a historical "Mitchell" lineage
  but are separately owned; Mitchell International's public developer.mitchell.com RepairCenter API belongs to the other company and is out of scope here.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mitchell1.png
layout: provider
modified: '2026-07-25'
name: Mitchell 1
nav: Providers
network: true
overview: 'Mitchell 1 publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Repair Information, Shop Management, Labor Guide, and VIN Decode.


  Mitchell 1''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Mitchell1 Plans Pricing
  plan_count: 4
  slug: mitchell1-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 52.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Mitchell1 Domain Security
  slug: mitchell1-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mitchell1
tags:
- Automotive
- Repair Information
- Shop Management
- Labor Guide
- VIN Decode
- Snap-on
- Partner API
- Gated
website: https://mitchell1.com/
---
