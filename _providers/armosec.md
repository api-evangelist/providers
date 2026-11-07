---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
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
  score: 28.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Armosec Agentic Access
  operation_count: 53
  slug: armosec-agentic-access
  summary_line: 53 operations · 25 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: Jira and collaboration/notification integrations.
  name: ARMO Integrations API
  slug: armosec-integrations-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: KSPM posture and compliance framework results.
  name: ARMO Posture API
  slug: armosec-posture-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: Container registry scanning.
  name: ARMO Registry API
  slug: armosec-registry-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: Runtime incidents (CADR), network and runtime policies.
  name: ARMO Runtime API
  slug: armosec-runtime-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The AccessKeys API from ARMO — 2 operation(s) for accesskeys.
  name: ARMO Access Keys API
  slug: armosec-accesskeys-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The AlertChannel API from ARMO — 1 operation(s) for alertchannel.
  name: ARMO Alert Channel API
  slug: armosec-alertchannel-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The AttackChains API from ARMO — 1 operation(s) for attackchains.
  name: ARMO Attack Chains API
  slug: armosec-attackchains-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Collaboration API from ARMO — 4 operation(s) for collaboration.
  name: ARMO Collaboration API
  slug: armosec-collaboration-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Commands API from ARMO — 1 operation(s) for commands.
  name: ARMO Commands API
  slug: armosec-commands-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The CustomerState API from ARMO — 6 operation(s) for customerstate.
  name: ARMO Customer State API
  slug: armosec-customerstate-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The ECS API from ARMO — 2 operation(s) for ecs.
  name: ARMO ECS API
  slug: armosec-ecs-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Exception API from ARMO — 2 operation(s) for exception.
  name: ARMO Exception API
  slug: armosec-exception-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Features API from ARMO — 1 operation(s) for features.
  name: ARMO Features API
  slug: armosec-features-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Inventory API from ARMO — 2 operation(s) for inventory.
  name: ARMO Inventory API
  slug: armosec-inventory-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The JiraIntegration API from ARMO — 6 operation(s) for jiraintegration.
  name: ARMO Jira Integration API
  slug: armosec-jiraintegration-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The KubernetesAccounts API from ARMO — 1 operation(s) for kubernetesaccounts.
  name: ARMO Kubernetes Accounts API
  slug: armosec-kubernetesaccounts-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Login API from ARMO — 7 operation(s) for login.
  name: ARMO Login API
  slug: armosec-login-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Repository API from ARMO — 7 operation(s) for repository.
  name: ARMO Repository API
  slug: armosec-repository-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The RuntimePolicies API from ARMO — 2 operation(s) for runtimepolicies.
  name: ARMO Runtime Policies API
  slug: armosec-runtimepolicies-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Seccomp API from ARMO — 2 operation(s) for seccomp.
  name: ARMO Seccomp API
  slug: armosec-seccomp-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The SecurityRisks API from ARMO — 3 operation(s) for securityrisks.
  name: ARMO Security Risks API
  slug: armosec-securityrisks-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Sensors API from ARMO — 1 operation(s) for sensors.
  name: ARMO Sensors API
  slug: armosec-sensors-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The SIEMIntegrations API from ARMO — 1 operation(s) for siemintegrations.
  name: ARMO SIEM Integrations API
  slug: armosec-siemintegrations-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Tenants API from ARMO — 2 operation(s) for tenants.
  name: ARMO Tenants API
  slug: armosec-tenants-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Vulnerability API from ARMO — 10 operation(s) for vulnerability.
  name: ARMO Vulnerability API
  slug: armosec-vulnerability-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Workload API from ARMO — 1 operation(s) for workload.
  name: ARMO Workload API
  slug: armosec-workload-api
- baseURL: https://api.armosec.io/api/v1
  baseurl_source: declared
  description: The Network Policy API from ARMO — 2 operation(s) for network policy.
  name: ARMO Network Policy API
  slug: armosec-network-policy-api
artifact_total: 44
collections:
- collection_type: open
  name: ARMO Platform Access Keys API
  slug: open-armosec-access-keys-api
- collection_type: open
  name: ARMO Platform Access Keys Clusters API
  slug: open-armosec-clusters-api
