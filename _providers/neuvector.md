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
  - '{''url'': ''https://neuvector.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.suse.com/products/rancher/security/ — a different registrable domain (neuvector.com -> suse.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Admission Control
  name: NeuVector Admission API
  slug: neuvector-admission-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Authenticates login or logout
  name: NeuVector Authentication API
  slug: neuvector-authentication-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Compliance
  name: NeuVector Compliance API
  slug: neuvector-compliance-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: The compliance profile. The payload body is the content of the compliance profile yaml file. API from NeuVector — 1 operation(s) for compliance profile. the payload body is the content of the complian
  name: NeuVector compliance profile. The payload body is the content of the compliance profile yaml file. API
  slug: neuvector-compliance-profile-the-payload-body-is-the-content-of-the-compliance-profile-yaml-file-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: The compliance profile. The payload body is the content of the vulnerability profile yaml file. API from NeuVector — 1 operation(s) for compliance profile. the payload body is the content of the vulne
  name: NeuVector compliance profile. The payload body is the content of the vulnerability profile yaml file. API
  slug: neuvector-compliance-profile-the-payload-body-is-the-content-of-the-vulnerability-profile-yaml-file-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Container
  name: NeuVector Container API
  slug: neuvector-container-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Controller
  name: NeuVector Controller API
  slug: neuvector-controller-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about DLP
  name: NeuVector DLP API
  slug: neuvector-dlp-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Enforcer
  name: NeuVector Enforcer API
  slug: neuvector-enforcer-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: End-User License Agreement
  name: NeuVector EULA API
  slug: neuvector-eula-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Federation
  name: NeuVector Federation API
  slug: neuvector-federation-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about File
  name: NeuVector File API
  slug: neuvector-file-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about File Monitor
  name: NeuVector File Monitor API
  slug: neuvector-file-monitor-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Group
  name: NeuVector Group API
  slug: neuvector-group-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Host
  name: NeuVector Host API
  slug: neuvector-host-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Log
  name: NeuVector Log API
  slug: neuvector-log-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Namespace
  name: NeuVector Namespace API
  slug: neuvector-namespace-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Policy
  name: NeuVector Policy API
  slug: neuvector-policy-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Process Profile
  name: NeuVector Process API
  slug: neuvector-process-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: The Remote Export Repository API from NeuVector — 1 operation(s) for remote export repository.
  name: NeuVector Remote Export Repository API
  slug: neuvector-remote-export-repository-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: The Remote Repository API from NeuVector — 2 operation(s) for remote repository.
  name: NeuVector Remote Repository API
  slug: neuvector-remote-repository-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Response Rule
  name: NeuVector Response Rule API
  slug: neuvector-response-rule-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Scan
  name: NeuVector Scan API
  slug: neuvector-scan-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Server
  name: NeuVector Server API
  slug: neuvector-server-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Service
  name: NeuVector Service API
  slug: neuvector-service-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Sniffer
  name: NeuVector Sniffer API
  slug: neuvector-sniffer-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about System
  name: NeuVector System API
  slug: neuvector-system-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about User
  name: NeuVector User API
  slug: neuvector-user-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about Vulnerability management
  name: NeuVector Vulnerability API
  slug: neuvector-vulnerability-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: Operations about waf Rule
  name: NeuVector WAF Rule API
  slug: neuvector-waf-rule-api
- baseURL: https://localhost:10443
  baseurl_source: declared
  description: The API Key API from NeuVector — 2 operation(s) for api key.
  name: NeuVector API Key API
  slug: neuvector-api-key-api
artifact_total: 67
collections:
- collection_type: open
  name: NeuVector Admission API
  slug: open-neuvector-admission-api
- collection_type: open
  name: NeuVector Apikey API
  slug: open-neuvector-apikey-api
- collection_type: open
  name: NeuVector Authentication API
  slug: open-neuvector-authentication-api
- collection_type: open
  name: NeuVector Compliance API
  slug: open-neuvector-compliance-api
- collection_type: open
  name: NeuVector compliance profile. The payload body is the content of the compliance profile yaml file. API
  slug: open-neuvector-compliance-profile-the-payload-body-is-the-content-of-the-compliance-profile-yaml-file-api
- collection_type: open
  name: NeuVector compliance profile. The payload body is the content of the vulnerability profile yaml file. API
  slug: open-neuvector-compliance-profile-the-payload-body-is-the-content-of-the-vulnerability-profile-yaml-file-api
- collection_type: open
  name: NeuVector Container API
  slug: open-neuvector-container-api
- collection_type: open
  name: NeuVector Controller API
  slug: open-neuvector-controller-api
