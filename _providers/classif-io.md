---
access_model:
  confidence: low
  label: Pricing not determined — a trial preceded paid volume-based tiers, but no price was ever published on a surface that survives
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - archive
  trial: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: One of the sixteen demo classification APIs Classif.io advertised, named "Fashion Style classification API" in the site navigation of the last archived capture of the homepage (2025-03-21). What the A
  name: Classif.io Fashion Style Classification API
  slug: fashion-style-classification-api
artifact_total: 6
common:
- group: design
  title: ''
  type: JSONLD
  url: json-ld/classif-io-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/classif-io-rules.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/classif-io-lifecycle.yml
coverage:
  checked: '2026-09-05'
  detail: 'Classif.io is gone, not merely unreachable: the .io registration has lapsed, the zone publishes no NS records, every resolver returns NXDOMAIN, and the registry operator''s RDAP endpoint answers HTTP 404 for the domain object, so the site, the Fashion Style Classification API page and every /.well-known/, /openapi.json and GraphQL probe fail at DNS before an HTTP request is made; the Internet Archive holds the homepage only — 18 rows, nothing after 2025-03-21, not one capture of any subpage — so no contract survives anywhere to harvest.'
  evidence:
  - status: 0
    url: https://www.classif.io/fashion-style-classification-api/
  - status: 0
    url: https://www.classif.io/
  - status: 0
    url: https://api.classif.io/openapi.json
  - status: 404
    url: https://rdap.identitydigital.services/rdap/domain/classif.io
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=classif.io
  - status: 404
    url: https://api.github.com/orgs/classif-io
  - status: 200
    url: http://web.archive.org/cdx/search/cdx?url=classif.io&matchType=domain
  reason: defunct
  state: none
created: '2025-03-01'
description: 'Classif.io was a machine-learning classification service that offered to build a custom classification model from a written description of the customer''s task, publish it as a REST API, and let prospects try an interactive demo before buying. Its site listed sixteen such demo APIs — Fashion Style Classification, Custom Car Part Identification, Surgical Instrument Classification, Retail Planogram Compliance and others — each on its own landing page, alongside a "describe your use case" intake form. The homepage credited Kindwise, the team behind Plant.id, Insect.id, Mushroom ID and crop.health, as the maker. The service is retired: the classif.io domain is no longer registered, the last live capture of the site is 2025-03-21, and no developer documentation, OpenAPI definition or other machine-readable contract survives in any public archive. See lifecycle/classif-io-lifecycle.yml for the retirement evidence.'
finops:
- name: Classif Io Finops
  service_category: API
  slug: classif-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/classif-io.png
jsonld:
- class_count: 13
  name: Classif Io Context
  property_count: 0
  slug: classif-io-context
layout: provider
modified: '2026-09-05'
name: Classif.io
nav: Providers
network: true
overview: 'Classif.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Apparel, Classification, Computer-Vision, Fashion, and Image Recognition.


  The Classif.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Classif Io Plans Pricing
  plan_count: 0
  slug: classif-io-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Classif Io Rate Limits
  slug: classif-io-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Classif.io API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: classif-io-rules
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 58.0
    catalog_earned_first_party: 0.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 45.5
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 45.5
    operational_transparency: 0.0
  previous_composite: 19.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
slug: classif-io
tags:
- Apparel
- Classification
- Computer-Vision
- Fashion
- Image Recognition
- Machine-Learning
- Recommendation
---
