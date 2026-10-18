---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 81
  human_in_the_loop: 4
  name: Ubicloud Agentic Access
  operation_count: 132
  slug: ubicloud-agentic-access
  summary_line: 132 operations · 81 acting · 4 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Audit Log Operations
  name: Ubicloud Audit Log API
  slug: ubicloud-audit-log-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Firewall Operations
  name: Ubicloud Firewall API
  slug: ubicloud-firewall-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Firewall Rule Operations
  name: Ubicloud Firewall Rule API
  slug: ubicloud-firewall-rule-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: GitHub Operations
  name: Ubicloud GitHub API
  slug: ubicloud-github-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Inference API Key Operations
  name: Ubicloud Inference Api Key API
  slug: ubicloud-inference-api-key-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Inference Endpoint Operations
  name: Ubicloud Inference Endpoint API
  slug: ubicloud-inference-endpoint-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Kubernetes Cluster Operations
  name: Ubicloud Kubernetes Cluster API
  slug: ubicloud-kubernetes-cluster-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Load Balancer Operations
  name: Ubicloud Load Balancer API
  slug: ubicloud-load-balancer-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Machine Image Operations
  name: Ubicloud Machine Image API
  slug: ubicloud-machine-image-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Postgres Database Operations
  name: Ubicloud Postgres Database API
  slug: ubicloud-postgres-database-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Postgres Firewall Rule Operations
  name: Ubicloud Postgres Firewall Rule API
  slug: ubicloud-postgres-firewall-rule-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Postgres Log Destination
  name: Ubicloud Postgres Log Destination API
  slug: ubicloud-postgres-log-destination-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Postgres Metric Destination
  name: Ubicloud Postgres Metric Destination API
  slug: ubicloud-postgres-metric-destination-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Private Location Operations
  name: Ubicloud Private Location API
  slug: ubicloud-private-location-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Private Subnet Operations
  name: Ubicloud Private Subnet API
  slug: ubicloud-private-subnet-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Project Operations
  name: Ubicloud Project API
  slug: ubicloud-project-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: SSH Public Key Operations
  name: Ubicloud SSH Public Key API
  slug: ubicloud-ssh-public-key-api
- baseURL: https://api.ubicloud.com
  baseurl_source: declared
  description: Virtual Machine Operations
  name: Ubicloud Virtual Machine API
  slug: ubicloud-virtual-machine-api
artifact_total: 32
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/agentic-access/ubicloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ubicloud-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/plans/ubicloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ubicloud-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/rules/ubicloud-ubicloud-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/ubicloud-ubicloud-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/rules/ubicloud-rules.yml
  title: ''
  type: Spectral
  url: rules/ubicloud-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/json-ld/ubicloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ubicloud-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/vocabulary/ubicloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ubicloud-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/data-model/ubicloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ubicloud-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/cli/ubicloud-cli.yml
  title: ''
  type: CLI
  url: cli/ubicloud-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/changelog/ubicloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ubicloud-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/conventions/ubicloud-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ubicloud-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/conventions/ubicloud-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ubicloud-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/lifecycle/ubicloud-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ubicloud-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/lifecycle/ubicloud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ubicloud-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/errors/ubicloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ubicloud-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/conformance/ubicloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ubicloud-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/overlays/ubicloud-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ubicloud-openapi-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/hosts/ubicloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ubicloud-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/vendors/ubicloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ubicloud-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/packages/ubicloud-packages.yml
  title: ''
  type: SDKs
  url: packages/ubicloud-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/packages/ubicloud-packages.yml
  title: ''
  type: Packages
  url: packages/ubicloud-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/authentication/ubicloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ubicloud-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/security/ubicloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ubicloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ubicloud.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/ubicloud/ubicloud/blob/33a6864a3236158c3e5e59dffd35ead66a5bd1d7/openapi/.spectral.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.ubicloud.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://www.ubicloud.com/docs/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ubicloud.com/docs/machine-images/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.ubicloud.com/docs/about/support
