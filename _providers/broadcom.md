---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
- acting_count: 22
  human_in_the_loop: 1
  name: Broadcom Agentic Access
  operation_count: 51
  slug: broadcom-agentic-access
  summary_line: 51 operations · 22 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL_template: https://{instance}.wavefront.com/api/v2
  baseurl_source: spec_template
  description: Alert management
  name: Broadcom Alerts API
  slug: broadcom-alerts-api
- baseURL_template: https://{instance}.wavefront.com/api/v2
  baseurl_source: spec_template
  description: API token management
  name: Broadcom API Tokens API
  slug: broadcom-api-tokens-api
- baseURL_template: https://{sddc-manager}/v1
  baseurl_source: spec_template
  description: Token-based authentication
  name: Broadcom Authentication API
  slug: broadcom-authentication-api
- baseURL_template: https://{sddc-manager}/v1
  baseurl_source: spec_template
  description: Cluster management
  name: Broadcom Clusters API
  slug: broadcom-clusters-api
- baseURL_template: https://{vcenter}/api
  baseurl_source: spec_template
  description: Content library management
  name: Broadcom Content Library API
  slug: broadcom-content-library-api
- baseURL_template: https://{instance}.wavefront.com/api/v2
  baseurl_source: spec_template
  description: Dashboard management
  name: Broadcom Dashboards API
  slug: broadcom-dashboards-api
- baseURL_template: https://{vcenter}/api
  baseurl_source: spec_template
  description: Operations for managing datastores
  name: Broadcom Datastores API
  slug: broadcom-datastores-api
- baseURL_template: https://{instance}.wavefront.com/api/v2
  baseurl_source: spec_template
  description: Event management
  name: Broadcom Events API
  slug: broadcom-events-api
- baseURL_template: https://{sddc-manager}/v1
  baseurl_source: spec_template
  description: ESXi host management
  name: Broadcom Hosts API
  slug: broadcom-hosts-api
- baseURL_template: https://{sddc-manager}/v1
  baseurl_source: spec_template
  description: Network pool management
  name: Broadcom Network Pools API
  slug: broadcom-network-pools-api
- baseURL_template: https://{vcenter}/api
  baseurl_source: spec_template
  description: Operations for managing networks
  name: Broadcom Networks API
  slug: broadcom-networks-api
- baseURL_template: https://{instance}.wavefront.com/api/v2
  baseurl_source: spec_template
  description: Proxy management
  name: Broadcom Proxies API
  slug: broadcom-proxies-api
- baseURL_template: https://{instance}.wavefront.com/api/v2
  baseurl_source: spec_template
  description: Query metrics data
  name: Broadcom Query API
  slug: broadcom-query-api
- baseURL_template: https://{vcenter}/api
  baseurl_source: spec_template
  description: Session management operations
  name: Broadcom Session API
  slug: broadcom-session-api
- baseURL_template: https://{instance}.wavefront.com/api/v2
  baseurl_source: spec_template
  description: Source management
  name: Broadcom Sources API
  slug: broadcom-sources-api
- baseURL_template: https://{vcenter}/api
  baseurl_source: spec_template
  description: Tag management and association operations
  name: Broadcom Tagging API
  slug: broadcom-tagging-api
- baseURL_template: https://{sddc-manager}/v1
  baseurl_source: spec_template
  description: Asynchronous task monitoring
  name: Broadcom Tasks API
  slug: broadcom-tasks-api
- baseURL_template: https://{sddc-manager}/v1
  baseurl_source: spec_template
  description: System upgrade management
  name: Broadcom Upgrades API
  slug: broadcom-upgrades-api
- baseURL_template: https://{vcenter}/api
  baseurl_source: spec_template
  description: Operations for managing virtual machines
  name: Broadcom Virtual Machines API
  slug: broadcom-virtual-machines-api
- baseURL_template: https://{sddc-manager}/v1
  baseurl_source: spec_template
  description: Workload domain lifecycle management
  name: Broadcom Workload Domains API
  slug: broadcom-workload-domains-api
artifact_total: 59
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts API
  slug: open-broadcom-alerts-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts API Tokens API
  slug: open-broadcom-api-tokens-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Authentication API
  slug: open-broadcom-authentication-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Clusters API
  slug: open-broadcom-clusters-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Content Library API
  slug: open-broadcom-content-library-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Dashboards API
  slug: open-broadcom-dashboards-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Datastores API
  slug: open-broadcom-datastores-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Events API
  slug: open-broadcom-events-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Hosts API
  slug: open-broadcom-hosts-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Network Pools API
  slug: open-broadcom-network-pools-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Networks API
  slug: open-broadcom-networks-api
