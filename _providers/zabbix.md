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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Zabbix Agentic Access
  operation_count: 20
  slug: zabbix-agentic-access
  summary_line: 20 operations · 20 acting
api_count: 10
apis:
- description: Action configuration for alerting and automation
  name: Zabbix Actions API
  slug: zabbix-actions-api
- description: User login and session management
  name: Zabbix Authentication API
  slug: zabbix-authentication-api
- description: Event retrieval and acknowledgement
  name: Zabbix Events API
  slug: zabbix-events-api
- description: Historical monitoring data
  name: Zabbix History API
  slug: zabbix-history-api
- description: Host group management
  name: Zabbix Host Groups API
  slug: zabbix-host-groups-api
- description: Host configuration and management
  name: Zabbix Hosts API
  slug: zabbix-hosts-api
- description: Monitoring item configuration
  name: Zabbix Items API
  slug: zabbix-items-api
- description: Active problem retrieval
  name: Zabbix Problems API
  slug: zabbix-problems-api
- description: Trigger configuration and management
  name: Zabbix Triggers API
  slug: zabbix-triggers-api
- description: User account management
  name: Zabbix Users API
  slug: zabbix-users-api
artifact_total: 44
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zabbix Actions API
  slug: open-zabbix-actions-api
- collection_type: open
  name: Zabbix Actions Authentication API
  slug: open-zabbix-authentication-api
- collection_type: open
  name: Zabbix Actions Events API
  slug: open-zabbix-events-api
- collection_type: open
  name: Zabbix Actions History API
  slug: open-zabbix-history-api
- collection_type: open
  name: Zabbix Actions Host Groups API
  slug: open-zabbix-host-groups-api
- collection_type: open
  name: Zabbix Actions Hosts API
  slug: open-zabbix-hosts-api
- collection_type: open
  name: Zabbix Actions Items API
  slug: open-zabbix-items-api
- collection_type: open
  name: Zabbix Actions Problems API
  slug: open-zabbix-problems-api
- collection_type: open
  name: Zabbix Actions Triggers API
  slug: open-zabbix-triggers-api
- collection_type: open
  name: Zabbix Actions Users API
  slug: open-zabbix-users-api
- collection_type: open
  name: Zabbix API
  slug: open-zabbix
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zabbix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zabbix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zabbix-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.zabbix.com
- group: company
  title: ''
  type: Blog
  url: https://blog.zabbix.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/zabbix/zabbix
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zabbix
- group: other
  title: ''
  type: Docker
  url: https://github.com/zabbix/zabbix-docker
- group: build
  title: ''
  type: AnsibleCollection
  url: https://github.com/zabbix/ansible-collection
- group: operate
  title: ''
  type: CommunityTemplates
  url: https://github.com/zabbix/community-templates
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/zabbix
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zabbix.com/privacy_policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zabbix.com/terms_of_use
- group: other
  title: ''
  type: Download
  url: https://www.zabbix.com/download
created: '2024-01-01'
description: Zabbix is an enterprise-class open source distributed monitoring solution for networks and applications. Zabbix enables real-time monitoring of millions of metrics collected from tens of thousands of servers, virtual machines, and network devices. The Zabbix API provides JSON-RPC 2.0 access for programmatically managing host configurations, collecting monitoring data, and automating operations.
examples:
- key_count: 2
  name: Zabbix History Get Example
  slug: zabbix-history-get-example
- key_count: 2
  name: Zabbix Host Get Example
  slug: zabbix-host-get-example
- key_count: 2
  name: Zabbix Problem Get Example
  slug: zabbix-problem-get-example
features:
- name: Host Monitoring
- name: Network Monitoring
- name: Application Monitoring
- name: Cloud Monitoring
- name: Agent-Based Collection
- name: Agentless Collection (SNMP, IPMI, JMX)
- name: Triggers and Alerting
- name: Dashboards and Visualizations
- name: Historical Data Storage
- name: Scalable Distributed Monitoring
- name: Auto Discovery
- name: API Automation
finops:
- name: Zabbix Finops
  service_category: API
  slug: zabbix-finops
image: https://www.zabbix.com/assets/img/logo/zabbix_logo.png
layout: provider
modified: '2026-05-19'
name: Zabbix
nav: Providers
network: true
overview: 'Zabbix publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Authentication API, Events API, and 7 more. Tagged areas include Monitoring, Infrastructure, Networks, Alerting, and Open Source.


  The Zabbix catalog on APIs.io includes 1 Spectral governance ruleset.


  Zabbix''s developer surface includes authentication, developer portal, engineering blog, GitHub presence, and 10 more developer resources.'
plans:
- name: Zabbix Plans Pricing
  plan_count: 3
  slug: zabbix-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Zabbix Rate Limits
  slug: zabbix-rate-limits
rules:
- effective_rule_count: 11
  extends: []
  name: Zabbix API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 4
  slug: zabbix-rules
score:
  band: thin
  composite: 36.1
  delta: -1.4
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 30.3
    contract_quality: 53.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 30.3
    operational_transparency: 13.2
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zabbix/refs/heads/main/screenshots/zabbix-2026-06-20T201756.png
security:
- kind: authentication
  name: Zabbix Authentication
  slug: zabbix-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zabbix Domain Security
  slug: zabbix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zabbix
tags:
- Monitoring
- Infrastructure
- Networks
- Alerting
- Open Source
- Observability
website: https://www.zabbix.com
---
