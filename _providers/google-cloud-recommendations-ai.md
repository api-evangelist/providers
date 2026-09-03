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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Recommendations Ai Agentic Access
  operation_count: 4
  slug: google-cloud-recommendations-ai-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- baseURL: https://recommendationengine.googleapis.com
  baseurl_source: declared
  description: The Projects API from Google Cloud Recommendations AI — 3 operation(s) for projects.
  name: Google Cloud Recommendations AI Projects API
  slug: google-cloud-recommendations-ai-projects-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Recommendations AI Projects API
  slug: open-google-cloud-recommendations-ai-projects-api
- collection_type: open
  name: Google Cloud Recommendations AI API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-recommendations-ai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-recommendations-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-recommendations-ai-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/recommendations-ai/docs/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/recommendations-ai/pricing
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: Google Cloud Recommendations AI delivers personalized product recommendations at scale. It uses machine learning to understand customer behavior and product catalog data to generate highly relevant recommendations for retail and e-commerce use cases including product discovery, related items, and frequently bought together.
finops:
- name: Google Cloud Recommendations Ai Finops
  service_category: API
  slug: google-cloud-recommendations-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-recommendations-ai.png
json_schemas:
- name: Catalog Item
  property_count: 8
  slug: catalog-item
jsonld:
- class_count: 14
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud Recommendations AI
nav: Providers
network: true
overview: 'Google Cloud Recommendations AI publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include E-Commerce, Google Cloud, Machine-Learning, Personalization, and Recommendations.


  The Google Cloud Recommendations AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Recommendations AI''s developer surface includes getting-started guide, pricing, and 5 more developer resources.'
plans:
- name: Google Cloud Recommendations Ai Plans Pricing
  plan_count: 3
  slug: google-cloud-recommendations-ai-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Google Cloud Recommendations Ai Rate Limits
  slug: google-cloud-recommendations-ai-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Recommendations AI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-recommendations-ai-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-recommendations-ai/refs/heads/main/screenshots/google-cloud-recommendations-ai-2026-06-20T182129.png
security:
- kind: domain-security
  name: Google Cloud Recommendations Ai Domain Security
  slug: google-cloud-recommendations-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Recommendations Ai Vulnerability Disclosure
  slug: google-cloud-recommendations-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-recommendations-ai
tags:
- E-Commerce
- Google Cloud
- Machine-Learning
- Personalization
- Recommendations
- Retail
---
