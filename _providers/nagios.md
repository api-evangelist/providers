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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Nagios Agentic Access
  operation_count: 33
  slug: nagios-agentic-access
  summary_line: 33 operations · 7 acting
api_count: 3
apis:
- description: Encrypted binary TCP daemon (default port 5667) that accepts passive service/host check results from remote machines. Not REST — clients send tab-delimited records over a shared-secret-encrypted socke
  name: NSCA (Nagios Service Check Acceptor)
  slug: nsca
- description: Daemon that runs Nagios plugins on a remote Linux/Unix host on TCP port 5666, returning the plugin's exit code and output to the Nagios server. Binary protocol, not REST.
  name: NRPE (Nagios Remote Plugin Executor)
  slug: nrpe
- description: Admin-only endpoints to add, modify, and delete hosts and services.
  name: Nagios Config API
  slug: nagios-config-api
- description: System-wide CPU utilization and core counts.
  name: Nagios CPU API
  slug: nagios-cpu-api
- description: Logical, physical, and mount-point disk metrics.
  name: Nagios Disk API
  slug: nagios-disk-api
- description: Network interface byte and packet counters.
  name: Nagios Interface API
  slug: nagios-interface-api
- description: Physical memory and swap.
  name: Nagios Memory API
  slug: nagios-memory-api
- description: Read-only backend for hosts, services, host groups, contacts, downtime, history, and other monitored objects.
  name: Nagios Objects API
  slug: nagios-objects-api
- description: User-defined Nagios-style plugins executed by the agent.
  name: Nagios Plugins API
  slug: nagios-plugins-api
- description: Running process inventory and resource use.
  name: Nagios Processes API
  slug: nagios-processes-api
- description: Host service / daemon status.
  name: Nagios Services API
  slug: nagios-services-api
- description: Submit passive check results and external commands.
  name: Nagios Submission API
  slug: nagios-submission-api
- description: Admin-only endpoints to manage Nagios XI subsystems, apply configuration, schedule downtime, and execute commands.
  name: Nagios System API
  slug: nagios-system-api
artifact_total: 49
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nagios XI REST Config API
  slug: open-nagios-config-api
- collection_type: open
  name: Nagios XI REST Config CPU API
  slug: open-nagios-cpu-api
- collection_type: open
  name: Nagios XI REST Config Disk API
  slug: open-nagios-disk-api
- collection_type: open
  name: Nagios XI REST Config Interface API
  slug: open-nagios-interface-api
- collection_type: open
  name: Nagios XI REST Config Memory API
  slug: open-nagios-memory-api
- collection_type: open
  name: Nagios XI REST Config Objects API
  slug: open-nagios-objects-api
- collection_type: open
  name: Nagios XI REST Config Plugins API
  slug: open-nagios-plugins-api
- collection_type: open
  name: Nagios XI REST Config Processes API
  slug: open-nagios-processes-api
- collection_type: open
  name: Nagios XI REST Config Services API
  slug: open-nagios-services-api
- collection_type: open
  name: Nagios XI REST Config Submission API
  slug: open-nagios-submission-api
- collection_type: open
  name: Nagios XI REST Config System API
  slug: open-nagios-system-api
- collection_type: open
  name: Nagios XI REST API
  slug: open-nagios-xi
- collection_type: open
  name: NCPA (Nagios Cross-Platform Agent) API
  slug: open-ncpa
- collection_type: open
  name: NRDP (Nagios Remote Data Processor) API
  slug: open-nrdp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nagios-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nagios-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nagios-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.nagios.org
- group: company
  title: ''
  type: Nagios XI Website
  url: https://www.nagios.com/products/nagios-xi/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nagios.org/documentation/
- group: build
  title: ''
  type: NagiosLibrary
  url: https://library.nagios.com/docs/
- group: operate
  title: ''
  type: Support Knowledgebase
  url: https://support.nagios.com/kb/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nagios.com/products/pricing/
- group: other
  title: ''
  type: Downloads
  url: https://www.nagios.org/downloads/
- group: other
  title: ''
  type: NagiosExchange
  url: https://exchange.nagios.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NagiosEnterprises
- group: other
  title: ''
  type: SourceRepo
  url: https://github.com/NagiosEnterprises/nagioscore
- group: other
  title: ''
  type: SourceRepo
  url: https://github.com/NagiosEnterprises/ncpa
- group: other
  title: ''
  type: SourceRepo
  url: https://github.com/NagiosEnterprises/nrpe
- group: other
  title: ''
  type: SourceRepo
  url: https://github.com/NagiosEnterprises/nsca
- group: other
  title: ''
  type: SourceRepo
  url: https://github.com/NagiosEnterprises/nrdp
- group: other
  title: ''
  type: SourceRepo
  url: https://github.com/NagiosEnterprises/ndoutils
