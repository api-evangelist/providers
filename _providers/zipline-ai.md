---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The fetch API from Zipline Ai — 4 operation(s) for fetch.
  name: Zipline Ai Fetch API
  slug: zipline-ai-fetch-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The health API from Zipline Ai — 2 operation(s) for health.
  name: Zipline Ai Health API
  slug: zipline-ai-health-api
- baseURL: http://localhost:9000
  baseurl_source: spec
  description: The schema API from Zipline Ai — 5 operation(s) for schema.
  name: Zipline Ai Schema API
  slug: zipline-ai-schema-api
- baseURL_template: https://{host}
  baseurl_source: spec_template
  description: The workflow API from Zipline Ai — 1 operation(s) for workflow.
  name: Zipline Ai Workflow API
  slug: zipline-ai-workflow-api
artifact_total: 14
collections:
- collection_type: open
  name: Zipline AI Fetcher fetch API
  slug: open-zipline-ai-fetch-api
- collection_type: open
  name: Zipline AI Fetcher fetch health API
  slug: open-zipline-ai-health-api
- collection_type: open
  name: Zipline AI Fetcher fetch schema API
  slug: open-zipline-ai-schema-api
- collection_type: open
  name: Zipline AI Fetcher fetch workflow API
  slug: open-zipline-ai-workflow-api
common:
- group: company
  title: ''
  type: Blog
  url: https://zipline.ai/blog
- group: other
  href: https://artifacts.apis.io/zipline-ai/capabilities/zipline-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zipline-ai-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/zipline-ai/skills/zipline-ai-fetch-features.md
  title: ''
  type: AgentSkill
  url: skills/zipline-ai-fetch-features.md
- group: agent
  href: https://artifacts.apis.io/zipline-ai/mcp/zipline-ai-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zipline-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/zipline-ai/overlays/zipline-ai-fetcher-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zipline-ai-fetcher-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/zipline-ai/security/zipline-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zipline-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/zipline-ai/authentication/zipline-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zipline-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://zipline.ai/
created: '2026-07-17'
description: Zipline Ai is a company surfaced as a portfolio company of wing-venture-capital and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zipline-ai.png
layout: provider
modified: '2026-10-06'
name: Zipline Ai
nav: Providers
network: true
overview: 'Zipline Ai publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Fetch API, Health API, Schema API, and 1 more. Tagged areas include Company.


  The Zipline Ai catalog on APIs.io includes 1 Spectral governance ruleset.


  Zipline Ai''s developer surface includes engineering blog, authentication, and 6 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Zipline Ai API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: zipline-ai-rules
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 26.5
    catalog_earned_first_party: 0.0
    catalog_gap: 88.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 31.8
    contract_quality: 36.1
    developer_ergonomics: 16.1
    discoverability: 46.4
    operational_transparency: 0.0
  previous_composite: 19.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/zipline-ai/zipline-ai-2026-09-02T171802.png
security:
- kind: authentication
  name: Zipline Ai Authentication
  slug: zipline-ai-authentication
  summary_line: http/oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Zipline Ai Domain Security
  slug: zipline-ai-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Zipline Ai Trust Center
  slug: zipline-ai-trust-center
  summary_line: trust center published
skill_count: 2
skills:
- name: Fetch online features for a model
  slug: zipline-ai-fetch-features
- name: Monitor a Zipline workflow run
  slug: zipline-ai-monitor-workflow
slug: zipline-ai
tags:
- Company
website: https://zipline.ai/
---
