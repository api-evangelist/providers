---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://admin.farmcommand.com/
  baseurl_source: declared
  description: The canplug API from Farmers Edge — 1 operation(s) for canplug.
  name: Farmers Edge canplug API
  slug: farmers-edge-canplug-api
- baseURL: https://admin.farmcommand.com/
  baseurl_source: declared
  description: The carbon API from Farmers Edge — 1 operation(s) for carbon.
  name: Farmers Edge carbon API
  slug: farmers-edge-carbon-api
- baseURL: https://admin.farmcommand.com/
  baseurl_source: declared
  description: The client API from Farmers Edge — 7 operation(s) for client.
  name: Farmers Edge client API
  slug: farmers-edge-client-api
- baseURL: https://admin.farmcommand.com/
  baseurl_source: declared
  description: The contact API from Farmers Edge — 2 operation(s) for contact.
  name: Farmers Edge contact API
  slug: farmers-edge-contact-api
- baseURL: https://admin.farmcommand.com/
  baseurl_source: declared
  description: The gridcalc API from Farmers Edge — 1 operation(s) for gridcalc.
  name: Farmers Edge gridcalc API
  slug: farmers-edge-gridcalc-api
- baseURL: https://admin.farmcommand.com/
  baseurl_source: declared
  description: The hefty API from Farmers Edge — 4 operation(s) for hefty.
  name: Farmers Edge hefty API
  slug: farmers-edge-hefty-api
- baseURL: https://admin.farmcommand.com/
  baseurl_source: declared
  description: The integrations API from Farmers Edge — 1 operation(s) for integrations.
  name: Farmers Edge integrations API
  slug: farmers-edge-integrations-api
- baseURL: https://admin.farmcommand.com/
  baseurl_source: declared
  description: The labcommand API from Farmers Edge — 3 operation(s) for labcommand.
  name: Farmers Edge labcommand API
  slug: farmers-edge-labcommand-api
- baseURL: https://admin.farmcommand.com/
  baseurl_source: declared
  description: The payments API from Farmers Edge — 3 operation(s) for payments.
  name: Farmers Edge payments API
  slug: farmers-edge-payments-api
- baseURL: https://admin.farmcommand.com/
  baseurl_source: declared
  description: The recengine API from Farmers Edge — 1 operation(s) for recengine.
  name: Farmers Edge recengine API
  slug: farmers-edge-recengine-api
- baseURL: https://admin.farmcommand.com/
  baseurl_source: declared
  description: The token-login API from Farmers Edge — 1 operation(s) for token-login.
  name: Farmers Edge token-login API
  slug: farmers-edge-token-login-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FarmCommand canplug API
  slug: open-farmers-edge-canplug-api
- collection_type: open
  name: FarmCommand canplug carbon API
  slug: open-farmers-edge-carbon-api
- collection_type: open
  name: FarmCommand canplug client API
  slug: open-farmers-edge-client-api
- collection_type: open
  name: FarmCommand canplug contact API
  slug: open-farmers-edge-contact-api
- collection_type: open
  name: FarmCommand canplug gridcalc API
  slug: open-farmers-edge-gridcalc-api
- collection_type: open
  name: FarmCommand canplug hefty API
  slug: open-farmers-edge-hefty-api
- collection_type: open
  name: FarmCommand canplug integrations API
  slug: open-farmers-edge-integrations-api
- collection_type: open
  name: FarmCommand canplug labcommand API
  slug: open-farmers-edge-labcommand-api
- collection_type: open
  name: FarmCommand canplug payments API
  slug: open-farmers-edge-payments-api
- collection_type: open
  name: FarmCommand canplug recengine API
  slug: open-farmers-edge-recengine-api
- collection_type: open
  name: FarmCommand canplug token-login API
  slug: open-farmers-edge-token-login-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/farmers-edge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/farmers-edge-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.farmcommand.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.farmcommand.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.farmcommand.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.farmcommand.com/docs/
- group: design
  title: ''
  type: Conventions
  url: conventions/farmers-edge-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/farmers-edge-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/farmers-edge-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/farmers-edge-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/farmers-edge-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/farmers-edge-farmcommand-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/farmers-edge-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/farmers-edge-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Farmers Edge is a precision-agriculture and digital-farming company whose FarmCommand platform combines satellite imagery, connected weather stations, in-field telematics (the CanPlug IoT device), agronomic modeling, carbon-program tooling, and soil/lab products such as LabCommand and Hefty/FESoils. The public FarmCommand API is a Django REST (drf-yasg) service on admin.farmcommand.com that handles self-serve client onboarding and verification, token-based login for FarmCommand, LabCommand, GridCalc, RecEngine and Hefty users, password resets, CanPlug device lookup, and inbound integration webhooks (Stripe billing, DocuSign envelopes, LEAF field alerts). Authentication is a FarmCommand API token passed as a query parameter.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/farmers-edge.png
layout: provider
modified: '2026-07-19'
name: Farmers Edge
nav: Providers
network: true
overview: 'Farmers Edge publishes 11 APIs on the [APIs.io](https://apis.io/) network, including canplug API, carbon API, client API, and 8 more. Tagged areas include Company, Enterprise, Agriculture, Precision Agriculture, and AgTech.


  Farmers Edge''s developer surface includes authentication, documentation, API reference, and 12 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 44.4
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 25.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/farmers-edge/refs/heads/main/screenshots/farmers-edge-2026-07-25T214231.png
security:
- kind: authentication
  name: Farmers Edge Authentication
  slug: farmers-edge-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Farmers Edge Domain Security
  slug: farmers-edge-domain-security
  summary_line: TLSv1.3 · HSTS
slug: farmers-edge
tags:
- Company
- Enterprise
- Agriculture
- Precision Agriculture
- AgTech
- Farm Management
- Digital Agriculture
- IoT
- Weather
- Carbon
website: https://www.farmcommand.com/
---