- group: other
  title: ''
  type: SourceRepo
  url: https://github.com/NagiosEnterprises/nagios-mod-gearman
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/NagiosEnterprises/napiv2
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NagiosEnterprises/automation
- group: other
  title: ''
  type: PrometheusExporter
  url: https://github.com/NagiosEnterprises/nagprom
- group: build
  title: ''
  type: ServiceNowIntegration
  url: https://github.com/NagiosEnterprises/NagiosXI-ServiceNow-EventHandler
- group: build
  title: ''
  type: PagerDutyIntegration
  url: https://github.com/NagiosEnterprises/nagiosxi-pagerduty-handler
- group: build
  title: ''
  type: VMwareIntegration
  url: https://github.com/NagiosEnterprises/NSXMon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nagios-enterprises-llc
- group: commercial
  title: ''
  type: License
  url: https://github.com/NagiosEnterprises/nagioscore/blob/master/LICENSE
- group: commercial
  title: ''
  type: Plans
  url: plans/nagios-plans-pricing.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/nagios-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/nagios-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.nagios.com/feed/
created: '2026-05-11'
description: Nagios is a family of open-source and commercial IT infrastructure monitoring tools, including Nagios Core (the original open-source monitoring engine), Nagios XI (the commercial enterprise distribution), Nagios Fusion, Nagios Log Server, and Nagios Network Analyzer, used to monitor hosts, services, networks, applications, and metrics with alerting and reporting. Nagios Core itself has no central HTTP API; Nagios XI ships a built-in REST API (typically reached at https://{nagios-xi-host}/nagiosxi/api/v1/) for reading, writing, deleting, and updating monitoring configuration and status. The Nagios XI API is authenticated via a per-user API key passed as a query parameter or header. Passive check results can also be submitted via NRDP (HTTP, JSON/XML) or NSCA (encrypted TCP, port 5667), and the NCPA cross-platform agent exposes a hierarchical REST API on port 5693.
examples:
- key_count: 2
  name: Nagios Xi Host Create Example
  slug: nagios-xi-host-create-example
- key_count: 2
  name: Nagios Xi Host Status Example
  slug: nagios-xi-host-status-example
- key_count: 2
  name: Nagios Xi Service Delete Example
  slug: nagios-xi-service-delete-example
- key_count: 2
  name: Nagios Xi System Status Example
  slug: nagios-xi-system-status-example
- key_count: 2
  name: Ncpa Cpu Percent Example
  slug: ncpa-cpu-percent-example
- key_count: 2
  name: Ncpa Memory Virtual Example
  slug: ncpa-memory-virtual-example
- key_count: 2
  name: Nrdp Submit Check Example
  slug: nrdp-submit-check-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nagios.png
json_schemas:
- name: Nagios Check Result
  property_count: 6
  slug: nagios-check-result
- name: Nagios XI Host
  property_count: 23
  slug: nagios-xi-host
- name: Nagios XI Service
  property_count: 19
  slug: nagios-xi-service
- name: NCPA Metric Response
  property_count: 0
  slug: ncpa-metric
json_structures:
- name: Nagios Check Result Structure
  property_count: 0
  slug: nagios-check-result-structure
- name: Nagios Xi Host Structure
  property_count: 0
  slug: nagios-xi-host-structure
jsonld:
- class_count: 9
  name: Nagios Context
  property_count: 21
  slug: nagios-context
layout: provider
modified: '2026-05-23'
name: Nagios
nav: Providers
network: true
overview: 'Nagios publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Config API, CPU API, Disk API, and 8 more. Tagged areas include Monitoring, Infrastructure Monitoring, Network Monitoring, Open-Source, and IT Operations.


  The Nagios catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Nagios'' developer surface includes authentication, documentation, pricing, engineering blog, and 27 more developer resources.'
plans:
- name: Nagios Plans Pricing
  plan_count: 4
  slug: nagios-plans-pricing
random_paper: 11
rules:
- effective_rule_count: 5
  extends: []
  name: Nagios API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nagios-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Nagios API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: nagios-xi-rules
- effective_rule_count: 44
  extends:
  - spectral:oas
  name: Nagios API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: ncpa-rules
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 32.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 28.8
    contract_quality: 58.1
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 2.6
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nagios/refs/heads/main/screenshots/nagios-2026-06-20T185930.png
security:
- kind: authentication
  name: Nagios Authentication
  slug: nagios-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Nagios Domain Security
  slug: nagios-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nagios
tags:
- Monitoring
- Infrastructure Monitoring
- Network Monitoring
- Open-Source
- IT Operations
- Alerting
- Observability
- Nagios XI
- Nagios Core
- NCPA
- NRPE
- NSCA
- NRDP
website: https://www.nagios.org
---
