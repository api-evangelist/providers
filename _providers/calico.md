---
access_model:
  confidence: medium
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Calico Agentic Access
  operation_count: 28
  slug: calico-agentic-access
  summary_line: 28 operations · 14 acting
api_count: 1
apis:
- description: 'The Calico Client Library provides programmatic access to manage Calico resources such as network policies, IP pools, BGP configuration, host and workload endpoints, and IPAM settings. It is the core '
  name: Calico Client API
  slug: calico-client-api
- description: calicoctl is the command-line tool that enables operators and automation systems to create, read, update, and delete Calico resources such as policies, IP pools, BGP peers, host endpoints, and workloa
  name: calicoctl CLI
  slug: calicoctl-cli
- description: Calico exposes its networking and security primitives through Kubernetes Custom Resource Definitions (CRDs) including NetworkPolicy, GlobalNetworkPolicy, IPPool, BGPConfiguration, BGPPeer, HostEndpoin
  name: Calico Kubernetes CRDs
  slug: calico-kubernetes-crds
- baseURL_template: https://{kube_apiserver_host}/apis/projectcalico.org/v3
  baseurl_source: spec_template
  description: The BGPConfiguration API from Calico — 2 operation(s) for bgpconfiguration.
  name: Calico BGPConfiguration API
  slug: calico-bgpconfiguration-api
- baseURL_template: https://{kube_apiserver_host}/apis/projectcalico.org/v3
  baseurl_source: spec_template
  description: The BGPPeer API from Calico — 2 operation(s) for bgppeer.
  name: Calico BGPPeer API
  slug: calico-bgppeer-api
- baseURL_template: https://{kube_apiserver_host}/apis/projectcalico.org/v3
  baseurl_source: spec_template
  description: The GlobalNetworkPolicy API from Calico — 2 operation(s) for globalnetworkpolicy.
  name: Calico GlobalNetworkPolicy API
  slug: calico-globalnetworkpolicy-api
- baseURL_template: https://{kube_apiserver_host}/apis/projectcalico.org/v3
  baseurl_source: spec_template
  description: The HostEndpoint API from Calico — 2 operation(s) for hostendpoint.
  name: Calico HostEndpoint API
  slug: calico-hostendpoint-api
- baseURL_template: https://{kube_apiserver_host}/apis/projectcalico.org/v3
  baseurl_source: spec_template
  description: The IPPool API from Calico — 2 operation(s) for ippool.
  name: Calico IPPool API
  slug: calico-ippool-api
- baseURL_template: https://{kube_apiserver_host}/apis/projectcalico.org/v3
  baseurl_source: spec_template
  description: The NetworkPolicy API from Calico — 2 operation(s) for networkpolicy.
  name: Calico NetworkPolicy API
  slug: calico-networkpolicy-api
- baseURL_template: https://{kube_apiserver_host}/apis/projectcalico.org/v3
  baseurl_source: spec_template
  description: The Profile API from Calico — 2 operation(s) for profile.
  name: Calico Profile API
  slug: calico-profile-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Project Calico API (projectcalico.org/v3) BGPConfiguration API
  slug: open-calico-bgpconfiguration-api
- collection_type: open
  name: Project Calico API (projectcalico.org/v3) BGPConfiguration BGPPeer API
  slug: open-calico-bgppeer-api
- collection_type: open
  name: Project Calico API (projectcalico.org/v3) BGPConfiguration GlobalNetworkPolicy API
  slug: open-calico-globalnetworkpolicy-api
- collection_type: open
  name: Project Calico API (projectcalico.org/v3) BGPConfiguration HostEndpoint API
  slug: open-calico-hostendpoint-api
- collection_type: open
  name: Project Calico API (projectcalico.org/v3) BGPConfiguration IPPool API
  slug: open-calico-ippool-api
- collection_type: open
  name: Project Calico API (projectcalico.org/v3) BGPConfiguration NetworkPolicy API
  slug: open-calico-networkpolicy-api
- collection_type: open
  name: Project Calico API (projectcalico.org/v3) BGPConfiguration Profile API
  slug: open-calico-profile-api
- collection_type: open
  name: Project Calico API (projectcalico.org/v3)
  slug: open-calico
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/projectcalico/calico/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/projectcalico/calico/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/projectcalico/calico/blob/master/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/projectcalico/calico/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/projectcalico/calico/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/calico-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/calico-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calico-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/calico-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/calico-life-sciences-llc
- group: company
  title: ''
  type: Website
  url: https://www.tigera.io/project-calico/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tigera.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tigera.io/calico/latest/getting-started/kubernetes/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/projectcalico
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/projectcalico/calico
- group: company
  title: ''
  type: Blog
  url: https://www.tigera.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tigera.io/tigera-products/calico/
- group: operate
  title: ''
  type: Slack
  url: https://slack.projectcalico.org/
- group: learn
  title: ''
  type: Training
  url: https://www.tigera.io/interactive-training/
- group: auth
  title: ''
  type: Certification
  url: https://www.tigera.io/lp/calico-certification/
created: '2026-03-26'
description: Calico is an open source networking and network security solution for containers, virtual machines, and native host-based workloads. Created and maintained by Tigera, it is the most widely adopted solution for container networking and security, powering over 8 million nodes daily across 166 countries.
finops:
- name: Calico Finops
  service_category: API
  slug: calico-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/calico.png
layout: provider
modified: '2026-04-23'
name: Calico
nav: Providers
network: true
overview: 'Calico publishes 7 APIs on the [APIs.io](https://apis.io/) network, including BGPConfiguration API, BGPPeer API, GlobalNetworkPolicy API, and 4 more. Tagged areas include CNI, Containers, eBPF, Kubernetes, and Network Policy.


  Calico''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, training material, and 14 more developer resources.'
plans:
- name: Calico Plans Pricing
  plan_count: 3
  slug: calico-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Calico Rate Limits
  slug: calico-rate-limits
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 51.9
    developer_ergonomics: 40.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 85.0
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 27.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/calico/refs/heads/main/screenshots/calico-2026-06-20T173846.png
security:
- kind: authentication
  name: Calico Authentication
  slug: calico-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Calico Domain Security
  slug: calico-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Calico Vulnerability Disclosure
  slug: calico-vulnerability-disclosure
  summary_line: disclosure policy published
slug: calico
tags:
- CNI
- Containers
- eBPF
- Kubernetes
- Network Policy
- Network Security
- Networking
- Open-Source
- Service Mesh
website: https://www.tigera.io/project-calico/
---
