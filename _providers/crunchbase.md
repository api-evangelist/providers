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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Crunchbase Agentic Access
  operation_count: 10
  slug: crunchbase-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 4
apis:
- description: Type-ahead suggestions for entities.
  name: Crunchbase Autocomplete API
  slug: crunchbase-autocomplete-api
- description: Feeds of deleted entities for downstream sync.
  name: Crunchbase Deletes API
  slug: crunchbase-deletes-api
- description: Entity lookup endpoints for organizations, people, funding rounds, acquisitions, and IPOs.
  name: Crunchbase Entities API
  slug: crunchbase-entities-api
- description: Full-text and faceted search across entity types.
  name: Crunchbase Search API
  slug: crunchbase-search-api
artifact_total: 20
collections:
- collection_type: postman
  name: Crunchbase Autocomplete API
  slug: postman-crunchbase-autocomplete-api
- collection_type: postman
  name: Crunchbase Autocomplete Deletes API
  slug: postman-crunchbase-deletes-api
- collection_type: postman
  name: Crunchbase Autocomplete Entities API
  slug: postman-crunchbase-entities-api
- collection_type: postman
  name: Crunchbase Autocomplete Search API
  slug: postman-crunchbase-search-api
- collection_type: open
  name: Crunchbase API
  slug: open-crunchbase
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/crunchbase/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crunchbase-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crunchbase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crunchbase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crunchbase-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.crunchbase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://data.crunchbase.com/docs
- group: start
  title: ''
  type: Signup
  url: https://www.crunchbase.com/register
- group: start
  title: ''
  type: Login
  url: https://www.crunchbase.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crunchbase.com/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://data.crunchbase.com/docs/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://data.crunchbase.com/docs/rate-limiting
- group: operate
  title: ''
  type: ChangeLog
  url: https://data.crunchbase.com/docs/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.crunchbase.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crunchbase.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crunchbase.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.crunchbase.com/blog
- group: other
  title: ''
  type: X
  url: https://twitter.com/crunchbase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crunchbase
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/crunchbase
- group: build
  title: ''
  type: GitHub
  url: https://github.com/crunchbase
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/crunchbase-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/crunchbase-organization-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/crunchbase-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/crunchbase-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/crunchbase-vocabulary.yml
created: '2026-03-24'
description: Crunchbase is a business data platform tracking companies, investors, funding rounds, acquisitions, and IPOs across the global startup and private market ecosystem. Its REST API (v4) provides programmatic access to over 600 endpoints powering customer-facing products, workflow enrichment, and AI training data.
finops:
- name: Crunchbase Finops
  service_category: API
  slug: crunchbase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crunchbase.png
json_schemas:
- name: CrunchbaseOrganization
  property_count: 23
  slug: crunchbase-organization
jsonld:
- class_count: 18
  name: Crunchbase Context
  property_count: 9
  slug: crunchbase-context
layout: provider
modified: '2026-05-19'
name: Crunchbase
nav: Providers
network: true
overview: 'Crunchbase publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Deletes API, Entities API, and 1 more. Tagged areas include Business Data, Funding, Investments, Startups, and Private Markets.


  The Crunchbase catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Crunchbase''s developer surface includes authentication, documentation, signup flow, pricing, changelog, support, engineering blog, and 19 more developer resources.'
plans:
- name: Crunchbase Plans Pricing
  plan_count: 3
  slug: crunchbase-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Crunchbase Rate Limits
  slug: crunchbase-rate-limits
rules:
- name: Crunchbase API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: crunchbase-jsonschema-spectral-rules
- name: Crunchbase API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: crunchbase-rules
score:
  band: strong
  composite: 61.3
  delta: -3.7
  facets:
    commercial_clarity: 84.2
    contract_quality: 63.6
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 65.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crunchbase/refs/heads/main/screenshots/crunchbase-2026-06-20T175258.png
security:
- kind: authentication
  name: Crunchbase Authentication
  slug: crunchbase-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Crunchbase Domain Security
  slug: crunchbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crunchbase Vulnerability Disclosure
  slug: crunchbase-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crunchbase
tags:
- Business Data
- Funding
- Investments
- Startups
- Private Markets
- Firmographics
website: https://www.crunchbase.com/
---
