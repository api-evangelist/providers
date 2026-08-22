---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 941
  human_in_the_loop: 3
  name: Lytics Agentic Access
  operation_count: 1467
  slug: lytics-agentic-access
  summary_line: 1467 operations · 941 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: Version 2 of the Lytics API — the current REST surface for the Lytics customer data platform. Covers accounts and users, authorizations and connections, data models and Cloud Connect, schema and ident
  name: Lytics API v2
  slug: lytics-api-v2
- description: 'Version 1 of the Lytics API — the data collection, personalization, segmentation, content and catalog surface. Includes the /collect data upload endpoints, the personalization and entity lookup APIs, '
  name: V1 Lytics API
  slug: lytics-api-v1
artifact_total: 22
asyncapis:
- description: ''
  name: Lytics Webhooks
  slug: lytics-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: V1 Lytics API
  slug: open-lytics-api-v1
- collection_type: open
  name: Lytics API
  slug: open-lytics-api-v2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lytics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lytics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lytics-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.lytics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lytics.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/lytics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lytics
- group: company
  title: ''
  type: Blog
  url: https://www.lytics.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lytics.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://lytics.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/lyticsio
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lytics.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.lytics.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/lytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lytics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lytics-finops.yml
- group: docs
  title: ''
  type: OpenAPI Source
  url: https://dash.readme.com/api/v1/api-registry/1y876emrv8pb2i
- group: build
  title: ''
  type: Packages
  url: packages/lytics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lytics-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lytics-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lytics-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/lytics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lytics-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lytics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lytics-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lytics-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/lytics-cli.yml
- group: design
  title: ''
  type: Components
  url: components/lytics-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lytics-webhooks.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lytics-trust-center.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/lytics-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/lytics-jsonschema-spectral-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/lytics-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lytics-user-profile-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lytics-collect-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lytics-segment-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/lytics-user-profile-example.json
- group: build
  title: ''
  type: Examples
  url: examples/lytics-collect-event-example.json
- group: build
  title: ''
  type: Examples
  url: examples/lytics-segment-scan-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/lytics-segment-scan-response-example.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lytics.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lytics.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lytics.com/reference/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.lytics.com/docs/developer-quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.lytics.com/register
- group: start
  title: ''
  type: Login
  url: https://app.lytics.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lytics.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lytics.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/lytics-cdp/lytics-s-public-workspace
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lytics
- group: operate
  title: ''
  type: Community
  url: https://docs.lytics.com/discuss
- group: auth
  title: ''
  type: Compliance
  url: https://docs.lytics.com/docs/compliance
created: '2026-06-13'
description: Lytics is a customer data platform (CDP) that provides two concurrent REST APIs for managing unified user profiles, behavioral audiences, content affinity scoring, campaign flows, and real-time personalization. The v2 API (886 paths / 1,331 operations) covers accounts, authorizations, connections, schema and identity configuration, data models, streams, jobs and ML models; the v1 API still owns data collection, personalization, entity lookup and content classification. Lytics ingests data from 100+ sources, builds predictive audiences, and activates them across advertising networks, email providers, data warehouses and on-site personalization. Lytics joined Contentstack in January 2025.
examples:
- key_count: 7
  name: Lytics Collect Event Example
  slug: lytics-collect-event-example
- key_count: 1
  name: Lytics Segment Scan Request Example
  slug: lytics-segment-scan-request-example
- key_count: 5
  name: Lytics Segment Scan Response Example
  slug: lytics-segment-scan-response-example
- key_count: 11
  name: Lytics User Profile Example
  slug: lytics-user-profile-example
finops:
- name: Lytics Finops
  service_category: ''
  slug: lytics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lytics.png
json_schemas:
- name: Lytics Collect Event
  property_count: 7
  slug: lytics-collect-event
- name: Lytics Segment
  property_count: 10
  slug: lytics-segment
- name: Lytics User Profile
  property_count: 11
  slug: lytics-user-profile
jsonld:
- class_count: 8
  name: Lytics Context
  property_count: 32
  slug: lytics-context
layout: provider
modified: '2026-08-13'
name: Lytics
nav: Providers
network: true
overview: 'Lytics publishes 2 APIs on the [APIs.io](https://apis.io/) network: API v2 and V1 Lytics API. Tagged areas include Customer Data Platform, CDP, Personalization, Segmentation, and User Profiles.


  The Lytics catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Lytics'' developer surface includes authentication, documentation, engineering blog, pricing, changelog, support, CLI, and 46 more developer resources.'
plans:
- name: Lytics Plans Pricing
  plan_count: 3
  slug: lytics-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Lytics Rate Limits
  slug: lytics-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lytics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lytics-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 66.5
  delta: -12.7
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 41.7
    contract_quality: 69.3
    developer_ergonomics: 65.5
    discoverability: 87.0
    governance: 41.7
    operational_transparency: 34.2
  previous_composite: 79.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/lytics/refs/heads/main/screenshots/lytics-2026-06-20T184816.png
security:
- kind: authentication
  name: Lytics Authentication
  slug: lytics-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Lytics Domain Security
  slug: lytics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Lytics Trust Center
  slug: lytics-trust-center
  summary_line: trust center published
slug: lytics
tags:
- Customer Data Platform
- CDP
- Personalization
- Segmentation
- User Profiles
- Behavioral Analytics
- Content Affinity
- Real-Time Data
- Marketing Automation
- Audience Activation
website: https://www.lytics.com/
---
