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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Cisco Directory Connectors Agentic Access
  operation_count: 10
  slug: cisco-directory-connectors-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 3
apis:
- description: REST API for managing directory synchronization and user provisioning.
  name: Cisco Directory Connector API
  slug: cisco-directory-connector-api
- description: The Groups API from Cisco Directory Connectors — 2 operation(s) for groups.
  name: Cisco Directory Connectors Groups API
  slug: cisco-directory-connectors-groups-api
- description: The People API from Cisco Directory Connectors — 2 operation(s) for people.
  name: Cisco Directory Connectors People API
  slug: cisco-directory-connectors-people-api
artifact_total: 10
collections:
- collection_type: open
  name: Cisco Directory Connectors API (via Webex People & Groups)
  slug: open-cisco-directory-connectors
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-directory-connectors-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-directory-connectors-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-directory-connectors-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: company
  title: ''
  type: Blog
  url: https://developer.cisco.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cisco.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/end-user-license-agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: agent
  title: ''
  type: LlmsText
  url: https://www.cisco.com/llms.txt
created: '2024-01-15'
description: The Cisco Directory Connectors API provides programmatic access to manage and synchronize user directories with Cisco services. It enables integration with Active Directory, LDAP, and other directory services to automate user provisioning and management.
finops:
- name: Cisco Directory Connectors Finops
  service_category: API
  slug: cisco-directory-connectors-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco-directory-connectors.png
layout: provider
modified: '2026-03-16'
name: Cisco Directory Connectors
nav: Providers
network: true
overview: 'Cisco Directory Connectors publishes 2 APIs on the [APIs.io](https://apis.io/) network: Groups API and People API. Tagged areas include Active Directory, Directory Services, Identity Management, LDAP, and User Synchronization.


  Cisco Directory Connectors'' developer surface includes authentication, developer portal, engineering blog, and 7 more developer resources.'
plans:
- name: Cisco Directory Connectors Plans Pricing
  plan_count: 3
  slug: cisco-directory-connectors-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Cisco Directory Connectors Rate Limits
  slug: cisco-directory-connectors-rate-limits
score:
  band: developing
  composite: 43.1
  delta: -1.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 53.4
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-directory-connectors/refs/heads/main/screenshots/cisco-directory-connectors-2026-06-20T174356.png
security:
- kind: authentication
  name: Cisco Directory Connectors Authentication
  slug: cisco-directory-connectors-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cisco Directory Connectors Domain Security
  slug: cisco-directory-connectors-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cisco-directory-connectors
tags:
- Active Directory
- Directory Services
- Identity Management
- LDAP
- User Synchronization
website: https://developer.cisco.com
---
