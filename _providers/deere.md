---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 7
apis:
- description: Provides access to the organizations a John Deere Operations Center user belongs to. Organizations are the top-level container for users, fields, equipment, and partner relationships in Operations Cen
  name: John Deere Operations Center Organizations API
  slug: operations-center-organizations-api
- description: Exposes growers, farms, fields, and field boundaries in Operations Center so that partner applications can sync agronomic field metadata and boundary geometry.
  name: John Deere Operations Center Fields API
  slug: operations-center-fields-api
- description: Provides metadata, telematics, and engine information for connected John Deere machines, including machine locations, engine hours, hours of operation, alerts, and device state reports.
  name: John Deere Operations Center Machines API
  slug: operations-center-machines-api
- description: Returns information about field operations such as planting, application, tillage, and harvest performed by connected John Deere machines, with links to machine, field, and product data.
  name: John Deere Operations Center Field Operations API
  slug: operations-center-field-operations-api
- description: Manages crop, seed, chemical, and fertilizer products used in field operations, allowing applications to read and reconcile product catalogs across an organization.
  name: John Deere Operations Center Products API
  slug: operations-center-products-api
- description: Lets partner applications subscribe to event notifications from Operations Center so that changes to organizations, machines, fields, and field operations can be received without polling.
  name: John Deere Operations Center Webhook API
  slug: operations-center-webhook-api
- description: A suite of APIs supporting precision agriculture workflows including prescription maps, work plans, setup files, and equipment configuration for connected John Deere machinery.
  name: John Deere Precision Tech APIs
  slug: precision-tech-apis
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deere-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JohnDeere
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/john-deere
- group: company
  title: ''
  type: Website
  url: https://www.deere.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.deere.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.deere.com/precision/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.deere.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.deere.com/whats-new
created: '2024-12-03'
description: John Deere is a manufacturer of agricultural, construction, and forestry machinery, equipment, and technology. Through its Operations Center and Precision Tech developer programs, John Deere exposes APIs that allow authorized partners and customers to access organization, field, machine, field operations, and webhook data tied to connected equipment and farm management workflows.
finops:
- name: Deere Finops
  service_category: Industry Platform
  slug: deere-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deere.png
layout: provider
modified: '2026-04-28'
name: John Deere
nav: Providers
network: true
overview: 'John Deere publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Agricultural Technology, AgTech, Construction, and Farming.


  John Deere''s developer surface includes getting-started guide, documentation, changelog, and 5 more developer resources.'
plans:
- name: Deere Plans Pricing
  plan_count: 2
  slug: deere-plans-pricing
press:
- date: '2026-05-25'
  title: At John Deere, 'Hard Iron Meets Artificial Intelligence'
  url: https://www.reddit.com/r/hardware/comments/mklv3o/at_john_deere_hard_iron_meets_artificial/
- date: '2026-05-25'
  title: John Deere
  url: https://www.ces.tech/success-stories/john-deere/
- date: '2026-05-25'
  title: Technology and Innovation - Our Company & Purpose
  url: https://about.deere.com/en-us/our-company-and-purpose/technology-and-innovation
- date: '2026-05-25'
  title: Ceres AI Renews and Enhances Integration with John ...
  url: https://www.prnewswire.com/news-releases/ceres-ai-renews-and-enhances-integration-with-john-deere-operations-center-to-simplify-farmland-management-302640187.html
- date: '2026-05-25'
  title: Artificial Intelligence at John Deere
  url: https://emerj.com/artificial-intelligence-at-john-deere/
random_paper: 13
rate_limits:
- limit_count: 3
  name: Deere Rate Limits
  slug: deere-rate-limits
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deere/refs/heads/main/screenshots/deere-2026-06-20T175814.png
security:
- kind: domain-security
  name: Deere Domain Security
  slug: deere-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deere
tags:
- Agriculture
- Agricultural Technology
- AgTech
- Construction
- Farming
- Forestry
- Machinery
- Operations Center
- Precision Agriculture
- Fortune 100
website: https://www.deere.com
---
