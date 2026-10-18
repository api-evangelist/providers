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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-17'
api_count: 12
apis:
- baseURL: https://api.cpln.io
  baseurl_source: declared
  description: The About API from ControlPlane — 1 operation(s) for about.
  name: ControlPlane About API
  slug: controlplane-about-api
- baseURL: https://api.cpln.io
  baseurl_source: declared
  description: The Artifacts API from ControlPlane — 1 operation(s) for artifacts.
  name: ControlPlane Artifacts API
  slug: controlplane-artifacts-api
- baseURL: https://api.cpln.io
  baseurl_source: declared
  description: The Audit API from ControlPlane — 1 operation(s) for audit.
  name: ControlPlane Audit API
  slug: controlplane-audit-api
- baseURL: https://api.cpln.io
  baseurl_source: declared
  description: The ControlPlane API API from ControlPlane — 1 operation(s) for controlplane api.
  name: ControlPlane ControlPlane API
  slug: controlplane-controlplane-api-api
- baseURL: https://api.cpln.io
  baseurl_source: declared
  description: The Docker API from ControlPlane — 1 operation(s) for docker.
  name: ControlPlane Docker API
  slug: controlplane-docker-api
- baseURL: https://api.cpln.io
  baseurl_source: declared
  description: The Health API from ControlPlane — 1 operation(s) for health.
  name: ControlPlane Health API
  slug: controlplane-health-api
- baseURL: https://api.cpln.io
  baseurl_source: declared
  description: The Helm API from ControlPlane — 1 operation(s) for helm.
  name: ControlPlane Helm API
  slug: controlplane-helm-api
- baseURL: https://api.cpln.io
  baseurl_source: declared
  description: The Org API from ControlPlane — 13 operation(s) for org.
  name: ControlPlane Org API
  slug: controlplane-org-api
- baseURL: https://api.cpln.io
  baseurl_source: declared
  description: The Quota Catalog API from ControlPlane — 1 operation(s) for quota catalog.
  name: ControlPlane Quota Catalog API
  slug: controlplane-quota-catalog-api
- baseURL: https://api.cpln.io
  baseurl_source: declared
  description: The Quota Increase Requests API from ControlPlane — 2 operation(s) for quota increase requests.
  name: ControlPlane Quota Increase Requests API
  slug: controlplane-quota-increase-requests-api
- baseURL: https://api.cpln.io
  baseurl_source: declared
  description: The Resources API from ControlPlane — 1 operation(s) for resources.
  name: ControlPlane Resources API
  slug: controlplane-resources-api
- baseURL: https://api.cpln.io
  baseurl_source: declared
  description: The Signups API from ControlPlane — 1 operation(s) for signups.
  name: ControlPlane Signups API
  slug: controlplane-signups-api
artifact_total: 23
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/rate-limits/controlplane-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/controlplane-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/rules/controlplane-rules.yml
  title: ''
  type: Spectral
  url: rules/controlplane-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/json-ld/controlplane-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/controlplane-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/vocabulary/controlplane-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/controlplane-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/data-model/controlplane-data-model.yml
  title: ''
  type: DataModel
  url: data-model/controlplane-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/changelog/controlplane-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/controlplane-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/authentication/controlplane-authentication.yml
  title: ''
  type: Authentication
  url: authentication/controlplane-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/conformance/controlplane-conformance.yml
  title: ''
  type: Conformance
  url: conformance/controlplane-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/llms/controlplane-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/controlplane-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/a2a/controlplane-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/controlplane-a2a.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/hosts/controlplane-hosts.yml
  title: ''
  type: Hosts
  url: hosts/controlplane-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/vendors/controlplane-vendors.yml
  title: ''
  type: Vendors
  url: vendors/controlplane-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://controlplane.com/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://controlplane.com/benefits/tenfold-enhancement/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://controlplane.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/controlplane-com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.controlplane.com/releases
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.controlplane.com\
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlplane/refs/heads/main/security/controlplane-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/controlplane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://controlplane.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.controlplane.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.controlplane.com/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://controlplane.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://controlplane.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://controlplane.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://controlplane.com/requestdemo
coverage:
  checked: '2026-10-10'
  detail: No OpenAPI or other machine-readable contract was found despite probing known API hosts and documentation pages.
  evidence:
  - status: error
    url: https://api.controlplane.com/openapi.json
  - status: 200
    url: https://console.cpln.io/openapi/core
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: ControlPlane provides a virtual cloud platform that unifies compute, networking, identity, and services across multiple clouds, bare metal, and on‑prem environments. It enables teams to build, ship, and scale applications with AI‑native automation, universal cloud identity, and zero‑ops operations, offering high availability and compliance features for enterprise workloads.
image: https://controlplane.com/opengraph-image?9bc49be7543d6542
json_schemas:
- name: GetQuotaCatalogResponse
  property_count: 10
  slug: controlplane-get-quota-catalog-response
- name: PatchOrgOrgAgentNameResponse
  property_count: 10
  slug: controlplane-patch-org-org-agent-name-response
- name: PostOrgMyOrgGvcMyGvcVolumesetMyVolumeSetCommandRequest
  property_count: 8
  slug: controlplane-post-org-my-org-gvc-my-gvc-volumeset-my-volume-set-command-request
- name: PostOrgMyOrgGvcMyGvcWorkloadWorkloadidCommandRequest
  property_count: 14
  slug: controlplane-post-org-my-org-gvc-my-gvc-workload-workloadid-command-request
- name: PostOrgMyOrgQuotaIncreaseRequestsResponse
  property_count: 10
  slug: controlplane-post-org-my-org-quota-increase-requests-response
- name: PostOrgOrgAgentResponse
  property_count: 10
  slug: controlplane-post-org-org-agent-response
jsonld:
- class_count: 15
  name: Controlplane Context
  property_count: 36
  slug: controlplane-context
layout: provider
modified: '2026-10-10'
name: ControlPlane
nav: Providers
network: true
overview: 'ControlPlane is listed with 12 APIs on the [APIs.io](https://apis.io/) network, including About API, Artifacts API, Audit API, and 9 more. Tagged areas include Company, Cloud, Virtualization, Artificial Intelligence, and DevOps.


  The ControlPlane catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ControlPlane''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 19 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 1
  name: Controlplane Rate Limits
  slug: controlplane-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ControlPlane API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: controlplane-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 25.6
    developer_ergonomics: 52.4
    discoverability: 78.6
    operational_transparency: 52.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Controlplane Authentication
  slug: controlplane-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Controlplane Domain Security
  slug: controlplane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: controlplane
tags:
- Company
- Cloud
- Virtualization
- Artificial Intelligence
- DevOps
website: https://controlplane.com/
---