- collection_type: open
  name: NeuVector DLP API
  slug: open-neuvector-dlp-api
- collection_type: open
  name: NeuVector Enforcer API
  slug: open-neuvector-enforcer-api
- collection_type: open
  name: NeuVector EULA API
  slug: open-neuvector-eula-api
- collection_type: open
  name: NeuVector Federation API
  slug: open-neuvector-federation-api
- collection_type: open
  name: NeuVector File API
  slug: open-neuvector-file-api
- collection_type: open
  name: NeuVector File Monitor API
  slug: open-neuvector-file-monitor-api
- collection_type: open
  name: NeuVector Group API
  slug: open-neuvector-group-api
- collection_type: open
  name: NeuVector Host API
  slug: open-neuvector-host-api
- collection_type: open
  name: NeuVector Log API
  slug: open-neuvector-log-api
- collection_type: open
  name: NeuVector Namespace API
  slug: open-neuvector-namespace-api
- collection_type: open
  name: NeuVector Policy API
  slug: open-neuvector-policy-api
- collection_type: open
  name: NeuVector Process API
  slug: open-neuvector-process-api
- collection_type: open
  name: NeuVector Remote Export Repository API
  slug: open-neuvector-remote-export-repository-api
- collection_type: open
  name: NeuVector Remote Repository API
  slug: open-neuvector-remote-repository-api
- collection_type: open
  name: NeuVector Response Rule API
  slug: open-neuvector-response-rule-api
- collection_type: open
  name: NeuVector Scan API
  slug: open-neuvector-scan-api
- collection_type: open
  name: NeuVector Server API
  slug: open-neuvector-server-api
- collection_type: open
  name: NeuVector Service API
  slug: open-neuvector-service-api
- collection_type: open
  name: NeuVector Sniffer API
  slug: open-neuvector-sniffer-api
- collection_type: open
  name: NeuVector System API
  slug: open-neuvector-system-api
- collection_type: open
  name: NeuVector User API
  slug: open-neuvector-user-api
- collection_type: open
  name: NeuVector Vulnerability API
  slug: open-neuvector-vulnerability-api
- collection_type: open
  name: NeuVector WAF Rule API
  slug: open-neuvector-waf-rule-api
common:
- group: commercial
  href: https://artifacts.apis.io/neuvector/plans/neuvector-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/neuvector-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/neuvector/rate-limits/neuvector-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/neuvector-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/neuvector/finops/neuvector-finops.yml
  title: ''
  type: FinOps
  url: finops/neuvector-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.suse.com/blog/
- group: other
  href: https://artifacts.apis.io/neuvector/capabilities/neuvector-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/neuvector-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/neuvector/security/neuvector-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/neuvector-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neuvector
- group: company
  title: ''
  type: Website
  url: https://neuvector.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open-docs.neuvector.com/
- group: docs
  title: ''
  type: SUSE Documentation
  url: https://documentation.suse.com/en-us/cloudnative/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neuvector
- group: other
  title: ''
  type: SUSE Product Page
  url: https://www.suse.com/products/neuvector/
created: '2026-03-26'
description: NeuVector is an open source, full lifecycle container security platform maintained by SUSE. It provides vulnerability scanning, runtime protection, compliance monitoring, and a Layer 7 container firewall for Kubernetes environments. The NeuVector REST API allows automation of scanning, policy management, configuration, user administration, and federated cluster operations.
finops:
- has_sources: false
  method: generated
  name: Neuvector Finops
  primary_unit: request
  service_category: API
  slug: neuvector-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neuvector.png
layout: provider
modified: '2026-10-06'
name: NeuVector
nav: Providers
network: true
overview: 'NeuVector publishes 31 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admission API, Authentication API, Compliance API, and 28 more. Tagged areas include Compliance, Containers, Kubernetes, Open Source, and Runtime Protection.


  The NeuVector catalog on APIs.io includes 1 Spectral governance ruleset.


  NeuVector''s developer surface includes engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Neuvector Plans Pricing
  plan_count: 3
  slug: neuvector-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Neuvector Rate Limits
  slug: neuvector-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: NeuVector API Rules
  rule_count: 60
  severity_counts:
    error: 45
    hint: 0
    info: 3
    warn: 12
  slug: neuvector-rules
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 41.1
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 24.7
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 31
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/neuvector/neuvector-2026-06-20T190220.png
security:
- kind: domain-security
  name: Neuvector Domain Security
  slug: neuvector-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: neuvector
tags:
- Compliance
- Containers
- Kubernetes
- Open Source
- Runtime Protection
- Security
- Vulnerability Scanning
website: https://neuvector.com/
---