- collection_type: open
  name: ARMO Platform Access Keys Integrations API
  slug: open-armosec-integrations-api
- collection_type: open
  name: ARMO Platform Access Keys Posture API
  slug: open-armosec-posture-api
- collection_type: open
  name: ARMO Platform Access Keys Registry API
  slug: open-armosec-registry-api
- collection_type: open
  name: ARMO Platform Access Keys Runtime API
  slug: open-armosec-runtime-api
- collection_type: open
  name: ARMO Platform Access Keys Security Risks API
  slug: open-armosec-security-risks-api
- collection_type: open
  name: ARMO Platform Access Keys Vulnerabilities API
  slug: open-armosec-vulnerabilities-api
- collection_type: open
  name: ARMO Platform API
  slug: open-armosec
common:
- group: other
  href: https://artifacts.apis.io/armosec/capabilities/armosec-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/armosec-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/armosec/agentic-access/armosec-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/armosec-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/armosec/security/armosec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/armosec-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/armosec/authentication/armosec-authentication.yml
  title: ''
  type: Authentication
  url: authentication/armosec-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/armosec
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/armosec
- group: company
  title: ''
  type: Website
  url: https://www.armosec.io/
- group: docs
  title: ''
  type: Documentation
  url: https://hub.armosec.io/docs/armo-platform
- group: commercial
  href: https://artifacts.apis.io/armosec/plans/armosec-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/armosec-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/armosec/rate-limits/armosec-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/armosec-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/armosec/finops/armosec-finops.yml
  title: ''
  type: FinOps
  url: finops/armosec-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.armosec.io/blog/
created: '2026-07-11'
description: ARMO is the cloud-native and Kubernetes security company behind the leading open-source project Kubescape. ARMO Platform is a runtime-driven CNAPP that unifies Kubernetes Security Posture Management (KSPM), vulnerability and image scanning, compliance frameworks, network and seccomp policy generation, and runtime Cloud Application Detection and Response (CADR) - correlating runtime behavior with posture and vulnerabilities to cut alert noise. ARMO exposes a documented REST API over HTTPS (base https://api.armosec.io/api/v1 in the EU region and https://api.us.armosec.io/api/v1 in the US region), authenticated with an account access key sent in the X-API-KEY header. The API covers clusters, workloads, vulnerabilities, posture and compliance, security risks, runtime incidents, attack chains, network and runtime policies, registry scanning, and integrations. API access is available to platform customers who have generated an Agent Access Key; the endpoints below are documented but
  the data returned requires a connected account and clusters.
finops:
- has_sources: true
  method: generated
  name: Armosec Finops
  primary_unit: ''
  service_category: Security
  slug: armosec-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/armosec.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.armosec.io over HTTP; 11 tools listed.
  name: ARMO MCP Server
  slug: armosec
modified: '2026-07-11'
name: ARMO
nav: Providers
network: true
overview: 'ARMO publishes 27 API contracts indexed on the [APIs.io](https://apis.io/) network, including Integrations API, Posture API, Registry API, and 24 more. Tagged areas include Kubernetes Security, Cloud Native Security, CNAPP, DevSecOps, and KSPM.


  The ARMO catalog on APIs.io includes 1 Spectral governance ruleset.


  ARMO''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Armosec Plans Pricing
  plan_count: 4
  slug: armosec-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Armosec Rate Limits
  slug: armosec-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: ARMO API Rules
  rule_count: 49
  severity_counts:
    error: 36
    hint: 0
    info: 3
    warn: 10
  slug: armosec-rules
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 47.6
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 10.5
  previous_composite: 26.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 75.0
      total: 36
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/armosec/armosec-2026-07-25T201225.png
security:
- kind: authentication
  name: Armosec Authentication
  slug: armosec-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Armosec Domain Security
  slug: armosec-domain-security
  summary_line: HSTS · DMARC
slug: armosec
tags:
- Kubernetes Security
- Cloud Native Security
- CNAPP
- DevSecOps
- KSPM
- Vulnerability Management
- Compliance
- Runtime Security
- CADR
- Kubescape
- Container Security
website: https://www.armosec.io/
---
