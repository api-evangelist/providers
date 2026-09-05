---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Flagsmith Agentic Access
  operation_count: 35
  slug: flagsmith-agentic-access
  summary_line: 35 operations · 17 acting
api_count: 1
apis:
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: The Flagsmith Flags API is the public-facing REST API that client-side and server-side SDKs use to retrieve feature flag values and remote configuration for environments and users. It uses a non-secre
  name: Flagsmith Flags API
  slug: flags-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Manage environments within a project. Environments represent deployment stages such as development, staging, and production.
  name: flagsmith Environments API
  slug: flagsmith-environments-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Manage feature flags within a project. Features can be toggled on or off and can have remote configuration values.
  name: flagsmith Features API
  slug: flagsmith-features-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Manage user identities within an environment. Identities represent individual users and their associated traits.
  name: flagsmith Identities API
  slug: flagsmith-identities-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Manage organisations within Flagsmith. Organisations are the top-level container for projects, users, and billing.
  name: flagsmith Organisations API
  slug: flagsmith-organisations-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Manage projects within an organisation. Projects contain environments and feature flags.
  name: flagsmith Projects API
  slug: flagsmith-projects-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Manage segments within a project. Segments define groups of users based on traits and rules for targeted flag delivery.
  name: flagsmith Segments API
  slug: flagsmith-segments-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Manage organisation users and their permissions within Flagsmith.
  name: flagsmith Users API
  slug: flagsmith-users-api
- baseURL: https://edge.api.flagsmith.com
  baseurl_source: declared
  description: Configure webhooks for environments and organisations to receive notifications about flag changes and audit log events.
  name: flagsmith Webhooks API
  slug: flagsmith-webhooks-api
artifact_total: 31
asyncapis:
- description: Flagsmith provides two types of webhooks for receiving event notifications. Environment webhooks automatically send flag evaluations for identified users whenever an identity's flags are evaluated via
  name: Flagsmith Webhook Events
  slug: flagsmith-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flagsmith Admin API
  slug: open-flagsmith-admin-api
- collection_type: open
  name: Flagsmith Admin Environments API
  slug: open-flagsmith-environments-api
- collection_type: open
  name: Flagsmith Admin Environments Features API
  slug: open-flagsmith-features-api
- collection_type: open
  name: Flagsmith Admin Environments Flags API
  slug: open-flagsmith-flags-api
- collection_type: open
  name: Flagsmith Admin Environments Identities API
  slug: open-flagsmith-identities-api
- collection_type: open
  name: Flagsmith Admin Environments Organisations API
  slug: open-flagsmith-organisations-api
- collection_type: open
  name: Flagsmith Admin Environments Projects API
  slug: open-flagsmith-projects-api
- collection_type: open
  name: Flagsmith Admin Environments Segments API
  slug: open-flagsmith-segments-api
- collection_type: open
  name: Flagsmith Admin Environments Users API
  slug: open-flagsmith-users-api
- collection_type: open
  name: Flagsmith Admin Environments Webhooks API
  slug: open-flagsmith-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flagsmith-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flagsmith-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flagsmith-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flagsmith
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flagsmith
- group: design
  title: ''
  type: JSONLD
  url: json-ld/flagsmith-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/flagsmith-feature-flag-schema.json
- group: company
  title: ''
  type: Blog
  url: https://flagsmith.com/blog
description: Flagsmith is an open-source feature flag and remote configuration platform that helps developers manage feature flags across web, mobile, and server-side applications.
finops:
- name: Flagsmith Finops
  service_category: API
  slug: flagsmith-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flagsmith.png
json_schemas:
- name: Flagsmith Feature Flag
  property_count: 12
  slug: flagsmith-feature-flag
jsonld:
- class_count: 0
  name: Flagsmith Context
  property_count: 9
  slug: flagsmith-context
layout: provider
modified: '2026-05-19'
name: Flagsmith
nav: Providers
network: true
overview: 'Flagsmith publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Flags API, Environments API, Features API, and 6 more.


  The Flagsmith catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Flagsmith''s developer surface includes authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Flagsmith Plans Pricing
  plan_count: 3
  slug: flagsmith-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Flagsmith Rate Limits
  slug: flagsmith-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Flagsmith API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: flagsmith-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Flagsmith API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: flagsmith-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 71.8
    developer_ergonomics: 23.8
    discoverability: 44.4
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flagsmith/refs/heads/main/screenshots/flagsmith-2026-06-20T181306.png
security:
- kind: authentication
  name: Flagsmith Authentication
  slug: flagsmith-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Flagsmith Domain Security
  slug: flagsmith-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flagsmith
---
