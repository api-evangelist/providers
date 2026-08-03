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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Cisco Directory Connector Agentic Access
  operation_count: 12
  slug: cisco-directory-connector-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 4
apis:
- description: SCIM 2.0 endpoints used by identity providers such as Microsoft Entra (Azure AD) and Okta to provision users and groups into Webex as an alternative to the on-premises Directory Connector.
  name: Webex SCIM 2.0 Provisioning
  slug: webex-scim
- description: The Groups API from Cisco Directory Connector — 3 operation(s) for groups.
  name: Cisco Directory Connector Groups API
  slug: cisco-directory-connector-groups-api
- description: The Organizations API from Cisco Directory Connector — 1 operation(s) for organizations.
  name: Cisco Directory Connector Organizations API
  slug: cisco-directory-connector-organizations-api
- description: The People API from Cisco Directory Connector — 2 operation(s) for people.
  name: Cisco Directory Connector People API
  slug: cisco-directory-connector-people-api
artifact_total: 12
collections:
- collection_type: open
  name: Cisco Directory Connector Management API (via Webex People & Groups)
  slug: open-cisco-directory-connector
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-directory-connector-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-directory-connector-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-directory-connector-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.webex.com
- group: start
  title: ''
  type: Console
  url: https://admin.webex.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.webex.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.webex.com/docs/integrations
- group: operate
  title: ''
  type: StatusPage
  url: https://status.webex.com
- group: company
  title: ''
  type: Blog
  url: https://developer.webex.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.webex.com
- group: other
  title: ''
  type: Downloads
  url: https://help.webex.com/en-us/article/nivpu1g/Deployment-Guide-for-Cisco-Directory-Connector
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/terms-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cisco-directory-connector-context.jsonld
created: '2024-01-01'
description: The Cisco Directory Connector is an on-premises Windows service that synchronizes users and groups from a corporate directory (typically Microsoft Active Directory or LDAP) into Cisco Webex Control Hub. It supports full and incremental sync, attribute mapping, dry-run preview, and scheduled jobs. Programmatic management is via the related Webex People, Groups, and Organizations APIs in Control Hub; modern deployments increasingly use SCIM 2.0 provisioning from identity providers (Azure AD, Okta) as an alternative to the on-premises connector.
finops:
- name: Cisco Directory Connector Finops
  service_category: API
  slug: cisco-directory-connector-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco-directory-connector.png
jsonld:
- class_count: 1
  name: Cisco Directory Connector Context
  property_count: 4
  slug: cisco-directory-connector-context
layout: provider
modified: '2026-04-23'
name: Cisco Directory Connector
nav: Providers
network: true
overview: 'Cisco Directory Connector publishes 3 APIs on the [APIs.io](https://apis.io/) network: Groups API, Organizations API, and People API. Tagged areas include Active Directory, Directory, Enterprise, Identity Management, and LDAP.


  The Cisco Directory Connector catalog on APIs.io includes 1 JSON-LD context.


  Cisco Directory Connector''s developer surface includes authentication, developer portal, developer console, getting-started guide, engineering blog, support, and 8 more developer resources.'
plans:
- name: Cisco Directory Connector Plans Pricing
  plan_count: 3
  slug: cisco-directory-connector-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Cisco Directory Connector Rate Limits
  slug: cisco-directory-connector-rate-limits
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.2
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-directory-connector/refs/heads/main/screenshots/cisco-directory-connector-2026-06-20T174400.png
security:
- kind: authentication
  name: Cisco Directory Connector Authentication
  slug: cisco-directory-connector-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cisco Directory Connector Domain Security
  slug: cisco-directory-connector-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cisco-directory-connector
tags:
- Active Directory
- Directory
- Enterprise
- Identity Management
- LDAP
- Provisioning
- SCIM
- Synchronization
website: https://developer.webex.com
---