- group: company
  title: ''
  type: Blog
  url: https://www.ubicloud.com/blog
- group: other
  title: ''
  type: RSSFeed
  url: https://www.ubicloud.com/rss/rss.xml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.ubicloud.com/docs/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ubicloud
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ubicloud/ubicloud
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ubicloud.com/docs/about/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.ubicloud.com/create-account
- group: start
  title: ''
  type: Login
  url: https://console.ubicloud.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ubicloud.com/docs/about/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ubicloud.com/docs/about/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ubicloud.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ubicloud.com
- group: company
  title: ''
  type: About
  url: https://www.ubicloud.com/about-ubicloud
- group: operate
  title: ''
  type: Contact
  url: https://www.ubicloud.com/contact-us
- group: other
  title: ''
  type: X
  url: https://twitter.com/UbicloudHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ubicloud/
created: '2026-10-09'
description: Ubicloud is an open source cloud that can run anywhere, positioned as an open source alternative to AWS. It provides cloud services such as compute (virtual machines), managed PostgreSQL, Kubernetes, GitHub Actions runners and machine images on bare metal providers like Hetzner, Leaseweb and AWS Bare Metal, offered as a managed service at console.ubicloud.com or self-hosted. It publishes an API reference and documentation at ubicloud.com/docs. Founded by Ozgun Erdogan, Umur Cubukcu and Daniel Farina.
image: https://cdn.prod.website-files.com/64f9d9b4e737e7b37d4e39a4/64fe41a59732cbbaa5762828_Webclip.png
json_schemas:
- name: FirewallRuleUpdate
  property_count: 0
  slug: ubicloud-firewall-rule-update
- name: PostgresCapabilities
  property_count: 2
  slug: ubicloud-postgres-capabilities
- name: PostgresConfig
  property_count: 4
  slug: ubicloud-postgres-config
- name: PostgresPatchConfig
  property_count: 0
  slug: ubicloud-postgres-patch-config
- name: SshPublicKey
  property_count: 3
  slug: ubicloud-ssh-public-key
- name: SshPublicKeyUpdate
  property_count: 0
  slug: ubicloud-ssh-public-key-update
jsonld:
- class_count: 37
  name: Ubicloud Context
  property_count: 111
  slug: ubicloud-context
layout: provider
modified: '2026-10-09'
name: Ubicloud
nav: Providers
network: true
overview: 'Ubicloud publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit Log API, Firewall API, Firewall Rule API, and 15 more. Tagged areas include Company, Cloud Computing, Open Source, Infrastructure-as-a-Service, and PostgreSQL.


  The Ubicloud catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ubicloud''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, support, and 38 more developer resources.'
plans:
- name: Ubicloud Plans Pricing
  plan_count: 13
  slug: ubicloud-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Ubicloud Rate Limits
  slug: ubicloud-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Ubicloud API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: ubicloud-rules
- authorship: provider
  effective_rule_count: 45
  extends:
  - spectral:oas
  name: Ubicloud — ubicloud rules
  rule_count: 4
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 0
  slug: ubicloud-ubicloud-spectral-rules
score:
  band: strong
  composite: 61.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 84.2
    contract_governance: 35.6
    contract_quality: 56.2
    developer_ergonomics: 63.7
    discoverability: 66.1
    operational_transparency: 44.7
  previous_composite: 63.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/ubicloud/refs/heads/main/screenshots/ubicloud-2026-10-11T131342.png
security:
- kind: authentication
  name: Ubicloud Authentication
  slug: ubicloud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ubicloud Domain Security
  slug: ubicloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ubicloud
tags:
- Company
- Cloud Computing
- Open Source
- Infrastructure-as-a-Service
- PostgreSQL
- Kubernetes
- Virtual Machines
- GitHub Actions
website: https://www.ubicloud.com/
---
