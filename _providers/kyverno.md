---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kyverno Agentic Access
  operation_count: 13
  slug: kyverno-agentic-access
  summary_line: 13 operations
api_count: 1
apis:
- description: Kyverno is a Kubernetes-native policy engine that runs as a dynamic admission controller to validate, mutate, and generate Kubernetes resources using policies written as Kubernetes resources. It suppo
  name: Kyverno
  slug: kyverno
- description: The Kyverno CLI provides a command-line interface for applying and testing Kyverno policies against Kubernetes resources outside of a cluster. It can be used in CI/CD pipelines to validate resources b
  name: Kyverno CLI
  slug: kyverno-cli
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Cluster-scoped policy report endpoints
  name: Kyverno ClusterPolicyReports API
  slug: kyverno-clusterpolicyreports-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Health and readiness endpoints
  name: Kyverno Health API
  slug: kyverno-health-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Namespace listing endpoints
  name: Kyverno Namespaces API
  slug: kyverno-namespaces-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Policy listing and detail endpoints
  name: Kyverno Policies API
  slug: kyverno-policies-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Policy result query endpoints
  name: Kyverno Results API
  slug: kyverno-results-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Policy source listing endpoints
  name: Kyverno Sources API
  slug: kyverno-sources-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Namespaced policy report endpoints
  name: Kyverno Policy Reports API
  slug: kyverno-policy-reports-api
artifact_total: 25
collections:
- collection_type: open
  name: Kyverno Policy Reporter ClusterPolicyReports API
  slug: open-kyverno-clusterpolicyreports-api
- collection_type: open
  name: Kyverno Policy Reporter ClusterPolicyReports Health API
  slug: open-kyverno-health-api
- collection_type: open
  name: Kyverno Policy Reporter ClusterPolicyReports Namespaces API
  slug: open-kyverno-namespaces-api
- collection_type: open
  name: Kyverno Policy Reporter ClusterPolicyReports Policies API
  slug: open-kyverno-policies-api
- collection_type: open
  name: Kyverno Policy Reporter API
  slug: open-kyverno-policy-reporter
- collection_type: open
  name: Kyverno Policy Reporter ClusterPolicyReports PolicyReports API
  slug: open-kyverno-policyreports-api
- collection_type: open
  name: Kyverno Policy Reporter ClusterPolicyReports Results API
  slug: open-kyverno-results-api
- collection_type: open
  name: Kyverno Policy Reporter ClusterPolicyReports Sources API
  slug: open-kyverno-sources-api
common:
- group: commercial
  href: https://artifacts.apis.io/kyverno/plans/kyverno-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kyverno-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kyverno/rate-limits/kyverno-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kyverno-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kyverno/finops/kyverno-finops.yml
  title: ''
  type: FinOps
  url: finops/kyverno-finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/kyverno/kyverno/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/kyverno/kyverno/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/kyverno/kyverno/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/kyverno/kyverno/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/kyverno/kyverno/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/kyverno/kyverno/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/kyverno/agentic-access/kyverno-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kyverno-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kyverno/security/kyverno-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kyverno-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nirmata
- group: company
  title: ''
  type: Website
  url: https://kyverno.io/
- group: docs
  title: ''
  type: Documentation
  url: https://kyverno.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://kyverno.io/docs/installation/
- group: operate
  title: ''
  type: ChangeLog
  url: https://kyverno.io/docs/releases/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kyverno
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kyverno/kyverno
- group: company
  title: ''
  type: Blog
  url: https://kyverno.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://kyverno.io/community/
- group: docs
  href: https://artifacts.apis.io/kyverno/json-schema/kyverno-policy-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/kyverno-policy-schema.json
- group: design
  href: https://artifacts.apis.io/kyverno/json-ld/kyverno-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kyverno-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://kyverno.io/llms.txt
created: '2025-01-01'
description: Kyverno is a Kubernetes native policy management engine for security, automation, and governance. It uses Kubernetes admission controllers to validate, mutate, and generate configurations using policies written as Kubernetes resources.
finops:
- has_sources: false
  method: generated
  name: Kyverno Finops
  primary_unit: request
  service_category: API
  slug: kyverno-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kyverno.png
json_schemas:
- name: Kyverno Policy
  property_count: 5
  slug: kyverno-policy
jsonld:
- class_count: 11
  name: Kyverno Context
  property_count: 47
  slug: kyverno-context
layout: provider
modified: '2026-05-19'
name: Kyverno
nav: Providers
network: true
overview: 'Kyverno publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including ClusterPolicyReports API, Health API, Namespaces API, and 6 more. Tagged areas include Cloud-Native, Governance, Kubernetes, Policy Management, and Security.


  The Kyverno catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kyverno''s developer surface includes documentation, getting-started guide, changelog, engineering blog, and 19 more developer resources.'
plans:
- name: Kyverno Plans Pricing
  plan_count: 3
  slug: kyverno-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Kyverno Rate Limits
  slug: kyverno-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Kyverno — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: kyverno-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 52.3
    catalog_earned_first_party: 0.0
    catalog_gap: 62.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 9.8
    contract_quality: 48.8
    developer_ergonomics: 33.3
    discoverability: 64.3
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/kyverno/kyverno-2026-06-20T184228.png
security:
- kind: domain-security
  name: Kyverno Domain Security
  slug: kyverno-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kyverno
tags:
- Cloud-Native
- Governance
- Kubernetes
- Policy Management
- Security
website: https://kyverno.io/
---
