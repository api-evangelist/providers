---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Forto Agentic Access
  operation_count: 22
  slug: forto-agentic-access
  summary_line: 22 operations · 9 acting
api_count: 7
apis:
- description: The Forto Public API provides programmatic access to Forto's digital freight forwarding platform. It exposes booking management (create, update, finalize, discard, list), shipment operations (list, ge
  name: Forto Public API
  slug: forto-public-api
- description: The Bookings API from Forto — 4 operation(s) for bookings.
  name: Forto Bookings API
  slug: forto-bookings-api
- description: The Documents API from Forto — 2 operation(s) for documents.
  name: Forto Documents API
  slug: forto-documents-api
- description: The Shipments API from Forto — 2 operation(s) for shipments.
  name: Forto Shipments API
  slug: forto-shipments-api
- description: The Subscriptions API from Forto — 3 operation(s) for subscriptions.
  name: Forto Subscriptions API
  slug: forto-subscriptions-api
- description: The Tokens API from Forto — 2 operation(s) for tokens.
  name: Forto Tokens API
  slug: forto-tokens-api
- description: The TransportPlans API from Forto — 4 operation(s) for transportplans.
  name: Forto TransportPlans API
  slug: forto-transportplans-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Forto Public Bookings API
  slug: open-forto-bookings-api
- collection_type: open
  name: Forto Public Bookings Documents API
  slug: open-forto-documents-api
- collection_type: open
  name: Forto Public Bookings Shipments API
  slug: open-forto-shipments-api
- collection_type: open
  name: Forto Public Bookings Subscriptions API
  slug: open-forto-subscriptions-api
- collection_type: open
  name: Forto Public Bookings Tokens API
  slug: open-forto-tokens-api
- collection_type: open
  name: Forto Public Bookings TransportPlans API
  slug: open-forto-transportplans-api
- collection_type: open
  name: Forto Public API
  slug: open-forto
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forto-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/forto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forto-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/forto-logistics
- group: company
  title: ''
  type: Website
  url: https://forto.com/en/
- group: start
  title: ''
  type: Portal
  url: https://developers.forto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.forto.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.forto.com/recipes/creation-of-booking-request
- group: learn
  title: ''
  type: Tutorials
  url: https://developers.forto.com/recipes
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.forto.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://forto.com/en/blog/
- group: operate
  title: ''
  type: Support
  url: https://forto.com/en/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://forto.com/en/career/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://forto.com/en/data-protection/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://forto.com/en/terms-and-conditions/
created: '2026-05-23'
description: Forto is a digital freight forwarder and supply chain platform that combines technology with logistics expertise to provide sea, air, and rail freight services across 100+ countries. The platform offers a public REST API for booking management, shipment tracking, transport plans, document handling, and webhook subscriptions, enabling shippers, enterprises, and partners to integrate Forto freight operations directly into their ERP, TMS, and supply chain systems via standard HTTPS APIs, EDI, or fully customized integrations.
features:
- description: Public HTTPS REST API exposing booking, shipment, transport plan, document, and subscription endpoints
  name: REST API
- description: Predefined EDI-based integrations for core data exchange with shipper systems
  name: EDI Integrations
- description: Create, list, and delete subscriptions to receive notifications on shipment and booking changes
  name: Webhook Subscriptions
- description: Multi-version transport plan API with 30+ milestone events at shipment and container level
  name: Transport Plan Tracking
- description: Upload and download shipment documents, invoices, and reports via API
  name: Document Management
- description: Create, list, and delete API tokens for authenticating requests
  name: Token-based Authentication
- description: AI solutions for the logistics industry providing agentic AI capabilities for logistics operations
  name: FortoLabs Agentic AI
finops:
- name: Forto Finops
  service_category: API
  slug: forto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forto.png
integrations:
- description: Integrate Forto shipment data into SAP ERP and supply chain modules
  name: SAP
- description: Connect Forto bookings and tracking events into Oracle ERP and SCM applications
  name: Oracle
- description: Exchange shipment and booking data with the Infor Nexus supply chain network
  name: Infor Nexus
- description: Predefined EDI integrations for standardized B2B freight data exchange
  name: EDI
layout: provider
modified: '2026-05-23'
name: Forto
nav: Providers
network: true
overview: 'Forto publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Documents API, Shipments API, and 3 more. Tagged areas include Freight, Logistics, Supply Chain, Shipping, and Freight Forwarding.


  Forto''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, and 10 more developer resources.'
plans:
- name: Forto Plans Pricing
  plan_count: 1
  slug: forto-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Forto Rate Limits
  slug: forto-rate-limits
score:
  band: thin
  composite: 28.9
  delta: 1.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.7
    developer_ergonomics: 46.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forto/refs/heads/main/screenshots/forto-2026-06-20T181445.png
security:
- kind: authentication
  name: Forto Authentication
  slug: forto-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Forto Domain Security
  slug: forto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Forto Vulnerability Disclosure
  slug: forto-vulnerability-disclosure
  summary_line: disclosure policy published
slug: forto
tags:
- Freight
- Logistics
- Supply Chain
- Shipping
- Freight Forwarding
- EDI
use_cases:
- description: Connect Forto shipments and bookings directly into SAP, Oracle, Infor Nexus, and other enterprise systems
  name: ERP / TMS Integration
- description: Surface live transport milestones into supply chain dashboards and control towers
  name: Real-Time Shipment Visibility
- description: Programmatically create, update, and finalize freight booking requests across sea, air, and rail
  name: Booking Automation
- description: Subscribe to webhooks to trigger downstream workflows when shipment status changes
  name: Event-Driven Workflows
- description: Pull emissions and Climate Visibility data into ESG and sustainability reporting
  name: Sustainability Reporting
website: https://forto.com/en/
---
