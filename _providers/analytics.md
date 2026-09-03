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
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://apievangelist.com
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/analytics-platform-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/analytics-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/analytics-vocabulary.yaml
- group: design
  title: ''
  type: Rules
  url: rules/analytics-jsonschema-spectral-rules.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/analytics-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
coverage:
  checked: '2026-08-13'
  detail: '"Analytics" is not a company — it is a curated topical index of the analytics ecosystem published by API Evangelist, so apis.yml carries an empty apis[] with no baseURL, no humanURL and no OpenAPI servers[] host; the only host it names is the publisher''s own site (apievangelist.com), whose one real discovery document (/.well-known/api-catalog) describes API Evangelist''s agent-skills index and belongs to the separate all/api-evangelist profile, not to this index. The 21 member platforms it points at each carry their own profiles and contracts.'
  evidence:
  - status: 404
    url: https://apievangelist.com/openapi.json
  - status: 404
    url: https://apievangelist.com/.well-known/security.txt
  - status: 404
    url: https://apievangelist.com/.well-known/agent-card.json
  - status: 200
    url: https://apievangelist.com/.well-known/api-catalog
  - status: 404
    url: https://raw.githubusercontent.com/api-evangelist/adjust/refs/heads/main/apis.yml
  reason: not-a-software-company
  state: none
created: '2024-01-15'
description: A curated index of analytics platforms, SDKs, and open source solutions spanning the full analytics spectrum — from web and product analytics (Google Analytics, Mixpanel, Amplitude, PostHog, Plausible, Matomo, Heap) to customer data platforms (Segment, mParticle, RudderStack), mobile analytics (Firebase Analytics, Adjust, AppsFlyer, Braze), business intelligence (Looker, Tableau, Metabase, Redash), event streaming (Kafka, Kinesis), and real-time analytics infrastructure (ClickHouse, Druid, Pinot). Covers both SaaS and self-hosted, open source and commercial offerings.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/analytics.png
json_schemas:
- name: Analytics Platform
  property_count: 14
  slug: analytics-platform
jsonld:
- class_count: 0
  name: Analytics Context
  property_count: 25
  slug: analytics-context
layout: provider
modified: '2026-08-13'
name: Analytics
nav: Providers
network: true
overview: 'Analytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Business Intelligence, Customer Data Platform, Data Pipeline, and Event Tracking.


  The Analytics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 2
rules:
- effective_rule_count: 5
  extends: []
  name: Analytics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: analytics-jsonschema-spectral-rules
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 71.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 25.0
    operational_transparency: 2.6
  previous_composite: 11.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/analytics/refs/heads/main/screenshots/analytics-2026-06-20T171946.png
slug: analytics
tags:
- Analytics
- Business Intelligence
- Customer Data Platform
- Data Pipeline
- Event Tracking
- Mobile Analytics
- Observability
- Product Analytics
- Real-Time Analytics
- Web Analytics
website: https://apievangelist.com
---
