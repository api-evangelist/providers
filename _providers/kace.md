---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for the KACE Systems Management Appliance. Authenticated KACE SMA users can manage appliance data across the Asset, Inventory, Managed Install, Scripting, User, and Service Desk modules. Requ
  name: KACE Systems Management Appliance (SMA) API
  slug: kace-systems-management-appliance-sma-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quest.com/kace/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.quest.com/kace/
- group: docs
  title: ''
  type: Documentation
  url: https://support.quest.com/kace-systems-management-appliance/technical-documents
- group: docs
  title: ''
  type: APIReference
  url: https://support.quest.com/technical-documents/kace-systems-management-appliance/15.0/api-reference-guide
- group: operate
  title: ''
  type: Support
  url: https://support.quest.com/kace-systems-management-appliance
- group: auth
  title: ''
  type: Authentication
  url: https://raw.githubusercontent.com/api-evangelist/kace/refs/heads/main/authentication/kace-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kace-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://support.quest.com/kb/4268357/kace-software-product-support-lifecycle-policy
- group: design
  title: ''
  type: Conformance
  url: conformance/kace-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kace-llms.txt
created: '2026-07-17'
description: KACE is the endpoint and systems management product line from Quest Software, originally founded in 2003 as KACE Networks (backed by Norwest Venture Partners, Sigma Partners, and Focus Ventures), acquired by Dell in 2010, and now sold as Quest KACE. The portfolio centers on the KACE Systems Management Appliance (SMA) for inventory, patching, software distribution, scripting, and service desk; the KACE Systems Deployment Appliance (SDA) for OS imaging and provisioning; and KACE Cloud for mobile device management and modern endpoint management. The KACE SMA ships a REST API (JSON and XML) that lets administrators programmatically manage assets, inventory, managed installations, scripting, users, and service-desk tickets on the customer-hosted appliance. This profile enriches the original Norwest portfolio lead with the real Quest KACE identity and its documented API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kace.png
layout: provider
modified: '2026-07-19'
name: Kace
nav: Providers
network: true
overview: 'Kace publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Endpoint Management, Systems Management, IT Asset Management, and Patch Management.


  Kace''s developer surface includes documentation, API reference, support, authentication, and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 9.6
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kace/refs/heads/main/screenshots/kace-2026-08-07T171122.png
security:
- kind: authentication
  name: Kace Authentication
  slug: kace-authentication
  summary_line: session · 1 scheme
- kind: domain-security
  name: Kace Domain Security
  slug: kace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kace
tags:
- Company
- Endpoint Management
- Systems Management
- IT Asset Management
- Patch Management
- Service Desk
- Device Management
- Quest Software
website: https://www.quest.com/kace/
---
