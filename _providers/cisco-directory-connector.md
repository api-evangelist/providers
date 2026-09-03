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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Cisco Directory Connector Agentic Access
  operation_count: 12
  slug: cisco-directory-connector-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- description: SCIM 2.0 endpoints used by identity providers such as Microsoft Entra (Azure AD) and Okta to provision users and groups into Webex as an alternative to the on-premises Directory Connector.
  name: Webex SCIM 2.0 Provisioning
  slug: webex-scim
- baseURL: https://webexapis.com/v1
  baseurl_source: declared
  description: The Groups API from Cisco Directory Connector — 3 operation(s) for groups.
  name: Cisco Directory Connector Groups API
  slug: cisco-directory-connector-groups-api
- baseURL: https://webexapis.com/v1
  baseurl_source: declared
  description: The Organizations API from Cisco Directory Connector — 1 operation(s) for organizations.
  name: Cisco Directory Connector Organizations API
  slug: cisco-directory-connector-organizations-api
- baseURL: https://webexapis.com/v1
  baseurl_source: declared
  description: The People API from Cisco Directory Connector — 2 operation(s) for people.
  name: Cisco Directory Connector People API
  slug: cisco-directory-connector-people-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cisco Directory Connector Management API (via Webex People & ) Groups API
  slug: open-cisco-directory-connector-groups-api
- collection_type: open
  name: Cisco Directory Connector Management API (via Webex People & ) Groups Organizations API
  slug: open-cisco-directory-connector-organizations-api
- collection_type: open
  name: Cisco Directory Connector Management API (via Webex & ) Groups People API
  slug: open-cisco-directory-connector-people-api
- collection_type: open
  name: Cisco Directory Connector Management API (via Webex People & Groups)
  slug: open-cisco-directory-connector
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/webex/
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
modified: '2026-08-19'
name: Cisco Directory Connector
nav: Providers
network: true
overview: 'Cisco Directory Connector publishes 3 APIs on the [APIs.io](https://apis.io/) network: Groups API, Organizations API, and People API. Tagged areas include Active Directory, Directory, Enterprise, Identity Management, and LDAP.


  The Cisco Directory Connector catalog on APIs.io includes 1 JSON-LD context.


  Cisco Directory Connector''s developer surface includes authentication, developer portal, developer console, getting-started guide, engineering blog, support, and 9 more developer resources.'
plans:
- name: Cisco Directory Connector Plans Pricing
  plan_count: 3
  slug: cisco-directory-connector-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Cisco Directory Connector Rate Limits
  slug: cisco-directory-connector-rate-limits
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 19.4
    developer_ergonomics: 52.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
