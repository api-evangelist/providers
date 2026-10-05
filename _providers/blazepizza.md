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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-10-04'
api_count: 5
apis:
- baseURL: https://your-worker.dev
  baseurl_source: declared
  description: The Blazepizza API API from Blazepizza — 1 operation(s) for blazepizza api.
  name: Blazepizza Blazepizza API
  slug: blazepizza-blazepizza-api-api
- baseURL: https://your-worker.dev
  baseurl_source: declared
  description: The Cat Pic API from Blazepizza — 1 operation(s) for cat pic.
  name: Blazepizza Cat Pic API
  slug: blazepizza-cat-pic-api
- baseURL: https://your-worker.dev
  baseurl_source: declared
  description: The Foo API from Blazepizza — 1 operation(s) for foo.
  name: Blazepizza Foo API
  slug: blazepizza-foo-api
- baseURL: https://your-worker.dev
  baseurl_source: declared
  description: The Http API from Blazepizza — 1 operation(s) for http.
  name: Blazepizza HTTP API
  slug: blazepizza-http-api
- baseURL: https://your-worker.dev
  baseurl_source: declared
  description: The Image API from Blazepizza — 1 operation(s) for image.
  name: Blazepizza Image API
  slug: blazepizza-image-api
artifact_total: 11
asyncapis:
- description: ''
  name: Blazepizza Webhooks
  slug: blazepizza-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/rules/blazepizza-rules.yml
  title: ''
  type: Spectral
  url: rules/blazepizza-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/json-ld/blazepizza-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blazepizza-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/vocabulary/blazepizza-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blazepizza-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/asyncapi/blazepizza-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/blazepizza-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/data-model/blazepizza-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blazepizza-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/changelog/blazepizza-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blazepizza-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/sandbox/blazepizza-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/blazepizza-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/authentication/blazepizza-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blazepizza-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/conformance/blazepizza-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blazepizza-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/a2a/blazepizza-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/blazepizza-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/well-known/blazepizza-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blazepizza-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/hosts/blazepizza-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blazepizza-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/vendors/blazepizza-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blazepizza-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thanx.com/consumer/best-practices/onboarding-authentication
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blazepizza/refs/heads/main/security/blazepizza-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blazepizza-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blazepizza.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.blazepizza.com/about-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://order.thanx.com/blazepizza
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blazepizza.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blazepizza.com/marketing-terms-conditions
- group: operate
  title: ''
  type: Contact
  url: https://www.blazepizza.com/contact
coverage:
  checked: '2026-09-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found in the markdown documentation.
  evidence:
  - status: 200
    url: https://docs.thanx.com/overview/api_collections.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: Blaze Pizza is a fast‑casual pizza chain founded in 2011 in Pasadena, California. It offers customizable artisan‑style pizzas made to order with a 24‑hour fermented dough, plus salads, desserts, drinks, and vegan options. The brand operates hundreds of locations across the United States and internationally, emphasizing quick service, fresh ingredients, and a modern digital ordering experience through its website and mobile apps. Blaze Pizza also provides franchising opportunities and community initiatives such as the Folds of Honor fundraisers.
json_schemas:
- name: GetResponse
  property_count: 6
  slug: blazepizza-get-response
jsonld:
- class_count: 1
  name: Blazepizza Context
  property_count: 6
  slug: blazepizza-context
layout: provider
modified: '2026-09-29'
name: Blazepizza
nav: Providers
network: true
overview: 'Blazepizza publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Blazepizza API, Cat Pic API, Foo API, and 2 more. Tagged areas include Company, Fast Casual, Pizza, Restaurant, and Franchise.


  The Blazepizza catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Blazepizza''s developer surface includes changelog, sandbox, authentication, getting-started guide, documentation, and 16 more developer resources.'
random_paper: 6
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Blazepizza API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: blazepizza-rules
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.2
    catalog_earned_first_party: 0.0
    catalog_gap: 60.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 25.6
    developer_ergonomics: 50.0
    discoverability: 67.9
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Blazepizza Authentication
  slug: blazepizza-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Blazepizza Domain Security
  slug: blazepizza-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blazepizza
tags:
- Company
- Fast Casual
- Pizza
- Restaurant
- Franchise
website: https://www.blazepizza.com
---
