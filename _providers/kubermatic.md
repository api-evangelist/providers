---
agent_readiness:
  band: agent-aware
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-04'
api_count: 9
apis:
- baseURL: https://github.com
  baseurl_source: declared
  description: The Apis API from Kubermatic — 1 operation(s) for apis.
  name: Kubermatic APIs API
  slug: kubermatic-apis-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Auth API from Kubermatic — 1 operation(s) for auth.
  name: Kubermatic Auth API
  slug: kubermatic-auth-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Clusters API from Kubermatic — 5 operation(s) for clusters.
  name: Kubermatic Clusters API
  slug: kubermatic-clusters-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Healthz API from Kubermatic — 1 operation(s) for healthz.
  name: Kubermatic Healthz API
  slug: kubermatic-healthz-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Kubermatic API API from Kubermatic — 1 operation(s) for kubermatic api.
  name: Kubermatic Kubermatic API
  slug: kubermatic-kubermatic-api-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Kubermatic API from Kubermatic — 2 operation(s) for kubermatic.
  name: Kubermatic Kubermatic API
  slug: kubermatic-kubermatic-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Mcp API from Kubermatic — 1 operation(s) for mcp.
  name: Kubermatic MCP API
  slug: kubermatic-mcp-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Metrics API from Kubermatic — 1 operation(s) for metrics.
  name: Kubermatic Metrics API
  slug: kubermatic-metrics-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The .well Known API from Kubermatic — 1 operation(s) for .well known.
  name: Kubermatic .well Known API
  slug: kubermatic-well-known-api
artifact_total: 18
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kubermatic/refs/heads/main/rules/kubermatic-rules.yml
  title: ''
  type: Spectral
  url: rules/kubermatic-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kubermatic/refs/heads/main/json-ld/kubermatic-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kubermatic-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kubermatic/refs/heads/main/vocabulary/kubermatic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kubermatic-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kubermatic/refs/heads/main/data-model/kubermatic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kubermatic-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kubermatic/refs/heads/main/conformance/kubermatic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kubermatic-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kubermatic/refs/heads/main/llms/kubermatic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kubermatic-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kubermatic/refs/heads/main/hosts/kubermatic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kubermatic-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kubermatic/refs/heads/main/vendors/kubermatic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kubermatic-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.kubermatic.com/tags/security/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kubermatic.com/secureguard/main/getting-started/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kubermatic/refs/heads/main/security/kubermatic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kubermatic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kubermatic.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kubermatic.com
- group: company
  title: ''
  type: Blog
  url: https://www.kubermatic.com/blog
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL files were found on the provider's documentation or API hosts.
  evidence:
  - status: 200
    url: https://docs.kubermatic.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Kubermatic provides a multi‑cloud Kubernetes management platform that enables enterprises to deploy, operate, and scale Kubernetes clusters across any infrastructure—public clouds, on‑premises data centers, and edge environments. The solution includes automated provisioning, lifecycle management, security controls, and integrated AI‑driven optimization for workloads. Kubermatic is recognized in the 2026 Gartner Magic Quadrant for Container Management and offers products such as Kubermatic Kubernetes Platform, Kubermatic AI, KubeLB, and SecureGuard.
image: https://www.kubermatic.com/images/Kubermatic-share.jpg
json_schemas:
- name: DeleteApiClustersIdResponse
  property_count: 1
  slug: kubermatic-delete-api-clusters-id-response
- name: GetApiClustersIdHealthResponse
  property_count: 2
  slug: kubermatic-get-api-clusters-id-health-response
- name: GetApiClustersResponse
  property_count: 3
  slug: kubermatic-get-api-clusters-response
- name: PostApiClustersKubeconfigRequest
  property_count: 3
  slug: kubermatic-post-api-clusters-kubeconfig-request
- name: PostApiClustersKubeconfigResponse
  property_count: 2
  slug: kubermatic-post-api-clusters-kubeconfig-response
- name: PostResponse
  property_count: 3
  slug: kubermatic-post-response
jsonld:
- class_count: 7
  name: Kubermatic Context
  property_count: 12
  slug: kubermatic-context
layout: provider
modified: '2026-10-03'
name: Kubermatic
nav: Providers
network: true
overview: 'Kubermatic publishes 9 APIs on the [APIs.io](https://apis.io/) network, including APIs API, Auth API, Clusters API, and 6 more. Tagged areas include Company, Kubernetes, Multi-Cloud, Platform, and Artificial Intelligence.


  The Kubermatic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kubermatic''s developer surface includes getting-started guide, documentation, engineering blog, and 11 more developer resources.'
random_paper: 7
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Kubermatic API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 1
  slug: kubermatic-rules
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.0
    developer_ergonomics: 23.8
    discoverability: 78.6
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Kubermatic Domain Security
  slug: kubermatic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kubermatic
tags:
- Company
- Kubernetes
- Multi-Cloud
- Platform
- Artificial Intelligence
website: https://www.kubermatic.com
---
