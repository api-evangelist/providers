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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: 'The SCORM 1.2 Run-Time Environment defines communication between e-learning content and an LMS via a JavaScript API. The API Adapter is an ECMAScript object named "API" accessible through the DOM. It '
  name: SCORM 1.2 Runtime API
  slug: scorm-12
- description: The SCORM 2004 Run-Time Environment extends SCORM 1.2 with improved sequencing and navigation capabilities. The API Adapter is an ECMAScript object named "API_1484_11". It supports 8 core API function
  name: SCORM 2004 Runtime API
  slug: scorm-2004
- description: xAPI (Experience API), also known as Tin Can API, is the modern successor to SCORM developed by ADL. It uses a Learning Record Store (LRS) and defines learning statements in a subject-verb-object form
  name: xAPI (Experience API / Tin Can)
  slug: xapi
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scorm-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://scorm.com/blog/
created: '2026-05-02'
description: SCORM (Sharable Content Object Reference Model) is a set of technical standards for e-learning software products. Originally developed by the Advanced Distributed Learning (ADL) Initiative, SCORM defines how online learning content and Learning Management Systems (LMS) communicate with each other, enabling interoperability between authoring tools, content packages, and LMS platforms. Key versions include SCORM 1.2 and SCORM 2004, with xAPI (Tin Can) as a modern successor.
examples:
- key_count: 5
  name: Scorm Api Initialize Example
  slug: scorm-api-initialize-example
finops:
- name: Scorm Finops
  service_category: API
  slug: scorm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scorm.png
json_schemas:
- name: SCORM CMI Data Model
  property_count: 23
  slug: scorm-cmi-data
json_structures:
- name: Scorm Package Structure
  property_count: 0
  slug: scorm-package-structure
jsonld:
- class_count: 0
  name: Scorm Context
  property_count: 16
  slug: scorm-context
layout: provider
modified: '2026-05-02'
name: SCORM
nav: Providers
network: true
overview: 'SCORM publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include E-Learning, LMS, Standards, Education, and Interoperability.


  The SCORM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SCORM''s developer surface includes engineering blog and 1 more developer resources.'
plans:
- name: Scorm Plans Pricing
  plan_count: 3
  slug: scorm-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Scorm Rate Limits
  slug: scorm-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: SCORM API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: scorm-jsonschema-spectral-rules
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 66.3
    catalog_earned_first_party: 0.0
    catalog_gap: 48.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 25.3
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 21.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scorm/refs/heads/main/screenshots/scorm-2026-06-20T193543.png
security:
- kind: domain-security
  name: Scorm Domain Security
  slug: scorm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scorm
tags:
- E-Learning
- LMS
- Standards
- Education
- Interoperability
---
