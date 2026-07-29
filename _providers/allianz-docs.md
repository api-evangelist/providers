---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Allianz Docs Agentic Access
  operation_count: 9
  slug: allianz-docs-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 6
apis:
- description: The Allianz Partners API Management portal provides insurance and assistance product APIs covering the full customer journey. APIs support policy purchase, change, and cancellation operations in XML a
  name: Allianz Partners API
  slug: allianz-partners-api
- description: The Allianz Global API Portal provides enterprise insurance APIs for registered business partners. The portal uses Apigee Edge for API key management and OAuth2 for authentication. Most API documentat
  name: Allianz Global API
  slug: allianz-global-api
- description: Operations for retrieving insurance certificates of currency
  name: Allianz Certificates API
  slug: allianz-docs-certificates-api
- description: Operations for submitting insurance leads to the Allianz sales team
  name: Allianz Leads API
  slug: allianz-docs-leads-api
- description: Operations for retrieving and completing insurance policy details
  name: Allianz Policy Details API
  slug: allianz-docs-policy-details-api
- description: Operations for generating and retrieving insurance price estimates and quotes
  name: Allianz Price Estimates API
  slug: allianz-docs-price-estimates-api
artifact_total: 80
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/allianz-docs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allianz-docs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/allianz-docs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/allianz-docs-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.allianz.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/allianz
- group: operate
  title: ''
  type: Support
  url: https://global.apis.allianz.com/contact
- group: design
  title: ''
  type: SpectralRules
  url: rules/allianz-docs-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/allianz-vocabulary.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allianz-docs-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allianz-docs-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.allianz.com/en/press.html
created: '2024-01-15'
description: Allianz is one of the world's largest insurance and financial services companies, serving over 86 million customers worldwide. Allianz offers developer APIs across multiple product lines including insurance quoting, policy management, claims, and trade credit services, enabling partners and distributors to integrate Allianz insurance products directly into their platforms.
examples:
- key_count: 4
  name: Api Connect Address Example
  slug: api-connect-address-example
- key_count: 10
  name: Api Connect Certificate Of Currency Example
  slug: api-connect-certificate-of-currency-example
- key_count: 3
  name: Api Connect Email Sent Response Example
  slug: api-connect-email-sent-response-example
- key_count: 5
  name: Api Connect Lead Referral Request Example
  slug: api-connect-lead-referral-request-example
- key_count: 4
  name: Api Connect Lead Referral Response Example
  slug: api-connect-lead-referral-response-example
- key_count: 3
  name: Api Connect Policy Details Assisted Request Example
  slug: api-connect-policy-details-assisted-request-example
- key_count: 6
  name: Api Connect Policy Details Response Example
  slug: api-connect-policy-details-response-example
- key_count: 2
  name: Api Connect Policy Details Self Service Request Example
  slug: api-connect-policy-details-self-service-request-example
- key_count: 3
  name: Api Connect Price Estimate Assisted Request Example
  slug: api-connect-price-estimate-assisted-request-example
- key_count: 3
  name: Api Connect Price Estimate Email Request Example
  slug: api-connect-price-estimate-email-request-example
- key_count: 6
  name: Api Connect Price Estimate Response Example
  slug: api-connect-price-estimate-response-example
- key_count: 3
  name: Api Connect Price Estimate Self Service Request Example
  slug: api-connect-price-estimate-self-service-request-example
- key_count: 7
  name: Api Connect Price Estimate Summary Example
  slug: api-connect-price-estimate-summary-example
- key_count: 3
  name: Api Connect Rating Factor Example
  slug: api-connect-rating-factor-example
- key_count: 8
  name: Api Connect Rating Factors Response Example
  slug: api-connect-rating-factors-response-example
- key_count: 3
  name: Api Connect Self Service Estimate Response Example
  slug: api-connect-self-service-estimate-response-example
- key_count: 3
  name: Api Connect Self Service Session Response Example
  slug: api-connect-self-service-session-response-example
- key_count: 4
  name: Api Connect Vehicle Example
  slug: api-connect-vehicle-example
features:
- description: APIs for generating price estimates and quotes for home, auto, and other insurance products enabling partner-embedded quoting flows.
  name: Insurance Quoting
- description: Purchase, change, and cancel insurance policies programmatically through REST and SOAP-compatible API interfaces.
  name: Policy Management
- description: Retrieve and manage insurance claims data, enabling ERP and enterprise system integration for claims tracking.
  name: Claims Integration
- description: Enable distributors, brokers, and financial institutions to embed Allianz insurance products into their customer journeys.
  name: Partner Distribution
- description: Secure API authentication using OAuth2 client credentials flow for programmatic access to partner APIs.
  name: OAuth2 Authentication
- description: APIs support both XML and JSON formats with content negotiation for flexible enterprise integration.
  name: Multi-Format Support
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allianz-docs.png
integrations:
- description: Allianz Trade APIs support Postman collection import for API exploration and testing.
  name: Postman
- description: Allianz Global API platform uses Apigee Edge for API key and credential management.
  name: Apigee Edge
- description: Allianz Partners portal is built on Azure API Management platform.
  name: Azure API Management
json_schemas:
- name: Address
  property_count: 4
  slug: api-connect-address
- name: CertificateOfCurrency
  property_count: 10
  slug: api-connect-certificate-of-currency
- name: EmailSentResponse
  property_count: 3
  slug: api-connect-email-sent-response
- name: LeadReferralRequest
  property_count: 5
  slug: api-connect-lead-referral-request
