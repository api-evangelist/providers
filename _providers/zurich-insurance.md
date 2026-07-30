---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 12
apis:
- description: Returns customer profile information for Zurich policyholders through the ConnectZ open insurance framework. Used by partners and aggregators that need normalized customer attributes to support cross-
  name: ConnectZ Profile Information API
  slug: connectz-profile-information
- description: Exposes the payment status of a Zurich insurance policy (paid, due, lapsed) so partners and downstream systems can reconcile billing and surface payment state in their own UX.
  name: ConnectZ Policy Payment Status API
  slug: connectz-policy-payment-status
- description: Retrieves claim records and status for Zurich policies, enabling partners, brokers, and aggregators to display real-time claims information without manual lookup.
  name: ConnectZ Claims Retrieval API
  slug: connectz-claims-retrieval
- description: Returns agency / distribution-partner details (name, branch, contact, commercial relationship) used to power partner-management dashboards and partner onboarding.
  name: ConnectZ Agencies Details API
  slug: connectz-agencies-details
- description: Generates indicative Third Party Liability quotes against Zurich underwriting rules, designed for embedding into partner sales journeys and aggregator quote-and-bind flows.
  name: Third Party Liability Quote API
  slug: third-party-liability-quote
- description: Surfaces Risk Engineering data (site surveys, loss prevention, risk grades) from the My Zurich commercial customer portal so partner risk management systems can ingest survey findings in real time wit
  name: Risk Engineering - My Zurich Connector API
  slug: risk-engineering-my-zurich-connector
- description: Returns commercial-policy data (cover, limits, sections, endorsements) from the My Zurich portal for ingestion into broker and corporate customer systems.
  name: Policy - My Zurich Connector API
  slug: policy-my-zurich-connector
- description: Submits new business and renewal submissions into Zurich's commercial underwriting flow from broker management systems via the My Zurich connector.
  name: Submission - My Zurich Connector API
  slug: submission-my-zurich-connector
- description: Document domain service (Australia) for managing, indexing, and retrieving structured document objects across Zurich's Australian operations.
  name: AU Document Domain API
  slug: au-document-domain
- description: Handles invoice, requisition, and contract approvals between Zurich's Coupa procurement platform and downstream finance / approver systems.
  name: Coupa Approvals Handling API
  slug: coupa-approvals-handling
- description: Programmatic access to Zurich's MyAccess entitlement-request platform for raising, approving, and tracking access requests across internal systems.
  name: Access Request Management (MyAccess) API
  slug: access-request-management
- description: Read/write integration with Zurich's ServiceNow Incident Management module for raising, updating, and querying incidents from other systems.
  name: ServiceNow Incidents API
  slug: servicenow-incidents
artifact_total: 29
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zurich-insurance-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZurichInsurance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zurich-insurance-company-ltd
- group: company
  title: ''
  type: Website
  url: https://www.zurich.com/
- group: start
  title: ''
  type: Portal
  url: https://exchange.zurich.com/
- group: docs
  title: ''
  type: Documentation
  url: https://exchange.zurich.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.zurich.com/
created: '2026-05-05'
description: A Swiss multinational insurance company and one of the world's largest insurers providing property, casualty, life, and specialty insurance products. Zurich operates a public API platform at exchange.zurich.com (Zurich Exchange / ConnectZ / Zurich Edge) that exposes 30+ internal and external APIs across policy, claims, quoting, partner analytics, procurement, and operations.
features:
- description: Central marketplace publishing 30+ internal and external APIs spanning policy, claims, quoting, procurement, and operations
  name: Zurich Exchange API Marketplace
- description: Open insurance connectivity framework exposing customer profile, policy payment status, claims, and agencies
  name: ConnectZ Open Insurance Framework
- description: Digital insurance solutions combining innovation and deep insurance expertise into tailored partner offerings
  name: Zurich Edge Platform
- description: Connector APIs for policy, submission, and risk engineering data from the My Zurich commercial customer portal
  name: My Zurich Connectors
- description: All published APIs are subject to vulnerability scanning prior to consumer onboarding
  name: Vulnerability Scanning
- description: Replaces manual data cleansing with automated, real-time feeds into partner systems
  name: Real-Time Data Integration
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zurich-insurance.png
integrations:
- description: Procurement approvals handled via the Coupa Approvals Handling API
  name: Coupa
- description: Incident management integrated through the ServiceNow Incidents API
  name: ServiceNow
- description: Three connector APIs (Policy, Submission, Risk Engineering) bridge the My Zurich commercial portal with broker and corporate systems
  name: My Zurich Portal
- description: Open insurance partners consume ConnectZ APIs for customer, policy, claims, and agency data
  name: ConnectZ Partners
layout: provider
modified: '2026-05-16'
name: Zurich Insurance
nav: Providers
network: true
overview: 'Zurich Insurance publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Financial, Property & Casualty, Open Insurance, and API Platform.


  Zurich Insurance''s developer surface includes developer portal, documentation, and 5 more developer resources.'
random_paper: 34
score:
  band: minimal
  composite: 9.9
  delta: -2.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zurich-insurance/refs/heads/main/screenshots/zurich-insurance-2026-06-20T202007.png
security:
- kind: domain-security
  name: Zurich Insurance Domain Security
  slug: zurich-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zurich-insurance
tags:
- Insurance
- Financial
- Property & Casualty
- Open Insurance
- API Platform
use_cases:
- description: Brokers and corporate customers ingest Zurich risk engineering data straight into their risk management systems
  name: Partner Risk Management Integration
- description: Partner platforms embed Third Party Liability quote generation directly in their sales journeys
  name: Embedded Insurance Quoting
- description: ConnectZ Profile, Policy Payment Status, and Claims Retrieval power policyholder aggregator dashboards
  name: Policy and Claims Aggregation
- description: Agency details API supports partner onboarding and partner-management dashboards
  name: Distribution Partner Management
- description: Coupa Approvals Handling automates invoice, requisition, and contract approval flows
  name: Internal Procurement Automation
- description: ServiceNow Incidents API enables external systems to raise and track Zurich incidents
  name: Cross-System Incident Management
website: https://www.zurich.com/
---
