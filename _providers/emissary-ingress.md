---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://www.getambassador.io/products/api-gateway'', ''status'': 301, ''note'': ''declared website redirects to https://landing.gravitee.io/gravitee-edge-stack-unified-api-visibility-and-governance — a different registrable domain (getambassador.io -> gravitee.io), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Emissary Ingress Agentic Access
  operation_count: 20
  slug: emissary-ingress-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 1
apis:
- description: Emissary-Ingress supports a subset of the Kubernetes Gateway API standard, including GatewayClass, Gateway, and HTTPRoute resources. This enables teams to use the next-generation Kubernetes ingress st
  name: Emissary-Ingress Gateway API
  slug: emissary-ingress-gateway-api
- baseURL_template: https://{kubernetes-api-server}
  baseurl_source: spec_template
  description: Operations for managing AuthService custom resources that configure external authentication and authorization services. Emissary-Ingress will call the configured auth service before forwarding request
  name: Emissary-Ingress AuthService API
  slug: emissary-ingress-authservice-api
- baseURL_template: https://{kubernetes-api-server}
  baseurl_source: spec_template
  description: Operations for managing Host custom resources that configure domain names, TLS certificate management via ACME/Let's Encrypt, and TLS termination for ingress traffic. A Host binds a hostname to TLS co
  name: Emissary-Ingress Host API
  slug: emissary-ingress-host-api
- baseURL_template: https://{kubernetes-api-server}
  baseurl_source: spec_template
  description: Operations for managing Mapping custom resources that define routing rules for inbound HTTP/HTTPS traffic. A Mapping connects a URL path or prefix to a backend Kubernetes service with support for head
  name: Emissary-Ingress Mapping API
  slug: emissary-ingress-mapping-api
- baseURL_template: https://{kubernetes-api-server}
  baseurl_source: spec_template
  description: Operations for managing RateLimitService custom resources that configure integration with external rate limiting services compatible with the Envoy rate limit API.
  name: Emissary-Ingress RateLimitService API
  slug: emissary-ingress-ratelimitservice-api
- baseURL_template: https://{kubernetes-api-server}
  baseurl_source: spec_template
  description: Operations for managing TLSContext custom resources that define reusable TLS configuration including certificates, cipher suites, minimum protocol versions, and client certificate validation settings.
  name: Emissary-Ingress TLSContext API
  slug: emissary-ingress-tlscontext-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Emissary-Ingress Configuration AuthService API
  slug: open-emissary-ingress-authservice-api
- collection_type: open
  name: Emissary-Ingress Configuration AuthService Host API
  slug: open-emissary-ingress-host-api
- collection_type: open
  name: Emissary-Ingress Configuration AuthService Mapping API
  slug: open-emissary-ingress-mapping-api
- collection_type: open
  name: Emissary-Ingress Configuration AuthService RateLimitService API
  slug: open-emissary-ingress-ratelimitservice-api
- collection_type: open
  name: Emissary-Ingress Configuration AuthService TLSContext API
  slug: open-emissary-ingress-tlscontext-api
- collection_type: open
  name: Emissary-Ingress Configuration API
  slug: open-emissary-ingress
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/emissary-ingress/emissary/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/emissary-ingress/emissary/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/emissary-ingress/emissary/blob/main/LICENSE
- group: other
  title: ''
  type: ParentCompany
  url: https://www.gravitee.io/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/emissary-ingress-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emissary-ingress-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getambassador.io/products/api-gateway
- group: docs
  title: ''
  type: Documentation
  url: https://www.getambassador.io/docs/emissary/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.getambassador.io/docs/emissary/latest/topics/install/yaml-install
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emissary-ingress
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/emissary-ingress/emissary
- group: operate
  title: ''
  type: Support
  url: https://www.getambassador.io/docs/emissary/latest/about/support
- group: operate
  title: ''
  type: Community
  url: https://emissary-ingress.dev/docs/4.0/community/
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/emissary-ingress/emissary/issues
- group: company
  title: ''
  type: Blog
  url: https://blog.getambassador.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://archive.getambassador.io/docs/emissary/3.1/release-notes/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/emissary-ingress-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/emissary-ingress-mapping-schema.json
created: '2026-03-16'
description: Emissary-Ingress is a CNCF incubating Kubernetes-native API gateway built on the Envoy proxy. It provides ingress control, load balancing, authentication, rate limiting, and traffic management for microservices. Emissary-Ingress is configured through Kubernetes custom resources and supports canary releases, circuit breaking, and automatic retries.
finops:
- name: Emissary Ingress Finops
  service_category: API
  slug: emissary-ingress-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emissary-ingress.png
json_schemas:
- name: Emissary-Ingress Mapping
  property_count: 5
  slug: emissary-ingress-mapping
jsonld:
- class_count: 0
  name: Emissary Ingress Context
  property_count: 10
  slug: emissary-ingress-context
layout: provider
modified: '2026-05-19'
name: Emissary-Ingress
nav: Providers
network: true
overview: 'Emissary-Ingress publishes 5 APIs on the [APIs.io](https://apis.io/) network, including AuthService API, Host API, Mapping API, and 2 more. Tagged areas include API Gateway, Cloud-Native, Envoy, Incubating, and Ingress.


  The Emissary-Ingress catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Emissary-Ingress'' developer surface includes documentation, getting-started guide, support, engineering blog, changelog, and 13 more developer resources.'
plans:
- name: Emissary Ingress Plans Pricing
  plan_count: 3
  slug: emissary-ingress-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Emissary Ingress Rate Limits
  slug: emissary-ingress-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Emissary-Ingress API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: emissary-ingress-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 58.3
    catalog_earned_first_party: 0.0
    catalog_gap: 56.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 59.3
    developer_ergonomics: 20.2
    discoverability: 66.7
    governance: 9.8
    operational_transparency: 10.5
  open_source:
    applies: true
    score: 50.0
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emissary-ingress/refs/heads/main/screenshots/emissary-ingress-2026-06-20T180636.png
security:
- kind: domain-security
  name: Emissary Ingress Domain Security
  slug: emissary-ingress-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: emissary-ingress
tags:
- API Gateway
- Cloud-Native
- Envoy
- Incubating
- Ingress
- Kubernetes
website: https://www.getambassador.io/products/api-gateway
---
