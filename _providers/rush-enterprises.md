---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: RushCare Service Connect is a technology platform that provides a single portal integrated with OEMs, third-party repair software systems, and real-time telematics providers. It integrates with Peterb
  name: RushCare Service Connect
  slug: rushcare-service-connect
- description: RushCare Parts Connect is a technology platform for managing commercial vehicle parts procurement and supply chain operations across Rush Truck Centers locations.
  name: RushCare Parts Connect
  slug: rushcare-parts-connect
- description: RushCare Telematics provides fleet visibility and vehicle data monitoring powered by Geotab, the world's largest provider of premium quality telematics hardware. The platform offers an open SDK for in
  name: RushCare Telematics
  slug: rushcare-telematics
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rush-enterprises-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rush-enterprises-inc
- group: company
  title: ''
  type: Website
  url: https://www.rushenterprises.com
- group: company
  title: ''
  type: Website
  url: https://www.rushtruckcenters.com
- group: other
  title: ''
  type: Technology
  url: https://rushcare.rushtruckcenters.com/
- group: company
  title: ''
  type: About
  url: https://www.rushenterprises.com/our-story
- group: company
  title: ''
  type: Investors
  url: https://investors.rushenterprises.com
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rush-enterprises/refs/heads/main/vocabulary/rush-enterprises-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rush-enterprises/refs/heads/main/json-ld/rush-enterprises-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rush-enterprises/refs/heads/main/json-schema/rush-enterprises-vehicle-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rush-enterprises/refs/heads/main/json-schema/rush-enterprises-service-event-schema.json
- group: company
  title: ''
  type: Blog
  url: https://www.rushtruckcenters.com/blog
created: '2026-03-21'
description: Rush Enterprises is the largest network of commercial vehicle dealerships in North America, operating Rush Truck Centers with more than 200 locations across the United States. The company offers new and used commercial vehicles, all-makes parts, vehicle technology solutions, collision repair, alternative fuel systems, vehicle and equipment leasing, and financial services. Rush Enterprises provides fleet technology through RushCare, including Service Connect (integrated with OEMs like Peterbilt, International, Hino, and Cummins), Parts Connect, and telematics solutions powered by Geotab.
examples:
- key_count: 9
  name: Rush Enterprises Service Event Example
  slug: rush-enterprises-service-event-example
- key_count: 10
  name: Rush Enterprises Vehicle Example
  slug: rush-enterprises-vehicle-example
finops:
- name: Rush Enterprises Finops
  service_category: API
  slug: rush-enterprises-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rush-enterprises.png
json_schemas:
- name: Rush Enterprises Service Event
  property_count: 10
  slug: rush-enterprises-service-event
- name: Rush Enterprises Commercial Vehicle
  property_count: 10
  slug: rush-enterprises-vehicle
json_structures:
- name: Rush Enterprises Service Event Structure
  property_count: 0
  slug: rush-enterprises-service-event-structure
- name: Rush Enterprises Vehicle Structure
  property_count: 0
  slug: rush-enterprises-vehicle-structure
jsonld:
- class_count: 0
  name: Rush Enterprises Context
  property_count: 19
  slug: rush-enterprises-context
layout: provider
modified: '2026-05-02'
name: Rush Enterprises
nav: Providers
network: true
overview: 'Rush Enterprises publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Commercial Vehicles, Fleet Management, Telematics, Truck Dealerships, and Transportation.


  The Rush Enterprises catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Rush Enterprises'' developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Rush Enterprises Plans Pricing
  plan_count: 3
  slug: rush-enterprises-plans-pricing
press:
- date: '2026-05-25'
  title: 'Q&A: Rush Execs Talk Industry Challenges and Trends'
  url: https://www.truckinginfo.com/news/qa-rush-ceo-and-ceo-talk-industry-challenges-and-trends
- date: '2026-05-25'
  title: Rush Enterprises signals Class 8 sales up 15% in Q2 as it ...
  url: https://seekingalpha.com/news/4582247-rush-enterprises-signals-class-8-sales-up-15-percent-in-q2-as-it-targets-june-close-for-gulf
- date: '2026-05-25'
  title: Is AI's Cooler View of Rush Enterprises' Growth Rewriting ...
  url: https://simplywall.st/stocks/us/capital-goods/nasdaq-rush.a/rush-enterprises/news/is-ais-cooler-view-of-rush-enterprises-growth-rewriting-the
- date: '2026-05-25'
  title: RUSH ENTERPRISES, INC
  url: https://investor.rushenterprises.com/static-files/c6ec57d1-bc1d-4edb-b52f-f9255962bb8e
- date: '2026-05-25'
  title: Norton Rose Fulbright represents Rush Enterprises in joint ...
  url: https://www.nortonrosefulbright.com/en-us/news/9cac52b2/norton-rose-fulbright-represents-rush-enterprises-in-joint-venture-with-cummins-inc
random_paper: 19
rate_limits:
- limit_count: 5
  name: Rush Enterprises Rate Limits
  slug: rush-enterprises-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Rush Enterprises API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rush-enterprises-jsonschema-spectral-rules
score:
  band: emerging
  composite: 17.0
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 11.3
    developer_ergonomics: 2.4
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 17.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rush-enterprises/refs/heads/main/screenshots/rush-enterprises-2026-06-20T193300.png
security:
- kind: domain-security
  name: Rush Enterprises Domain Security
  slug: rush-enterprises-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rush-enterprises
tags:
- Commercial Vehicles
- Fleet Management
- Telematics
- Truck Dealerships
- Transportation
- Fortune 1000
website: https://www.rushenterprises.com
---