- name: LeadReferralResponse
  property_count: 4
  slug: api-connect-lead-referral-response
- name: PolicyDetailsAssistedRequest
  property_count: 3
  slug: api-connect-policy-details-assisted-request
- name: PolicyDetailsResponse
  property_count: 6
  slug: api-connect-policy-details-response
- name: PolicyDetailsSelfServiceRequest
  property_count: 2
  slug: api-connect-policy-details-self-service-request
- name: PriceEstimateAssistedRequest
  property_count: 3
  slug: api-connect-price-estimate-assisted-request
- name: PriceEstimateEmailRequest
  property_count: 3
  slug: api-connect-price-estimate-email-request
- name: PriceEstimateResponse
  property_count: 6
  slug: api-connect-price-estimate-response
- name: PriceEstimateSelfServiceRequest
  property_count: 3
  slug: api-connect-price-estimate-self-service-request
- name: PriceEstimateSummary
  property_count: 7
  slug: api-connect-price-estimate-summary
- name: RatingFactor
  property_count: 3
  slug: api-connect-rating-factor
- name: RatingFactorsResponse
  property_count: 8
  slug: api-connect-rating-factors-response
- name: SelfServiceEstimateResponse
  property_count: 3
  slug: api-connect-self-service-estimate-response
- name: SelfServiceSessionResponse
  property_count: 3
  slug: api-connect-self-service-session-response
- name: Vehicle
  property_count: 4
  slug: api-connect-vehicle
json_structures:
- name: Api Connect Address Structure
  property_count: 4
  slug: api-connect-address-structure
- name: Api Connect Certificate Of Currency Structure
  property_count: 10
  slug: api-connect-certificate-of-currency-structure
- name: Api Connect Email Sent Response Structure
  property_count: 3
  slug: api-connect-email-sent-response-structure
- name: Api Connect Lead Referral Request Structure
  property_count: 5
  slug: api-connect-lead-referral-request-structure
- name: Api Connect Lead Referral Response Structure
  property_count: 4
  slug: api-connect-lead-referral-response-structure
- name: Api Connect Policy Details Assisted Request Structure
  property_count: 3
  slug: api-connect-policy-details-assisted-request-structure
- name: Api Connect Policy Details Response Structure
  property_count: 6
  slug: api-connect-policy-details-response-structure
- name: Api Connect Policy Details Self Service Request Structure
  property_count: 2
  slug: api-connect-policy-details-self-service-request-structure
- name: Api Connect Price Estimate Assisted Request Structure
  property_count: 3
  slug: api-connect-price-estimate-assisted-request-structure
- name: Api Connect Price Estimate Email Request Structure
  property_count: 3
  slug: api-connect-price-estimate-email-request-structure
- name: Api Connect Price Estimate Response Structure
  property_count: 6
  slug: api-connect-price-estimate-response-structure
- name: Api Connect Price Estimate Self Service Request Structure
  property_count: 3
  slug: api-connect-price-estimate-self-service-request-structure
- name: Api Connect Price Estimate Summary Structure
  property_count: 7
  slug: api-connect-price-estimate-summary-structure
- name: Api Connect Rating Factor Structure
  property_count: 3
  slug: api-connect-rating-factor-structure
- name: Api Connect Rating Factors Response Structure
  property_count: 8
  slug: api-connect-rating-factors-response-structure
- name: Api Connect Self Service Estimate Response Structure
  property_count: 3
  slug: api-connect-self-service-estimate-response-structure
- name: Api Connect Self Service Session Response Structure
  property_count: 3
  slug: api-connect-self-service-session-response-structure
- name: Api Connect Vehicle Structure
  property_count: 4
  slug: api-connect-vehicle-structure
jsonld:
- class_count: 21
  name: Allianz Api Connect Context
  property_count: 48
  slug: allianz-api-connect-context
layout: provider
modified: '2026-06-20'
name: Allianz
nav: Providers
network: true
overview: 'Allianz publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Certificates API, Leads API, Policy Details API, and 1 more. Tagged areas include Financial Services, Insurance, and Asset Management.


  The Allianz catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Allianz''s developer surface includes authentication, support, engineering blog, and 9 more developer resources.'
random_paper: 62
rules:
- name: Allianz API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: allianz-docs-jsonschema-spectral-rules
- name: Allianz API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 9
  slug: allianz-docs-spectral-rules
scopes:
- name: Allianz Docs Scopes
  scope_count: 4
  slug: allianz-docs-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: thin
  composite: 41.1
  delta: -4.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 68.6
    developer_ergonomics: 17.4
    discoverability: 83.3
    governance: 80.2
    operational_transparency: 5.3
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 51.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allianz-docs/refs/heads/main/screenshots/allianz-docs-2026-07-25T195659.png
security:
- kind: authentication
  name: Allianz Docs Authentication
  slug: allianz-docs-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Allianz Docs Domain Security
  slug: allianz-docs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: allianz-docs
tags:
- Financial Services
- Insurance
- Asset Management
use_cases:
- description: Financial institutions and retailers embedding Allianz insurance offers at the point of sale within their own customer journey.
  name: Embedded Insurance
- description: Enterprise companies integrating Allianz trade credit and policy management directly into their ERP systems for automation.
  name: ERP Integration
- description: Insurance brokers building digital platforms that access Allianz products to offer customers real-time quotes and policy management.
  name: Broker Portals
- description: Automating claims reporting, status tracking, and management through API integration with enterprise workflow systems.
  name: Claims Automation
website: https://www.allianz.com/
---
