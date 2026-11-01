---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API reference for Reo.dev low-code platform
  name: Reo.dev API
  slug: reo-dev-api
- baseURL: https://ingest.reo.dev
  baseurl_source: declared
  description: 'Reo.dev API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Reo.dev API
  slug: reodev-api
artifact_total: 7
asyncapis:
- description: ''
  name: Reodev Webhooks
  slug: reodev-webhooks
common:
- group: design
  href: https://artifacts.apis.io/reodev/rules/reodev-rules.yml
  title: ''
  type: Spectral
  url: rules/reodev-rules.yml
- group: design
  href: https://artifacts.apis.io/reodev/json-ld/reodev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/reodev-context.jsonld
- group: design
  href: https://artifacts.apis.io/reodev/vocabulary/reodev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/reodev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/reodev/asyncapi/reodev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/reodev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/reodev/data-model/reodev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reodev-data-model.yml
- group: design
  href: https://artifacts.apis.io/reodev/conformance/reodev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reodev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/reodev/llms/reodev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reodev-llms.txt
- group: agent
  href: https://artifacts.apis.io/reodev/well-known/reodev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/reodev-well-known.yml
- group: other
  href: https://artifacts.apis.io/reodev/hosts/reodev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reodev-hosts.yml
- group: other
  href: https://artifacts.apis.io/reodev/vendors/reodev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reodev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reo.dev/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reo.dev/
- group: start
  title: ''
  type: SignUp
  url: https://www.reo.dev/feature/signup-deanonymization
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reo.dev/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/johndoe
- group: company
  title: ''
  type: Blog
  url: https://www.reo.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reo.dev/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.reo.dev/
- group: auth
  href: https://artifacts.apis.io/reodev/security/reodev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reodev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reo.dev
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract found despite documentation pages.
  evidence:
  - status: 404
    url: https://api.reo.dev/openapi.json
  - status: 404
    url: https://api.reo.dev/openapi.yaml
  - status: 404
    url: https://api.reo.dev/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Reo.dev provides a low-code platform that enables developers to quickly build, test, and deploy APIs and integrations. The service offers visual workflow designers, pre-built connectors to popular SaaS services, and robust monitoring tools. Founded in 2022 and backed by Heavybit, Reo.dev aims to simplify API development for startups and enterprises alike, focusing on speed, scalability, and developer experience. Their platform includes features such as automated documentation, versioning, and security controls, making it a comprehensive solution for modern API-driven applications.
image: https://cdn.prod.website-files.com/67e6b65ee328bc6b91324c9a/6a58c7d586ec14acfc997712_Homepage%20-%20Opengraph.png
json_schemas:
- name: PostApiProductAggregateusageRequest
  property_count: 1
  slug: reodev-post-api-product-aggregateusage-request
jsonld:
- class_count: 1
  name: Reodev Context
  property_count: 1
  slug: reodev-context
layout: provider
modified: '2026-10-29'
name: Reo.dev
nav: Providers
network: true
overview: 'Reo.dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include low-code, API-platform, integration, developer-tools, and startup.


  The Reo.dev catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Reo.dev''s developer surface includes signup flow, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Reo.dev API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: reodev-rules
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 26.8
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Reodev Domain Security
  slug: reodev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: reodev
tags:
- low-code
- API-platform
- integration
- developer-tools
- startup
website: https://www.reo.dev
---
