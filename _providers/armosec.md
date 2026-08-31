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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 39
  human_in_the_loop: 3
  name: Armosec Agentic Access
  operation_count: 53
  slug: armosec-agentic-access
  summary_line: 53 operations · 39 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: Account API access key management.
  name: ARMO Access Keys API
  slug: armosec-access-keys-api
- description: Connected clusters and workloads.
  name: ARMO Clusters API
  slug: armosec-clusters-api
- description: Jira and collaboration/notification integrations.
  name: ARMO Integrations API
  slug: armosec-integrations-api
- description: KSPM posture and compliance framework results.
  name: ARMO Posture API
  slug: armosec-posture-api
- description: Container registry scanning.
  name: ARMO Registry API
  slug: armosec-registry-api
- description: Runtime incidents (CADR), network and runtime policies.
  name: ARMO Runtime API
  slug: armosec-runtime-api
- description: Correlated security risks and attack chains.
  name: ARMO Security Risks API
  slug: armosec-security-risks-api
- description: Image and workload vulnerability scanning and results.
  name: ARMO Vulnerabilities API
  slug: armosec-vulnerabilities-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/armosec-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/armosec-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/armosec-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/armosec-rate-limits.yml
- group: commercial
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
- name: Armosec Finops
  service_category: Security
  slug: armosec-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/armosec.png
layout: provider
modified: '2026-07-11'
name: ARMO
nav: Providers
network: true
overview: 'ARMO publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Access Keys API, Clusters API, Integrations API, and 5 more. Tagged areas include Kubernetes Security, Cloud Native Security, CNAPP, DevSecOps, and KSPM.


  ARMO''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Armosec Plans Pricing
  plan_count: 4
  slug: armosec-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Armosec Rate Limits
  slug: armosec-rate-limits
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.3
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/armosec/refs/heads/main/screenshots/armosec-2026-07-25T201225.png
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