- collection_type: open
  name: Broadcom Operations for Applications REST API
  slug: open-broadcom-operations-for-applications
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Proxies API
  slug: open-broadcom-proxies-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Query API
  slug: open-broadcom-query-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Session API
  slug: open-broadcom-session-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Sources API
  slug: open-broadcom-sources-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Tagging API
  slug: open-broadcom-tagging-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Tasks API
  slug: open-broadcom-tasks-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Upgrades API
  slug: open-broadcom-upgrades-api
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Virtual Machines API
  slug: open-broadcom-virtual-machines-api
- collection_type: open
  name: Broadcom VMware Cloud Foundation API
  slug: open-broadcom-vmware-cloud-foundation
- collection_type: open
  name: Broadcom vSphere Automation API
  slug: open-broadcom-vsphere-automation
- collection_type: open
  name: Broadcom Operations for Applications REST Alerts Workload Domains API
  slug: open-broadcom-workload-domains-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/broadcom-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/broadcom-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/broadcom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/broadcom-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Broadcom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/broadcom
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/appneta/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/brocade/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/ca/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/newport-communications/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/symantec/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/vmware/
created: '2025-01-14'
description: Broadcom is a global technology company that specializes in the design and manufacturing of semiconductors and other hardware components for a wide range of industries. They provide a diverse portfolio of products for the enterprise, data center, networking, telecommunications, and consumer electronics markets. Broadcom's technology is used in a variety of devices such as smartphones, tablets, routers, and smart TVs.
finops:
- name: Broadcom Finops
  service_category: Enterprise Software & Infrastructure
  slug: broadcom-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/broadcom.png
json_schemas:
- name: Broadcom Alert
  property_count: 14
  slug: broadcom-alert
- name: Broadcom Cluster
  property_count: 12
  slug: broadcom-cluster
- name: Broadcom Dashboard
  property_count: 11
  slug: broadcom-dashboard
- name: Broadcom Host
  property_count: 11
  slug: broadcom-host
- name: Broadcom Task
  property_count: 11
  slug: broadcom-task
- name: Broadcom Virtual Machine
  property_count: 11
  slug: broadcom-virtual-machine
- name: Broadcom Workload Domain
  property_count: 8
  slug: broadcom-workload-domain
jsonld:
- class_count: 3
  name: Broadcom Context
  property_count: 18
  slug: broadcom-context
layout: provider
modified: '2026-08-21'
name: Broadcom
nav: Providers
network: true
overview: 'Broadcom publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, API Tokens API, Authentication API, and 17 more. Tagged areas include Cloud Infrastructure, Gateways, Management, Networks, and Observability.


  The Broadcom catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Broadcom''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Broadcom Plans Pricing
  plan_count: 1
  slug: broadcom-plans-pricing
press:
- date: '2026-05-25'
  title: Experience AI
  url: https://broadcomfoundation.org/programs/experience-ai/
- date: '2026-05-25'
  title: OpenAI and Broadcom announce strategic collaboration to ...
  url: https://investors.broadcom.com/news-releases/news-release-details/openai-and-broadcom-announce-strategic-collaboration-deploy-10
- date: '2026-05-25'
  title: Broadcom (@Broadcom) / Posts / X
  url: https://x.com/Broadcom
- date: '2026-05-25'
  title: Broadcom agrees to support development of Meta's next- ...
  url: https://www.manufacturingdive.com/news/broadcom-support-meta-next-generation-ai-chips/818108/
- date: '2026-05-25'
  title: News Releases - Broadcom News and Stories
  url: https://news.broadcom.com/releases
random_paper: 20
rate_limits:
- limit_count: 3
  name: Broadcom Rate Limits
  slug: broadcom-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Broadcom API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: broadcom-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 64.3
    catalog_earned_first_party: 0.0
    catalog_gap: 50.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 69.3
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/broadcom/refs/heads/main/screenshots/broadcom-2026-06-20T173721.png
security:
- kind: authentication
  name: Broadcom Authentication
  slug: broadcom-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Broadcom Domain Security
  slug: broadcom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: broadcom
tags:
- Cloud Infrastructure
- Gateways
- Management
- Networks
- Observability
- Virtualization
- Fortune 500
---
